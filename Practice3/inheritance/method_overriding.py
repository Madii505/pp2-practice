class A:
    def speak(self): print('A')
class B(A):
    def speak(self): print('B')
B().speak()