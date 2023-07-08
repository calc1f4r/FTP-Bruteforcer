### ⚔ Description

#### 🔥 Asynchronous FTP Bruteforcer

This is a Python script that implements an asynchronous FTP (File Transfer Protocol) bruteforcer. It utilizes asynchronous programming techniques to efficiently perform password guessing attacks on FTP servers.

The FTP Bruteforcer is designed to automate the process of attempting various usernames and passwords combinations to gain unauthorized access to an FTP server. It takes advantage of the aioftp library, which provides an asynchronous FTP client implementation.

Key Features:

- **Asynchronous execution**: The script leverages asyncio to achieve high concurrency and efficiency, allowing multiple login attempts to be performed simultaneously.
- **Command-line interface**: The script accepts command-line arguments such as the target hostname, port, username, and wordlist file to customize the attack.
- **Password guessing**: It reads a wordlist file containing potential passwords and iterates through each password, attempting to log in to the FTP server.

This is the modern approach to doing this type of thing as it uses minimal resources.

**Usage**
To use the FTP Bruteforcer, you need to have Python 3.x installed. Additionally, you'll need to install the required dependencies, which can be done using the following command:

```shell
pip install aioftp termcolor asyncio argparse
```

Once the dependencies are installed, you can run the script from the command line, providing the necessary arguments:

```shell
python ftp_bruteforcer.py <target> -p <port> -u <username> -w <wordlist>
```

Once the dependencies are installed, you can run the script from the command line, providing the necessary arguments:

```shell
python ftp_bruteforcer.py <target> -p <port> -u <username> -w <wordlist>
```

> Will Suggest using this script, as this uses fewer resources and works better than the other one.

**Tutorial:**


https://github.com/calc1f4r/FTP-Bruteforcer/assets/74751675/a2a81ec4-594a-41c5-8b2f-ad2d84c8c594


### 🔥 Multithreaded SSH and FTP Bruteforcer

This Python script is a multithreaded SSH and FTP bruteforcer. It allows for simultaneous password-guessing attempts on SSH and FTP servers using multiple threads, increasing the efficiency and speed of the brute-forcing process. The script utilizes the paramiko library for SSH connections and the ftplib library for FTP connections.

The Multithreaded SSH and FTP Bruteforcer script automate the process of attempting different username and password combinations to gain unauthorized access to SSH and FTP servers. It takes advantage of multithreading to perform concurrent brute-force attempts, significantly reducing the time required for the attack.

Key Features:

- **Support for SSH and FTP**: The script can perform brute-force attacks on both SSH and FTP servers, based on the user's choice.
- **Multithreaded execution**: The script uses multiple threads to perform simultaneous login attempts, increasing the speed of the brute-forcing process.
- **Command-line interface**: The script accepts command-line arguments such as the target hostname, port, username, wordlist file, and the number of threads to use.

**Usage**

To use the Multithreaded SSH and FTP Bruteforcer, you need to have Python 3.x installed. Additionally, you'll need to install the required dependencies, which can be done using the following command:

```shell
pip install paramiko termcolor argparse ftplib
```

Once the dependencies are installed, you can run the script from the command line, providing the necessary arguments:

```shell
python multithread-ssh-and-Ftp-Bruteforcer.py <target> -p <port> -w <wordlist> -u <username> -t <thread> <-ssh|-ftp>
```

- <target>: The hostname or IP address of the SSH or FTP server you want to attack.
- -p <port> (optional): The port number to use for the SSH or FTP connection. The default is 22 for SSH and 21 for FTP if not specified.
- -w <wordlist>: The path to a file containing a list of potential passwords. Each password should be on a separate line in the file.
- -u <username>: The username to use for the brute-forcing attempts.
- -t <threads> (optional): The number of threads to use for concurrent brute-forcing attempts. The default is 4 if not specified. It supports up to 8 threads.
- -ssh or -ftp: Specify either -ssh for SSH bruteforcing or -ftp for FTP bruteforcing.

**Example:**

```python
multithread-ssh-and-Ftp-Bruteforcer.py 10.10.10.10 -p 22 -w passwords.txt -u admin -t 6 -ssh```
```
