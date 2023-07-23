from datetime import datetime

"""
Formantando data e hora do formato americano para o brasileiro
"""
fmt = '%d/%m/%Y %H:%M:%S'
data = datetime.strptime('2023-01-13 07:53:32', '%Y-%m-%d %H:%M:%S')
print(data)

data_formatada = data.strftime(fmt)
print(data_formatada)