immutable_var = 1, "строка", False
print(immutable_var, type(immutable_var))
print(immutable_var[-1])
#immutable_var[0]=50  #в этой строке я пробую изменить неизменяемый объект согласно заданию
print(immutable_var)

mutable_list = [25, 4, 'список']
print(mutable_list, type (mutable_list))
mutable_list.append('добавленный элемент в конец списка')
mutable_list[1] = 'замененный элемент'
mutable_list[0]=mutable_list[0]+100
print(mutable_list)
