# all: ckt.lexc ckt.twol ;
# 	hfst-lexc ckt.lexc -o ckt.lexc.hfst ;
# 	hfst-twolc ckt.twol -o ckt.twol.hfst ;
# 	hfst-compose-intersect -1 ckt.lexc.hfst -2 ckt.twol.hfst -o ckt.hfst
all: ckt.rules.lexc ckt.twol ;
	cat ckt.rules.lexc > ckt.lexc
	for i in `ls lexicons/` ; do \
	cat $(join "lexicons/", $$i) >> ckt.lexc ; \
	done
	hfst-lexc --Werror ckt.lexc -o ckt.lexc.hfst ;
	hfst-twolc ckt.twoc -o ckt.twoc.hfst ;
	hfst-twolc ckt.twol -o ckt.twol.hfst ;
	hfst-compose-intersect -1 ckt.lexc.hfst -2 ckt.twoc.hfst -o ckt.lexctwoc.hfst
	hfst-compose-intersect -1 ckt.lexctwoc.hfst -2 ckt.twol.hfst -o ckt.gen.hfst
	hfst-invert ckt.gen.hfst -o ckt.mor.hfst
	hfst-fst2fst --format=optimized-lookup-weighted -i ckt.mor.hfst -o ckt.mor.hfstol
	hfst-fst2fst --format=optimized-lookup-weighted -i ckt.gen.hfst -o ckt.gen.hfstol
twolc: ckt.twol ; hfst-twolc ckt.twol -o ckt.twol.hfst
lexc: ckt.rules.lexc ;
	cat ckt.rules.lexc > ckt.lexc
	for i in `ls lexicons/` ; do \
	cat $(join "lexicons/", $$i) >> ckt.lexc ; \
	done
	hfst-lexc --Werror ckt.lexc -o ckt.lexc.hfst
	hfst-twolc ckt.twoc -o ckt.twoc.hfst ;
	hfst-compose-intersect -1 ckt.lexc.hfst -2 ckt.twoc.hfst -o ckt.lexctwoc.hfst
final: ckt.lexctwoc.hfst ckt.twol.hfst ;
	hfst-compose-intersect -1 ckt.lexctwoc.hfst -2 ckt.twol.hfst -o ckt.gen.hfst
	hfst-invert ckt.gen.hfst -o ckt.mor.hfst
	hfst-fst2fst --format=optimized-lookup-weighted -i ckt.mor.hfst -o ckt.mor.hfstol
	hfst-fst2fst --format=optimized-lookup-weighted -i ckt.gen.hfst -o ckt.gen.hfstol
