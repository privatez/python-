from setuptools import find_packages, setup

install_requires = ['pytest']

setup(name='python-learn',
      version='0.0.1',
      description='Python learn',
      platforms=['POSIX'],
      packages=find_packages(),
      include_package_data=False,
      install_requires=install_requires,
      zip_safe=False)
