file=lab2
make:
	latex $(file).tex
	latex $(file).tex
	dvips $(file).dvi -o
	ps2pdf13 $(file).ps
show:
	evince $(file).pdf
clean:
	rm *.dvi *.aux *.out *.log
