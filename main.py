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
    692734511095742535
    
@client.event
async def on_message(message):
  server = client.get_guild(691616063334514749)
  membro = server.get_member(message.author.id)
  is_lider = (discord.utils.get(membro.roles, name = 'Lider') == discord.utils.get(server.roles, name = 'Lider'))
  is_gerente = (discord.utils.get(membro.roles, name = 'Gerente') == discord.utils.get(server.roles, name = 'Gerente'))
  johnatan = client.get_user(239100590276214785) 
  adolfho = client.get_user(692727946242424883)
  if message.author == client.user:
    return

  if message.content.startswith('!meuid'):
    msg = 'Seu id é: %s' % message.author.id
    await message.author.send(msg)

  if message.content.startswith('!ola') or message.content.startswith('!help') or message.content.startswith('!ajuda'):
    msg = """Olá, Eu sou o Cotequinho Bot e já sei fazer algumas coisas! \n
- Você pode pedir Dump para a equipe de Banco de dados assim: \n
!dump Sistema Ambiente_origem -> Ambiente_destino \n
- Você pode pedir para o DBA lhe ajudar a criar uma consulta assim: \n
!sqlhelp Sistema \n
- Quer uma ajuda pra melhorar uma consulta que já existe? \n
!slqtune Sistema \n
- Para solicitar recovery, integração ou acesso a algum banco: \n
!manutencaobd Descrição \n
- Você também pode pedir para cadastrar um novo relógio no banco do ponto assim: \n
!novorelogio 172.123.123.123 URBFOR   
"""
    await message.channel.send(msg)

  if message.content.startswith('!dump'):
    if is_lider or is_gerente:
      msg, msgdba = banco_de_dados.issue_jira_dump(jira('9090'), client, message)
      if msgdba != '':
        await johnatan.send(msgdba)
        await adolfho.send(msgdba)
    else:
      msg = 'Olá %s! Infelizmente somente os líderes podem pedir dump!' % message.author.mention
      msgdba = '%s tentou pedir um dump.' %  message.author.mention
      await johnatan.send(msgdba)
      await adolfho.send(msgdba)
    await message.channel.send(msg)

  if message.content.startswith('!novorelogio'):
    msg, msgdba = banco_de_dados.issue_jira_novo_relogio(jira('9090'), client, message)
    if msgdba != '':
      await johnatan.send(msgdba)
      await adolfho.send(msgdba)
    await message.channel.send(msg)

  if message.content.startswith('!manutencaobd'):
    msg, msgdba = banco_de_dados.issue_jira_manutencaobd(jira('9090'), client, message)
    if msgdba != '':
      await johnatan.send(msgdba)
      await adolfho.send(msgdba)
    await message.channel.send(msg)

  if message.content.startswith('!sqlhelp'):
    msg, msgdba = banco_de_dados.issue_jira_sqlhelp(jira('9090'), client, message)
    if msgdba != '':
      await johnatan.send(msgdba)
      await adolfho.send(msgdba)
    await message.channel.send(msg)

  if message.content.startswith('!sqltune'):
    msg, msgdba = banco_de_dados.issue_jira_sqltune(jira('9090'), client, message)
    if msgdba != '':
      await johnatan.send(msgdba)
      await adolfho.send(msgdba)
    await message.channel.send(msg)
@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id) 
    print('------')

client.run(TOKEN)
