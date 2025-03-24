import datetime

# criando data e hora
d = datetime.datetime(2023, 7, 19, 13, 46)
print(d)

# adicionando uma semana
d = d + datetime.timedelta(weeks=1)
print(d)

from datetime import timedelta, datetime, date

tipo_carro = 'M' # P, M, G
tempo_pequeno = 30
tempo_medio = 45
tempo_grande = 60
data_atual = datetime.now()

if tipo_carro == 'P':
    data_estimada = data_atual + timedelta(minutes=tempo_pequeno)
    print(f"Entrada:{data_atual}")
    print(f"Saída:{data_estimada}")
elif tipo_carro == 'M':
    data_estimada = data_atual + timedelta(minutes=tempo_medio)
    print(f"Entrada:{data_atual}")
    print(f"Saída:{data_estimada}")
else:
    data_estimada = data_atual + timedelta(minutes=tempo_grande)
    print(f"Entrada:{data_atual}")
    print(f"Saída:{data_estimada}")

print(date.today() - timedelta(days=1))

resultado = datetime(2023, 7, 25, 10, 19, 20) - timedelta(hours=1)
print(resultado.time())
print(datetime.now().date())