movie = {
	"name": "Rush",
	"release": 2013,
	"duration": 123,
	"director": "Ron Howard"
}

for key, val in movie.items():
	#print (key + ": " + str(val))
	print(f"{key}: {val}")

#print("My favorite movie is {name} which was released in {release_year}, is directed by {director} and has a duration of {duration}".format(name = name, release = release, duration = duration, director = director))