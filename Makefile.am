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
# 
# The lexc.hfst file will look like:
# ӈэвысӄэт<n><erg>:ӈ{Æ}высӄ{Æ}т>{T}{Æ}
#

$(LANG1).lexc: $(LANG1).rules.lexc
	cat $(LANG1).rules.lexc > $(LANG1).lexc
	cat lexicons/misc.lexc >> $(LANG1).lexc
	cat lexicons/nominals.lexc >> $(LANG1).lexc
	cat lexicons/nominalt.lexc >> $(LANG1).lexc
	cat lexicons/nominalu.lexc >> $(LANG1).lexc
	cat lexicons/nom_rules.lexc >> $(LANG1).lexc
	cat lexicons/pronouns.lexc >> $(LANG1).lexc
	cat lexicons/verb_deriv.lexc >> $(LANG1).lexc
	cat lexicons/verb_rules.lexc >> $(LANG1).lexc
	cat lexicons/verbs.lexc >> $(LANG1).lexc
	cat lexicons/verbt.lexc >> $(LANG1).lexc
	cat lexicons/verbu.lexc >> $(LANG1).lexc

$(LANG1).lexc.hfst: $(LANG1).lexc
	hfst-lexc --Werror $(LANG1).lexc -o $(LANG1).lexc.hfst

###############################################################################


## Compose the lexical transducer with the morphophonological rules
# 
# The lexctwol.hfst file will look like:
# 
#
$(LANG1).lexctwol.hfst: $(LANG1).lexc.hfst $(LANG1).twol.hfst
	hfst-compose-intersect -1 $(LANG1).lexc.hfst -2 $(LANG1).twol.hfst -o $(LANG1).lexctwol.hfst

# Invert the transducer ready for applying the morphotactic rules
#
# The lexctwol.mor.hfst file will look like:
#
#
$(LANG1).lexctwol.mor.hfst: $(LANG1).lexctwol.hfst
	hfst-invert $(LANG1).lexctwol.hfst -o $(LANG1).lexctwol.mor.hfst

# Apply the morphotactic rules to generate the final analyser
#
# The mor.hfst file will look like:
#
#
$(LANG1).mor.hfst: $(LANG1).lexctwol.mor.hfst $(LANG1).twoc.hfst
	hfst-compose-intersect -1 $(LANG1).lexctwol.mor.hfst -2 $(LANG1).twoc.hfst -o $(LANG1).mor.hfst

# Invert the transducer to generate the final generator
#
# The gen.hfst file will look like:
#
#
$(LANG1).gen.hfst: $(LANG1).mor.hfst
	hfst-invert $(LANG1).mor.hfst -o $(LANG1).gen.hfst

# Convert to optimised lookup format for faster lookup

$(LANG1).mor.hfstol: $(LANG1).mor.hfst
	hfst-fst2fst --format=optimized-lookup-weighted -i $(LANG1).mor.hfst -o $(LANG1).mor.hfstol

$(LANG1).gen.hfstol: $(LANG1).gen.hfst
	hfst-fst2fst --format=optimized-lookup-weighted -i $(LANG1).gen.hfst -o $(LANG1).gen.hfstol

###############################################################################

chkchndir=$(prefix)/share/chkchn
chkchn_DATA = $(TARGETS)

CLEANFILES = $(TARGETS)

###############################################################################
