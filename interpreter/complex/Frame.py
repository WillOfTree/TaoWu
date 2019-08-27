class Frame(object):
    def __init__(self, code_obj, global_names, local_names, prev_frame):
        self.code_obj = code_obj
        self.f_globals = global_names
        self.f_locals = local_names
        self.prev_frame = prev_frame

        self.stack = [] # 数据栈
        self.block_stack = [] # block栈

        if prev_frame:
            self.builtin_names = prev_frame.builtin_names
        else:
            self.builtin_names = local_names['__builtins__']
            if hasattr(self.builtin_names, "__dict__"):
                self.builtin_names = self.builtin_names.__dict__

            self.last_instruction = 0 # 最后运行的指令 初始为0

            