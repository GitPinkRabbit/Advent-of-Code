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
	cx += 10000000000000
	cy += 10000000000000
	assert ax * by != ay * bx
	i = cx * by - cy * bx
	j = cy * ax - cx * ay
	k = ax * by - ay * bx
	if i % k == 0 and j % k == 0 and i // k >= 0 and j // k >= 0:
		sum += 3 * (i // k) + (j // k)

print(sum)
