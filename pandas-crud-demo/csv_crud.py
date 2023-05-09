import pandas
from cfg import *

class CsvCrud():

    def __init__(self, fpath):

        self.row_id = 0
        # self.df: list = self.load(fpath)
        self.df= self.load(fpath)

        self.count = len(self.df)

    def create(self, row):

        match (type(row)):
            case dict():
                new_row_obj = pandas.DataFrame(row)
                self.df = pandas.concat(
                    [new_row_obj, self.df.loc[:]]).reset_index(drop=True)
            case (_):
                new_row_list = row
                self.df.loc[len(self.df)] = new_row_list

    def read(self, where=False):

        def read_where(key, value):
            return self.df[self.df[key].isin([value])]
        if where:
            # This is kinda long winded
            return read_where(next(iter(where)), next(iter(where.items()))[1])
        else:
            return self.df

    def get_id(self, row):
        self.row_index = row.index.tolist()

    def update(self, id, data):
        updated_row_obj = pandas.DataFrame(data)
        self.df.iloc[[id]] = updated_row_obj

    def delete(self, id):
        self.df.drop(id, axis=0, inplace=True)

    def load(self, fpath):

        print(f"Loading data")
        self.fpath = fpath
        # self.df = pandas.DataFrame(data=pandas.read_csv(fpath))
        # return list()
        return pandas.DataFrame(data=pandas.read_csv(fpath))

    def save(self,custom_name = False):
        self.df.to_csv(self.fpath, mode='w',index=False) #  index=False

