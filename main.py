from pprint import pprint


def get_cook_book():
    cook_book = {}
    with open('Recipe.txt', encoding='utf-8') as f:
        for line in f:
            dish = line.strip()
            cook_book[dish] = []
            count = int(f.readline().strip())
            temp_list = []
            for sub_str in range(count):
                s = f.readline().strip()
                lst = s.split('|')
                dic = {'ingredient_name': lst[0].strip(), 'quantity': int(lst[1].strip()), 'measure': lst[2].strip()}
                temp_list.append(dic)
            cook_book[dish] = temp_list
            f.readline().strip()
        # pprint(cook_book, sort_dicts=False)
        return cook_book


def get_shop_list_by_dishes(dishes, person_count):
    cook_book = get_cook_book()
    dic = {}
    for dish in dishes:
        temp_dish = cook_book[dish]
        for ingredients in temp_dish:
            quantity = 0
            if ingredients['ingredient_name'] in dic:
                quantity = dic[ingredients['ingredient_name']]['quantity']
            dic[ingredients['ingredient_name']] = {'measure': ingredients['measure'],
                                                   'quantity': ingredients['quantity']*person_count+quantity}
    pprint(dic)
    return


get_shop_list_by_dishes(['Омлет', 'Запеченный картофель'], 4)
