```python
import pandas as pd
from sklearn.preprocessing import StandardScaler, MinMaxScaler

class DataPreprocessor:
    def __init__(self):
        self.scaler = StandardScaler()

    def clean_data(self, data):
        # Remove duplicates
        data = data.drop_duplicates()

        # Remove null values
        data = data.dropna()

        return data

    def normalize_data(self, data):
        # Normalize data with StandardScaler
        data = self.scaler.fit_transform(data)

        return data

    def preprocess_data(self, data):
        # Clean the data
        data = self.clean_data(data)

        # Normalize the data
        data = self.normalize_data(data)

        return data

def preprocess_data(data):
    preprocessor = DataPreprocessor()
    preprocessed_data = preprocessor.preprocess_data(data)

    return preprocessed_data
```