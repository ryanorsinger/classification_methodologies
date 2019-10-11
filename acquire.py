import pandas as pd

def get_url(database_name):
    from env import user, password, host
    return f'mysql+pymysql://{user}:{password}@{host}/{database_name}'


def get_titanic_data():
    return pd.read_sql('SELECT * FROM passengers', get_url('titanic_db'))