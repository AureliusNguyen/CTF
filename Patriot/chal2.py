def gauss():
    import sympy

    b = 74 * 4
    half_b = b // 2

    m = [[0] * (b + 1) for _ in range(b + 10)]

    # M = sympy.Matrix([[1, 2, 3], [3, 4, 5]])
    # print(M.rref())

    with open("output.txt", "r") as f:
        for i, line in enumerate(f):
            bits = int(line, 16)

            cnt = half_b
            for j in range(b):
                if bits >> j & 1:
                    cnt -= 1
                    m[i][j] = -1
                else:
                    m[i][j] = 1
            m[i][-1] = cnt

            # +2 for safety
            if i >= b + 2:
                break

    M = sympy.Matrix(m)
    M_rref = M.rref()

    for i in range(10):
        print(str(int(M_rref[0][i, -1])))

    s = []
    for i in range(b):
        s.append(str(int(M_rref[0][i, -1])))
    print("".join(s))

    while True:
        exec(input())
gauss()

FLAG = "PCTF{y0u_b3tt3r_sti11_giv3_m3_my_fry}"
