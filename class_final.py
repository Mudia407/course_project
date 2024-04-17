import sqlite3

#Create a connection to the database
conn = sqlite3.connect('example.db')

#Create a cursor
data = conn.cursor()

#var transaction_data, transaction_type, symbol, qty, price

#Create a table
data.execute('''CREATE TABLE IF NOT EXISTS stocks 
             (date text, trans text, symbol text, qty real, price real)''') 

#Insert a row of data 

data.execute("INSERT INTO stocks VALUES stock_date, 'BUY', 'AAPL', 100, 167.78)")

#Save (connit) the changes 
conn.commit() 

#Query the database 
data.execute('SELECT * FROM stocks')

#Print the results 
for row in data.fetchall(): 
    print (row) 
    
#Close the connection 
conn.close() 