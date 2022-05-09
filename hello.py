#!/usr/bin/python
# -*- coding: UTF-8 -*-
# print('hello!world')

name = 100;
set = 'wqeqe231';
list = [ 'runoob', 786 , 2.23, 'john', 70.2 ];
lists = {
    'name': '老王',
    'id':'23q'
}
a = 8;
b = 6;
c = 0;

c = a % b;
print('c的值为：',c)

print(name);
print(set[2:5]); #输出下标2到5之间的字母
print(list[1]); #输出元组的第一个元素
print(lists);
print(lists.keys());
print(lists.values());

# Fibonacci series: 斐波纳契数列
# 两个元素的总和确定了下一个数
a, b = 0, 1
while b < 10:
    # print(b);
    print(b,end=',');
    a, b = b, a+b; #a=b,b=a+b

cls = 0;
while(cls < 6):
    print(' ');
    cls += 1;

nums = 0;
suma = 1;
while(suma <= 100):
      nums = nums + suma;
      suma += 1;
print('sum:%d,%d'%(suma,nums));

# age = int(input('请输入年龄'));
# print('......');
# if (age < 0):{
#     print('输入有误！')
# }    
# elif (age == 1):{
#      print('年龄为1')
# }
# elif (age >= 2):{
#     print('年岁已高')  
# }
    
