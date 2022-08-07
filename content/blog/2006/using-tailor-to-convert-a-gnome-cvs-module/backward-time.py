import sys
import os

def prev_rev(rev):
    '''Returns a string representing the previous revision of the argument.'''
    r = rev.split('.')
    # decrement final revision component
    r[-1] = str(int(r[-1]) - 1)
    # prune if we pass the beginning of the branch
    if len(r) > 2 and r[-1] == '0':
        r = r[:-2]
    return '.'.join(r)


filename = sys.argv[1]

os.environ['FILENAME'] = filename
fp = os.popen('rlog "$FILENAME"', 'r')

# get the revision dates
revisiondates = {}
line = fp.readline()
while line:
    if line.startswith('revision '):
        rev = line[9:].strip()
        line = fp.readline()
        if not line: continue
        if not line.startswith('date: '): continue
        date = line[6:25]

        revisiondates[rev] = date
    line = fp.readline()
fp.close()

found_errors = False

revisions = revisiondates.items()
revisions.sort()

for (rev, date) in revisions:
    prev = prev_rev(rev)
    if revisiondates.has_key(prev):
        if date < revisiondates[prev]:
            if not found_errors:
                print filename
                found_errors = True
            print '  %-20s - %s < %s' % (rev, date, revisiondates[prev])

if found_errors:
    print
