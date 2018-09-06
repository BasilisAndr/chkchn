import re
from pprint import pprint


verbs = {}
links = {}

with open('corpora/Vdictionary.txt') as f:
    for line in f:
        per = re.findall('пер\.', line)
        if len(per) == 1:
            if 'См.' not in line:
                lemma = ''
                line_sp = line.lower().split('пер.')
                lemma_tmp = '{}пер.)'.format(line_sp[0])
                transitivity = lemma_tmp.split('(')[-1].strip(')')
                lemma_tmp = lemma_tmp.split('[')[0].split(',')[0].strip()
                if len(lemma_tmp.split()) == 1:
                    if lemma_tmp.endswith('к'):
                        lemma = lemma_tmp
                elif '(' in lemma_tmp:
                    if len(lemma_tmp.split('(')[0].split()) == 1 and lemma_tmp.split()[0].endswith('к'):
                        lemma = lemma_tmp.split()[0]
                elif '/' in lemma_tmp:
                    # print(lemma_tmp)
                    if lemma_tmp[1] == 'ы':
                        lemma = lemma_tmp.split()[0]
                        lemma = lemma[0] + '%{ы%}' + lemma[2:]
                    elif lemma_tmp[0] == 'р':
                        lemma = lemma_tmp.split()[0]
                        lemma = '%{R%}' + lemma[1:]
                    # else:
                        # print(lemma_tmp)
                if lemma:
                    if len(lemma.split()) > 1:
                        print(lemma)
                    try:
                        tr = line_sp[1].strip(' .2').split('. ')[2]
                        verbs[lemma] = ';'.join([transitivity, tr])
                    except:
                        try:
                            tr = line_sp[1].strip(' .2').split('? ')[2]
                            verbs[lemma] = ';'.join([transitivity, tr])
                        except:
                            print(line)
                            raise Exception
                    del lemma
                    # else:
                    #     print(lemma)
            else:
                links[line.split('См.')[0]] = line.split('См.')[1]
        elif len(per) == 2:
            if 'См.' not in line:
                line_sp = line.lower().split('пер.')
                lemma_one = '{}пер.)'.format(line_sp[0])
                lemma_two = '{}пер.)'.format(line_sp[1])
                transitivity = lemma_one.split('(')[-1].strip(')')
                lemma_one = lemma_one.split('[')[0].split(',')[0].strip()
                lemma_two = lemma_two.split('[')[0].split(',')[0].strip()
                if lemma_one.endswith('к'):
                    if len(lemma_one.split()) == 1:
                        try:
                            tr = line_sp[2].strip(' .2').split('. ')[2]
                            verbs[lemma_one] = ';'.join([transitivity, tr])
                            verbs[lemma_two] = ';'.join([transitivity, tr])
                        except:
                            try:
                                tr = line_sp[2].strip(' .2').split('? ')[2]
                                verbs[lemma_one] = ';'.join([transitivity, tr])
                                verbs[lemma_two] = ';'.join([transitivity, tr])
                            except:
                                print(line)
                                raise Exception

# pprint(verbs[:10])
print(len(verbs))

verbs_already = []
with open('ckt.lexc') as ff:
    for line in ff:
        if ' V ;' in line:
            verbs_already.append(line.split(':')[0])

not_yet = set(verbs.keys()) - set(verbs_already)
print(len(not_yet))

with open('lexicons/verbv.lexc', 'w') as fff:
    for verb in not_yet:
        if verbs[verb].split(';')[0] == 'пер.':
            trans = 'tv'
        else:
            trans = 'iv'
        try:
            if verb[-2] == 'ы':
                verb_sh = verb[:-2]
            else:
                verb_sh = verb[:-1]
        except:
            print(verb)
        fff.write('@U.V.{0}@{1}:@U.V.{0}@{2} V ;        ! {3}\n'.format(trans, verb, verb_sh, verbs[verb].split(';')[1]))
