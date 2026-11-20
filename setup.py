
import setuptools


def _read_version():

    with open('diagnosticism/__init__.py') as source:

        for line in source:

            if line.startswith('__version__'):

                return line.split('=', 1)[1].strip().strip("'\"")

    raise RuntimeError('__version__ was not found')


setuptools.setup(

    name='diagnosticism',
    python_requires='>=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*, !=3.4.*, !=3.5.*, !=3.6.*, !=3.7.*',
    version=_read_version(),

    author='Matt Wilson',
    author_email='matthew@synesis.com.au',
    classifiers=[

        'Intended Audience :: Developers',
        "License :: OSI Approved :: BSD License",
        'Natural Language :: English',
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
        "Programming Language :: Python :: 3.14",
    ],
    description='Basic diagnostic facilities, for Python',
    keywords='Diagnostic Diagnostics Logging Trace Tracing Stopwatch',
    license='BSD-3-Clause',
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(exclude=[
        'examples',
        'tests',
    ]),
    url='https://github.com/synesissoftware/Diagnosticism.Python',
)
