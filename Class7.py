#Que1
print("create a dictionary")
class demo:
    def check(self):
        dict1 = dict({})
        a = int(input("enter the no. of elements in dictionary : "))
        for i in range(0,a):
            key = input("enter the key for dictionary : ")
            value = input("enter the value for dictionary : ")
            dict1.update({key:value})
        print(dict1)
obj = demo()
obj.check()
print("\n")

#Que2
print("create a nested dictionary to store the marks of a student")
class marks:
    def student(self):
        dictionary = {"Ishani":{"English":"87", "Maths":"90", "Science":"78"},"Archit":{"English":"89","Maths":"95","Science":"85"}}
        for id,info in dictionary.items():
            print("Student Name : ",id)
            for key in info:
                print(key + ":", info[key])
obj = marks()
obj.student()