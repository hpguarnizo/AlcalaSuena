import os
import uuid

import datetime
from django.utils.deconstruct import deconstructible

# Random name generator to avoid file overwrites
@deconstructible
class RandomFileName(object):
    def __init__(self, path):
        self.path = os.path.join(path, "%s%s")

    def __call__(self, _, filename):
        # @note It's up to the validators to check if it's the correct file type in name or if one even exist.
        extension = os.path.splitext(filename)[1]
        return self.path % (uuid.uuid4(), extension)

LATENIGHT_HOURS = datetime.time(5, 0, 0)
def order_latenight(event_a, event_b):
    if event_a.time == event_b.time:
        return 0
    elif event_a.time < LATENIGHT_HOURS:
        if event_b.time < LATENIGHT_HOURS:
            return -1 if event_a.time < event_b.time else 1
        else:
            return -1
    elif event_b.time < LATENIGHT_HOURS:

        return -1
    else:
        return -1 if event_a.time < event_b.time else 1

def get_query(query_string, search_fields):

    '''
    Returns a query, that is a combination of Q objects.
    That combination aims to search keywords within a model by testing the given search fields.
    '''

    query = None  # Query to search for every search term
    terms = normalize_query(query_string)

    print terms
    for term in terms:
        if len(term) < 3:
            continue
        or_query = None  # Query to search for a given term in each field
        for field_name in search_fields:
            q = Q(**{"%s__icontains" % field_name: term})
            if or_query is None:
                or_query = q
            else:
                or_query = or_query | q
        if query is None:
            query = or_query
        else:
            query = query & or_query

    return query
