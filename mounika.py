a = input("Enter a string: ")
b = input("Enter b string: ")
c = input("Enter c string: ")
#checking whether above words are palindrome or not
if(a == a[::-1]):
    print(f"{a} is a palindrome")
else:
    print(f"{a} is not a palindrome")
if(b == b[::-1]):
    print(f"{b} is a palindrome")
else:
    print(f"{b} is not a palindrome")
if(c == c[::-1]):
    print(f"{c} is a palindrome")
else:
    print(f"{c} is not a palindrome")        

