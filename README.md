pass backend for python keyring lib
===================================

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

