# search-pypi
search pypi.org because pip search has been broken for some time.

```
$ pip search some-package
ERROR: XMLRPC request failed [code: -32500]
RuntimeError: PyPI's XMLRPC API is currently disabled due to unmanageable load and will be deprecated in the near future. See https://status.python.org/ for more information.
```
* search up to the first ten pages of a search result

## TODO
* include last updated time/date
* sort by newest
* option to limit number of searched pages

