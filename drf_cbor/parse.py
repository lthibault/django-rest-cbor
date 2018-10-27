import cbor2 as cbor
from rest_framework.parsers import BaseParser
from .render import CBORRenderer


class CBORParser(BaseParser):
    """parse CBOR-serialized data with the highly-optimized `cbor2` package.
    """

    media_type = 'application/cbor'
    renderer_class = CBORRenderer

    def parse(self, stream, media_type=None, parser_context=None):
        """parse the incoming bytestream as CBOR and returns the resulting data
        """
        return cbor.load(stream)