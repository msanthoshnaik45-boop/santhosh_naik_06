s=input("enter line of text")
cons=0
vowels=0
digits=0
for ch in s:
    if ch.lower() in " a e i o u ":
        vowels+=1
    elif ch.isalpha():
      cons+=1
    elif ch.isdigit():
      digits+=1
print("vowels:{}\nconsonants:{}\ndigits:{}".format(vowels,cons,digits))
         
