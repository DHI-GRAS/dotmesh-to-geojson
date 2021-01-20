try:
    from dotmeshgj._version import version as __version__  # noqa: F401
except ImportError:  # pragma: no cover
    raise RuntimeError(
        "Package has not been installed correctly. Please run `pip install -e .` or "
        "`python setup.py develop` in the package folder."
    ) from None
