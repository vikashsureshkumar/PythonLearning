import decimal
import multiprocessing
from multiprocessing import Process
from multiprocessing import Pool
import time
import numpy

from CSVAdapter import CSVAdapter
from Database import Database
from InterfaceConvertor import InterfaceConvertor

import pandas as pd
import os
import json
from glob import glob
import csv
import requests
import sqlite3

from JSONAdapter import JSONAdapter
from XMLAdapter import XMLAdapter


def conversionFactor(tupler):
    url = 'https://api.exchangerate-api.com/v4/latest/' + tupler['toCurrency']
    r = requests.get(url=url, params={})
    data = r.json()
    if 'error_type' in data:
        print('Conversion from ' + tupler['fromCurrency'] + 'to ' + tupler['toCurrency'] + ' is un-supported')
        tupler['status'] = 'not_converted'
    else:
        tupler['convertedRateAt'] = decimal.Decimal(round(decimal.Decimal(data['rates'][str(tupler['fromCurrency'])]), 2))
        tupler['convertedAmount'] = decimal.Decimal(round(decimal.Decimal(tupler['amount']) / decimal.Decimal(tupler['convertedRateAt']), 2))
        tupler['status'] = 1
    return tupler

def getAllTransactionRequests(path):
    allTransactionRequests = []

    csv_files = numpy.array(Convertor(CSVAdapter()).convertor(path))
    json_files = numpy.array(Convertor(XMLAdapter()).convertor(path))
    xml_files = numpy.array(Convertor(JSONAdapter()).convertor(path))

    allTransactionRequests.append(TransactionRequest(CSVAdapter()).transactionRequests(csv_files))

    return allTransactionRequests


class Convertor(object):

    def convertor(self, path):
        return self._convertor.conversion(path)

    def __init__(self, convertor):
        self._convertor = convertor


class TransactionRequest(object):

    def transactionRequests(self, files):
        return self._transactionRequests.getTransactionRequests(files)

    def __init__(self,  transactionRequests):
        self._transactionRequests = transactionRequests



if __name__ == "__main__":
    csv_folder_path = '/Users/vikash/Downloads/TransferMateAssignment/PythonTask/internalFormats/'
    allTransactionRequests = getAllTransactionRequests(csv_folder_path)
    InStoreUpdater = []
    db = Database()
    for fileTypeData in allTransactionRequests:
        for fileData in fileTypeData:
            InStoreUpdater.append(conversionFactor(fileData))
    db.storeItInMemoryDatabase(InStoreUpdater)
    # print('allTransactionRequests', allTransactionRequests)
