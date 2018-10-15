import requests
import json

index = 1

# ask the user for a Wikipedia article and strip the input
user_article = input("Only enter the title of the Wikipedia article: ").strip()
# replace the spaces with lowercase dashes
user_article = user_article.replace(" ","_")
# ask for first languague of choice
user_languague = input("Please input the first languague of your choice (e.g. nl): ").strip().lower()
# combine the API URL of Wikipedia with the correct formated lanuague + input article
user_url = "https://" + user_languague + ".wikipedia.org/api/rest_v1/page/summary/" + user_article

# continue this loop untill there is a total of three languagues in this program
while index <= 3:
	# check the created API URL
	print(user_url)

	# request the website from the given url
	r = requests.get(user_url)

	# define the status code variable
	status_code = r.status_code

	# check if the status code is equal to 200 or not. Exit if not the case
	if status_code != 200:
		print("Status code is " + str(status_code) + ", this is not equal to 200: exiting the program.")
		exit()
	else:
		print("Status code is equal to 200.")

	data = json.loads(r.text)
	# print the title
	print("Title: " + data["title"])
	# print the extract
	print("Extract: " + data["extract"])
	# print the description
	print("Description: " + data["description"])

	index = index + 1

	# get a clear seperation between the different languagues 
	print(" ")
	# ask for the next languague
	user_languague = input("Please input the next languague of your choice (e.g. en): ").strip().lower()

	# combine the API URL of Wikipedia with the correct formated lanuague + input article
	user_url = "https://" + user_languague + ".wikipedia.org/api/rest_v1/page/summary/" + user_article

