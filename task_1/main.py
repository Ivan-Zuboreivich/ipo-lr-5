string=input("Введите строку")
lenght = len(string)
print(lenght)
glc = 0
sglc = 0
gl = " А, О, У, И, Ы, Э, Я, Е, Ё, Ю"
sgl = "Б, В, Г, Д, Ж, З, Й, К, Л, М, Н, П, Р, С, Т, Ф, Х, Ц, Ч, Ш, Щ"
for i in string:
     if (gl.lower().find(i.lower()) != -1):
          glc += 1
     else:
          sglc += 1
print("количество гласных", glc)
print("количество согласных", sglc)


