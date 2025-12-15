anagramm = True
s1 = input("Введите строку 1")
s2 = input("Введите строку 2")
for i in s1.lower():
    if i not in s2.lower():
        anagramm = False
        break
print("строки являются анаграмамми", anagramm)
