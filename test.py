"""testing application"""

from signpy import *

if __name__ == "__main__":
    connection = 0

    # check the standard connection mechanism
    def rise_connection(connection: int):
        connection += 1
        print(f"connection = {connection}")

    def reset_connection(connection: int):
        connection = 0
        print(f"connection = {connection}")

    signal = Signal()
    signal.connect(rise_connection)
    signal2 = Signal(reset_connection)
    print(signal.emit(connection))
    print(signal2.emit(connection))

    # check the connect decorator
    signal3 = Signal()

    @connect(signal3)
    def connected_fun():
        print("inside connected_fun")

    print(signal3.emit())

    # check the emit decorator

    @emit(signal3)
    def emitting_fun(num: int = 2):
        print(f"num={num}")

    print(emitting_fun())
