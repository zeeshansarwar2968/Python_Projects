"""
> 10. X is a normally normally distributed variable with mean μ = 30 and standard deviation σ = 4. Write a program to find
> a. P(x < 40)
> b. P(x > 21)
> c. P(30 < x < 35)
"""
# Solution by Zeeshan Sarwar


# z-score = (X - μ)/σ
def z_score(value, mean, deviation):
    """
    Returns the z-value of the given input
    :param value: a random variable input value from a normal distribution
    :param mean: mean value of a normal distribution
    :param deviation: standard deviation of X
    :return: Calculate and return the z-score value
    """
    return (value-mean)/deviation


# Provided Values
μ = 30
σ = 4

try:
    # a. P(x < 40)
    z_score_a = z_score(40, μ, σ)

    print(f"z_score_a : {z_score_a}")
    print(f"P(x < 40) : 0.9938")    # z_score = 2.5

    # b. P(x > 21)
    z_score_b = z_score(21, μ, σ)

    print(f"z_score_a : {z_score_b}")
    print(f"P(x > 21) : {1-0.0122}")    # z_score = -2.25

    # c. P(30 < x < 35)
    z_score_c_1 = z_score(30, μ, σ)
    z_score_c_2 = z_score(35, μ, σ)
    print(f"z_score_c_1 : {z_score_c_1}")  # z_score = 0.00      0.5000
    print(f"z_score_c_2 : {z_score_c_2}")   # z_score =1.25     0.8944
    print(f"P(30 < x < 35) : {0.8944-0.5000}")

except Exception as e:
    print(f"Error: {e}")

