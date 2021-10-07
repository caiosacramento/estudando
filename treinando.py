import pandas as pd  
from yahoofinancials import YahooFinancials
import mysql.connector
from datetime import date 


mydb = mysql.connector.connect(
      host = "localhost",
      user = "root",
      database = "mercadoacoes",
)

#TODO metodos que devolve o valor medio da ação no fechamento da bolsa de 7 dias, 15 dias, 30 dias, 60 , 90 , 180, 365 CHECK
def precoSete(numColunas):
      # retorna a media dos preços dos ultimos 7 dias de bolsa
      media = 0 
      for i in range(int(numColunas), int(numColunas) - 7, -1):
          media = float(tsla_df.loc[i,'close']) + media 
          
      return  (media/7)
def precoQuinze(numColunas):
      # retorna a media dos preços dos ultimos 15 dias de bolsa
      media = 0 
      for i in range(int(numColunas), int(numColunas) - 15, -1):
          media = float(tsla_df.loc[i,'close']) + media
      return (media/15)
def precoTrinta(numColunas):
      # retorna a media dos preços dos ultimos 30 dias de bolsa
      media = 0 
      for i in range(int(numColunas), int(numColunas) - 30, -1):
          media = float(tsla_df.loc[i,'close']) + media
      return (media/30)     
def precoSessenta(numColunas):
      # retorna a media dos preços dos ultimos 60 dias de bolsa
      media = 0 
      for i in range(int(numColunas), int(numColunas) - 60, -1):
          media = float(tsla_df.loc[i,'close']) + media
      return (media/60)
def precoNoventa(numColunas):
      # retorna a media dos preços dos ultimos 90 dias de bolsa
      media = 0 
      for i in range(int(numColunas), int(numColunas) - 90, -1):
          media = float(tsla_df.loc[i,'close']) + media
      return (media/90)
def precoCentoOitenta(numColunas):
      # retorna a media dos preços dos ultimos 180 dias de bolsa
      media = 0 
      for i in range(int(numColunas), int(numColunas) - 180, -1):
          media = float(tsla_df.loc[i,'close']) + media
      return (media/180)
def precoTrezentosSessenta(numColunas):
      # retorna a media dos preços dos ultimos 365 dias de bolsa
      media = 0 
      for i in range(int(numColunas), int(numColunas) - 365, -1):
          media = float(tsla_df.loc[i,'close']) + media
      return (media/365)

#TODO metodo que devolve o valor medio da açao no high de 7 dias, 15 dias, 30 dias, 60 , 90 , 180, 365 CHECK
def precoHighSete(numColunas):
          # retorna a media dos preços dos ultimos 7 dias de bolsa
      media = 0 
      for i in range(int(numColunas), int(numColunas) - 7, -1):
          media = float(tsla_df.loc[i,'high']) + media 
          
      return  (media/7)
def precoHighQuinze(numColunas):
      # retorna a media dos preços dos ultimos 15 dias de bolsa
      media = 0 
      for i in range(int(numColunas), int(numColunas) - 15, -1):
          media = float(tsla_df.loc[i,'high']) + media
      return (media/15)
def precoHighTrinta(numColunas):
      # retorna a media dos preços dos ultimos 30 dias de bolsa
      media = 0 
      for i in range(int(numColunas), int(numColunas) - 30, -1):
          media = float(tsla_df.loc[i,'high']) + media
      return (media/30)     
def precoHighSessenta(numColunas):
      # retorna a media dos preços dos ultimos 60 dias de bolsa
      media = 0 
      for i in range(int(numColunas), int(numColunas) - 60, -1):
          media = float(tsla_df.loc[i,'high']) + media
      return (media/60)
def precoHighNoventa(numColunas):
      # retorna a media dos preços dos ultimos 90 dias de bolsa
      media = 0 
      for i in range(int(numColunas), int(numColunas) - 90, -1):
          media = float(tsla_df.loc[i,'high']) + media
      return (media/90)
def precoHighCentoOitenta(numColunas):
      # retorna a media dos preços dos ultimos 180 dias de bolsa
      media = 0 
      for i in range(int(numColunas), int(numColunas) - 180, -1):
          media = float(tsla_df.loc[i,'high']) + media
      return (media/180)
def precoHighTrezentosSessenta(numColunas):
      # retorna a media dos preços dos ultimos 365 dias de bolsa
      media = 0 
      for i in range(int(numColunas), int(numColunas) - 365, -1):
          media = float(tsla_df.loc[i,'high']) + media
      return (media/365)

#TODO metodo que devolve o valor medio da ação no min de 7 dias, 15 dias, 30 dias, 60 , 90 , 180, 365 CHECK
def precoMinSete(numColunas):
          # retorna a media dos preços dos ultimos 7 dias de bolsa
      media = 0 
      for i in range(int(numColunas), int(numColunas) - 7, -1):
          media = float(tsla_df.loc[i,'low']) + media 
          
      return  (media/7)
def precoMinQuinze(numColunas):
      # retorna a media dos preços dos ultimos 15 dias de bolsa
      media = 0 
      for i in range(int(numColunas), int(numColunas) - 15, -1):
          media = float(tsla_df.loc[i,'low']) + media
      return (media/15)
def precoMinTrinta(numColunas):
      # retorna a media dos preços dos ultimos 30 dias de bolsa
      media = 0 
      for i in range(int(numColunas), int(numColunas) - 30, -1):
          media = float(tsla_df.loc[i,'low']) + media
      return (media/30)     
def precoMinSessenta(numColunas):
      # retorna a media dos preços dos ultimos 60 dias de bolsa
      media = 0 
      for i in range(int(numColunas), int(numColunas) - 60, -1):
          media = float(tsla_df.loc[i,'low']) + media
      return (media/60)
def precoMinNoventa(numColunas):
      # retorna a media dos preços dos ultimos 90 dias de bolsa
      media = 0 
      for i in range(int(numColunas), int(numColunas) - 90, -1):
          media = float(tsla_df.loc[i,'low']) + media
      return (media/90)
def precoMinCentoOitenta(numColunas):
      # retorna a media dos preços dos ultimos 180 dias de bolsa
      media = 0 
      for i in range(int(numColunas), int(numColunas) - 180, -1):
          media = float(tsla_df.loc[i,'low']) + media
      return (media/180)
def precoMinTrezentosSessenta(numColunas):
      # retorna a media dos preços dos ultimos 365 dias de bolsa
      media = 0 
      for i in range(int(numColunas), int(numColunas) - 365, -1):
          media = float(tsla_df.loc[i,'low']) + media
      return (media/365)

#pega a data atual
dataAtual = date.today()
print(dataAtual)

#abre cursor para mandar informação para o db
my_cursor = mydb.cursor()

# pega o nome do Ticker
acao = input()

#pega o historico de valores do Ticker passado 
yahoo_financials = YahooFinancials(acao)
data = yahoo_financials.get_historical_price_data(start_date='2000-01-01', 
                                                  end_date=str(dataAtual), 
                                                  time_interval='daily')
tsla_df = pd.DataFrame(data[acao]['prices'])

#print(tsla_df)
#print(tsla_df.loc[5474,'high'])

numColunas = str(tsla_df.tail(1)).split()[8]

preco = float(tsla_df.loc[int(numColunas),'close'])
preco_abertura = float(tsla_df.loc[int(numColunas),'open'])
preco_max = float(tsla_df.loc[int(numColunas),'high'])
preco_min = float(tsla_df.loc[int(numColunas),'low'])
volume = float(tsla_df.loc[int(numColunas),'volume'])
preco_sete = precoSete(numColunas)
preco_sete_max = precoHighSete(numColunas)
preco_sete_min = precoMinSete(numColunas)
preco_quinze = precoQuinze(numColunas)
preco_quinze_max = precoHighQuinze(numColunas)
preco_quinze_min = precoMinQuinze(numColunas)
preco_trinta = precoTrinta(numColunas)
preco_trinta_max = precoHighTrinta(numColunas)
preco_trinta_min = precoMinTrinta(numColunas)
preco_sessenta = precoSessenta(numColunas)
preco_sessenta_max = precoHighSessenta(numColunas)
preco_sessenta_min = precoMinSessenta(numColunas)
preco_noventa = precoNoventa(numColunas)
preco_noventa_max = precoHighNoventa(numColunas)
preco_noventa_min = precoMinNoventa(numColunas)
preco_cento_oitenta = precoCentoOitenta(numColunas)
preco_cento_oitenta_max = precoHighCentoOitenta(numColunas)
preco_cento_oitenta_min = precoMinCentoOitenta(numColunas)
preco_trezentos_sessenta = precoTrezentosSessenta(numColunas)
preco_trezentos_sessenta_max = precoHighTrezentosSessenta(numColunas)
preco_trezentos_sessenta_min = precoMinTrezentosSessenta(numColunas)

acaoConstrutor = "INSERT INTO acao (name, precoatual, precoatualopen, precoatualmax, precoatualmin, volume, precosete, precosetehigh, precosetemin, precoquinze, precoquinzehigh, precoquinzemin, precotrinta, precotrintahigh, precotrintamin, precosessenta, precosessentahigh, precosessentamin, preconoventa, preconoventahigh, preconoventamin, precocentoitenta, precocentoitentahigh, precocentoitentamin, precotrezentosssenta, precotrezentosssentahigh, precotrezentosssentamin) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
acaoValores = (acao, preco, preco_abertura, preco_max, preco_min, volume, preco_sete, preco_sete_max, preco_sete_min, preco_quinze, preco_quinze_max, preco_quinze_min, preco_trinta, preco_trinta_max, preco_trinta_min, preco_sessenta, preco_sessenta_max, preco_sessenta_min, preco_noventa, preco_noventa_max, preco_noventa_min, preco_cento_oitenta, preco_cento_oitenta_max, preco_cento_oitenta_min, preco_trezentos_sessenta, preco_trezentos_sessenta_max, preco_trezentos_sessenta_min)
my_cursor.execute(acaoConstrutor,acaoValores)
mydb.commit()

