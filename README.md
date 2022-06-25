# SQLI Dorks Generator

this is simple script for generate dorks list for sql injection

## How to use

* Write the names of the sites that have the same category in **sites.txt**
  * for example shopping will be `Amazon`, `Walmart`, `Ali Baba`... etc

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
