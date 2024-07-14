class Villager:
    def __init__(self, name: str, type: str, profession: str, level: int) -> None:
        self.name = name
        self.type = type
        self.prof = profession
        self.level = level
        self.trades = []

    def addTrade(self, buyId: str, b_count: int, sellId: str, s_count: int, maxUses = 9999999):
        aux = dict(buy = dict(id = buyId, Count = b_count), sell = dict(id = sellId, Count = s_count), maxUses = maxUses)
        self.trades.append(aux)

    def format_dict(self, d):
        if isinstance(d, dict):
            formatted_items = []
            for key, value in d.items():
                formatted_items.append(f"{key}: {self.format_dict(value)}")
            return "{" + ", ".join(formatted_items) + "}"
        elif isinstance(d, list):
            formatted_items = [self.format_dict(item) for item in d]
            return "[" + ", ".join(formatted_items) + "]"
        elif isinstance(d, str):
            return f"'{d}'"
        else:
            return str(d)

    def getCommand(self):
        return self.format_dict(dict(VillagerData = dict(profession=self.prof, level=self.level, type=self.type), Offers = dict(Recipes = self.trades)))

v = Villager("test", "plains", "farmer", "5")
v.addTrade("emerald", )


    