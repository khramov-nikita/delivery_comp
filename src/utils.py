import pandas as pd


class ReadXLSX:

    def __init__(self, path):
        self.path = path
        self.df = self.get_df()

    def get_df(self):
        result = pd.read_excel(self.path)
        return result


class LoadXLSX:

    def __init__(self):
        pass

