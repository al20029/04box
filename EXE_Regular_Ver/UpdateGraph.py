"""
*******************************************************************
***  File Name      : UpdateGraph.py
***  Version        : V1.1
***  Designer       : 太田峻輔
***  Date           : 2022.6.14
***  Purpose       	: 渡された瞬間Wi-Fi速度データをグラフに追加し更新する
*******************************************************************/
"""

"""
*******************************************************************
***  Class Name     : UpdateGraph
***  Designer       : 太田峻輔
***  Date           : 2022.6.14
***  Purpose       	: 渡された瞬間Wi-Fi速度データをグラフに追加し更新する
*******************************************************************/
"""

class UpdateGraph:

    """
    *******************************************************************
    ***  Function Name  : UpdateGraph
    ***  Designer       : 太田峻輔
    ***  Date           : 2022.6.21
    ***  Purpose       	: 渡された瞬間Wi-Fi速度データをグラフに追加し更新する
    *******************************************************************/
    """

    def UpdateGraph(InstantSpeed,a):
        a.ListInstantSpeed.append(InstantSpeed)
        if(a.MaxSpeed < InstantSpeed):
            a.MaxSpeed = InstantSpeed