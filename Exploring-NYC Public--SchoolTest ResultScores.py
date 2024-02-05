import pandas as pd
import numpy as np
schools = pd.read_csv("schools.csv")
schools.head()
schools=schools.fillna(0)
schools.head()
max_grade=800
best_math_schools=schools[schools['average_math']>=0.8*max_grade]
best_math_schools=best_math_schools[["school_name","average_math"]].sort_values(by="average_math",ascending=False).round(2)
print(best_math_schools)
schools["total_SAT"]=schools[["average_math","average_reading","average_writing"]].sum(axis=1)
schools.head()
top_10_schools=schools[['school_name','total_SAT']].sort_values(by='total_SAT',ascending=False).round(2).head(10)
print(top_10_schools)
#largest_std_dev=schools[['borough','school_name','total_SAT']].pivot_table(values='total_SAT',index='borough',aggfunc=[np.mean,np.std])
borough=schools[['borough','school_name','total_SAT']]
borough=borough.groupby("borough")['total_SAT'].agg(["count","mean","std"]).round(2)
borough.columns=["num_schools","average_SAT","std_SAT"]
print(borough)
largest_std_dev=borough[borough["std_SAT"] == borough["std_SAT"].max()]
print(largest_std_dev)