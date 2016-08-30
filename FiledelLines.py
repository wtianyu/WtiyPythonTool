
# 去除三位行数
# 将timer.py中带行数的代码重写进timer02.py不带行数
flag = 3
with open('timer.py','r',encoding='u8') as fr:
    with open('timer02.py','w',encoding='u8') as fw:
        for line in fr.readlines():
            try:
              int(line[:flag])
              fw.write(line[flag:])
            except ValueError as e:
                fw.write(line)