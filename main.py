while True:
    try:
        year = int(input("Введите год: "))
        if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
            print(f"{year} - високосный год")
        else:
            print(f"{year} - не високосный год")

        closest_leap = year + (4 - year % 4)
        if closest_leap < year:
            closest_leap += 4
        print(f"Ближайший високосный год: {closest_leap}")

        print("Високосные годы в интервале 1900-2100:")
        for i in range(1900, 2101):
            if i % 4 == 0 and (i % 100 != 0 or i % 400 == 0):
                print(i, end=" ")

        break  # Выход из цикла
    except ValueError:
        print("Некорректный ввод. Введите год снова.")

