"""
signpy package

A convenient notification tool between python classes.

Contents
--------
Signal: class
    the core object of this package which allows to handle different source of
    signalling events

connect: decorator
    a decorator to be used to link a target function to an existing signal

emit: decorator
    a decorator which allow the emission of a signal after the execution of
    a function
"""

from .signals import *
