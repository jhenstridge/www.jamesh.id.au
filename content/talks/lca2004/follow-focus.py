import ORBit, CORBA
import bonobo, gnome

ORBit.load_typelib('Accessibility')
import Accessibility
import Accessibility__POA

gnome.init('follow-focus', '0.0')
orb = CORBA.ORB_init()

REGISTRY_IID = 'OAFIID:Accessibility_Registry:1.0'
registry = bonobo.activation.activate("iid == '%s'" % REGISTRY_IID)

ev_count = 50

class MyListener(Accessibility__POA.EventListener):
    def ref(self): pass
    def unref(self): pass
    def queryInterface(self, repo_id):
        if repo_id == 'IDL:Accessibility/EventListener:1.0':
            return self._this()
        else:
            return None
    def notifyEvent(self, event):
        global ev_count
        ev_count -= 1
        if ev_count == 0:
            bonobo.main_quit()
        
        print 'type:   ', event.type
        if event.source:
            print 'source: ', event.source.name or 'unnamed', '-', \
                  event.source.getRoleName()
        if event.detail1:
            print 'detail1:', event.detail1
        if event.detail2:
            print 'detail2:', event.detail2
        if event.any_data.value():
            print 'data:   ', event.any_data.value()
        print

listener = MyListener()
objref = listener._this()
listener._default_POA().the_POAManager.activate()

registry.registerGlobalEventListener(objref, 'focus:')

bonobo.main()

registry.deregisterGlobalEventListener(objref, 'focus:')

registry.unref()
