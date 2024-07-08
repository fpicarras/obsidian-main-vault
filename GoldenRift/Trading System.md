***
# Wares Mod

> Used to create trading contracts to change items in the **Delivery Table** (workstation), players can buy contracts from world venders.

Contracts can also expire or not, via time or number of uses. Unlimited contracts should cost more.
For reference here is the [GitHub page](https://github.com/mortuusars/Wares/wiki).
## Delivery Agreement

Example of a simple agreement without trade limit - *ordered* field:
```/give @s wares:sealed_delivery_agreement{title:'{"text":"A Great Deal"}',requested:[{id:"minecraft:stick",Count:{min:4,max:16,step:4}}],payment:[{id:"minecraft:emerald",Count:1}],ordered:-1}```


