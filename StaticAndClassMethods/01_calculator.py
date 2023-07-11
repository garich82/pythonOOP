class Calculator:
    @staticmethod
    def add(*args):
        return sum(args)

    @staticmethod
    def multiply(*args):
        result = 1
        for num in args:
            result *= num
        return result

    @staticmethod
    def divide(*args):
        if len(args) == 0:
            raise ValueError("No arguments provided.")
        result = args[0]
        for num in args[1:]:
            result /= num
        return result

    @staticmethod
    def subtract(*args):
        if len(args) == 0:
            raise ValueError("No arguments provided.")
        result = args[0]
        for num in args[1:]:
            result -= num
        return result
