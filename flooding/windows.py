from flooding.settings import *

ENVIRONMENT = 'production'

SECRET_KEY = 'liu%(qb17(uvqc7f44i=_^e0bbv^gq11s0q5agzwrxv=c0ufd6'

try:
    from flooding.localsettings import *
except ImportError:
    pass
