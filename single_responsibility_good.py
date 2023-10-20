"""
The single responsibility principle: a class should have only one responsibility for change.
"""


# Good
class Report:
    def __init__(self, title: str, content: str):
        self.title = title
        self.content = content

    def edit_title(self, new_title: str):
        self.title = new_title


class ReportWriter:
    @staticmethod
    def write_report(report: Report, file_path: str):
        with open(file_path, 'w') as file:
            file.write(f"{report.title}/n{report.content}")
