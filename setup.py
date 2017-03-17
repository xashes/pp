from setuptools import setup, find_packages

package = 'pp'
version = '0.1'

setup(
    name=package,
    version=version,
    description="Poker Hands Evaluation",
    url='https://github.com/xashes/pp',
    package=find_packages(exclude=('tests')))
