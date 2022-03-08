import numpy as np
import matplotlib.pyplot as plt

import tikzplotlib

if __name__ == '__main__':
    x=np.arange(49)
    
    y=np.array([-59.00138158129509, 
                -43.966695525591895, 
                -52.5277642686108,
                -32.1793153104166,
                -37.81484603001339,
                -24.97787027415733,
                -20.170115700140766,
                -19.194577812051865,
                -24.267556747544734,
                -18.56846706310683,
                -24.168507205879642,
                -21.613453728913854,
                -19.833679338413056,
                -16.78310378266553,
                -15.692655896866523,
                -15.496178593312704,
                -15.23787215267857,
                -14.754095951096263,
                -12.79724037524585,
                -11.496812508420765,
                -11.593305322673082,
                -12.144980726639616,
                -11.889169042516812,
                -10.983010599192548,
                -10.751331950717917,
                -10.887445777009278,
                -10.94197566653676,
                -10.983575687515879,
                -10.315668585661115,
                -10.200188159394665,
                -10.2623815297516,
                -9.98878690162022,
                -9.664489111145294,
                -9.798550374351311,
                -9.66769644336881,
                -9.114549499466483,
                -9.259332831572362,
                -9.175694376996443,
                -9.415038345909062,
                -9.50191440403006,
                -9.36517394141991,
                -9.244892043097575,
                -9.220243263930586,
                -9.160062939634974,
                -9.293750423507198,
                -9.189954421974406,
                -9.125946744761388,
                -9.182482014624696,
                -9.135265034880312])
    
    plt.plot()
    plt.plot(x,y)
    tikzplotlib.save(plt)