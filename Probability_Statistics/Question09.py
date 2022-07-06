"""
> 9. In a particular pain clinic, 10% of patients are prescribed narcotic pain killers. Overall,
> five percent of the clinic’s patients are addicted to narcotics (including pain killers and illegal
> substances). Out of all the people prescribed pain pills, 8% are addicts. If a patient is an addict,
> write a program to find the probability that they will be prescribed pain pills?
"""
# Solution by Zeeshan Sarwar

# P(the probability that a patient will be prescribed pain pills | given the patient is an addict) = 
# (P(the probability that a patient will be prescribed pain pills)/P(the patient is an addict)) * P(a patient is an addict | given the probability that a patient will be prescribed pain pills) 

# (P(the probability that a patient will be prescribed pain pills)
prob_prescribed_pain_pill = 0.1

# P(the patient is an addict)
prob_patient_is_addict = 0.05

# P(a patient is an addict | given the probability that a patient will be prescribed pain pills) 
prob_addict_given_prescribed = 0.08

try:
    prob_prescribed_given_addiction = (prob_prescribed_pain_pill/prob_patient_is_addict) * prob_addict_given_prescribed
    print("\n----------------------------------------------------------------\n")
    print(f"P(the probability that a patient will be prescribed pain pills | given the patient is an addict) = {prob_prescribed_given_addiction}")
    print("\n----------------------------------------------------------------\n")
except Exception as e:
    print(f"Error : {e}")

