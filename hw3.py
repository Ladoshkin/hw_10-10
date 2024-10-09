def vklad(summa_vklada, itog_vklada, procent):
    years = 0
    summa = summa_vklada
    
    while summa < itog_vklada:
        summa += summa * procent / 100
        summa = int(summa)  # отбрасываем дробную часть
        years += 1
    
    return years

def main():
    print("Введите начальную сумму вклада (X):")
    summa = float(input())
    
    print("Введите целевую сумму (Y):")
    itog_vklada = float(input())
    
    print("Введите процентную ставку (P):")
    procent = float(input())
    
    years_needed = vklad(summa_vklada, itog_vklada, procent)
    
    print("Количество лет, необходимых для достижения суммы {target_amount}: {years_needed}")

if __name__ == "__main__":
    main()
