class Villager:
    def __init__(self, name: str, type: str, profession: str, level: int, helmet=None, hands=None) -> None:
        self.nbtData = dict(VillagerData = dict(profession=profession, level=level, type=type), Offers = dict(Recipes = []))
        if helmet:
            self.nbtData["ArmorItems"] = [{}, {}, {}, dict(id=helmet, Count=1)]
        if name:
            self.nbtData["CustomName"] = '"\\"'+name+'\\""'
        if hands:
            self.nbtData["HandItems"] = [dict(id = hands, Count = 1), {}]

    def addTrade(self, buyId: str, b_count: int, sellId: str, s_count: int, maxUses = 9999999):
        aux = dict(buy = dict(id = buyId, Count = b_count), sell = dict(id = sellId, Count = s_count), maxUses = maxUses)
        self.nbtData["Offers"]["Recipes"].append(aux)

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

    def getSummon(self):
        aux = self.format_dict(self.nbtData)
        return "/summon villager ~ ~1 ~ " + aux.replace("'","")
    
    def getEgg(self):
         aux = self.format_dict(dict(EntityTag = self.nbtData))
         return "/give @p villager_spawn_egg" + aux.replace("'","")

v = Villager("test", "swamp", "librarian", "5", helmet="blue_stained_glass", hands="book")
v.addTrade("emerald", 1, "stone", 16)
print(v.getEgg())


    