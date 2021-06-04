from setuptools import setup


setup(name='sqwalk',
      version='0.1',
      description='A simple quantum walk simulator in python',
      keywords='quantum walker stochastic decomposition',
      url='https://github.com/Buffoni/SQWalk',
      author='Lorenzo Buffoni',
      author_email='lorenzo.buffoni@unifi.it',
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
