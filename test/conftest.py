import pytest
import pandas as pd


@pytest.fixture
def X():
    return pd.read_csv('test/data/test_data.csv').drop('Species',axis=1)


@pytest.fixture
def y():
    return pd.read_csv('test/data/test_data.csv')[['Species']]


@pytest.fixture
def train_args():

    class args():
        data_path='test/data/test_data.csv'
        max_iter=100
        model_path=f''

    return args


@pytest.fixture
def predict_args():

    class args():
        model_path='test/data/test_model.pkl'
        port=8080
    return args
