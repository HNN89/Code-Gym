num=int(input("Chon 1 so tu 1 - 7: "))
day=["Chu Nhat","Thu 2","Thu 3","Thu 4","Thu 5","Thu 6","Thu 7"]
if (num<8 and num>0):
    print(day[num-1])
else:
    print("Ban da nhap sai")