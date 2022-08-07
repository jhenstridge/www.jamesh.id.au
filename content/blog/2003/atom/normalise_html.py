import sys
import urlparse

import libxml2

# turn off errors
def noerr(ctx, str): pass
libxml2.registerErrorHandler(noerr, None)

def parse(data, encoding='ISO-8859-1'):
    '''Parses an HTML fragment, and returns a <div> node containing the
    content in a DOM tree.  This makes it easy to insert into an XML
    document, and also gets rid of problems with unclosed elements.'''

    html_template = '<html><head><title></title></head><body>%s</body></html>'

    doc = libxml2.htmlParseDoc(html_template % data, encoding)
    # body is second element of root node
    body = doc.getRootElement().children.next

    div = libxml2.newNode('div')
    div.setNs(div.newNs('http://www.w3.org/1999/xhtml', None))

    # move nodes over to div
    child = body.children
    while child:
        nextchild = child.next
        child.unlinkNode()
        div.addChild(child)
        child = nextchild
    #doc.free()

    return div

def resolve_relative(node, base_uri):
    '''Makes sure that the URIs in a document are all absolute'''
    for attr in ('src', 'href', 'cite'):
        if node.hasProp(attr):
            node.setProp(attr, urlparse.urljoin(base_uri, node.prop(attr)))

    child = node.children
    while child:
        if child.type == 'element':
            resolve_relative(child, base_uri)
        child = child.next

def sanitise(node, remove_styles=False):
    '''Removes script elements and on* attributes.  Optionally removes
    style related elements and attributes too.

    This is not a fool proof way to sanitise content -- for that, you
    would want a complete list of allowed elements and attributes.'''
    
    # get rid of js handler attributes
    attr = node.properties
    while attr:
        print attr.name
        nextattr = attr.next
        if attr.name.lower().startswith('on') or \
               remove_styles and attr.name.lower() == 'style':
            attr.unlinkNode()
            attr.freeNode()
        attr = nextattr

    child = node.children
    while child:
        nextchild = child.next
        if child.type == 'element':
            if child.name == 'script' or \
                   remove_styles and (child.name == 'style' or
                                      (child.name == 'link' and
                                       child.hasProp('rel') and
                                       child.prop('rel').lower() == 'stylesheet')):
                child.unlinkNode()
                child.freeNode()
            else:
                sanitise(child, remove_styles=remove_styles)
        child = nextchild

doc = libxml2.newDoc('1,0')
div = parse(sys.stdin.read())
resolve_relative(div, 'http://www.gnome.org/~james/')
sanitise(div)
doc.addChild(div)

doc.formatDump(sys.stdout, True)
