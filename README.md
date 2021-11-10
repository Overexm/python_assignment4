# python_assignment4

## Title
This assignment is about parsing the newses from coinmarket site
```html
Done by: Orynbassar Merey, Kiyubayeva Kamila
Group:SE-2010
```

### Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Examples](#examples)
- [License](#lisense)

---

## Installation

* ### Create a virtual environment:
```python $ virtualenv env```
* ### Activate a virtual environment:
For Windows:
```python env\Scripts\activate```

For Mac OS,Linux:
```python source env/bin/activate```

* ### Flask
```python $ pip install flask```

* ### SQLAlchemy
```python $ pip install SQLAlchemy ```
* ### BeautifulSoup
```python $ pip install beautifulsoup4```
* ### pyjwt
```python $ pip install pyjwt ```
* ### PostgreSQL Database [Download](https://www.enterprisedb.com/downloads/postgres-postgresql-downloads)



[Back To The Top](#python_assignment4)

## Usage

```python
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from bs4 import BeautifulSoup, re
from selenium import webdriver
import pwjt
import requests
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service

```
[Back To The Top](#python_assignment4)
## Examples
```html
There when you will type all info about coin will be appeared

```
[Back To The Top](#python_assignment4)

## License

MIT License

Copyright (c) 2021 Overexm
Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

[Back To The Top](#python_assignment4)

