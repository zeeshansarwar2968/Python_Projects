"""
> 8. In a communication system each data packet consists of 1000 bits. Due to the noise,
> each bit may be received in error with probability 0.1. It is assumed bit errors occur
> independently. Find the probability that there are more than 120 errors in a certain data packet.
"""
# Solution by Zeeshan Sarwar


# z-score = (Xi - (μ*n))/(σ*(n**0.5))   ------- by Central Limit theorem, this is approximately standard normal for sample space of 50
def z_score(value, mean_value, deviation_value, N):
    """
    Returns the z-value of the given input
    :param value: a random variable input value from a normal distribution
    :param mean_value: mean value of a normal distribution
    :param deviation_value: standard deviation of X
    :param N: sample size
    :return: Calculate and return the z-score value
    """
    return (value-(mean_value*N))/(deviation_value*(N**0.5))


# Provided Values
p = 0.1
EXi = p
μ = 0.1
N = 1000
try:
    variance_Xi = p*(1-p)
    std_deviation_Xi = variance_Xi**0.5
    z_score_value = z_score(120, p, std_deviation_Xi, N)
    print(f"z_score_value : {z_score_value}")
    print(f"P(X>120) : {1-0.9854}")
except Exception as e:
    print(f"Error: {e}")