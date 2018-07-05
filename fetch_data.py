#!/usr/bin/env python
import argparse


from data.datasources import giphy


def main(datasource, raw, file_dest):
    if not file_dest:
        if datasource == 'giphy':
            items = giphy.GiphyItems()
        else:
            pass
        items.print_rows()
    else:
        print('Saving to CSV is not implemented.')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Fetch data from datasources.')
    parser.add_argument("datasource",
                        help="Choose a datasource",
                        action="store",
                        choices=('giphy',))
    parser.add_argument("--raw",
                        help="Display raw data instead of summary rows",
                        action="store_true",
                        default=False,)
    parser.add_argument("--save",
                        help="Save data to file as a CSV",
                        action="store",
                        default=None,)
    args = parser.parse_args()
    main(args.datasource, args.raw, args.save)
