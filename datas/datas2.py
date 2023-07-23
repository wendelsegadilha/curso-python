from datetime import datetime
from pytz import timezone

data_atual = datetime.now(timezone("America/Sao_Paulo"))
print(data_atual)
