TEX = pdflatex
OUTDIR = ./build
FLAGS = -output-directory $(OUTDIR)
SRC = paper
BIB = bibtex

default:
	if [ ! -d $(OUTDIR) ]; then mkdir -p $(OUTDIR); fi
	$(TEX) $(FLAGS) $(SRC).tex
	$(BIB) $(OUTDIR)/$(SRC).aux
