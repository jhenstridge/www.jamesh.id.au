#!/usr/bin/env python

import sys, os, re

slideheader = '<html>\n' + \
	      '  <head>\n' + \
	      '    <title>%(prefix)s: %(title)s</title>\n' + \
	      '    <link rel="StyleSheet" href="%(prefix)s.css" type="text/css">\n' + \
	      '  </head>\n' + \
	      '  <body>\n'

slidefooter = '  </body>\n' + \
	      '</html>\n'


slidestart = re.compile(r'<slide title="(.*)">')
slideend = re.compile(r'</slide>')

if len(sys.argv) < 2:
    sys.stderr.write('Usage: slides.py filename')

filename = sys.argv[1]

prefix = os.path.splitext(filename)[0]

fp = open(filename, 'r')
out = None
write_out = False

for line in fp:
    m = slidestart.search(line)
    if m:
        if out is None:
	    out = open("%s.html" % prefix, 'w')
	    out.write(slideheader % { 'title': m.group(1),
				      'prefix': prefix})
        out.write('    <div class="slide">\n')
        write_out = True
	line = ''
    m = slideend.search(line)
    if m:
        out.write('    </div>\n')
        write_out = False
    if write_out:
	out.write(line)

if out is not None:
    out.write(slidefooter)
