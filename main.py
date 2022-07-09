import math

USEFUL_WIDTH_METAL_TILE: float = 1.10
FULL_WIDTH_METAL_TILE: float = 1.19
MIN_LENGTH: int = 850
MAX_LENGTH: int = 5050
OVERLAP: int = 150
WAVE_STEP: int = 350
COST_ROOF_PLANKS: float = 23.00

UNWRAPPED_CORNICE_PLANK: float = 0.178
UNWRAPPED_L_PLANK: float = 0.210
UNWRAPPED_END_PLANK: float = 0.250
UNWRAPPED_SNOW_HOLDER: float = 0.250


def int_r(num: float):
    """
    Статическая функция int_r, округляет в меньшую сторону, если число после запятой < 0.5,
    а так же округляет в большую сторону, если число после запятой > 0.5.
    На вход принимает параметр num (число с плавающей точкой) и возвращает int num.
    """
    num = int(num + (0.5 if num > 0 else -0.5))
    return num


def break_sheets(value):
    """
    Статическая функция break_sheets, позволяет разбить длину листов пополам или на три, четыре листа,
    при превышении длины листов более 5050мм.
    """
    if MIN_LENGTH <= length_metal_tile1 > MAX_LENGTH and length_metal_tile1 <= 9950:
        row1_sheets1 = (math.ceil(
            ((round((length_metal_tile1 + OVERLAP) / 2)) - MIN_LENGTH) / WAVE_STEP) * WAVE_STEP) + MIN_LENGTH
        row2_sheets1 = round(length_metal_tile1 + OVERLAP) - row1_sheets1
        print(f'Длина листов ската №1:         {row1_sheets1}мм    {row2_sheets1}мм\n'
              f'Количество листов МЧ ската №1: {number_sheets1}шт      {number_sheets1}шт')
        print(f'РАССЧИТАННЫЕ ЛИСТЫ НА ЗАКАЗ:   {row1_sheets1}мм    {row2_sheets1}мм\n'
              f'СКАТ №1                        {number_sheets1}шт      {number_sheets1}шт')
    elif MIN_LENGTH <= length_metal_tile1 > 9950 and length_metal_tile1 < 14850:
        row1_sheets1 = (math.ceil(
            ((round((length_metal_tile1 + OVERLAP * 2) / 3)) - MIN_LENGTH) / WAVE_STEP) * WAVE_STEP) + MIN_LENGTH
        row2_sheets1 = row1_sheets1
        row3_sheets1 = round(length_metal_tile1 + OVERLAP * 2) - row1_sheets1 - row2_sheets1
        print(f'Длина листов ската №1:         {row1_sheets1}мм    {row2_sheets1}мм    {row3_sheets1}мм\n'
              f'Количество листов МЧ ската №1: {number_sheets1}шт      {number_sheets1}шт      {number_sheets1}шт')
        print(f'РАССЧИТАННЫЕ ЛИСТЫ НА ЗАКАЗ:   {row1_sheets1}мм    {row3_sheets1}мм\n'
              f'СКАТ №1                        {number_sheets1 * 2}шт      {number_sheets1}шт')
    elif MIN_LENGTH <= length_metal_tile1 >= 14850:
        row1_sheets1 = (math.ceil(
            ((round((length_metal_tile1 + OVERLAP * 3) / 4)) - MIN_LENGTH) / WAVE_STEP) * WAVE_STEP) + MIN_LENGTH
        row2_sheets1 = row1_sheets1
        row3_sheets1 = row1_sheets1
        row4_sheets1 = round(length_metal_tile1 + OVERLAP * 3) - row1_sheets1 - row2_sheets1 - row3_sheets1
        print(
            f'Длина листов ската №1:         '
            f'{row1_sheets1}мм    {row2_sheets1}мм    {row3_sheets1}мм    {row4_sheets1}мм\n'
            f'Количество листов МЧ ската №1: '
            f'{number_sheets1}шт      {number_sheets1}шт      {number_sheets1}шт      {number_sheets1}шт')
        print(f'РАССЧИТАННЫЕ ЛИСТЫ НА ЗАКАЗ:   {row1_sheets1}мм    {row4_sheets1}мм\n'
              f'СКАТ №1                        {number_sheets1 * 3}шт      {number_sheets1}шт')
    else:
        row1_sheets1 = round(length_metal_tile1)
        print(f'Длина листов ската №1:         {row1_sheets1}мм\n'
              f'Количество листов МЧ ската №1: {number_sheets1}шт')
        print(f'РАССЧИТАННЫЕ ЛИСТЫ НА ЗАКАЗ:   {row1_sheets1}мм\n'
              f'СКАТ №1                        {number_sheets1}шт')

    if MIN_LENGTH <= length_metal_tile2 > MAX_LENGTH and length_metal_tile2 <= 9950:
        row1_sheets2 = (math.ceil(
            ((round((length_metal_tile2 + OVERLAP) / 2)) - MIN_LENGTH) / WAVE_STEP) * WAVE_STEP) + MIN_LENGTH
        row2_sheets2 = round(length_metal_tile2 + OVERLAP) - row1_sheets2
        print(f'Длина листов ската №2:         {row1_sheets2}мм    {row2_sheets2}мм\n'
              f'Количество листов МЧ ската №2: {number_sheets2}шт      {number_sheets2}шт')
        print(f'РАССЧИТАННЫЕ ЛИСТЫ НА ЗАКАЗ:   {row1_sheets2}мм    {row2_sheets2}мм\n'
              f'СКАТ №2                        {number_sheets2}шт      {number_sheets2}шт')
    elif MIN_LENGTH <= length_metal_tile2 > 9950 and length_metal_tile1 < 14850:
        row1_sheets2 = (math.ceil(
            ((round((length_metal_tile2 + OVERLAP * 2) / 3)) - MIN_LENGTH) / WAVE_STEP) * WAVE_STEP) + MIN_LENGTH
        row2_sheets2 = row1_sheets2
        row3_sheets2 = round(length_metal_tile2 + OVERLAP * 2) - row1_sheets2 - row2_sheets2
        print(f'Длина листов ската №2:         {row1_sheets2}мм    {row2_sheets2}мм    {row3_sheets2}мм\n'
              f'Количество листов МЧ ската №2: {number_sheets2}шт      {number_sheets2}шт      {number_sheets2}шт')
        print(f'РАССЧИТАННЫЕ ЛИСТЫ НА ЗАКАЗ:   {row1_sheets2}мм    {row3_sheets2}мм\n'
              f'СКАТ №2                        {number_sheets2 * 2}шт      {number_sheets2}шт')
    elif MIN_LENGTH <= length_metal_tile2 > 14850:
        row1_sheets2 = (math.ceil(
            ((round((length_metal_tile2 + OVERLAP * 3) / 4)) - MIN_LENGTH) / WAVE_STEP) * WAVE_STEP) + MIN_LENGTH
        row2_sheets2 = row1_sheets2
        row3_sheets2 = row1_sheets2
        row4_sheets2 = round(length_metal_tile2 + OVERLAP * 3) - row1_sheets2 - row2_sheets2 - row3_sheets2
        print(
            f'Длина листов ската №1:         '
            f'{row1_sheets2}мм    {row2_sheets2}мм    {row3_sheets2}мм    {row4_sheets2}мм\n'
            f'Количество листов МЧ ската №1: '
            f'{number_sheets2}шт      {number_sheets2}шт      {number_sheets2}шт      {number_sheets2}шт')
        print(f'РАССЧИТАННЫЕ ЛИСТЫ НА ЗАКАЗ:   {row1_sheets2}мм    {row4_sheets2}мм\n'
              f'СКАТ №1                        {number_sheets2 * 3}шт      {number_sheets2}шт')
    else:
        row1_sheets2 = round(length_metal_tile2)
        print(f'Длина листов ската №2:         {row1_sheets2}мм\n'
              f'Количество листов МЧ ската №2: {number_sheets2}шт')
        print(f'РАССЧИТАННЫЕ ЛИСТЫ НА ЗАКАЗ:   {row1_sheets2}мм\n'
              f'СКАТ №2                        {number_sheets2}шт')
    return value


class RoofSlope:
    def __init__(self,
                 ridge: float,
                 cornice: float,
                 left_end: float,
                 right_end: float,
                 cornice_clearance: float = 0.05,
                 ridge_clearance: float = 0.0,
                 ):
        """
        slope1:                 ridge_clearance
                  ___________________ridge________________________
                 |                                               |
                 |                      ↓                        |
                 |                      ↓                        |
        left_end |                      ↓                        | right_end
                 |                      ↓                        |
                 |                                               |
                 |__________________cornice______________________|
                                cornice_clearance

        Класс RoofSlope (кровельный скат), включает в себя следующие параметры:
        ridge: конёк - верхняя сторона прямоугольника в единицах измерения мп
        cornice: карниз - нижняя сторона прямоугольника в единицах измерения мп
        left_end: левый торец - левая сторона прямоугольника в единицах измерения мп
        right_end: правый торец - правая сторона прямоугольника в единицах измерения мп
        cornice_clearance: карнизный напуск - на какую величину в мп, выходят листы
        металлочерепицы за край карниза
        ridge_clearance: коньковый напуск - на какую величину в мп, выходят листы
        металлочерепицы выше края конька (по умолчанию равен нулю)
        """
        self.ridge = ridge
        self.cornice = cornice
        self.left_end = left_end
        self.right_end = right_end
        self.cornice_clearance = cornice_clearance
        self.ridge_clearance = ridge_clearance

    def number_sheets(self):
        return round(self.cornice / USEFUL_WIDTH_METAL_TILE, 2)

    def length_sheets(self):
        return self.left_end + self.cornice_clearance + self.ridge_clearance


class RoofSlope2(RoofSlope):
    def __init__(self,
                 ridge: float,
                 cornice: float,
                 left_end: float,
                 right_end: float,
                 cornice_clearance: float = 0.05,
                 ridge_clearance: float = 0.0,
                 ):
        """
        slope2:                 ridge_clearance
                  ___________________ridge________________________
                 |                                               |
                 |                      ↓                        |
                 |                      ↓                        |
        left_end |                      ↓                        | right_end
                 |                      ↓                        |
                 |                                               |
                 |__________________cornice______________________|
                                cornice_clearance

        Класс RoofSlope2 (кровельный скат №2), включает в себя следующие параметры:
        ridge: конёк - верхняя сторона прямоугольника в единицах измерения мп ската №2
        cornice: карниз - нижняя сторона прямоугольника в единицах измерения мп ската №2
        left_end: левый торец - левая сторона прямоугольника в единицах измерения мп ската №2
        right_end: правый торец - правая сторона прямоугольника в единицах измерения мп ската №2
        cornice_clearance: карнизный напуск - на какую величину в мп, выходят листы
        металлочерепицы за край карниза ската №2
        ridge_clearance: коньковый напуск - на какую величину в мп, выходят листы
        металлочерепицы выше каря конька  ската №2 (по умолчанию равен нулю)
        """
        super().__init__(ridge, cornice, left_end, right_end, cornice_clearance, ridge_clearance)


slope1 = RoofSlope(11.3, 11.3, 15, 15, 0, 0.05)
useful_metal_tile_area1 = slope1.number_sheets() * slope1.length_sheets() * USEFUL_WIDTH_METAL_TILE
full_metal_tile_area1 = slope1.number_sheets() * slope1.length_sheets() * FULL_WIDTH_METAL_TILE
length_metal_tile1 = round(slope1.length_sheets() * 1000)
number_sheets1 = math.ceil(slope1.number_sheets())
cornice_plank1 = math.ceil((slope1.cornice * 1.05) / 2)
l_plank1 = (slope1.cornice * 1.05) / 2
end_plank1 = ((slope1.left_end + slope1.right_end + (slope1.cornice_clearance + slope1.ridge_clearance) * 2) * 1.05) / 2
snow_holder1 = slope1.cornice / 2

slope2 = RoofSlope2(11.3, 11.3, 15, 15, 0, 0.05)
useful_metal_tile_area2 = slope2.number_sheets() * slope2.length_sheets() * USEFUL_WIDTH_METAL_TILE
full_metal_tile_area2 = slope2.number_sheets() * slope2.length_sheets() * FULL_WIDTH_METAL_TILE
length_metal_tile2 = round(slope2.length_sheets() * 1000)
number_sheets2 = int_r(slope2.number_sheets())
cornice_plank2 = (slope2.cornice * 1.05) / 2
l_plank2 = (slope2.cornice * 1.05) / 2
end_plank2 = ((slope2.left_end + slope2.right_end + (slope2.cornice_clearance + slope2.ridge_clearance) * 2) * 1.05) / 2
snow_holder2 = slope2.cornice / 2

roof_area = round(slope1.cornice * slope1.left_end + slope2.cornice * slope2.left_end, 3)
useful_metal_tile_area = round(useful_metal_tile_area1 + useful_metal_tile_area2, 3)
full_metal_tile_area = round(full_metal_tile_area1 + full_metal_tile_area2, 3)
# length_metal_tile = length_metal_tile1 + length_metal_tile2
number_sheets = number_sheets1 + number_sheets2
waterproofing_film = f'{math.ceil(roof_area / 75)}рул = {math.ceil(roof_area / 75) * 75}м2'
roofing_membrane = f'{math.ceil(roof_area / 75)}рул = {math.ceil(roof_area / 75) * 75}м2'
vapor_barrier = f'{math.ceil(roof_area / 70)}рул = {math.ceil(roof_area / 70) * 70}м2'
roofing_screws = f'{math.ceil((roof_area * 8) / 250)}уп = {(math.ceil((roof_area * 8) / 250) * 250)}шт'
ridge_screws = f'{math.ceil((slope1.ridge * 6) / 100)}уп = {(math.ceil((slope1.ridge * 6) / 100) * 100)}шт'
ridge_ribbon = f'{math.ceil(slope1.ridge / 5)}шт = {math.ceil(slope1.ridge / 5) * 5}мп'
ridge150 = f'{math.ceil((slope1.ridge * 1.05) / 2)}шт = {(math.ceil((slope1.ridge * 1.05) / 2)) * 2}мп'
ridge_cylindrical = f'{math.ceil((slope1.ridge * 1.05) / 1.2)}шт = {(math.ceil((slope1.ridge * 1.05) / 1.2)) * 1.25}мп'
plug_simple = f'{int(slope1.ridge / slope1.ridge) * 2}шт'
cornice_plank = f'{math.ceil(cornice_plank1 + cornice_plank2)}шт = {(math.ceil(cornice_plank1 + cornice_plank2) * 2)}мп'
cost_cornice_plank = round((math.ceil(cornice_plank1 + cornice_plank2) * 2) * UNWRAPPED_CORNICE_PLANK * COST_ROOF_PLANKS, 2)
l_plank = f'{math.ceil(l_plank1 + l_plank2)}шт = {(math.ceil(l_plank1 + l_plank2) * 2)}мп'
cost_l_plank = round((math.ceil(l_plank1 + l_plank2) * 2) * UNWRAPPED_L_PLANK * COST_ROOF_PLANKS, 2)
end_plank = f'{math.ceil(end_plank1 + end_plank2)}шт = {(math.ceil(end_plank1 + end_plank2)) * 2}мп'
cost_end_plank = round(((math.ceil(end_plank1 + end_plank2)) * 2) * UNWRAPPED_END_PLANK * COST_ROOF_PLANKS, 2)
snow_holder = f'{math.ceil(snow_holder1 + snow_holder2)}шт = {(math.ceil(snow_holder1 + snow_holder2) * 2)}мп'
cost_snow_holders = round((math.ceil(snow_holder1 + snow_holder2) * 2) * UNWRAPPED_SNOW_HOLDER * COST_ROOF_PLANKS, 2)

break_sheets(RoofSlope)
print(f'S кровли:                      {roof_area}м2')
print(f'Полезной S металлочерепицы:    {useful_metal_tile_area}м2')
print(f'Полной S металлочерепицы:      {full_metal_tile_area}м2')
print(f'Гидроизоляционная пленка:      {waterproofing_film}')
print(f'Мембрана:                      {roofing_membrane}')
print(f'Пароизоляционная пленка:       {vapor_barrier}')
print(f'Саморезы кровельные 4,8х29мм:  {roofing_screws}')
print(f'Саморезы коньковые 4,8х70мм:   {ridge_screws}')
print(f'Лента коньковая 260мм х 5м:    {ridge_ribbon}')
print(f'Конек 150:                     {ridge150}')
print(f'Конек цилиндрический:          {ridge_cylindrical}')
print(f'Заглушка простая:              {plug_simple}')
print(f'Карнизная планка:              {cornice_plank}       {cost_cornice_plank}руб')
print(f'L-планка:                      {l_plank}       {cost_l_plank}руб')
print(f'Торцевая планка:               {end_plank}       {cost_end_plank}руб')
print(f'Планка снегозадержателя:       {snow_holder}       {cost_snow_holders}руб')
