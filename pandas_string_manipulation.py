import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("chicago.csv").dropna(how='all')

df["Employee Annual Salary"] = df["Employee Annual Salary"].str.replace("$", "")
df["Employee Annual Salary"] = df["Employee Annual Salary"].astype(float)

df["Name"] = df["Name"].str.title()

# print(df.nunique())

df["Department"] = df["Department"].astype("category")

for col in df.columns:
    if type(df[col][0]) == str:
        df[col] = df[col].str.title()

df["Last Name"] = df["Name"].str.split(",").str.get(0).str.strip()
df["First Name"] = df["Name"].str.split(",").str.get(1).str.strip()
df.drop("Name", axis=1, inplace=True)

# sobrenomes mais comuns
sobrenomes_comuns = df["Last Name"].value_counts().nlargest(10)
sobrenomes_dict = sobrenomes_comuns.to_dict()
lista_sobrenomes_comuns = []
for name in sobrenomes_dict.keys():
    lista_sobrenomes_comuns.append(name)

# nomes mais populares
nomes_comuns = df["First Name"].str.split().str.get(0).value_counts().nlargest(10)
lista_nomes_comuns = []
for name in nomes_comuns.index:
    lista_nomes_comuns.append(name)

# Maiores salários por departamento
grouped_departments = df.groupby("Department")
largest_salaries = grouped_departments["Employee Annual Salary"].mean().nlargest(10)

largest_salaries.plot(kind='bar', title='Average Salaries by Department', ylabel='Mean Salaries',
                      xlabel='Departments')
plt.show()

# Maiores departamentos
biggest_departments = grouped_departments.size().nlargest(10)

biggest_departments.plot(kind='bar', title='Size of the top 10 biggest departments', ylabel='Number of Employees',
                         xlabel='Departments', figsize=(10, 8))
plt.show()
