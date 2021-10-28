# Create calculate_insurance_cost() function below: 
def calculate_insurance_cost(age, sex, bmi, num_of_children, smoker, person):
  estimated_cost = 250*age - 128*sex + 370*bmi + 425*num_of_children + 24000*smoker - 12500
  test = 10
  
  return estimated_cost

def difference_in_cost (insurance_cost1, insurance_cost2):
  difference = insurance_cost1 - insurance_cost2
  print("The difference in cost between the two given insurances is: " + str(abs(difference)) + " dollars.")
  
#age (int)
#sex (boolean) 0 for female
#bmi (float)
#num_of_children (int)
#smoker(boolean) 0 for non-smoker

# Estimate Maria's insurance cost
maria_insurance_cost = calculate_insurance_cost(28, 0, 26.2, 3, 0, "Maria")
print(maria_insurance_cost)
# Estimate Omar's insurance cost 
omar_insurance_cost = calculate_insurance_cost(35, 1, 22.2, 0, 1, "Omar")
print(omar_insurance_cost)
difference_in_cost(maria_insurance_cost, omar_insurance_cost)
