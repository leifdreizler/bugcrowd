from setuptools import setup

setup(
    name='bugcrowd',
    packages=['bugcrowd'],
    version='0.1',
    description='Python wrapper for the Bugcrowd API',
    url='https://github.com/leifdreizler/bugcrowd',
    author='Leif Dreizler',
    author_email='leifdreizler@gmail.com',
    license='MIT',
    install_requires=[
        'requests',
        'pytest',
        'pprint'
    ],
    download_url = 'https://github.com/leifdreizler/bugcrowd/archive/0.1.tar.gz',
    keywords = ['bugcrowd'],
    zip_safe=False
)
