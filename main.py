class employee:
    def __init__(self):
        print("Function created")
    def __del__(self):
        print("Deleted.....")

def x():
    y = employee()
    return y

y = x()
