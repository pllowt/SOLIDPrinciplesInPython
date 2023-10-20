"""
Open closed principle:
    Software entities (classes, modules, functions, etc.) should be open to extension but close to modification
"""


# Bad
class Report:
    def __init__(self, title: str, content: str):
        self.title = title
        self.content = content

    def edit_title(self, new_title: str):
        self.title = new_title

    def format_as_html(self):
        return f'<html><head><title>{self.title}</title></head><body>{self.content}</body></html>'

    def format_as_plain_text(self):
        return f'{self.title}\n{self.content}'


class ReportWriter:
    @staticmethod
    def write_report(report: Report, file_path: str):
        with open(file_path, 'w') as file:
            file.write(f"{report.title}/n{report.content}")


if __name__ == '__main__':
    new_report = Report(
        'Reporty Mcreportface', "this is some content inside of a report, I'm reporty mcreportface"
    )
    print(new_report.format_as_html())
    print(new_report.format_as_plain_text())
