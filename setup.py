import pathlib
from setuptools import setup, find_packages


here = pathlib.Path(__file__).parent.resolve()

with open('README.rst') as f:
    readme = f.read()


setup(
    name='aiotube',
    version='1.5.3',
    description='A library to access YouTube Public Data without YouTubeAPI',
    long_description=readme,
    long_description_content_type="text/x-rst",
    url='https://github.com/jnsougata/aiotube',
    author='jnsougata',
    author_email='jnsougata@gmail.com',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Topic :: Internet',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Utilities',
    ],
    keywords='youtube, youtube-data, youtube-api, youtube-data-api-v3',
    package_dir={'': 'src'},
    packages=find_packages(where='src'),
    python_requires='>=3.8.0',
    install_requires=['urllib3'],
    project_urls={
        'Documentation': 'https://aiotube.readthedocs.io/en/latest/',
        'Source': 'https://github.com/jnsougata/aiotube'
    },
)
