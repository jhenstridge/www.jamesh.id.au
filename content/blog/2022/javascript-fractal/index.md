---
title: "Improved JS Mandelbrot Renderer"
date: 2022-09-01T13:27:17+08:00
tags: ['JavaScript']
---

[Eleven years ago](../../2011/javascript-fractal/index.md), I wrote a
Mandelbrot set generator in JavaScript as a way to test out the then
somewhat new [Web Workers
API](https://developer.mozilla.org/en-US/docs/Web/API/Web_Workers_API),
allowing me to make use of multiple cores and not tie up the UI thread
with the calculations.

Recently I decided to see how much I could improve it with
improvements to the web stack that have happened since then. The
result was much faster than what I'd managed previously:

<iframe src="{{< resource-ref "mandelbrot.html" >}}"
  width="640" height="480" class="mw-100" allowfullscreen></iframe>

The main improvements came from the use of [typed
arrays](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Typed_arrays). As
well as the memory savings compared to regular JS arrays that can
contain arbitrary values, it enabled the following improvements:

1. It's possible for two arrays to share the same backing buffer, even
   if they have different types. So while image data is exposed as
   byte arrays with four entries per pixel (the RGBA components), we
   can create a `uint32` array view of the same data with one entry
   per pixel.

2. Array buffers can be transferred when posting messages to/from
   workers. This basically lets us move blocks of memory between
   threads rather than having to copy them.

3. It's now possible to construct new `ImageData` objects from
   existing arrays. So we can use arrays transferred from workers as
   image data directly, removing another set of copies.

I also switched the workers over to rendering 128x128 tiles rather
than single rows. This means the memory buffers don't have to change
when the window is resized. In fact, I can allocate one buffer per
worker up front, and just transfer it back and forward to avoid more
allocations.

It renders nice and fast on my 16 hyperthread desktop system, and also
performs decently on the Android devices I have.

Another improvement I added is a simple a toolbar to allow panning
around the image, zooming out as well as in, resetting the viewport
and switching to fullscreen.

I've published the code in a git repo here:

<https://github.com/jhenstridge/jsfractal>
