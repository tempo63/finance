from cs50 import SQL


db = SQL("sqlite:///finance.db")

check = db.execute('SELECT SUM(qty) FROM txn WHERE stock_name="AAPL"')

print(check)
