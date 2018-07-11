
基于numpy,提供更强的功能和方便的操作.

# 文件读取


```python
import pandas as pd
food_info = pd.read_csv("food_info.csv")
print(type(food_info))
```

    <class 'pandas.core.frame.DataFrame'>
    

数据类型不需要和numpy一样一致.


```python
print(food_info.dtypes)
```

    NDB_No               int64
    Shrt_Desc           object
    Water_(g)          float64
    Energ_Kcal           int64
    Protein_(g)        float64
    Lipid_Tot_(g)      float64
    Ash_(g)            float64
    Carbohydrt_(g)     float64
    Fiber_TD_(g)       float64
    Sugar_Tot_(g)      float64
    Calcium_(mg)       float64
    Iron_(mg)          float64
    Magnesium_(mg)     float64
    Phosphorus_(mg)    float64
    Potassium_(mg)     float64
    Sodium_(mg)        float64
    Zinc_(mg)          float64
    Copper_(mg)        float64
    Manganese_(mg)     float64
    Selenium_(mcg)     float64
    Vit_C_(mg)         float64
    Thiamin_(mg)       float64
    Riboflavin_(mg)    float64
    Niacin_(mg)        float64
    Vit_B6_(mg)        float64
    Vit_B12_(mcg)      float64
    Vit_A_IU           float64
    Vit_A_RAE          float64
    Vit_E_(mg)         float64
    Vit_D_mcg          float64
    Vit_D_IU           float64
    Vit_K_(mcg)        float64
    FA_Sat_(g)         float64
    FA_Mono_(g)        float64
    FA_Poly_(g)        float64
    Cholestrl_(mg)     float64
    dtype: object
    

# 常用操作


```python
# 默认前5条
food_info.head()
```




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
      <th>NDB_No</th>
      <th>Shrt_Desc</th>
      <th>Water_(g)</th>
      <th>Energ_Kcal</th>
      <th>Protein_(g)</th>
      <th>Lipid_Tot_(g)</th>
      <th>Ash_(g)</th>
      <th>Carbohydrt_(g)</th>
      <th>Fiber_TD_(g)</th>
      <th>Sugar_Tot_(g)</th>
      <th>...</th>
      <th>Vit_A_IU</th>
      <th>Vit_A_RAE</th>
      <th>Vit_E_(mg)</th>
      <th>Vit_D_mcg</th>
      <th>Vit_D_IU</th>
      <th>Vit_K_(mcg)</th>
      <th>FA_Sat_(g)</th>
      <th>FA_Mono_(g)</th>
      <th>FA_Poly_(g)</th>
      <th>Cholestrl_(mg)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1001</td>
      <td>BUTTER WITH SALT</td>
      <td>15.87</td>
      <td>717</td>
      <td>0.85</td>
      <td>81.11</td>
      <td>2.11</td>
      <td>0.06</td>
      <td>0.0</td>
      <td>0.06</td>
      <td>...</td>
      <td>2499.0</td>
      <td>684.0</td>
      <td>2.32</td>
      <td>1.5</td>
      <td>60.0</td>
      <td>7.0</td>
      <td>51.368</td>
      <td>21.021</td>
      <td>3.043</td>
      <td>215.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1002</td>
      <td>BUTTER WHIPPED WITH SALT</td>
      <td>15.87</td>
      <td>717</td>
      <td>0.85</td>
      <td>81.11</td>
      <td>2.11</td>
      <td>0.06</td>
      <td>0.0</td>
      <td>0.06</td>
      <td>...</td>
      <td>2499.0</td>
      <td>684.0</td>
      <td>2.32</td>
      <td>1.5</td>
      <td>60.0</td>
      <td>7.0</td>
      <td>50.489</td>
      <td>23.426</td>
      <td>3.012</td>
      <td>219.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1003</td>
      <td>BUTTER OIL ANHYDROUS</td>
      <td>0.24</td>
      <td>876</td>
      <td>0.28</td>
      <td>99.48</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.0</td>
      <td>0.00</td>
      <td>...</td>
      <td>3069.0</td>
      <td>840.0</td>
      <td>2.80</td>
      <td>1.8</td>
      <td>73.0</td>
      <td>8.6</td>
      <td>61.924</td>
      <td>28.732</td>
      <td>3.694</td>
      <td>256.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1004</td>
      <td>CHEESE BLUE</td>
      <td>42.41</td>
      <td>353</td>
      <td>21.40</td>
      <td>28.74</td>
      <td>5.11</td>
      <td>2.34</td>
      <td>0.0</td>
      <td>0.50</td>
      <td>...</td>
      <td>721.0</td>
      <td>198.0</td>
      <td>0.25</td>
      <td>0.5</td>
      <td>21.0</td>
      <td>2.4</td>
      <td>18.669</td>
      <td>7.778</td>
      <td>0.800</td>
      <td>75.0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>1005</td>
      <td>CHEESE BRICK</td>
      <td>41.11</td>
      <td>371</td>
      <td>23.24</td>
      <td>29.68</td>
      <td>3.18</td>
      <td>2.79</td>
      <td>0.0</td>
      <td>0.51</td>
      <td>...</td>
      <td>1080.0</td>
      <td>292.0</td>
      <td>0.26</td>
      <td>0.5</td>
      <td>22.0</td>
      <td>2.5</td>
      <td>18.764</td>
      <td>8.598</td>
      <td>0.784</td>
      <td>94.0</td>
    </tr>
  </tbody>
</table>
<p>5 rows × 36 columns</p>
</div>




```python
food_info.head(3)
```




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
      <th>NDB_No</th>
      <th>Shrt_Desc</th>
      <th>Water_(g)</th>
      <th>Energ_Kcal</th>
      <th>Protein_(g)</th>
      <th>Lipid_Tot_(g)</th>
      <th>Ash_(g)</th>
      <th>Carbohydrt_(g)</th>
      <th>Fiber_TD_(g)</th>
      <th>Sugar_Tot_(g)</th>
      <th>...</th>
      <th>Vit_A_IU</th>
      <th>Vit_A_RAE</th>
      <th>Vit_E_(mg)</th>
      <th>Vit_D_mcg</th>
      <th>Vit_D_IU</th>
      <th>Vit_K_(mcg)</th>
      <th>FA_Sat_(g)</th>
      <th>FA_Mono_(g)</th>
      <th>FA_Poly_(g)</th>
      <th>Cholestrl_(mg)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1001</td>
      <td>BUTTER WITH SALT</td>
      <td>15.87</td>
      <td>717</td>
      <td>0.85</td>
      <td>81.11</td>
      <td>2.11</td>
      <td>0.06</td>
      <td>0.0</td>
      <td>0.06</td>
      <td>...</td>
      <td>2499.0</td>
      <td>684.0</td>
      <td>2.32</td>
      <td>1.5</td>
      <td>60.0</td>
      <td>7.0</td>
      <td>51.368</td>
      <td>21.021</td>
      <td>3.043</td>
      <td>215.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1002</td>
      <td>BUTTER WHIPPED WITH SALT</td>
      <td>15.87</td>
      <td>717</td>
      <td>0.85</td>
      <td>81.11</td>
      <td>2.11</td>
      <td>0.06</td>
      <td>0.0</td>
      <td>0.06</td>
      <td>...</td>
      <td>2499.0</td>
      <td>684.0</td>
      <td>2.32</td>
      <td>1.5</td>
      <td>60.0</td>
      <td>7.0</td>
      <td>50.489</td>
      <td>23.426</td>
      <td>3.012</td>
      <td>219.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1003</td>
      <td>BUTTER OIL ANHYDROUS</td>
      <td>0.24</td>
      <td>876</td>
      <td>0.28</td>
      <td>99.48</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.0</td>
      <td>0.00</td>
      <td>...</td>
      <td>3069.0</td>
      <td>840.0</td>
      <td>2.80</td>
      <td>1.8</td>
      <td>73.0</td>
      <td>8.6</td>
      <td>61.924</td>
      <td>28.732</td>
      <td>3.694</td>
      <td>256.0</td>
    </tr>
  </tbody>
</table>
<p>3 rows × 36 columns</p>
</div>




```python
# 同理还有tail
food_info.tail()
```




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
      <th>NDB_No</th>
      <th>Shrt_Desc</th>
      <th>Water_(g)</th>
      <th>Energ_Kcal</th>
      <th>Protein_(g)</th>
      <th>Lipid_Tot_(g)</th>
      <th>Ash_(g)</th>
      <th>Carbohydrt_(g)</th>
      <th>Fiber_TD_(g)</th>
      <th>Sugar_Tot_(g)</th>
      <th>...</th>
      <th>Vit_A_IU</th>
      <th>Vit_A_RAE</th>
      <th>Vit_E_(mg)</th>
      <th>Vit_D_mcg</th>
      <th>Vit_D_IU</th>
      <th>Vit_K_(mcg)</th>
      <th>FA_Sat_(g)</th>
      <th>FA_Mono_(g)</th>
      <th>FA_Poly_(g)</th>
      <th>Cholestrl_(mg)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>8613</th>
      <td>83110</td>
      <td>MACKEREL SALTED</td>
      <td>43.00</td>
      <td>305</td>
      <td>18.50</td>
      <td>25.10</td>
      <td>13.40</td>
      <td>0.00</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>...</td>
      <td>157.0</td>
      <td>47.0</td>
      <td>2.38</td>
      <td>25.2</td>
      <td>1006.0</td>
      <td>7.8</td>
      <td>7.148</td>
      <td>8.320</td>
      <td>6.210</td>
      <td>95.0</td>
    </tr>
    <tr>
      <th>8614</th>
      <td>90240</td>
      <td>SCALLOP (BAY&amp;SEA) CKD STMD</td>
      <td>70.25</td>
      <td>111</td>
      <td>20.54</td>
      <td>0.84</td>
      <td>2.97</td>
      <td>5.41</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>...</td>
      <td>5.0</td>
      <td>2.0</td>
      <td>0.00</td>
      <td>0.0</td>
      <td>2.0</td>
      <td>0.0</td>
      <td>0.218</td>
      <td>0.082</td>
      <td>0.222</td>
      <td>41.0</td>
    </tr>
    <tr>
      <th>8615</th>
      <td>90480</td>
      <td>SYRUP CANE</td>
      <td>26.00</td>
      <td>269</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.86</td>
      <td>73.14</td>
      <td>0.0</td>
      <td>73.2</td>
      <td>...</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.00</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.000</td>
      <td>0.000</td>
      <td>0.000</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>8616</th>
      <td>90560</td>
      <td>SNAIL RAW</td>
      <td>79.20</td>
      <td>90</td>
      <td>16.10</td>
      <td>1.40</td>
      <td>1.30</td>
      <td>2.00</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>...</td>
      <td>100.0</td>
      <td>30.0</td>
      <td>5.00</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.1</td>
      <td>0.361</td>
      <td>0.259</td>
      <td>0.252</td>
      <td>50.0</td>
    </tr>
    <tr>
      <th>8617</th>
      <td>93600</td>
      <td>TURTLE GREEN RAW</td>
      <td>78.50</td>
      <td>89</td>
      <td>19.80</td>
      <td>0.50</td>
      <td>1.20</td>
      <td>0.00</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>...</td>
      <td>100.0</td>
      <td>30.0</td>
      <td>0.50</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.1</td>
      <td>0.127</td>
      <td>0.088</td>
      <td>0.170</td>
      <td>50.0</td>
    </tr>
  </tbody>
</table>
<p>5 rows × 36 columns</p>
</div>




```python
# 数据形状
food_info.shape
```




    (8618, 36)




```python
# 根据行进行数据获取  要注意区间是都闭合的
print(food_info.loc[0:1])
print("===============================================================")
print(food_info.loc[[0,1]])
```

       NDB_No                 Shrt_Desc  Water_(g)  Energ_Kcal  Protein_(g)  \
    0    1001          BUTTER WITH SALT      15.87         717         0.85   
    1    1002  BUTTER WHIPPED WITH SALT      15.87         717         0.85   
    
       Lipid_Tot_(g)  Ash_(g)  Carbohydrt_(g)  Fiber_TD_(g)  Sugar_Tot_(g)  \
    0          81.11     2.11            0.06           0.0           0.06   
    1          81.11     2.11            0.06           0.0           0.06   
    
            ...        Vit_A_IU  Vit_A_RAE  Vit_E_(mg)  Vit_D_mcg  Vit_D_IU  \
    0       ...          2499.0      684.0        2.32        1.5      60.0   
    1       ...          2499.0      684.0        2.32        1.5      60.0   
    
       Vit_K_(mcg)  FA_Sat_(g)  FA_Mono_(g)  FA_Poly_(g)  Cholestrl_(mg)  
    0          7.0      51.368       21.021        3.043           215.0  
    1          7.0      50.489       23.426        3.012           219.0  
    
    [2 rows x 36 columns]
    ===============================================================
       NDB_No                 Shrt_Desc  Water_(g)  Energ_Kcal  Protein_(g)  \
    0    1001          BUTTER WITH SALT      15.87         717         0.85   
    1    1002  BUTTER WHIPPED WITH SALT      15.87         717         0.85   
    
       Lipid_Tot_(g)  Ash_(g)  Carbohydrt_(g)  Fiber_TD_(g)  Sugar_Tot_(g)  \
    0          81.11     2.11            0.06           0.0           0.06   
    1          81.11     2.11            0.06           0.0           0.06   
    
            ...        Vit_A_IU  Vit_A_RAE  Vit_E_(mg)  Vit_D_mcg  Vit_D_IU  \
    0       ...          2499.0      684.0        2.32        1.5      60.0   
    1       ...          2499.0      684.0        2.32        1.5      60.0   
    
       Vit_K_(mcg)  FA_Sat_(g)  FA_Mono_(g)  FA_Poly_(g)  Cholestrl_(mg)  
    0          7.0      51.368       21.021        3.043           215.0  
    1          7.0      50.489       23.426        3.012           219.0  
    
    [2 rows x 36 columns]
    


```python
# 根据列名取获取列 一样可以用list获取
food_info["NDB_No"][0:1]
```




    0    1001
    Name: NDB_No, dtype: int64




```python
columns = food_info.columns.tolist()
gram_c = []
for c in columns:
    if c.endswith("(g)"):
        gram_c.append(c)
food_info[gram_c].head(2)
```




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
      <th>Water_(g)</th>
      <th>Protein_(g)</th>
      <th>Lipid_Tot_(g)</th>
      <th>Ash_(g)</th>
      <th>Carbohydrt_(g)</th>
      <th>Fiber_TD_(g)</th>
      <th>Sugar_Tot_(g)</th>
      <th>FA_Sat_(g)</th>
      <th>FA_Mono_(g)</th>
      <th>FA_Poly_(g)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>15.87</td>
      <td>0.85</td>
      <td>81.11</td>
      <td>2.11</td>
      <td>0.06</td>
      <td>0.0</td>
      <td>0.06</td>
      <td>51.368</td>
      <td>21.021</td>
      <td>3.043</td>
    </tr>
    <tr>
      <th>1</th>
      <td>15.87</td>
      <td>0.85</td>
      <td>81.11</td>
      <td>2.11</td>
      <td>0.06</td>
      <td>0.0</td>
      <td>0.06</td>
      <td>50.489</td>
      <td>23.426</td>
      <td>3.012</td>
    </tr>
  </tbody>
</table>
</div>




```python
# 数学计算 和numpy差不多
w2 = food_info["Water_(g)"] * 2
w2.head(2)
```




    0    31.74
    1    31.74
    Name: Water_(g), dtype: float64




```python
water_energy = food_info["Water_(g)"] * food_info["Energ_Kcal"]
print(water_energy.head(2))
print(water_energy.shape)
food_info["water_(mg)"] = food_info["Water_(g)"] / 1000
print(food_info.shape)
```

    0    11378.79
    1    11378.79
    dtype: float64
    (8618,)
    (8618, 37)
    


```python
# 一些统计函数
print(food_info["water_(mg)"].max())
print(food_info["water_(mg)"].min())
print(food_info["water_(mg)"].sum())
print(food_info["water_(mg)"].count())
```

    0.1
    0.0
    466.4578700000006
    8612
    


```python
# 排序操作 默认会返回一个新的 用inplace指定原地排序
food_info.sort_values("NDB_No", inplace=True, ascending=False)
food_info.head(2)
```




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
      <th>NDB_No</th>
      <th>Shrt_Desc</th>
      <th>Water_(g)</th>
      <th>Energ_Kcal</th>
      <th>Protein_(g)</th>
      <th>Lipid_Tot_(g)</th>
      <th>Ash_(g)</th>
      <th>Carbohydrt_(g)</th>
      <th>Fiber_TD_(g)</th>
      <th>Sugar_Tot_(g)</th>
      <th>...</th>
      <th>Vit_A_RAE</th>
      <th>Vit_E_(mg)</th>
      <th>Vit_D_mcg</th>
      <th>Vit_D_IU</th>
      <th>Vit_K_(mcg)</th>
      <th>FA_Sat_(g)</th>
      <th>FA_Mono_(g)</th>
      <th>FA_Poly_(g)</th>
      <th>Cholestrl_(mg)</th>
      <th>water_(mg)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>8617</th>
      <td>93600</td>
      <td>TURTLE GREEN RAW</td>
      <td>78.5</td>
      <td>89</td>
      <td>19.8</td>
      <td>0.5</td>
      <td>1.2</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>...</td>
      <td>30.0</td>
      <td>0.5</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.1</td>
      <td>0.127</td>
      <td>0.088</td>
      <td>0.170</td>
      <td>50.0</td>
      <td>0.0785</td>
    </tr>
    <tr>
      <th>8616</th>
      <td>90560</td>
      <td>SNAIL RAW</td>
      <td>79.2</td>
      <td>90</td>
      <td>16.1</td>
      <td>1.4</td>
      <td>1.3</td>
      <td>2.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>...</td>
      <td>30.0</td>
      <td>5.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.1</td>
      <td>0.361</td>
      <td>0.259</td>
      <td>0.252</td>
      <td>50.0</td>
      <td>0.0792</td>
    </tr>
  </tbody>
</table>
<p>2 rows × 37 columns</p>
</div>


