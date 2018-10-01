# define the lists
names = ["Pieter", "Jantje", "Greta"]
snacks = []

# length of the names
for name in names:
	print(name)
	print(len(name))

index = 0
# create a for loop
for name in names:
	# ask each person personally what their favorite snack is
	snack = input("What is your favourite snack " + name + "? ")
	# add the results to the 'snacks' list
	snacks.append(snack)
	# print the favorite snack of each person as a response
	print(name + " your favourite snack is " + snacks[index])
	# ask again untill no names left
	index = index + 1