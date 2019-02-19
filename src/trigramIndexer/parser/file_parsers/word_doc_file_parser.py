from docx import Document

class WordDocFileParser(object):
    
    # """
    #     Read in the file, and break it up into trigrams.
    #     return the list of trigrams.
    # """
    def parse(self, file_name):
        trigrams = []

        document = Document(file_name)

        for paragraph in document.paragraphs:
            for i in range(len(paragraph.text) - 2):
                trigrams.append(paragraph.text[i : i + 3].lower())

        return trigrams