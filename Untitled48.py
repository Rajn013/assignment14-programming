#!/usr/bin/env python
# coding: utf-8

# 1.Define a class with a generator which can iterate the numbers, which are divisible by
# 7, between a given range 0 and n.

# In[4]:


class DivisibleBySeven:
    def divisible_by_seven(self, n):
        for i in range(n):
            if i % 7 == 0:
                yield i
                
divisible_by_seven = DivisibleBySeven()
for number in divisible_by_seven.divisible_by_seven(50):
    print(number)


# 2.Write a program to compute the frequency of the words from the input. The output should output after sorting the key alphanumerically. 
# Suppose the folclowing input is supplied to the program:
# New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3.
# Then, the output should be:
# 2:2
# 3.:1
# 3?:1
# New:1
# Python:5
# Read:1
# and:1
# \between:1
# choosing:1
# \or:2
# to:1

# In[13]:


from collections import defaultdict

text = input("Enter some text: ")
word_freq = defaultdict(int)

for word in text.split():
    word_freq[word] +=1

for word, freq in sorted(word_freq.items()):
    print(f"{word}:{freq}")


# 3.Define a class Person and its two child classes: Male and Female. All classes have a method "getGender" which can print "Male" for Male class and "Female" for Female class.

# In[3]:


class Person:
    def getGender(self):
        print("Unknown")
        
class Male(Person):
    def getGender(self):
        print("Male")
        
class Female(Person):
    def getGender(self):
        print("Female")
        
person = Person()
person.getGender()
    
person = Male()
person.getGender()
    
person = Female()
person.getGender()


# 4.Please write a program to generate all sentences where subject is in ["I", "You"] and verb is in ["Play", "Love"] and the object is in ["Hockey","Football"].

# In[11]:


def identify_grnder(self):
    print("Unkonwn")
def identify_gender(self):
    print("male")
def identify_gender(self):
          print("Female")
                
                
person = Person()
person.getGender()
    
person = Male()
person.getGender()
    
person = Female()
person.getGender()


# 5.Please write a program to compress and decompress the string "hello world!hello world!hello world!hello world!".
# 

# In[23]:


import zlib
compressed_strint = zlib.compress(b"hello world!hello world!hello world ! hello world ! " )
print("Compressed string:", compressed_strint)
decompressed_string = zlib.decompress(compressed_strint)
print(decompressed_string.decode())


# 6.Please write a binary search function which searches an item in a sorted list. The function should return the index of element to be searched in the list.
# 

# In[38]:


arr = [1,2,3,4,5,6,7,8,9]
x = 4

def binary_search(arr , x):
    low = 0
    

    high = 1
    
    while low <= high:
        mid = (low + high)  // 2
        
        if arr[mid] == x :
            return mid
        elif arr[mid] < x:
            low = mid + 1
        else:
                high = mid - 1
                
    return -1

result = binary_search(arr , x)

if result != -1:
    print(f"element {x} is present at index {result}")
else:
        print(f"Element {x} is not present in the list")


# In[ ]:




