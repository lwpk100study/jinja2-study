from jinja2 import Environment, FileSystemLoader

env = Environment(loader=FileSystemLoader('templates'))
template = env.get_template('helloName.jinja')
output = template.render(name="John")
print(output)
