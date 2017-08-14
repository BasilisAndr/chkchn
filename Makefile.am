###############################################################################

LANG1=ckt

TARGETS=$(LANG1).mor.hfstol  $(LANG1).gen.hfstol $(LANG1).mor.hfst $(LANG1).gen.hfst

###############################################################################

## Compile the morphotactic constraints

$(LANG1).twoc.hfst: $(LANG1).twoc
	hfst-twolc $(LANG1).twoc -o $(LANG1).twoc.hfst

## Compile the morphophonological constraints

$(LANG1).twol.hfst: $(LANG1).twol
	hfst-twolc $(LANG1).twol -o $(LANG1).twol.hfst

## Compile the lexicon

$(LANG1).lexc: $(LANG1).rules.lexc
	cat $(LANG1).rules.lexc > $(LANG1).lexc
	for i in `ls lexicons/` ; do \
	cat $(join "lexicons/", $$i) >> $(LANG1).lexc ; \
	done

$(LANG1).lexc.hfst: $(LANG1).lexc
	hfst-lexc --Werror $(LANG1).lexc -o $(LANG1).lexc.hfst

###############################################################################

$(LANG1).gen.hfst: $(LANG1).mor.hfst
	hfst-invert $(LANG1).mor.hfst -o $(LANG1).gen.hfst


$(LANG1).lexctwol.hfst: $(LANG1).lexc.hfst $(LANG1).twol.hfst
	hfst-compose-intersect -1 $(LANG1).lexc.hfst -2 $(LANG1).twol.hfst -o $(LANG1).lexctwol.hfst

$(LANG1).mor.hfst: $(LANG1).lexctwol.mor.hfst $(LANG1).twoc.hfst
	hfst-compose-intersect -1 $(LANG1).lexctwol.mor.hfst -2 $(LANG1).twoc.hfst -o $(LANG1).mor.hfst

$(LANG1).lexctwol.mor.hfst: $(LANG1).lexctwol.hfst
	hfst-invert $(LANG1).lexctwol.hfst -o $(LANG1).lexctwol.mor.hfst

$(LANG1).mor.hfstol: $(LANG1).mor.hfst
	hfst-fst2fst --format=optimized-lookup-weighted -i $(LANG1).mor.hfst -o $(LANG1).mor.hfstol

$(LANG1).gen.hfstol: $(LANG1).gen.hfst
	hfst-fst2fst --format=optimized-lookup-weighted -i $(LANG1).gen.hfst -o $(LANG1).gen.hfstol

###############################################################################

chkchndir=$(prefix)/share/chkchn
chkchn_DATA = $(TARGETS)

CLEANFILES = $(TARGETS)

###############################################################################
