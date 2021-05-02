Python 3.9.1 (tags/v3.9.1:1e5d33e, Dec  7 2020, 17:08:21) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> num=int(input("Enter a number:"))
Enter a number:89
>>> if num>1:
...     for i in range(2,num):
...             if(num%i==0):
...                     print(num,"is not a prime number")
...                     break
...     else:
...             print(num,"is a prime number")
... else:
...     print(num,"number is not a prime number")
...
89 is a prime number
>>>