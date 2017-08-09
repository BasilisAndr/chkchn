#!/bin/bash

fails=cat test.lookup.txt | hfst-lookup ckt.gen.hfstol | grep '>+?'

echo "Failed forms:"

for i in fails ; do
  echo $i ;
done
