n=int(input("N sekund ni kiriting: "))
print("Natija: ", n//60)
print("Soatni hisoblash: ", n//3600)

soat = n//3600
minut = (n-soat*3600)//60
secund = (n-soat*3600)%60
print(soat, minut, secund)