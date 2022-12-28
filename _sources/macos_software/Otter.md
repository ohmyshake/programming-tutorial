# Otter



## Otter



How to perform real-time transcription of meeting and video content?
I use `AirPods` + `Otter` + `Loopback` + `BlackHole-2ch`.

:::{dropdown} Do you know **Loopback** and **BlackHole-2ch**?
:color: info
:icon: info
**BlackHole** is a virtual audio device that converts audio output into audio input. BlackHole redirect sounds an app plays on BlackHole to another app using BlackHole as input.

**Loopback** is an audio routing software that can take multiple audio output streams, mix them, and split them into multiple output streams. It works as a virtual audio device as well as BlackHole.

More info can be found in https://blog.tai2.net/how-to-use-otter-en.html
:::

1. Firstly install `BlackHole-2ch` using `brew`, and the github repository is [here.](https://github.com/ExistentialAudio/BlackHole)

    ```bash
    brew install blackhole-2ch
    ```


2. Download `Loopback` software. You can download it from its official [website](https://rogueamoeba.com/loopback/) or other ways.


3. Set sound environment in your Macbook as following:

```{figure} ./files/otter.jpg
---
scale: 40%
align: center
name: otter
---
My `Loopback` setting
```

```{figure} ./files/input.jpg
---
scale: 30%
align: center
name: otter_input
---
My `Sound` input setting
```

```{figure} ./files/output.jpg
---
scale: 30%
align: center
name: otter_output
---
My `Sound` output setting
```


Now if you use `Zoom`, you need set Microphones same as system as following:

```{figure} ./files/zoom.jpg
---
scale: 60%
align: center
name: otter_zoom
---
My `Zoom` setting
```

If you want view video from webpage or local, the above setting also can work. 
It is worth mentioning that if you use `Chrome`, you can use `Live Caption` function
provided by Chrome itself.
