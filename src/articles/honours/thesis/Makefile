all: simulate.ps thesis.ps

all-gz: simulate.ps.gz thesis.ps.gz

all-pdf: thesis.pdf

clean:
	rm -f *.aux *.dvi *.log *~

simulate.ps: simulate.dvi
thesis.ps: thesis.dvi

simulate.dvi: simulate.tex simulate-flowchart.eps

thesis.dvi: thesis.tex intro.tex background.tex why-gap.tex user-desc.tex \
	implementation.tex conclusion.tex strauss.eps simulate-flowchart.eps \
	red-black.eps thesis.bib
thesis.pdf: thesis.tex intro.tex background.tex why-gap.tex user-desc.tex \
	implementation.tex conclusion.tex strauss.png simulate-flowchart.pdf \
	red-black.pdf


%.dvi: %.tex
	latex $<
	bibtex $*
	latex $<
	latex $<

%.pdf: %.tex
	pdflatex $<

%.ps: %.dvi
	dvips -o $@ $<

%.ps.gz: %.ps
	gzip --best -c $< > $@

%.eps: %.dia
	dia --export $@ $<

%.eps: %.png
	pngtopnm $< | pnmtops -noturn -nocenter > $@

%.pdf: %.eps
	epstopdf --outfile=$@ $<
