import memoryHandler as mh
import traceback


@mh.track
def textFunc():
    x = "hello"
    bol = True
    intType = 1
    floatType = 3.2
    sequenceList = ["lib1", "lib2"]
    # String Types
    print(type(x) == str)
    print(memoryview(x))
    # Bool Types
    print(type(bol) == bool)
    # Number Types
    print(type(intType), type(floatType))
    # Sequence Types
    print(type(sequenceList))


textFunc()
