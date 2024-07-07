from piecewise import (
    gen_data,
    minimize_piecewise_linear_convex,
    verbose_minimize_non_linear,
)
from piecewise_ncvx import minimize_piecewise_linear


def my_function(x):
    from math import exp, sin

    return sin(x) * exp(x)


def main():
    import random
    import sys

    import tableutils

    n = 6
    if len(sys.argv) <= 1:
        print("Usage is main [data|run|non|ncvx] [seed] [bound] [False]")
        return
    elif len(sys.argv) >= 3:
        random.seed(int(sys.argv[2]))
    (C, B) = gen_data(n, sys.argv[4] == "True")
    if len(sys.argv) >= 4:
        B = int(sys.argv[3])
    if sys.argv[1] == "data":
        C.insert(0, ["(From", "To]", "Unit cost", "(Total cost", "Total cost]"])
        tableutils.printmat(C, True)
    elif sys.argv[1] == "run":
        Data = [(C[i][0], C[i][3]) for i in range(n)]
        Data.append((C[n - 1][1], C[n - 1][4]))
        G = minimize_piecewise_linear_convex(Data, B)
        G = [list(range(n + 1)), G]
        G[0].append("Solution")
        G[1].append(r"\sum \delta=" + str(sum(G[1][i] for i in range(n + 1))))
        G.append([Data[i][0] for i in range(n + 1)])
        G[2].append("x=" + str(sum(G[1][i] * G[2][i] for i in range(n + 1))))
        G.append([Data[i][1] for i in range(n + 1)])
        G[3].append(
            "Cost=" + str(f"{sum(G[1][i] * G[3][i] for i in range(n + 1)):.0f}")
        )
        G[0].insert(0, "Interval")
        G[1].insert(0, r"$\delta_i$")
        G[2].insert(0, "$x_i$")
        G[3].insert(0, "$f(x_i)$")
        tableutils.printmat(G, True)
    elif sys.argv[1] == "ncvx":
        Data = [(C[i][0], C[i][3]) for i in range(n)]
        Data.append((C[n - 1][1], C[n - 1][4]))
        rc, G, H = minimize_piecewise_linear(Data, B)
        if rc == 0:
            G = [list(range(n + 1)), G]
            G[0].append("Solution")
            G[1].append(r"\sum \lambda=" + str(sum(G[1][i] for i in range(n + 1))))
            G.append([Data[i][0] for i in range(n + 1)])
            G[2].append("x=" + str(sum(G[1][i] * G[2][i] for i in range(n + 1))))
            G.append(H)
            G[3].extend(["", r"\sum \delta=" + str(sum(G[3][i] for i in range(n - 1)))])
            G.append([Data[i][1] for i in range(n + 1)])
            G[4].append(
                "f(x)=" + str(f"{sum(G[1][i] * G[4][i] for i in range(n + 1)):.2f}")
            )
            tableutils.printmat(G, True)
        else:
            print("Infeasible", rc, G, H)
    elif sys.argv[1] == "non":
        G = verbose_minimize_non_linear(my_function, 2, 8, 0.05)
        m = len(G)
        G.insert(0, ["Interval", *list(range(len(G[0])))])
        G[0].append("$x^*$")
        G[0].append("$f(x^*)$")
        for i in range(1, m, 3):
            G[i].insert(0, "$x_i$")
            G[i + 1].insert(0, "$f(x_i)$")
            G[i + 2].insert(0, r"$\delta_i$")
        tableutils.printmat(G, True, 1)


main()
