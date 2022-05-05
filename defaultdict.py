
import random
import string
n = 100
val_str = ''.join([random.choice(string.ascii_lowercase) for i in range(n)])
print(val_str)
d = {}

for key in val_str:
    if key not in d:

        d[key] = 0
    d[key] += 1
print(d)

from collections import defaultdict
d = defaultdict(int)

for key in val_str:
    d[key] += 1

print(d)
print(d['i'])
#d = defaultdict(lambda: defaultdict(list))
d = defaultdict(list)
d['key']['a'].append(10)
d['key']['a'].append(15)

print(d)

d = defaultdict(list)