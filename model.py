import random

class Toy: 
    id: int 
    name: str 
    win_percent: int 
 
    def __init__(self, id: int, name: str, win_percent: int): 
        self.id = id 
        self.name = name 
        self.win_percent = win_percent 
 
    def add_new_toy_to_file(self): 
        with open("toys.txt", "a") as file: 
            file.write(f'{self.id}, {self.name}, {self.win_percent}\n') 
 
def add_new_toy(): 
    toy = [] 
    id = random.randint(1, 100) 
    name = input("Введите название игрушки: ") 
    win_percent = input("Введите частоту выпадения игрушки: ") 
 
    toy.append(id) 
    toy.append(name) 
    toy.append(win_percent) 
 
    return toy 
 
def open_file_list(path): 
    with open(path) as file: 
        list1 = [] 
        for i in file: 
            res = i[:-1].split(', ') 
            list1.append(res) 
    return list1 