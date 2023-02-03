import sqlite3
import decimal


class Database(object):

    def storeItInMemoryDatabase(self,allTransactionRequests):
        inserter = []
        for request in allTransactionRequests:
            inserter.append((request['transactionId'], request['fromCurrency'], request['toCurrency'], str(request['amount']), request['file_name'],
                             str(request['convertedRateAt']), str(request['convertedAmount']), request['status']))
        print("inserter", inserter)
        self.conn.execute("Drop Table if exists transactions")
        self.conn.execute("CREATE TABLE `transactions` (`id` INTEGER PRIMARY KEY NOT NULL, `trx_id` INTEGER NOT NULL , `from_currency` VARCHAR(20) NOT NULL , `to_currency` VARCHAR(20) NOT NULL , `amount` VARCHAR(2000) NOT NULL , `file_name` VARCHAR(100) NOT NULL , `converted_rate_at` VARCHAR(2000) NOT NULL , `converted_amount` VARCHAR(2000) NOT NULL , `status` INTEGER NOT NULL )")
        self.conn.executemany("Insert into transactions (trx_id,from_currency,to_currency,amount,file_name,converted_rate_at,converted_amount,status) VALUES (?,?,?,?,?,?,?,?)", inserter)
        self.conn.commit()
        cursor = self.conn.execute("select * from transactions")
        print("cursor", cursor)
        for row in cursor:
            print("row", row)
        self.conn.close()

    def __init__(self):
        self.conn = sqlite3.connect('currency_converter.db')
        print("Opened database successfully")
