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
[Download Globus Connect Personal for Mac](https://docs.globus.org/how-to/globus-connect-personal-mac/)



## Transfer Data

### 1. WebGUI



### 2. Shell Script


```bash
pip install globus-cli
```

### 3. Python Script

```bash
pip install globus-sdk
```

## Reference

- [Feng's blog](http://marscfeng.github.io/post/Fast-data-transfer-sync-using-globus/)



