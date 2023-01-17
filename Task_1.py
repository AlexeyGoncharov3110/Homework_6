
# number=int(input('Введите число : '))
# my_list=[]
# sum=0
# for i in range(1,number+1):
#     my_list.append(round((1+1/i)**i,2))
#     sum=sum+my_list[i-1]
# print(my_list)
# print(round(sum,2))

number = int(input('Введите число : '))
my_list = list(map(lambda x: round((1+1/x)**x, 2),[x for x in range(1, number+1)]))
sum=sum(my_list)
print(my_list)
print(sum)
