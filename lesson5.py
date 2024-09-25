immutable_var = (1,3,5,7, "Скелетор")
print(immutable_var)
#immutable_var_[2] = 9
print(immutable_var)#кортеж не поддерживает обращение по элементам
mutable_list = [5,7,"Т","о","р"]
mutable_list.append("и Локи")
print(mutable_list)
mutable_list.extend("бдсм")
print(mutable_list)
mutable_list.remove("и Локи")
print(mutable_list)