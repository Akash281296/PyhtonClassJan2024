
Purpose: Data Type Conversions - int, float, complex, boolean, string, None

    int - decimal       - int() -base 10  (0-9)
        - binary        - bin() -base  2  (0-1)
        - hexadecimal   - hex()
        - octal         - oct()
    floatm
        float()
    String
        str()


int -> float int -> str

float -> int float -> str

str -> int str -> float """

num = 12
print("num=", num, type(num))
num= 12 <class 'int'>
# int -> float
print(12, float(12))  # 12 12.0
12 12.0
# int -> str
print(12, str(12))  # 12 '12'
12 12
# float -> int
print(3.1416, int(3.1416))  # 3.1416,  3
print(3.1416, str(3.1416))  # 3.1416, '3.1416'
3.1416 3
3.1416 3.1416
# str  -> int
print("23", int("23"))  # '23 ', 23
print("23 ", int("23 "))  # '23 ', 23
23 23
23  23
print('2 3', int('2 3'))
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
Cell In[6], line 1
----> 1 print('2 3', int('2 3'))

ValueError: invalid literal for int() with base 10: '2 3'
print('two', int('two'))
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
Cell In[7], line 1
----> 1 print('two', int('two'))

ValueError: invalid literal for int() with base 10: 'two'
print('23.24', int('23.24')) 
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
Cell In[8], line 1
----> 1 print('23.24', int('23.24')) 

ValueError: invalid literal for int() with base 10: '23.24'
# str -> float
print("23   ", float("23"))  # '23   ', 23.0
print("23.24", float("23.24"))  # '23.24', 23.24
print("23.  ", float("23."))  # '23.  ', 23.0
23    23.0
23.24 23.24
23.   23.0
print("23   ", float("23  "))  # '23   ', 23.0
23    23.0
print('2 3. ', float('2 3.'))
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
Cell In[12], line 1
----> 1 print('2 3. ', float('2 3.'))

ValueError: could not convert string to float: '2 3.'
float()                 # 0.0
float("+1.23")          # 1.23
float("   -12345\n")    # -12345.0
float("1e-003")         # 0.001
float("+1E6")           # 1000000.0
float("-Infinity")      # -inf
-inf
float("+Infinity")      # +inf
inf
float("+inf")      # +inf
inf
float("-inf")      # -inf
-inf
float("-inf")      # -inf
-inf
float("-INF")      # -inf
-inf
# NOTE: Anything can be converted to str; but not vice versa
print("str(12)          ", str(12))
print("str(121233.12323)", str(121233.12323))
print("str(-0.000012)   ", str(-0.000012))
print("str(True)        ", str(True))
print("str(None)        ", str(None))
str(12)           12
str(121233.12323) 121233.12323
str(-0.000012)    -1.2e-05
str(True)         True
str(None)         None
REpresentations of Integers
- decimal form 
- binary 
- octal 
- Hexadecimal
num1 = 33
print("num1 =", num1, type(num1))  # -> Decimal form
num1 = 33 <class 'int'>
bin(23)
'0b10111'
bin()
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
Cell In[22], line 1
----> 1 bin()

TypeError: bin() takes exactly one argument (0 given)
bin(23.3)
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
Cell In[23], line 1
----> 1 bin(23.3)

TypeError: 'float' object cannot be interpreted as an integer
bin(int(23.3))
'0b10111'
#       128 64 32 16  8 4 2 1
# 23 ->   0  0  0  1  0 1 1 1 = 16 + 4 + 2 + 1 = 23
#  9 ->   0  0  0  0  1 0 0 1

bin(23)
'0b10111'
bin(9)
'0b1001'
bin(-9)
'-0b1001'
int('0b1001')
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
Cell In[28], line 1
----> 1 int('0b1001')

ValueError: invalid literal for int() with base 10: '0b1001'
# binary -> decimal form
print("0b1001", int("0b1001", base=0))  # 9
print("1001  ", int("1001", base=0))  # 1001
print("bin(9)", int(bin(9), base=0))  # 9
0b1001 9
1001   1001
bin(9) 9
print((9).bit_length())   # 4 <- '0b1001'
print((23).bit_length())  # 5 <- '0b10111'
4
5
# Octal -> 0-7
# decimal -> octal
print("oct(9)  ", oct(9))  # '0o11'
print("oct(-23)", oct(-23))  # '-0o27'
oct(9)   0o11
oct(-23) -0o27
# octal -> decimal
print(int(oct(9), base=8))  # 9
print(int("0o11", base=8))  # 9
print(int("11", base=8))  # 9
print(int("11"))  # 11
9
9
9
11
# Hexadecimal - 0-9 A-F
# decimal -> hexadecimal
print("hex(9)  ", hex(9))       # '0x9'
print("hex(-23)", hex(-23))     # '-0x17'

# hexadecimal -> decimal
print(int(hex(-23), base=16))   # -23
print(int("-0x17", base=16))    # -23
print(int("-17", base=16))      # -23
print(int("-17"))               # -17
hex(9)   0x9
hex(-23) -0x17
-23
-23
-23
-17
"%#o" % 10
'0o12'
"%o" % 10 
'12'
"%#o" % 10, "%o" % 10  # ('0o12', '12')
format(10, "#o"), format(10, "o")  # ('0o12', '12')
f"{10:#o}", f"{10:o}"  # ('0o12', '12')
('0o12', '12')
"%#x" % 255, "%x" % 255, "%X" % 255  # ('0xff', 'ff', 'FF')
format(255, "#x"), format(255, "x"), format(255, "X")  # ('0xff', 'ff', 'FF')
f"{255:#x}", f"{255:x}", f"{255:X}"  # ('0xff', 'ff', 'FF')
('0xff', 'ff', 'FF')
# Checks ##################
# is_integer -> Return True if the float is an integer.
print((-2.0).is_integer())      # True
print((-2.1).is_integer())      # False
print((-1.9999).is_integer())   # False
True
False
False
# ---- telugu numbers
print(int("42"))  # 42
print(int("४२"))  # 42
print(int("٤٢"))  # 42
print(int("४२", 16))  # 66
print(int("४२", base=16))  # 66
42
42
42
66
66
# Telugu numbers
for num in ["౦", "౧", "౨", "౩", "౪", "౫", "౬", "౭", "౮", "౯"]:
    print(num, int(num, base=16))

# Ref: https://unicode-table.com/
౦ 0
౧ 1
౨ 2
౩ 3
౪ 4
౫ 5
౬ 6
౭ 7
౮ 8
౯ 9
 