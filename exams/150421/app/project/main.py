from project import aquarium
from project.controller import Controller

controller = Controller()
controller.add_aquarium('FreshwaterAquarium', 'Aqua')
controller.add_decoration('Plant')
controller.add_decoration('Ornament')
print(controller.insert_decoration('Aqua', 'Plant'))
print(controller.insert_decoration('Aqua', 'Ornament'))
print(controller.add_fish('Aqua', 'FreshwaterFish', 'Nemo', 'species', 2.6))
print(controller.add_fish('Aqua', 'FreshwaterFish', 'Nemo1', 'species', 2.6))
print(controller.add_fish('Aqua', 'FreshwaterFish', 'Nemo2', 'species', 2.6))
controller.add_aquarium('SaltwaterAquarium', 'Aqua2')
print(controller.calculate_value('Aqua'))
print(controller.feed_fish('Aqua2'))
print(controller.report())
