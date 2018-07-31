#!/bin/bash

TXT="cat test.lookup.txt"
F="/tmp/fails.txt"
# $TXT | hfst-lookup ckt.lexc.hfst | grep '>+?' | cut -f1 > $F
$TXT | hfst-lookup ckt.gen.hfst > "test.lookup.all"

# echo "Failed forms:"
#
# for i in `cat $F` ; do
#   echo $i ;
# done
