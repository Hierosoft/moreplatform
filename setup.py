import setuptools
import sys
import os


# versionedModule = {}
# versionedModule['urllib'] = 'urllib'
# if sys.version_info.major < 3:
#     versionedModule['urllib'] = 'urllib2'

install_requires = []

if os.path.isfile("requirements.txt"):
    with open("requirements.txt", "r") as ins:
        for rawL in ins:
            line = rawL.strip()
            if len(line) < 1:
                continue
            install_requires.append(line)

description = (
    "Manually interact with files and the os. Do more than the platform module."
)
long_description = description
if os.path.isfile("readme.md"):
    with open("readme.md", "r") as fh:
        long_description = fh.read()

setuptools.setup(
    name='pycodetool',
    version='0.9.0',
    description=description,
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        'Development Status :: 3 - Alpha',  # Development Status :: 4 - Beta
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License', # See also: license below
        'Topic :: System',
        # 'Operating System :: POSIX :: Linux',
    ],
    keywords='',
    url="https://github.com/hierosoft/moreplatform",
    author="Jake Gustafson",
    author_email='7557867+poikilos@users.noreply.github.com',
    license='MIT License',  # See also: license classifier above.
    # packages=setuptools.find_packages(),
    packages=['moreplatform'],
    include_package_data=False,  # look for MANIFEST.in; requires zip_safe=False
    # scripts=['example'] ,
    # See <https://stackoverflow.com/questions/27784271/
    # how-can-i-use-setuptools-to-generate-a-console-scripts-entry-
    # point-which-calls>
    '''
    entry_points={
        'console_scripts': [
            'checkpath=moreplatform.checkpath:main',
        ],
    },
    '''
    install_requires=install_requires,
    #     versionedModule['urllib'],
    # ^ "ERROR: Could not find a version that satisfies the requirement
    #   urllib (from nopackage) (from versions: none)
    # ERROR: No matching distribution found for urllib"
    test_suite='nose.collector',
    tests_require=['nose', 'nose-cover3'],
    zip_safe=True,  # It can't run zipped due to needing data files.
 )
