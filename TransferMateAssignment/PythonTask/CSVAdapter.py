import csv
import decimal
import os
from glob import glob

from InterfaceConvertor import InterfaceConvertor


class CSVAdapter(InterfaceConvertor):
    @staticmethod
    def conversion(csv_path):
        return [file for (path, subdir, files) in os.walk(csv_path) for file in glob(os.path.join(path, '*.csv'))]

    @staticmethod
    def getTransactionRequests(all_csv_files_converted):
        transactionRequests = []
        for file in all_csv_files_converted:
            fileParts = str(file).split('/')
            file_name = fileParts[len(fileParts) - 1]

            with open(file) as csvfile:
                delimiter = csv.Sniffer().sniff(csvfile.read(1024))
                csvfile.seek(0)
                csv_reader = csv.reader(csvfile, delimiter)
                for row in csv_reader:
                    if str(row[0]) not in ['TrxId', 'ID']:
                        transactionRequests.append({
                            'file_name': str(file_name),
                            'transactionId': int(row[0]),
                            'fromCurrency': str(row[1]),
                            'toCurrency': str(row[2]),
                            'amount': round(decimal.Decimal(row[3]), 2),
                            'convertedRateAt': 0,
                            'convertedAmount': 0,
                            'status': 0,
                        })
        return transactionRequests
