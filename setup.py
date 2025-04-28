from setuptools import setup

setup(
    name='removebg',
    version='1.0',
    py_modules=['removebg'],
    install_requires=[
        'rembg>=2.0',
        'pillow>=9.0',
    ],
    entry_points={
        'console_scripts': [
            'removebg=removebg:main',
        ],
    },
)