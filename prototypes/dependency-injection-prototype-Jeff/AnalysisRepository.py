from abc import ABC, abstractmethod
import pandas as pd

# for this project, repositories associated
# with analysis services should return pandas
# dataframes. Otherwise, they should return a
# model associated with the service they are
# called by.
# For example, if we're using a repository
# within UserService, all methods should
# work with User models.


class Repository:
    @abstractmethod
    def __create__(self, datasource):
        self.datasource = datasource

    @abstractmethod
    def get_all():
        pass

    # @abstractmethod
    # def get_one():
    #     pass

    # @abstractmethod
    # def insert():
    #     pass

    # @abstractmethod
    # def update():
    #     pass

    # @abstractmethod
    # def delete():
    #     pass


class CSVRepository(Repository):
    def __init__(self, datasource):
        self.__create__(datasource)

    def __create__(self, datasource):
        self.csv_source = datasource
        try:
            self.dataframe = pd.read_csv(datasource)
        except Exception:
            print(f'Invalid datasource: {self.datasource}')

    def get_all(self):
        return self.dataframe
