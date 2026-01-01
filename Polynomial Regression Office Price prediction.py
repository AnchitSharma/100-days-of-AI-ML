import pandas as pd
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
x = input()
if x:
    x2 = x.split(" ")
    F, N = int(x2[0]), int(x2[1])
# print("F=", F, "N=", N)

df_dict = {}
for f in range(F):
    df_dict[f"feat_{f}"] = []

df_dict['target'] = []

# print("feature dict: ", df_dict)

for i in range(N):
    r1 = input()
    r1 = r1.split(" ")
    
    for f in range(F):
        df_dict[f"feat_{f}"].append(float(r1[f]))
    df_dict['target'].append(float(r1[-1]))
        
    
df = pd.DataFrame(df_dict)
# print("Table=", df.head())

X = df.iloc[:, :-1]
y = df.loc[:, 'target']

poly = PolynomialFeatures(degree=3, include_bias=False)
X_poly = poly.fit_transform(X)

# print(X, y)
lr = LinearRegression()
lr = lr.fit(X_poly, y)
# print(lr.coef_)
# print(lr.intercept_)





# test data rows
test_r = int(input())
# print(test_r)

df_dict = {}
for f in range(F):
    df_dict[f"feat_{f}"] = []

df_dict['target'] = []



for i in range(test_r):
    r1 = input()
    r1 = r1.split(" ")
    
    for f in range(F):
        df_dict[f"feat_{f}"].append(float(r1[f]))
    df_dict['target'].append(0.0)
    

df_test = pd.DataFrame(df_dict)
X_test_poly = poly.transform(df_test.iloc[:, :-1])
pred = lr.predict(X_test_poly)

for p in pred:
    print(round(p,2))

# # coef_[0]* f1 + coef_[1]*f2 + intercept

# def apply_coefs(r):
#     m = 0
#     for f in range(F):
#         m = m + lr.coef_[f]*r[f"feat_{f}"]
#     m = m + lr.intercept_
#     return m

# df_test["target"] = df_test.apply(lambda x : apply_coefs(x), axis=1)

# for x in df_test["target"].values:
#     print(round(x, 2))

        


