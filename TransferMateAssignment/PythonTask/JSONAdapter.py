import os
from glob import glob

from InterfaceConvertor import InterfaceConvertor


class JSONAdapter(InterfaceConvertor):
    @staticmethod
    def conversion(json_path) -> str:
        return [file for (path, subdir, files) in os.walk(json_path) for file in glob(os.path.join(path, '*.json'))]


    @staticmethod
    def getTransactionRequests(all_csv_files_converted):
        transactionRequests = []
        for file in all_csv_files_converted:
            fileParts = str(file).split('/')
            file_name = fileParts[len(fileParts) - 1]
            typeOfFile = str(file_name).split('.')[1]

        return transactionRequests
