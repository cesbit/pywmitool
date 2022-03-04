"""
Upload to PyPI

python3 setup.py sdist
twine upload --repository pypitest dist/pywmitool-X.X.X.tar.gz
twine upload --repository pypi dist/pywmitool-X.X.X.tar.gz
"""
from setuptools import setup, find_packages

try:
    with open('README.md', 'r') as f:
        long_description = f.read()
except IOError:
    long_description = ''

setup(
    name='pywmitool',
    version='0.1.0',  # Update version in pywmitool as well
    description='WMI query tool',
    url='https://github.com/transceptor-technology/pywmitool',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Jeroen van der Heijden',
    author_email='jeroen@transceptor.technology',
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
        'aiowmi'
    ],
    keywords='pywmitool',
)