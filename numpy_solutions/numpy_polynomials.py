import numpy
#A polynomial with roots [-1, 1, 1, 10] is (x + 1)(x - 1)(x - 1)(x - 10)
#np.poly expands this and returns the coefficients as an array in descending order of powers.
#np.roots returns the roots of the polynomial with the given coefficients.
#np.polyint computes the indefinite integral of a polynomial whose coefficients are given without the constant of integration unless specified.
#np.polyder computes the derivative of the specified order of a polynomial. It returns the coefficients in descending order of powers.
#np.polyvar evaluates the polynomial at specific value.
#np.polyfit(x, y, deg) fits a polynomial of degree deg to the points (x[i], y[i]) using the **least-squares method`.Here, deg = 2, so it finds a quadratic polynomial (ax^2 + bx+ c)

P = numpy.array(input().split(), float)
#P = [float(x) if '.' else int(x) for x in input().split()]
x = int(input())
print(numpy.polyval(P,x))
