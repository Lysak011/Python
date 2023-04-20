def show_data():
    with open('data.txt', 'r', encoding='UTF-8') as file:
        book = file.read()  # .split('\n')
    return book

def new_data():
    with open('data.txt', 'a', encoding='UTF-8') as file:
        data = input('Введите новую строку (Фамилия Имя, номер телефона, комментарий:) ')
        data += '\n'
        file.write(data)
        file.close()

def find_data():
    with open('data.txt', 'r', encoding='UTF-8') as file:
        book = file.read().split('\n')
        temp = input('Введите данные для поиска: ')
        for i in book:
            if temp in i:
                print(f'Вот кого мы нашли: -> {i} \n')
                file.close()

def delete_contact(name):
    with open('data.txt', 'r', encoding="UTF-8") as fr:
            lines = fr.readlines()
            with open('data.txt', 'w', encoding="UTF-8") as fw:
                for line in lines:
                    if line.strip('\n') != name:
                        fw.write(line)
    print("Готово, контакт удален!")

def edit_contact():
    with open('data.txt', 'r') as file:
        data = file.read()
        data = data.replace(search_text, replace_text)
        with open('data.txt', 'w') as file:
            file.write(data)
            file.close()

def spr_data():
    my_file = open('data.txt', 'w+')
    print('Создан новый справочник -> data.txt')



while True:
    mode = input('\nВыберите действие:' + '\n'
                 + '1. Найти контакт \n2. Просмотр справочника \n3. Добавить контакт \n4. Удалить контакт \n5. Изменить контакт \n6. Создать файл \n7. Выход: \n-> ')
    if mode == '2':
        print(show_data())
    elif mode == '1':
        find_data()
    elif mode == '3':
        new_data()
    elif mode == '4':
        name = input(f'Введите полностью кого удалить из справочника:\n{show_data()} \n ->')
        delete_contact(name)
    elif mode == '5':
        search_text = input(f'Введите запись которую надо изменить в справочнике: -> ')
        replace_text = input('Введите новую запись: ')
        edit_contact()
    elif mode == '6':
        spr_data()
    elif mode == '7':
        break
    else:
        print('Нет такого, попробуй еще раз')

