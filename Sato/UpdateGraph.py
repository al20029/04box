# from Data import Data 
class UpdateGraph:
    # def UpdateGraph(InstantSpeed):
    #     Data.ListInstantSpeed.append(InstantSpeed)
    #     if(Data.MaxSpeed < InstantSpeed):
    #         Data.MaxSpeed = InstantSpeed
    
    def UpdateGraph(InstantSpeed,a):
        a.ListInstantSpeed.append(InstantSpeed)
        if(a.MaxSpeed < InstantSpeed):
            a.MaxSpeed = InstantSpeed