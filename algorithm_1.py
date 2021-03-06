﻿# -*- coding: utf-8 -*-

"""算法逻辑训练""""

from collections import Counter, defaultdict

# one :  以下是用户id对应的技能爱好，比如(0, "Hadoop")表示0号用户爱好是Hadoop
#        根据以下数据集，给一个用户id，算出与该用户技能爱好最多的其他用户（可能有多个）
interests = [
 (0, "Hadoop"), (0, "Big Data"), (0, "HBase"), (0, "Java"),
 (0, "Spark"), (0, "Storm"), (0, "Cassandra"),
 (1, "NoSQL"), (1, "MongoDB"), (1, "Cassandra"), (1, "HBase"),
 (1, "Postgres"), (2, "Python"), (2, "scikit-learn"), (2, "scipy"),
 (2, "numpy"), (2, "statsmodels"), (2, "pandas"), (3, "R"), (3, "Python"),
 (3, "statistics"), (3, "regression"), (3, "probability"),
 (4, "machine learning"), (4, "regression"), (4, "decision trees"),
 (4, "libsvm"), (5, "Python"), (5, "R"), (5, "Java"), (5, "C++"),
 (5, "Haskell"), (5, "programming languages"), (6, "statistics"),
 (6, "probability"), (6, "mathematics"), (6, "theory"),
 (7, "machine learning"), (7, "scikit-learn"), (7, "Mahout"),
 (7, "neural networks"), (8, "neural networks"), (8, "deep learning"),
 (8, "Big Data"), (8, "artificial intelligence"), (9, "Hadoop"),
 (9, "Java"), (9, "MapReduce"), (9, "Big Data")
]


def get_set():
    """每个用户对应的所有技能爱好"""
    a = set()
    for i, j in interests:
        a.add(i)
    r_list = list(a)
    r_dic = {num: set() for num in r_list}
    for a in r_dic:
        for i, j in interests:
            if i == a:
                r_dic[a].add(j)
    return r_dic


def get_person(id):
    if id not in get_set():
        print('用户无效')
        return None
    r_dic = get_set()
    obj = r_dic[id]
    same_num = [(0, 0)]
    for i in r_dic:
        s_list = [i[0] for i in same_num]
        if i == id or i in s_list:
            continue
        num = len(r_dic[i] & obj)
        if num > same_num[0][1]:
            same_num=[]
            same_num.append((i, num))
            continue
        if num == same_num[0][1]:
            same_num.append((i, num))
    return same_num
print(get_person(0))


# two :  以下是一个元素是序号和值组成的元祖的列表，相同序号的元祖的值相加，得到一个没有重复序号的新列表
#       a = [(105, 1), (101, 2), (104, 3), (105, 4)]  -->  a = [(105, 5), (101, 2), (104, 3)] 顺序可以改变
#  方法一：
a = [(105, 1), (101, 2), (104, 3), (105, 4)]
r_set = {i[0] for i in a}
b = [[i, 0] for i in list(r_set)]
for i in b:
    for j in a:
        if i[0] == j[0]:
            i[1] += j[1]
c = [tuple(i) for i in b]
print(c)

# 方法二：
d = defaultdict(list)  # 设置字典d的value默认是列表
for k, v in a:
   d[k].append(v)
r_list = [(i, sum(dict(d)[i])) for i in dict(d)]
print(r_list)


# three :  实现字符串形式的二进制加法运算：
#          '1100' + '10101' = '100001'
#  方法一：
def my_bites(a, b):
    """将两个字符串二进制数变成列表，并将元素少的用0补充与元素多的等长，再相加"""
    middle = 0  # 进位数（只可能是1或者0）
    result = ''
    a_list = [int(i) for i in a][::-1]
    b_list = [int(i) for i in b][::-1]
    max_s, min_s = (a_list, b_list) if len(a) > len(b) else (b_list, a_list)
    for _ in range(len(max_s)-len(min_s)):
        min_s.append(0)
    for i in range(len(max_s)):
        if max_s[i]+min_s[i]+middle >= 2:
            result += str(max_s[i]+min_s[i]+middle-2)
            middle = 1
        else:
            result += str(max_s[i] + min_s[i] + middle)
            middle = 0
    if middle:
        result += '1'
    return result[::-1]
print(my_bites('1100','10101'))


# 方法二：
def add_bin(a, b):
    a_b = int(a, 2)
    b_b = int(b, 2)
    return bin(a_b+b_b)[2:]
print(add_bin('1100', '10101'))


# four:  实现机械学习KNN算法
def distance(a, b):
    """计算两个向量距离"""
    sum_d = 0
    for i in range(len(a)):
        sum_d += (a[i] - b[i]) ** 2
    return sum_d**0.5


def my_knn(test_data, cla, data, k):
    d_list = [(cla[i], distance(data, test_data[i])) for i in range(len(test_data))]
    d_list.sort(key=lambda x: x[1])
    r_list = [i[0] for i in d_list][:k]
    r_c = Counter(r_list).most_common()[0][0]
    return r_c


# 测试KNN算法
test_data = [(1, 150), (4, 123), (130, 2), (148, 8)]
cla = ['love', 'love', 'action', 'action']
data = (45, 46)
k = 3
print(my_knn(test_data, cla, data, k))


# five :  有一千盏灯，全都是灭的，第一个人从第一盏灯开始全都按一下，第二个人
#         从第二盏灯开始往后的等都按一下，第三个人从第三盏灯开始往后的等都按
#         一下，以此类推，有一千个人，问最后有多少灯是亮着的，多少灯是灭的
# 0 代表灯是灭的状态 , 1 代表灯是亮的状态
a = [0 for _ in range(1000)]
for i in range(1000):
    i += 1
    for j in range(1, 1001):
        if i//j == 0:
            a[i-1] = 0 if a[i-1] else 1
print(a)
print(f'灭的灯共:{a.count(0)}盏')
print(f'亮的灯共:{a.count(1)}盏')


# six :  替换某个字符串中的一个或者多个子串
# 方法一
def str_replace(ostr, old_str, new_str):
    list_s = ostr.split(old_str)
    str_result = ''
    for strs in list_s[:-1]:
        str_result += strs+new_str
    return str_result+list_s[-1]
a = 'heluollo luoshuxiaoluoll'
print(str_replace(a, 'luo', '##'))


# 方法二
def str_replace1(ostr, old_str, new_str):
    return ostr.replace(old_str, new_str)
print(str_replace1(a, 'luo', '##'))


# seven : 冒泡排序算法
def my_sort(list1):
    for i in range(len(list1)):
        for j in range(i+1, len(list1)):
            if list1[i] > list1[j]:
                list1[i], list1[j] = list1[j], list1[i]
    return list1


# eight :  100课糖随机分配给10个小朋友，求糖果获得第n多的小朋友获得的糖果（不能用语言自带的排序）

def my_sorted(ch_list, k):
    for i in range(len(ch_list)):
        for j in range(len(ch_list)-1):
            if ch_list[i] > ch_list[j]:
                ch_list[i], ch_list[j] = ch_list[j], ch_list[i]
    num = ch_list[0]
    n = 1
    for i in ch_list[1:]:
        if i == num:
            continue
        else:
            n += 1
            num = i
            if n == k:
                return i
    else:
        print('输入错误')
        
        
ch_list = [10, 30, 5, 7, 12, 20, 3, 3, 10]
k = 3
print(my_sorted(ch_list, 3))


# night ： 归并排序算法
def split_data(data):
    if len(data) == 1:
        return data
    mid = len(data)//2
    left_data = data[:mid]
    right_data = data[mid:]
    left = split_data(left_data)
    right = split_data(right_data)
    return merger_sort(left,right)

def merger_sort(left_list,right_list):
    result = []
    while len(left_list)>0 and len(right_list)>0:
        if left_list[0] >= right_list[0]:
            result.append(left_list.pop(0))
        else:
            result.append(right_list.pop(0))
    result.extend(left_list)
    result.extend(right_list)
    return result


test_list = [1, 2, 1, 5, 6, 7, 10, 43, 24, 45, 23]
print(split_data(test_list))

# ten : 快速排序

def quick_sort(lis):
    if len(lis) > 1:
        left, right = [], []
        mid = lis[len(lis)//2]
        lis.remove(mid)
        for i in lis:
            if i >= mid:
                right.append(i)
            else:
                left.append(i)
        return quick_sort(left)+[mid]+quick_sort(right)
    return lis

# eleven : 二分查找

def bin_search(link, val):
    min = 0
    max = len(link)-1
    while min <= max:
        mid = (min+max)//2
        if val == link[mid]:
            return mid
        elif val > link[mid]:
            min = mid+1
        elif val < link[mid]:
            max = mid-1
    return None

# twelve : 斐波那契数列

def feibolaqi(num):
    a, b, c = 0, 1, []
    for i in range(num-1):
        c.append(b)
        a, b = b, a+b
    c.append(b)
    return b,c
其中：b代表第num个斐波那契数，c代表前num个斐波拉契数

# thirteen : python实现双向链表

# fourteen : 判断一个数是不是快乐数
#     快乐数：对于正整数，每一次将该数替换为它每个
#             位置上的数字的平方和，然后重复这个过程直到这个数
#             变为1，也可能是无限循环始终变不到1，如果可以变为1，
#             那么这个数就是快乐数

# fifteen : python实现二叉树