chieucao=float(input("Nhap chieu cao cua ban (cm): "))/100
cannang=float(input("Nhap can nang cuar ban (kG): "))
bmi=cannang/chieucao/chieucao
print("Chi so BMI cua ban la: ",bmi)
if bmi>40:
    print("Ban bi beo phi cap do III")
elif bmi>=35:
    print("Ban bi beo phi cap do II")
elif bmi>=30:
    print("Ban bi beo phi cap do I")
elif bmi>=25:
    print("Ban bi thua can")
elif bmi>=18.5:
    print("Chuc mung! ban co can nang ly tuong")
elif bmi>=17:
    print("Ban bi gay cap do I")
elif bmi>=16:
    print("Ban bi gay cap do II")
else :
    print("Ban bi gay cap do III")