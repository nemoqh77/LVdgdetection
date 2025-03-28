from setuptools import setup, find_packages

def readme():
    with open('README.rst') as f:
        return f.read()

setup(name = "LVdgdetection",
    version = "0.1",
    description = "Dwarf galaxy detecion for CSST image data",
    long_description = readme(),
    long_description_content_type="text/x-rst",
    author = "Han Qu",
    author_email = "",
    url = "https://github.com/nemo77/LVdgdetection",
    packages = find_packages(),
    package_data = {},
    include_package_data = True,
    classifiers=[
      'Development Status :: 3 - Alpha',
      'Intended Audience :: Science/Research',
      'Operating System :: OS Independent',
      'Programming Language :: Python',
      'Topic :: Scientific/Engineering :: Astronomy'
      ],
    zip_safe=False
)
