# search-pypi
search pypi.org because pip search has been broken for some time.

```
$ pip search some-package
ERROR: XMLRPC request failed [code: -32500]
RuntimeError: PyPI's XMLRPC API is currently disabled due to unmanageable load and will be deprecated in the near future. See https://status.python.org/ for more information.
```

* limited to first page of relevant results
* can pass -l or --latest to get first page of last updated packages that match your search

## TODO
* pagination fetch N pages including the first page, or prompt to get the next page.
* include last updated time/date
