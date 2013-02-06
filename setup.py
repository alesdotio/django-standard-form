from setuptools import setup, find_packages
import os
import standard_form

CLASSIFIERS = [
    "Development Status :: 3 - Alpha",
    "Framework :: Django",
    "Intended Audience :: Developers",
    "License :: OSI Approved :: BSD License",
    "Operating System :: OS Independent",
    "Programming Language :: Python :: 2.6",
    "Programming Language :: Python :: 2.7",
    "Topic :: Software Development",
    "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
]

setup(
    author="Ales Kocjancic",
    author_email="alesdotio@gmail.com",
    name='django-standard-form',
    version=standard_form.__version__,
    description='Quick and simple django templatetags for displaying forms.',
    long_description=open(os.path.join(os.path.dirname(__file__), 'README.rst')).read(),
    url='https://github.com/alesdotio/django-standard-form',
    packages=find_packages(),
    include_package_data = True,
    zip_safe = False,
    license='BSD License',
    platforms=['OS Independent'],
    classifiers=CLASSIFIERS,
    install_requires=[
        'Django>=1.3',
        'django-classy-tags>=0.3.3',
    ],
)

