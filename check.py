with open('paste2') as f:
    ques = {line.split('^')[2].split('/')[0]:line.split('^')[2].split('/')[1:]  for line in f}

check = {}
with open('corpora/corpus-stat-res.txt') as f:
    for line in f:
        try:
            check[line.strip('^').split('/')[0]] = line.strip('^').split('/')[1]
        except:
            pass
    # check = {line.strip('^').split('/')[0]: line.strip('^').split('/')[1] for line in f}

count = 0
for q in ques:
    if '*' in check[q]:
        count += 1
        print(q, '/'.join(ques[q]), sep='/')
print(count)
