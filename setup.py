from setuptools import setup, find_packages

import versioneer

setup(
    name="ROQ",
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    packages=find_packages(),
    python_requires='>=3.6.*',
    install_requires=[
        'numpy'
    ]
)
