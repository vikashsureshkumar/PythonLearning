import pandas as pd
import os
csv_path = '/Users/vikash/Downloads/TransferMateAssignment/PandasTask/sales_records/'

total_length = 0
all_files = []
for file_name in [file for file in os.listdir(csv_path) if file.endswith('.csv')]:
    all_files.append(str(csv_path + file_name))
data_frame = pd.concat(map(pd.read_csv, all_files), ignore_index=True)
data_frame.to_csv('/Users/vikash/Downloads/TransferMateAssignment/PandasTask/sales_record_output/649855_Rows.csv', index=False)

