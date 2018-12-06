
__all__ = ['PI','AAA']
PI = 3.14
def showPI():
    print("PI = %g"%PI)

class AAA():
    id = 100
    def __init__(self):
        self.age = 10
    @classmethod
    def testClassMethod(cls):
        print("我是类方法")

    def test1(self):
        print("我是成员方法test1")

    @staticmethod
    def testStaticMethod():
        print("我是静态方法")

if __name__ == '__main__':
    # print(__name__)
    print('id = %d' % AAA.id)
    AAA.testClassMethod()
    AAA.testStaticMethod()
    AAA().test1()
    showPI()
# print('id = %d' % AAA.id)
# AAA.testClassMethod()
# AAA.testStaticMethod()
# AAA().test1()
# showPI()