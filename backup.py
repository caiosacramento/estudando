import pandas as pd  
from yahoofinancials import YahooFinancials
import mysql.connector
from datetime import date 


#mydb = mysql.connector.connect(
      #host = "localhost",
      #user = "root",
      #database = "testdb",
#)

dataAtual = date.today()
print(dataAtual)
#my_cursor = mydb.cursor()
acao = input()
yahoo_financials = YahooFinancials(acao)
#data = yahoo_financials.get_stock_price_data()

data = yahoo_financials.get_historical_price_data(start_date='2000-01-01', 
                                                  end_date=str(dataAtual), 
                                                  time_interval='weekly')

#print(data)

#data = yahoo_financials.get_current_price()
tsla_df = pd.DataFrame(data[acao]['prices'])
print(tsla_df)
print(tsla_df.loc[3,'high'])
#tsla_df = tsla_df.drop('date', axis=1).set_index('formatted_date')
#tsla_df.head()
#print(data)
#print(tsla_df)


#for valor in tsla_df:
      #print(valor)
#acaoValor = "INSERT INTO mercado (name, valor) VALUES(%s,%s)"
#testando = (acao, data)
#my_cursor.execute(acaoValor,testando)
#mydb.commit()
#criar uma classe nova pra buscar esses dados a cada 30 minutos
#salvar informações no bd