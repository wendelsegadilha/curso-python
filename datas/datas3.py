from datetime import datetime

"""
LINUX EPHOC
"""
data = datetime.now()
timestamp_atual = data.timestamp()

print(data)
print(timestamp_atual)

timestamp_to_date = datetime.fromtimestamp(timestamp_atual)

print(timestamp_to_date)
