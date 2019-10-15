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
    scaler = MinMaxScaler()

    # Embark town has lots of missing ppieces
    df.embark_town.fillna("Other", inplace=True)

    # Embarked has some missing pieces
    df.embarked.fillna("Other", inplace=True)

    encoder.fit(df.embarked)
    df["encoded_embarked"] = encoder.transform(df.embarked)

    # Drop the deck column
    df.drop(columns=['deck'], inplace=True)

    # fill in missing ages
    mean_age = df.age.mean()
    df.age.fillna(mean_age, inplace=True)

    # Add a MinMax scaler for age and fare.
    scaler.fit(df[["age"]])
    df["scaled_age"] = scaler.transform(df[["age"]])

    scaler.fit(df[["fare"]])
    df["scaled_fare"] = scaler.transform(df[["fare"]])

    # I may need to encode sex, class, and embark_town?
    return df


def prep_iris(df):
    # drop species_id and #measurement_id
    df.drop(columns=['species_id', 'measurement_id'], inplace=True)

    # rename species_name to species
    df.rename(columns={"species_name": "species"}, inplace=True)

    # encode the species name using sklearn label encoder
    encoder = LabelEncoder()
    encoder.fit(df.species)

    df["species_encoded"] = encoder.transform(df.species)

    return df