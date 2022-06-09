"""
Upload to PyPI

python setup.py sdist
twine upload --repository pypitest dist/pywmitool-X.X.X.tar.gz
twine upload --repository pypi dist/pywmitool-X.X.X.tar.gz
"""
from setuptools import setup, find_packages

try:
    with open('README.md', 'r') as f:
        long_description = f.read()
except IOError:
    long_description = ''

version = '0.1.3'  # Update version in bin/pywmitool as well

setup(
    name='pywmitool',
    version=version,
    description='WMI query tool',
    url='https://github.com/cesbit/pywmitool',
    download_url=(
        'https://github.com/cesbit/'
        'pywmitool/tarball/v{}'.format(version)),
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Jeroen van der Heijden',
    author_email='jeroen@cesbit.com',
    scripts=['bin/pywmitool'],
    license='MIT',
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 4 - Beta',

        # Indicate who your project is intended for
        'Intended Audience :: Developers',
        'Topic :: Database :: Front-Ends ',

        # Pick your license as you wish (should match "license" above)
        'License :: OSI Approved :: MIT License',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ],
    install_requires=[
        'aiowmi>=0.1.13'
    ],
    keywords='pywmitool',
)
