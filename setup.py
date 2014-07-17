try:
    from setuptools import Command
    from setuptools.command.install import install as DefaultInstallCommand
    from setuptools.command.install_lib import install_lib as \
            DefaultInstallLibCommand
except ImportError:
    try:
        from distutils.cmd import Command
        from distutils.command.install import install as DefaultInstallCommand
        from distutils.command.install_lib import install_lib as \
                DefaultInstallLibCommand
    except ImportError:
        Command = object
        class DefaultInstallCommand(Command):
            user_options = []
        class DefaultInstallLibCommand(DefaultInstallCommand):
            pass

from setuptools import find_packages
from setuptools import setup


version = '0.0.7'
long_description = '\n\n'.join([open(f).read() for f in [
    'README.rst',
    'LICENSE.rst',
    'CHANGELOG.rst',
    ]])
requires = [
    ]
tests_require = [
    ]


class InstallCommand(DefaultInstallCommand):

    root = None
    finalized = True
    user_options = (
            DefaultInstallCommand.user_options +
            DefaultInstallLibCommand.user_options
        )
    boolean_options = (
            DefaultInstallCommand.boolean_options +
            DefaultInstallLibCommand.boolean_options
        )

    def __getattribute__(self, attr):
        # To trick options detection
        try:
            return object.__getattribute__(self, attr)
        except AttributeError:
            return None

    def __init__(self, dist):
        pass

    def ensure_finalized(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        print("You've probably made a mistake here and are trying to install "
              "from a 'src' directory which doesn't exist.")
        raise SystemExit(1)


setup(
    name='src',
    version=version,
    description='',
    long_description=long_description,
    keywords='',
    author='Richard Mitchell',
    author_email='mitch@awesomeco.de',
    url='https://github.com/mitchellrj/src',
    license='Apache 2.0',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        ],
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=requires,
    tests_require=tests_require,
    extras_require={
        'test': tests_require,
    },
    entry_points="""
    """,
    cmdclass={
        'install': InstallCommand,
        'install_lib': InstallCommand,
    },
)
