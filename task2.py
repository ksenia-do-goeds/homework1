num = input("Введите число: ")

if num.isdigit():
  num = int(num)
  if num%2 == 0:
    print(f"Число {num} является четным.")
  else:
    print(f"Число {num} не является четным.")
else:
  print("Ошибка: введено не число.")
