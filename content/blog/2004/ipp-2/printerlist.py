import urllib2
import urlparse
import ipplib
import time

import gobject
import gtk

def _(s): return s

class PrinterListModel(gtk.ListStore):
    URI = 0
    NAME = 1
    DESCRIPTION = 2
    LOCATION = 3
    STATUS = 4
    DOCUMENTS = 5
    def __init__(self, uri='ipp://localhost/'):
        gtk.ListStore.__init__(self, str, str, str, str, str, int)
        self.set_sort_column_id(self.NAME, gtk.SORT_ASCENDING)
        self.server = ipplib.CUPSServer(uri)
        self.refresh()
    def refresh(self):
        self.clear()
        # dictionary mapping printer URIs to their liststore row
        rows = dict([(row[self.URI], row) for row in self])
        for info in self.server.get_printer_info() + \
                self.server.get_class_info():
            state = { 3: 'idle',
                      4: 'processing',
                      5: 'stopped' }.get(info['printer-state'], '')
            if info['printer-state-reasons'] != 'none':
                if isinstance(info['printer-state-reasons'], str):
                    state += ' (%s)' % info['printer-state-reasons']
                else:
                    state += ' (%s)' % ', '.join(info['printer-state-reasons'])
            if info.has_key('printer-state-message') \
                   and info['printer-state-message']:
                state += ' - %s' % info['printer-state-message']
            data = (info['printer-uri-supported'],
                    info['printer-name'],
                    info['printer-info'],
                    info['printer-location'],
                    state,
                    info['queued-job-count'])
            row = rows.get(data[self.URI])
            if row:
                row[self.NAME]        = data[self.NAME]
                row[self.DESCRIPTION] = data[self.DESCRIPTION]
                row[self.LOCATION]    = data[self.LOCATION]
                row[self.STATUS]      = data[self.STATUS]
                row[self.DOCUMENTS]   = data[self.DOCUMENTS]
                del rows[data[self.URI]]
            else:
                self.append(data)
        # remove remaining rows
        for row in rows.values():
            self.remove(row.iter)

class JobListModel(gtk.ListStore):
    URI = 0
    JOBID = 1
    NAME = 2
    OWNER = 3
    SIZE = 4
    SUBMITTED = 5
    STATUS = 6
    def __init__(self, uri):
        gtk.ListStore.__init__(self, str, int, str, str, str, str, str)
        self.set_sort_column_id(self.JOBID, gtk.SORT_ASCENDING)
        self.server = ipplib.IPPPrinter(uri)
        self.myjobs = False
        self.which = 'not-completed'
        self.refresh()
    def show_myjobs(self, myjobs):
        self.myjobs = myjobs != False
    def show_completed(self, completed):
        if completed:
            self.which = 'completed'
        else:
            self.which = 'not-completed'
    def refresh(self):
        self.clear()
        # dictionary mapping printer URIs to their liststore row
        rows = dict([(row[self.URI], row) for row in self])
        attrs = ['job-id', 'job-uri', 'job-name', 'job-originating-user-name',
                 'job-state', 'job-state-reasons', 'job-state-message',
                 'job-k-octets', 'time-at-creation']
        for info in self.server.get_job_info(attrs=attrs,
                                             which=self.which,
                                             myjobs=self.myjobs):
            state = { 3: 'pending',
                      4: 'pending-held',
                      5: 'processing',
                      6: 'processing-stopped',
                      7: 'canceled',
                      8: 'aborted',
                      9: 'completed',}.get(info['job-state'], '')
            if info['job-state-reasons'] != 'none':
                if isinstance(info['job-state-reasons'], str):
                    state += ' (%s)' % info['job-state-reasons']
                else:
                    state += ' (%s)' % ', '.join(info['job-state-reasons'])
            if info.has_key('job-state-message') \
                   and info['job-state-message']:
                state += ' - %s' % info['job-state-message']
            name = info['job-name']
            if type(name) == type([]):
                name = name[0]
            data = (info['job-uri'],
                    info['job-id'],
                    name,
                    info['job-originating-user-name'],
                    '%dk' % info['job-k-octets'],
                    info['time-at-creation'],
                    state)
            row = rows.get(data[self.URI])
            if row:
                row[self.JOBID] = data[self.JOBID]
                row[self.NAME] = data[self.NAME]
                row[self.OWNER] = data[self.OWNER]
                row[self.SIZE] = data[self.SIZE]
                row[self.SUBMITTED] = data[self.SUBMITTED]
                row[self.STATUS] = data[self.STATUS]
                del rows[data[self.URI]]
            else:
                self.append(data)
        # remove remaining rows
        for row in rows.values():
            self.remove(row.iter)

class PasswordMgr(urllib2.HTTPPasswordMgr):
    def find_user_password(self, realm, authuri):
        user, password = \
              urllib2.HTTPPasswordMgr.find_user_password(self, realm, authuri)
        if user is not None:
            return user, password

        dialog = gtk.Dialog(_('Enter Password'), None, gtk.DIALOG_MODAL,
                            (gtk.STOCK_OK, gtk.RESPONSE_OK,
                             gtk.STOCK_CANCEL, gtk.RESPONSE_CANCEL))
        table = gtk.Table(3, 2, False)
        table.set_col_spacings(12)
        table.set_row_spacings(6)
        dialog.vbox.add(table)
        
        label = gtk.Label(_('Enter username and password for "%s" at %s')
                          % (realm, authuri))
        table.attach(label, 0, 2, 0, 1,
                     gtk.FILL|gtk.EXPAND, gtk.FILL|gtk.EXPAND, 0, 0)

        label = gtk.Label(_('User name:'))
        table.attach(label, 0, 1, 1, 2, gtk.FILL, gtk.FILL|gtk.EXPAND, 0, 0)
        user_entry = gtk.Entry()
        table.attach(user_entry, 1,2, 1,2,
                     gtk.FILL|gtk.EXPAND, gtk.FILL|gtk.EXPAND, 0, 0)

        label = gtk.Label(_('Password:'))
        table.attach(label, 0, 1, 2, 3, gtk.FILL, gtk.FILL|gtk.EXPAND, 0, 0)
        password_entry = gtk.Entry()
        password_entry.set_visibility(False)
        table.attach(password_entry, 1,2, 2,3,
                     gtk.FILL|gtk.EXPAND, gtk.FILL|gtk.EXPAND, 0, 0)

        dialog.show_all()
        response = dialog.run()

        if response == gtk.RESPONSE_OK:
            user = user_entry.get_text()
            password = password_entry.get_text()
            self.add_password(realm, authuri, user, password)

        dialog.destroy()

        return user, password

mgr = PasswordMgr()
opener = urllib2.build_opener(urllib2.HTTPBasicAuthHandler(mgr),
                              urllib2.HTTPDigestAuthHandler(mgr))
urllib2.install_opener(opener)
del mgr, opener


class PrinterListWindow(gtk.Window):
    def __init__(self, uri='ipp://localhost/'):
        gtk.Window.__init__(self)
        self.set_default_size(500, 250)
        self.uri = uri
        self.set_title(_('Printer Manager'))

        self.model = PrinterListModel(uri)

        self.vbox = gtk.VBox()
        self.add(self.vbox)

        accelgroup = gtk.AccelGroup()
        self.add_accel_group(accelgroup)
        self.itemfactory = gtk.ItemFactory(gtk.MenuBar, '<main>', accelgroup)
        self.itemfactory.create_items([
            ('/_Printer', None, None, 0, '<Branch>'),
            ('/Printer/_Open', None, self.open, 0),
            ('/Printer/sep2', None, None, 0, '<Separator>'),
            ('/Printer/_Quit', '<control>Q', self.close, 0,
             '<StockItem>', gtk.STOCK_QUIT),
            ('/_View', None, None, 0, '<Branch>'),
            ('/View/_Refresh', '<control>R', self.refresh, 0,
             '<StockItem>', gtk.STOCK_REFRESH),
            ])
        self.vbox.pack_start(self.itemfactory.get_widget('<main>'),
                             expand=False)

        swin = gtk.ScrolledWindow()
        swin.set_policy(gtk.POLICY_AUTOMATIC, gtk.POLICY_AUTOMATIC)
        self.vbox.pack_start(swin)

        treeview = gtk.TreeView(self.model)
        treeview.set_rules_hint(True)
        self.selection = treeview.get_selection()
        self.selection.set_mode(gtk.SELECTION_BROWSE)

        column = gtk.TreeViewColumn(_('Name'), gtk.CellRendererText(),
                                    text=self.model.NAME)
        column.set_resizable(True)
        column.set_sort_column_id(self.model.NAME)
        treeview.append_column(column)

        column = gtk.TreeViewColumn(_('Description'), gtk.CellRendererText(),
                                    text=self.model.DESCRIPTION)
        column.set_resizable(True)
        column.set_sort_column_id(self.model.DESCRIPTION)
        treeview.append_column(column)

        column = gtk.TreeViewColumn(_('Location'), gtk.CellRendererText(),
                                    text=self.model.LOCATION)
        column.set_resizable(True)
        column.set_sort_column_id(self.model.LOCATION)
        treeview.append_column(column)

        column = gtk.TreeViewColumn(_('Status'), gtk.CellRendererText(),
                                    text=self.model.STATUS)
        column.set_resizable(True)
        column.set_sort_column_id(self.model.STATUS)
        treeview.append_column(column)

        column = gtk.TreeViewColumn(_('Documents'), gtk.CellRendererText(),
                                    text=self.model.DOCUMENTS)
        column.set_sort_column_id(self.model.DOCUMENTS)
        treeview.append_column(column)

        treeview.connect('row_activated', self.row_activated)

        swin.add(treeview)

        self.vbox.show_all()

        # refresh every 30 seconds
        self.timer_id = gobject.timeout_add(30000, self.refresh)
        self.connect('destroy', self.destroy_cb)

    def destroy_cb(self, widget):
        if self.timer_id: gobject.source_remove(self.timer_id)
        self.timer_id = 0

    def open(self, action, widget):
        model, iter = self.selection.get_selected()
        if iter:
            printer_uri = self.model[iter][self.model.URI]
            window = JobListWindow(printer_uri)
            window.show()
            
    def close(self, action=0, widget=None):
        self.destroy()
    def refresh(self, action=0, widget=None):
        model, iter = self.selection.get_selected()
        if iter:
            printer_uri = self.model[iter][self.model.URI]
        else:
            printer_uri = None
        self.model.refresh()
        if printer_uri:
            for row in self.model:
                if row[self.model.URI] == printer_uri:
                    self.selection.select_iter(row.iter)
                    break
        return True
    def row_activated(self, treeview, path, column):
        printer_uri = self.model[path][self.model.URI]
        window = JobListWindow(printer_uri)
        window.show()

class JobListWindow(gtk.Window):
    def __init__(self, uri='ipp://localhost/'):
        gtk.Window.__init__(self)
        self.uri = uri
        self.set_default_size(500, 250)

        self.printer = ipplib.IPPPrinter(uri)
        self.model = JobListModel(uri)

        self.vbox = gtk.VBox()
        self.add(self.vbox)

        accelgroup = gtk.AccelGroup()
        self.add_accel_group(accelgroup)
        self.itemfactory = gtk.ItemFactory(gtk.MenuBar, '<jobs>', accelgroup)
        self.itemfactory.create_items([
            ('/_Printer', None, None, 0, '<Branch>'),
            ('/Printer/Pause Queue', None, self.pause_queue, True),
            ('/Printer/Resume Queue', None, self.pause_queue, False),
            ('/Printer/sep1', None, None, 0, '<Separator>'),
            ('/Printer/Accept Jobs', None, self.accept_jobs, True),
            ('/Printer/Reject Jobs', None, self.accept_jobs, False),
            ('/Printer/sep2', None, None, 0, '<Separator>'),
            ('/Printer/_Close', '<control>W', self.close, 0,
             '<StockItem>', gtk.STOCK_CLOSE),
            ('/_View', None, None, 0, '<Branch>'),
            ('/View/Show Completed Jobs', None, self.changeview, 0, '<ToggleItem>'),
            ('/View/Show Only My Jobs', None, self.changeview, 0, '<ToggleItem>'),
            ('/View/sep1', None, None, 0, '<Separator>'),
            ('/View/_Refresh', '<control>R', self.refresh, 0,
             '<StockItem>', gtk.STOCK_REFRESH),
            ])
        self.vbox.pack_start(self.itemfactory.get_widget('<jobs>'),
                             expand=False)

        swin = gtk.ScrolledWindow()
        swin.set_policy(gtk.POLICY_AUTOMATIC, gtk.POLICY_AUTOMATIC)
        self.vbox.pack_start(swin)

        treeview = gtk.TreeView(self.model)
        treeview.set_rules_hint(True)
        self.selection = treeview.get_selection()
        self.selection.set_mode(gtk.SELECTION_BROWSE)

        column = gtk.TreeViewColumn(_('Name'), gtk.CellRendererText(),
                                    text=self.model.NAME)
        column.set_resizable(True)
        column.set_sort_column_id(self.model.NAME)
        treeview.append_column(column)

        column = gtk.TreeViewColumn(_('ID'), gtk.CellRendererText(),
                                    text=self.model.JOBID)
        column.set_sort_column_id(self.model.JOBID)
        treeview.append_column(column)

        column = gtk.TreeViewColumn(_('Owner'), gtk.CellRendererText(),
                                    text=self.model.OWNER)
        column.set_resizable(True)
        column.set_sort_column_id(self.model.OWNER)
        treeview.append_column(column)

        column = gtk.TreeViewColumn(_('Size'), gtk.CellRendererText(),
                                    text=self.model.SIZE)
        column.set_sort_column_id(self.model.SIZE)
        treeview.append_column(column)

        column = gtk.TreeViewColumn(_('Status'), gtk.CellRendererText(),
                                    text=self.model.STATUS)
        column.set_resizable(True)
        column.set_sort_column_id(self.model.STATUS)
        treeview.append_column(column)

        swin.add(treeview)

        self.vbox.show_all()

        self.update_printer_info()

        # refresh every 30 seconds
        self.timer_id = gobject.timeout_add(30000, self.refresh)
        self.connect('destroy', self.destroy_cb)

    def destroy_cb(self, widget):
        if self.timer_id: gobject.source_remove(self.timer_id)
        self.timer_id = 0

    def close(self, action=0, widget=None):
        self.destroy()
    def update_printer_info(self):
        self.printer_info = self.printer.get_attributes()
        name = self.printer_info['printer-name']
        hostname = urlparse.urlparse(self.uri)[1]
        stopped = (self.printer_info['printer-state'] == 5)
        accept = self.printer_info['printer-is-accepting-jobs']

        title = _('%s on %s') % (name, hostname)
        if stopped:
            title += _(' [stopped]')
        if not accept:
            title += _(' [rejecting jobs]')
        self.set_title(title)

        pause_queue = self.itemfactory.get_widget('<jobs>/Printer/Pause Queue')
        resume_queue = self.itemfactory.get_widget('<jobs>/Printer/Resume Queue')
        accept_jobs = self.itemfactory.get_widget('<jobs>/Printer/Accept Jobs')
        reject_jobs = self.itemfactory.get_widget('<jobs>/Printer/Reject Jobs')

        pause_queue.set_sensitive(not stopped)
        resume_queue.set_sensitive(stopped)
        accept_jobs.set_sensitive(not accept)
        reject_jobs.set_sensitive(accept)

    def refresh(self, action=0, widget=None):
        model, iter = self.selection.get_selected()
        if iter:
            job_uri = self.model[iter][self.model.URI]
        else:
            job_uri = None
        self.model.refresh()
        if job_uri:
            for row in self.model:
                if row[self.model.URI] == job_uri:
                    self.selection.select_iter(row.iter)
                    break
        self.update_printer_info()
        return True

    def changeview(self, action, widget):
        completed = self.itemfactory.get_widget('<jobs>/View/Show Completed Jobs').get_active()
        myjobs = self.itemfactory.get_widget('<jobs>/View/Show Only My Jobs').get_active()
        self.model.show_completed(completed)
        self.model.show_myjobs(myjobs)
        self.refresh()

    def pause_queue(self, action, widget):
        if action: # pause
            self.printer.pause_printer()
        else:
            self.printer.resume_printer()
        self.update_printer_info()
    def accept_jobs(self, action, widget):
        if action: # accept
            self.printer.accept_jobs()
        else:
            self.printer.reject_jobs()
        self.update_printer_info()

if __name__ == '__main__':
    import sys

    if len(sys.argv) == 2:
        uri = 'ipp://%s/' % sys.argv[1]
    elif len(sys.argv) == 1:
        uri = 'ipp://localhost/'
    else:
        sys.stderr.write('usage: %s [hostname]\n' % sys.argv[0])
        sys.exit(1)
    
    window = PrinterListWindow(uri)
    window.connect('destroy', lambda x: gtk.main_quit())

    window.show_all()

    gtk.main()
