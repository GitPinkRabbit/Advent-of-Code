def get_middle_page_number(rules, pages):
	middle_page_numbers = []
	for page in pages:
		ok = True
		for i in range(len(page)):
			for j in range(i):
				if (page[i], page[j]) in rules:
					ok = False
		if ok:
			pass
		else:
			# topological sort of {page} in another way
			queue = []
			in_degree = [0] * 100
			for i in page:
				for j in page:
					if (j, i) in rules:
						in_degree[i] += 1
			for i in page:
				if in_degree[i] == 0:
					queue.append(i)
			sorted_page2 = []
			while queue:
				node = queue.pop(0)
				sorted_page2.append(node)
				for i in page:
					if (node, i) in rules:
						in_degree[i] -= 1
						if in_degree[i] == 0:
							queue.append(i)
			assert len(page) == len(sorted_page2)
			middle_page_numbers.append(sorted_page2[len(page) // 2])
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
