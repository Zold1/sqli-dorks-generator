# SQLI Dorks Generator

this is simple script for generate dorks list for sql injection

## How to use

* Write the names of the sites that have the same category in **sites.txt**
  * for example shopping will be `Amazon`, `Walmart`, `Alibaba`... etc

* Write the keywords for these sites in **keywords.txt**
  * for example `shop electronics`, `cash on delivery`... etc

* Write the page types in **page_types.txt**
  * for example `php`, `cfg`, `aspx`... etc

* Write the page parameters in **page_parameters.txt**
  * for example `id`, `item_id`, `order_id`... etc

* Write the dork search functions in **search_functions.txt**
  * for example `inurl`, `intext`... etc

* Finally, write the patterns of dorks in **patterns.txt**, for example:
  * `{site} {keyword} .{page_type}?{page_parameter}=`
  * `{site} -{keyword} - / {page_type}?{page_parameter}= + {search_function}:`

After finished run the script by `python dorks.py`

results in **dorks.txt** will be like this:

``` plain
Alibaba shop electronics .php?item_id=
Amazon shop electronics .php?order_id=
Alibaba -cash on delivery - / aspx?id= + inurl:
Amazon -shop electronics - / cfg?item_id= + intext:
Amazon cash on delivery .php?order_id=
Amazon -shop electronics - / aspx?order_id= + inurl:
Walmart shop electronics .cfg?order_id=
Walmart -cash on delivery - / aspx?order_id= + intext:
Walmart cash on delivery .php?item_id=
Alibaba cash on delivery .cfg?item_id=
Alibaba shop electronics .php?id=
Walmart -cash on delivery - / cfg?item_id= + intext:
Alibaba shop electronics .cfg?order_id=
Amazon cash on delivery .cfg?id=
Amazon -shop electronics - / cfg?order_id= + intext:
Amazon shop electronics .cfg?item_id=
Walmart shop electronics .aspx?item_id=
Walmart -shop electronics - / php?id= + inurl:
Alibaba shop electronics .cfg?item_id=
Alibaba cash on delivery .aspx?item_id=
```
