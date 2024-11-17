"""Setup file to install library."""
from setuptools import setup, find_packages

setup(
    name='pybayes',
    version='0.0.0',
    packages=find_packages(),
    author='Clément Jacquet - clement.jacquet@laposte.net',
    install_requires=[
        'numpy',
        'pandas',
        'xarray',
        # 'scikit-learn',
        'matplotlib',
        'seaborn',
        'statsmodels',
        'pymc',
        # 'hvplot',
        'pydantic',
        'pytest',
        'pyyaml',
        'flake8',
        'ipykernel',
        'openpyxl',
    ]
)
