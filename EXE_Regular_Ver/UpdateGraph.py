"""
*******************************************************************
***  File Name      : UpdateGraph.py
***  Version        : V1.0
***  Designer       : 
***  Date           : 2022.6.14
***  Purpose       	: 
***
*******************************************************************/
"""

class UpdateGraph:
    def UpdateGraph(InstantSpeed,a):
        a.ListInstantSpeed.append(InstantSpeed)
        if(a.MaxSpeed < InstantSpeed):
            a.MaxSpeed = InstantSpeed