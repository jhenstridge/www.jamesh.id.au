import aspell
import ORBit, CORBA
import bonobo, gnome

ORBit.load_typelib('Accessibility')
import Accessibility
import Accessibility__POA

gnome.init('spell-check', '0.0')
orb = CORBA.ORB_init()

REGISTRY_IID = 'OAFIID:Accessibility_Registry:1.0'
registry = bonobo.activation.activate("iid == '%s'" % REGISTRY_IID)

spell = aspell.ASpell('--master=british')

ev_count = 10

class MyListener(Accessibility__POA.EventListener):
    def ref(self): pass
    def unref(self): pass
    def queryInterface(self, repo_id):
        if repo_id == 'IDL:Accessibility/EventListener:1.0':
            return self._this()
        else:
            return None
    def notifyEvent(self, event):
        # get the word at the carret
        atext = event.source.queryInterface('IDL:Accessibility/Text:1.0')
        (word, start, end) = atext.getTextAtOffset(atext.caretOffset,
                                     Accessibility.TEXT_BOUNDARY_WORD_START)

        # we only care when the whole word has been printed
        if not word or word[-1] not in ' \n\t': return
        word = word[:-1]

        corrections = spell.check(word)
        if corrections:
            print word, 'is misspelled?', chr(7)
            for w, suggestions in corrections:
                print '  ', w, '->', ', '.join(suggestions)
        else:
            return

        global ev_count
        ev_count -= 1
        if ev_count == 0:
            bonobo.main_quit()


listener = MyListener()
objref = listener._this()
listener._default_POA().the_POAManager.activate()

registry.registerGlobalEventListener(objref, 'object:text-changed')

bonobo.main()

registry.deregisterGlobalEventListener(objref, 'object:text-changed')

registry.unref()
