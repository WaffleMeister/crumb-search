from src.trigramIndexer.parser.file_parsers.word_doc_file_parser import WordDocFileParser
from src.trigramIndexer.parser.file_parsers.utf8_file_parser import UTF8FileParser

class FileParserFactory:

    def __init__(self):
        self.file_map = {
            '.docx': WordDocFileParser()
        }

    def get_parser_for_filetype(self, file_type):
        if file_type in self.file_map:
            return self.file_map[file_type]
        else:
            return UTF8FileParser()