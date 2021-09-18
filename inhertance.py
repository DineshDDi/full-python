class pubg():
    def Player(self, Guns, Bags, Bullet_proof_Vast, Helmet, Bullets, Health_Kit, Bom):
        self.Guns = Guns
        self.Bags = Bags
        self.Bullet_Proof_Vast = Bullet_proof_Vast
        self.Helmet = Helmet
        self.Bullets = Bullets
        self.Health_Kit = Health_Kit
        self.Bom = Bom

        Guns = "M416" or not "AKM" or not "AWM" or not "UMP9" or not "Kar98" or not "SLR" or not "M762" or not "M24"
        Bags = "1st Level" or not "2nd Level" or not "3rd Level"
        Bullet_Proof_Vast = "1st Level" or not "2nd Level" or not "3rd Level"
        Helmet = "1st Level" or not "2nd Level" or not "3rd Level"
        Bullets = "9.9MM" or not "5.5MM" or not "7.6MM"
        Health_Kit = "First Aid Kit" or not "Bandage" or not "Health Drink" or not "Tablets"
        Bom = "Normal Bom" or not "Fire Bom" or not "Smoke Bom"


class COD(pubg):
    def Player(self, Drone, Shield, Robots):
        self.Drone = Drone
        self.Shield = Shield
        self.Robots = Robots

        Drone = "100KM Range"
        Shield = "2nd Level"
        Robots = "1st Level"


#The Object Name is player I'd
Hunter_Killer = COD()
Hunter_Killer.Guns = "M416", "M24"
Hunter_Killer.Bags = "3rd Level"
Hunter_Killer.Bullets = "5.5MM", "7.6MM"
Hunter_Killer.Bullet_Proof_Vast = "3rd Level"
Hunter_Killer.Health_Kit = "First Aid Kit", "Health Drink"
Hunter_Killer.Helmet = "2nd Level"
Hunter_Killer.Drone = "100KM Range"
Hunter_Killer.Shield = "2nd Level"
Hunter_Killer.Robots = "1st Level"
print("Hunter_Killer =", Hunter_Killer.__dict__)


yuvan = COD()
yuvan.Guns = "M24", "UMP9"
yuvan.Bags = "2nd Level"
yuvan.Bullets = "9.9MM", "5.5MM"
yuvan.Bullet_Proof_Vast = "2nd Level"
yuvan.Health_Kit = "Health Drink", "First Aid Kit"
yuvan.Helmet = "3rd level"
yuvan.Drone = "150KM Range"
yuvan.Shield = "3rd Level"
yuvan.Robots = "2nd Level"
print("yuvan =", yuvan.__dict__)
