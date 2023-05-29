import time
import csv


data = time.strftime("%d.%m.%Y - %H:%M:%S", time.localtime())
print('Дата создания заметки:', data)

with open('note.csv','w',newline= ';') as file:
    writer = csv.writer(file)