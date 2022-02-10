
#Part A
weeks = 16
classes = 5
tuition = 6000
cost_per_week = ((tuition / classes) / weeks)
print("Cost per week:", cost_per_week)
classes_per_week = 5
cost_per_class = cost_per_week/ classes_per_week
print("The cost per class: ", cost_per_class)
def print_value_and_type(variable):
  print(variable, type(variable))
every_variable= [weeks, classes, tuition, cost_per_week, classes_per_week, cost_per_class]
for variable in every_variable:
  print_value_and_type(variable)
#Part B
import random
list_of_random=["apple", "class", "watch", "4th object", "5th object"]
choice_of_random= random.choice(list_of_random)
print("""The random choice from the list "list_of_random" is: """, choice_of_random)