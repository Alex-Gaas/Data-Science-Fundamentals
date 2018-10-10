import requests

# ask the user for a url and strip this
user_url = input("Please enter a url: ")
user_url.strip()

# request the website from the given url
r = requests.get(user_url)

# define the status code variable
status_code = r.status_code

# check if the status code is equal to 200 or not. Exit if not the case
if status_code != 200:
	print("Status code is not equal to 200: exiting the program.")
	exit()
else:
	print("Status code is equal to 200.")

# define the headers variable
headers = r.headers

# tell and print the key and values of the page
for key, value in headers.items():
	print(f"{key}: {value}")

# give extra space so that there is a clear line between the key/values and the 10 lines
print("Here comes the text:")
print("")

# define the text variable
text = r.text
# use index as a counter
index = 0

# give the limit that the index should go to and print these lines
while index < 10:
	line = text.splitlines()[index]
	print(line)
	index = index + 1