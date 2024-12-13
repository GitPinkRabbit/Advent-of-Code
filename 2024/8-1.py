s = []

try:
	while True:
		s.append(list(input()))
except Exception as e:
	pass

n = len(s)
m = len(s[0])

t = [['.'] * m for _ in range(n)]

lc = dict()

for i in range(n):
	for j in range(m):
		if s[i][j] != '.':
			lc[s[i][j]] = lc.get(s[i][j], []) + [(i, j)]

for k, v in lc.items():
	for i in range(len(v)):
		for j in range(i + 1, len(v)):
			x, y = 2 * v[i][0] - v[j][0], 2 * v[i][1] - v[j][1]
			if 0 <= x < n and 0 <= y < m:
				t[x][y] = '#'
			x, y = 2 * v[j][0] - v[i][0], 2 * v[j][1] - v[i][1]
			if 0 <= x < n and 0 <= y < m:
				t[x][y] = '#'

print(sum([x.count('#') for x in t]))
