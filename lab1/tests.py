from reversed import reversed_index
from forward import forward_index

r_i = reversed_index(['sample1.txt', 'sample2.txt', 'sample3.txt'])

assert len(r_i['I']) == 2
assert 'sample1.txt' in r_i['I']
assert 'sample2.txt' in r_i['I']

assert len(r_i['kill']) == 1
assert 'sample3.txt' in r_i['kill']

f_i = forward_index(['sample1.txt', 'sample2.txt', 'sample3.txt'])

assert len(f_i['sample1.txt']) > 10
assert 'I' in f_i['sample1.txt']
assert 'I' in f_i['sample2.txt']

assert len(f_i['sample3.txt']) >30
assert 'kill' in f_i['sample3.txt']