#sampling distribution
import random
import csv
import pandas as pd
import plotly.figure_factory as ff
import statistics

df=pd.read_csv("medium_data.csv")
data=df["responses"].tolist()
fig=ff.create_distplot([data], ["Responses"], show_hist=False)
fig.show()
p_mean=statistics.mean(data)
print(p_mean)

#finding random samples from the entire population(conducting check of sampling distribution)
def random_setofmeans(counter):
    samples=[]
    for i in range(0,counter):
        random_index=random.randint(0, len(data))
        value=data[random_index]
        samples.append(value)
        s_mean=statistics.mean(samples)
    return s_mean
def showfig(mean_list):
    df=mean_list
    fig=ff.create_distplot([df], ["sampling means"], show_hist=False)
    fig.show()

def setup():
    mean_list=[]
    for i in range(0, 100):
        setofmeans=random_setofmeans(10)
        mean_list.append(setofmeans)
    showfig(mean_list)
    m_mean=statistics.mean(mean_list)
    print(m_mean)
setup()
