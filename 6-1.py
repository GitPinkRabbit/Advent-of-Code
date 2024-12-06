s = []

try:
	while True:
		s.append(list(input()))
except Exception as e:
	pass

n = len(s)
m = len(s[0])

x, y = -1, -1
for i in range(n):
	for j in range(m):
		if s[i][j] == '^':
			x, y = i, j
			break
dir = -1, 0

while 0 <= x < n and 0 <= y < m:
	s[x][y] = 'X'
	nx, ny = x + dir[0], y + dir[1]
	if nx < 0 or nx >= n or ny < 0 or ny >= m:
		x, y = nx, ny
	elif s[nx][ny] == '#':
		dir = dir[1], -dir[0]
	else:
		x, y = nx, ny

print(sum([ss.count('X') for ss in s]))
