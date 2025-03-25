name = input('Ваше имя: ')
surname = input('Ваша фамилия: ')
age = input('Ваш возраст: ')

# Реализация через format
formatted_string = "Ваше имя: {}, Фамилия: {}, Возраст: {} лет.".format(name, surname, age)
print("Реализация через format:")
print(formatted_string)

# Реализация через f-string
f_string = f"Ваше имя: {name}, Фамилия: {surname}, Возраст: {age} лет."
print("Реализация через f-string:")
print(f_string)
