all:
	hfst-lexc ckt.lat_to_cyrl.lexc -o ckt.lat_to_cyrl.lexc.hfst
	hfst-twolc ckt.lat_to_cyrl.twol -o ckt.lat_to_cyrl.twol.hfst
	hfst-compose-intersect -1 ckt.lat_to_cyrl.lexc.hfst -2 ckt.lat_to_cyrl.twol.hfst -o ckt.lat_to_cyrl.hfst
	

# echo "ʔ:0 e:э {ʔ}:ʼ ɬ:ԓ ʔ:ъ e:э {ʔ}:0 ɬ:ԓ" | hfst-pair-test ckt.lat_to_cyrl.twol.hfst
# echo "ʔeɬʔeɬ" | hfst-strings2fst | hfst-compose -2 ckt.lat_to_cyrl.lexc.hfst | hfst-fst2strings
# echo "ʔeɬʔeɬ" | hfst-strings2fst | hfst-compose -2 ckt.lat_to_cyrl.hfst | hfst-fst2strings
