import re
import unicodedata

import random
import string

# using this slugify function instead of previously use one: 'from django.utils.text import slugify'
SLUG_OK = "-_~"


def slugify(s, ok=SLUG_OK, lower=True, spaces=False):
    # L and N signify letter/number.
    # http://www.unicode.org/reports/tr44/tr44-4.html#GC_Values_Table
    rv = []
    s = re.sub("\s*&\s*", " and ", s)
    for c in unicodedata.normalize("NFKC", s):
        cat = unicodedata.category(c)[0]
        if cat in "LN" or c in ok:
            rv.append(c)
        if cat == "Z":  # space
            rv.append(" ")
    new = "".join(rv).strip()
    if not spaces:
        new = re.sub("[-\s]+", "-", new)
    return new.lower() if lower else new



def random_string_generator(size=10, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


def unique_slug_generator(instance, new_slug=None):
    
    if new_slug is not None:
        slug = new_slug
    else:
        slug = slugify(instance.name)

    Klass = instance.__class__
    qs_exists = Klass.objects.filter(slug=slug).exists()
    if qs_exists:
        new_slug = "{slug}-{randstr}".format(
            slug=slug,
            randstr=random_string_generator(size=4)
        )
        return unique_slug_generator(instance, new_slug=new_slug)
    return slug
