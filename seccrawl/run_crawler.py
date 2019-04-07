import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-p', help="Run the spiders in parallel", action="store_true")
args = parser.parse_args()

command = 'scrapy list|xargs -n 1 ' + ('-P 0 ' if args.p else '') + 'scrapy crawl'
os.system(command)