
show: talk.mgp strauss-eqn.eps
	mgp -g 800x600 talk.mgp

.PHONY: show

%.dvi: %.tex
	latex $<
%.eps: %.dvi
	dvips -o $@ -E $<
