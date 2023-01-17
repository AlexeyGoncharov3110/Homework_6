# size=int(input('Введите размер списка : '))
# my_list=[]
# sum=0
# for i in range(size):
#     i=int(input('Введите элементы списка : '))
#     my_list.append(i)
# print(my_list)
# my_list2=[]
# for i in range(len(my_list)-int(size/2)):
#    my_list2.append(my_list[i]*my_list[len(my_list)-1-i])
# print(my_list2)


size=int(input('Введите размер списка : '))
my_list =[int(input('Введите элемент :')) for _ in range(size)]
my_list=[my_list[x]*my_list[size-1-x] for x in range(len(my_list)-int(size/2))]      
print(my_list)