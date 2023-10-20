class TableMapping:
    def __init__(self):
        self.mapping_dict = {}


class DataInserter:
    def __init__(self, table_mapping: TableMapping):
        self.table_mapping = table_mapping

    def insert_into_table(self, data: str, table: str):
        loc = self.table_mapping.mapping_dict[table]
        if not loc:
            raise Exception("Table not found")

        return "successfully inserted into to table"


class DataReader:
    def __init__(self, table_mapping: TableMapping):
        self.table_mapping = table_mapping

    def read_from_table(self, table: str):
        loc = self.table_mapping.mapping_dict[table]
        if not loc:
            raise Exception("Table not found")

        return "I'm some data"


class TableClearer:
    def __init__(self, table_mapping: TableMapping):
        self.table_mapping = table_mapping

    def clear_table(self):
        return "successfully cleared the table"
