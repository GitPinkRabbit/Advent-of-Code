import re

s = []

try:
	while len(s0:=input()):
		s.append(s0)
except Exception as e:
	pass

s = "|".join(s)

pattern = '(mul\\(\\d+\\,\\d+\\)|do\\(\\)|don\\\'t\\(\\))'

result = re.findall(pattern, s)

def mul(a, b):
	return a * b

su = 0

toggle = 1

for s0 in result:
	if s0[0] == 'd':
		toggle = 1 if len(s0) == 4 else 0
	else:
		su += toggle * eval(s0)

print(su)
