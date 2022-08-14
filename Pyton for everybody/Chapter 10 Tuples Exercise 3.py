import string
fname = input('Enter file name: ')
try:
	fhandle = open(fname)
except:
	print ('File cannot be opened:', fname)
	exit()
letters = dict()
for line in fhandle:
	line = line.translate(str.maketrans('', '', string.punctuation))
	line = line.translate(str.maketrans('', '', string.digits))
	line = line.lower()
	line = line.split()
	for t in line:
		word = list(t)
		for letter in word:
			letters[letter] = letters.get(letter,0) + 1
letterlist = []
for letter, count in letters.items():
	letterlist.append( (count, letter) )
letterlist.sort(reverse=True)
for count, letter in letterlist:
  print (letter, count)

