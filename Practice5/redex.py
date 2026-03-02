import re

# 1. Строка: буква 'a' и после неё 0 или больше 'b'
stroka1 = "abbb"
rez1 = re.fullmatch(r"ab*", stroka1)
print("1:", rez1 is not None)


# 2. Строка: 'a' и после неё 2-3 буквы 'b'
stroka2 = "abb"
rez2 = re.fullmatch(r"ab{2,3}", stroka2)
print("2:", rez2 is not None)


# 3. Найти слова из маленьких букв через _
tekst3 = "hello_world test_string notValid ok_test"
spisok3 = re.findall(r"\b[a-z]+_[a-z]+\b", tekst3)
print("3:", spisok3)


# 4. Найти слова: 1 большая буква + маленькие
tekst4 = "Hello World TEST Apple banana Cat"
spisok4 = re.findall(r"\b[A-Z][a-z]+\b", tekst4)
print("4:", spisok4)


# 5. Строка начинается с 'a' и заканчивается на 'b'
stroka5 = "axxxb"
rez5 = re.fullmatch(r"a.*b", stroka5)
print("5:", rez5 is not None)


# 6. Заменить пробел, запятую и точку на :
tekst6 = "Hello, world. How are you"
novaya6 = re.sub(r"[ ,\.]", ":", tekst6)
print("6:", novaya6)


# 7. Перевод snake_case в camelCase
def snake_v_camel(text):
    # ищем _буква и делаем её большой
    return re.sub(r"_([a-z])", lambda m: m.group(1).upper(), text)

print("7:", snake_v_camel("hello_world_test"))


# 8. Разделить строку по большим буквам
tekst8 = "HelloWorldTest"
spisok8 = re.split(r"(?=[A-Z])", tekst8)
print("8:", spisok8)


# 9. Вставить пробел перед каждой большой буквой
tekst9 = "HelloWorldTest"
novaya9 = re.sub(r"([A-Z])", r" \1", tekst9).strip()
print("9:", novaya9)


# 10. Перевод camelCase в snake_case
def camel_v_snake(text):
    s = re.sub(r"([A-Z])", r"_\1", text)
    return s.lower().lstrip("_")

print("10:", camel_v_snake("HelloWorldTest"))