

```python
import numpy as np
# 文件读取
world_alcohol = np.genfromtxt("world_alcohol.txt", delimiter=",", dtype=str, skip_header=1)
print(world_alcohol)
print(type(world_alcohol))
```

    [['1986' 'Western Pacific' 'Viet Nam' 'Wine' '0']
     ['1986' 'Americas' 'Uruguay' 'Other' '0.5']
     ['1985' 'Africa' "Cte d'Ivoire" 'Wine' '1.62']
     ..., 
     ['1987' 'Africa' 'Malawi' 'Other' '0.75']
     ['1989' 'Americas' 'Bahamas' 'Wine' '1.5']
     ['1985' 'Africa' 'Malawi' 'Spirits' '0.31']]
    <class 'numpy.ndarray'>
    


```python
vector = np.array([1,2,3,4,5])
print(vector.shape)
matrix = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(matrix.shape)
print(matrix.dtype)
```

    (5,)
    (3, 3)
    int32
    


```python
# 类型 必须是同个类型
vector2 = np.array([1,"2",3,4,5])
print(vector2.dtype)
print(world_alcohol[1,0:2])
```

    <U11
    ['1986' 'Americas']
    


```python
print(matrix[:,1:3])
```

    [[2 3]
     [5 6]
     [8 9]]
    


```python
# 判断 获得布尔矩阵
print(matrix % 2 == 0)
# 用来过滤
print(matrix[matrix % 2 == 0])
```

    [[False  True False]
     [ True False  True]
     [False  True False]]
    [2 4 6 8]
    


```python
# and 操作
print((matrix % 2 == 0) & (matrix % 4 ==0))
```

    [[False False False]
     [ True False False]
     [False  True False]]
    


```python
matrix[matrix > 2].sum()
```




    42




```python
# 按列
matrix.sum(axis=0)
```




    array([12, 15, 18])




```python
# 按行
matrix.sum(axis=1)
```




    array([ 6, 15, 24])



# 几种构造方式:


```python
# 0到9 每隔1个
np.arange(0,10,1)
```




    array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])




```python
matrix2 = np.arange(15).reshape(3,5)
```


```python
matrix2.ndim
```




    2




```python
matrix2.size
```




    15




```python
matrix2.dtype
```




    dtype('int32')




```python
np.zeros((2,3))
```




    array([[ 0.,  0.,  0.],
           [ 0.,  0.,  0.]])




```python
np.ones((3,3), dtype=np.int32)
```




    array([[1, 1, 1],
           [1, 1, 1],
           [1, 1, 1]])




```python
np.random.random((3,3))
```




    array([[ 0.37497851,  0.29746481,  0.15731771],
           [ 0.34267549,  0.46344982,  0.94492579],
           [ 0.26436992,  0.38101645,  0.34686669]])




```python
# 初始值 终点(包括) 要取几个数 平均间隔
np.linspace(0,100,10, dtype=np.int32)
```




    array([  0,  11,  22,  33,  44,  55,  66,  77,  88, 100])



# 一些数学运算


```python
x = np.array([1,2,3,4,5])
y = np.array([1,2,3,4,5])
print(x - y)
print(x + 1)
print(x ** 2)
print(x * 2)
```

    [0 0 0 0 0]
    [2 3 4 5 6]
    [ 1  4  9 16 25]
    [ 2  4  6  8 10]
    


```python
a = np.array([[1,2],[3,4]])
b = np.array([[1,2],[3,4]])
print(a)
print(b)
# 对应位置相乘
print("a * b = {0}".format(a * b))
# 矩阵乘法
print("a dot b = {0}".format(a @ b))
```

    [[1 2]
     [3 4]]
    [[1 2]
     [3 4]]
    a * b = [[ 1  4]
     [ 9 16]]
    a dot b = [[ 7 10]
     [15 22]]
    


```python
np.floor(np.linspace(0,5,10))
```




    array([ 0.,  0.,  1.,  1.,  2.,  2.,  3.,  3.,  4.,  5.])




```python
# 拉平
np.zeros((2,2)).ravel()
```




    array([ 0.,  0.,  0.,  0.])




```python
# 转置 resharp使用-1自动计算
np.arange(6).reshape(2,-1).T
```




    array([[0, 3],
           [1, 4],
           [2, 5]])




```python
a = np.arange(4).reshape(2,-1)
print(a)
b = np.arange(4,8).reshape(2, -1)
print(b)
# 水平拼接
print(np.hstack((a,b)))
# 垂直拼接
print(np.vstack((a,b)))
```

    [[0 1]
     [2 3]]
    [[4 5]
     [6 7]]
    [[0 1 4 5]
     [2 3 6 7]]
    [[0 1]
     [2 3]
     [4 5]
     [6 7]]
    


```python
a = np.arange(16).reshape(4,4)
print(a)
# 垂直切 数量
print(np.vsplit(a,4))
# 水平切 数量
print(np.hsplit(a,4))
#指定位置(行 列)的切分
print(np.vsplit(a, (1,2)))
print(np.hsplit(a, (1,2)))
```

    [[ 0  1  2  3]
     [ 4  5  6  7]
     [ 8  9 10 11]
     [12 13 14 15]]
    [array([[0, 1, 2, 3]]), array([[4, 5, 6, 7]]), array([[ 8,  9, 10, 11]]), array([[12, 13, 14, 15]])]
    [array([[ 0],
           [ 4],
           [ 8],
           [12]]), array([[ 1],
           [ 5],
           [ 9],
           [13]]), array([[ 2],
           [ 6],
           [10],
           [14]]), array([[ 3],
           [ 7],
           [11],
           [15]])]
    [array([[0, 1, 2, 3]]), array([[4, 5, 6, 7]]), array([[ 8,  9, 10, 11],
           [12, 13, 14, 15]])]
    [array([[ 0],
           [ 4],
           [ 8],
           [12]]), array([[ 1],
           [ 5],
           [ 9],
           [13]]), array([[ 2,  3],
           [ 6,  7],
           [10, 11],
           [14, 15]])]
    

# 复制操作


```python
a = np.arange(12)
b = a
print(b is a)
print(id(a))
print(id(b))
```

    True
    2701409062464
    2701409062464
    


```python
a = np.arange(12).reshape(2,-1)
print(a)
# 共享底层数据
b = a.view()
print(b is a)
b.shape = 3,-1
print(b.shape)
print(a.shape)
b[0,0]=11111
print(a)
# reshape返回的新的其实也是共享底层数据
a.reshape(1,-1)[0,0]=2222
print(a)
```

    [[ 0  1  2  3  4  5]
     [ 6  7  8  9 10 11]]
    False
    (3, 4)
    (2, 6)
    [[11111     1     2     3     4     5]
     [    6     7     8     9    10    11]]
    [[2222    1    2    3    4    5]
     [   6    7    8    9   10   11]]
    


```python
a = np.arange(12).reshape(2,-1)
print(a)
# 拷贝 没有关联
b = a.copy()
print(b is a)
b.shape = 3,-1
print(b.shape)
print(a.shape)
b[0,0]=11111
print(a)
```

    [[ 0  1  2  3  4  5]
     [ 6  7  8  9 10 11]]
    False
    (3, 4)
    (2, 6)
    [[ 0  1  2  3  4  5]
     [ 6  7  8  9 10 11]]
    

# 其他操作


```python
a = np.arange(20).reshape(5,4)
# 带arg的是取索引的操作
ind = a.argmax(axis=0)
print(a)
print(ind)
```

    [[ 0  1  2  3]
     [ 4  5  6  7]
     [ 8  9 10 11]
     [12 13 14 15]
     [16 17 18 19]]
    [4 4 4 4]
    


```python
a = np.arange(4)
print(a)
# 扩展
print(np.tile(a,(4,3)))
```

    [0 1 2 3]
    [[0 1 2 3 0 1 2 3 0 1 2 3]
     [0 1 2 3 0 1 2 3 0 1 2 3]
     [0 1 2 3 0 1 2 3 0 1 2 3]
     [0 1 2 3 0 1 2 3 0 1 2 3]]
    
