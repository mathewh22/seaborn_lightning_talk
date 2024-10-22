import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.image as mpimg


# Read in COurt Stencil Overlay
img = mpimg.imread('court_image.png')


# Data Manipulation using Pandas
data  = pd.read_csv('NBA_2024_Shots.csv')

subset  = data[['PLAYER_NAME','SHOT_MADE', 'LOC_X','LOC_Y']]

# Select Player 
player = 'Stephen Curry'
# Pull Shot locations for a player 
sshots = subset[subset['PLAYER_NAME'] == player]

# Shot locations for Stephen Curry made shots
smakes  = sshots[sshots['SHOT_MADE']== True]


# Pass into final data frmae for mapping
[x,y]= smakes["LOC_X"], smakes["LOC_Y"]

stephframe ={'X':x,"Y":y}

sf = pd.DataFrame(stephframe)



# Use Seaborn's Histplot to create heatmap
asd = sns.histplot(x = sf["X"], y =sf["Y"],zorder = 2,alpha=.8, color= 'red' ) 

#Insert overlay image with proper dimensions
asd.imshow(img,aspect= asd.get_aspect(),extent = [-25,25,0,47] , zorder= 1)

# Present Figure     
plt.xlabel('X ')
plt.ylabel('Y ')
plt.title('Heatmap for {}'.format(player))
plt.show()  
     

#asd.get_xlim() + asd.get_ylim()