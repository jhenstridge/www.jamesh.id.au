
all: ../content/talks/lca2003/talk.pdf \
     ../content/talks/guadec2001/python.pdf \
     ../content/talks/guadec2002/python.pdf

.PHONY: all

../content/%.pdf: %.mgp
	mgp2ps -c -m -p a4 $< | ps2pdf -sPAPERSIZE=a4 -dFastWebView=true - $@
