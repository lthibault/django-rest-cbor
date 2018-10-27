from rest_framework.renderers import BaseRenderer
import cbor2 as cbor


class CBORRenderer(BaseRenderer):
    """Renderer which serializes to CBOR using the highly-optimized `cbor2`
    package.
    """

    media_type = 'application/cbor'
    format = 'cbor'
    charset = None
    render_style = 'binary'

    def render(self, data, *args, **kwargs):
        if data is None:
            return ''
        return cbor.dumps(data)
