#!/home/shiyanlou/anaconda3/bin/python 
import json
import pandas as pd

def analysis(file, user_id):
    df = pd.read_json(file)
    #print(df.columns)
    times = 0
    minutes = 0
    
#    print(df.columns)
#    print(df.user_id.dtype)
    df_r = df.loc[:,['user_id','created_at','minutes']][df['user_id'] == user_id]
    times, minutes = df_r.created_at.size, df_r.minutes.sum()
#[df['user_id'] == user_id]]
#    print(df_r)
    return times, minutes


if __name__ == '__main__':
    t, m = analysis('user_study.json', 199071)
    print(t, m)
