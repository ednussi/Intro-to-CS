#!/usr/bin/env python3
'''
usage: hzip.py [-h] [-o OUTFILE] [-s SUFFIX] [-f] [-l LEVEL] [-a] infile

Compress files using the hzlib module.

positional arguments:
  infile

optional arguments:
  -h, --help            show this help message and exit
  -o OUTFILE, --outfile OUTFILE
                        Name of output file
  -s SUFFIX, --suffix SUFFIX
                        Suffix to use instead of .hz
  -f, --force           Force compression and overwrite output file if it
                        exists
  -l LEVEL, --level LEVEL
                        Maximum levels of compression
  -a, --alwayscompress  Compress to max level even if it would make output
                        larger

Format of saved file is the following:
The string of bytes MAGIC from hzlib, followed by one byte containing the
compression level of the data, followed by the data.

Compression level 0 is the raw input. The data used in compression level
n+1 is the result of compressing the result provided by compression
level n. Note that each level includes its codebook in its data, but does
not include the magic number.
'''
import hzlib

DEFAULT_EXTENSION = '.hz'
MAX_COMPRESSION_LEVEL = 255
MIN_COMPRESSION_LEVEL = 0

def main():
    import argparse
    parser = argparse.ArgumentParser(
        description='Compress files using the hzlib module.')
    parser.add_argument("infile")
    parser.add_argument("-o", "--outfile", type=str, default=None, 
                        help='Name of output file')
    parser.add_argument("-s", "--suffix", type=str, default=DEFAULT_EXTENSION,
                        help=('Suffix to use instead of ' +
                              DEFAULT_EXTENSION))
    parser.add_argument("-f", "--force", action='store_true',
                        help=('Force compression and overwrite output ' +
                              'file if it exists'))
    parser.add_argument("-l", "--level", type=int,
                        default=MAX_COMPRESSION_LEVEL,
                        help='Maximum levels of compression')
    parser.add_argument("-a", "--alwayscompress", action='store_true',
                        help=('Compress to max level even if it would ' +
                              'make output larger'))
    args = parser.parse_args()

    #Your code goes here and in the other functions you should write...

if __name__ == '__main__':
    main()
