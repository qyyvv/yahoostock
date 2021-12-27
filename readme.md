![Version](https://img.shields.io/pypi/v/yahoostock?color=g)
![Package Size](https://img.shields.io/github/repo-size/rohan0x/yahoostock)
![Last Commit](https://img.shields.io/github/last-commit/rohan0x/yahoostock)
![Release Date](https://img.shields.io/github/release-date-pre/rohan0x/yahoostock)
![License](https://img.shields.io/pypi/l/yahoostock)

# yahoostock
 A package designed to scrape data from Yahoo Finance.

## Installation
The most simple installation method is through PIP.
```
pip install yahoostock
```
The PyPI page can be found [here](https://pypi.org/project/yahoostock/).

## Usage
Use the following code to see a list of useful methods.
```py
from yahoostock import yahoo
print(dir(yahoo))
```
Note that each method accepts a stock ticker as a single parameter and returns a float with the specified statistic.

Here's an example:
```py
from yahoostock.yahoo import *

stock_name = "GOOGL"

function_list = [
    get_price,
    get_open,
    get_previous_close,
    get_change,
    get_percent_change
]

for function in function_list:
    # prints price ($), opening price ($), last closing price ($),
    # change in price ($), and relative change (%)
    print(function(stock_name))
```

For information about a specific method's purpose refer to the respective method's docstrings.

For example:
```py
from yahoostock.yahoo import get_price

help(get_price)
```
