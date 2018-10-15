import requests
import json

# ask the user for a Wikipedia article and strip the input
user_article = input("Only enter the title of the Wikipedia article: ").strip()
# replace the spaces with lowercase dashes
user_article = user_article.replace(" ","_")
# combine the API URL of Wikipedia with the correct formated input article
user_article = "https://en.wikipedia.org/api/rest_v1/page/summary/" + user_article

# check the created API URL
print(user_article)

# request the website from the given url
r = requests.get(user_article)

# define the status code variable
status_code = r.status_code

# check if the status code is equal to 200 or not. Exit if not the case
if status_code != 200:
	print("Status code is not equal to 200: exiting the program.")
	exit()
else:
	print("Status code is equal to 200.")

data = json.loads(r.text)
# print the title
print("Title: " + data["title"])
# print the extract
print("Extract: " + data["extract"])
# check if there is a description and print accordingly
#if data["description"] >= 1:
print("Description " + data["description"])
#else:
	#print("This article has no description.")


#for key in data:
#	value = data[key]
#	print(key, value)