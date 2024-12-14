import re

s = []

try:
	while True:
		s.append(input())
except Exception as e:
	pass

n = 101
m = 103

t = [[0] * m for _ in range(n)]

for ss in s:
	px, py, vx, vy = map(int, re.findall(r'-?\d+', ss))
	x = (px + 100 * vx) % n
	y = (py + 100 * vy) % m
	t[x][y] += 1

q = [0] * 4

for i in range(n):
	for j in range(m):
		if i != n // 2 and j != m // 2:
			q[(i > n // 2) * 2 + (j > m // 2)] += t[i][j]

ans = q[0] * q[1] * q[2] * q[3]

print(ans)
