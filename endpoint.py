import urllib3 as url

data = url.request("GET", "http://aze-m.com:3002/posts/init")
body = data.json()

print(data.data)

