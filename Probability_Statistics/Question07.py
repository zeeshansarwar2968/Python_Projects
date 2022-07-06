"""
> 7. A bank teller serves customers standing in the queue one by one. Suppose that the
> service time Xi for customer i has mean EXi=2 (minutes) and Var(Xi)=1. We assume that
> service times for different bank customers are independent. Let Y be the total time the bank
> teller spends serving 50 customers. Write a program to find P(90<Y<110)
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


n = 50
mean = 2
variance = 1
standard_dev = variance**0.5
point_x1 = 90
point_x2 = 110

try:
    print("\n------------------------------------------\n")
    print(f"z_score_1 function : {z_score(90, mean, standard_dev, n)}")
    print(f"z_score_2 function : {z_score(110, mean, standard_dev, n)}")
    print("\n------------------------------------------\n")
    val_for_z1 = 0.0764
    val_for_z2 = 0.9236
    print(f"P(90<Y<110) : {val_for_z2-val_for_z1}")
    print("\n------------------------------------------\n")
except Exception as e:
    print(f"Error: {e}")