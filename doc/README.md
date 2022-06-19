# HTML 5

This document covers HTML 5.

## Minimal HTML 5

```
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <title>Title</title>
  </head>
  <body>
    <!-- Content -->
  </body>
</html>
```

## Basic tags

| Tag | Description |
| --- | --- |
| `<!DOCTYPE html>` | [https://www.w3schools.com/tags/tag_doctype.asp](https://www.w3schools.com/tags/tag_doctype.asp) 'The <!DOCTYPE> declaration must be the very first thing in your HTML document, before the <html> tag. The <!DOCTYPE> declaration is not an HTML tag; it is an instruction to the web browser about what version of HTML the page is written in.' |
| `<html lang="en">`<br>`</html>` | [https://www.w3schools.com/tags/tag_html.asp](https://www.w3schools.com/tags/tag_html.asp) 'The <html> tag is the container for all other HTML elements (except for the <!DOCTYPE> DTD).' The lang="en" attribute specifies the language of the webpage is English (See: https://www.w3schools.com/Tags/ref_language_codes.asp) |
| `<head>`<br>`</head>` | https://www.w3schools.com/tags/tag_head.asp 'The <head> element can include a title for the document, scripts, styles, meta information, and more,' including:  <title> (this element is required in an HTML document), <style>, <base>, <link>, <meta>, <script>, <noscript>.
| `<meta charset="utf-8">` | https://www.w3schools.com/tags/tag_meta.asp 'Metadata is data (information) about data. The <meta> tag provides metadata about the HTML document.' The charset="utf-8" attribute tells the browser that the page is encoded using UTF-8 character encoding. (See: https://www.w3.org/International/articles/definitions-characters/)
<title>
</title>
https://www.w3schools.com/tags/tag_title.asp 'The <title> tag is required in all HTML documents and it defines the title of the document.'
<body>
</body>
https://www.w3schools.com/tags/tag_body.asp 'The <body> tag defines the document's body. The <body> element contains all the contents of an HTML document...'
<p>
</p>
https://www.w3schools.com/tags/tag_p.asp 'The <p> tag defines a paragraph.'
<em>
</em>
https://www.w3schools.com/Tags/tag_em.asp 'The <em> tag is a phrase tag.' The phrase tags are: '<em> (renders as emphasized text), <strong> (defines important text), <code> (defines a piece of computer code), <samp> (defines sample output from a computer program), <kbd> (defines keyboard input), and <var> (defines a variable).'
<h1> — <h6>
</h1> — </h6>
https://www.w3schools.com/tags/tag_hn.asp 'The <h1> to <h6> tags are used to define HTML headings. <h1> defines the most important heading. <h6> defines the least important heading.'
<ul>
</ul>
https://www.w3schools.com/tags/tag_ul.asp The <ul> tag (together with the <li> tag) defines an unordered (bulleted) list. The <ul> tag is a container tag that contains any number of <li> tags.
<ol>
</ol>
https://www.w3schools.com/tags/tag_ol.asp The <ol> tag (together with the <li> tag) defines an unordered (numerical or alphabetical) list. The <ol> tag is a container tag that contains any number of <li> tags.
</li>
</li>
https://www.w3schools.com/tags/tag_li.asp 'The <li> tag defines a list item... used in ordered lists(<ol>), unordered lists (<ul>), and in menu lists (<menu>).'
<img src="smiley.gif" alt="Smiley face">
https://www.w3schools.com/tags/tag_img.asp 'The <img> tag defines an image in an HTML page. The <img> tag has two required attributes: src and alt.'
<a href="http://google.com/">
</a>
https://www.w3schools.com/tags/tag_a.asp 'The <a> tag defines a hyperlink used to link from one page to another. The most important attribute of the <a> element is the href attribute, which indicates the link's destination.'
<!-- This is a comment -->
https://www.w3schools.com/tags/tag_comment.asp 'The comment tag is used to insert comments in the source code. Comments are not displayed in the browsers.'
    </tr>
  </tbody>
</table>