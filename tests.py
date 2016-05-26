from compiler import scan, parse, visit, compile
from environment import execute_program


def test_scan():
    result = " ".join([str(token) for token in scan('1+  2*3 +42')])
    assert result == '[1] [+] [2] [*] [3] [+] [42]'


def test_parse():
    result = parse(scan('1 + 2 * 3'))
    assert str(result) == """[+]
  [1]
  [*]
    [2]
    [3]"""


def test_visit():
    assert str((visit(parse(scan('1 + 2 * 3'))))) == '[[1], [2], [3], [*], [+]]'




def test_compile():
    result = compile(visit(parse(scan('1 + 2 * 3'))))
    assert result == ["put 1", "put 2", "put 3", "mul", "add", "end"]

def test_execute_program():
    assert execute_program(["put 1", "put 2", "put 3", "mul", "add", "end"]) == 7
def test_correctness():
    assert execute_program(compile(visit(parse(scan("5 + 3"))))) == 8
    assert execute_program(compile(visit(parse(scan("5 + 3*9 + 1"))))) == 33
    assert execute_program(compile(visit(parse(scan("5 * 3"))))) == 15
    assert execute_program(compile(visit(parse(scan("5 - 3"))))) == 2
    assert execute_program(compile(visit(parse(scan("10 / 5"))))) == 2
    assert execute_program(compile(visit(parse(scan("10 / 5 + 3"))))) == 5
    assert execute_program(compile(visit(parse(scan("2* 10 / 5 + 3"))))) == 7

if __name__ == "__main__":
    test_scan()
    test_parse()
    test_visit()
    test_execute_program()
    test_compile()
    test_correctness()