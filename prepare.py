import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
import seaborn as sns
from acquire import get_titanic_data, get_iris_data

# ignore warnings
import warnings
warnings.filterwarnings("ignore")

from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import MinMaxScaler

def prep_titanic(df):
    encoder = LabelEncoder()

    # Embark town has lots of missing ppieces
    df.embard_town = df.embark_town.fillna("Other")


    df = df.drop(columns=['deck'])


df = get_titanic_data()
