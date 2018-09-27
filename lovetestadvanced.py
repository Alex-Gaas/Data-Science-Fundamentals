# Input of two variables
name_1 = input("What is your name? ")
name_2 = input("What is your lovers name? ")

# Lowercase the variables
name_1 = name_1.lower()
name_2 = name_2.lower()

# Strip the variables
name_1 = name_1.strip()
name_2 = name_2.strip()

# Counting the characters in both variables
count_name_1 = len(name_1)
count_name_2 = len(name_2)

# Difference in amount characters can be negatives, "abs" makes it positive
calc_dif = abs(count_name_1 - count_name_2)

# Calculate the difference between the amount characters. Lower means higher percentage of a match.
if calc_dif == 0:
	print("Fantastic! You are a 100% match!")
elif calc_dif == 1:
	print("Very nice! You are a 80% match!")
elif calc_dif == 2:
	print("Possible, you are a 60% match.")
elif calc_dif == 3:
	print("Doubful, you are only a 40% match.")
elif calc_dif == 4:
	print("Are you sure? You are just a 20% match.")
else:
	print ("Not gonna work, you are a 0% match.")