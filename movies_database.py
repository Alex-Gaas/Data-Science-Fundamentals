import json

with open("movies.json") as f:
	movies = json.load(f)

# ask the user for a year 
year_user = int(input("What year are you interested in?: "))

# show the movies that were released in that given year
for movie in movies:
	year = movie["year"]
	title = movie["title"]
	if year == year_user:
		print(title)

# ask the user for a minimal duration for a movie
duration_user = int(input("What has to be the minimal duration of the movie?: "))

# only print the movies that are equal to that given duration or are longer
for movie in movies:
	duration = movie["duration"]
	title = movie["title"]
	if duration >= duration_user:
		print(title)

# ask the user if they want to see movies where the director and actor is equal
directoractor_user = input("Do you want to see movies where the director is also an actor in the movie? (yes/no): ")
# format the input to lowercase
directoractor_user.strip().lower()

# only run the this code if the input from the user is equal to: "yes"
if directoractor_user == "yes":
	# show all the movies where the director is also an actor in the movie
	for movie in movies:
		director = movie["director"]
		actor = movie ["actors"]
		if movie["director"] in actor:
			print(f"In the movie {movie['title']} the director is also an actor in the movie")

# ask the user for a director
director_user = input("From which director do you want to see the movies?: ")
director_user.title()

# show the movies from that given director
for movie in movies:
	director = movie["director"]
	title = movie["title"]
	if director == director_user:
		print(title)

# ask the user for a actor
actor_user = input("From which actor do you want to see the movies?: ")
actor_user.title()

# show the movies from that given actor
for movie in movies:
	actor = movie["actors"]
	title = movie["title"]
	if actor == actor_user:
		print(title)

