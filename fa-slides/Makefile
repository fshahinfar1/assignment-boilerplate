OUTDIR = ./build/
default:
	mkdir -p $(OUTDIR)
	xelatex  -interaction=batchmode -output-directory=$(OUTDIR) solution.tex
	bibtex $(OUTDIR)/solution.aux

i:
	mkdir -p $(OUTDIR)
	xelatex  -output-directory=$(OUTDIR) solution.tex
	bibtex $(OUTDIR)/solution.aux

clean:
	rm -rf $(OUTDIR)
