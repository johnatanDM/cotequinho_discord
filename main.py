# Work with Python 3.6
import discord
import re
import os
from atlassian import Jira

from conecta import Conexao
import banco_de_dados 


TOKEN = os.environ['TOKEN_COTEQUINHO']
jiraurl = os.getenv("JIRA_URL")

host_database = os.getenv("HOST_DATABASE")
database = os.getenv("DATABASE")
user_database = os.getenv("USER_DATABASE")
pass_user_database = os.getenv("PASS_USER_DATABASE")

client = discord.Client()
autorizado = True

def jira(porta):
    jira = Jira(
        url=jiraurl + ':' + porta,
        username='sistema',
        password= os.getenv("JIRA_SENHA_" + porta))
    return jira

def conectar():
    con=Conexao(host_database, database, user_database, pass_user_database)
    return con
    
    
@client.event
async def on_message(message):
  johnatan = client.get_user(239100590276214785) 
  if message.author == client.user:
    return

  if message.content.startswith('!meuid'):
    msg = 'Seu id é: %s' % message.author.id
    await message.author.send(msg)

  if message.content.startswith('!ola'):
    msg = 'Olá mundo'
    await message.channel.send(msg)

  if message.content.startswith('!dump'):
    msg, msgdba = banco_de_dados.issue_jira_dump(jira('9090'), client, message)
    await johnatan.send(msgdba)
    await message.channel.send(msg)

  if message.content.startswith('!novorelogio'):
    msg, msgdba = banco_de_dados.issue_jira_novo_relogio(jira('9090'), client, message)
    await johnatan.send(msgdba)
    await message.channel.send(msg)

  if message.content.startswith('!manutencaobd'):
    msg, msgdba = banco_de_dados.issue_jira_manutencaobd(jira('9090'), client, message)
    await johnatan.send(msgdba)
    await message.channel.send(msg)

  if message.content.startswith('!sqlhelp'):
    msg, msgdba = banco_de_dados.issue_jira_sqlhelp(jira('9090'), client, message)
    await johnatan.send(msgdba)
    await message.channel.send(msg)

  if message.content.startswith('!sqltune'):
    msg, msgdba = banco_de_dados.issue_jira_sqltune(jira('9090'), client, message)
    await johnatan.send(msgdba)
    await message.channel.send(msg)
@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id) 
    print('------')

client.run(TOKEN)