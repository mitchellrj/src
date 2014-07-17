src
===

Not your source.

Because sometimes you mistype filenames or files aren't where you
expect them. Package managers should never punish the user by
downloading and running remote code in this case.

This package mitigates the risk and safely exits in the case that
you mistype ``easy_install src`` or ``pip install src`` when no ``src``
directory exists.

See also:

* https://github.com/pypa/pip/issues/1940
* https://bitbucket.org/pypa/setuptools/issue/235
