import requests

api_url = "https://jsonplaceholder.typicode.com/todos/5"
post_url = "https://jsonplaceholder.typicode.com/posts"
data = {
        "userID" : 1,
        "title" : "my first post request",
        'body'  : "Learning APIs"
}


response = requests.get(api_url)
print(response.status_code)
print(response.json())


response1 = requests.post(post_url, json=data)
print(response1.status_code)
print(response1.json())
