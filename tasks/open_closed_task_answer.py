from abc import ABC, abstractmethod

import pandas as pd


class TablesReader(ABC):
    @abstractmethod
    def read(self, tables_adaptor, table: str):
        pass


class TablesAdaptor:
    def table_map(self, key):
        """
        This is a function to stop python
        running the lookup when this file is imported
        """
        table_map = {
            "FOO_TABLE": "I'm a foo table",
            "BAR_TABLE": "I'm a foo table",
        }
        return table_map[key]

    def clear_table(self):
        return "successfully cleared the table"


class DataFrameReader(TablesReader):
    def read(self, tables_adaptor: TablesAdaptor, table):
        """
                Return a table
                as a pandas dataframe
                """

        loc = tables_adaptor.table_map(table)
        if not loc:
            raise Exception("Table not found")

        return pd.DataFrame()


class PlainTextReader(TablesReader):
    def read(self, tables_adaptor: TablesAdaptor, table):
        """
               Return a table
               as a string
               """

        loc = tables_adaptor.table_map(table)
        if not loc:
            raise Exception("Table not found")
