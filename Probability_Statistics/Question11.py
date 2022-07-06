"""
> 11. A radar unit is used to measure speeds of cars on a motorway. The speeds are
> normally distributed with a mean of 90 km/hr and a standard deviation of 10 km/hr. Write a
> program to find the probability that a car picked at random is traveling at more than 100 km/hr?
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


# mean of 90 km/hr
mean = 90
# standard deviation of 10 km/hr
standard_deviation = 10

try:
    print("--------------------------------------------\n")
    print("The probability that a car picked at random is traveling at more than 100 km/hr : ")
    z_score_value = z_score(100, mean, standard_deviation)
    print(f"z-score value for speed of 100km/hr : {z_score_value}")
    print(f"P(X>100) of z-score {z_score_value} : {round((1-0.8413),4)}")
    print("\n--------------------------------------------\n")

except Exception as e:
    print(f"Error: {e}")