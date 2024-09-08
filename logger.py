from data_create import name_data, surname_data, phone_data, address_data




def input_data():
    name = name_data()
    surname = surname_data()
    phone = phone_data()
    address = address_data()
    var = int(input(f"В каком формате записать данные?\n\n"
    f"1 Вариант: \n"
    f"{name}\n{surname}\n{phone}\n{address}\n\n"
    f"2 Вариант: \n"
    f"{name};{surname};{phone};{address}\n\n"                
    f"Выберите вариант: "))
    
    while var !=1 and var != 2:
        print("Неправильный ввод")
        var = int(input("Введите число: "))
        
    if var == 1:
        with open('data_first_variant.csv','a',encoding='utf-8') as f:
            f.write(f"{name}\n{surname}\n{phone}\n{address}\n\n")
    elif var == 2:
        with open('data_second_variant.csv','a',encoding='utf-8') as f:
            f.write(f"{name};{surname};{phone};{address}\n\n")
      
            
def print_data():
    print("Вывожу данные из первого файла:\n")
    with open('data_first_variant.csv','r',encoding='utf-8') as f:
        data_first = f.readlines()
        data_first_list =[]
        j = 0
        for i in range(len(data_first)):
            if data_first[i]=='\n' or i==len(data_first) - 1:
                data_first_list.append(''.join(data_first[j:i + 1]).rstrip('\n') + '\n' + '\n')
                j=i+1
        print(''.join(data_first_list))
    print("Вывожу данные из второго файла:\n")    
    with open('data_second_variant.csv','r',encoding='utf-8') as f:
        data_second = f.readlines()
        print(*data_second)
      
        
def change_data():
    number = int(input("Введите номер списка, в котором нужно внести изменения: "))
    
    while number !=1 and number !=2:
        print("Неправильный ввод")
        number = int(input("Введите номер списка, в котором нужно внести изменения: "))
        
    if number == 1:
    
        number_record = int(input("Введите номер записи, которую нужно изменить: "))
        with open('data_first_variant.csv','r',encoding='utf-8') as f:
            data_first = f.readlines()
            data_first_list =[]
            j = 0
            for i in range(len(data_first)):
                if data_first[i]=='\n' or i==len(data_first) - 1:
                    data_first_list.append(''.join(data_first[j:i + 1]).rstrip('\n') + '\n' + '\n')
                    j=i+1
    
        while number_record > len(data_first_list) and number_record !=0:
            print("Нет такой записи")
            number_record = int(input("Введите номер записи, которую нужно изменить: "))
        
        data_first_list_change =[]
        for i in range(number_record):
            data_first_list_change.append(data_first_list[i])       
        with open('data_first_variant.csv','w',encoding='utf-8') as f:    
            f.write(''.join(data_first_list_change[:number_record-1]))#записана первая часть в список
                   
        name = name_data()
        surname = surname_data()
        phone = phone_data()
        address = address_data()
        with open('data_first_variant.csv','a',encoding='utf-8') as f:
            f.write(f"{name}\n{surname}\n{phone}\n{address}\n\n")  #изменен элемент
        
        data_first_list_change1 =[]    
        for i in range(number_record,len(data_first_list)):
            data_first_list_change1.append(data_first_list[i])       
        with open('data_first_variant.csv','a',encoding='utf-8') as f:    
            f.write(''.join(data_first_list_change1[:len(data_first_list)])) #записан хвост списка     
           
    elif number == 2:             
        
        number_record = int(input("Введите номер записи, которую нужно изменить: "))
        with open('data_second_variant.csv','r',encoding='utf-8') as f:
            data_second = f.readlines()
            data_second_list =[]
            j = 0
            for i in range(len(data_second)):
                if data_second[i]=='\n' or i==len(data_second) - 1:
                    data_second_list.append(''.join(data_second[j:i + 1]).rstrip('\n') + '\n' + '\n')
                    j=i+1
        while number_record > len(data_second_list) and number_record !=0:
            print("Нет такой записи")
            number_record = int(input("Введите номер записи, которую нужно изменить: "))
                      
        data_second_list_change =[]
        for i in range(number_record):
            data_second_list_change.append(data_second_list[i])       
        with open('data_second_variant.csv','w',encoding='utf-8') as f:    
            f.write(''.join(data_second_list_change[:number_record-1]))#записана первая часть в список
                   
        name = name_data()
        surname = surname_data()
        phone = phone_data()
        address = address_data()
        with open('data_second_variant.csv','a',encoding='utf-8') as f:
            f.write(f"{name};{surname};{phone};{address}\n\n")  #изменен элемент          
        
        data_second_list_change1 =[]    
        for i in range(number_record,len(data_second_list)):
            data_second_list_change1.append(data_second_list[i])       
        with open('data_second_variant.csv','a',encoding='utf-8') as f:    
            f.write(''.join(data_second_list_change1[:len(data_second_list)])) #записан хвост списка 
                
 
def delete_data():
    
    number = int(input("Введите номер списка, в котором нужно внести изменения: "))
    
    while number !=1 and number !=2:
        print("Неправильный ввод")
        number = int(input("Введите номер списка, в котором нужно внести изменения: "))
        
    if number == 1:
    
        number_record = int(input("Введите номер записи, которую нужно удалить: "))
        with open('data_first_variant.csv','r',encoding='utf-8') as f:
            data_first = f.readlines()
            data_first_list =[]
            j = 0
            for i in range(len(data_first)):
                if data_first[i]=='\n' or i==len(data_first) - 1:
                    data_first_list.append(''.join(data_first[j:i + 1]).rstrip('\n') + '\n' + '\n')
                    j=i+1
    
        while number_record > len(data_first_list) and number_record !=0:
            print("Нет такой записи")
            number_record = int(input("Введите номер записи, которую нужно удалить: "))
            
        data_first_list.pop(number_record-1)    
        with open('data_first_variant.csv','w',encoding='utf-8') as f:    
            f.write(''.join(data_first_list))
        
    elif number == 2:
            
        number_record = int(input("Введите номер записи, которую нужно удалить: "))
        with open('data_second_variant.csv','r',encoding='utf-8') as f:
            data_second = f.readlines()
            data_second_list =[]
            j = 0
            for i in range(len(data_second)):
                if data_second[i]=='\n' or i==len(data_second) - 1:
                    data_second_list.append(''.join(data_second[j:i + 1]).rstrip('\n') + '\n' + '\n')
                    j=i+1
        while number_record > len(data_second_list) and number_record !=0:
            print("Нет такой записи")
            number_record = int(input("Введите номер записи, которую нужно удалить: "))
            
        data_second_list.pop(number_record-1)    
        with open('data_second_variant.csv','w',encoding='utf-8') as f:    
            f.write(''.join(data_second_list))