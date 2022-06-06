year=int(input("請輸入年份："))
print("您输入的是",year,"年")
x=year%4
y=year%100
z=year%400
if  x==0:
   if y!=0 or z==0:
    print("%s是閏年"%year)
else:
    print("%s不是閏年"%year)
