"""
pass.py

A keyring class to store and get passwords from pass
password-store http://zx2c4.com/projects/password-store/
"""
from keyring.backend import KeyringBackend
from subprocess import Popen, PIPE


class Keyring(KeyringBackend):
    """Pass Keyring"""

    def supported(self): 
        return 0

    def get_password(self, service, username):
        proc = Popen(['pass', 'show', '/'.join([service,username])],
            stdin=None, stdout=PIPE, stderr=PIPE)
        password, _ = proc.communicate()
        proc.wait()
        if(proc.returncode == 0):
            return password.rstrip('\n')
        else:
            return None

    def set_password(self, service, username, password):
        proc = Popen(['pass', 'insert', '--echo', '--force', '/'.join([service,username])],
            stdin=PIPE, stdout=PIPE)
        proc.communicate(password.encode('utf-8'));
        proc.wait()

    def delete_password(self, service, username):
        proc = Popen(['pass', 'rm', '--force', '/'.join([service,username])])
        proc.wait() 
        if(proc.returncode != 0):
            raise PasswordDeleteError("Password not found")
