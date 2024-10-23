n=int(input("3 honali sonni kiriting: "))
birlar=n%10
onlar = (n//10)%10
yuzlar = n//100
print("Natija: ", yuzlar*100+birlar*10+onlar*1)