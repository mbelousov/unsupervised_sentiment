import os

from setuptools import setup


with open(os.path.join(os.path.dirname(__file__), 'README.md')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='unsupervised_sentiment',
    version='0.0.1',
    install_requires=[
        'nltk',
        'numpy',
        'stemming',
    ],
    packages=['unsupervised_sentiment', 'unsupervised_sentiment.datasets'],
    package_dir={'unsupervised_sentiment': 'unsupervised_sentiment'},
    package_data={
        'unsupervised_sentiment': [
            'datasets/*.data',
            'datasets/*.ttf',
            'lexicon/*',
            'stanford-postagger/models/*',
            'stanford-postagger/*.jar',
            'stored/*',
        ]
    },

    include_package_data=True,
    license='Creative Commons Licence'
            '(Attribution-NonCommercial-NoDerivs 3.0 Unported)',
    description='Subjectivity and sentiment classification'
                'using polarity lexicons',
    long_description=README,
    author='Nikolaos Pappas, Maksim Belousov',
    author_email='nikolaos.pappas@idiap.ch, belousov.maks@gmail.com',
    classifiers=[
        'Intended Audience :: Researches',
    ],
)