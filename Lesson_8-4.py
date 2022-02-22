pay=int(input("Nhap so tien hang hoa: "))
if pay>=150:
    print("So tien can thanh toan la: ",pay-50)
elif pay>=100:
    print("So tien can thanh toan la: ",pay-25)
elif pay>=75:
    print("So tien can thanh toan la: ",pay-15)
else:
    print("So tien can thanh toan la: ",pay)