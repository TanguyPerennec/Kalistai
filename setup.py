from setuptools import find_packages, setup

setup(
    name=’Kalistai’,
    packages=find_packages(include=[‘mypythonlib’]),
    version=’0.0.1',
    description=’Basic function to facilitate DL’,
    author=’Kalistai group’,
    license=’MIT’,
    install_requires=[],
    setup_requires=[‘pytest-runner’],
    tests_require=[‘pytest==4.4.1’],
    test_suite=’tests’,
)