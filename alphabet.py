s = 'abc'
sl = set(s)
l = set(map(chr, range(ord("A"), ord("z"))))
print(sl.issubset(l))