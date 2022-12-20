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


***Endpoint ID:**

```bash
globus endpoint search "Fu's M1-max"
```



### 3. Python Script

```bash
pip install globus-sdk
```

## Reference

- [Feng's blog](http://marscfeng.github.io/post/Fast-data-transfer-sync-using-globus/)



