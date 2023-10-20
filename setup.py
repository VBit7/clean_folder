from setuptools import setup, find_namespace_packages

with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name='clean_folder_vbit7',
    version='0.0.5',
    description='A script for sorting files in a specified directory',
    url='https://github.com/VBit7/clean_folder.git',
    author='Vitalii B.',
    author_email='vbit2000@gmail.com',
    long_description=long_description,
    long_description_content_type="text/markdown",    
    license='MIT',
    classifiers = [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=find_namespace_packages(),
    include_package_data=True,
    entry_points={'console_scripts': ['clean-folder = clean_folder_vbit7.main:main']}
)