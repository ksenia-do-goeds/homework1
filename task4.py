while True:
  num = input("Введите число (или 'exit' для выхода): ")
  if num.lower() == 'exit':
    print("Выход из программы...")
    break
  elif num.lstrip('-').isdigit():
    length = len(num.lstrip('-'))
    print(f"В этом числе {length} цифры.")
  else:
    print("Ошибка: данные не являются числом.")
