from fake_useragent import UserAgent
import requests

URL = 'http://httpbin.org/user-agent/'
ua = UserAgent()
headers = {
    'user-agent': ua.random
}

response = requests.get(url=URL, stream=True)
with open('file.mp4', 'wb') as file:
    for piece in response.iter_content(chunk_size=100_000):
        file.write(piece)


# ua = UserAgent()

# for x in range(10):
#     ua = UserAgent()
#     fake_ua = {'user-agent': ua.random}
#     response = requests.get(url=URL, headers=fake_ua)

#     print(response.text)

