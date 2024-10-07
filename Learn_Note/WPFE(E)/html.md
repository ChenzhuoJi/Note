## ELENMENTS

Now we show a HTML code below:

```html
<!DOCTYPE html>
<html>
    <body>
        <h1>This is the Main Heading</h1>
        <p>This text might be an introduction to the rest of this page.<p>
        <h2>This is a Sub-Heading.</h2>
        <p>This text might be the article of Sub-Heading.</p>
    </body>
</html>
```

The HTML is made up of the characters that klive inside anglesd brackets "<>" -- these are called HTML elements.Elements are usually made up of two tags: an opening tag "`<html>`"and a closing tag"`</html>`"(The closing tag has an extra forward slash in it."/")

## ATTRIBUTES

Attribute tells us the additional information about the contents of the elements. They are madup of two parts: a aname and a value

```html
<p lang="en-us">Paragrah in English</p>
```

The value of the ``lang`` attribute is an abbreviated way of specifying which language is used inside the element that all browsers understand.

## Body, Head and Title

| `<body>`               | `<head>`                                                | `<title>`                             |
| ------------------------ | --------------------------------------------------------- | --------------------------------------- |
| the part the web showing | the heading in the webpage ``<h1>,<h2>``,...can be chosen | the content at the top of your browsers |

## Text

* **Structual markup:** the elements taht you can use to decribe both headings and paragraph
* **Semantic markup:** whci provides extra information; such as where emphasis is place in a sentence,that something ypu have written is a quotation(and who said it.),the meaning of aconyms,and so on.
  | Name                     |                                                                   Meaning and Use                                                                   |
  | ------------------------ | :-------------------------------------------------------------------------------------------------------------------------------------------------: |
  | ``<h1>,<h2>,...``        |                                                                        heads                                                                        |
  | ``<p>``                  |         pagragraph. By defalut, the browsers will show each paragraph on a new line wit some space between it and any subsequent paragraphs         |
  | ``<b>,<i>``              |                                                                   bold and italic                                                                   |
  | ``<sup>,<sub>``          |                                                   superscript and subscript ``E=MC<sup>2</sup>``                                                   |
  | ``<br />``               |                                                     line break in the middle of the paragraph.                                                     |
  | ``<hr />``               |                                                          horizontal rule between sections.                                                          |
  | ``<blockquote>,<q>``     |                                                                        quote                                                                        |
  | ``<abbr>``,``<acronym>`` | abbreviations and acronym ``<abbr title="Professor">Prof</abbr>`` ``<acronym title="National Aeronautics and Space Administration">NASA</acronym>`` |
  | ``<address>``            |                                                                                                                                                    |
  | `<ins>`,`<del>`      |                                                                                                                                                    |

## List

We show a HTML code :

```html
<ol>
    <li>1</li>
    <li>2</li>
    <li>3</li>
    <li>4</li>
    <li>5</li>
</ol>
<ul>
    <li>*</li>
    <li>*</li>
</ul>
```

## Link

Code example:

```html
<html>
<head>
 <title>Links</title>
</head>
<body>
 <h1 id="top">Film Folk</h1>
 <h2>Festival Diary</h2>
 <p>Here are some of the film festivals we 
 will be attending this year.<br />Please 
 <a href="mailto:filmfolk@example.org">
 contact us</a> if you would like more 
 information.</p>
 <h3>January</h3>
 <p><a href="http://www.sundance.org">
 Sundance Film Festival</a><br />
 Park City, Utah, USA<br />
 20 - 30 January 2011</p>
 <h3>February</h3>
 <p><a href="http://www.tropfest.com">
 Tropfest</a><br />
 Sydney, Australia<br />
 20 February 2011</p>
 <!-- additional content -->
 <p><a href="about.html">About Film Folk</a></p>
 <p><a href="#top">Top of page</a></p>
</body>
</html>
```

* Links are created using the `<a>` element.
* The `<a>` element uses the href attribute to indicate the page you are linking to.
* If you are linking to a page within your own site, it is best to use relative links rather than qualified URLs.
* You can create links to open email programs with an email address in the "to" field.
* You can use the id attribute to target elements within a page that can be linked to.

## Table
```html
<html>
<head>
 <title>Tables</title>
</head>
<body>
 <table>
 <thead>
 <tr>
 <th></th>
 <th scope="col">Home starter hosting</th>
 <th scope="col">Premium business hosting</th>
 </tr>
 </thead>
 <tbody>
 <tr>
 <th scope="row">Disk space</th>
 <td>250mb</td>
 <td>1gb</td>
 </tr>
 <tr>
 <th scope="row">Bandwidth</th>
 <td>5gb per month</td>
 <td>50gb per month</td>
 </tr>
 <!-- more rows like the two above here -->
 </tbody>
 <tfoot>
 <tr>
 <td></td>
 <td colspan="2">Sign up now and save 10%!</td>
 </tr>
 </tfoot>
 </table>
</body>
</html>
```
* The <table> element is used to add tables to a web page.
* A table is drawn out row by row. Each row is created with the <tr> element.
* Inside each row there are a number of cells represented by the <td> element (or <th> if it is a header).
* You can make cells of a table span more than one row or column using the rowspan and colspan attributes.
* For long tables you can split the table into a <thead>, <tbody>, and <tfoot>.

## Image

* The `<img>` element is used to add images to a web page.
* You must always specify a src attribute to indicate the source of an image and an alt attribute to describe the content of an image.
* You should save images at the size you will be using them on the web page and in the appropriate format.
* Photographs are best saved as JPEGs; illustrations or logos that use flat colors are better saved as GIFs.

## Form

Traditionally, the term 'form' has referred to a printed document that contains spaces for you to fill in information.

* Whenever you want to collect information from visitors you will need a form, which lives inside a <form> element.
* Information from a form is sent in name/value pairs.
* Each form control is given a name, and the text the user types in or the values of the options they select are sent to the server.
* HTML5 introduces new form elements which make it easier for visitors to fill in forms.

## Video and audio

* Flash allows you to add animations, video and audio to the web.
* Flash is not supported on iPhone or iPad.
* HTML5 introduces new `<video>` and `<audio>` elements for adding video and audio to web pages, but these are only supported in the latest browsers.
* Browsers that support the HTML5 elements do not all support the same video and audio formats, so you need to supply your files in different formats to ensure that everyone can see/hear them.
