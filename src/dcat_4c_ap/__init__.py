try:
    from dcat_4c_ap._version import __version__, __version_tuple__
except ImportError:  # pragma: no cover
    __version__ = "0.0.0"
    __version_tuple__ = (0, 0, 0)

from .datamodel.dcat_4c_ap import *
