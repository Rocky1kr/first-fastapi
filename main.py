from fastapi import FastAPI, Request
import random
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory='templates')

@app.get('/')
def home():
    return {'hello': 'hi'}

@app.get('/lunch')
def lunch():
    menu = ['김밥', '라면', '떡볶이']
    return {
        'pick': random.choice(menu)
    }

@app.get('/lotto')
def lotto():
    numbers = sorted(random.sample(range(1, 46), 6))
    return {'numbers': numbers}

@app.get('/lotto/html')
def lotto_html(request: Request):
    numbers = random.sample(range(1, 46), 6)
    return templates.TemplateResponse(
        request=request, 
        name='lotto.html', 
        context={'numbers': numbers, 'hi': 'sungjin'}
    )

@app.get('/profile/{username}')
def profile(username: str):
    return{'username': username}

@app.get('/cube/{number}')
def cube(number: int):
    return {'number': number ** 3}

@app.get('/api/lotto')
def lotto_api(count: int = 1):
    games = []
    for i in range(count):
        numbers = random.sample(range(1, 46), 6)
        games.append(numbers)

    return games

@app.get('/lotto/html2')
def lotto_html2(request: Request, count: int = 1):
    games = [random.sample(range(1, 46), 6) for _ in range(count)]

    return templates.TemplateResponse(
        request=request,
        name='lotto2.html',
        context={'games': games}
    )

@app.get('/ping')
def ping(request: Request):
    # 입력할 수 있는 빈 종이 주기
    return templates.TemplateResponse(
        request=request,
        name='ping.html'
    )

@app.get('/pong')
def pong(count: int):
    return {'count': count * 2}

@app.get('/lotto/ping')
def lotto_ping(request: Request):
    return templates.TemplateResponse(
        request=request,
        name = 'lotto_ping.html'
    )

@app.get('/lotto/pong')
def lotto_pong(request: Request, count: int):
    games = [random.sample(range(1, 46), 6) for _ in range(count)]
    return templates.TemplateResponse(
        request=request,
        name='lotto_pong.html',
        context={'games': games}
        
        

    )
    