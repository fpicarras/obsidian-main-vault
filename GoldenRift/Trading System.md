***
# Wares Mod

> Used to create trading contracts to change items in the **Delivery Table** (workstation), players can buy contracts from world venders.

Contracts can also expire or not, via time or number of uses. Unlimited contracts should cost more.
For reference here is the [GitHub page](https://github.com/mortuusars/Wares/wiki).
## Delivery Agreement

Example of a simple agreement without trade limit - *ordered* field:
```/give @s wares:sealed_delivery_agreement{title:'{"text":"A Great Deal"}',requested:[{id:"minecraft:stick",Count:{min:4,max:16,step:4}}],payment:[{id:"minecraft:emerald",Count:1}],ordered:-1}```

Relevant fields:
- `id` - _string_ - Transfered as is.
- `buyerName` - either _Component_ or _List of WeightedComponent_.
- `buyerAddress` - either _Component_ or _List of WeightedComponent_.
- `title` - either _Component_ or _List of WeightedComponent_.
- `message` - either _Component_ or _List of WeightedComponent_.
- [`seal`](https://github.com/mortuusars/Wares/wiki/Seal) - _string_ - Transfered as is.
- `sealTooltip` - _component_ - Text shown on seal mouse over. Not transfered.
- `backsideMessage` - _component_ - Text shown on the back of a letter (In the inspect screen). Not transfered.
- `requested` - either _LootTable path_ or [List of [Sealed Requested Items]](https://github.com/mortuusars/Wares/wiki/Sealed-Delivery-Agreement#sealed-requested-item) - Gets the list of items from a loot table or just transfers as is if list is provided.
- `payment` - either _LootTable path_ or [List of ItemStack] - Gets the list of items from a loot table or just transfers as is if list is provided.
- `ordered` - _Integer_ or [Stepped Int](https://github.com/mortuusars/Wares/wiki/Sealed-Delivery-Agreement#stepped-int) - Finalized to a number.
- `experience` - _Integer_ or [Stepped Int](https://github.com/mortuusars/Wares/wiki/Sealed-Delivery-Agreement#stepped-int) - Finalized to a number.
- `deliveryTime` - _Integer_ or [Stepped Int](https://github.com/mortuusars/Wares/wiki/Sealed-Delivery-Agreement#stepped-int) - Finalized to a number.
- `expiresInSeconds` - _Integer_ or [Stepped Int](https://github.com/mortuusars/Wares/wiki/Sealed-Delivery-Agreement#stepped-int) - Finalized to a number.
## Script

> To improve trade making, a Python script and a Excel file were added in this directory, they allow for the easy creation of wares trades.
***
# Pricing

Prices need to be based of the Vanilla item prices of the game. Aimed for the prices sold with discount - for example, 1 Pumpkin for 1 emerald.
***
# Villagers

> Villagers are unique, because they allow some worldbuilding to occur, one could create stalls or custom villages that focus on some specific products; like a magic town or a wandering gypsy monster hunter!

## Datapack

This [Datapack](https://www.planetminecraft.com/data-pack/villager-shop-creator/) allows us to create simple villager trades with a huge customization potential.
On the downside... It requires in-game action... meaning we can't simply generate a script to do the job... Or can we 👀...

## Commands

This is wayyy funnier! You see a simple command for a villager would be like this:
```/summon villager ~ ~1 ~ {VillagerData:{profession:farmer,level:2,type:plains},PersistenceRequired:1,Offers:{Recipes:[{buy:{id:acacia_boat,Count:1},sell:{id:emerald,Count:2},rewardExp:0b,priceMultiplier:0f,specialPrice:-1,demand:5,maxUses:9999999}]}}```

And so... we can exploit this: [[Villager Command Generator]]