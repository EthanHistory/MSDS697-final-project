from setuptools import setup, find_packages

with open("requirements.txt", "r") as f:
    install_requires = f.read().splitlines()

setup(
    name='msds697_final_project',
    version='0.1.0',
    packages=find_packages(),
    install_requires=install_requires,
    author='Inseong Han',
    description='project',
    url='https://github.com/EthanHistory/MSDS697-final-project',
    python_requires='==3.8.18'
)
