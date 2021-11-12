import pytest

from http_seekable_file import AsyncSeekableHTTPFile

# TODO: test Content-Disposition name


@pytest.mark.asyncio
async def test_async():
    async with AsyncSeekableHTTPFile('https://raw.githubusercontent.com/torvalds/linux/master/LICENSES/preferred/GPL-2.0') as f:
        assert f.name == 'GPL-2.0'
        assert len(f) == 18729
        assert await f.read(10) == b'Valid-Lice'
        assert await f.read(10) == b'nse-Identi'
        await f.seek(3)
        assert await f.read(10) == b'id-License'
        assert await f.read(10) == b'-Identifie'
        assert await f.readline() == b'r: GPL-2.0\n'
