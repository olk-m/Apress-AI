from ortools.linear_solver import pywraplp

from my_or_tools_c import bounds_on_box


def main():
    a,b = [2,3],5
    s = pywraplp.Solver("Test Box",pywraplp.Solver.GLOP_LINEAR_PROGRAMMING)
    x = [s.NumVar(-1,6,""),s.NumVar(-3,5,"")]
    bounds = bounds_on_box(a,x,b)
    print(bounds==[-16,22])
main()
