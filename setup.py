from setuptools import setup


setup(
    name='tangled.contrib',
    version='0.1a4.dev0',
    description='Tangled namespace for contributed packages',
    long_description=open('README.rst').read(),
    url='http://tangledframework.org/',
    download_url='https://github.com/TangledWeb/tangled.contrib/tags',
    author='Wyatt Baldwin',
    author_email='self@wyattbaldwin.com',
    packages=[
        'tangled',
        'tangled.contrib',
        'tangled.contrib.scaffolds',
        'tangled.contrib.tests',
    ],
    include_package_data=True,
    install_requires=[
        'tangled>=0.1a8',
    ],
    extras_require={
        'dev': [
            'tangled[dev]>=0.1a8',
        ],
    },
    entry_points="""
    [tangled.scaffolds]
    contrib = tangled.contrib.scaffolds:default
    contrib-core = tangled.contrib.scaffolds:core

    """,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],
)
