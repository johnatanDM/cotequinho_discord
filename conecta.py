import psycopg2
import os


class Conexao(object):
  _db=None  
  def __init__(self, mhost, db, usr, pwd):
    self._db = psycopg2.connect(host=mhost, database=db, user=usr,  password=pwd)
  def manipular(self, sql):
    try:
      cur=self._db.cursor()
      cur.execute(sql)
      cur.close()
      self._db.commit()
    except psycopg2.Error as e:
      return e
    
    return True
  def consultar(self, sql):
      rs=None
      try:
          cur=self._db.cursor()
          cur.execute(sql)
          rs=cur.fetchall()
      except:
          return None
      return rs

  def fechar(self):
    self._db.close()

  def rollback(self):
    self._db.rollback()