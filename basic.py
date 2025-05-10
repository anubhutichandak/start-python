# print("hello world")
 
# name = "anubhuti"
# print(name)

# number  = 5000
# print(number)
# num = 67.89
# print(num)
 

# print(15 + 5 * 10)

 
 # >>>>>>>>>>>>>>>>>>>>>>>>>> string >>>>>>>>>>>>>>>>>>>>>>>>>

# name = "anubhuti"  
# print(name[0:2])
# print(name[4])
# print(type(name))
# num = 100.6
# print(type(num))
# var = True
# print(type(var))
#print(len(name)) #find the lenght of string


# name = "anubhuti" 
# name_upper = "ANUBHUTI" 
# print(name.upper()) 
# print(name_upper.lower()) # convert upper case into lower case
# print(name.swapcase())
# print(name.title())
 
 # print(name.replace("anubhuti", "anu")) #to replace one element to another
 
# name = "anubhuti"
# last_name = "chandak"
 # print(name + " " +  last_name) #adding of string
 # print(name.find("h")) # finding the particular character
 # print(name.capitalize()) # capitalize fist letter
 
 # print("My name is ", name, "and my last name is ", last_name) 
 
 
 # print(3 * name) #print name 3 times
 
# print(f"my name is  {name}  and my last name is  {last_name}")
 
 
 
# print(name.replace("i", "j"))
 # print(name.replace("i", "j", 1))
 
 
 
 # text =  " hello world "
 
 # # print(text.replace("world", "python"))
 # print(text.index("world"))
 
 
 
 
 
 #>>>>>>>>>>>>>>>>>>>>> list >>>>>>>>>>>>>>>>>>>>>>>>>>. 
 
 
 # my_list = [1,2,3,4,5,5,5,5,54,5,5,5,55]
 # print(type(my_list))
 
 
 # my_list1 = [1,"anu",3,4.2,True,5,5,5,54,5,5,5,55]
 # print(type(my_list1))
 # print(my_list1)
 
 # print(my_list)
 # print(my_list[2])
 
 
 # my_list = [1,2,3,4,5,5,54,67,6,55]
 # print(my_list[-1]) 
 # print(my_list[-2])
 # print(my_list[-3])
 # print(my_list[-4])
 # print(my_list[-5])
 
 # print(my_list[1])
 # print(my_list[2])
 # print(my_list[3])
 # print(my_list[4])
 # print(my_list[5])
 
 
 # my_list = [1,2,3,4,5,5,54,67,6,55]
 
 
 # print(my_list[1:5])
 # print(my_list[:5]) # same as [1:5]
 # print(my_list[1:]) # same as [1:len(list)]
 # print(my_list[:]) 
 
 
 # print(len(my_list))
 
 
 # my_list.append(100) # add the element
 # print(my_list)
 
 # my_list.insert(1,100)
 # print(my_list)
 # my_list.remove(5) # remove element
 # print(my_list)
 # my_list.pop() #remove radom element
 # print(my_list)
 # my_list.index(5)
 # print(my_list)
 
 # my_num = [5,4,3,2,1]
 # my_num.sort() # sort the list in assending oder
 # my_num.clear() # clear whole list
 # print(my_num)
 
 
 
 
 # >>>>>>>>>>>>>tuple >>>>>>>>>>>>>>>>>>>>
 
 
 
# tpl = (1,2,3,4,5)
# print("tpl:",tpl) 
# print("type of tpl:",type(tpl))
# print("len  of tpl:",len(tpl))
 
# print("0 position of element :-",tpl[0])
# print("1 position of element :-",tpl[1])
# print("2 position of element :-",tpl[2])
# print("3 position of element :-",tpl[3])
# print("4 position of  element :-",tpl[4])

 
 
 
# tpl = (1,2,3,4,5)
  
# print("0 to 2  position of  elements :-",tpl[0:2])
# print("1 position of elements :-",tpl[::-1])  
 
 
 
# print("1 position of element :-",tpl[1:-1])  
# tpl = (1,2,3,4,5)
 
# print(2 in tpl)
# print(10  in tpl)
 
 
# print("max of tpl:-",max(tpl)) # maximum element in tuple
# print("min of tpl:-",min(tpl)) # minmum element in tuple
# print("sum of tpl:-",sum(tpl)) # sum of elements of tuple
 
 
 
 
 
 # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> dict >>>>>>>>>>>>>>>>>>>>
 
# dict = {
#      "name" : "anubhuti",
#      "last_name" : "chandak",
#      "age" : 19
#  }
# print("dict type:-",type(dict))
# print("dict :-",dict)
 
# print(dict["name"])
 
# print("name :-",dict["name"])
# print("last_name :-",dict["last_name"]) 
# print("age :-",dict["age"]) 
 
 
# print("dict keys:-",dict.keys())
# print("dict values:-",dict.values())
# print("dict items:-",dict.items())

 
 # item adding in dct 
 
# dict['Gender'] = "Female"   # Add new key value pair
# print(dict)
 
 
# dict['age'] = 22 # update age with new value
# print(dict)
 
# del dict['last_name'] # deleting the items
# print(dict) 
# dict.pop('last_name')
# print(dict)
 
 # dict.clear()
 # print(dict)
 # print('name' in dict)
 # print('anubhuti' in dict)
 
 
 
 
# dict1 = dict.copy() #copydict into dict1
# print(dict1)
 
# copy_dict=dict.copy()
# print("copy dict ",copy_dict)
# print("original dict ",dict)
 
 
 
#  #  Merging Dictionaries
 
 
# dict1 = {
#      "name1" : "vikram",
   
#      "age1" : 21
#  } 
 
# dict2 = {
#      "name2" : "kapil",
#      "last_name" : "kumar",
#      "age2" : 21
#  } 
 
# dict1.update(dict2)
# print(dict1)
 
 
# key = ["a","b","c"]
# default_dict=dict.fromkeys(key, 0)
 
 # print(default_dict)   # {'a': 0, 'b': 0, 'c': 0}
 
 
 
 # >>>>>>>>>>>>>>>>>>>> Set >>>>>>>>>>>>>>>>>
 
# my_set = {1,2,3,4,5,"anu"}
 # print(type(my_set))
 # # print(my_set)
 
 # my_set.add(100)
 # my_set.add("aachal")
 # my_set.add("arati")
 
 # print(my_set)
 
 # my_set.remove("anu")
 # print("remove element:-",my_set)
 # my_set.discard(5)
 # print("discard element:-",my_set)
 
 # my_set.pop()
 # print("pop element:-",my_set)
 # my_set.clear()
 # print("clear element:-",my_set)
 

#>>>>>>>>>>>>>>>> updating dict >>>>>>>>>>>>>

# my_dict = {'name': 'anubhuti', 'age': 25}

# # change the key 'name' to 'new_name'
# my_dict['new_name'] = my_dict['name'] #Add new key with old value
# del my_dict['name']                   #Delete old key

# print(my_dict)

#>>>>>>>>>>>>>>>>>>>>>>>>>>>> oprateors >>>>>>>>>>>>>>>>>

#>> arithmetic oprateor >>
# a = 10
# b = 3
# print(a + b)  # Addition
# print(a - b)  # Subtraction
# print(a * b)  # Multiplication
# print(a / b)  # Division
# print(a % b)  # Modulus
# print(a ** b) # Exponentiation
# print(a // b) # Floor division

#>>> assigment opateor >>>>>>
# x = 5
# print(x)
# x += 3  # x = x + 3 = 8
# print(x)
# x -= 2  # x = x - 2 = 6
# print(x)
# x *= 4  # x = x * 4 = 24
# print(x)
# x /= 2  # x = x / 2 = 12.0
# print(x)
# x %= 3  # x = x % 3 = 0.0
# print(x)
# x **= 2 # x = x ** 2 = 0.0
# print(x)
# x //= 2 # x = x//2 = 0
# print(x)

#>>> relational oprateors >>>
# a = 5
# b = 10
# print(a == b)  # Equal
# print(a != b)  # Not equal
# print(a > b)   # Greater than
# print(a < b)   # Less than
# print(a >= b)  # Greater than or equal to
# print(a <= b)  # Less than or equal 

#>>>> logical oprateors >>>
# x = True
# y = False
# print(x and y) # AND - true if both are true
# print(x or y)  # OR  - true if one of them are true
# print(not x)   # NOT - oposite of x

#>>>bitwise oprators >>>>>.
# a = 5 #0101
# b = 3 #0011
# print(a & b)  # AND
# print(a | b)  # OR
# print(a ^ b)  # XOR
# print(~a)     # NOT
# print(a << 1) # Left Shift
# print(a >> 1) # Right Shift

#>>>> membership oprateors >>>>
# lst = [1, 2, 3]
# print(2 in lst)     # if 2 is in list the then true if not then false 
# print(3 not in lst) # if 3 is in list then false if not the true

#>>> identity opreators >>>>
# a = b = [1, 2]
# c = [1, 2]
# print(a is b)     # True
# print(a is c)     # False
# print(a is not c) # True 

