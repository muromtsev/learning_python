import json
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

with open('selenium/result2.json', 'r') as file:
    data = json.load(file)


names, price = [], []
for d in data:
    names.append(d['Name'])
    price.append(int(d['Price']))


my_style = LS('#333366', base_style=LCS)
chart = pygal.Bar(style=my_style, x_label_rotation=45, show_legend=False)
chart.title = 'Prebena price'
chart.x_labels = names

chart.add('', price)
chart.render_to_file('selenium/prebena_price.svg')

