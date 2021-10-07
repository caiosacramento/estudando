#from yahoo_finance import Share
#import time
#stock = Share('MSFT')
#stock.refresh()
#stock.get_price()
#print (stock)

from yahoo_finance import Share
yahoo = Share('YHOO')
print (yahoo.get_open())  