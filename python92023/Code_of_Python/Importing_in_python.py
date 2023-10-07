# import pandas and use it's functionalites
import pandas as pd
import math
print(math.floor(4.7859))
print(pd.__version__)
# pd.read_csv("ajay.csv")
pd.read_clipboard("ajay")
# pd.read_xml("ajay.xlsx")# parsal  must  be intalled  for read  any  file read




#  we  can do   this also 
from  math import sqrt,pi
result= sqrt(423423)*pi
print(result)

from math import*

from math import sqrt as s

a=23420384023
res=s(a)
print(res)

import math as m
resss=3459

p=print(m.sqrt(resss))
p=print(m.pi*(resss))


import math
print(dir(math))


from ajay import ajay,my_name
from ajay import*
import ajay as a
print("this is external file ")
a.ajay()
print(a.my_name)