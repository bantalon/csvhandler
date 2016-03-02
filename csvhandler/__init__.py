import csv
import sys

# Avoid issue with fields larger than max size
csv.field_size_limit(sys.maxint)

VERSION = '0.3.2'


class Processor(object):

    def __init__(self, fields=None, invert=False, delimiter=',',
            quotechar='"', skip=0, grep_fields_map={}, substitutions_map={}):
        self.fields = fields
        self.invert = invert
        self.delimiter = delimiter
        self.quotechar = quotechar
        self.skip = skip
        self.validators = []
        self.grep_fields_map = grep_fields_map
        self.substitutions_map = substitutions_map

    def add_validator(self, f):
        self.validators.append(f)

    def skip_due_to_grep(self, row):
        for field_index, grep_expression in self.grep_fields_map.iteritems():
            if row[field_index] != grep_expression:
                return True
        return False

    def substitute(self, row):
        for field_index, field_substitutions_map in self.substitutions_map.iteritems():
            source_string = row[field_index]
            dest_string = field_substitutions_map.get(source_string)
            if dest_string:
                row[field_index] = dest_string

    def process(self, file_handle):
        reader = csv.reader(file_handle, delimiter=self.delimiter,
            quotechar=self.quotechar)
        for row in reader:
            output = None
            if reader.line_num <= self.skip:
                continue
            if self.skip_due_to_grep(row):
                continue
            self.substitute(row)
            if self.fields:
                if not self.invert:
                    output = [row[i] for i in self.fields if len(row) > i]
                else:
                    output = [e for i,e in enumerate(row) if i not in self.fields]
            else:
                output = row
            if not self.is_valid(output):
                continue
            if output:
                yield output

    def is_valid(self, row):
        for validator in self.validators:
            if not validator(row):
                return False
        return True
