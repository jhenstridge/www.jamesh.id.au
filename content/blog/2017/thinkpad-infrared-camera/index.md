---
title: 'ThinkPad Infrared Camera'
slug: thinkpad-infrared-camera
date: 2017-10-22T14:20:39+08:00
tags: ['GStreamer', 'Linux', 'ThinkPad', 'Ubuntu']
---

One of the options available when configuring the my ThinkPad was an
Infrared camera. The main selling point being [\"Windows
Hello\"](https://docs.microsoft.com/en-us/windows-hardware/design/device-experiences/windows-hello-face-authentication)
facial recognition based login. While I wasn\'t planning on keeping
Windows on the system, I was curious to see what I could do with it
under Linux. Hopefully this is of use to anyone else trying to get it to
work.

The camera is manufactured by Chicony Electronics (probably a
[CKFGE03](http://www.chicony.com.tw/products_detail.php?id=QCUlXiQjMTA5QCUlXiQj)
or similar), and shows up as two USB devices:

    04f2:b5ce Integrated Camera
    04f2:b5cf Integrated IR Camera

Both devices are bound by the `uvcvideo` driver, showing up as separate
video4linux devices. Interestingly, the IR camera seems to be assigned
`/dev/video0`, so generally gets picked by apps in preference to the
colour camera. Unfortunately, the image it produces comes up garbled:

{{< figure src="2017-10-22-105539.jpg" >}}

So it wasn\'t going to be quite so easy to get things working. Looking
at the advertised capture modes, the camera supports Motion-JPEG and
YUYV raw mode. So I tried capturing a few JPEG frames with the following
GStreamer pipeline:

    gst-launch-1.0 v4l2src device=/dev/video0 num-buffers=10 ! image/jpeg ! multifilesink location="frame-%02d.jpg"

Unlike in raw mode, the red illumination LEDs started flashing when in
JPEG mode, which resulted in frames having alternating exposures.
Here\'s one of the better exposures:

{{< figure src="frame-04.jpg" >}}

What is interesting is that the JPEG frames have a different aspect
ratio to the raw version: a more normal 640x480 rather than 400x480. So
to start, I captured a few raw frames:

    gst-launch-1.0 v4l2src device=/dev/video0 num-buffers=10 ! "video/x-raw,format=(string)YUY2" ! multifilesink location="frame-%02d.raw"

The illumination LEDs stayed on constantly while recording in raw mode.
The contents of the raw frames show something strange:

    00000000  11 48 30 c1 04 13 44 20  81 04 13 4c 20 41 04 13  |.H0...D ...L A..|
    00000010  40 10 41 04 11 40 10 81  04 11 44 00 81 04 12 40  |@.A..@....D....@|
    00000020  00 c1 04 11 50 10 81 04  12 4c 10 81 03 11 44 00  |....P....L....D.|
    00000030  41 04 10 48 30 01 04 11  40 10 01 04 11 40 10 81  |A..H0...@....@..|
    ...

The advertised YUYV format encodes two pixels in four bytes, so you
would expect any repeating patterns to occur at a period of four bytes.
But the data in these frames seems to repeat at a period of five bytes.

Looking closer it is actually repeating at a period of 10 bits, or four
packed values for every five bytes. Furthermore, the 800 byte rows work
out to 640 pixels when interpreted as packed 10 bit values (rather than
the advertised 400 pixels), which matches the dimensions of the JPEG
mode.

The following Python code can unpack the 10-bit pixel values:

    def unpack(data):
        result = []
        for i in range(0, len(data), 5):
            block = (data[i] |
                     data[i+1] << 8 |
                     data[i+2] << 16 |
                     data[i+3] << 24 |
                     data[i+4] << 32)
            result.append((block >> 0) & 0x3ff)
            result.append((block >> 10) & 0x3ff)
            result.append((block >> 20) & 0x3ff)
            result.append((block >> 30) & 0x3ff)
        return result

After adjusting the brightness while converting to 8-bit greyscale, I
get a usable image. Compare a fake YUYV frame with the decoded version:

{{< figure src="test-05-yuv.jpg" >}}
{{< figure src="test-05-norm.jpg" >}}

I suppose this logic could be wrapped up in a GStreamer element to get
usable infrared video capture.

I\'m still not clear why the camera would lie about the pixel format it
produces. My best guess is that they wanted to use the standard USB
Video Class driver on Windows, and this let them get at the raw data to
process in user space.

---
### Comments:
#### L - <time datetime="2017-12-20 18:46:50">20 Dec, 2017</time>

Hey,=\
this is very interesting, I was wondering about this too - I am now
using Ubuntu on Thinkpad P51s!

Did you figure out how to tell apps to use the actual webcam instead of
the IR?\
Are you considering coding something up to make use of the IR?

Best,\
L

---
#### [Tomáš Janoušek](http://work.lisk.in/) - <time datetime="2018-01-03 10:34:19">3 Jan, 2018</time>

Hi, thanks for the post! I was also interested in this but didn\'t get
to it yet.

My ThinkPad has two IR cameras so that Windows Hello can take a stereo
picture. It seems that we only get images from one of them. Or can we
perhaps interpret the raw image as two 5-bit images?

---
