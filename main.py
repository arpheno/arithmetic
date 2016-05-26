from compiler import scan, parse, visit, compile
from environment import execute_program

if __name__ == "__main__":
    while True:
        equation = input("Type your equation, or type 'end' to stop the program")
        if equation == "end":
            break
        program = compile(visit(parse(scan(equation))))
        result = execute_program(program)
        print('The result is ', result)
