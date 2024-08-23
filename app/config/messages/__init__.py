from os import environ


DEFAULT_LANGUAGE = "en"


if environ.get("lANGUAGE", DEFAULT_LANGUAGE) == "en":
    from .en import (
        ERR_SECURE_PROXY,
    )


__all__ = [
    'ERR_SECURE_PROXY',
]