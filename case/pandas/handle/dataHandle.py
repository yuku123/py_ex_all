import pandas as pd
import numpy as np

# 写入的文件路径配置
ns_category_file = '/Users/zifang/Downloads/文档/python_input/ns_category.csv'
ns_dict_file = '/Users/zifang/Downloads/文档/python_input/ns_dict.csv'
ns_dict_value_file = '/Users/zifang/Downloads/文档/python_input/ns_dict_value.csv'
ns_dict_value_category_file = '/Users/zifang/Downloads/文档/python_input/ns_dict_value_category.csv'

# 写出的文件路径
ns_dict_value_out_file = '/Users/zifang/Downloads/文档/python_output/ns_dict_value.csv'
ns_dict_out_file = '/Users/zifang/Downloads/文档/python_output/ns_dict.csv'

ns_category = pd.read_csv(ns_category_file, sep=',', dtype=str, delimiter=None, low_memory=False)
ns_dict = pd.read_csv(ns_dict_file, sep=',', dtype=str, delimiter=None, low_memory=False)
ns_dict_value = pd.read_csv(ns_dict_value_file, sep=',', delimiter=None, low_memory=False)
ns_dict_value_category = pd.read_csv(ns_dict_value_category_file, sep=',', delimiter=None, low_memory=False)

print(ns_category.head())
print(ns_dict.head())
print(ns_dict_value.head())
print(ns_dict_value_category.columns)
print(ns_dict_value_category.head())

# 处理字典值域表
ns_dict_value_temp = ns_dict_value[['id','category','value','define','explain']]
ns_dict_value_category_temp = ns_dict_value_category[['ns_code','ns_value_name']]
ns_dict_value_temp_joined = pd.merge(
    ns_dict_value_temp,
    ns_dict_value_category_temp,
    left_on='category',
    right_on='ns_value_name',
    how="left"
)
print(ns_dict_value_temp_joined.head(20))

ns_dict_value_temp_joined\
    .drop(['ns_value_name'],axis=1)\
    .to_csv(ns_dict_value_out_file,index=0)

# 处理字典
ns_category["join_key"] = ns_category["category_main"] + ns_category["category_sub"]
ns_dict["join_key"] = ns_dict['ns_code'].str[2:4] + ns_dict['ns_code'].str[5:7]

ns_dict_temp = pd.merge(
    ns_dict.drop(['ns_category_id'],axis=1),
    ns_category[['id','join_key']].rename(columns={'id':'ns_category_id'}),
    how="left",
    on='join_key'
)

ns_dict_temp.drop(['join_key'],axis=1).to_csv(ns_dict_out_file,index=0)

print(ns_dict_temp.head())


