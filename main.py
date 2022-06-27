USEFUL_WIDTH_OF_THE_METAL_TILE: float = 1.10
FULL_WIDTH_OF_THE_METAL_TILE: float = 1.19


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
        print(self.near_cornice_bar / USEFUL_WIDTH_OF_THE_METAL_TILE)

    def length_of_the_ramp_sheets_1(self):
        print(self.near_left_end_plate + self.cornice_overhang + self.ridge_clearance)

    def number_of_ramp_sheets_2(self):
        print(self.far_cornice_bar / USEFUL_WIDTH_OF_THE_METAL_TILE)

    def length_of_the_ramp_sheets_2(self):
        print(self.far_left_end_plate + self.cornice_overhang + self.ridge_clearance)


dimensions_of_the_gable_roof = GableRoof(10, 10, 10, 5, 5, 5, 5, 0.05, 0)
