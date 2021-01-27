import os
import pandas as pd

path = os.getcwd()

location_counts_df = pd.read_excel(path+'/location_count.xlsx', index_col = 0, engine='openpyxl')
location_df = pd.read_excel(path+'/locations.xlsx', engine='openpyxl')

location_data = pd.merge(location_df, location_counts_df,
                         how = 'inner', left_on = '장소', right_index=True)

print(location_data)
