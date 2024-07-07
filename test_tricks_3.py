from ortools.linear_solver import pywraplp

from my_or_tools import SolVal
from my_or_tools_c import maximax


def main():
    s = pywraplp.Solver("", pywraplp.Solver.CBC_MIXED_INTEGER_PROGRAMMING)
    a = [[2], [-2]]
    b = [3, -12]
    x = s.NumVar(2, 5, "x")
    z, l = maximax(s, a, [x], b)
    s.Solve()
    print("x = ", SolVal(x))
    print("z = ", SolVal(z))
    print("delta = ", SolVal(l))


main()
