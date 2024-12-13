import itertools

s = []

try:
	while True:
		a, b = tuple([ss.strip() for ss in input().split(':')])
		s.append((int(a), list(map(int, b.split(' ')))))
except Exception as e:
	pass

sum = 0
for a, b in s:
	m = len(b)
	flag = False
	for st in itertools.product(range(2), repeat=m - 1):
		now = b[0]
		for i in range(m - 1):
			j = st[i]
			if j == 0:
				now += b[i + 1]
			else:
				now *= b[i + 1]
			if now > a:
				now = -1
				break
		if now == a:
			flag = True
			break
	if flag:
		sum += a

print(sum)
