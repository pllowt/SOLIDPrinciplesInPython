"""
The single responsibility principle: a class should have only one responsibility for change.
"""


# Bad
class Report:
    def __init__(self, title: str, content: str):
        self.title = title
        self.content = content

    def edit_title(self, new_title: str):
        self.title = new_title


if __name__ == '__main__':
    new_report = Report(
        'Reporty Mcreportface', "this is some content inside of a report, I'm reporty mcreportface"
    )
