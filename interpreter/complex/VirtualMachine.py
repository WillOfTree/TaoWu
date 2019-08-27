#
# VirtualMachine
# --------------
#
# 每次运行一个python程序我们仅创建一个VirtualMachine对象，它维护一个调用栈，
# 异常状态和帧之间传递的返回值，运行代码入口为run_code,
# 它读入code object并创立起第一个帧，
# 之后会因为函数调用或其他原因，在该帧上创建新帧，直到最后一帧返回，代码运行结束

class VirtualMachineError(Exception):
    pass

class VirtualMachine(object):
    def __init__(self):
        self.frames = [] # 调用栈
        self.frame = None # 当前运行的帧
        self.return_value = None # frame返回时的值
        self.last_exception = None 

    def run_code(self, code, global_name=None, local_names=None):
        """运行python程序入口，程序编译后生成code_obj,这里code_obj在参数
        code中，run_code根据输入的code_obj新建一个frame并开始运行        
        """
        frame = self.make_frame(code, global_names=global_names, local_names=local_names)

        self.run_frame(frame)

    def make_frame(self, code, callargs={}, global_names=None, local_names=None):
        """操控Frame类的方法，包括调用栈内帧的压入与弹出操作，
        创建帧的操作make_frame(该方法主要工作是对帧拥有的名字空间的初始化)
        当然还要一个运行帧的方法run_frame,
        """
        if global_names is not None:
            global_names = global_names
            if local_names is None:
                local_names = global_names
        elif self.frames:
            global_names = self.frame.global_names
            local_names = {}
        else:
            global_names = local_names = {
                "__builtins__": __builtins__,
                "__name__": "__main__",
                "__doc__": None,
                "__package__": None,
            }

        # 将函数调用时的参数更新到局部变量空间中
        local_names.update(callargs)
        frame = Frame(code, global_names, local_names, self.frame)

        return frame

    # 调用栈压入frame
    def push_frame(self, frame):
        self.frames.append(frame)
        self.frame = frame

    # 调用栈弹出frame
    def pop_frame(self):
        self.frames.pop()
        if self.frames:
            self.frame = self.frame[-1]
        else:
            self.frame = None
    
    def run_frame(self, frame):
        pass

    #-------------
    # 数据栈操作
    def top(self):
        return self.frame

    def pop(self):
        return self.frame.stack.pop()

    def push(self, *vals):
        self.frame.stack.exetend(vals)

    def popn(self, n):
        """弹出多个栈"""
        if n:
            ret = self.frame.stack[-n:]
            self.frame.stack[-n:] = []
            return ret
        else:
            return []