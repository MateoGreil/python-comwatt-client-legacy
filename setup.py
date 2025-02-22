from setuptools import setup, find_packages

with open("README.md", 'r') as f:
    long_description = f.read()

setup(
    name='comwatt-client-legacy',
    version='0.1.2',
    author='Matéo Greil',
    author_email='contact@greil.fr',
    description='Python Client for Comwatt API (legacy: go.energy.comwatt)',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url="https://github.com/MateoGreil/python-comwatt-client-legacy",
    packages=find_packages(),
    install_requires=[
        'requests',
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
)
