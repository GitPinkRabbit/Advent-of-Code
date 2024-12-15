s = []

try:
	while True:
		s.append(list(input()))
except Exception as e:
	pass

s, t = s[:s.index([])], [c for w in s[s.index([]) + 1:] for c in w]
s = [[c for ss in [list('..' if c == '.' else '##' if c == '#' else '[]' if c == 'O' else '@.') for c in row] for c in ss] for row in s]

n = len(s)
m = len(s[0])

sx, sy = -1, -1
for i in range(n):
	for j in range(m):
		if s[i][j] == '@':
			sx, sy = i, j
			break
	if sx != -1:
		break

v = [[False] * m for _ in range(n)]

for c in t:
	dir = (0, 1) if c == '>' else (0, -1) if c == '<' else (1, 0) if c == 'v' else (-1, 0)
	if dir[0] == 0:
		l = 1
		while s[sx][sy + l * dir[1]] in '[]':
			l += 1
		if s[sx][sy + l * dir[1]] == '#':
			continue
		for i in range(l):
			s[sx][sy + (l - i) * dir[1]] = s[sx][sy + (l - i - 1) * dir[1]]
		s[sx][sy] = '.'
		sy += dir[1]
	else:
		ok = True
		v[sx + dir[0]][sy] = True
		que = [(sx + dir[0], sy)]
		head = 0
		while head < len(que):
			x, y = que[head]
			head += 1
			if s[x][y] == '#':
				ok = False
				break
			if s[x][y] in '[]':
				v[x + dir[0]][y] = True
				v[x + dir[0]][y + (1 if s[x][y] == '[' else -1)] = True
				que.append((x + dir[0], y))
				que.append((x + dir[0], y + (1 if s[x][y] == '[' else -1)))
		if not ok:
			for x, y in que:
				v[x][y] = False
			continue
		for x, y in reversed(que):
			s[x][y] = s[x - dir[0]][y]
		for x, y in que:
			if not v[x - dir[0]][y]:
				s[x - dir[0]][y] = '.'
		for x, y in que:
			v[x][y] = False
		sx += dir[0]

sum = 0
for i in range(n):
	for j in range(m):
		if s[i][j] == '[':
			sum += 100 * i + j

print(sum)
