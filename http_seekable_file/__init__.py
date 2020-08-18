__version__ = '0.1.0'

try:
    import aiohttp

    from .AsyncSeekableHTTPFile import AsyncSeekableHTTPFile
except ImportError:
    pass

