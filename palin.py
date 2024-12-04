num=int(input("Enter a nimber \n"))
rev=0;d=0

dup=num

while num>0:
    d=num%10
    rev=rev*10+d
    num=num//10

if rev ==dup:
    print("palindrome")
      