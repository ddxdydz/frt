color = input("Введите цвет для светофора (red,green,yellow)\n")


match color:
    case "red":
        print("Стоп")
    case "green":
        print("Вперед")
    case "yellow":
        print("Внимание")
    case _:
        print("Поломка светофора")