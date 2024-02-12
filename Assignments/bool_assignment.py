print("bool(33)          ", bool(33))
print("bool(-33)         ", bool(-33))
print("bool(0.00)        ", bool(0.00))
print("bool(0.000000001) ", bool(0.0000001))
print("bool(-0.000000001)", bool(-0.00000000000000000001))
print("bool(0.01)        ", bool(0.00000000000000000000000000000000000000000000000000000000001))
# Assignment - after decimal, if you write how many zeros followed by 1 in last, will make the result as False
# Answer: It wont happen because floating point numbers close to 0 or  even with many number of zeros after the decimal point are still considered non-zero.