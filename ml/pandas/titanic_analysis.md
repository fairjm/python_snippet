

```python
import pandas as pd
data = pd.read_csv("titanic_train.csv")
print(len(data))
data.head(4)
```

    891
    




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>PassengerId</th>
      <th>Survived</th>
      <th>Pclass</th>
      <th>Name</th>
      <th>Sex</th>
      <th>Age</th>
      <th>SibSp</th>
      <th>Parch</th>
      <th>Ticket</th>
      <th>Fare</th>
      <th>Cabin</th>
      <th>Embarked</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>0</td>
      <td>3</td>
      <td>Braund, Mr. Owen Harris</td>
      <td>male</td>
      <td>22.0</td>
      <td>1</td>
      <td>0</td>
      <td>A/5 21171</td>
      <td>7.2500</td>
      <td>NaN</td>
      <td>S</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>1</td>
      <td>1</td>
      <td>Cumings, Mrs. John Bradley (Florence Briggs Th...</td>
      <td>female</td>
      <td>38.0</td>
      <td>1</td>
      <td>0</td>
      <td>PC 17599</td>
      <td>71.2833</td>
      <td>C85</td>
      <td>C</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>1</td>
      <td>3</td>
      <td>Heikkinen, Miss. Laina</td>
      <td>female</td>
      <td>26.0</td>
      <td>0</td>
      <td>0</td>
      <td>STON/O2. 3101282</td>
      <td>7.9250</td>
      <td>NaN</td>
      <td>S</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
      <td>1</td>
      <td>1</td>
      <td>Futrelle, Mrs. Jacques Heath (Lily May Peel)</td>
      <td>female</td>
      <td>35.0</td>
      <td>1</td>
      <td>0</td>
      <td>113803</td>
      <td>53.1000</td>
      <td>C123</td>
      <td>S</td>
    </tr>
  </tbody>
</table>
</div>




```python
# age分析 找出为缺失的
age = data["Age"]
age_is_null = pd.isnull(age)
# 用等len的boolean作为index筛选
age_is_null_true = age[age_is_null]
print(age_is_null_true.head(3))
print(len(age_is_null_true))
good_age = age[age_is_null == False]
print(len(good_age))
print(age.sum())
print(good_age.sum())
```

    5    NaN
    17   NaN
    19   NaN
    Name: Age, dtype: float64
    177
    714
    21205.17
    21205.17
    


```python
# 使用py自己的sum sum(data['Age']) 如果有nan 放返回nan 这里不用担心
mean_age = data["Age"].sum() / len(data["Age"])
print(mean_age)
mean_age = data["Age"].sum() / len(good_age)
print(mean_age)
print(data["Age"].mean())
```

    23.79929292929293
    29.69911764705882
    29.69911764705882
    

2018/07/12 02:33


```python
# 不同舱的均价
passenger_classes = [1,2,3]
fares_by_class = {}
for c in passenger_classes:
    data_class = data[data["Pclass"] == c]
    fares_by_class[c] = data_class["Fare"].mean()
print(fares_by_class)
```

    {1: 84.15468749999992, 2: 20.66218315217391, 3: 13.675550101832997}
    


```python
# 可以用pivot_table这个函数
# 求出获救的平均人数
import numpy as np
pass_survial = data.pivot_table(index="Pclass",values="Survived", aggfunc=np.mean)
print(pass_survial)
```

            Survived
    Pclass          
    1       0.629630
    2       0.472826
    3       0.242363
    


```python
pass_age = data.pivot_table(index=["Pclass","Survived"],values="Age", aggfunc=np.mean)
print(pass_age)
```

                           Age
    Pclass Survived           
    1      0         43.695312
           1         35.368197
    2      0         33.544444
           1         25.901566
    3      0         26.555556
           1         20.646118
    


```python
# 1是列或者指定columns 如果列数据有na就把列去掉
drop_na_cols = data.dropna(axis=1)
print(drop_na_cols.head(2))
# 行 根据指定的列如果是na就去除该行
drop_na_rows = data.dropna(axis=0, subset=['Age','Sex'])
print(drop_na_rows.head(2))
```

       PassengerId  Survived  Pclass  \
    0            1         0       3   
    1            2         1       1   
    
                                                    Name     Sex  SibSp  Parch  \
    0                            Braund, Mr. Owen Harris    male      1      0   
    1  Cumings, Mrs. John Bradley (Florence Briggs Th...  female      1      0   
    
          Ticket     Fare  
    0  A/5 21171   7.2500  
    1   PC 17599  71.2833  
       PassengerId  Survived  Pclass  \
    0            1         0       3   
    1            2         1       1   
    
                                                    Name     Sex   Age  SibSp  \
    0                            Braund, Mr. Owen Harris    male  22.0      1   
    1  Cumings, Mrs. John Bradley (Florence Briggs Th...  female  38.0      1   
    
       Parch     Ticket     Fare Cabin Embarked  
    0      0  A/5 21171   7.2500   NaN        S  
    1      0   PC 17599  71.2833   C85        C  
    


```python
sort_by_age = data.sort_values("Age")
print(sort_by_age.head(2))
```

         PassengerId  Survived  Pclass                             Name   Sex  \
    803          804         1       3  Thomas, Master. Assad Alexander  male   
    755          756         1       2        Hamalainen, Master. Viljo  male   
    
          Age  SibSp  Parch  Ticket     Fare Cabin Embarked  
    803  0.42      0      1    2625   8.5167   NaN        C  
    755  0.67      1      1  250649  14.5000   NaN        S  
    


```python
# drop=True不会新增一列index(原来旧的)
print(sort_by_age.reset_index(drop=True).head(2))
```

       PassengerId  Survived  Pclass                             Name   Sex   Age  \
    0          804         1       3  Thomas, Master. Assad Alexander  male  0.42   
    1          756         1       2        Hamalainen, Master. Viljo  male  0.67   
    
       SibSp  Parch  Ticket     Fare Cabin Embarked  
    0      0      1    2625   8.5167   NaN        C  
    1      1      1  250649  14.5000   NaN        S  
    


```python
# 自定义函数 axis=1 是行操作 传入row
def not_null_count(column):
    column_null = pd.isnull(column)
    return len(column[column_null == False])
print(data.apply(not_null_count))
```

    PassengerId    891
    Survived       891
    Pclass         891
    Name           891
    Sex            891
    Age            714
    SibSp          891
    Parch          891
    Ticket         891
    Fare           891
    Cabin          204
    Embarked       889
    dtype: int64
    


```python
def generate_label(row):
    age = row['Age']
    if(pd.isnull(age)):
        return "unknown"
    elif age < 18:
        return "minor"
    else:
        return "adult"
data["age_label"] = data.apply(generate_label,axis=1)
print(data.head(2))
```

       PassengerId  Survived  Pclass  \
    0            1         0       3   
    1            2         1       1   
    
                                                    Name     Sex   Age  SibSp  \
    0                            Braund, Mr. Owen Harris    male  22.0      1   
    1  Cumings, Mrs. John Bradley (Florence Briggs Th...  female  38.0      1   
    
       Parch     Ticket     Fare Cabin Embarked age_label  
    0      0  A/5 21171   7.2500   NaN        S     adult  
    1      0   PC 17599  71.2833   C85        C     adult  
    


```python
print(data.pivot_table(index = "age_label", values="Survived"))
```

               Survived
    age_label          
    adult      0.381032
    minor      0.539823
    unknown    0.293785
    
