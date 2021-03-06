#!/usr/bin/env python
import argparse


from data.datasources import giphy
from data.datasources import hacker_news 

def main(datasource, raw, file_dest):
    if not file_dest:
        if datasource == 'giphy':
            items = giphy.GiphyItems()
        elif datasource == 'hacker_news':
            items = hacker_news.HackerNewsItems()
        else:
            pass
        if raw:
            print 'raw'
            items.print_rows(raw)
        else:
            items.print_rows()
    else:
        items = hacker_news.HackerNewsItems()
        items.save_csv(file_dest)
        print('Saving to CSV is not implemented.')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Fetch data from datasources.')
    parser.add_argument("datasource",
                        help="Choose a datasource",
                        action="store",
                        choices=('giphy','hacker_news'))
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
