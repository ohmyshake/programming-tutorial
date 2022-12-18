# PROMISE Utility

My disk's version is `Pegasus32 R4`, refer to https://www.promise.com/Products/Pegasus/Pegasus32

Drivers can be downloaded via https://www.promise.com/Support/DownloadCenter/Pegasus/Pegasus32/R4#Drivers

Open the Terminal and type `promiseutil` and hit Return to log into the CLI
Force the drives back online with the following commands:



```bash
promiseutil
phydrv -a online -p1
phydrv -a online -p2
phydrv -a online -p3
phydrv -a online -p4
```

After forcing the PDs (Physical Disks) back online, the LEDs will turn back to blue and your volume should be accessible after forcing the (3) PDs back online.


Reference:
- https://forum.promise.com/thread/pegasus-r4-multiple-drive-failures/