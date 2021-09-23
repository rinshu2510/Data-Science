import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from plotly import __version__
import cufflinks as cf
from plotly.offline import download_plotlyjs,init_notebook_mode,plot,iplot
init_notebook_mode(connected=True)
cf.go_offline()

# print(__version__)

df1 = pd.DataFrame(np.random.randn(100,4),columns='A B C D'.split())
print(df1.head())

df2 = pd.DataFrame({'Category':['A','B','C'],'Values':[32,43,50]})
print(df2.head())

df1.iplot()
plt.show()