#Started on 22 Jul
#Test
driving = input("Have you ever driven a car?\n(Yes/No): ")
if driving != 'Yes' and 'No':
	print ('Only Yes/No')
	raise SystemExit
age = input("Age?: ")
age = int(age)
if driving == 'Yes':
	if age >= 18:
		print('You have passed the test')
	else:
		print('You have violated the regulation')
elif driving == 'No':
	if age >= 18:
		print('You are able to take the license class')
	else:
		print('Great! Only few years left to get a license')
