import os
import json
import requests
from aiohttp import web
from banco_de_dados import resposta_jira_dump 
token = os.getenv("WEBHOOK")
lhost = os.getenv("LHOST")
URL = "https://discordapp.com/api/webhooks/{}".format(token)

async def resposta_dump(request):
    resposta_jira = await request.json()
    mensagem, usuario = resposta_jira_dump(resposta_jira) 
    data = {
      'username': 'cotequinho',
      'content': ('%s, <@%s>' % (mensagem, usuario)),
      }
    requests.post(URL, data = data)
    print(data)
    print('ok')
    return web.Response()


app = web.Application()
app.add_routes([web.post('/resposta_dump', resposta_dump)])
web.run_app(app,host=lhost, port=3030)



