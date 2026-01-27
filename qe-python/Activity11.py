dict =  {"pinapple":30,
         "banana":30,
         "apple":50}
x = input("enter a fruit\n")
if x in dict:
    print(dict.get(x))
else:
    print("not available")    