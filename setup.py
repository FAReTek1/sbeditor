from setuptools import setup
import subprocess

# Copied from https://www.youtube.com/watch?v=U-aIPTS580s
# ⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️ WARNING ⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️
# WHEN USING THIS SCRIPT TO AUTOMATICALLY GET THE VERSION
# NUMBER, IT HAS CAUSED ISSUES (I DON'T KNOW WHY). I
# RECOMMEND UPDATING THE VERSION NUMBER MANUALLY

# remote_version = subprocess.run(['git', 'describe', '--tags'], stdout=subprocess.PIPE).stdout.decode('utf-8').strip()
# assert '.' in remote_version

with open('README.md', 'r', encoding="utf-8") as readme:
    long_description = readme.read()

setup(
    name='sbeditor',
    version="v0.0.2",
    packages=['sbeditor'],
    url='https://github.com/FAReTek1/sbeditor',
    license='MIT',
    author='faretek1',
    author_email='',
    description='A parser for all things sb3',
    long_description=long_description
)
