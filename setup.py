from setuptools import setup

setup(
    name='cbw-api-toolbox',
    description='CyberWatch Api Tools.',
    long_description=open('README.md').read().strip(),
    version='0.0.1',
    author='CyberWatch SAS',
    author_email='support-it+api@cyberwatch.fr',
    license='MIT',
    url='https://github.com/Cyberwatch/cyberwatch_api_toolbox',
    py_modules=['cbw-api-toolbox'],
    zip_safe=False,
    packages=['cbw_api_toolbox', 'cbw_api_toolbox.cbw_objects'],
    package_dir={'cbw_api_toolbox': 'cbw_api_toolbox', 'cbw_objects': 'cbw_api_toolbox/cbw_objects'},
    install_requires=[
        "requests>=2.20.1"
    ]
)
