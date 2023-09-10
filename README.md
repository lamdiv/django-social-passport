# Django Social Passport
A Python library for seamless social authentication integration with Django.

[![PyPI - Downloads](https://img.shields.io/pypi/dm/django-social-passport)](https://pypi.org/project/django-social-passport/)
[![PyPI](https://img.shields.io/pypi/v/django-social-passport)](https://pypi.org/project/django-social-passport/)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/django-social-passport)](https://pypi.org/project/django-social-passport/)
[![](https://img.shields.io/pypi/l/django-social-passport.svg)](https://pypi.org/project/django-social-passport/)

## Installation

You can install `Django Social Passport` and its dependencies using [pip](https://pypi.org/project/django-social-passport/):

```bash
$ pip install django-social-passport
```
    

## Usage
Now, create `test.py` file. You have to import the `socialhi` function in that file. 

```python
from passport.socialplay import socialhi

first_meet = socialhi()
print(first_meet)
```

After importing, You have to call the imported function and print the output.


## Notes

**Current Version: ![PyPI - Downloads](https://img.shields.io/pypi/v/django-social-passport)** release serves as a demonstration and does not include a functional social authentication system. We plan to implement a fully working social authentication system in future versions.

## License

[MIT](https://choosealicense.com/licenses/mit/)

