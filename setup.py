from setuptools import find_packages, setup

def get_requirements():
        with open('requirements.txt') as file_obj:
                req = file_obj.read()
        requirements = req.split('\n')
        return requirements

setup(
        name='customer-churn-prediction',
        version='0.1',
        packages=find_packages(),
        install_requires=get_requirements(),
        author='Yash Saxena',
        author_email='syash11@gmail.com',
        long_description=open('README.md').read(),
        long_description_content_type='text/markdown',
        url='https://github.com/starryziggy/customer-churn-prediction'
)