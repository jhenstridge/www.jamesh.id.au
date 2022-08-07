
import struct
import urlparse
import urllib2
try:
    import datetime
except ImportError:
    datetime = None
import getpass # for getuser

# XXXX hack
if 'ipp' not in urlparse.uses_netloc:
    urlparse.uses_netloc.append('ipp')
    urlparse.uses_relative.append('ipp')

if datetime:
    class _UTCOffset(datetime.tzinfo):
        '''Helper class for representing IPP datetime UTC offsets'''
        def __init__(self, hours, minutes):
            self.offset = datetime.timedelta(hours=hours, minutes=minutes)
            self.name = '%s%02d:%02d' % (hours >= 0 and '+' or '-', abs(hours),
                                         minutes)
        def __repr__(self):
            return "<UTCOffset %s>" % self.name
        def utcoffset(self, dt):
            return self.offset
        def dst(self, dt):
            return datetime.timedelta(0)
        def tzname(self, dt):
            return self.name
    def _as_datetime(s):
        (year, month, day, hour, minute, second,
         decisecond, sign, houroffs, minoffs) = struct.unpack('!HBBBBBBcBB', s)
        if sign == '-': houroffs = -houroffs
        return datetime.datetime(year, month, day, hour, minute, second,
                                 decisecond * 100000,
                                 tzinfo=_UTCOffset(houroffs, minoffs))
    def _from_datetime(dt):
        decisecond = dt.microsecond // 100000
        if dt.tzinfo:
            utcoffs = dt.tzinfo.utcoffset(dt).seconds
        else:
            utcoffs = 0 # assume UTC?
        sign = utcoffs >= 0 and '+' or '-'
        utcoffs = abs(utcoffs)
        houroffs = utcoffs // 3600
        minoffs = (utcoffs // 60) % 60
        return struct.pack('!HBBBBBBcBB', dt.year, dt.month, dt.day,
                           dt.hour, dt.minute, dt.second, decisecond,
                           sign, houroffs, minoffs)
else:
    # should we bother with a more complicated fallback for Python < 2.3?
    def _as_datetime(s):
        return s
    def _from_datetime(dt):
        assert len(dt) == 11, 'date string must be 11 octets long'
        return dt

# attribute group tags
OPERATION_ATTRIBUTES_TAG    = 0x01
JOB_ATTRIBUTES_TAG          = 0x02
END_OF_ATTRIBUTES_TAG       = 0x03
PRINTER_ATTRIBUTES_TAG      = 0x04
UNSUPPORTED_ATTRIBUTES_TAG  = 0x05

# out-of-band value tags
UNSUPORTED_VALUE            = 0x10
DEFAULT_VALUE               = 0x11
UNKNOWN_VALUE               = 0x12
NO_VALUE                    = 0x13

# integer value tags
INTEGER_VALUE               = 0x21
BOOLEAN_VALUE               = 0x22
ENUM_VALUE                  = 0x23
# octetString value tags
OCTET_STRING_VALUE          = 0x30
DATE_TIME_VALUE             = 0x31
RESOLUTION_VALUE            = 0x32
RANGE_OF_INTEGER_VALUE      = 0x33
TEXT_WITH_LANGUAGE_VALUE    = 0x35
NAME_WITH_LANGUAGE_VALUE    = 0x36
# character string value tags
TEXT_WITHOUT_LANGUAGE_VALUE = 0x41
NAME_WITHOUT_LANGUAGE_VALUE = 0x42
KEYWORD_VALUE               = 0x44
URI_VALUE                   = 0x45
URI_SCHEME_VALUE            = 0x46
CHARSET_VALUE               = 0x47
NATURAL_LANGUAGE_VALUE      = 0x48
MIME_MEDIA_TYPE_VALUE       = 0x49

# operation IDs
PRINT_JOB               = 0x0002
PRINT_URI               = 0x0003
VALIDATE_JOB            = 0x0004
CREATE_JOB              = 0x0005
SEND_DOCUMENT           = 0x0006
SEND_URI                = 0x0007
CANCEL_JOB              = 0x0008
GET_JOB_ATTRIBUTES      = 0x0009
GET_JOBS                = 0x000A
GET_PRINTER_ATTRIBUTES  = 0x000B
HOLD_JOB                = 0x000C
RELEASE_JOB             = 0x000D
RESTART_JOB             = 0x000E
PAUSE_PRINTER           = 0x0010
RESUME_PRINTER          = 0x0011
PURGE_JOBS              = 0x0012
SET_JOB_ATTRIBUTES      = 0x0014

# CUPS proprietary operation IDs
CUPS_GET_DEFAULT        = 0x4001
CUPS_GET_PRINTERS       = 0x4002
CUPS_ADD_MODIFY_PRINTER = 0x4003
CUPS_DELETE_PRINTER     = 0x4004
CUPS_GET_CLASSES        = 0x4005
CUPS_ADD_MODIFY_CLASS   = 0x4006
CUPS_DELETE_CLASS       = 0x4007
CUPS_ACCEPT_JOBS        = 0x4008
CUPS_REJECT_JOBS        = 0x4009
CUPS_SET_DEFAULT        = 0x400A
CUPS_GET_DEVICES        = 0x400B
CUPS_GET_PPDS           = 0x400C
CUPS_MOVE_JOB           = 0x400D

class IPPAttributeGroup:
    def __init__(self, grouptag):
        assert 0x00 < grouptag <= 0x0f, 'group tag out of range'
        assert grouptag != END_OF_ATTRIBUTES_TAG, \
               'group tag must not be end-of-attributes-tag'
        self.grouptag = grouptag
        # a dictionary mapping names to [ (type, value) ] lists
        self.attributes = {}
    def __repr__(self):
        groupname = { OPERATION_ATTRIBUTES_TAG: 'operation',
                      JOB_ATTRIBUTES_TAG: 'job',
                      PRINTER_ATTRIBUTES_TAG: 'printer',
                      UNSUPPORTED_ATTRIBUTES_TAG: 'unsupported'
                    }.get(self.grouptag, str(self.grouptag))
        return "<IPPAttributeGroup '%s'>" % groupname
    def keys(self):
        return self.attributes.keys()
    def has_key(self, name):
        return self.attributes.has_key(name)
    def addattr(self, name, type, value):
        self.attributes.setdefault(name, []).append((type, value))
    def getattr(self, name):
        '''get [ (type, value) ] list for attribute name.'''
        return self.attributes[name]
    def __getitem__(self, attr):
        '''get value for attribute name without type information'''
        ret = [ val for (valtype, val) in self.attributes[attr] ]
        if len(ret) == 1: ret = ret[0]
        return ret
    def __setitem__(self, attr, value):
        self.attributes[attr] = value
    def __delitem__(self, attr):
        del self.attributes[attr]
    def as_string(self):
        # empty 
        if not self.attributes: return ''
        ret = [ struct.pack('!B', self.grouptag) ]
        # get list of attribute names.  Order is not important, except that
        # attributes-charset and attributes-natural-language must come first.
        attrnames = self.attributes.keys()
        if 'attributes-natural-language' in self.attributes:
            attrnames.remove('attributes-natural-language')
            attrnames.insert(0, 'attributes-natural-language')
        if 'attributes-charset' in self.attributes:
            attrnames.remove('attributes-charset')
            attrnames.insert(0, 'attributes-charset')
        for name in attrnames:
            first_value = True
            for (type, value) in self.attributes[name]:
                if first_value:
                    ret.append(struct.pack('!Bh', type, len(name)))
                    ret.append(name)
                else:
                    ret.append(struct.pack('!Bh', type, 0))
                first_value = False
                if 0x10 <= type < 0x1f: # out-of-band
                    ret.append(struct.pack('!h', 0))
                # integer types
                elif type in (INTEGER_VALUE, ENUM_VALUE):
                    ret.append(struct.pack('!hi', 4, value))
                elif type == BOOLEAN_VALUE:
                    ret.append(struct.pack('!hb', 1, value != False))
                elif type == DATE_TIME_VALUE:
                    ret.append(struct.pack('!h', 11))
                    ret.append(_from_datetime(value))
                elif 0x30 <= type <= 0x3f: # octet strings
                    ret.append(struct.pack('!h', len(value)))
                    ret.append(value)
                elif 0x40 <= type <= 0x4f: # character strings
                    ret.append(struct.pack('!h', len(value)))
                    ret.append(value)
                else:
                    assert False, 'unhandled value type'
        return ''.join(ret)

class IPPMessage:
    operation_attributes = \
            property(lambda self: self.getgroup(OPERATION_ATTRIBUTES_TAG))
    job_attributes = \
            property(lambda self: self.getgroup(JOB_ATTRIBUTES_TAG))
    printer_attributes = \
            property(lambda self: self.getgroup(PRINTER_ATTRIBUTES_TAG))
    unsupported_attributes = \
            property(lambda self: self.getgroup(UNSUPPORTED_ATTRIBUTES_TAG))
    def __init__(self, version, operation_id, request_id):
        self.version = version
        self.operation_id = operation_id
        self.status_code = operation_id
        self.request_id = request_id
        self.attrgroups = []
        self.data = None
    def addgroup(self, grouptag):
        group = IPPAttributeGroup(grouptag)
        self.attrgroups.append(group)
        return group
    def getgroup(self, grouptag):
        return [ group for group in self.attrgroups
                 if group.grouptag == grouptag ]
    def set_data(self, data):
        self.data = data
    def as_string(self):
        ret = [ struct.pack('!hhi', self.version, self.operation_id,
                            self.request_id) ]
        self.attrgroups.sort(lambda a, b: cmp(a.grouptag, b.grouptag))
        for group in self.attrgroups:
            ret.append(group.as_string())
        ret.append(struct.pack('!B', END_OF_ATTRIBUTES_TAG))

        if self.data:
            ret.append(self.data)
        return ''.join(ret)

status_codes = {
    0x0000: 'successful-ok',
    0x0001: 'successful-ok-ignored-or-substituted-attributes',
    0x0002: 'successful-ok-conflicting-attributes',
    0x0400: 'client-error-bad-request',
    0x0401: 'client-error-forbidden',
    0x0402: 'client-error-not-authenticated',
    0x0403: 'client-error-not-authorized',
    0x0404: 'client-error-not-possible',
    0x0405: 'client-error-timeout',
    0x0406: 'client-error-not-found',
    0x0407: 'client-error-gone',
    0x0408: 'client-error-request-entity-too-large',
    0x0409: 'client-error-request-value-too-long',
    0x040A: 'client-error-document-format-not-supported',
    0x040B: 'client-error-attributes-or-values-not-supported',
    0x040C: 'client-error-uri-scheme-not-supported',
    0x040D: 'client-error-charset-not-supported',
    0x040E: 'client-error-conflicting-attributes',
    0x040F: 'client-error-compression-not-supported',
    0x0410: 'client-error-compression-error',
    0x0411: 'client-error-document-format-error',
    0x0412: 'client-error-document-access-error',
    0x0500: 'server-error-internal-error',
    0x0501: 'server-error-operation-not-supported',
    0x0502: 'server-error-service-unavailable',
    0x0503: 'server-error-version-not-supported',
    0x0504: 'server-error-device-error',
    0x0505: 'server-error-temporary-error',
    0x0506: 'server-error-not-accepting-jobs',
    0x0507: 'server-error-busy',
    0x0508: 'server-error-job-canceled',
    0x0509: 'server-error-multiple-document-jobs-not-supported',
}

class IPPException(Exception):
    def __init__(self, message):
        status_code = message.status_code
        desc = ''
        if status_codes.has_key(status_code): desc += status_codes[status_code]
        group = message.operation_attributes[0]
        if group.attributes.has_key('status-message'):
            desc += ': ' + group['status-message']
        Exception.__init__(self, status_code, desc)

        self.version = message.version
        self.status_code = message.status_code
        self.message = message

def decode(fp, Message=IPPMessage):
    head = fp.read(8)
    (version, operation_id, request_id) = struct.unpack('!hhi', head)
    msg = Message(version, operation_id, request_id)
    grouptag = struct.unpack('!B', fp.read(1))[0]
    while grouptag != END_OF_ATTRIBUTES_TAG:
        group = msg.addgroup(grouptag)
        lastname = None
        valuetype = struct.unpack('!B', fp.read(1))[0]
        while valuetype >= 0x10: # < 0x10 means a new attribute group
            length = struct.unpack('!h', fp.read(2))[0]
            if length > 0:
                name = fp.read(length)
                lastname = name
            else:
                name = lastname
            length = struct.unpack('!h', fp.read(2))[0]
            if length > 0:
                data = fp.read(length)
            else:
                data = ''
            # conversions to native forms
            if valuetype in (INTEGER_VALUE, ENUM_VALUE):
                data = struct.unpack('!i', data)[0]
            elif valuetype == BOOLEAN_VALUE:
                data = struct.unpack('!b', data)[0] != False
            elif valuetype == DATE_TIME_VALUE:
                data = _as_datetime(data)

            group.addattr(name, valuetype, data)
            # next value type
            valuetype = struct.unpack('!B', fp.read(1))[0]
        grouptag = valuetype
    # all attribute groups read
    msg.set_data(fp.read())
    return msg

def send_request(uri, message):
    # convert ipp URIs to http ones that can be used with urllib2
    parts = urlparse.urlparse(uri)
    if parts[0].lower() == 'ipp':
        host = parts[1]
        if ':' not in host: host += ':631'
        uri = urlparse.urlunparse(('http', host) + parts[2:])

    req = urllib2.Request(uri)
    req.add_header('Content-Type', 'application/ipp')
    req.add_data(message.as_string())

    response = decode(urllib2.urlopen(req))
    if response.status_code >= 0x0100: # error
        raise IPPException(response)
    else:
        return response

class IPPObject:
    def __init__(self, uri):
        self.uri = uri
    def __eq__(self, other):
        return self.uri == other.uri
    def _create_message(self, operation):
        # request-id is not necessary for IPP over HTTP
        msg = IPPMessage(0x0101, operation, 0)
        group = msg.addgroup(OPERATION_ATTRIBUTES_TAG)
        group.addattr('attributes-charset', CHARSET_VALUE, 'utf-8')
        group.addattr('attributes-natural-language', NATURAL_LANGUAGE_VALUE,
                      'en-AU')
        group.addattr('requesting-user-name', NAME_WITHOUT_LANGUAGE_VALUE,
                      getpass.getuser())
        return msg

class IPPPrinter(IPPObject):
    def __init__(self, uri):
        IPPObject.__init__(self, uri)
    def __repr__(self):
        return "<IPPPrinter '%s'>" % self.uri
    def _create_message(self, operation):
        msg = IPPObject._create_message(self, operation)
        group = msg.operation_attributes[0]
        group.addattr('printer-uri', URI_VALUE, self.uri)
        return msg        
    def get_attributes(self, names=[]):
        msg = self._create_message(GET_PRINTER_ATTRIBUTES)
        group = msg.operation_attributes[0]
        for name in names:
            group.addattr('requested-attributes', KEYWORD_VALUE, name)
        resp = send_request(self.uri, msg)
        return resp.printer_attributes[0]
    def get_jobs(self, which='not-completed', myjobs=False):
        msg = self._create_message(GET_JOBS)
        group = msg.operation_attributes[0]
        group.addattr('requested-attributes', KEYWORD_VALUE, 'job-uri')
        group.addattr('which-jobs', KEYWORD_VALUE, which)
        group.addattr('my-jobs', BOOLEAN_VALUE, myjobs)
        resp = send_request(self.uri, msg)
        return [ IPPJob(group['job-uri']) for group in resp.job_attributes ]
    def get_job_info(self, attrs=[], which='not-completed', myjobs=False):
        msg = self._create_message(GET_JOBS)
        group = msg.operation_attributes[0]
        for attr in attrs:
            group.addattr('requested-attributes', KEYWORD_VALUE, attr)
        group.addattr('which-jobs', KEYWORD_VALUE, which)
        group.addattr('my-jobs', BOOLEAN_VALUE, myjobs)
        resp = send_request(self.uri, msg)
        return resp.job_attributes

    def pause_printer(self):
        msg = self._create_message(PAUSE_PRINTER)
        try:
            resp = send_request(self.uri, msg)
        except IPPException, e:
            if e.status_code == 1027: # client-not-authorized
                resp = send_request(urlparse.urljoin(self.uri, '/admin/'), msg)
            else:
                raise
    def resume_printer(self):
        msg = self._create_message(RESUME_PRINTER)
        try:
            resp = send_request(self.uri, msg)
        except IPPException, e:
            if e.status_code == 1027: # client-not-authorized
                resp = send_request(urlparse.urljoin(self.uri, '/admin/'), msg)
            else:
                raise
    def purge_jobs(self):
        msg = self._create_message(PURGE_JOBS)
        try:
            resp = send_request(self.uri, msg)
        except IPPException, e:
            if e.status_code == 1027: # client-not-authorized
                resp = send_request(urlparse.urljoin(self.uri, '/admin/'), msg)
            else:
                raise

    # CUPS proprietary operations
    def accept_jobs(self):
        msg = self._create_message(CUPS_ACCEPT_JOBS)
        resp = send_request(urlparse.urljoin(self.uri, '/admin/'), msg)
    def reject_jobs(self):
        msg = self._create_message(CUPS_REJECT_JOBS)
        resp = send_request(urlparse.urljoin(self.uri, '/admin/'), msg)
        

class IPPJob(IPPObject):
    def __init__(self, uri):
        IPPObject.__init__(self, uri)
    def __repr__(self):
        return "<IPPJob '%s'>" % self.uri
    def _create_message(self, operation):
        msg = IPPObject._create_message(self, operation)
        group = msg.operation_attributes[0]
        group.addattr('job-uri', URI_VALUE, self.uri)
        return msg        
    def get_attributes(self, names=[]):
        msg = self._create_message(GET_JOB_ATTRIBUTES)
        group = msg.operation_attributes[0]
        for name in names:
            group.addattr('requested-attributes', KEYWORD_VALUE, name)
        resp = send_request(self.uri, msg)
        return resp.job_attributes[0]
    

class CUPSServer(IPPObject):
    def __init__(self, uri='ipp://localhost/'):
        IPPObject.__init__(self, uri)
    def __repr__(self):
        return "<CUPSServer '%s'>" % self.uri
    def get_default(self):
        msg = self._create_message(CUPS_GET_DEFAULT)
        group = msg.operation_attributes[0]
        group.addattr('requested-attributes', KEYWORD_VALUE,
                      'printer-uri-supported')
        resp = send_request(self.uri, msg)
        group = resp.printer_attributes[0]
        return IPPPrinter(group['printer-uri-supported'])
    def get_printers(self):
        msg = self._create_message(CUPS_GET_PRINTERS)
        group = msg.operation_attributes[0]
        group.addattr('requested-attributes', KEYWORD_VALUE,
                      'printer-uri-supported')
        resp = send_request(self.uri, msg)
        return [ IPPPrinter(group['printer-uri-supported'])
                 for group in resp.printer_attributes ]
    def get_printer_info(self, attrs=[]):
        msg = self._create_message(CUPS_GET_PRINTERS)
        group = msg.operation_attributes[0]
        for attr in attrs:
            group.addattr('requested-attributes', KEYWORD_VALUE, attr)
        resp = send_request(self.uri, msg)
        return resp.printer_attributes
    def get_classes(self):
        msg = self._create_message(CUPS_GET_CLASSES)
        group = msg.operation_attributes[0]
        group.addattr('requested-attributes', KEYWORD_VALUE,
                      'printer-uri-supported')
        resp = send_request(self.uri, msg)
        return [ IPPPrinter(group['printer-uri-supported'])
                 for group in resp.printer_attributes ]
    def get_class_info(self, attrs=[]):
        msg = self._create_message(CUPS_GET_CLASSES)
        group = msg.operation_attributes[0]
        for attr in attrs:
            group.addattr('requested-attributes', KEYWORD_VALUE, attr)
        resp = send_request(self.uri, msg)
        return resp.printer_attributes

