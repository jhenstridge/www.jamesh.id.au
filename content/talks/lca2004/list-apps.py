import ORBit
import bonobo, gnome

ORBit.load_typelib('Accessibility')
gnome.init('list-apps', '0.0')

REGISTRY_IID = 'OAFIID:Accessibility_Registry:1.0'
registry = bonobo.activation.activate("iid == '%s'" % REGISTRY_IID)

# get first desktop
desktop = registry.getDesktop(0)

for i in range(desktop.childCount):
    child = desktop.getChildAtIndex(i)
    print child.name
    child.unref()

desktop.unref()
registry.unref()
