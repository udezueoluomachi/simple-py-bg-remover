from setuptools import setup

setup(
    name='removebg',
    version='1.1',
    py_modules=['removebg'],
    install_requires=[
        'rembg>=2.0',
        'pillow>=9.0',
        'onnxruntime>=1.15.1',  # Explicitly add onnxruntime
    ],
    entry_points={
        'console_scripts': [
            'removebg=removebg:main',
        ],
    },
)