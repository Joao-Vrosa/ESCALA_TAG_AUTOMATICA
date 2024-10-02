from setuptools import setup, find_packages


setup(
    name='mybaynexx',
    description='Framework criado para contemplar as principais funcionalidades utilizadas'
                'na criação dos robôs.',
    packages=find_packages(),
    package_data={'': ['*.html']},
    version='1.7.2',
    download_url='https://git.nexxera.com/impdev/mybaynexx',
    install_requires=['selenium==4.11.2']
)
