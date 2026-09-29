name = input('ФИО: ').split()
print('Инициалы: ', name[0][0],name[1][0],name[2][0],'.', sep='')
print('Длина (символов):',len(name[0])+len(name[1])+len(name[2])+2)
