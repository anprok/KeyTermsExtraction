# create the planets.txt
planets = ['Mercury\n', 'Venus\n', 'Earth\n', 'Mars\n', 'Jupiter\n', 'Saturn\n', 'Uranus\n', 'Neptune\n']
planets_file = open('planets.txt', 'w', encoding='utf-8')
planets_file.writelines(planets)
planets_file.close()
