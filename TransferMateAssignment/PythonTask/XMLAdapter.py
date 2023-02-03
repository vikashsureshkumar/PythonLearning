import os
from glob import glob

from InterfaceConvertor import InterfaceConvertor


class XMLAdapter(InterfaceConvertor):
    @staticmethod
    def conversion(xml_path) -> str:
        return [file for (path, subdir, files) in os.walk(xml_path) for file in glob(os.path.join(path, '*.xml'))]

    @staticmethod
    def getTransactionRequests(all_csv_files_converted):
        transactionRequests = []
        for file in all_csv_files_converted:
            fileParts = str(file).split('/')
            file_name = fileParts[len(fileParts) - 1]
            typeOfFile = str(file_name).split('.')[1]

        return transactionRequests

