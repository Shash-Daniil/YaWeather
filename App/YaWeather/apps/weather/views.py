import requests
from django.shortcuts import render

def weath(request):
	id = '22c0a572ab9efba6090c50484afe1d54'
	url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=' + id
	city = 'Moscow'
	res = requests.get(url.format(city)).json()
	speed_info = {
		'temp': res["main"]["temp"]
	}

	if(request.method == "post"):
		print("debil?")

	context = {'info': speed_info}
	return render(request, 'weather/weatherPage.html', context)