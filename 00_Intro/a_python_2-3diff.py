# print "Hello world"    # works on in python 2
print("Hello world")

print(35+ 0)
print(35 * 0)
  
  
try:
  print(35 / 0)
except Exception as ex:
  print("Got Exception", ex)