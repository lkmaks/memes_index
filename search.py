import os

t = 'обни'

for file in os.listdir('results'):
    content = open('results/' + file).read()
    if t in content:
        print(file.split('.')[0])

