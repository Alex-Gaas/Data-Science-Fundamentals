# define the lists
wrong = ["milk", "energy", "karnemelk", "water", "soda"]
words = []

# ask the user for the input in form of a sentence
sentence = input("Enter in a sentence what your favorite drink is: ")

# split the sentence by using a space as an indicator
words = sentence.split(" ")

# see the results of the input and the split
print(words)

index = 0
# compare the "words" list to the "wrong" list and give a message based on the input
for word in words:
	if words[index] in wrong:
		print("Wrong")
		# replace the wrong words with correct ones
		if words[index] == "milk":
			words[index] = "soja"
		elif words[index] == "energy":
			words[index] = "coffee"
		elif words[index] == "karnemelk":
			words[index] = "soja"
		elif words[index] == "water":
			words[index] = "siroop"
		elif words[index] == "soda":
			words[index] = "vitamin water"				
	index = index + 1

# join the speperated word back into a sentence
words = " ".join(words)

# print the corrected sentence
print(words)