from item import Item

#Instantiating Objects
water_gun = Item("Water Gun")
water_gun.set_description( "Zombies afraid of water!" )

sauce_pan = Item("Sauce Pan")
sauce_pan.set_description( "A hot pan chases skeletons away!" )

#invoking methods
water_gun.get_details()
sauce_pan.get_details()