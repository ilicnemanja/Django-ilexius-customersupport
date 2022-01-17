from django.db import models
import hashlib, binascii, os

class User(models.Model):
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=32, unique=True)
    password = models.CharField(max_length=255)
    
    
    def __str__(self):
        return f"{self.first_name} {self.last_name} [{self.email}]"
    
    def to_dict(self):
        return {
            "id": self.id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "email": self.email,
        }
    
    def create_hashed_password(self, password):
        salt = hashlib.sha256(os.urandom(60)).hexdigest().encode('ascii')
        pwdhash = hashlib.pbkdf2_hmac('sha512', password.encode('utf-8'), 
                                salt, 100000)
        pwdhash = binascii.hexlify(pwdhash)
        self.password = (salt + pwdhash).decode('ascii')
    
    def verify_password(self, password):
        salt = self.password[:64]
        stored_password = self.password[64:]
        pwdhash = hashlib.pbkdf2_hmac('sha512', 
                                  password.encode('utf-8'), 
                                  salt.encode('ascii'), 
                                  100000)
        pwdhash = binascii.hexlify(pwdhash).decode('ascii')
        return pwdhash == stored_password 