import json
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

with open('selenium/result2.json', 'r') as file:
    data = json.load(file)


names, plot_dicts = [], []
for d in data:
    names.append(d['Name'])
    plot_dict = {
        'value': int(d['Price']),
        'xlink': d['URL']

    }
    plot_dicts.append(plot_dict)


my_style = LS('#333366', base_style=LCS)
my_config = pygal.Config()
my_config.x_label_rotation = 45
my_config.show_legend = False
my_config.title_font_size = 24
my_config.label_font_size = 14
my_config.major_label_font_size = 18
my_config.truncate_label = 15
my_config.show_y_guides = False
my_config.width = 1000

chart = pygal.Bar(my_config, style=my_style)
chart.title = 'Prebena price'
chart.x_labels = names

chart.add('', plot_dicts)
chart.render_to_file('selenium/prebena_price3.svg')

