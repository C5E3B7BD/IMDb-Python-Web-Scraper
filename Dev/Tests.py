class Tests:
    y = lambda x: x+1
    def null(*args): pass
    def xyz(bar):
        for foo in bar:
            yield foo
    def abc(foo, fooL=[]):
        xL = fooL
        x = foo
        if foo < 100:
            x = Tests.abc(Tests.y(foo), fooL)
        fooL.append(x)
        return fooL
    def _passedTest_(*args): pass
    def _helpersTest_():
        from Workers import Helpers
        for _ in [1]:
            s = []
            t = []
            for i in range(1,100):
                s.append(i)
                t.append(i)
                for j in range (1,i):
                    s.append(j)
            x = Helpers.makeUnique(s)
        return Tests._passedTest_(x == t) == None
