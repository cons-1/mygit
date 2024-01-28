# 函数：将NetCDF数据转换为CSV
def netcdf_to_csv(datafile, variable, output_dir, convert_units):
    ds = xr.open_dataset(datafile)
    var_data = ds[variable]

    for time in var_data.time:
        # 提取特定时间点的所有数据
        df = var_data.sel(time=time).to_dataframe().reset_index()
        df = df[["lon", "lat", variable]]  # 选择需要的列

        # 单位转换和小数位处理
        if convert_units:
            if variable == "pr":
                df[variable] = df[variable] * 86400 / 10  # 转换为 cm/day
            elif variable == "tas":
                df[variable] = df[variable] - 273.15  # 转换为摄氏度
                df[variable] = df[variable].round(2)  # 对tas保留两位小数

        df.columns = ["X", "Y", "Value"]  # 重命名列

        # 格式化时间并保存为CSV
        date_str = pd.to_datetime(str(time.values)).strftime("%Y%m%d")
        csv_filename = f"{output_dir}/{variable}_{date_str}.csv"
        df.to_csv(csv_filename, index=False)
        print(f"Saved {csv_filename}")

        # 格式化时间并保存为CSV
        date_str = pd.to_datetime(str(time.values)).strftime("%Y%m%d")
        csv_filename = f"{output_dir}/{variable}_{date_str}.csv"
        df.to_csv(csv_filename, index=False)
        print(f"Saved {csv_filename}")


# 函数：转换指定目录下的所有NetCDF文件
def convert_all_netcdf_in_directory(directory, variable, output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for filepath in glob.glob(os.path.join(directory, f"{variable}_*.nc")):
        print(f"Processing {filepath}")
        netcdf_to_csv(filepath, variable, output_dir, convert_units=True)
