LATEX=pdflatex
object=deck.tex

OUTDIR=./build/
FLAGS=-output-directory $(OUTDIR)

default: $(OUTDIR)
	$(LATEX) $(FLAGS) $(object)
	$(LATEX) $(FLAGS) $(object)

$(OUTDIR):
	mkdir -p $(OUTDIR)

