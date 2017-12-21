import os
import sys
import timeit
import textwrap

range_size = 1000
count = 1000

'''
This show_results was taken from somewhere likely the monthly python site.
'''

def show_results(result):
    "Print microseconds per pass and per item."
    global count, range_size
    per_pass = 1000000 * (result / count)
    s = '{:6.2f} usec/pass'.format(per_pass)
    per_item = per_pass / range_size
    s += '{:6.2f} usec/item'.format(per_item)
    return s

def print_save(s, fd):
    fd.write("%s\n" % s)
    print(s)

def main():
    _setup_dict = ';'.join([
                            "l = [(str(x), x) for x in range(1000)]",
                            "d = {}",
                        ])
    _setup_list = ';'.join(["x = ['a', 'b', 'c', 'd', 'e']",
                            "z = ['f', 'g', 'h']"
                            "y = []"])

    _setup_cls = ';'.join([
"""
class Test(object):
    def __init__(self):
        self.foo = None
        print('test')

    def bar(self, baz):
        self.foo = baz""",
                            "f = Test()"])

    perfs = {'DICT: Set Dict Item Normally': (
                            """
                            for s, i in l:
                                d[s] = i
                            """,
                            _setup_dict
                        ),
            'DICT: Set Dict Item using setdefault': (
                        """
                        for s, i in l:
                            d.setdefault(s, i)
                        """,
                        _setup_dict
                        ),
            'DICT: Set only if key doesnt exist. Use KeyError exception to determine existence': (
                        """
                        for s, i in l:
                            try:
                                existing = d[s]
                            except KeyError:
                                d[s] = i
                        """,
                        _setup_dict
                        ),
            'DICT: Set only if key doesnt exist. Use in to determine existence': (
                        """
                        for s, i in l:
                            if s not in d:
                                d[s] = i
                        """,
                        _setup_dict
                        ),
            'DICT: Set only if key doesnt exist. Use get() to determine existence': (
                        """
                        for s, i in l:
                            if d.get(s) is None:
                                d[s] = i
                        """,
                        _setup_dict
                        ),
            'OBJ: Set attr by calling getattr on method to set variable.': (
                                """
                                class Test(object):
                                    def __init__(self):
                                        self.foo = None

                                    def bar(self, baz):
                                        self.foo = baz
                                f = Test()
                                for i in range(1000):
                                    getattr(f, 'bar')("bar")
                                """,
                                _setup_cls
                            ),
            'OBJ: Set attr by calling method to set variable.': (
                                """
                                class Test(object):
                                    def __init__(self):
                                        self.foo = None

                                    def bar(self, baz):
                                        self.foo = baz
                                f = Test()
                                for i in range(1000):
                                    f.bar("baz")
                                """,
                                _setup_cls
                            ),
            'OBJ CLEAR: x.x = None': (
                                """
                                class Test1(object):
                                    def __init__(self, x):
                                        self.x = x

                                    def clear(self):
                                        self.x = None

                                class Test(object):
                                    def __init__(self):
                                        self.foo = [Test1(x) for x in range(1000)]

                                    def bar(self):
                                        for x in self.foo:
                                            x.x = None

                                f = Test()
                                f.bar()
                                """,
                                _setup_cls
                            ),
            'OBJ CLEAR: setattr(x,x,None)': (
                                """
                                class Test1(object):
                                    def __init__(self, x):
                                        self.x = x

                                    def clear(self):
                                        self.x = None

                                class Test(object):
                                    def __init__(self):
                                        self.foo = [Test1(x) for x in range(1000)]

                                    def bar(self):
                                        [setattr(x, 'x', None) for x in self.foo]
                                f = Test()
                                f.bar()
                                """,
                                _setup_cls
                            ),

             'OBJ CLEAR: x.clear()': (
                                """
                                class Test1(object):
                                    def __init__(self, x):
                                        self.x = x

                                    def clear(self):
                                        self.x = None

                                class Test(object):
                                    def __init__(self):
                                        self.foo = [Test1(x) for x in range(1000)]

                                    def bar(self):
                                        for x in self.foo:
                                            x.clear()

                                f = Test()
                                f.bar()
                                """,
                                _setup_cls
                            ),
             'OBJ CLEAR: [x.clear()]': (
                                """
                                class Test1(object):
                                    def __init__(self, x):
                                        self.x = x

                                    def clear(self):
                                        self.x = None

                                class Test(object):
                                    def __init__(self):
                                        self.foo = [Test1(x) for x in range(1000)]

                                    def bar(self):
                                        [x.clear() for x in self.foo]

                                f = Test()
                                f.bar()
                                """,
                                _setup_cls
                            )

}

    fd = open("README.md", "w")
    for name, (code, setup_stmt) in sorted(perfs.items()):
        s = name + ' '
        t = timeit.Timer(
            textwrap.dedent(code),
            setup_stmt,
        )

        s += show_results(t.timeit(number=count))
        print_save(s, fd)
    print('\n')
    s = "{} items".format(range_size)
    print_save(s, fd)
    s = "{} iterations".format(count)
    print_save(s, fd)
    print()

if __name__ == '__main__':
    sys.exit(main())
