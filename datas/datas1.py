from datetime import datetime

data = datetime(2023, 1, 20)
data_hora = datetime(2023, 1, 20, 14, 25, 30)

print(data)
print(data_hora)

data_str = '20/04/2022 07:15:55'
data_str_fmt = '%d/%m/%Y %H:%M:%S'
data_formatada = datetime.strptime(data_str, data_str_fmt)
print(data_formatada)