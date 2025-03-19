with open('data.txt', 'r', encoding="utf-8") as in_file:
    content = in_file.readlines()
    print(content)

with open('tmp.txt', 'w', encoding="utf-8") as out_file:
    data = reversed(content)
    out_file.writelines(data)
