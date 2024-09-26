import os
import matplotlib.pyplot as plt
from collections import Counter

n_words = dict()

for file in os.listdir('results'):
    content = open('results/' + file).read()
    id = file.split('.')[0]
    words = content.split()
    n_words[id] = len(words)

counts = Counter()
for id in n_words:
    counts[n_words[id]] += 1

print(f'{counts[0] / len(n_words) * 100:.2f}% empty')

plt.hist([n_words[id] for id in n_words], bins=50)
plt.savefig('n_words.png')

