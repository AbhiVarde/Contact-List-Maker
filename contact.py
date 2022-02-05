
names = []
contact_no = []
num = 5

print("\n\t* Create Your Contact List *")
for i in range(num):
    Name = input("\nName : ")
    Contact = input("Contact No : ")
    names.append(Name)
    contact_no.append(Contact)
print("\n Name \t\t Contact No \n")

for i in range(num):
    print("{} \t\t {} ".format(names[i], contact_no[i]))

Search = input("\n Enter Search item : ")
if Search in names:
    index = names.index(Search)
    Contact = contact_no[index]
    print("\nHere Your Search item : ")
    print(" Name : {} \n Conatact No : {}\n".format(Search,Contact))
else:
    print("\nSearched Item Not Found ! \n")