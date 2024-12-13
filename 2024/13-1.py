import re

s = []

try:
	while True:
		s.append(input())
except Exception as e:
	pass

s = list(zip(*[iter(filter(lambda x: len(x) != 0, s))] * 3))

sum = 0
for a, b, c in s:
	ax, ay = map(int, re.findall(r'\d+', a))
	bx, by = map(int, re.findall(r'\d+', b))
	cx, cy = map(int, re.findall(r'\d+', c))
	minnum = 999999999
	for i in range(100):
		for j in range(100):
			if ax * i + bx * j == cx and ay * i + by * j == cy:
				minnum = min(minnum, 3 * i + j)
	if minnum != 999999999:
		sum += minnum

print(sum)
