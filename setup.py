from setuptools import setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(name='sqwalk',
      version='0.5.3',
      description='A simple quantum walk simulator in python',
      long_description=long_description,
      long_description_content_type="text/markdown",
      keywords='quantum walker stochastic decomposition',
      url='https://github.com/Buffoni/SQWalk',
      author='Lorenzo Buffoni',
      license='Apache License 2.0',
      packages=['sqwalk'],
      install_requires=[
          'qutip',
          'numpy',
          'matplotlib',
          'qiskit'
      ],
      include_package_data=True,
      zip_safe=False)
