s = []

try:
	while True:
		s.append(list(map(int, list(input()))))
except Exception as e:
	pass

n = len(s)
m = len(s[0])

sum = 0
for i in range(n):
	for j in range(m):
		if s[i][j] != 0:
			continue
		t = [[False] * m for _ in range(n)]
		t[i][j] = True
		for k in range(1, 10):
			for x in range(n):
				for y in range(m):
					if s[x][y] != k:
						continue
					for dx, dy in ((0, 1), (0, -1), (1, 0), (-1, 0)):
						nx, ny = x + dx, y + dy
						if nx < 0 or nx >= n or ny < 0 or ny >= m:
							continue
						if t[nx][ny] and s[nx][ny] == k - 1:
							t[x][y] = True
							break
		for x in range(n):
			for y in range(m):
				if s[x][y] == 9 and t[x][y]:
					sum += 1

print(sum)
