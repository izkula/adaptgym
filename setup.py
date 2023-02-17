import setuptools
import pathlib


setuptools.setup(
    name='adaptgym',
    version='0.1.1',
    description='Environments for testing agent adaptation.',
    url='http://github.com/izkula/adaptgym',
    long_description=pathlib.Path('README.md').read_text(),
    long_description_content_type='text/markdown',
    packages=['adaptgym'],
    install_requires=['numpy>=1.19.5', 'scipy>=1.7.0', 'matplotlib>=3.4.2', 'imageio', 
                      'dm-control==1.0.7', 'dm-env==1.5', 'dm-tree==0.1.7', 
                      'crafter==1.8.0', 'Pillow>=9.2.0'],
    python_requires='>=3.7',
    classifiers=[
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
    ],
)
