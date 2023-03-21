<h1>xpath with Scrapy</h1>

```html
html_doc = '''
<html>
    <head>
        <title>Title of the page</title>
    </head>
    <body>
        <h1>H1 tag</h1>
        <h2>H2 tag with <a href="#">link</a></h2>
        <p>First Paragraph</p>
        <p>Second Paragraph</p>
    </body>
</html>
'''
```

***

Enables to navigate through xml path
```python
from scrapy.selector import Selector
```

> %paste

```python
In [5]: sel = Selector(text=html_doc)

In [6]: sel.extract()
Out[6]: '<html>\n    <head>\n        <title>Title of the page</title>\n    </head>\n    <body>\n        <h1>H1 tag</h1>\n        <h2>H2 tag with <a href="#">link</a></h2>\n        <p>First Paragraph</p>\n        <p>Second Paragraph</p>\n    </body>\n</html>'

```
***
- Select Title

```python
In [7]: sel.xpath('/html/head/title')
Out[7]: [<Selector xpath='/html/head/title' data='<title>Title of the page</title>'>]

In [10]: sel.xpath('/html/head/title').extract()
Out[10]: ['<title>Title of the page</title>']

```

***

- Select all of titles

```python
In [11]: sel.xpath('//title').extract()
Out[11]: ['<title>Title of the page</title>']
```

***

- Select all text

```python

In [14]: sel.xpath('//text()').extract()
Out[14]: 
['\n    ',
 '\n        ',
 'Title of the page',
 '\n    ',
 '\n    ',
 '\n        ',
 'H1 tag',
 '\n        ',
 'H2 tag with ',
 'link',
 '\n        ',
 'First Paragraph',
 '\n        ',
 'Second Paragraph',
 '\n    ',
 '\n']
```

***

- Select Paragraphs

```python
In [15]: sel.xpath('/html/body/p')
Out[15]: 
[<Selector xpath='/html/body/p' data='<p>First Paragraph</p>'>,
 <Selector xpath='/html/body/p' data='<p>Second Paragraph</p>'>]

In [16]: sel.xpath('/html/body/p').extract()
Out[16]: ['<p>First Paragraph</p>', '<p>Second Paragraph</p>']
```

***

- Select all paragraphs

```python
In [17]: sel.xpath('//p')
Out[17]: 
[<Selector xpath='//p' data='<p>First Paragraph</p>'>,
 <Selector xpath='//p' data='<p>Second Paragraph</p>'>]
```

***

- Select paragraph by order

```python
In [18]: sel.xpath('//p[1]')
Out[18]: [<Selector xpath='//p[1]' data='<p>First Paragraph</p>'>]

In [19]: sel.xpath('//p[2]')
Out[19]: [<Selector xpath='//p[2]' data='<p>Second Paragraph</p>'>]

#list slice from Python
In [20]: sel.xpath('//p')[0]
Out[20]: <Selector xpath='//p' data='<p>First Paragraph</p>'>

#text
In [21]: sel.xpath('//p/text()')[0].extract()
Out[21]: 'First Paragraph'

#first data point
In [21]: sel.xpath('//p/text()').extract_first()
Out[21]: 'First Paragraph'
```

***

- Select h2 and link (href)

```python
In [22]: sel.xpath('//h2').extract()
Out[22]: ['<h2>H2 tag with <a href="#">link</a></h2>']

# text
In [23]: sel.xpath('//h2/a').extract()
Out[23]: ['<a href="#">link</a>']

#tag <a>

In [24]: sel.xpath('//h2/a/@href').extract()
Out[24]: ['#']

```

<h2>CSS</h2>

```python
In [25]: sel.css('h2')
Out[25]: [<Selector xpath='descendant-or-self::h2' data='<h2>H2 tag with <a href="#">link</a><...'>]
```


