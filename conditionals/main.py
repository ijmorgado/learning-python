
x = int(raw_input('Please enter a number:'))


if x < 0:
	x = 0
	print 'Negative changed to 0'
elif x == 0:
	print 'Zero'
elif x == 1:
	print 'Single'
else:
	print 'More...'


words = ['cat','dog','cow']

for w in words:
	print w, len(w)


print 'Another sample...'


for w in words[:]:
	if len(w) == 3:
		words.insert(0,w)
		print w, len(w)


x = range(-1,10)

print x

for x in range(-12,10,3):
	print x

for x in range(len(words)):
	print x, words[x]