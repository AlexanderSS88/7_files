from pprint import pprint
import os

def c_book(file, encoding):
    with open('recipes.txt', encoding=encoding) as file:
        cook_book = {}
        for line in file:
            dish = line.strip()
            num_ingredients = int(file.readline().strip())
            list_ing = []
            for id in range(0, num_ingredients):
                string = file.readline().split(' | ')
                dict_ing = {'ingredient_name': string[0], 'quantity': string[1], 'measure': string[2].strip()}
                list_ing.append(dict_ing)
            file.readline()
            cook_book[dish] = list_ing
        return cook_book


def dict_ingred(cook_book, dishes, persons):
    need_dishes = {}
    for num in range(persons):
        for dish in dishes:
            if dish in need_dishes:
                need_dishes[dish] += 1
            else:
                need_dishes[dish] = 1
    dict_ingredients = {}
    for dish, num in need_dishes.items():
        x = cook_book[dish]
        for ingred in x:
            if ingred['ingredient_name'] in dict_ingredients:
                # print(f'Ингридиент {ingred["ingredient_name"]} повторился')
                dict_ingredients[ingred['ingredient_name']][1] += int(ingred['quantity']) * num
            else:
                dict_ingredients[ingred['ingredient_name']] = [ingred['measure'], (int(ingred['quantity'])) * num]
    return dict_ingredients


def create_file(dir, encoding):
    work_dir = os.getcwd()
    files = os.listdir(dir)
    dict_file = {}
    dict_file_final = {}
    dict_file_final_n = {}
    name_file = {}
    for file in files:
        file_path = os.path.join(work_dir, dir_files_name, file)
        with open(file_path, encoding=encoding) as doc:
            data = doc.readlines()
            length_file = len(data)
            dict_file[length_file] = data
            name_file[length_file] = file
    list_d = list(dict_file.items())
    list_d.sort(key=lambda i:i[1], reverse=True)
    list_n = list(name_file.items())
    list_n.sort(key=lambda i:i[0])
    for id in list_d:
        dict_file_final[id[0]] = id[1]
    for id in list_n:
        dict_file_final_n[id[0]] = id[1]
    with open('final.txt', mode='a', encoding=encoding) as doc:
        for line, data in dict_file_final.items():
            doc.write(f'{str(dict_file_final_n[line])} \n')
            doc.write(f'{str(line)}\n')
            for id in dict_file_final[line]:
                doc.write(f'{id.strip()}\n')
            doc.write('\n')
    return doc


dir_files_name = 'sort'
dir_files_path = os.path.abspath(dir_files_name)
print(dir_files_path)
create_file(dir_files_path, 'utf-8')
cook_book = c_book('recipes.txt', 'utf-8')
dishes = ['Омлет', 'Фахитос', 'Утка по-пекински', 'Омлет']



