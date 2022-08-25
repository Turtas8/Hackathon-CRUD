import json

FILE_PATH = 'data.json'


def get_data():
    with open(FILE_PATH) as file:
        return json.load(file)


def create_product():
    data = get_data()
    product = {
        'id': get_id(),
        'brand': input('Введите название продукта: '),
        'model': input('Введите модель продукта: '),
        'data': int(input('Введите дату выпуска продукта: ')),
        'description': input('Введите описание продукта: '),
        'price': round(float(input('Введите цену продукта: ')), 2)
    }
    data.append(product)

    with open(FILE_PATH, 'w') as file:
        json.dump(data, file, indent=2)
    return 'CREATED'


def list_of_products():
    data = get_data()
    for product in data:
        print(f'{product}\n')
    return 'Список товаров'
    

def get_one_product():
    data = get_data()
    id = int(input('Введите id продукта: '))
    product = list(filter(lambda x: x['id'] == id, data))
    if product:
        return product[0]
    else:
        return 'Такого продукта нет'


def detail_retrieve():
    data = get_data()
    id_product = int(input('Введите id продукта: '))
    try:
        product = list(filter(lambda x: x['id'] == id_product, data))[0]
    except IndexError:
        print('Такого продукта нет')
    else:
        print('Id', product['id'])
        print('Title', product['title'])
        print('Description', product['description'])
        print('Price', product['price'])
        print()


def get_id():
    with open('id.txt', 'r') as file:
        id = int(file.read())
        id += 1
    with open ('id.txt', 'w') as file:
        file.write(str(id))
    return id


def update_product():
    data = get_data()
    flag = False
    id = int(input('Введите id продукта: '))
    product = list(filter(lambda x: x['id'] == id, data))

    if not product:
        return 'Такого продукта нет'
    index_ = data.index(product[0])
    choice_ = input('Что вы хотите изменить?\n(1 - brand)\t(2 - model)\t(3 - data)\t(4 - description)\t(5 - price): ') 
 
    if choice_ == '1': 
        data[index_]['brand'] = input('Введите новое название продукта: ')
        flag = True 
    elif choice_ == '2': 
        data[index_]['model'] = input('Введите новую модель продукта: ')
        flag = True 
    elif choice_ == '3':
        data[index_]['data'] = int(input('Введите новую дату продукта): '))
        flag = True
    elif choice_ == '4':
        data[index_]['description'] = input('Введите новое описание продукта: ')
        flag = True
    elif choice_ == '5':
        data[index_]['price'] = round(float(input('Введите новую цену продукта: ')), 2)
    else: print('Такого поля нет')

    with open(FILE_PATH, 'w') as file:
        json.dump(data, file)
    
    if flag:
        return 'UPDATED'
    else:
        return 'Not updated'


def delete_product():
    data = get_data()
    id = int(input('Введите id продукта: '))
    product = list(filter(lambda x: x['id'] == id, data))

    if not product:
        return 'Такого продукта нет!'

    index_ = data.index(product[0])
    data.pop(index_)

    json.dump(data, open(FILE_PATH, 'w'))

    return 'DELETED'

