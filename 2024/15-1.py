s = []

try:
	while True:
		s.append(list(input()))
except Exception as e:
	pass

s, t = s[:s.index([])], [c for w in s[s.index([]) + 1:] for c in w]

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

for c in t:
	dir = (0, 1) if c == '>' else (0, -1) if c == '<' else (1, 0) if c == 'v' else (-1, 0)
	len = 1
	while s[sx + len * dir[0]][sy + len * dir[1]] == 'O':
		len += 1
	if s[sx + len * dir[0]][sy + len * dir[1]] == '#':
		continue
	for i in range(len):
		s[sx + (len - i) * dir[0]][sy + (len - i) * dir[1]] = s[sx + (len - i - 1) * dir[0]][sy + (len - i - 1) * dir[1]]
	s[sx][sy] = '.'
	sx, sy = sx + dir[0], sy + dir[1]

sum = 0
for i in range(n):
	for j in range(m):
		if s[i][j] == 'O':
			sum += 100 * i + j

print(sum)
