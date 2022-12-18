# PROMISE Utility


## Introduction
- My disk's version is `Pegasus32 R4`, the product website is https://www.promise.com/Products/Pegasus/Pegasus32

- Resources (drivers, utilities, and manuals) can be downloaded via https://www.promise.com/Support/DownloadCenter/Pegasus/Pegasus32/R4#Drivers


## Dirvers


:::{admonition} A common problem is:  eject one of the drives in Pegasus R4 system when it is working, when plug it back in, it came up with a red light instead of blue, which will show as "Dead" in the Promise utility. How to recover it?

Open the Terminal and type `promiseutil`(based on `Pegasus32 Series Utility for Mac`), and hit Return to log into the CLI
Force the drives back online with the following commands:


```bash
# open `cliib` mode
promiseutil

# input in `cliib` mode
phydrv -a online -p1
phydrv -a online -p2
phydrv -a online -p3
phydrv -a online -p4
```

After forcing the PDs (Physical Disks) back online, the LEDs will turn back to blue and your volume should be accessible after forcing the (3) PDs back online.

**Reference with same problem:**
- https://forum.promise.com/thread/r4-array-bad/
- https://forum.promise.com/thread/pegasus-r4-multiple-drive-failures/
:::

