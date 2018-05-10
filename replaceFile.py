y = open('233','r')
y_new = open('233_new','w')
tihuan = input('输入要替换的替换：')
tihuan_new = input('输入要替换的替换：')

for i in y:
    print('for:' + i)
    if tihuan in i:
        i = i.replace(tihuan,tihuan_new)
    y_new.write(i)

y.close()
y_new.close()