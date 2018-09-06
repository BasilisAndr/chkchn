import re

with open('true_new.txt') as f:
    words = f.readlines()

verbs = []
adjs = []
nouns = []
advs = []
elses = []
for line in words:
    line = line.strip()
    if line.endswith('ть') or line.endswith('ти') or 'ться' in line or 'ть.' in line:
        line = line.split('\t')
        verbs.append('{0}к:{0} V ;\t\t\t! {1}'.format(line[0], line[-1]))
    elif 'ый' in line or 'ий' in line or 'ой' in line:
        line = line.split('\t')
        adjs.append('{0}:{0} ADJ ;\t\t\t! {1}'.format(line[0], line[-1]))
    elif line.endswith('а'):
        line = line.split('\t')
        nouns.append('{0}:{0} N ;\t\t\t! {1}'.format(line[0], line[-1]))
    elif line.endswith('е'):
        line = line.split('\t')
        advs.append('{0}:{0} ADV ;\t\t\t! {1}'.format(line[0], line[-1]))
    else:
        line = line.split('\t')
        elses.append('{0}:{0} ??? ;\t\t\t! {1}'.format(line[0], line[-1]))


with open('new.lexc', 'w') as f:
    for arr in [verbs, adjs, nouns, advs, elses]:
        f.write('\n'.join(arr))
        f.write('\n\n\n')
