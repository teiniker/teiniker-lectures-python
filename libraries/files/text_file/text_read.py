with open('data.txt', 'r', encoding="utf-8") as in_file:
    for line in in_file:
        print(f"> {line}", end='')
