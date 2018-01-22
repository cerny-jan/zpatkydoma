from unidecode import unidecode
from taggit.utils import _parse_tags


def comma_splitter(tag_string):
    result = _parse_tags(tag_string)
    return [unidecode(r.lower()) for r in result]
