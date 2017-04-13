all: popytka.twol try.lexc ; hfst-compile-intersect -1 try.lexc -2 popytka.twol -o together.hfst
twolc: popytka.twol ; hfst-twolc popytka.twol -o popytka.hfst
lexc: try.lexc ; hfst-lexc try.lexc -o try.lexc.hfst
