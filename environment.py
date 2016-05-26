"""
This file contains the runtime environment to execute a rudimentary arithmetic language
"""
import re


def add(a, b):
    # The order is switched because we're dealing with postfix notation
    return b + a


def sub(a, b):
    # The order is switched because we're dealing with postfix notation
    return b - a


def mul(a, b):
    # The order is switched because we're dealing with postfix notation
    return b * a


def div(a, b):
    # The order is switched because we're dealing with postfix notation
    return b / a


def handle_errors(instruction):
    # Make sure the instructions are correct
    if instruction[0] not in ["mul", "add", "end", "put", "div", "sub"]:
        raise ArithmeticError("Operation not supported")
    if instruction[0] is "put":
        try:
            int(instruction[1])
        except:
            raise ArithmeticError("Only integer numbers allowed")


def execute_program(instructions):
    stack = []
    for instruction in [re.split('\s', instruction) for instruction in instructions]:
        handle_errors(instruction)

        if instruction[0] == 'put':
            stack.append(int(instruction[1]))
        if instruction[0] == "add":
            stack.append(add(stack.pop(), stack.pop()))
        if instruction[0] == "sub":
            stack.append(sub(stack.pop(), stack.pop()))
        if instruction[0] == "mul":
            stack.append(mul(stack.pop(), stack.pop()))
        if instruction[0] == "div":
            stack.append(div(stack.pop(), stack.pop()))
        if instruction[0] == "end":
            assert len(stack) == 1, "Program invalid"
            return stack[0]
    raise RuntimeError("Program does not contain end statement")
