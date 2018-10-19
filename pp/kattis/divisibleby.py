import sys

def divisible_by_p_q(m, n, p, q):
    # Use the variable rv to accumulate the sum of the values that are
    # divisible by both p and q.
    rv = 0

    # YOUR LOOP GOES HERE

    return rv


if __name__ == "__main__":
    # parse the input
    (m, n, p, q) = [int(item.strip()) for item  in sys.stdin.read().split()]

    rv = divisible_by_p_q(m, n, p, q)

    print(rv)
