class A:
    def class_a_method(self):
        return "I\'m just a Class A Method"
    def hello(self):
        return "hello from class A"
class B:
    def class_b_method(self):
        return "I\'m just a Class B Method"
    def hello(self):
        return "hello from Class B"
class C(B,A):
    pass

instance_c=C()
# print(instance_c.class_a_method())
# print(instance_c.class_b_method())
# print(instance_c.hello())
# print(help(C))
# print(C.mro())
# print(C.__mro__)
# print("Hello")
