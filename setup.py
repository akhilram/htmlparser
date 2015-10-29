from distutils.core import setup

setup(
    name='htmlparser',
    packages=['htmlparser'],
    version='1.0.0',
    description='Parse html to extract required content',
    author='Akhil Ramachandran',
    author_email='akhilram@usc.edu',
    url='https://github.com/akhilram/htmlparser',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
    requires=['html2text', 'bs4']
)
