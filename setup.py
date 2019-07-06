
import setuptools

setuptools.setup(

    name='diagnosticism',
    version='0.2.0',

    author='Matt Wilson',
    author_email='matthew@synesis.com.au',
    description='Basic diagnostic facilities, for Python',
    keywords='Diagnostic Diagnostics Logging Trace Tracing Stopwatch',
    license='BSD-3-Clause',
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    packages=['diagnosticism', 'examples', 'tests'],
    url='https://github.com/synesissoftware/diagnosticism.Python',
    classifiers=[

        'Intended Audience :: Developers',
        "License :: OSI Approved :: BSD License",
        'Natural Language :: English',
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
    ],
)

