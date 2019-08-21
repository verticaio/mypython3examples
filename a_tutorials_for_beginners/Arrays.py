# Python code to demonstrate the working of 
# array(), append(), insert()
  
# importing "array" for array operations
import array
arr = array.array('i',[1,2,3])
#print(arr[1])
#print(arr[1])
#print(arr[1])
# printing original array
print("The new created array is : " , end="")
for i in range(0,3):
	print(arr[i], end ="  ")

print("\r")
# using append() to insert new value at end
arr.append(4);
print ("The appended array is : ", end="")
for i in range (0, 4):
    print (arr[i], end=" ")

print("\r")

arr.insert(2,5)
# printing array after insertion
print ("The array after insertion is : ", end="")
for i in range (0, 5):
    print (arr[i], end=" ")



# printing original array
print ("The new created array is : ",end="")
for i in range (0,5):
    print (arr[i],end=" ")
 
print ("\r")
 
# using pop() to remove element at 2nd position
print ("The popped element is : ",end="")
print (arr.pop(2));
 
# printing array after popping
print ("The array after popping is : ",end="")
for i in range (0,4):
    print (arr[i],end=" ")
 
print("\r")
 
# using remove() to remove 1st occurrence of 1
arr.remove(1)
 
# printing array after removing
print ("The array after removing is : ",end="")
for i in range (0,3):
    print (arr[i],end=" ")