import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("online_retail.csv")
print(df.head())

print(df.shape)

df.info()

print(df.isnull().sum())

print(df.duplicated().sum())

df = df.dropna(subset=["CustomerID"])

df = df[df["Quantity"] > 0]

df = df[df["UnitPrice"] > 0]

df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"])

df["CustomerID"] = df["CustomerID"].astype(int)

df["Revenue"] = df["Quantity"] * df["UnitPrice"]

monthly_sales = df.resample("M", on="InvoiceDate")["Revenue"].sum()

monthly_sales.plot(
    figsize=(10,5),
    title="Monthly Revenue Trend"
)

plt.show()

top_products = (
    df.groupby("Description")["Revenue"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

print(top_products)

top_customers = (
    df.groupby("CustomerID")["Revenue"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)
print(top_customers)

country_sales = (
    df.groupby("Country")["Revenue"]
    .sum()
    .sort_values(ascending=False)
)

print(country_sales.head(10))