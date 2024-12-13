s = []

try:
	while len(s0:=input()):
		s.append(s0)
except Exception as e:
	pass

n = len(s)
m = len(s[0])

c = 0
for i in range(1, n - 1):
	for j in range(1, m - 1):
		if s[i][j] != 'A':
			continue
		w = sorted([s[i - 1][j - 1], s[i - 1][j + 1], s[i + 1][j - 1], s[i + 1][j + 1]])
		if w != sorted(['M', 'M', 'S', 'S']):
			continue
		if s[i - 1][j - 1] == s[i + 1][j + 1]:
			continue
		c += 1

print(c)
