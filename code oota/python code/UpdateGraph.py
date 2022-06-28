from Data import Data 
class UpdateGraph:
    def UpdateGraph(InstantSpeed):
        Data.ListInstantSpeed.append(InstantSpeed)
        if(Data.MaxSpeed < InstantSpeed):
            Data.MaxSpeed = InstantSpeed