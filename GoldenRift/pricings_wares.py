import pandas as pd

class WaresCreator:
    def __init__(self, experience=0, expiresInSeconds=-1, ordered=-1) -> None:
        self.base = "/give @p wares:sealed_delivery_agreement"
        self.experience = experience
        self.expiresInSeconds = expiresInSeconds
        self.ordered = ordered
    
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

    def generate(self, requested, quantity, payment, price, title=None, buyerName=None, message=None, backsideMessage=None):
        pay = []
        req = []
        pay.append(dict(id=payment, Count=price*quantity))
        req.append(dict(id=requested, Count=quantity))
        nbtData = dict(requested=req, payment=pay, ordered=self.ordered)

        if title:
            title = dict(text=title)
            nbtData["title"] = title
        if buyerName:
            #buyerName = dict(text=buyerName)
            nbtData["buyerName"] = buyerName
        if message:
            message = self.format_dict(dict(text=message)).replace("'", '"')
            nbtData["message"] = message
        if backsideMessage:
            #backsideMessage = dict(text=backsideMessage)
            nbtData["backsideMessage"] = backsideMessage

        return self.base + self.format_dict(nbtData)

class MarkdownPage:
    def __init__(self, name) -> None:
        self.page = []
        self.name = name

    def addTrade(self, requested_name, qty, payment_name, price, command):
        t_str = ["## " + requested_name]
        t_str.append(str(qty) + " **" + requested_name + "** for " + str(round(price*qty)) + " **" + payment_name+"**.")
        t_str.append("```" + command + "```")
        self.page += t_str

    def addLine(self, text):
        self.page += [text]
    
    def write(self, path="./"):
        name = path + self.name + ".md"
        try:
            with open(name, "w") as fp:
                for line in self.page:
                    fp.write(line + "\n")
                fp.close()
        except Exception as e:
            print(e)

class TradingPages:
    def __init__(self, filePath, newFileName) -> None:
        self.filePath = filePath
        self.newFileName = newFileName

        self.data = pd.read_excel('GoldenRift-Pricing.xlsx')
        self.data = self.data.groupby('Type')

    def createSinglePage(self):
        md = MarkdownPage(name="test")
        wc = WaresCreator(experience=10)

        # Print each group
        for group_name, group_data in self.data:
            md.addLine("# " + group_name)
            for index, row in group_data.iterrows():
                command = wc.generate(row['ID'], row['Qty'], 'emerald', row['Sell Price (Unit)'])
                md.addTrade(row['Name'], row['Qty'], 'Emerald', row['Sell Price (Unit)'], command)
            md.addLine("***")

#command = wc.generate("emerald", 4, "diamond", 1, backsideMessage="hihi", buyerName="filipe", message="Those stripped of the grace of gold shall all meet fate, in the embrace of Messmer´s Flame")
#print(command)

#md.addTrade("Esmerald", 4, "Diamond", 1, command)
md.write()
