from setuptools import setup

setup(
    name='pycrowd',
    packages=['pycrowd'],
    version='0.1',
    description='Python wrapper for the Bugcrowd API',
    url='https://github.com/leifdreizler/pycrowd',
    author='Leif Dreizler',
    author_email='leifdreizler@gmail.com',
    license='MIT',
    packages=['pycrowd'],
    install_requires=[
        'requests',
        'pytest'
    ],
    download_url = 'https://github.com/leifdreizler/pycrowd/archive/0.1.tar.gz',
    keywords = ['bugcrowd'],
    zip_safe=False
)
