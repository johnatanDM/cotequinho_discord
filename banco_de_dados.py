import re


def issue_jira_dump(jira, bot, message):
  msg = ''
  msgdba = ''
  match = re.match(r'.+ +.+->.+', message.content)
  if match:
      titulo = message.content[6:]
      usuario = message.author.id
      fields = {
          'project': {
              'key': "ADDBDD"
          },
          'summary': 'Dump: %s' % titulo,
          'customfield_10500': '%s' % usuario,
          'issuetype': {
              'name': "Task"
          }
      }
      atividade = jira.issue_create(fields)
      if atividade: 
        msg = ("Seu Dump foi registrado no nosso JIRA %s" % message.author.mention)
        msgdba = ("Dump: %s" % titulo)
      else: 
        msg = atividade
  else:
      msg = ("Por favor me informe o seu dump como no exemplo: \n \"/dump Sistema Ambiente_origem -> Ambiente_destino\"")
  return msg, msgdba

    

def issue_jira_sqlhelp(jira, bot, message):
  msg = ''
  msgdba = ''
  titulo = message.content[9:]
  usuario = message.author
  fields = {
      'project': {
          'key': "ADDBDD"
      },
      'summary': 'SQLHelp: %s' % titulo,
      'description': '%s' % usuario,
      'issuetype': {
          'name': "Task"
      }
  }
  atividade = jira.issue_create(fields)
  if atividade:
    msg = ("O DBA já foi avisado e assim que possível irá lhe atender %s." % message.author.mention)
    msgdba = ("SQLHelp: %s, %s" % (titulo, usuario)) 
  else:
    msg = atividade
  return msg, msgdba

def issue_jira_sqltune(jira, bot, message):
  msg = ''
  msgdba = ''
  titulo = message.content[9:]
  usuario = message.author
  fields = {
      'project': {
          'key': "ADDBDD"
      },
      'summary': 'SQLTune: %s' % titulo,
      'description': '%s' % usuario,
      'issuetype': {
          'name': "Task"
      }
  }
  atividade = jira.issue_create(fields)
  if atividade:
    msg = ("O DBA já foi avisado e assim que possível irá lhe atender %s." % message.author.mention)
    msgdba = ("SQLHelp: %s, %s" % (titulo, usuario)) 
  else:
    msg = atividade
  return msg, msgdba

def issue_jira_manutencaobd(jira, bot, message):
  msg = ''
  msgdba = ''
  titulo = message.content[14:]
  usuario = message.from_user.first_name + ' ' + (message.from_user.last_name or '')
  fields = {
      'project': {
          'key': "ADDBDD"
      },
      'summary': 'ManutençãoBD: %s' % usuario,
      'customfield_10500': '%s' % usuario,
      'description': '%s' % titulo,
      'issuetype': {
          'name': "Task"
      }
    } 
  atividade = jira.issue_create(fields)
  if atividade:
    msg = "O DBA já foi avisado e assim que possível irá lhe atender."
    msgdba = ("ManutençãoBD: %s, %s" % (titulo, usuario))
  else: 
    msg = atividade
  return msg, msgdba

def issue_jira_novo_relogio(jira, bot, message):
    msg = ''
    msgdba = ''
    match = re.match(r'.+(?:\d{1,3}\.){3}\d{1,3}.+', message.content)
    if match:
        titulo = message.content[14:]
        usuario = message.author.id
        fields = {
            'project': {
                'key': "ADDBDD"
            },
            'summary': 'Cadastrar IP relógio: %s' % titulo,
            'description': ('%s' % usuario),
            'issuetype': {
                'name': "Task"
            }
        }
        atividade = jira.issue_create(fields)
        if atividade:
          msg = ("Sua requisição foi registrado no nosso JIRA %s" % message.author.mention)
          msgdba = "Cadastrar IP relógio: %s" % titulo
    else: 
        msg = "IP inválido"
    return msg, msgdba


def resposta_jira_dump(resposta_jira):
    usuario = resposta_jira["issue"]["fields"]["customfield_10500"]
    mensagem = "O %s terminou" % resposta_jira["issue"]["fields"]["summary"]
    return mensagem, usuario