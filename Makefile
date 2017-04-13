all: popytka.twol try.lexc ;
	hfst-twolc popytka.twol -o popytka.hfst ;
	hfst-lexc try.lexc -o try.lexc.hfst ;
	hfst-compose-intersect -1 try.lexc.hfst -2 popytka.hfst -o together.hfst
twolc: popytka.twol ; hfst-twolc popytka.twol -o popytka.hfst
lexc: try.lexc ; hfst-lexc try.lexc -o try.lexc.hfst
final: try.lexc.hfst popytka.hfst ;
	hfst-compose-intersect -1 try.lexc.hfst -2 popytka.hfst -o together.hfst
