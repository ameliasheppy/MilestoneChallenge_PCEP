import requests

url = "https://icanhazdadjoke.com/"
headers = {"Accept": "application/json"}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    joke = response.json().get("joke")
    print("Here's a dad joke for you:")
    print(joke)
else:
    print("Oops! Couldn't fetch a joke.")
