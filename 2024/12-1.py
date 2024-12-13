s = []

try:
	while True:
		s.append(list(input()))
except Exception as e:
	pass

n = len(s)
m = len(s[0])

v = [[False] * m for _ in range(n)]

sum = 0
for i in range(n):
	for j in range(m):
		if v[i][j]:
			continue
		area = 1
		perimeter = 4
		stk = [(i, j)]
		v[i][j] = True
		while stk:
			x, y = stk.pop()
			for dx, dy in (1, 0), (-1, 0), (0, 1), (0, -1):
				nx, ny = x + dx, y + dy
				if 0 <= nx < n and 0 <= ny < m and s[nx][ny] == s[i][j]:
					perimeter -= 1
					if v[nx][ny]:
						continue
					v[nx][ny] = True
					stk.append((nx, ny))
					area += 1
					perimeter += 4
		sum += area * perimeter

print(sum)
