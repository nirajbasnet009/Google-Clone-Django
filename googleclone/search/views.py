from django.shortcuts import render
from django.http import HttpResponse
from bs4 import BeautifulSoup as bs
import requests

# Create your views here.
def home(request):
    if request.method == 'post':
        pass
    return render(request, 'home.html')

def search(request):
    if request.method == 'POST':
        search = request.POST['search']

        url = "https://www.bing.com/search?q="+search

        response = requests.get(url)
        soup = bs(response.text,'lxml')

        result_listings = soup.find_all("li",{'class':"b_algo"})

        final_result = []
        for result in result_listings:
            result_title = result.find('h2').text
            result_url = result.find('a',class_='tilk').get('href')
            result_desc = result.find('p').text
            # 
            final_result.append((result_title,result_url,result_desc))

        context = {
            "final_result":final_result
        }
        return render(request,'search.html',context)
    return render(request, 'search.html')
