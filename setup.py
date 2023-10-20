from setuptools import setup, find_namespace_packages

setup(
    name='clean_folder',
    version='0.0.1',
    description='A script for sorting files in a specified directory',
    url='https://github.com/VBit7/clean_folder.git',
    author='Vitalii B.',
    author_email='vbit2000@gmail.com',
    license='MIT',
    packages=find_namespace_packages(),
    entry_points={'console_scripts': ['clean-folder = clean_folder_vbit7.main:main']}
)