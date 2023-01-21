
# TODO
* sort by newest
* option to specify number of searched pages instead of the statically  set 10 page limit
* * will need to also have a hard set limit, say no more than 100
* include last updated time/date
* modularize/create distributable package with command line so that it is pip installable
* figure if we can replace the builtin "pip search" command or some way of hooking into it in a pythonic way.
* * it can be done with a shell function in the environment that replaces that command and nothing else, this can be added to bashrc. For example, in bash:
```
function pip () {
  if [[ "$2" == "search" ]]; then
    shift
    shift
    search-pipy $@
  fi
}
```
