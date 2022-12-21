# Globus

- Author: *{{Fu}}*
- Update: *Dec 18, 2022*
- Reading: *60 min*

---





## Introduction

[Globus](https://www.globus.org/) is a secure, reliable **research data management** service. It works as a bridge between the remote endpoint and the local endpoint,  and it’s a better alternative tool for [rsync](https://rsync.samba.org/).


:::{admonition} What is the Globus?
With Globus, subscribers can move, share, publish & discover data via a single
interface, whether your files live on a supercomputer, lab cluster, tape archive,
public cloud or your laptop, you can manage this data from anywhere, using your
existing identities, via just a web browser.
:::


## Create Account

### Create Globus ID

Globus needs to know your identity.

- Signing in with your `Google` or `ORCiD ID` credentials, or if your `Organization` has been set up with Globus, showing in {numref}`globus-login`.

- Otherwise, create and sign into Globus using a `Globus ID`

- PS: if you are a student in Joanthan's group, just email Rice IT team to add `condo` from jonathan's storage into your `collection`.


```{figure} ./files/globus-login.jpg
---
scale: 50%
align: center
name: globus-login
---
Globus Login with `Google` or `ORCiD ID`
```


### Download Globus Connect Personal for Mac
Most users might try to transfer data between `cluster's endpoint` and `personal PC's endpoint`, so users need to create new personal endpoint which can be refered to the 
[tutorial](https://docs.globus.org/how-to/globus-connect-personal-mac/).

```{figure} ./files/globus-personal-app.jpg
---
scale: 50%
align: center
name: globus-personal-app
---
Globus Personal App
```

## Transfer Data

### 1. WebApp

- After logging in globus, you will get a webpage like {numref}`globus-webapp`, which is called as `Globus Web App`. 

- You can add different `collection` and mark them in `BOOKMARKS`, and choose the two panel mode for your two endpoints to transfer data between two PCs.

- After globus submits your work, you can find the mission process in `ACTIVITY` part.

```{figure} ./files/globus-webapp.jpg
---
scale: 40%
align: center
name: globus-webapp
---
Globus Web App
```




### 2. Shell Script
Sometimes you may have a lot of files (not a single file) to transfer, you need to write a script to do this work. [`globus-cli`](https://docs.globus.org/cli/) provides a `command-line-shell` tool to transfer data, and install it following the [open source code in github](https://github.com/globus/globus-cli):

```bash
pip install globus-cli
```

**Login:**

- When you login successfully, it will generate a file in `.globus/cli/storage.db`, which will remember your login info, avoiding the repeated login actions next time. 

```bash
globus login
```

```{figure} ./files/globus-cli-login.jpg
---
scale: 50%
align: center
name: globus-cli-login
---
Globus Login in Terminal
```

```{figure} ./files/globus-cli-login-code.jpg
---
scale: 40%
align: center
name: globus-cli-login-code
---
Globus Login in Terminal with Authorization Code
```


**Endpoint ID:**

- Approach-1: get Endpoint ID via `globus-cli`, take `Fu's M1-max` for example which is my personal endpoint name:

```bash
# get endpoint
globus endpoint search "Fu's M1-max"

# copy and paste the desired Endpoint ID from the search results
ep1=f34fbbd4-6708-11ed-8422-xxxxxxxxxx

# now we can use the endpoint in a human readable fashion
globus endpoint show $ep1
```

```{figure} ./files/globus-m1-endpoint.jpg
---
scale: 35%
align: center
name: globus-m1-endpoint
---
Globus M1-max Endpoint ID
```


- Approach-2: get Endpoint ID via `Globus Web App`, click the specified collections to show detailed info, then the `UUID` is the Endpoint ID:


```{figure} ./files/globus-m1-endpoint-app.jpg
---
scale: 35%
align: center
name: globus-m1-endpoint-app
---
Globus M1-max Endpoint ID in Globus Web App
```



**Filesystem Operations**

- Demonstrates the synchronous commands of `mkdir`, `rename`, and `ls`.

```bash
# Tutorial Endpoint ID found from 'globus endpoint search Tutorial'
$ ep1=ddb59aef-6d04-11e5-ba46-22000b92c6ec

# Make a new directory
$ globus mkdir $ep1:\~/cli_example_dir
The directory was created successfully

# Rename the directory
$ globus rename $ep1:\~/cli_example_dir $ep1:\~/cli_example_dir_renamed
File or directory renamed successfully

# Show the directory contents after the changes
# (assuming ~/ was empty before these commands)
$ globus ls $ep1:\~/
cli_example_dir_renamed/
```

**Single Item Transfers**

- Submits transfer requests for a file and a directory from one Globus Tutorial Endpoint to another

```bash
# Tutorial Endpoint IDs found from 'globus endpoint search Tutorial'
$ ep1=ddb59aef-6d04-11e5-ba46-22000b92c6ec
$ ep2=ddb59af0-6d04-11e5-ba46-22000b92c6ec

# transfer file1.txt from one endpoint to another
$ globus transfer $ep1:/share/godata/file1.txt $ep2:\~/file1.txt --label "CLI single file"
Message: The transfer has been accepted and a task has been created and queued for execution
Task ID: 466a5962-dda0-11e6-9d11-22000a1e3b52

# recursively transfer the godata folder from one endpoint to another
$ globus transfer $ep1:/share/godata $ep2:~/godata --recursive --label "CLI single folder"
Message: The transfer has been accepted and a task has been created and queued for execution
Task ID: 47477b62-dda0-11e6-9d11-22000a1e3b52
```

**Batch Transfers**

- Uses a `input.txt` file to request multiple files in one transfer request.

```bash
# this is the contents of in.txt:
# a list of source paths followed by destination paths

file1.txt file1.txt
file2.txt file2.txt # inline-comments are also allowed
file3.txt file3.txt
```

- Use `--batch` on `input.txt`

```bash
# Tutorial Endpoint IDs found from 'globus endpoint search Tutorial'
$ ep1=ddb59aef-6d04-11e5-ba46-22000b92c6ec
$ ep2=ddb59af0-6d04-11e5-ba46-22000b92c6ec

# pass `--batch` mode an input .txt file
# all paths from stdin are relative to the paths supplied here
$ globus transfer $ep1:/share/godata/ $ep2:~/ --label "CLI Batch" --batch input.txt
Message: The transfer has been accepted and a task has been created and queued for execution
Task ID: 306900e0-dda1-11e6-9d11-22000a1e3b52
```
:::{admonition} Only One Task?
Note that only one task was needed even though there are multiple files to be transferred.
:::


**[More example here](https://docs.globus.org/cli/examples/)**

### 3. Python Script
This SDK provides a convenient Pythonic interface to `Globus web APIs`, including the `Transfer API` and the Globus `Auth API` (tools for authenticating logins). Documentation for the APIs is available at https://docs.globus.org/api/, install it firstly:

```bash
pip install globus-sdk
```

There are some app-examples using the python SDK, https://github.com/globus/native-app-examples

```python


```



## Reference

- [Feng's blog](http://marscfeng.github.io/post/Fast-data-transfer-sync-using-globus/)

- [Globus Docs](https://docs.globus.org/)

