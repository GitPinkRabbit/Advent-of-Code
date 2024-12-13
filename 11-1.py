def trans(s):
	t = []
	for x in s:
		if x == 0:
			t.append(1)
		elif len(str(x)) % 2 == 0:
			t.append(int(str(x)[:len(str(x)) // 2]))
			t.append(int(str(x)[len(str(x)) // 2:]))
		else:
			t.append(x * 2024)
	return t

s = list(map(int, input().split()))
for _ in range(25):
	s = trans(s)

print(len(s))
