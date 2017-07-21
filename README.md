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

The files in .hfstol format are the faster versions of .hfst.


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

make_and_count.sh compiles the transducer and counts the coverage; it's a composition of `make` and `scripts/corpus-stat-res.sh`

### Coverage
69.8%
