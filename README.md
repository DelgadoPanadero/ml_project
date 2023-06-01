# ML Project Prototype

This project shows a dummy Machine Learning project as a prototype of project structure, code testing and CI pipeline for Machine Learning projects.

## Project Structure

```
ml_project
├── data
│   └── iris.csv
├── Dockerfile
├── model
│   └── ml_project.pkl
├── requirements.txt
├── src
│   ├── model
│   │   ├── custom_model.py
│   │   └── __init__.py
│   ├── predict.py
│   └── train.py
└── test
    ├── conftest.py
    ├── data
    │   ├── test_data.csv
    │   └── test_model.pkl
    ├── test_custom_model.py
    ├── test_predict.py
    └── test_train.py

```

## Code Design Pattern

The majority of the Machine Learning modules can be build following mainly two design patterns

#### Command Modules

This scripts are build to execute a machine learning process given a concrete configuration (e.g. [train.py](./src/train.py) [predict.py](./src/predict.py)).

#### Model Modules

This modules are build to define all the machine learning logic. Usually this king of modules follow a [Chain of Responsability](https://refactoring.guru/design-patterns/chain-of-responsibility/python/example) desing pattern with the following interface:

```
class ModelInterface():

    def __init__(**params: dict):
        pass
        
    def fit(X: pd.DataFrame, y: pd.DataFrame) -> None:
        pass

    def predict(X: pd.DataFrame) -> pd.DataFrame:
        pass

    def save(model_path: str) -> None:
        pass
    
    def load(model_path: str) -> None:
        pass
```

## Testing

The tests defined in the `test/` directory are thought 

* **Unit Testing**: This test are used for testing the behavior of each method from the `Model Modules` (p.e. [test_custom_model.py](test/test_custom_model.py))
* **Functional Testing**: This model are used for testing the behavior of the `Command Module` process (p.e. [test_train.py](test/test_train.py)
* **Data Testing**: Data components required to execute the test. Normally they are light dataset samples and model artifacts used just to test the code execution

## Continuous Integration

When we create a release (which means a commit tagged with the format "v*.*.*") a Github Action pipeline is executed with the following steps

* **Test**: Execute the code testing programatically

* **Build**: Build a docker image with the code

The result of the release is out project artifact, which is a Docker image with the model code (**NOTE**: we consider that the model artifact produced by the training is part of the deployment).


## Execute

Once the release have been done, we can execute the project release throught docker commands

```sh
$ docker pull ghcr.io/delgadopanadero/ml_project:sha256-500e64dc1f9aacb8fdcf922ddd6a1ece379658a132b25dc8d765a9de9778a6c8.sig
$ docker run \
  -v ${DATA_PATH}:/home/data \
  -v ${MODEL_PATH}:/home/model \
  ghcr.io/delgadopanadero/ml_project \
  python train.py
```

