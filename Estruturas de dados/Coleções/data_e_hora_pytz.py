# import pytz
# from datetime import datetime

# criando datetime com timezone
# data = datetime.now(pytz.timezone("Europe/Oslo"))
# print(data)

# uando timezone sem biblioteca externa
from datetime import datetime, timezone, timedelta

data_oslo = datetime.now(timezone(timedelta(hours=2)))
data_sao_paulo = datetime.now(timezone(timedelta(hours=-3)))

print(data_oslo)
print(data_sao_paulo)
