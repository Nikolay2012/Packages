import setuptools
#
with open('README.md') as file:
    readme_file = file.read()
print(readme_file)
# 
if __name__ == '__main__':
    # print(__name__)
    setuptools.setup(
        name="modules",
        version="0.0.0",
        author="Group 14:00",
        description="This is package was create for control tables in database sqlite3",
        long_description=readme_file,
        packages=["modules"],
        url="https://github.com/Nikolay2012/Packages",
        classifiers=[
            'Programming Language :: Python :: 3',
            'License :: OSI Approved :: WorldIT.academy',
            'Operating System :: OS Independent'
        ],
        python_requires='>=3.7'
    )