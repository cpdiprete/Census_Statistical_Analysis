import pandas as pd
import numpy as np
import matplotlib as plt
import csv
import sklearn

df = pd.read_csv("data/ACSST1Y2010.S0101.csv")
df["label"] = df["Label (Grouping)"].str.strip()
df.to_csv("age_estimates_only.csv", index=False)
# print(df.head)

dude = df.to_numpy()
print(dude)
# np.savetxt('output.csv', dude, delimiter=',')

