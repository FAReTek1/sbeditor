from setuptools import setup
import subprocess

# Copied from https://www.youtube.com/watch?v=U-aIPTS580s
# remote_version = subprocess.run(['git', 'describe', '--tags'], stdout=subprocess.PIPE).stdout.decode('utf-8').strip()
# assert '.' in remote_version

# with open('README.md', 'r', encoding="utf-8") as readme:
#     long_description = readme.read()

# print(remote_version)

setup(
    name='sbeditor',
    version="v0.0.0-beta.5",
    packages=['sbeditor'],
    url='https://github.com/FAReTek1/sbeditor',
    license='MIT',
    author='faretek1',
    author_email='',
    description='A parser for all things sb3',
    long_description=
    """
    A parser for all things sb3! This is a module made by faretek1 on scratch
    """
)
