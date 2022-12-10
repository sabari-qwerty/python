import pandas as pd , os

input_path = input("input path: ").replace('\\', '/') 
output_path = input("output path: ").replace('\\', '/')
input_path =  input_path if input_path[-1] == '/' else f'{input_path}/'
output_path = output_path if input_path[-1] == '/' else f'{input_path}/'

for file in os.listdir(input_path):
    if ".xlsx" in  file:
        read_file = pd.read_excel(input_path + '/'+ file)
        read_file.to_csv(file[:-4] + 'csv', index=None, header=True)
        df = pd.DataFrame(output_path + pd.read_csv(file[:-4] + 'csv'))
        df
