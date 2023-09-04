class City:
	"""Класс описывающий город, в атрибутах хранит:
	  свой номер(используется для отладки кода), 
	  список дорог, которые ведут к нему,  
	  информацию о штате, которому принадлежит,
	  флаг, который поднимается во время проверок после катаклизма"""
	
	def __init__(self, num):
		self.num = num
		self.roads = []
		self._state = None
		self.checked = False

	@property
	def state(self):
		'''свойство города о принадлежности к штату'''
		return self._state

	@state.setter
	def state(self, state):
		"""При присоединении города к штату в штат передается информация о городе"""
		# назначить свой штат
		self._state = state
		# добавить в штат себя 
		state.cities.append(self)


	def find_neighbours(self, state):
		"""Метод для создания штата. 
		Город 'отправляет представителей' по всем дорогам, которые к нему ведут с информацией о себе и своем штате,
		а так же назначает каждой дороге свой штат.
		Рекурсивно используется с функицей make_neighbours класса Road"""
		for road in self.roads:
			# соотнести дорогу со штатом
			road.state = self.state
			# рекурсивно вызвать функцию make_neighbours этой дороги
			road.make_neighbours(self, state)

	def check(self, x):
		"""Метод проверяющий количество городов, до которых можно добраться из этого города, возвращает количество доступных городов
		получает число x - дороги которые не больше этого числа уничтожены и ими нельзя пользоваться """
		# Поднимаем флаг, что город проверен что бы не вернуться к нему из-за рекурсии
		self.checked = True
		# 'Отправляем вестников по уцелевшим дорогам'
        # Вызываем метод check для дорог, которые больше числа x, суммируем возвращаемые данные и записываем в result
		result = sum(road.check(self, x) for road in self.roads if road.lenght > x) + 1    # граничное значение
		# после выхода из рекурсии снимаем флаг и возвращаем полученное значение
		self.checked = False
		return result



	def __repr__(self):
		'''Формальное представление для отладки кода, не совсем корректно, 
		должно быть (return f"City({self.num}") но на момент решения нужны были именно эти данные'''
		return f"City({self.num}, {self.roads}, {self.state})"


class Road:
	"""Класс описывающий дорогу. 
	Храни в атрибутах:
	Информацию о штате, к которой принадлежит
	информацию о городах в которых находится
	информацию о своей длине"""
	def __init__(self, first, second, lenght):
		self.state = None
		self.first = first
		self.second = second
		self.lenght = lenght

	def make_neighbours(self, city, state):
		"""метод для создания связей между городами
		получает информацию о вызвавшем его городе и штате, записывает свой штат и вызывает метод find_neighbours и второго своего города"""
		if self.first is city:
			if self.second.state is None:	
				self.second.state = state
				self.second.find_neighbours(state)
		elif self.second is city:
			if self.first.state is None:	
				self.first.state = state
				self.first.find_neighbours(state)

	def __repr__(self):
		'''Формальное представление для отладки кода, не совсем корректно, 
		должно быть (return f"Road({self.first}, {self.second}, {self.lenght}") но на момент решения нужны были именно эти данные'''
		return f"Road({self.state}, {self.lenght})"

	def check(self, city,  num):
		"""Вспомогательный метод для метода check класса City, получает информацию о вызвавшем городе 
		и число х - дороги которые не больше этого числа уничтожены и ими нельзя пользоваться.
		  Проверяет информацию о вызвавшем его городе и вызывает метод check во втором, если он еще не проверен """
		if self.first is city:
			if self.second.checked:	
				return 0
			else:
				return self.second.check(num) 
		elif self.second is city:
			if self.first.checked:	
				return 0
			else:
				return self.first.check(num) 
	


class State:
	def __init__(self, num):
		self.num = num
		self.cities = []

	def __repr__(self):
		return f"State({self.num})"
	
# считываем данные о количестве городов и дорог
city_count, road_count = [int(i) for i in input().split()]

# создаем города 
cities = [City(i) for i in range(1, city_count+1)]

# создаем список для хранения дорог
roads = []

# Создаем переменные для хранения штатов и их количества
states = []
states_count = 0

# создаем цикл по количеству дорог
for i in range(road_count):
	# считываем все данные о дороге и создаем дорогу на основе этой информации
	first, second, lenght = [int(i) for i in input().split()]
	temp = Road(cities[first-1], cities[second-1], lenght)
	#добавляем ее в список дорог и в списки дорог в городах куда она ведет
	roads.append(temp)
	cities[first-1].roads.append(temp)
	cities[second-1].roads.append(temp)

# обходим все города в цикле
for i in cities:
	# если у города еще нет штата создаем новый штат, добавляем город к этому штату и вызываем у города метод find_neighbours
    # Метод рекурсивно обходит все доступные города и добавляет их в штат
    # теперь эти города будут пропущены в цикле, а при обнаружении города без штата снова будет создан штат и запущен рекурсивный метод 
	if i.state is None:
		states_count += 1
		temp = State(states_count)
		states.append(temp)
		i.state = temp
		i.find_neighbours(temp)

# находим максимальную длину дороги из всех дорог
max_len = max(roads, key = lambda x: x.lenght).lenght

# ищем максимально возможное число - длина дороги больше которой разрушать нельзя
largest = 0

# постепенно увеличиваем число и проверяем штаты

for i in range(1, max_len + 1):
	flag = True
	for state in states:
		# для первого города в каждом штате вызываем метод check и смотрим, во сколько городов из него можно попасть
        # если городов стало меньше, ставим flag = False и прерываем цикл 
		if len(state.cities) != state.cities[0].check(i):
			flag = False
			break
	if flag:
		# Если число городов во всех штатах не изменилось, дороги до такой длины можно уничтожить 
		largest = i


# выводим результат
print(largest)