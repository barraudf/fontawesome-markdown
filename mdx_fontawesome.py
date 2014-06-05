#! /usr/bin/env python

import markdown
from markdown.extensions import Extension
from markdown.inlinepatterns import Pattern
from markdown.util import etree

fontawesome_pattern = r':(fa-[^:]+):'

class FontAwesomePattern(Pattern):
    def handleMatch(self, m):
        el = etree.Element('i')
        icon_name = m.group(2)
        el.attrib = {'class':'fa {0}'.format(icon_name)}
        return el

class FontAwesomeExtension(Extension):

    def extendMarkdown(self, md, md_globals):
        fontawesome = FontAwesomePattern(fontawesome_pattern)
        md.inlinePatterns.add('fontawesome', fontawesome, '<reference')

def makeExtension(configs={}):
    return FontAwesomeExtension(configs=dict(configs))


if __name__ == "__main__":
    import doctest
    doctest.testmod()