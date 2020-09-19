def rec_sum(n):
    # write the insides here!

    return n + rec_sum(n - 1) if n > 0 else 0
