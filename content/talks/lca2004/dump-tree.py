import sys

import ORBit
import bonobo, gnome

ORBit.load_typelib('Accessibility')
import Accessibility
gnome.init('dump-tree', '0.0')

REGISTRY_IID = 'OAFIID:Accessibility_Registry:1.0'
registry = bonobo.activation.activate("iid == '%s'" % REGISTRY_IID)

def find_app(registry, name):
    '''Iterates over each app on each desktop til it finds one with a
    matching name, which is then returned.'''
    for desknum in range(registry.getDesktopCount()):
        desktop = registry.getDesktop(desknum)
        for i in range(desktop.childCount):
            child = desktop.getChildAtIndex(i)
            if child.name == name:
                desktop.unref()
                return child
            child.unref()
        desktop.unref()
    raise ValueError('could not find application %s' % name)

def dump_tree(accessible, indent=''):
    name = accessible.name or 'unnamed'
    role = accessible.getRoleName()
    description = accessible.description
    print '%s* %s "%s": %s' % (indent, role, name, description)
    for i in range(accessible.childCount):
        child = accessible.getChildAtIndex(i)
        dump_tree(child, indent + '   ')
        child.unref()

if len(sys.argv) != 2:
    sys.stderr.write('usage: dump-tree.py appname\n')
    sys.exit(1)

try:
    app = find_app(registry, sys.argv[1])
    dump_tree(app)
finally:
    app.unref()
    registry.unref()
