import model, random, view

def button():
    view.what_to_do() 
    do = input("Введите цифру: ") 

    if do == "1": 
        toy_parameters = model.add_new_toy() 
        toy = model.Toy(toy_parameters[0], toy_parameters[1], toy_parameters[2]) 
        toy.add_new_toy_to_file() 
    elif do == "2": 
        win_percent_of_toy = random.randint(1, 100) 
        result = model.open_file_list("toys.txt") 
        check = False 
        win_toy = random.choice(result) 
        while not check:
            if int(win_toy[2]) < win_percent_of_toy:
                win_toy = random.choice(result)
            else:
                check = True
                
        print(f"Вы выиграли игрушку {win_toy[1]}! Поздравляем!")