year=int(input('输入一个年份'))
if (year%4==0and year%100!=0)or (year%400==0):
    print('闰年')
else :
    print('不是')
