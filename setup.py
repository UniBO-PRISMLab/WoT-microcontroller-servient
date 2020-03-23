from setuptools import setup, find_packages

setup(
    name='embeddedWotServient',
    url='https://github.com/UniBO-PRISMLab/WoT-microcontroller-servient',
    author='Daniele Rossi',
    version='0.1',
    license='MIT',
    description='WoT module for build TDs and executable scripts for embedded systems',
    long_description=open('README.md').read(),
    py_modules=['embeddedWotServient'],
    install_requires=['Click','jinja2','pyyaml','jsonschema',],
    entry_points='''
        [console_scripts]
        embeddedWotServient=embeddedWotServient:cli
    '''
)