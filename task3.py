age = input("Введите ваш возраст: ")

if age.isdigit():
  age = int(age)
  if age < 0:
    print("Ошибка: возраст не может быть отрицательным!")
  else:
    if age >= 18:
      print("Вы совершеннолетний.")
    else:
      print("Вы несовершеннолетний.")
else:
  print("Ошибка: введено не число!")      
