with open('data.bin','rb') as in_file:
    data = in_file.read()
    print(data)

with open('tmp.bin','wb') as out_file:
    out_file.write(data)
