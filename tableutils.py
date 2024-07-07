import copy


def flatten(l):
    return [e for s in l for e in s]


def set2string(S):
    s = "{ "
    if S is not None:
        for i in range(len(S)):
            s = s + str(S[i])
            s = s + "; " if i < len(S) - 1 else s + " "
    return s + "}"


def wrapmat(M, left, header):
    T = copy.deepcopy(M)
    _m, _n = len(T), len(T[0])
    for i in range(len(left)):
        T[i].insert(0, left[i])
    if header is not None:
        if len(header) < len(T[0]):
            T.insert(0, ["", *header])
        else:
            T.insert(0, header)
    return T


def formatmat(M, zeroes=False, decimals=4):
    T = copy.deepcopy(M)
    for i in range(len(M)):
        for j in range(len(M[i])):
            el = T[i][j]
            if type(el) == int:
                el = f"{el:4d}" if el or zeroes else ""
                T[i][j] = el
            elif type(el) == float:
                if el or zeroes:
                    if decimals == 4:
                        el = f"{el:.4f}"
                    elif decimals == 3:
                        el = f"{el:.3f}"
                    elif decimals == 2:
                        el = f"${el:.2f}"
                    elif decimals == 1:
                        el = f"{el:.1f}"
                    elif decimals == 0:
                        el = f"{el:.0f}"
                else:
                    el = ""
                T[i][j] = el
            elif el is None:
                el = ""
                T[i][j] = el
    return T


def printmat(M, zeroes=False, decimals=4):
    T = formatmat(M, zeroes, decimals)
    for row in T:
        l = ""
        for i in range(len(row)):
            l = l + str(row[i])
            if i < len(row) - 1:
                l = l + ","
        print(l)


def splitwrapmat(M, left, header):
    T = wrapmat(M, left, None)
    if len(T) % 2:
        T.append([])
    T2 = [T[i] + T[i + 1] for i in range(0, len(T), 2)]
    return wrapmat(T2, [], header + header)
