#
# 简单解释器实现过程
# ---------------
#
# 模拟堆栈机器的虚拟机，将python代码转换为字节码
#   * 使用数组实现堆栈
#
#   * LOAD_VALUE      加载数值
#   * ADD_TWO_VALUES  加法计算
#   * PRINT_ANSWER    打印结果
#   * STORE_NAME      设置变量
#   * LOAD_NAME       读取变量


class Instructions(object):

    def __init__(self, instructions):
        self.instructions = instructions  # 保存要运行的指令
        self.environment = dict()  # 保存环境变量
        self.stack = []  # 即将使用的数据

    def LOAD_VALUE(self, value):
        """压入堆栈的命令"""
        self.stack.append(value)

    def STORE_NAME(self, name):
        """保存变量，映射"""
        val = self.stack.pop()
        self.environment[name] = val

    def LOAD_NAME(self, name):
        """读取变量"""
        val = self.environment[name]
        self.stack.append(val)

    def ADD_TWO_VALUES(self):
        first_num = self.stack.pop()    # 弹出最后一个元素
        second_num = self.stack.pop()   # 弹出最后一个元素
        total = first_num + second_num  # 将元素添加
        self.stack.append(total)        # 添加元素进堆栈

    def PRINT_ANSWER(self):
        answer = self.stack.pop()
        print(answer)

    def parse_argument(
        self, instruction:str, argv:any, exection:any
    )->any:
        """变量解析方法"""

        # 这里对应无变量映射
        numbers = ["LOAD_VALUE"]
        # 这里对应着变量的映射功能
        names = ["LOAD_NAME", "STORE_NAME"] 
      
        argument = None
        if instruction in numbers:
            # 判断 是否为数组
            if isinstance(exection, list):
                argument = exection[argv]
            else:
                argument = exection["value"][argv]
        elif instruction in names:
            argument = exection['key'][argv]
               

        return argument

    def run_code(self, info:dict)->None:
        """numbers 要运算的数组"""

        # instructions = self.instructions  # 预设的指令集合
        for each_step in self.instructions:
            # 获取命令集合
            instruction, argument = each_step
            # 处理参数
            argument = self.parse_argument(instruction, argument, info)

            if instruction == "LOAD_VALUE":
                self.LOAD_VALUE(argument)

            elif instruction == "ADD_TWO_VALUES":
                self.ADD_TWO_VALUES()

            elif instruction == "PRINT_ANSWER":
                self.PRINT_ANSWER()

            elif instruction == "STORE_NAME":
                self.STORE_NAME(argument)

            elif instruction == "LOAD_NAME":
                self.LOAD_NAME(argument)


if __name__ == "__main__":
    # 变量映射
    # instructions = [       # 指令集合
    #     ("LOAD_VALUE", 0), # 压入一个数据
    #     ("STORE_NAME", 0), # 弹出数据，将数据压入另一个变量中--映射
    #     ("LOAD_VALUE", 1),
    #     ("STORE_NAME", 1),
    #     ("LOAD_NAME", 0),  # 根据关系对应取回，变量1
    #     ("LOAD_NAME", 1),  # 根据关系对应取回，变量2
    #     ("ADD_TWO_VALUES", None),
    #     ("PRINT_ANSWER", None)
    # ]
    # info = {  # 模拟a=1, b=4过程
    #     "key":["a", "b"],
    #     "value":[1, 4]
    # }

    #===================================
    # 无变量映射
    instructions = [       # 命令集合
        ("LOAD_VALUE", 0),        # 压入一个数据
        ("LOAD_VALUE", 1),        # 压入一个数据
        ("ADD_TWO_VALUES", None), # 计算
        ("PRINT_ANSWER", None)    # 打印
    ]
    info = [2,3]


    instr = Instructions(instructions) # 加载指令
    instr.run_code(info)    # 添加运行数据
