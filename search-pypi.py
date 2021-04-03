#!/usr/bin/env python

from bs4 import BeautifulSoup as zoup
from requests import get
from sys import argv

# TODO
# pagination, only gets the first page of relevant results for now
# include last updated time/date

if len(argv) < 2:
    print("no input, please give a search term. (-l|--latest for first page of latest updated")
    exit()

if '-l' in argv or '--latest' in argv:
        if '-l' in argv[1] or '--latest' in argv[1]:
            search = f"{argv[2]}&o=-created"
        else:
            search = f"{argv[1]}&o=-created"
else:
    search = argv[1]

src = get(f'https://pypi.org/search/?q={search}').text
pypi = zoup(src, "html.parser")
lis = list(pypi.find_all('li'))
likids = [ lii for lii in lis if lii != '\n' ]

output = list()
for liss in likids:
    li = zoup(str(liss), 'html.parser')
    try:
        name = li.find('span', class_ = "package-snippet__name").get_text()
        version = li.find('span', class_ = "package-snippet__version").get_text()
        desc = li.find('p', class_ = "package-snippet__description").get_text()
        if desc == "": desc = "*** no description ***"
        output.append((name, version, desc))
    except:
        continue

l = max([ len(n[0]) for n in output ]) + 4

for n,v,d in sorted(output):
    print(f"{n : <{l}} {v : <10}\t{d}")
