namespaces = {'global':{'parent': None}}

#for _ in range(int(input())):
while True:
	s = input().split()
	if s[0] == 'create':
		#if s[1] not in namespaces:
		namespaces[s[1]] = {'parent':s[2]}
	elif s[0] == 'add':
		if s[1] in namespaces:
			namespaces[s[1]][s[2]] = None
	elif s[0] == 'get':
		if s[1] in namespaces:
			name = s[1]
			isFound = False
			while name != None:
				if s[2] in namespaces[name].keys():
					print(name)
					isFound = True
					break
				else:
					name = namespaces[name]['parent']
					#print(name)
			print(name)
			#if not isFound: print(None)
		#else: print(None)
	elif s[0] == 'show':
		print(namespaces)
	else: print("Unknown command!")

#print(namespaces)
