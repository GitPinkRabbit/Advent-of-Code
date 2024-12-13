s = [(v, -1 if i & 1 else i >> 1) for i, v in enumerate(map(int, list(input())))]
s = [v for c, v in s for _ in range(c)]

i = 0
j = len(s) - 1
while i < j:
	while s[j] == -1:
		j -= 1
	while s[i] != -1:
		i += 1
	if i < j:
		s[i], s[j] = s[j], s[i]

sum = 0
for i, v in enumerate(s):
	sum += i * v if v != -1 else 0

print(sum)
