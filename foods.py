class Proteins:
    def __init__(self, Beef, Lamb, Chicken, Seafood):
        self.beef = Beef
        self.lamb = Lamb
        self.chicken = Chicken
        self.seafood = Seafood

        def __str__(self):
            return f'{self.beef}Beef {self.lamb}Lamb {self.chicken}Chicken {self.seafood}Seafood'
