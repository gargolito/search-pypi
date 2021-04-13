#!/usr/bin/env python3
from bs4 import BeautifulSoup as zoup
from requests import Session
from sys import argv, version_info
from tqdm import trange

if version_info < (3,6,5):
    print("this script requires Python 3.6.5 or higher")
    exit(1)

if len(argv) < 2:
    print(f"No input given, please give a search term:\n\t{argv[0]} [search term]")
    exit(1)

seek = argv[1]

def parse_html(src):
    """[summary]

    Args:
        src (str): html content

    Returns:
        list: list of class elements with unordered list html tag
    """
    pypi = zoup(src, "html.parser")
    lis = list(pypi.find_all('li'))
    likids = [ lii for lii in lis if lii != '\n' ]
    return likids

def extract_info(likids):
    """Use bs4 to fine search results that match css tags

    Args:
        likids (class): class object with parsed html list elements

    Returns:
        list: tuples with package names, version, and description
    """
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
    if output:
        return output
    else:
        return None

def print_output(output, search_term, total, pages):
    """ Parse list of tuples with pkg, version, description
    Args:
        output (list): list of tuples
        search_term (str): the pip package name that was searched
        total (int): total number of results found
        pages (int): total number of pages with results
    """
    dic = dict((x[0],x[1:]) for x in output)
    keys = sorted(dic, key = lambda s: s.casefold())
    out = [(k,dic[k][0],dic[k][1]) for k in keys]
    l = max([ len(n[0]) for n in output ]) + 4
    # for n,v,d in sorted(output):
    for n,v,d in out:
        print(f"{n : <{l}} {v : <10}\t{d}")
    print(f"\nFound {total} results for \"{search_term}\" in {pages} pages.")

def main(search, page = 1):
    """ kick off the good stuff

    Args:
        search (str): pip package to look for
        page (int, optional): starting page number. Defaults to 1.

    Returns:
        [type]: [description]
    """
    global s
    # first page does not use the page number parameter
    if page > 1:
        src = s.get(f'https://pypi.org/search/?q={search}&page={page}').text
    else:
        src = s.get(f'https://pypi.org/search/?q={search}').text
    parsed = parse_html(src)
    extracted = extract_info(parsed)
    if extracted:
        return extracted
    else:
        return None

if __name__ == '__main__':
    s = Session()
    out = set()
    print(f"\nSearching for \"{seek}\" in up to 10 pages at pypi.org")
    pages = -1
    for n in trange(1,11,1):
        pages += 1
        if n == 1:
            out |= set(main(seek))
        else:
            more = main(seek, n)
            if more:
                out |= set(more)
            else:
                break
    if pages == 9:
        pages = 10
    print(f"\nResults for {seek}:")
    print_output(list(out), seek, len(list(out)), pages)
