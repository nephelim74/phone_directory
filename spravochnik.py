import tkinter as tk
from tkinter import * 
from tkinter import messagebox
import csv
from tkinter import simpledialog
import subprocess



def read_txt(filename): 
    phone_book=[]
    fields=['Фамилия', 'Имя', 'Телефон', 'Описание']
    with open(filename,'r',encoding='utf-8') as phb:
        for line in phb:
            line = line.replace("\n","")
            record = dict(zip(fields, line.split(',')))
			#dict(( (фамилия,Иванов),(имя, Точка),(номер,8928) ))
            # print(record)
            phone_book.append(record)	
    return phone_book

def read_txt(filename): 
    phone_book=[]
    fields=['Фамилия', 'Имя', 'Телефон', 'Описание']
    with open(filename,'r',encoding='utf-8') as phb:
        for line in phb:
            line = line.replace("\n","")
            record = dict(zip(fields, line.split(',')))
			#dict(( (фамилия,Иванов),(имя, Точка),(номер,8928) ))
            # print(record)
            phone_book.append(record)	
    return phone_book

def find_by_subscr(phone_book, value , flag):
    if flag == 0: print('Поиск по Фамилии')
    else: print('Поиск по Номеру')
    for i in range(0, len(phone_book)):
        
        # print(f'{int([m for m in phone_book[i].values()][flag])} {int(value)}')
        # print(value)
        if [m for m in phone_book[i].values()][flag] == value:
            res = '--------------------\n'
            for teg1, teg2 in phone_book[i].items():
                
                res =  f'{res} {teg1}: {teg2} \n'
            res = f'{res} --------------------\n'
    if res == '': res = 'Абонент не найден \n' 
    # print(res)
    return res     

def find_by_subscr(phone_book, value , flag):
    if flag == 0: print('Поиск по Фамилии')
    else: print('Поиск по Номеру')
    for i in range(0, len(phone_book)):
        
        # print(f'{int([m for m in phone_book[i].values()][flag])} {int(value)}')
        # print(value)
        if [m for m in phone_book[i].values()][flag] == value:
            res = '--------------------\n'
            for teg1, teg2 in phone_book[i].items():
                
                res =  f'{res} {teg1}: {teg2} \n'
            res = f'{res} --------------------\n'
    if res == '': res = 'Абонент не найден \n' 
    # print(res)
    return res  
   
def add_new_suscriber(subscriber_data, phone_book):
    fields=['Фамилия', 'Имя', 'Телефон', 'Описание']
    record = dict(zip(fields, subscriber_data))
    # phone_book.append(record)
    # print(''.join(phone_book))
    for ph_dic in phone_book:
        for teg1, teg2 in ph_dic.items():
            print(f'{teg1}: {teg2}')
        print("------")
    # print(phone_book)
    return record

def read_txt(filename): 
    phone_book=[]
    fields=['Фамилия', 'Имя', 'Телефон', 'Описание']
    with open(filename,'r',encoding='utf-8') as phb:
        for line in phb:
            line = line.replace("\n","")
            record = dict(zip(fields, line.split(',')))
			#dict(( (фамилия,Иванов),(имя, Точка),(номер,8928) ))
            # print(record)
            phone_book.append(record)	
    return phone_book

def write_txt(filename , phone_book):
    with open(filename,'w',encoding='utf-8') as phout:
        for i in range(len(phone_book)):
            s=''
            for v in phone_book[i].values():
                print(v)
                s = s + v + ','
            phout.write(f'{s[:-1]}\n')
            
def copy_to_file(in_file, out_file):
    bd_tel = open(in_file,"r", encoding='utf-8')
    out_csv = open(out_file, "w", encoding='utf-8')

    line_count = 0
    for line in bd_tel:
        if line != "\n":

            print(line)
            out_csv.write(line)
            line_count += 1

    bd_tel.close()
    out_csv.close()
    return f'Cформирован файл {out_file}'


def get_bd():
    text.delete(1.0, END)
    # s = read_txt(filename)
    s = phone_book
    # text.insert(10.0, s)
    # Фамилия,Имя,Телефон,Описание
    count=1
    for i in s:
        for j, k in i.items():
            if (k == 'Фамилия') or (k == 'Имя') or (k == 'Телефон') or (k == 'Описание'):
                continue
            else:
                text.insert(10.0, f'{j} : {k} \n' )
                # text.insert('-------------------- \n')
                count +=1
 
 
def find_suscr():
    text.delete(1.0, END)
    last_name = simpledialog.askstring(title="Ввод Фамилии",
                                  prompt="Введите фамилию абонента:")
    result = find_by_subscr(phone_book,last_name, 0)
    text.insert(10.0, result )
    
def find_num():
    text.delete(1.0, END)
    num = simpledialog.askstring(title="Ввод Номера",
                                  prompt="Введите Номер телефона:")
    result = find_by_subscr(phone_book, num, 2)
    text.insert(10.0, result )
def add_new_subscr():
    text.delete(1.0, END)
    subscriber_data = []
    fields=['Фамилия', 'Имя', 'Телефон', 'Описание']
    for i in range(0,4):
        subscriber_data.append(str(simpledialog.askstring(title="Ввод" + fields[i],
                                  prompt="Введите " + fields[i] + ":")))
            
    text.insert(10.0, subscriber_data ) 
    phone_book.append(add_new_suscriber(subscriber_data, phone_book))      

def save_data():
    text.delete(1.0, END)
    write_txt(filename, phone_book)
    s = read_txt(filename)
    count=1
    for i in s:
        for j, k in i.items():
            if (k == 'Фамилия') or (k == 'Имя') or (k == 'Телефон') or (k == 'Описание'):
                continue
            else:
                text.insert(10.0, f'{j} : {k} \n' )
                # text.insert('-------------------- \n')
                count +=1


            # out_file=input('Ведите название файла: ')
            # print(copy_to_file('phonebook.txt', out_file))
            
def export_to_file():
    out_file = simpledialog.askstring(title="Экспорт",
                                  prompt="Введите название файла:")
    copy_to_file(filename, out_file)
    subprocess.run(["notepad",out_file])

def game_over():
    root.quit()
    root.destroy()


root = Tk()
 
text = Text(width=50, height=10)
text.pack(side=LEFT)
 
scroll = Scrollbar(command=text.yview)
scroll.pack(side=LEFT, fill=Y)
 
text.config(yscrollcommand=scroll.set)

frame = Frame()
frame.pack()
Button(frame, text="Отобразить весь справочник",
       command=get_bd).pack(side=TOP)
Button(frame, text="Найти абонента по фамилии",
       command=find_suscr).pack(side=TOP)
Button(frame, text="Найти абонента по номеру",
       command=find_num).pack(side=TOP)
Button(frame, text="Добавить абонента в справочник",
       command=add_new_subscr).pack(side=TOP)
Button(frame, text="Сохранить в БД",
       command=save_data).pack(side=TOP)
Button(frame, text="Эксорт в файл",
       command=export_to_file).pack(side=TOP)
Button(frame, text="Выход",
       command=game_over).pack(side=TOP)
filename = 'phonebook.txt'
phone_book=read_txt(filename) 
label = Label()
label.pack()
 
root.mainloop()
