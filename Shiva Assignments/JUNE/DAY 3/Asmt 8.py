# ------------------------------------------ASSIGNMENT 8----------------------------------------------
# Q. In a town, the percentage of men is 52. The percentage of
# total literacy is 48. If total percentage of literate men is 35 of
# the total population, write a program to find the total number
# of illiterate men and women if the population of the town is 80,000.

population_total = 80000
population_men = population_total * 0.52
population_women = population_total - population_men

literate_total = population_total * 0.48
literate_men = population_total * 0.35
literate_women = literate_total - literate_men

illiterate_men = population_men - literate_men
illiterate_women = population_women - literate_women

print("Total number of illiterate men = {0}\n"
      "Total number of illiterate women = {1}".format(illiterate_men,illiterate_women))