pass backend for python keyring lib
===================================

A pass-powered backend for Python Keyring Lib
https://bitbucket.org/kang/python-keyring-lib
http://www.zx2c4.com/projects/password-store/

Installation
------------
- put this directory somewhere
- edit your *python_keyring/keyringrc.cfg* config (get path by executing `python -c "import keyring.util.platform_; print(keyring.util.platform_.config_root())"`)
- paste/adapt following
```
[backend]
default-keyring=pass.Keyring
keyring-path=/path/to/your/pass_python_keyring
```
- Alternatively, install it with `python setup.py install`, and put the
following in your *python_keyring/keyringrc.cfg* config:
```
[backend]
default-keyring=pass.Keyring
```
