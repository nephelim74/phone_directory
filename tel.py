

def work_with_phonebook():
    choice=show_menu()
    phone_book=read_txt('phonebook.txt')
    while (choice!=7):
        if choice==1:
            print_result(phone_book)
        elif choice==2:
            last_name=input('Введите Фаилию абонента: ')
            print(find_by_subscr(phone_book,last_name, 0))
        elif choice==3:
            tel_number=input('Введите номер телефона: ')
            print(find_by_subscr(phone_book,tel_number, 2))
        elif choice==4:
            subscriber_data = []
            fields=['Фамилия', 'Имя', 'Телефон', 'Описание']
            for i in range(0,4):
               subscriber_data.append(str(input(f'{fields[i]}')))
            # subscriber_data=input('Введите через запятую: Фамилию, Имя, номер телефона, Описание  ')
            phone_book.append(add_new_suscriber(subscriber_data, phone_book))
            # print(phone_book)
        # elif choice==5:
        #     number=input('number ')
        #     print(find_by_number(phone_book,number))
        elif choice==6:
            write_txt('phonebook.txt',phone_book)
        elif choice==7:
            choice = co_out()
        choice=show_menu()

def co_out():
    return 7

def print_result(phb):
    print("Телефонный справочник")
    fine_woll=''.join(list('-<>-' for i in range(0,10)))
    num = 1
    for ph_dic in phb:
        print(f' {num}  {fine_woll}')
        num += 1
        for teg1, teg2 in ph_dic.items():
            print(f'{teg1}: {teg2}')
        print(fine_woll)

def find_by_subscr(phone_book, value , flag):
    if flag == 0: print('Поиск по Фамилии')
    else: print('Поиск по Номеру')
    for i in range(0, len(phone_book)):
        
        # print([m for m in phone_book[i].values()][0])
        # print(value)
        if [m for m in phone_book[i].values()][flag] == value:
            res = '--------------------\n'
            for teg1, teg2 in phone_book[i].items():
                res =  f'{res} {teg1}: {teg2} \n'
            res = f'{res} --------------------\n'
        else: res = 'Абонент не найден \n' 
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


def show_menu():
    print("\nВыберите необходимое действие:\n"
          "1. Отобразить весь справочник\n"
          "2. Найти абонента по фамилии\n"
          "3. Найти абонента по номеру телефона\n"
          "4. Добавить абонента в справочник\n"
          "5. Сохранить отчет\n"
          "6. Сохранить в БД\n"
          "7. Закончить работу\n")
    choice = int(input())
    return choice

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

work_with_phonebook()
