def get_middle_page_number(rules, pages):
	middle_page_numbers = []
	for page in pages:
		ok = True
		for i in range(len(page)):
			for j in range(i):
				if (page[i], page[j]) in rules:
					ok = False
		if ok:
			middle_page_numbers.append(page[len(page) // 2])
	return sum(middle_page_numbers)

s = []

try:
	while True:
		s.append(input())
except Exception as e:
	pass

rules = s[:s.index('')]
pages = s[s.index('') + 1:]

rules = [tuple(map(int, rule.split('|'))) for rule in rules]
pages = [list(map(int, page.split(','))) for page in pages]

print(get_middle_page_number(rules, pages))
