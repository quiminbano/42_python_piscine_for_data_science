import pandas as pd
from pandas.errors import ParserError, EmptyDataError


def load(path: str) -> pd.DataFrame:
    try:
        if path is None or isinstance(path, str) is False:
            raise AssertionError("Handle later")
        if path.endswith(".csv") is False:
            raise AssertionError("Handle later")
        dataset = pd.read_csv(path)
        print(f"Loading dataset of dimensions {dataset.shape}")
        return dataset
    except (AssertionError, FileNotFoundError, PermissionError,
            ParserError, EmptyDataError) as e:
        print(e)
        return None
