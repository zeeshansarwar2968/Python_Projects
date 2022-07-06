"""
> 5. In my town, it's rainy one third of the days. Given that it is rainy, there will be heavy traffic 
> with probability 12, and given that it is not rainy, there will be heavy traffic with probability
> 14. If it's rainy and there is heavy traffic, I arrive late for work with probability 12. On the other
> hand, the probability of being late is reduced to 18 if it is not rainy and there is no heavy traffic.
> In other situations (rainy and no traffic, not rainy and traffic) the probability of being late is 0.25.
> You pick a random day.
> Write a program to find following : 
> a. What is the probability that it's not raining and there is heavy traffic and I am not late?
> b. What is the probability that I am late?
> c. Given that I arrived late at work, what is the probability that it rained that day?
"""
# Solution by Zeeshan Sarwar

# Provided data

# rain
rain_prob = 1/3
rain_heavy_traffic = 1/2
rain_heavy_traffic_late = 1/2
rain_heavy_traffic_not_late = 1/2
rain_light_traffic = 1/2
rain_light_traffic_late = 1/4
rain_light_traffic_not_late = 3/4

# no rain
no_rain_prob = 2/3
no_rain_heavy_traffic = 1/4
no_rain_heavy_traffic_late = 1/4
no_rain_heavy_traffic_not_late = 3/4
no_rain_light_traffic = 3/4
no_rain_light_traffic_late = 1/8
no_rain_light_traffic_not_late = 7/8

try:    
    # Late probability
    late_due_to_rain = (rain_prob*rain_heavy_traffic*rain_heavy_traffic_late)+(rain_prob*rain_light_traffic*rain_light_traffic_late)
    late_due_to_no_rain = (no_rain_prob*no_rain_heavy_traffic*no_rain_heavy_traffic_late)+(no_rain_prob*no_rain_light_traffic*no_rain_light_traffic_late)
    prob_late = late_due_to_rain + late_due_to_no_rain

    # a. What is the probability that it's not raining and there is heavy traffic and I am not late?
    print("\n-------------------------------------\n")
    print(f"The probability that it's not raining and there is heavy traffic and I am not late :")
    print(f"P(No_Rain & Heavy_Traffic & Not_Late) : {no_rain_prob * no_rain_heavy_traffic * no_rain_heavy_traffic_not_late})")
    print("\n-------------------------------------\n")
    # b. What is the probability that I am late?
    print(f"The probability that I am late is : ")
    print(f"P(Late) : {prob_late}")
    print("\n-------------------------------------\n")
    # c. Given that I arrived late at work, what is the probability that it rained that day?
    print("The probability that it rained that day, given that I arrived late at work is : ")
    print("THe calculation formula according to Bayes' theorem is : \nP(Rained | Late) : (P(Late) * P(Late | Rained) ) /P(Rained) ")
    print(f"P(Late | Rained) : {(prob_late * late_due_to_rain)/rain_prob }")
    print(f"late_due_to_rain : {late_due_to_rain}")
    print(f"prob_late : {prob_late}")
    print("\n-------------------------------------\n")

except Exception as e:
    print(f" Error: {e}")