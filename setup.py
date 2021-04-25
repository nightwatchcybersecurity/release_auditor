from setuptools import find_packages, setup
from release_auditor.utils import ReleaseAuditorUtils

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='release_auditor',
    version=ReleaseAuditorUtils.get_version(),
    description='A tool for checking if release assets were modified after publication.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/nightwatchcybersecurity/release_auditor',
    author='Nightwatch Cybersecurity',
    author_email='research@nightwatchcybersecurity.com',
    license='Apache',
    packages=find_packages(exclude=["scripts.*", "scripts", "tests.*", "tests"]),
    include_package_data=True,
    install_requires=open('requirements.txt').read().splitlines(),
    entry_points={
        'console_scripts': [
            'release_auditor = release_auditor.cli:cli'
        ]
    },
    classifiers=[
        'Environment :: Console',
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    python_requires='>=3.6',
    project_urls={
        'Bug Reports': 'https://github.com/nightwatchcybersecurity/release_auditor/issues',
        'Source': 'https://github.com/nightwatchcybersecurity/release_auditor',
    },
)
