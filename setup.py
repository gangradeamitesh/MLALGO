from setuptools import setup , find_packages

setup(
    name = "MLALGO",
    version="0.1.0",
    author = "Amitesh Gangrade", 
    author_email= "gangradeamitesh@gmail.com",
    description= "A simple ML Algorithms library",
    url= "https://github.com/gangradeamitesh/MLALGO",
    packages=find_packages(), 
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)