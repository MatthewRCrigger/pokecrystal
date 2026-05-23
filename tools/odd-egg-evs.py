filename = 'data/events/odd_eggs.asm'

with open(filename, 'r', encoding='utf8') as file:
    content = file.read()

old = '''\t; Stat exp
\tbigdw 0
\tbigdw 0
\tbigdw 0
\tbigdw 0
\tbigdw 0'''

new = '''\tdb 0, 0, 0, 0, 0, 0 ; EVs
\tdb 0, 0, 0, 0 ; padding'''

content = content.replace(old, new)

with open(filename, 'w', encoding='utf8') as file:
    file.write(content)

print('Done!')
