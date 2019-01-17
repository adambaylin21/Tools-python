# -*- encode:uft8 -*-

import re
from unidecode import unidecode

_punct_re = re.compile(r'[\t !"#$%&\'()*\-/<=>?@\[\\\]^_`{|},.]+')


def slugify(text, delim=u'-'):
    """Generates an ASCII-only slug."""
    result = []
    for word in _punct_re.split(text.lower()):
        result.extend(unidecode(word).split())
    print (unicode(delim.join(result)))

if __name__ == '__main__':
    slugify('Phạm Văn Hải')