Font Awesome and Markdown, together!
####################################
For when words aren't enough.
-----------------------------

A Markdown extension that looks for things like ``:fa-coffee:`` and replaces
them with the Font Awesome icon markup.

Installation
------------

    pip install git+git://github.com/barraudf/fontawesome-markdown.git


Dependencies
------------

* [Markdown 2.0+](http://www.freewisdom.org/projects/python-markdown/)

Usage
-----

* From commande line:
    >echo "I ♥ :fa-coffee:" | markdown_py -x fontawesome
    ><p>I ♥ <i class="fa fa-coffee"></i></p>
     
* In a file:
    >from markdown import Markdown
    >from fontawesome_markdown import FontAwesomeExtension
    >markdown = Markdown(extensions=[FontAwesomeExtension()]
    >markdown.convert('i ♥ :fa-coffee:')
    ><p>i ♥ <i class="fa fa-coffee"></i></p>
