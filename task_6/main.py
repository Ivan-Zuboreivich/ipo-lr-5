with open("text.txt", "r", encoding="utf-8") as file:
    data = file.read()
out = ""
strs = data.split("\n")
for i in strs:
    if len(i) > 5:
        out += i + "\n"
with open("output.txt", "w", encoding="utf-8") as wr:
    wr.write(out)

