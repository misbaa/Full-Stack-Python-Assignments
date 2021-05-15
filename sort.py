Python 3.9.1 (tags/v3.9.1:1e5d33e, Dec  7 2020, 17:08:21) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
                                                
>>> ip=["192.168.10.1","192.168.10.20","192.168.10.9","192.168.10.100","192.168.10.5"]
>>> def fun(x):
...     return int(x.rsplit(".",1)[-1])
...
>>> ip.sort(key=fun)
>>> print(ip)
['192.168.10.1', '192.168.10.5', '192.168.10.9', '192.168.10.20', '192.168.10.100']
>>>