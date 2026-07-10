import sys
import math

# -------------------------------------------------
# Xây các mẫu Grundy B_k cho từng đoạn [2^k, 2^(k+1)-1]
# -------------------------------------------------

def build_Bs(kmax: int):
    """
    Trả về dict Bs[k] = list Grundy mẫu B_k cho đoạn [2^k, 2^(k+1)-1].
    Độ dài:
        k = 1: P1 = 2
        k = 2: P2 = 4
        k >= 3: Pk = k + 2
    """
    # Build DP nhỏ để lấy B1, B2, B3 làm base
    lim = 1 << 5  # 32 là quá đủ
    g = [0] * (lim + 1)

    for s in range(1, lim + 1):
        # m = floor(log2 s) + 1 = bit_length
        m = s.bit_length()
        moves = set()
        for k in range(1, m + 1):
            if s - k >= 0:
                moves.add(g[s - k])
        # mex
        gval = 0
        while gval in moves:
            gval += 1
        g[s] = gval

    Bs = {}

    # Base: k = 1, 2, 3 lấy trực tiếp từ DP nhỏ
    up_to = min(3, kmax)
    for k in range(1, up_to + 1):
        L = 1 << k
        if k <= 2:
            P = 1 << k  # P1 = 2, P2 = 4
        else:
            P = k + 2   # từ k >= 3 trở đi
        Bs[k] = [g[L + i] for i in range(P)]

    # Quy nạp cho k >= 4
    for k in range(4, kmax + 1):
        Lk = 1 << k            # 2^k
        Lprev = 1 << (k - 1)   # 2^(k-1)

        # Độ dài chu kỳ k-1
        if (k - 1) <= 2:
            Pprev = 1 << (k - 1)
        else:
            Pprev = (k - 1) + 2

        Bprev = Bs[k - 1]

        m = k + 1      # số nước bốc tối đa ở đoạn này
        P = k + 2      # độ dài chu kỳ mới B_k

        Bk = []

        def get_g(x: int) -> int:
            """
            Lấy Grundy của trạng thái x, chỉ trong khoảng cần thiết:
            - x >= Lk: lấy từ Bk (đã build một phần)
            - x  thuộc [Lprev, Lk-1]: suy ra từ Bprev (chu kỳ)
            """
            if x >= Lk:
                idx = x - Lk
                if idx < len(Bk):
                    return Bk[idx]
                else:
                    # Không bao giờ truy cập "tương lai" nếu code đúng
                    raise ValueError("Access future Grundy")
            else:
                # x luôn thuộc đoạn [2^(k-1), 2^k - 1]
                idx = x - Lprev
                return Bprev[idx % Pprev]

        for i in range(P):
            s = Lk + i
            moves = set()
            for t in range(1, m + 1):
                x = s - t
                if x < 0:
                    break
                moves.add(get_g(x))
            gval = 0
            while gval in moves:
                gval += 1
            Bk.append(gval)

        Bs[k] = Bk

    return Bs


def grundy_single(s: int, Bs) -> int:
    """
    Grundy của 1 cột sỏi có s viên, dùng bảng Bs đã build.
    """
    if s == 0:
        return 0
    if s == 1:
        return 1  # g(1) = 1 từ DP nhỏ

    k = s.bit_length() - 1  # floor(log2 s)
    Bk = Bs[k]
    Lk = 1 << k
    Pk = len(Bk)
    idx = (s - Lk) % Pk
    return Bk[idx]


# -------------------------------------------------
# Hàm solve chính
# -------------------------------------------------

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    N = int(data[0])
    a = list(map(int, data[1:1 + N]))

    max_s = max(a)
    kmax = max_s.bit_length() - 1  # tối đa k cần build
    Bs = build_Bs(kmax)

    nim_sum = 0
    for s in a:
        print(grundy_single(s, Bs))
        nim_sum ^= grundy_single(s, Bs)

    # nim_sum != 0 => Dat thắng, ngược lại Phu
    # print("Dat" if nim_sum != 0 else "Phu")
    f = [grundy_single(i, Bs) for i in range(1, 14)]
    print(f)


if __name__ == "__main__":
    main()
