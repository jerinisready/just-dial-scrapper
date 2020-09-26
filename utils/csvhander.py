

class CsvHandler(object):

    def __init__(self, filename=None, encoding='UTF-8', filename_suffix='', filename_extension='.csv'):
        base_filename: str = filename or './data/output'
        self.filename = f"{base_filename}_{filename_suffix}{filename_extension}"
        self.encoding: str = encoding
        headers = '"Name", "Summery", "Address", "Contact", "JDVerified", Link\n'
        self.write_row(headers, mode='w')   # overwrite as new file.

    def write_row(self, line, mode='a'):
        with open(self.filename, mode, encoding=self.encoding) as f:
            f.write(line)

    @staticmethod
    def clean(val):
        return '"{}"'.format(val)


clean = CsvHandler.clean
