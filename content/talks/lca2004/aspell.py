import popen2

class ASpell:
    def __init__(self, args = ''):
        (self.aspell_stdout,
         self.aspell_stdin) = popen2.popen2('aspell -a %s' % args)
        self.version = self.aspell_stdout.readline()

    def check(self, line):
        '''checks the line of text, and returns a sequence of
        (word, suggestions) tuples.'''
        assert '\n' not in line
        self.aspell_stdin.write(line + '\n')
        self.aspell_stdin.flush()

        ret = []
        line = self.aspell_stdout.readline()
        while line and line != '\n':
            if line[0] == '*':
                pass
            elif line[0] == '&':
                word = line.split(' ')[1]
                matches = [ match.strip()
                            for match in line.split(': ')[1].split(',') ]
                ret.append((word, matches))
            elif line[0] == '#':
                word = line.split(' ')[1]
                ret.append((word, []))
            else:
                raise ValueError('unknown response type %s' % line[0])
            line = self.aspell_stdout.readline()
        return ret
