import numpy as np
import matplotlib.pyplot as plt
import math
import pandas as pd
from sklearn.linear_model import LinearRegression  
from sklearn.model_selection import train_test_split
from scipy.stats import pearsonr

from Labsta import drawliner

# f1=np.array([0.695,0.895,0.995,1.1,1.3,1.5,1.8,2.0,2.2,2.4,2.6,2.8,3.0,3.3,3.6,3.9,4.2,4.5])

# K1=np.array([0.329212916,0.337974684,0.338488844,0.33822335,0.332722646,0.325254582,0.316488004,0.301229508,0.291474063,0.280729702	
# ,0.27128866,0.261867905	,0.252740434,0.239015544,0.226375909,0.214330218,0.20421436,0.194111516
# ])

# phi1=np.array([27.036	,8.389,	0	,-7.917,	-28.092,	-29.189,	-39.184,	-51.84,	-62.334,	-62.791,
#               -75.423,	-77.72,	-83.243,	-93.509,	-95.895,-101.617,	-105.883,	-113.673
# ])

# drawliner(f,K,model=0,style=3,pcl='black')
# plt.xlabel('f/kHz',fontsize=12)
# plt.ylabel('K(UR/U)',fontsize=12)
# plt.title("f-K",fontsize=12)

# drawliner(f,phi,style=3,pcl='black',model=0)
# plt.xlabel('f/kHz',fontsize=12)
# plt.ylabel('φ/degree',fontsize=12)
# plt.title('f-phi',fontsize=12)

# f=np.array([1.0,	1.5	,2.0	,2.5	,3.0	,3.5	,4.0	,4.5	,5.0	,5.5	,6.0	,6.5	,7.0])


# phi=np.array([-100.8	,-106.505	,-129.6,	-144,	-133.346,	-145.943	,-172.8	,
#              -165.425	,-144,	-161.772,	-165.6	,-149.591,	-183.672])
# K=np.array([0.656441718	,0.549638056	,0.442827443,	0.367954071,	0.313971743,	0.273298429,	0.24148769,
#              0.217139853,	0.19621252,	0.179473684,	0.165350184,	0.155508698	,0.142857143])
f=np.array([1,1.1,1.2,1.5	,1.7,	2	,2.2,	2.4,	2.6,	2.8,	3	,3.5
])

phi=np.array([80.64	,73.372	,61.95	,52.06	,49.967	,43.2	,28.654	,46.524	,41.838	,39.328,	35.675,	29.748
])

K=np.array([0.67296883	,0.690415172	,0.705035971	,0.736842105,	0.752587992,	0.769350649	,0.777835588	,
            0.930729167,	0.940594059,	0.947889526,	0.9518828452	,0.968586387
])
drawliner(f,K,model=0,style=3,pcl='black')
plt.xlabel('f/kHz',fontsize=12)
plt.ylabel('K(UR/U)',fontsize=12)
plt.title("f-K",fontsize=12)

# drawliner(f,phi,style=3,pcl='black',model=0)
# plt.xlabel('f/kHz',fontsize=12)
# plt.ylabel('φ/degree',fontsize=12)
# plt.title('f-phi',fontsize=12)
plt.show()