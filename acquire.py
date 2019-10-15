import pandas as pd

def get_url(database_name):
    from env import user, password, host
    return f'mysql+pymysql://{user}:{password}@{host}/{database_name}'

def get_titanic_data():
    return pd.read_sql('SELECT * FROM passengers', get_url('titanic_db'))

def get_iris_data():
    query = "SELECT * FROM measurements join species on species.species_id = measurements.species_id"
    return pd.read_sql(query, get_url('iris_db'))    

