from django.shortcuts import render
import random

users = {}
def send_the_homepage(request):
    
    user_id = request.COOKIES.get('user_id')
    if not user_id or not user_id in users:
        user_id = str(random.randint(1000000,9999999))
        users[user_id] = 1
        response = render(request, 'view_counter_app/index.html', {'views': users[user_id]} )
        response.set_cookie('user_id', user_id)
        return response
    else:
        users[user_id] += 1
        response = render(request, 'view_counter_app/index.html', {'views': users[user_id]} )
        return response