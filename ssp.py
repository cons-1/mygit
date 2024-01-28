import xarray as xr
import pandas as pd
import os
import glob
from ssp_fuc import netcdf_to_csv, convert_all_netcdf_in_directory
from ssp_fuc2 import netcdf_to_csv2, convert_all_netcdf_in_directory2

# 打开NetCDF文件
pr_file = xr.open_dataset(
    "/Users/blue/PROGRAM/python/ZX_SSP/ssp126nc/pr/pr_day_ACCESS-CM2_ssp126_r1i1p1f1_gn_2015.nc"
)  # 请替换为你的文件名
tas_file = xr.open_dataset(
    "/Users/blue/PROGRAM/python/ZX_SSP/ssp126nc/tas/tas_day_ACCESS-CM2_ssp126_r1i1p1f1_gn_2015.nc"
)  # 请替换为你的文件名

# 查看文件的维度
print("\n---------------------------------- dims -----------------------------------\n")
print(pr_file.dims)
print(tas_file.dims)
print("\n-------------------------------- data_vars --------------------------------\n")
# 查看文件的变量
print(pr_file.data_vars)
print(tas_file.data_vars)
print("\n----------------------------------- pr  -----------------------------------\n")
# 查看pr变量
print(pr_file["pr"])
print("\n----------------------------------- tas -----------------------------------\n")
# 查看tas变量
print(tas_file["tas"])
print("\n----------------------------------- lon -----------------------------------\n")
# 查看经度(lon)变量
print(pr_file["lon"])
print("\n----------------------------------- lat -----------------------------------\n")
# 查看纬度(lat)变量
print(pr_file["lat"])


# 转换tas目录下的所有数据
tas_directory = "/Users/blue/PROGRAM/python/ZX_SSP/ssp126nc/tas"
convert_all_netcdf_in_directory(tas_directory, "tas", "output1/tas")

# 转换pr目录下的所有数据
pr_directory = "/Users/blue/PROGRAM/python/ZX_SSP/ssp126nc/pr"
convert_all_netcdf_in_directory(pr_directory, "pr", "output1/pr")

# 使用示例
pr_directory = "/Users/blue/PROGRAM/python/ZX_SSP/pr/"
lat_range = (24, 30.25)  # 纬度范围
lon_range = (113.25, 118.5)  # 经度范围
convert_all_netcdf_in_directory2(pr_directory, "pr", "output1/pr", lat_range, lon_range)
