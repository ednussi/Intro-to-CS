#!/usr/bin/env python3
'''
usage: hunzip.py [-h] [-o OUTFILE] [-s SUFFIX] [-S OUTSUFFIX] [-f] infile

Decompress files using the hzlib module.

positional arguments:
  infile

optional arguments:
  -h, --help            show this help message and exit
  -o OUTFILE, --outfile OUTFILE
                        Name of output file
  -s SUFFIX, --suffix SUFFIX
                        Default suffix to remove instead of .hz
  -S OUTSUFFIX, --outsuffix OUTSUFFIX
                        Default suffix to add if instead of .out
  -f, --force           Force decompression and overwrite output file if it
                        exists
'''
import hzlib

DEFAULT_IN_EXTENSION = '.hz'
DEFAULT_OUT_EXTENSION = '.out'

def main():
    import argparse
    parser = argparse.ArgumentParser(
        description='Decompress files using the hzlib module.')
    parser.add_argument("infile")
    parser.add_argument("-o", "--outfile", type=str, default=None, 
                        help='Name of output file')
    parser.add_argument("-s", "--suffix", type=str,
                        default=DEFAULT_IN_EXTENSION,
                        help=('Default suffix to remove instead of ' +
                              DEFAULT_IN_EXTENSION))
    parser.add_argument("-S", "--outsuffix", type=str,
                        default=DEFAULT_OUT_EXTENSION,
                        help=('Default suffix to add if instead of ' +
                              DEFAULT_OUT_EXTENSION))
    parser.add_argument("-f", "--force", action='store_true',
                        help=('Force decompression and overwrite output ' +
                              'file if it exists'))
    args = parser.parse_args()
 
    #Your code goes here and in the other functions you should write...

if __name__ == '__main__':
    main()
