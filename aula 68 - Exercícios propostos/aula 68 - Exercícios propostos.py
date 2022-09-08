
string = '01234567890123456789012345678901234567890123456789'
x = 10
l1 = [string[i:i+x] for i in range(0, len(string), x)]
print(l1)
print(".".join(l1))