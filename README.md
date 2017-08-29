# Chukchi morphological parser

### Description

This is a Google Summer of Code project for a morphological analyzer (autoglosser) for Chukchi based on Helsinki Finite State Transducers (HFST).<br />

#### Chukchi
Chukchi is a language with rich morphology, both inflexional and derivational, and a language with vowel harmony. Vowel harmony is a linguistic phenomenon when vowels are grouped and only vowels from the same group can occur in one word (e.g. Turkic languages). That means, (almost) all vowels in a word can change if a certain affix is attached. </br>
Chukchi also has quite a lot of morphophonology, which is expressed via mutations of letters in some contexts. This is further complicated by Chukchi orthography, which in some cases doesn't reflect the order of the sounds adequately. </br>
Morphological parsers that have been used for Chukchi by now (e.g. regexp-based) cannot natively and easily account for all these complications. That is why HFST technology was chosen in this project.

#### This transducer
The full transducer is composed of three transducers:<br />
- lexc deals with morphology and lexicon;
- twoc helps to implement morphology that is not possible (or too difficult) to implement in lexc;
- twol deals with phonology and morphophonology.

Compilation produces the before mentioned transducers plus two composed ones:
- ckt.mor.hfst is the transducer for morphological analysis;
- ckt.gen.hfst is the one for forms generation.

The files in .hfstol format are faster versions of .hfst.

The last GSoC commit is [here](https://github.com/BasilisAndr/chkchn/commit/2aef3a1bdb8f8b0c3ab40629dd4851a9d763aae6).

### Compilation

| command       | result |
|------------|------------------------------------------------------|
| make       | to compile twolc & lexc files in a single transducer |
| make twolc | to compile twolc only                                |
| make lexc  | to compile lexc only                                 |
| make final | to compose existing transducers into a single one    |

Compilation + coverage count is done by ./make_and_count.sh script.

### Testing

test.sh is a hfst-pair-test for twolc. The input file for the positive test is test.test.<br />
alltest.sh is a hfst-lookup test for the whole transducer.<br />

### Usage

#### by token
If you need to analyze a token, use this command:
$ echo "token" | hfst-lookup ckt.mor.hfst
To generate a form from a succession of tags, use this command:
echo "root\<tag1\>\<tag2\>" | hfst-lookup ckt.gen.hfst

#### whole text
This requires a bit more preparation. Go to scripts/corpus-stat.sh and change this line:
CMD="cat ../corpora/ckt.crp.txt"
according to the location of your text. The file with the text should be in .txt format.
Then run corpus-stat.sh.
The output of the script (e.g. analyzed tokens) will be in the file corpora/corpus-stat-res.txt. If you want to change location of the output, change this line in scripts/corpus-stat.sh:
F=../corpora/corpus-stat-res.txt


### Results
#### Coverage

Coverage (percentage of tokens analyzed) is calculated over the corpora/ckt.crp.txt file, which is a compilation of Chukchi fairytales.

Current state: 76.2%

#### Paradigms
Current state of this parser accounts for:
- all of morphophonology and orthography issues;
- nominal, pronominal, adjectival inflection and derivation;
- uniflexionable parts of speech;
- verbal inflection except certain future paradigm cells;
- verbal derivation.

It also contains structures to parse compounds and incorporation, but they burst the complexity of the transducer and it was impossible to test them on the capacities availiable.

### Further work
- Refactoring for better and quicker performance;
- Fix future;
- Incorporation on refactored transducer;
- Dictionary enlargement.
