a = int(input("Введите место студента в списке: "))

if a <= 10:
    b = int(input("Введите общий балл студента: "))
    print("Поздравляем! Вы поступили!")
    
    if b >= 290:
        print("Бонусов вам будет начислятся стипендия.")
    else:
        print("Но вым не хватило баллов для стипендии.")
else:
    print("К сожалению, вы не поступили.")
