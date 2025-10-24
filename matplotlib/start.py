import matplotlib.pyplot as plt
import numpy as np

x = np.array([2023,2024,2025,2026])
y1 = np.array([15,19,30,45])
y2 = np.array([20,30,40,50])
y3 = np.array([12,45,33,44])

line_style = dict(marker = "o" ,
          markersize = 5 , 
          markerfacecolor="black",
          markeredgecolor="black",
          linestyle="solid",
          linewidth=2,
          color="cyan")
#plt.plot(x,y)

#plt.show()

# PLOT CUSTOMIZATION

#plt.plot(x,y1, **line_style)  unpacking the dictionary
#plt.plot(x,y2, **line_style )
#plt.plot(x,y3, **line_style )

#plt.show()


# LABELS

plt.title("class size" , fontsize=20 , family="Arial",fontweight="bold")

plt.xlabel("year",fontsize=13, family="Arial")
plt.ylabel("students",fontsize=13,family="Arial")

plt.tick_params(axis="both", 
                colors="gray")


plt.plot(x,y1)
plt.plot(x,y2)
plt.plot(x,y3)


plt.xticks(x)
plt.show()