import requests
api_key ="1f15e3d684be326f722323dcbea6ee16"
url=f"https://api.openweathermap.org/data/2.5/weather?q=delhi&appid=1f15e3d684be326f722323dcbea6ee16&units=metric"
response=requests.get(url)
print(response.json())