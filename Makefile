all: popytka.twol try.lexc ; hfst-twolc popytka.twol -o popytka.hfst ; hfst-lexc try.lexc -o try.lexc.hfst
twolc: popytka.twol ; hfst-twolc popytka.twol -o popytka.hfst
lexc: try.lexc ; hfst-lexc try.lexc -o try.lexc.hfst
