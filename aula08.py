"""import datetime 

x = datetime.datetime.now()
print(x)

print(x.year)
print(x.strftime("%C"))
"""

#Exercícios simples com datetime
#1. Importe o módulo datetime.
import datetime
#2. Imprima a data e hora atual.
x= datetime.datetime.now()
print(x)
#3. Imprima apenas a data atual (sem o horário).
x = datetime.date.today()
print(x)
#4. Imprima apenas a hora atual.
x = datetime.datetime.now().time()
print(x)

#5. Crie uma variável que armazene a data e hora atual.
data = datetime.datetime.now()
#6. Imprima o ano atual.
print(data.year)
#7. Imprima o mês atual.
print(data.month)
#8. Imprima o dia atual.
print(data.day)
#9. Imprima a hora atual.
print(data.hour)
#10. Imprima os minutos atuais.
print(data.minute)
#11. Imprima os segundos atuais.
print(data.second)
#12. Crie uma data personalizada (ano, mês, dia) usando datetime.datetime.
data = datetime.datetime(2010, 10, 10)
print(data)
#13. Crie uma data e hora personalizada (ano, mês, dia, hora, minuto, segundo).
data = datetime.datetime(2010,10,10,23,59,59)
print(data)
#14. Converta uma data para o formato de string (ex: "YYYY-MM-DD").
data = datetime.datetime.now()
data_formatada = data.strftime('%Y-%m-%d')
print(data_formatada)
#15. Converta um horário para o formato de string (ex: "HH:MM:SS").
hora_formatada = data.strftime('%H:%M:%S')
print(hora_formatada)
#16. Adicione 5 dias à data atual.
nova_data = data + datetime.timedelta(days=5)
print(nova_data)
#17. Subtraia 10 dias da data atual.
nova_data = data + datetime.timedelta(days=-10)
print(nova_data)
#18. Adicione 3 horas ao horário atual.
nova_data = data + datetime.timedelta(hours=3)
print(nova_data)
#19. Subtraia 30 minutos do horário atual.
nova_data = data + datetime.timedelta(minutes=-30)
print(nova_data)
#20. Converta uma string de data "2024-12-03" em um objeto datetime.
data_str = "2024-12-03"

data_objeto = datetime.datetime.strptime(data_str, '%Y-%m-%d')
print(data_objeto)