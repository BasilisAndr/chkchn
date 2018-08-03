import re


files = ['intr.txt', 'tr.txt']
verb_files = ['lexicons/verbs.lexc', 'lexicons/verbt.lexc', 'lexicons/verbu.lexc']

file = files[0]
with open(file) as f:
    verbs = set(x.strip().lower() for x in f.readlines())
file = files[1]
with open(file) as f:
    t_verbs = set(x.strip().lower() for x in f.readlines())

flag = 'IV'
print('вак' in verbs)
verbs = verbs - t_verbs
print(flag)
print(len(verbs))
for v_fil in verb_files:
    with open(v_fil) as f:
        with open('{}_new'.format(v_fil), 'w') as ff:
            for line in f:
                if line.split(':')[0] in verbs:
                    line = re.sub('V ;', 'V-{} ;'.format(flag), line)
                    if line.split(':')[0] == 'вак':
                        print(line)
                ff.write(line)

t_verbs = t_verbs - verbs
flag = 'TV'
print(flag)
print(len(t_verbs))
for v_fil in verb_files:
    with open('{}_new'.format(v_fil)) as f:
        with open('{}_new_new'.format(v_fil), 'w') as ff:
            for line in f:
                if line.split(':')[0] in t_verbs:
                    if line.split(':')[0] == 'вак':
                        print('here!')
                    line = re.sub('V ;', 'V-{} ;'.format(flag), line)
                ff.write(line)

print('вак' in verbs)
print(verbs&t_verbs)
