import argparse

def multinomial(params):
  if len(params) == 1:
    return 1
  return binomial(sum(params), params[-1]) * multinomial(params[:-1])

def count_bin_ones(a):
    """Counts the number of ones in the base-2 expansion of a"""
    result = 0
    while a != 0:
        if a % 2 == 1:
            result = result + 1
        a = a >> 1  
    return result

def f(a, b):
    """for binary strings a and b, computes the function f from the beginning of Section 5 of the paper"""
    if a | b == b:
        return 1 / 2^(count_bin_ones(b))
    else:
        return 0

def inv(a, n):
    """Considering a as a binary string of length n, returns bitwise negation"""
    return (2^n - 1) ^^ a

def g(a, b, n):
    """For binary strings a and b of length n, computes the function g from the beginning of Section 5 of the paper"""
    return 1 / 4 * (f(a, b) + f(inv(a, n), b) + f(a, inv(b, n)) + f(inv(a, n), inv(b, n)))

def shift(a, n):
    """Considering a as a binary string of length n, returns its cyclic shift to the left"""
    return ( (a << 1) & (2^n - 1) ) + (a >> (n - 1))

def build_matrix(n):
    """For a given n, constructs matrix G_n defined by (2) in the paper"""
    result = []
    for a in xrange(2^n):
        row = []
        for b in xrange(2^n):
            row.append(g(a, shift(b, n), n))
        result.append(row)
    return matrix(QQ, result)

def expected_number_attractors(length):
    G = build_matrix(length)
    return 1 / (G.charpoly().diff().substitute(1) * length)

#######################

if __name__=="__main__":
    parser = argparse.ArgumentParser(description = 'Computes the limit of the expected number of attractors of given length in a random Boolean network of canalizing depth 1')
    parser.add_argument('length', type = int)
    args = parser.parse_args()
    print("The expected number is " + str(expected_number_attractors(args.length)))
