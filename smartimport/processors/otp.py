import csv 
from dateutil.parser import parse as parse_date

from smartimport.processors import BaseParser

class OtpParser(BaseParser):
    def __init__(self):
        pass
    pass

    def _predict_tags(self, row):
        # Here comes the magic§
        return row

    def _read_csv(self,utf8_data, dialect=csv.excel, **kwargs):
        csv_reader = csv.reader(utf8_data, dialect=dialect, **kwargs)
        for row in csv_reader:
            yield {
                'date': parse_date(row[4]),
                'price': float(row[2]),
                'text': " ".join((row[8], row[9], row[12])).strip(),
                'tags': []
            }

    def preprocess(self, payload):
        dialect = csv.Sniffer().sniff(payload.read(1024))
        payload.seek(0)
        reader = self._read_csv(payload, dialect=dialect)
        return [self._predict_tags(row) for row in reader]
    pass


def dispatch():
    return OtpParser()
