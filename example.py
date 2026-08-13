def greet():
    print("Hello")
if __name__=="__main__":
    print("This is example.py")

# 1️⃣ Function definitions (ALWAYS at top)
def add(a, b):
    return a + b

def sub(a, b):
    return a - b


# 2️⃣ Execution / test code (ONLY here)
if __name__ == "__main__":
    print("Calculator started")
    print(add(10, 5))
    print(sub(10, 5))
