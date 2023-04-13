names = input("Enter the list of names :")
to_remove = input("Enter the string value to remove :")

names_list= names.split(";")

count =1

for x in names_list:
    print(x.replace(to_remove, '').split('<')[0].strip())
    count = count+1
    print('')


print("total count :",count)    
input("Press any key to exit")

#print(names_list)