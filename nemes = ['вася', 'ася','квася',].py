from collections import Counter



nemes = ['вася', 'ася', 'квася', 'ася',]
counter = dict(Counter(nemes))
for k, v in counter.items():
    print(f'{k}: {v}')
