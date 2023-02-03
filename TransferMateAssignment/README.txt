Project link : https://drive.google.com/drive/folders/1edcf1KJkE9icp5jJ2ugT77Pt3iDosWDB?usp=sharing
^ this will have the entire project with all csv files whose records are around 1 and 5 million

please download the above files
In sales_records place -> 130k1, 130k2, 130k3, 130k4, 130k5

The Assessment Project consist of two task
1. Pandas Task
2. Python Task

1. Pandas Task:
   To use of variety of functionalities around pandas to get the desired output

   folders and its uses:
        1. csvConvertedFiles   -> this will contain csv files, which are grouped into single csv based on the input extension file.
                                  if you have 2 csv and 1 json file, then this folder will have 2 csv file, where 2 csv is combined into single one based on its internal column match and other one is json file as 1 csv file
        2. json_folder         -> this will contain all json file and a txt file to check if that file is being parsed or not while reading only json files from a folder
        3. sales_record_output -> this will contain a single csv file where it has 5millions rows which are obtained from merging five 1 million record csv
        4. sales_record        -> this will have the five 1 million record csv which needs to be combined into a single csv file

   files and its uses:
        1. 1millionTo5million.py -> this will merge input csv files and output single csv file
        2. jsonToCsv.py          -> converts json to csv file

   To run:
        1. python3 1millionTo5million.py
        2. python3 jsonToCsv.py

2. Python Task:
   To use variety of functional requirement to get the desired output

   folder and its uses:
        1. internalFormats:
            1. convertedFiles -> testing folder to convert al processed files into a single format files
            2. formatOne -> this contains csv, json, xml all having same format data
            3. formatThree -> this contains csv, json, xml all having same format data
            4. formatTwo -> this contains csv, json, xml all having same format data

   files and its uses:
        1. Convertor.py             -> main file to run
        2. CSVAdapter.py            -> adapter sub file to convert to csv file
        3. Database.py              -> to initialize orm and use it for db related operations
        4. InterfaceConvertor.py    -> interface class file to utilize functionality
        5. JSONAdapter.py           -> adapter sub file to convert from json to csv file
        6. XMLAdapter.py            -> adapter sub file to convert from xml to csv file
        7. currency_convertor.py    -> this is the database which has all converted data which is stored by orm using sql lite3

   To run:
        1. python3 convertor.py




