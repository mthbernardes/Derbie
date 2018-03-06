import os
import sys
from core.generator import Generator 


if len(sys.argv) < 3:
    print('SYNTAX ERROR\npython {} package-name script-file.sh'.format(sys.argv[0]))
    sys.exit(-1)

if not os.path.exists(sys.argv[2]):
    print('Script file does not exist!')
    sys.exit(-1)


package = sys.argv[1]
scriptfile = sys.argv[2]
deb = Generator()
deb.create(package,scriptfile)
