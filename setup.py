from pathlib import Path
from setuptools import setup, find_packages


def post_install():
    """ Implement post installation routine """
    with open('./requirements.txt') as f:
        install_requires = f.read().splitlines()

    return install_requires


def pre_install():
    """ Implement pre installation routine """
    # read the contents of your README file
    global long_description
    this_directory = Path(__file__).parent
    long_description = (this_directory / "README.md").read_text()


pre_install()


setup(
    name='PlantsAI',
    version='0.0.0',
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages=["plantsai"],
    setup_requires=[
        'numpy'
    ],
    url='https://github.com/PlantsAI/plantsai',
    license='',
    author='Sajjad Aemmi',
    author_email='sajjadaemmi@gmail.com',
    description='PlantsAI',
    include_package_data=True,
    # package_data={"plantsai": ['main.ui']},
    install_requires=post_install(),
    entry_points={
        "console_scripts": ["plantsai=plantsai:__init__"],
    },
)
