import math

USEFUL_WIDTH_OF_THE_METAL_TILE: float = 1.10
FULL_WIDTH_OF_THE_METAL_TILE: float = 1.19


def int_r(num: float):
    num = int(num + (0.5 if num > 0 else -0.5))
    return num


class GableRoof:
    def __init__(self,
                 skate_bar: float,
                 near_cornice_bar: float,
                 far_cornice_bar: float,
                 near_left_end_plate: float,
                 near_right_end_plate: float,
                 far_left_end_plate: float,
                 far_right_end_plate: float,
                 cornice_overhang: float = 0.05,
                 ridge_clearance: float = 0.0,
                 ):
        """
        Класс GableRoof (двухскатная крыша), включает в себя следующие параметры:
        skate_bar: коньковая планка
        near_cornice_bar: ближняя карнизная планка
        far_cornice_bar: дальняя карнизная планка
        near_left_end_plate: ближняя левая торцевая планка
        near_right_end_plate: ближняя правая торцевая планка
        far_left_end_plate: дальняя левая торцевая планка
        far_right_end_plate: дальняя правая торцевая планка
        cornice_overhang: карнизный свес
        ridge_clearance: коньковый напуск (по умолчанию равен нулю)
        """
        self.skate_bar = skate_bar
        self.near_cornice_bar = near_cornice_bar
        self.far_cornice_bar = far_cornice_bar
        self.near_left_end_plate = near_left_end_plate
        self.near_right_end_plate = near_right_end_plate
        self.far_left_end_plate = far_left_end_plate
        self.far_right_end_plate = far_right_end_plate
        self.cornice_overhang = cornice_overhang
        self.ridge_clearance = ridge_clearance

    def number_of_ramp_sheets_1(self):
        return self.near_cornice_bar / USEFUL_WIDTH_OF_THE_METAL_TILE

    def length_of_the_ramp_sheets_1(self):
        return self.near_left_end_plate + self.cornice_overhang + self.ridge_clearance

    def number_of_ramp_sheets_2(self):
        return round(self.far_cornice_bar / USEFUL_WIDTH_OF_THE_METAL_TILE, 2)

    def length_of_the_ramp_sheets_2(self):
        return self.far_left_end_plate + self.cornice_overhang + self.ridge_clearance


slope1 = GableRoof(10, 10, 10, 5, 5, 5, 5, 0.05)
slope2 = GableRoof(10, 10, 10, 5, 5, 5, 5, 0)
roof_area = slope1.near_cornice_bar * slope1.near_left_end_plate + slope2.far_cornice_bar * slope2.far_left_end_plate
print(f'Длина листов ската №1:         {round(slope1.length_of_the_ramp_sheets_1() * 1000)}мм\n'
      f'Количество листов МЧ ската №1: {int_r(slope1.number_of_ramp_sheets_1())}шт')
print(f'Длина листов ската №2:         {round(slope2.length_of_the_ramp_sheets_2() * 1000)}мм\n'
      f'Количество листов МЧ ската №2: {int_r(slope2.number_of_ramp_sheets_2())}шт')
print(f'Итого листов по двум скатам:   {round(slope1.number_of_ramp_sheets_1() + slope2.number_of_ramp_sheets_2())}шт')
print(f'S кровли:                      {round(roof_area, 3)}м2')
print(f'Полезной S металлочерепицы:    {round(slope1.number_of_ramp_sheets_1() * slope1.length_of_the_ramp_sheets_1() * USEFUL_WIDTH_OF_THE_METAL_TILE, 3)}м2')
print(f'Полной S металлочерепицы:      {round(slope1.number_of_ramp_sheets_1() * slope1.length_of_the_ramp_sheets_1() * FULL_WIDTH_OF_THE_METAL_TILE, 3)}м2')
print(f'Гидроизоляционная пленка:      {math.ceil(roof_area / 75)}рул')
print(f'Мембрана:                      {math.ceil(roof_area / 75)}рул')
print(f'Пароизоляционная пленка:       {math.ceil(roof_area / 70)}рул')
print(f'Саморезы кровельные 4,8х29мм:  {math.ceil((roof_area * 8) / 250) * 250}шт')
print(f'Саморезы коньковые 4,8х70мм:   {math.ceil((slope1.skate_bar * 6) / 100) * 100}шт')
print(f'Лента коньковая 260мм х 5м:    {math.ceil(slope1.skate_bar / 5)}шт')
print(f'Конек 150:                     {math.ceil((slope1.skate_bar * 1.05) / 2)}шт или {(math.ceil((slope1.skate_bar * 1.05) / 2)) * 2}мп')
