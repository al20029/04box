from tkinter import Tk
from tkinter import ON, messagebox
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
import tkinter
import numpy as np
from UpdateGraph_test import UpdateGraph_test
from DisplayOngoingWindow import OngoingWindow
from UpdateGraph import UpdateGraph




#counter()
UpdateGraph_test()
OngoingWindow()
#Ongoing_flag=1
    # s =input()
    # UpdateGraph.UpdateGraph(int(s))   
# if Ongoing_flag == 1:
#     def repeat_func():
#         tki = OngoingWindow()
#         print(2)
#         tki.after(2000,repeat_func)
        
#     print(1)
#     tki =tkinter.Tk()   
#     fig = plt.Figure()
#     ax = fig.add_subplot(111)
#     canvas = FigureCanvasTkAgg(fig, master=tki)
#     # w = tki.winfo_screenwidth() - 515
#     # h = tki.winfo_screenheight() - 430
#     print(2)   
#     tki.after(2000,repeat_func)
#     print(3)
#     tki.mainloop()
#     print(4)