"""
The single responsibility principle: a class should have only one responsibility for change.
"""


# Bad
class Report:
    def __init__(self, title: str, content: str):
        self.title = title
        self.content = content

    def write_report(self, file_path):
        with open(file_path, 'w') as file:
            file.write(f"{self.title}/n{self.content}")

    def edit_title(self, new_title: str):
        self.title = new_title
