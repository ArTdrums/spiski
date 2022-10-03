a = input()
s = list(a)
for i in range(s.count('a')):
    s.remove('a')
for i in range(s.count('e')):
    s.remove('e')
for i in range(s.count('u')):
    s.remove('u')
print(s)