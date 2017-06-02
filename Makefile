# all: ckt.lexc ckt.twol ;
# 	hfst-lexc ckt.lexc -o ckt.lexc.hfst ;
# 	hfst-twolc ckt.twol -o ckt.twol.hfst ;
# 	hfst-compose-intersect -1 ckt.lexc.hfst -2 ckt.twol.hfst -o ckt.hfst
all: ckt.rules.lexc ckt.twol ;
	cat ckt.rules.lexc > ckt.lexc
	for i in `ls lexicons/` ; do \
	cat $(join "lexicons/", $$i) >> ckt.lexc ; \
	done
	hfst-lexc ckt.lexc -o ckt.lexc.hfst ;
	hfst-twolc ckt.twol -o ckt.twol.hfst ;
	hfst-compose-intersect -1 ckt.lexc.hfst -2 ckt.twol.hfst -o ckt.hfst
twolc: ckt.twol ; hfst-twolc ckt.twol -o ckt.twol.hfst
lexc: ckt.lexc ; hfst-lexc ckt.lexc -o ckt.lexc.hfst
final: ckt.lexc.hfst ckt.twol.hfst ;
	hfst-compose-intersect -1 ckt.lexc.hfst -2 ckt.twol.hfst -o ckt.hfst
