#!/bin/bash

TXT="cat test.lookup.txt"
F="/tmp/fails.txt"
$TXT | hfst-lookup ckt.gen.hfstol | grep '>+?' | cut -f1 > $F

echo "Failed forms:"

for i in `cat $F` ; do
  echo $i ;
done
