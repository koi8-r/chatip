from setuptools import setup


setup(
    name='chatip',
    version='0.0.1',
    url='https://github.com/koi8-r/chatip',
    description="DevOp | Print user sessions meta (IP address) using Openfire REST API | glob support (admin*r)",
    package_dir={'': 'src'},
    packages=['chatip'],
    include_package_data=True,
    install_requires=[
        'requests'
    ],
    author='koi8-r',
    author_email='koi8-r@oz.net.ru',
    license='MIT',
    zip_safe=False,
    scripts=[],
    classifiers=[
        'Environment :: Console',
        'Programming Language :: Python :: 3.6'
    ]
)
