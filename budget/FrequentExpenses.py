from . import Expense
import collections
import matplotlib.pyplot as plt

"""
Count Expenses by Category
Read in the Spending Data and display the categories with the most purchases in a graph.
"""

expenses = Expense.Expenses()
expenses.read_expenses('data/spending_data.csv')

# Create a List of the Spending Categories
spending_categories = []

for expense in expenses.list:
    spending_categories.append(expense.category)

# Count Categories with a Counter Collection
spending_counter = collections.Counter(spending_categories)
print(spending_counter)

# Get the Top 5 Categories
top5 = spending_counter.most_common(5)

# Convert the Dictionary to 2 Lists
categories, count = zip(*top5)

# Plot the Top 5 Most Common Categories
fig, ax = plt.subplots()

ax.bar(categories, count)

# Create the bar chart
ax.set_title('# of Purchases by Category')

# Display the graph
plt.show()
