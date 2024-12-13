s = [(v, -1 if i & 1 else i >> 1) for i, v in enumerate(map(int, list(input())))]
s = list(filter(lambda x: x[0] != 0, s))

maxhole = 999999
j = len(s)
while j >= 0:
	j -= 1
	if s[j][1] == -1:
		continue
	if s[j][0] > maxhole:
		continue
	thismaxhold = 0
	holeid = -1
	for i in range(j):
		if s[i][1] == -1:
			thismaxhold = max(thismaxhold, s[i][0])
			if s[i][0] >= s[j][0]:
				holeid = i
				break
	if holeid == -1:
		maxhole = thismaxhold
		continue
	print(f'{j} -> {holeid}')
	if s[holeid][0] > s[j][0]:
		newhole = (s[holeid][0] - s[j][0], -1)
		s[holeid] = (s[j][0], s[j][1])
		s[j] = (s[j][0], -1)
		s.insert(holeid + 1, newhole)
		j += 1
	else:
		s[holeid] = (s[j][0], s[j][1])
		s[j] = (s[j][0], -1)

s = [v for c, v in s for _ in range(c)]
# print(''.join(map(lambda x: '.' if x == -1 else str(x), s)))

sum = 0
for i, v in enumerate(s):
	sum += i * v if v != -1 else 0

print(sum)
