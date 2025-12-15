with open("text.txt", "r", encoding="utf-8") as file:
    data = file.read()
print("Слов в тексте: ", data.count(" "))