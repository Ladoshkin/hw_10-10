place = int(input("Введите место студента в списке: "))

if place <= 10:
    score = int(input("Введите общий балл студента: "))
    print("Поздравляем! Вы поступили!")
    
    if score >= 290:
        print("Бонусов вам будет начислятся стипендия.")
    else:
        print("Но вым не хватило баллов для стипендии.")
else:
    print("К сожалению, вы не поступили.")
