import setuptools
from setuptools import find_packages, setup

setup(
    name='gen_ai_project',  # Updated to follow Python naming conventions
    version='0.1.0',  # Typically, 0.x.x is used for early-stage development
    author='Vilas Tade',
    author_email='tadevilas@gmail.com',
    description='A brief description of the Gen AI Project',
    long_description='A longer description of the Gen AI Project, including its purpose, features, and installation instructions.',
    long_description_content_type='text/markdown',
    url='https://github.com/tadevilas/MedicalChatBot.git',  # Replace with actual URL if available
    packages=find_packages(),
    install_requires=[],  # Add dependencies if needed
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
