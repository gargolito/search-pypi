# search-pypi
search pypi.org because pip search has been broken for some time.

```
$ pip search some-package
ERROR: XMLRPC request failed [code: -32500]
RuntimeError: PyPI's XMLRPC API is currently disabled due to unmanageable load and will be deprecated in the near future. See https://status.python.org/ for more information.
```
* search up to the first ten pages of a search result

# Minimum Requirements
* Python >= 3.6.5
* Modules
* * see requirements.txt

# Operating System
* Tested in MacOS and Ubuntu

# Installation
1. git clone https://github.com/gargolito/search-pypi
2. cd search-pypi
3. pip install -r requirements.txt
4. make sure the script is executable by you: chmod u+x search-pypi.py

Once requirements are met, usage:
```
./search-pypi.py yoursearchword
```

## Optional Installation
* if you don't already have a scripts directory in your user environment (tsk, tsk) and you want to run the script from anywhere:
```
mkdir ~/bin
cp search-pypi.py ~/bin
```
* add ~/bin to your shell environment (i'm a bash user so...)
```
open your ~/.bashrc in your favorite editor and add your ~/bin directory to PATH
export PATH=~/bin:${PATH}
```

## [TODO](TODO.md)
