import os
import pickle
import subprocess as sb


def parse_img(path):
    ret = sb.call(['tesseract', path,
                   os.path.join('results', path.split('/')[1].split('.')[0] + '.txt'),
                  '-l', 'rus'])
    return ret

cnt = 0
pref = 'R'
for file in os.listdir('data'):
    print(file)
    os.rename(os.path.join('data', file), os.path.join('data', f'R{cnt}.png'))
    cnt += 1

cnt = 0
for file in os.listdir('data'):
    print(file)
    os.rename(os.path.join('data', file), os.path.join('data', f'{cnt}.png'))
    cnt += 1

res = [''] * len(os.listdir('data'))

for file in os.listdir('data'):
    id = int(file.split('.')[0])
    res[id] = parse_img(os.path.join('data', file))

