# Chukchi morphological parser

### Description

This is a Google Summer of Code project for a morphological analyzer (autoglosser) for Chukchi based on HFST.<br />
The full transducer is composed of three transducers:<br />
- lexc deals with morphology and lexicon;
- twoc helps to implement morphology that is not possible (or too difficult) to implement in lexc;
- twol deals with phonology and morphophonology.

Compilation produces the before mentioned transducers plus two composed ones:
- ckt.mor.hfst is the transducer for morphological analysis;
- ckt.gen.hfst is the one for forms generation.

The files in .hfstol format are faster versions of .hfst.

### Compilation

| make       | for |
|------------|-----------------------------------------------------|
| make       | to compile twol & lexc files in a single transducer |
| make twolc | to compile twolc only                               |
| make lexc  | to compile lexc only                                |
| make final | to compose existing transducers into a single one   |

### Testing

test.sh is a hfst-pair-test for twolc. The input file for the positive test is test.test.<br />
alltest.sh is a hfst-lookup for the whole transducer.<br />

### Usage

##### by token
If you need to analyze a token, use this command:
$ echo "" | hfst-lookup ckt.mor.hfst
To generate a form from a succession of tags, use this command:
echo "root<tag1><tag2>" | hfst-lookup ckt.gen.hfst

##### whole text
This requires a bit more preparation. Go to scripts/corpus-stat.sh and change this line:
CMD="cat ../corpora/ckt.crp.txt"
according to the location of your text. The file with the text should be in .txt format.
Then run corpus-stat.sh.
The output of the script (e.g. analyzed tokens) will be in the file corpora/corpus-stat-res.txt. If you want to change location of the output, change this line in scripts/corpus-stat.sh:
F=../corpora/corpus-stat-res.txt


### Coverage
76.2%
