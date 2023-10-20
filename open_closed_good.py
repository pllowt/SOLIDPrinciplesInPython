"""
Open closed principle:
    Software entities (classes, modules, functions, etc.) should be open to extension but close to modification
"""
from abc import ABC, abstractmethod


class Formatter(ABC):
    @abstractmethod
    def format(self, report):
        pass


# Good
class Report:
    def __init__(self, title: str, content: str):
        self.title = title
        self.content = content

    def edit_title(self, new_title: str):
        self.title = new_title

    def get_formatted_report(self, formatter: Formatter):
        return formatter.format(self)


class HTMLFormatter(Formatter):

    def format(self, report: Report):
        return f'<html><head><title>{report.title}</title></head><body>{report.content}</body></html>'


class PlainTextFormatter(Formatter):
    def format(self, report: Report):
        return f'{report.title}\n{report.content}'


class ReportWriter:
    @staticmethod
    def write_report(report: Report, file_path: str):
        with open(file_path, 'w') as file:
            file.write(f"{report.title}/n{report.content}")


if __name__ == '__main__':
    new_report = Report(
        'Reporty Mcreportface', "this is some content inside of a report, I'm reporty mcreportface"
    )
    html_formatter = HTMLFormatter()
    plain_text_formatter = PlainTextFormatter()
    print(new_report.get_formatted_report(html_formatter))
    print(new_report.get_formatted_report(plain_text_formatter))
