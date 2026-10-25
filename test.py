# import pandas as pd

# data = {
#     "Id":[101,102,103,104,105],
#     "Name":["Harsh","Tinkal","Reena","Vinod","Asha"],
#     "Age":[23,26,27,55,48],
#     "Department":["CS","Mathematics","Physics","Biology","Engineering"],
#     "GPA":[3.85,3.40,3.90,3.75,3.10]
# }
# df = pd.DataFrame(data)
# df.to_csv("student.csv",index=False)
# print("Create file successfully..!")

# import csv
# student_csv = [
#     ["ID","Name","Age","Department","GPA"],
#     [1,"Harsh",23,"CS",3.85],
#     [2,"Tinkal",26,"Mathematics",3.40],
#     [3,"Reena",27,"Physics",3.90],
#     [4,"Vinod",55,"CS",3.75],
#     [5,"Asha",48,"Biology",3.10],
# ]
# with open("student.csv",mode="w",newline="",encoding="utf-8") as file:
#     writer = csv.writer(file)
#     writer.writerows(student_csv)
# print("Create file successfully..!")



# import pandas as pd
# df = pd.read_csv("student.csv")
# df.to_csv("output.tsv",sep="/t",index=False)
# print("DONE")

# import numpy as np
# import pandas as pd
# df = pd.read_csv("student.csv")
# n = np.mean(df.GPA)
# print(n)

# import scipy as st
# import pandas as pd
# df = pd.read_csv("student.csv")
# r = df['GPA'].mode()
# print(r)
# import pandas as pd
# import numpy as np

# df = pd.read_csv("student.csv")

# # Option 1: Pandas .median() automatically ignores NaN values
# med = df['GPA'].median()
# print("Median (Pandas):", med)

# # Option 2: NumPy nanmedian
# med_np = np.nanmedian(df['GPA'])
# print("Median (NumPy):", med_np)

# import matplotlib.pyplot as plt
# import pandas as pd
# df = pd.read_csv("student.csv")
# plt.scatter(df.ID,df.GPA)
# plt.title("Scatter plot")
# plt.xlabel("ID")
# plt.ylabel("GPA")
# plt.show()

# import matplotlib.pyplot as plt
# import pandas as pd
# df = pd.read_csv("student.csv")
# plt.boxplot(df.GPA)
# plt.xlabel("Groups")
# plt.ylabel("GPA")
# plt.title("Box Plot")
# plt.show()

# import csv
# new_row = [106,"TOM",24,"Chemistry",""]
# with open("student.csv",mode="a",newline="") as file:
#     writer = csv.writer(file)
#     writer.writerow(new_row)
# print("new Row add")

# import pandas as pd
# data = pd.read_csv("student.csv")
# data1 = data.dropna()
# print(data1)
# data1.to_csv("student.csv",index=False)



# import pandas as pd
# data = pd.read_csv("student.csv")
# data['GPA'] = data['GPA'].fillna(data['GPA'].mean())
# print(data)
# data.to_csv("student.csv", index=False)

# import pandas as pd
# df = pd.read_csv("student.csv")
# print(df.tail(1))
# print(df.head(2))