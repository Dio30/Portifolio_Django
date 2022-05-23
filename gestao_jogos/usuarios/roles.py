from zoneinfo import available_timezones
from rolepermissions.roles import AbstractUserRole

class Admin(AbstractUserRole):
    available_permissions = {'admin': True}

class Usuario(AbstractUserRole):
    available_permissions = {'admin': False}