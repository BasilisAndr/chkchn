#!/bin/sh
# http://wiki.apertium.org/wiki/Asturian#Calculating_coverage


# Example use:
# zcat corpa/en.crp.txt.gz | sh corpus-stat.sh


#CMD="cat corpa/en.crp.txt"
CMD="cat ../corpora/ckt.crp.txt"

F=../corpora/corpus-stat-res.txt
# for fil in `ls ../corpora/corporatxt`; do
#   echo "$fil";
#   $CMD="cat ../corpora/corporatxt/$fil";
#   $F="/tmp/$fil"
# Calculate the number of tokenised words in the corpus:
# for some reason putting the newline in directly doesn't work, so two seds
$CMD | apertium-destxt | hfst-proc ../ckt.mor.hfstol | apertium-retxt | sed 's/\$[^^]*\^/$^/g' | sed 's/\$\^/$\
^/g' > $F

# first=$CMD | apertium-destxt | hfst-lookup ckt.hfst
# echo first

NUMWORDS=`cat $F | wc -l`
echo "Number of tokenised words in the corpus: $NUMWORDS"



# Calculate the number of words that are not unknown

NUMKNOWNWORDS=`cat $F | grep -v '\*' | wc -l`
echo "Number of known words in the corpus: $NUMKNOWNWORDS"
echo "Top known words in the corpus:"
cat $F | grep -v '\*' | sort -f | uniq -c | sort -gr | head -10



# Calculate the coverage

COVERAGE=`calc "round($NUMKNOWNWORDS/$NUMWORDS*1000)/10"`
echo "Coverage: $COVERAGE %"

#If you don't have calc, change the above line to:
#COVERAGE=$(perl -e 'print int($ARGV[0]/$ARGV[1]*1000)/10;' $NUMKNOWNWORDS $NUMWORDS)

# Show the top-ten unknown words.

echo "Top unknown words in the corpus:"
cat $F | grep '\*' | sort -f | uniq -c | sort -gr | head -10
# done
# Update hitparade
cat $F | cut -f2 -d'^' | cut -f1 -d'/' | sort -f | uniq -c | sort -gr  > ../corpora/ckt.hitparade.txt
#
# Update glossed hitparade
bash hitparade.sh > ../corpora/hitparade.txt

# Update unknown list
cat ../corpora/hitparade.txt | grep '/\*[^0-9]' > ../corpora/unknown.txt
