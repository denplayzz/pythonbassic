user_str = input("Введите строку: ")
# Переводення строки в нижній регістр
user_str = user_str.lower()
# Видалення символів пунктуації
user_str = user_str.replace(".","")
user_str = user_str.replace(",","")
user_str = user_str.replace("-","")
user_str = user_str.replace(":","")
user_str = user_str.replace(";","")
user_str = user_str.replace("?","")
user_str = user_str.replace("!","")
#Видалення табів і пробілів з правої сторони
user_str = user_str.strip()
#Заміна слова в строці і показ індекса слова яке хоче замінити користувач
replace_str = input("Какое слово, или словосочитание вы хотите заменить?: ")
index = user_str.find(replace_str)
print(index)
replace_str1 = input("На какое слово вы хотите заменить?: ")
user_replace_str = user_str.replace(replace_str, replace_str1)

print(user_replace_str)