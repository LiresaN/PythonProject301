list1 = [elem for elem in range(1,11) if elem % 2 == 0]
print(list1)

list2 = [elem for elem in range(1,11)]
print(list2)
list3 = []

for elem in list2:
    if elem % 2 == 0:
        list3.append(elem)
print(list3)

#########################################################################################

list_a = [elem for elem in range(3,11)]
list_b = [elem for elem in range(6,15)]
print(list(set(list_a+list_b)))
print(set(list_a+list_b))
