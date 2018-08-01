def contour_plot(pos_data, vvm_data):
    
    from matplotlib.mlab import griddata
    import matplotlib
    import matplotlib.pyplot as plt
    import numpy as np

    x_data = []
    y_data = []
    amp_data = []    

    for i in range(len(pos_data)):
        x_data.append(pos_data[i][0])
        y_data.append(pos_data[i][1])
    
        if type(vvm_data[0]) == tuple:
            amp_data.append(vvm_data[i][0])
        
        elif type(vvm_data[0]) == str:
            amp_data.append(float(vvm_data[i].split(",")[0]))
    
    pos_x_min = min(x_data)
    pos_x_max = max(x_data)
    pos_y_min = min(y_data)
    pos_y_max = max(y_data)
    
    xi = np.linspace(pos_x_min, pos_x_max, 1000)
    yi = np.linspace(pos_y_min, pos_y_max, 1000)
    zi = griddata(x_data, y_data, amp_data, xi, yi, interp = "linear")

    CS = plt.contour(xi, yi, zi, levels=[-90.5,-90,-89.5,-89], colors='black')
    plt.clabel(CS, inline =1)
    plt.xlabel("X Position (mm)")
    plt.ylabel("Y Position (mm)")
    matplotlib.rcParams['contour.negative_linestyle'] = 'solid'
    plt.xlim(pos_x_min, pos_x_max)
    plt.ylim(pos_y_min, pos_y_max)
    plt.title("Amplitude vs. Position")
    plt.show()
    