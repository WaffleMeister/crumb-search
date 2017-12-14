# crumb-search

CrumbSearch is a python implementation of <a href="https://swtch.com/~rsc/regexp/regexp4.html">Russ Cox's</a> Google Code Search project. It allows a user to index a directory of UTF-8 files, and search using a limited regular expression set against that directory.

## Getting Started

### Prerequisites

Python 3 is recommended. This project may have some incompatiabilities with Python 2. You can get Python <a href="https://www.python.org/downloads/">here</a>.

### Installing

This project isn't hosted in pip, so just git clone the repository.

### Usage

To index a directory:
```
python cindex.py -d DIRECTORY
```

Index a directory, but only index files of the given type:
```
python3 cindex.py -i go,json,blah -d DIRECTORY
```

Search against the created index:
```
python csearch.py -s SEARCH_TERM
```

Case-Insensitive search against a created index:
```
python csearch.py -i -s SEARCH_TERM
```

Brute-Force search. This will instead search through all files in the index for the search term, rather than files which match the search query's ngrams:

```
python3 csearch.py -b -s SEARCH_TERM
```

Additional options for each command (cindex, csearch) are available by passing in the "-h" argument. You must first run cindex to index a directory before running csearch. Once an index is created, you can run searches for however long you wish against that index.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Built With

Python

## Todo:

Integrate with Elastic Search

Prettify some error handling

Handle more regular expression characters. Currently, only '+' and '*' special characters are supported.

## Acknowledgments

* Much thanks to https://twitter.com/_rsc?lang=en