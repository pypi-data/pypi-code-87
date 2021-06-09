from . import presettings

import random


def file_link_url(request, linkobject):
    """returns the access url of the of the dynamicLink object"""
    return '%s://%s%s/link/%s/%s' % (
        presettings.DYNAMIC_LINK_SCHEMA_PROTO,
        request.META.get('HTTP_HOST'),
        presettings.DYNAMIC_LINK_URL,
        linkobject.link_key,
        linkobject.get_filename()
    )


def site_link_url(request, siteobj):
    """returns a site urls form already given keys"""
    return '%s://%s%s/site/%s' % (
        presettings.DYNAMIC_LINK_SCHEMA_PROTO,
        request.META.get('HTTP_HOST'),
        presettings.DYNAMIC_LINK_URL,
        siteobj.link_key
    )


def gen_key():
    """
    function for generating random keys
    """
    key = ''
    chars = presettings.KEY_POLL
    key_length = presettings.KEY_LENGTH
    for y in range(key_length):
        key += chars[random.randint(0, len(chars) - 1)]
    return key
