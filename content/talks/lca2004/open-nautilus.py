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

def find_icon(accessible):
    icon = None
    for i in range(accessible.childCount):
        child = accessible.getChildAtIndex(i)
        if child.getRole() == Accessibility.ROLE_ICON:
            return child
        icon = find_icon(child)
        child.unref()
        if icon: break
    return icon



try:
    app = find_app(registry, 'nautilus')
    icon = find_icon(app)

    print 'Openning icon "%s"' % icon.name
    actions = icon.queryInterface('IDL:Accessibility/Action:1.0')
    for i in range(actions.nActions):
        if actions.getName(i) == 'open':
            actions.doAction(i)
finally:
    icon.unref()
    app.unref()
    registry.unref()
