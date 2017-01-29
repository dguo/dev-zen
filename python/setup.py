from setuptools import setup, find_packages

setup(
    name='dev_zen',
    version='0.1.0',
    description='Run dev scripts',
    url='https://github.com/dguo/dev-zen',
    author='Danny Guo',
    author_email='dannyguo91@gmail.com',
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Topic :: Software Development',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    keywords='docker development environment CLI',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[],
    entry_points={
        'console_scripts': [
            'dev=dev_zen.dev:main'
        ]
    }
)
