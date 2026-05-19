import requests

# 1. API endpoint (URL)
url = "https://jsonplaceholder.typicode.com/posts/1"

# 2. Send GET request
response = requests.get(url)
print(f"Response Status Code: {response}")

# 3. Convert response to JSON
data = response.json()
#print(data)

# 4. Display data
print("✅ Post Details:")
print("Title:", data['title'])
print("Body:", data['body'])
print("User I'd:", data['userId'])
