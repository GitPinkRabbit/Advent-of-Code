s = []

try:
	while len(s0:=input()):
		s.append(s0)
except Exception as e:
	pass

n = len(s)
m = len(s[0])

dirs = [(1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]
pattern = 'XMAS'

c = 0
for i in range(n):
	for j in range(m):
		for dx, dy in dirs:
			ok = True
			for k in range(4):
				x = i + dx * k
				y = j + dy * k
				if x < 0 or x >= n or y < 0 or y >= m or s[x][y] != pattern[k]:
					ok = False
					break
			if ok:
				c += 1

print(c)
