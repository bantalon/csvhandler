================================
csvhandler - Simple CSV filtering
================================

A simple wrapper around Python's CSV module to provide a command-line tool for
filtering columns from a CSV file.  This is useful as standard tools like awk
can't easily handle the quoting and escaping used in CSV files.  

Basically, it's a bit like ``cut`` but for CSVs.

Install
-------

From PyPi::

    pip install csvhandler

Use
---

Pluck fields 1, 3 and 5 from ``in.csv``::

    csvhandler -f 1,3,5 in.csv > out.csv

Pluck all fields apart from column 2 from STDIN::

    cat in.csv | csvhandler -f 2 -i > out.csv

Convert pipe-separated file to comma-separated (by default, output is 
comma-separated)::

    csvhandler -d"|" in.psv > out.csv 

Skip that pesky header row::

    cat in.csv | csvhandler --skip=1

As you can see, CSV data can be supplied through STDIN or by running ``csvhandler`` directly on a
file.

Help is in the usual place::

    $ csvhandler --help

    Usage: csvhandler [options] [inputfile]

    Source: https://github.com/codeinthehole/csvhandler/

    Options:
    -h, --help            show this help message and exit
    -f FIELDS, --fields=FIELDS
                            Specify which fields to pluck
    -s SKIP, --skip=SKIP  Number of rows to skip
    -d DELIMITER, --delimiter=DELIMITER
                            Delimiter of incoming CSV data
    -q QUOTECHAR, --quotechar=QUOTECHAR
                            Quotechar of incoming CSV data

    -i, --inverse         Invert the filter - ie drop the selected fields
    --out-delimiter=OUT_DELIMITER
                            Delimiter to use for output
    --out-quotechar=OUT_QUOTECHAR
                            Quote character to use for output

Report issues
-------------

Use the `Github issue tracker`_ or, better still...

.. _`Github issue tracker`: https://github.com/codeinthehole/csvhandler/issues

Contribute
----------

After cloning, install the testing requirements::

    make 

Run the tests with::

    nosetests

and, if it helps, use the fixture files to test your amendments::

    cat fixtures/au.csv | csvhandler -f 3,1,2 -s 1
    csvhandler fixutres/au.csv -f 1,2 -i

Have fun.
