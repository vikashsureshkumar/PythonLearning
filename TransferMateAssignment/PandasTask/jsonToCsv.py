import pandas as pd
import os,json

json_path = '/Users/vikash/Downloads/TransferMateAssignment/PandasTask/json_folder/'

data_dictionary = {}
for file_name in [file for file in os.listdir(json_path) if file.endswith('.json')]:
  with open(json_path + file_name) as json_file:
    data = json.load(json_file)
    try:
        data_dictionary[str(list(data.keys()))].append(data)
    except:
        data_dictionary[str(list(data.keys()))] = [data]

counter = 1
data_frame = pd.DataFrame()
frames = []
for data_dict in data_dictionary:
    for i in range(0, len(data_dictionary[data_dict])):
        if frames:
            frames.append(pd.DataFrame(data_dictionary[data_dict][i]))
        else:
            frames = [pd.DataFrame(data_dictionary[data_dict][i])]
    pd.json_normalize(frames)
    data_frame = pd.concat(frames, ignore_index=True)
    data_frame.to_csv('/Users/vikash/Downloads/TransferMateAssignment/PandasTask/csvConvertedFiles/csvOutputFile' + str(counter) +'.csv')
    counter += 1
    frames = []
