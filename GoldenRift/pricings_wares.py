import pandas as pd
import os

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

    def generate(self, requested: str, quantity: int, payment: str, price: float, title=None, buyerName=None, message=None, backsideMessage=None):
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
    def __init__(self, name: str) -> None:
        self.page = []
        self.name = name

    def addTrade(self, requested_name: str, qty: int, payment_name: str, price: float, command: str):
        t_str = ["## " + requested_name]
        t_str.append(str(qty) + " **" + requested_name + "** for " + str(round(price*qty)) + " **" + payment_name+"**.")
        t_str.append("```" + command + "```")
        self.page += t_str

    def addLine(self, text: str):
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
    def __init__(self, filePath: str, newFileName: str, waresCreator: WaresCreator) -> None:
        self.filePath = filePath
        self.newFileName = newFileName
        self.wares = waresCreator

    def createSinglePage(self):
        data = pd.read_excel(self.filePath)
        data = data.groupby('Type')

        md = MarkdownPage(name=self.newFileName)

        # Print each group
        for group_name, group_data in data:
            md.addLine("# " + group_name)
            for index, row in group_data.iterrows():
                command = self.wares.generate(row['ID'], row['Qty'], 'emerald', row['Sell Price (Unit)'])
                md.addTrade(row['Name'], row['Qty'], 'Emerald', row['Sell Price (Unit)'], command)
            md.addLine("***")
            md.write()

    def createMultiPage(self):
        # Create the folder for housing the pages
        folderName = "./" + self.newFileName
        if not os.path.exists(folderName):
            os.makedirs(folderName)

        data = pd.read_excel(self.filePath)
        group_names = data['Type'].unique()

        for group_name in group_names:
            md = MarkdownPage(name=folderName + "/" + group_name)
            group_data = data[data["Type"] == group_name]
            for index, row in group_data.iterrows():
                command = self.wares.generate(row['ID'], row['Qty'], 'emerald', row['Sell Price (Unit)'])
                md.addTrade(row['Name'], row['Qty'], 'Emerald', row['Sell Price (Unit)'], command)
            md.addLine("***")
            md.write()

wc = WaresCreator(experience=10)
test = TradingPages("GoldenRift-Pricing.xlsx", "test", )
test.createMultiPage()


        
