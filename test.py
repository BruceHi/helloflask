colors = ['blue', 'green', 'yellow']
print(colors)

c = str(colors)
print(c)

print(c[1:-1])
print('%s' % c[1:-1])

print('/colors/<any(%s):color>' % colors)

print('/colors/<any(%s):color>' % str(colors)[1:-1])