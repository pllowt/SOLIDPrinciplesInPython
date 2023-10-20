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

    def insert(self, data: str, table: str) -> str:
        return "successfully inserted into to table"

    def read_from_table(self, table: str) -> str:
        """
        Return a table
        as a string
        """

        loc = self.table_map(table)
        if not loc:
            raise Exception("Table not found")

        return "I'm some data"

    def clear_table(self):
        return "successfully cleared the table"
