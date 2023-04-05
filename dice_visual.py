import plotly.express as px

from dice import Dice

# Create two D6 dice.
dice_1 = Dice()
dice_2 = Dice()

# Make some rolls, and store results in a list.
results = []
for roll_num in range(1000):
    result = dice_1.roll() + dice_2.roll()
    results.append(result)

# Analyze the results.
frequencies = []
max_result = dice_1.num_sides + dice_2.num_sides
poss_results = range(2, max_result+1)
for value in poss_results:
    frequency = results.count(value)
    frequencies.append(frequency)

# Visualize the results
title = "Results of Rolling two D6 dice 1,000 times"
labels = {'x': 'Result', 'y': 'Frequency of Result'}
fig = px.bar(x=poss_results, y=frequencies, title=title, labels=labels)

# Further customize chart.
fig.update_layout(xaxis_dtick=1)

fig.show()