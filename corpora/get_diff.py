with open('corpus-stat-res-lower.txt') as f:
	less = f.readlines()
with open('corpus-stat-res.txt') as f:
        more = f.readlines()
diff = set(more)-set(less)
inverse = set(less)-set(more)
print('from more to less: {}'.format(len(diff)))
print('from less to more: {}'.format(len(inverse)))
with open('diff.txt', 'w') as f:
	f.write('\n'.join(sorted(diff)))
	f.write('\ninverse\n')
	f.write('\n'.join(sorted(inverse)))
