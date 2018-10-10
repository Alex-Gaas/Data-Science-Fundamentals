movie = {
	"name": "Rush",
	"release": 2013,
	"duration": 123,
	"director": "Ron Howard"
}

# define the actors and add these to the directory: movie
movie["actors"] = ["Chris Hemsworth", "Daniel Brühl", "Olivia Wilde"]

for key, val in movie.items():
	# only if the key is "duration": put minutes behind the value
	if key == "duration":
		print(f"{key}: {val} minutes")
	# only if the key is "actors": print the key, colon, and each actor with a comma and space between them untill nothing left
	elif key == "actors":
		print(key + ": " + ", ".join(val))
	# print the rest of the keys and values that have not been put in a if statement
	else:
		print(f"{key}: {val}")

