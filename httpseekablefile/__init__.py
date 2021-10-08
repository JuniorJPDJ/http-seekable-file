__version__ = '0.3.0'


__all__ = []

try:
    import aiohttp

    from .AsyncSeekableHTTPFile import AsyncSeekableHTTPFile
    __all__.append('AsyncSeekableHTTPFile')
except ImportError:
    pass
