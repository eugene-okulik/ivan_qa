class Flowers:
    def __init__(self, name, color, freshness, stem_length, price, life_time):
        self.name = name
        self.color = color
        self.freshness = freshness
        self.stem_length = stem_length
        self.price = price
        self.life_span = life_time

    def __str__(self):
        return (f'STR {self.name} ({self.color}), '
                f'Stem: {self.stem_length}cm, Fresh: {self.freshness}, '
                f'Price: {self.price}$, Life: {self.life_span}d')

    def __repr__(self):
        return (f'REPR {self.name} ({self.color}), '
                f'Stem: {self.stem_length}cm, Fresh: {self.freshness}, '
                f'Price: {self.price}$, Life: {self.life_span}d')


class PartyFlowers(Flowers):
    def __init__(self, name, color, freshness, stem_length, price, life_time):
        super().__init__(name, color, freshness, stem_length, price, life_time)
        self.party_flower = True

    def __str__(self):
        return (f'{self.name} ({self.color}), '
                f'Stem: {self.stem_length}cm, Fresh: {self.freshness}, '
                f'Price: {self.price}$, Life: {self.life_span}d')


class WeddingFlowers(Flowers):
    def __init__(self, name, color, freshness, stem_length, price, life_time):
        super().__init__(name, color, freshness, stem_length, price, life_time)
        self.wedding_flower = True

    def __str__(self):
        return (f'{self.name} ({self.color}), '
                f'Stem: {self.stem_length}cm, Fresh: {self.freshness}, '
                f'Price: {self.price}$, Life: {self.life_span}d')


class Buquet:
    def __init__(self, *flowers):
        self.flowers = list(flowers)

    # Добавление цветка в букет
    def add_flower(self, flower):
        self.flowers.append(flower)

    # Общая стоимость букета
    def total_price(self):
        return sum(flower.price for flower in self.flowers)

    # Средний срок жизни цветов в букете
    def average_life_span(self):
        return sum(
            flower.life_span for flower in self.flowers) / (
            len(self.flowers) if self.flowers else 0)

    # Сортировка цветов по свежести
    def sort_by_freshness(self):
        self.flowers.sort(key=lambda flower: flower.freshness, reverse=True)
        return self.flowers

    # Сортировка цветов по цвету
    def sort_by_color(self):
        self.flowers.sort(key=lambda flower: flower.color, reverse=False)
        return self.flowers

    # Сортировка по длине стебля
    def sort_by_stem_length(self):
        self.flowers.sort(key=lambda flower: flower.stem_length, reverse=True)
        return self.flowers

    # Сортировка по цене
    def sort_by_price(self):
        self.flowers.sort(key=lambda flower: flower.price, reverse=False)
        return self.flowers

    # Поиск цветка по name
    def search_by_name(self, name):
        return [flower for flower in self.flowers if flower.name == name]


# Экземпляры цветов
party_rose_red = PartyFlowers("Rose", "Red", True, 40, 10, 5)
party_lily_yellow = PartyFlowers("Lily", "Yellow", True, 35, 12, 6)
wedding_lily_red = WeddingFlowers("Lily", "Red", False, 30, 15, 7)
wedding_camomile_blue = WeddingFlowers("Camomile", "Blue", True, 25, 8, 4)

simple_buquet = Buquet(party_rose_red, wedding_lily_red)

big_buquet = Buquet(
    party_rose_red,
    party_lily_yellow,
    wedding_lily_red,
    wedding_camomile_blue)
print(big_buquet.average_life_span())
print(big_buquet.search_by_name("Rose"))
