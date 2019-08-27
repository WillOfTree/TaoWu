#
# Function
#
# 每次调用一个函数，其实是调用了对象的__call__方法，
# 每次调用都新建一个frame对象并开始运行它

class Function(object):
    __slots__ = [ # 允许绑定的属性
        "func_code", "func_name", "func_defaults", "func_globals",
        "func_locals", "func_dict", "func_closure",
        "__name__", "__dict__", "__doc__",
        "_vm", "_func"
    ]

    def __init__(self, name, code, globs, defaults, closure, vm):
        self._vm = vm
        self.func_code = code # 这里的code即调用的函数code_obj
        self.func_name = self.__name__ = name or code.co_name # 函数的名会存在code.co_name中

        # 函数参数的默认值，如func(a=5,b=3),则func_defaults为(5,3)
        self.func_defaults = tuple(defaults)
        self.func_globals = globs
        self.func_locals = self._vm.frame.f_locals
        self.__dict__ = {}

        # 函数闭包信息
        self.func_closure = closure
        self.__doc__ = code.co_consts[0] if code.co_consts else None

        # 一些时候需要用到python的函数，下面代码是为它准备的
        kw = {
            'argdefs': self.func_defaults,
        }
        # 为闭包创建cell对象
        if closure:
            kw['closure'] = tuple(make_call(0) for _ in closure)
        self._func = types.FunctionType(code, globs, **kw)

    def __call__(self, *args, **kwargs):
        """每当调用一次函数，会创建一个新的frame并运行"""
        # 通过inspect获得函数的参数
        callargs = inspect.getcallargs(self.func, *args, **kwargs)
        frame = self._vm.make_frame(
            self.func_code, callargs, self.func_globals, {}
        )

        return  self._vm.run_frame(frame)

def make_cell(value):
    """创建一个真实的cell对象"""
    # Thanks to Alex Gaynor for help with this bit of twistiness.
    fn = (lambda x: lambda: x)(value)
    return fn.__closure__[0]
