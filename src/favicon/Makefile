
favicon.ico: 16.png 32.png 48.png 256.png
	convert $^ $@

%.png: favicon.svg
	inkscape -w $* -h $* -o $@ $<
	optipng -o7 $@
