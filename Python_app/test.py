import requests


book = "Harry Potter and the half-Blood Prince"

response = requests.get("https://aot-api.vercel.app/quote")
print(response.text)