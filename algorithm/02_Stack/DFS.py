def func1():
    func2()
    print("1번째 함수 발동!")

def func2():
    func3()
    print("2번째 함수 발동!")

def func3():
    print("3번째 함수 발동!")

func1()