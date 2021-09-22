from setuptools import setup, find_packages
import os


VERSION = '0.0.3'
DESCRIPTION = "Gets today's nepali date"
LONG_DESCRIPTION = "A package that allows to get today's nepali date."

# Setting up
setup(
    name="nepdate",
    version=VERSION,
   entry_points ={
            'console_scripts': [
                'nepalidate = src.date:main'
            ]
        },
    author="Samir Maharjan  ",
    author_email="Samir84753@gmail.com",
    description=DESCRIPTION,
    packages=find_packages(),
    install_requires=['beautifulsoup4==4.10.0','bs4==0.0.1','certifi==2021.5.30','charset-normalizer==2.0.6','idna==3.2','requests==2.26.0','soupsieve==2.2.1','urllib3==1.26.6'],
    keywords=['nepalidate', 'date'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)