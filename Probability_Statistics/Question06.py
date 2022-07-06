"""
> 6. Given the following statistics, write a program to find the probability that a woman has cancer if she has a positive mammogram result?
> a. One percent of women over 50 have breast cancer.
> b. Ninety percent of women who have breast cancer test positive on mammograms.
> c. Eight percent of women will have false positives.
"""
# Solution by Zeeshan Sarwar

try:
    # GIVEN DATA
    having_cancer_prob = 1/100
    having_cancer_test_positive = 90/100
    having_cancer_test_negative = 10/100    # false negative
    not_having_cancer_prob = 1 - having_cancer_prob
    not_having_cancer_test_positive = 8/100     # false positive
    not_having_cancer_test_negative = 92/100     # false positive


    # the probability that a woman has cancer if she has a positive mammogram result
    # P(cancer | positive_result) = (P(cancer)/P(positive_result)) * P(positive_result | cancer)
    prob_positive_results = (having_cancer_prob*having_cancer_test_positive) + (not_having_cancer_prob*not_having_cancer_test_positive)
    prob_positive_results_given_cancer = having_cancer_prob * having_cancer_test_positive
    print(f"The probability that a woman has cancer if she has a positive mammogram result is : ")
    print(f"P(cancer | positive_result) : {round((having_cancer_prob/prob_positive_results)*prob_positive_results_given_cancer, 4)}")
except Exception as e:
    print(f"Error: {e}")