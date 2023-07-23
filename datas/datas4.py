from datetime import datetime, timedelta

data_fmt = '%d/%m/%Y %H:%M:%S'
data_inicio = datetime.strptime('20/04/2022 07:15:55', data_fmt)
data_fim = datetime.strptime('05/06/2022 08:00:49', data_fmt)

print(data_fim > data_inicio)

delta = data_fim - data_inicio
print(delta)
delta = delta + timedelta(days=10,hours=0, seconds=0)
print(delta)
segundos = delta.total_seconds()
print(segundos)
