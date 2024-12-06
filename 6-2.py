import copy

s = []

try:
	while True:
		s.append(list(input()))
except Exception as e:
	pass

n = len(s)
m = len(s[0])

sx, sy = -1, -1
for i in range(n):
	for j in range(m):
		if s[i][j] == '^':
			sx, sy = i, j
			break
sdir = -1, 0

ans = 0
for i in range(n):
	for j in range(m):
		if s[i][j] == '^' or s[i][j] == '#':
			continue
		t = copy.deepcopy(s)
		dir = copy.deepcopy(sdir)
		t[i][j] = '#'
		c = 0
		x, y = sx, sy
		while 0 <= x < n and 0 <= y < m:
			t[x][y] = 'X'
			c += 1
			if c > 4 * n * m:
				break
			nx, ny = x + dir[0], y + dir[1]
			if nx < 0 or nx >= n or ny < 0 or ny >= m:
				x, y = nx, ny
			elif t[nx][ny] == '#':
				dir = dir[1], -dir[0]
			else:
				x, y = nx, ny
		print('.', end='', flush=True)
		if c > 4 * n * m:
			ans += 1

print(ans)
