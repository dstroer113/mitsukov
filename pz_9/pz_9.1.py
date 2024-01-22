list = {"растение": "лимон","ягода": "малина", "овощ": "огурец"}
if "фрукт" not in list:
    print("первоначальный", list)
    list["фрукт"] = "яблоко"
    print("второй", list)
else:
    print(list)
