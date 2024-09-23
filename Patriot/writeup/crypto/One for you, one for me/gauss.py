def gauss(batch_size):
    import sympy

    b = 74 * 4  
    half_b = b // 2
    m = [[0] * (b + 1) for _ in range(b + 10)] 

    with open("outshort.txt", "r") as f:
        for _ in range(batch_size):
            next(f)
        for i, line in enumerate(f):
            bits = int(line.strip(), 16)  
            cnt = half_b  
            for j in range(b):
                if bits >> j & 1:
                    cnt -= 1
                    m[i][j] = -1  
                else:
                    m[i][j] = 1 
            m[i][-1] = cnt
            if i >= batch_size - 1:
                break

    M = sympy.Matrix(m)
    M_rref, _ = M.rref()

    s = []
    for i in range(b):
        s.append(str(int(M_rref[i, -1]))) 

    binary_string = "".join(s)[::-1] 
    flag = "".join([chr(int(binary_string[i:i + 8], 2)) for i in range(0, len(binary_string), 8)])
    print(f"Recovered FLAG:", flag)

gauss(batch_size=296) 
