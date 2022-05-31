from fractions import Fraction

def solution(pegs):
    '''
    I found the solution pattern of the linear system by hand and
    coded the algorithm for the result.
    '''

    # find radius of the nth (last) gear
    k = len(pegs)
    sign = -1
    rn = 0
    for index, peg in enumerate(pegs):

        if index == 0:
            rn += sign*peg
        elif index == k-1:
            rn += sign*peg
        else:
            rn += sign*2*peg
        sign = -sign

    # the solution differs if there are an even or odd number of pegs
    rn = Fraction(rn,3) if (k % 2 == 0) else Fraction(rn)

    # calculate the other radii and return [-1, -1] if any radius < 1
    radius = rn
    for index in range(k-2, -1,-1):

        radius = Fraction(pegs[index+1] - pegs[index]) - radius
        if radius < 1:
            return [-1, -1]

    return [radius.numerator, radius.denominator]

# test_case = [4, 30, 50]
# test_case = [4, 17, 50]
test_case = [4, 12, 16, 20]
result = solution(test_case)
print(result)