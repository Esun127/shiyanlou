#!/home/shiyanlou/anaconda3/bin/python

import pandas as pd
import numpy as np
from matplotlib import pyplot as plt


df = pd.read_json(path_or_buf='user_study.json')
data = df.groupby('user_id')[['minutes']].sum()

fig = plt.figure()
ax = fig.add_subplot(1,1,1)

ax.set_title('StudyData')
ax.set_xlabel('User ID')
ax.set_ylabel('Study Time')
ax.plot(data.index.values,data.values)
plt.show()
