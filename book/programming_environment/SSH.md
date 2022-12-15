# SSH & SSHFS

- Author: *{{Fu}}*
- Update: *July 26, 2022*
- Reading: *15 min*

---


SSH (Secure Shell) is a network protocol that encrypts communication between two computers and supports various authentication mechanisms.

In practice, it is mainly used to ensure the security of remote login and remote communication. Any network service can be encrypted with this protocol.

## Basic usage

Use the `-V` parameter to check the version number

```bash
ssh -V
```

The following commands are used to log in to the server over `SSH`

```bash
ssh user@hostname
```

By default, `SSH` connects to port `22` of the server


```bash
ssh -p 22 -X user@hostname
```

- `-p`: specifies the server port that the SSH client connects to
 
- `-X`: opens the X window for forwarding (eg. X11)




## Create SSH keys

::::{margin} About Passphrase:
:::{toggle}
One of the questions is about **_"Enter passphrase (empty for no passphrase)"_**, and I chosse empty.
:::
::::

To create the keys, a preferred command is `ssh-keygen`. And `ssh-keygen` asks a series of questions and then writes **_a private key_** and **_a matching public key_**.

SSH keys are by default kept in the `~/.ssh` directory. If you do not have a `~/.ssh` directory, the `ssh-keygen` command creates it for you with the correct permissions. If an SSH key pair exists in the current location, those files are overwritten.




The following ssh-keygen command generates SSH RSA public and private key files by default in the `~/.ssh` directory.


```bash
ssh-keygen -t rsa -C "fy21@rice.edu"
```

- `ssh-keygen`: the program used to create the keys

- `-t rsa`: type of key to create, in this case in the RSA format

- `-C "fy21@rice.edu"`: a comment appended to the end of the public key file to easily identify it. Normally an email address is used as the comment, but use whatever works best for your infrastructure.

The `~/.ssh` directory has some personal key files and other files.

```bash
ls -l ~/.ssh
total 32
-rw-r--r--@ 1 yinfu  staff  1479 Jul 26 16:23 config
-rw-------  1 yinfu  staff  2602 Jul 20 22:53 id_rsa
-rw-r--r--  1 yinfu  staff   567 Jul 20 22:53 id_rsa.pub
-rw-------  1 yinfu  staff   749 Jul 20 23:02 known_hosts
```

- `config`: the configuration file
- `id_rsa`: the private key
- `id_rsa.pub`: the public key
- `known_hosts`: the public key's fingerprint of existing SSH servers


## Upload SSH keys

The user public key is stored in the `~/.ssh/authorized_keys` file on the server. Each public key occupies a line. If the file does not exist, you can manually create it. 

The permission of the `authorized_keys` file must be set to `644`, that is, only the file owner can write.


:::::{tab-set}
::::{tab-item} Manually Uploading a Public Key
User can edit the `authorized_keys` file manually and paste the public key into it, or can run the following command on the local computer.

```bash
cat ~/.ssh/id_rsa.pub | ssh user@host "mkdir -p ~/.ssh && cat >> ~/.ssh/authorized_keys"
chmod 644 ~/.ssh/authorized_keys
```
::::

::::{tab-item} ssh-copy-id
OpenSSH comes with the `ssh-copy-id` command to automatically copy the public key to the `~/. SSH /authorized_keys` file on the remote server. If the `~/.ssh/authorized_keys` file does not exist, the `ssh-copy-id` command automatically creates the file.
 

```bash
ssh-copy-id -i ~/.ssh/id_rsa.pub user@host
```
:::{note}
`ssh-copy-id` adds the public key directly to the end of the `authorized_keys` file. If the end of the `authorized_keys` file is not a newline character, the new public key will be added to the end of the previous public key, and the two public keys will be linked together, making neither of them valid. Therefore, if the `authorized_keys` file already exists, make sure that the `authorized_keys` file ends with a newline character before using the `ssh-copy-id` command (assuming the file already exists).
:::



::::
:::::




## Configure SSH config file

Some main configuration commands of the SSH config file

- `Host`: the alias name.
- `HostName`: specifies the domain name or IP address.
- `User`: specify the account name for remote login.
- `IdentityFile`: specifies the private key file.
- `Port`: indicates the SSH server Port that the specified client connects to.


My `~/.ssh/config` configuration file

::::{toggle}
```bash
#####################################
# Rice -- Prof. Jonathan's group in NOTS
#####################################
Host nots
  HostName nots.rice.edu
  ForwardX11Trusted yes
  ForwardX11 yes
  User fy21
  IdentityFile /Users/yinfu/.ssh/id_rsa
  Port 22


#####################################
# USTC -- Prof. Junlun Li's group
#####################################
Host li
  HostName 222.195.76.240
  ForwardX11Trusted yes
  ForwardX11 yes
  User yinfu
  IdentityFile /Users/yinfu/.ssh/id_rsa
  Port 22


#####################################
# USTC -- Prof. Baoshan Wang's group
#####################################
Host core
  HostName 222.195.74.184
  ForwardX11Trusted yes
  ForwardX11 yes
  User yinf
  IdentityFile /Users/yinfu/.ssh/id_rsa
  Port 1010

Host m1
  HostName 222.195.74.184
  ForwardX11Trusted yes
  ForwardX11 yes
  User yinf
  IdentityFile /Users/yinfu/.ssh/id_rsa
  Port 1011

Host m2
  HostName 222.195.74.184
  ForwardX11Trusted yes
  ForwardX11 yes
  User yinf
  IdentityFile /Users/yinfu/.ssh/id_rsa
  Port 1012

Host m3
  HostName 222.195.74.184
  ForwardX11Trusted yes
  ForwardX11 yes
  User yinf
  IdentityFile /Users/yinfu/.ssh/id_rsa
  Port 1013

Host m4
  HostName 222.195.74.184
  ForwardX11Trusted yes
  ForwardX11 yes
  User yinf
  IdentityFile /Users/yinfu/.ssh/id_rsa
  Port 1014

Host crust
  HostName 222.195.74.184
  ForwardX11Trusted yes
  ForwardX11 yes
  User yinf
  IdentityFile /Users/yinfu/.ssh/id_rsa
  Port 1015


########################################
# SUSTech -- Prof. Xiaofei Chen's group
########################################
Host seislab2
  HostName 10.20.11.42
  ForwardX11Trusted yes
  ForwardX11 yes
  User yinfu
  IdentityFile /Users/yinfu/.ssh/id_rsa
  Port 22

```
::::



## SSHFS

`SSHFS` is Secure Shell FileSystem, and it can mount a remote hard disk to the local Mac. `SSHFS` depends on `FUSE` on Mac, and the [macFUSE](https://osxfuse.github.io/) allows you to extend macOS's native file handling capabilities via third-party file systems.

- Download `macFUSE` firstly, click _macfuse-x.x.x.dmg_ to install.
- Download `SSHFS`, click the _X.dmg_ to install.


It can be used after the installation is complete, for example:

```bash
sshfs -o follow_symlinks -p 1012 yinf@222.195.74.184:/ /Users/yf/share1/
sshfs -o follow_symlinks fy21@nots.rice.edu:/ /Users/yinfu/share2/
```

## Reference

1. [地震"学"](https://seismo-learn.org/seismology101/best-practices/vscode/)
1. [Wang doc](https://wangdoc.com/ssh/key.html)
1. [Liam blog](https://liam.page/2017/09/12/rescue-your-life-with-SSH-config-file/)
1. [CSDN blog & sshfs](https://blog.csdn.net/SweetTool/article/details/72801265)
1. [Microsoft ssh manual](https://docs.microsoft.com/en-us/azure/virtual-machines/linux/create-ssh-keys-detailed)
