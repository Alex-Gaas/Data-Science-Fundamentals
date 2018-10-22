import requests

def apicall(title, value):
	print(title)
	print(value)
	url = f"https://en.wikipedia.org/api/rest_v1/page/summary/{title}"
	req = requests.get(url)
	if req.status_code != 200:
		print(f"We got an error: {req.status_code}")
		exit()
	data = req.json()
	return data[f"{value}"]

title = input("Give me the article that you want to lookup? ").strip()
value = input("Do you want the description or extract? ").strip().lower()
data = apicall(title, value)
print(f"Here is the {value} for {title}:")

print(data)