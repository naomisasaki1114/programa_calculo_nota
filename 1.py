s=input("Digite algo: ")
while (len(s)>20) or (len(s)<1):
    s=input("Digite algo: ")
cont=0

for x in range (len(s)):
    if s[x]=="a":
        cont+=1
    
print(cont)
