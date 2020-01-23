import pandas as pd
import numpy as np

"platform to be analyzed"

platform = pd.read_csv('seriesview.csv')

n = 1
order_platform=tuple(platform.head(1))
duplicate_pixels = []

while n < 18 :
    
    date04 = np.array(platform[order_platform  [n]].tolist())
    date10 = np.array(platform[order_platform [n+1]].tolist())
    date16 = np.array(platform[order_platform [n+2]].tolist())
    
    pixel = 0
    parcial = []
    while pixel < 49:
        
        x1 = date04[pixel]
        x2 = date10[pixel]
        x3 = date16[pixel]
        
        y1 = date04[pixel+1]
        y2 = date10[pixel+1]
        y3 = date16[pixel+1]        
        
        if x1==y1 and x2==y2 and x3==y3:
            parcial.append(90)
        if x1==y1 and x2==y2:
            parcial.append(50)
        else:
            parcial.append (10)
        pixel = pixel + 1
    duplicate_pixels.append(parcial)
    n = n + 3

line = ['H12V09 E','H12VO9 N','H12V10 E','H12V10 N','H12V11 E','H12V11 N',]    
duplicate_pixels =pd.DataFrame(duplicate_pixels, index= line)


import seaborn as sns
import matplotlib.pyplot as plt

fig, ax = plt.subplots (figsize=(12,3))

sns.heatmap(duplicate_pixels.iloc[:,0:50],cmap = 'gray_r', vmin=0,vmax=100, 
            linecolor='white', linewidths=2, cbar= False, 
            yticklabels = True, xticklabels = True)


"Change to the evaluated platform name"

plt.savefig ('satveg_time.jpg', format = 'jpg', dpi = 600)   
    

"reference platform"

appeears = pd.read_csv('APP_MOD13Q1.csv')
order_appeears =tuple(appeears.head(1))

n = 1
platform_divergence = []

while n < 19:
    
    platform1 =np.array(platform[order_platform [n]].tolist())
    platform2 = np.array(appeears[order_appeears[n]].tolist())

    pixel = 0
    divergence = []
    
    while pixel < 50:
        
        sample1 = platform1[pixel]
        sample2 = platform2[pixel]
        
        test1 = str(sample1 == sample2)
        test2 = str(sample1 in platform2)
        
        if test1 == 'True':
            divergence.append(10)
        if test2 =='True':
            divergence.append(40)
        else:
            divergence.append(90)
        pixel = pixel+1
        
    platform_divergence.append(divergence)
    n = n+1

line = list(order_appeears[1:])
    
platform_divergence =pd.DataFrame(platform_divergence, index = line)

fig, ax = plt.subplots (figsize=(12,5))


sns.heatmap(platform_divergence.iloc[0:9,0:50],cmap = 'gray_r', vmin=0,vmax=100, 
            linecolor='white', linewidths=2, cbar= False, 
            yticklabels = True, xticklabels = True)

"Change to the evaluated platform name"

plt.savefig ('divergence_satveg_east.jpg', format = 'jpg', dpi = 300)

fig, ax = plt.subplots (figsize=(12,5))

sns.heatmap(platform_divergence.iloc[9:18,0:50],cmap = 'gray_r', vmin=0,vmax=100, 
            linecolor='white', linewidths=2, cbar= False, 
            yticklabels = True, xticklabels = True)

"Change to the evaluated platform name"

plt.savefig ('divergence_satveg_north.jpg', format = 'jpg', dpi = 300)   



"Run if the evaluation is in the differences in error (%) between platforms"

n = 1
platform_divergence = []

while n < 19:
    
    platform1 =np.array(platform[order_platform [n]].tolist())
    platform2 = np.array(appeears[order_appeears[n]].tolist())

    pixel = 0
    divergence = []
    
    while pixel < 50:
        
        sample1 = platform1[pixel]
        sample2 = platform2[pixel]
        
        error = abs((sample1-sample2)/sample2)*100
        
        
        if error < 5:
            divergence.append(10)
        if error > 5 and error < 10:
            divergence.append(40)
        else:
            divergence.append(90)
        pixel = pixel+1
        
    platform_divergence.append(divergence)
    n = n+1

line = list(order_appeears[1:])
    
platform_divergence =pd.DataFrame(platform_divergence, index = line)

fig, ax = plt.subplots (figsize=(12,5))


sns.heatmap(platform_divergence.iloc[0:9,0:50],cmap = 'gray_r', vmin=0,vmax=100, 
            linecolor='white', linewidths=2, cbar= False, 
            yticklabels = True, xticklabels = True)

"Change to the evaluated platform name"

plt.savefig ('divergence_satveg_east.jpg', format = 'jpg', dpi = 300)

fig, ax = plt.subplots (figsize=(12,5))

sns.heatmap(platform_divergence.iloc[9:18,0:50],cmap = 'gray_r', vmin=0,vmax=100, 
            linecolor='white', linewidths=2, cbar= False, 
            yticklabels = True, xticklabels = True)

"Change to the evaluated platform name"

plt.savefig ('divergence_satveg_north.jpg', format = 'jpg', dpi = 300)   


