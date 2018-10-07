# open csv file
footballers = open("footballers.csv")

# for loop to turn the sentence into columns
for line in footballers:
	line = line.strip().split(",")

	# determine which column is what kind of data
	player = line[0]
	club = line [1]
	transfer = line[2]

	# print the line
	print(player + " has made a transfer to " + club + " for the amount of " + transfer + " million euros.")	

# tell program which file to write to
newfile = open("footballers.txt", "w")

# how does the lines in the .txt file need to be written
newfile.write(player + " has made a transfer to " + club + " for the amount of " + transfer + ".000.000" + " milion euros.") 

# add the details about a new transfer
print("Please enter details about the transfer you want to add: ")
writenew_player = input("Which player has made the transfer? (first- + last name): ")
writenew_club = input("To which club has the player made the transfer?: ")
writenew_transfer = input("For how much has this transfer been made? (e.g. 135.000.000): ")

# add the inputs to the .txt. file
writenew = "\n" + writenew_player + "," + writenew_club + "," + writenew_transfer + "\n"

# close csv file
footballers.close()

# open csv file in different way
footballers = open("footballers.csv", "a")

# write the new line added by the user
footballers.write(writenew)

# close both files
newfile.close()
footballers.close()