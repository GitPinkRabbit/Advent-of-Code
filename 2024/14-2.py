import re

s = []

try:
	with open('input.txt') as f:
		s = f.readlines()
except Exception as e:
	pass

n = 101
m = 103

# test
for _ in [7753]:
	t = [[0] * m for _ in range(n)]

	for ss in s:
		px, py, vx, vy = map(int, re.findall(r'-?\d+', ss))
		x = (px + _ * vx) % n
		y = (py + _ * vy) % m
		t[x][y] += 1

	print('\n'.join(''.join(map(lambda x: '.' if x == 0 else '#', row)) for row in t))
	print(_)
	pause = input()

# ans = 7753
for _ in range(28, 1000000, 103):
	t = [[0] * m for _ in range(n)]

	for ss in s:
		px, py, vx, vy = map(int, re.findall(r'-?\d+', ss))
		x = (px + _ * vx) % n
		y = (py + _ * vy) % m
		t[x][y] += 1

	print('\n'.join(''.join(map(lambda x: '.' if x == 0 else '#', row)) for row in t))
	print(_)
	pause = input()
