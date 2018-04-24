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

slidenum = 0

fp = open(filename, 'r')
out = None

line = fp.readline()
while line:
	m = slidestart.search(line)
	if m:
		out = open("%(prefix)s-%(slidenum)d.html" %
			   { 'prefix': prefix, 'slidenum': slidenum }, 'w')
		slidenum = slidenum + 1
		out.write(slideheader % { 'title': m.group(1),
					  'prefix': prefix})
		line = ''
	m = slideend.search(line)
	if m:
		if out:
			out.write('\n    <hr noshade>\n')
			out.write('    <table width="80%" align=center><tr>\n')
			if slidenum > 1:
				out.write('      <td align="left">')
				out.write('<a href="' + prefix + '-' +
					  str(slidenum - 2) + '.html">')
				out.write('Prev</a></td>\n')
			out.write('      <td align="right">')
			out.write('<a href="' + prefix + '-' +
				  str(slidenum) + '.html">')
			out.write('Next</a></td>\n')
			out.write('    </tr></table>\n')
			out.write(slidefooter)
			out.close()
		out = None
	if out:
		out.write(line)
	line = fp.readline()
