"""
signpy.signals module

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

#! IMPORTS


from typing import Any, Callable, Union


#! EXPORTS


__all__ = ["Signal", "connect", "emit"]


#! CLASSES


class Signal:
    """
    Generate event signals and connect them to functions.

    Parameters
    ----------
    fun: Callable | None = None
        if provided, this will be the function connected to the signal. Thus
        this function will be recalled when the signal is emitted.

    Raises
    ------
    TypeError
        In case a non-callable object is provided as "fun".
    """

    _is_connected: bool
    _connected_fun: Callable

    def __init__(self, fun: Union[Callable, None] = None):
        self._is_connected = False
        if fun is None:
            self._connected_fun = self._unconnected
        else:
            _check_type(fun, Callable)
            self._connected_fun = fun
            self._is_connected = True

    def _unconnected(self, *args, **kwargs):
        """
        private method used to assign function with no effect on the signal
        emission
        """
        return None

    def is_connected(self):
        """check whether this signal is connected to a function."""
        return self._is_connected

    @property
    def connected_function(self):
        """return the function connected to this signal."""
        if self.is_connected():
            return self._connected_fun
        return self._unconnected

    def emit(self, *args, **kwargs):
        """emit the signal with the provided parameters."""
        if self.is_connected():
            if len(self.connected_function.__annotations__) == 0:
                return self.connected_function()
            return self.connected_function(*args, **kwargs)
        return None

    def connect(self, fun: Callable):
        """
        connect a function/method to the actual signal

        Parameters
        ----------
        fun: Callable
            the function to be connected to the signal.

        Parameters
        ----------
        fun : Callable
            the function to be connected

        Raises
        ------
        TypeError: in case the provided fun agrument is not Callable.
        """
        _check_type(fun, Callable)
        self._connected_fun = fun
        self._is_connected = True

    def disconnect(self):
        """disconnect the signal from the actual function."""
        self._connected_fun = self._unconnected
        self._is_connected = False


#! FUNCTIONS


def _check_type(obj: object, typ: Any):
    """ensure the object is of the provided type/s"""
    if not isinstance(obj, typ):
        raise TypeError(f"{obj} must be an instance of {typ}.")
    return True


def connect(signal: Signal):
    """
    decorator connecting the decorated function to an exising signal.

    Parameters
    ----------
    signal : Signal
        the signal that will receive "fun" as connection.

    Raises
    ------
    TypeError
        in case the connected object is not Callable or signal is not a Signal.
    """
    _check_type(signal, Signal)

    def _inner(fun: Callable):
        _check_type(fun, Callable)
        signal.connect(fun)

    return _inner


def emit(signal: Signal):
    """
    decorator invoking the emission of the signal after its completition.

    Parameters
    ----------
    signal : Signal
        the signal that will receive "fun" as connection.

    Raises
    ------
    TypeError
        in case the connected object is not callable or signal is not a Signal.

    Note
    ----
    the signal emission, provides all the outputs of the decorated function
    as arguments for the function connected to the signal.
    Despite using this decorator can be a concise way of emitting signals,
    please use the standard signal.emit method if you require a different
    way to emit the signal with specific arguments.
    """
    _check_type(signal, Signal)

    def _inner1(fun: Callable):
        _check_type(fun, Callable)

        def _inner2(*args, **kwargs):
            return signal.emit(fun(*args, **kwargs))

        return _inner2

    return _inner1
