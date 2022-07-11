from django.shortcuts import render
import random
import time

users = {}

def generate_id():
    return random.randint(1000, 9999999)

def index(request):
    session_id = request.COOKIES.get('session_id')
    user = users.get(session_id)
    if not user:
        session_id = str(generate_id())
        users[session_id] = {
            'count': 1,
            'start_time': time.time()
        }
    else:
        users[session_id]['count'] += 1
    response = render(request, 'view_app/index.html', {'count': users[session_id]['count']})
    response.set_cookie('session_id', session_id)
    return response

