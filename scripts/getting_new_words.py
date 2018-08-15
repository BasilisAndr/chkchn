import re, os

with open('ckt.lexc') as f:
    complete = f.read()

with open('true_new.txt') as f:
    new = f.readlines()

true_new = []
for n in new:
    m = re.search(n.split('\t')[-1].strip(), complete)
    if m:
        m = re.search(n.split('\t')[0].strip(), complete)
        if not m:
            true_new.append(n)
    elif not m:
        true_new.append(n)
print(len(true_new))
with open('true_new.txt', 'w') as f:
    f.write(''.join(true_new))


# with open('new_words.lexc') as f:
#     new = f.readlines()
#
# true_new = []
# for n in new:
#     m = re.search('\n{}:'.format(n.split('\t')[0].strip()), complete)
#     # if m:
#     #     m = re.search(n.split('\t')[0].strip(), complete)
#     #     if not m:
#     #         true_new.append(n)
#     if not m:
#         true_new.append(n)
# print(len(true_new))
# with open('true_new.txt', 'w') as f:
#     f.write(''.join(true_new))
