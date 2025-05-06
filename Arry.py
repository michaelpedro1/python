import array

my_array=array.array('i',[1,2,3,5,7,8,6])
my_array.append(12)
print(my_array)
my_array.remove(2)
print(my_array)

print(my_array[5])