def print_line_info(line, return_dict=False):
	"""
	Prints details of a line
	"""
	import numpy as np
	
	dx = line.x2-line.x1
	dy = line.y2-line.y1
	angle = np.arctan(dy/dx)
	angle_degree = angle *180/np.pi
	
	print('Start:  ({},{}) [px]'.format(line.x1, line.y1))
	print('Finish: ({},{} [px])'.format(line.x2, line.y2))
	print('Width:  {} [px]'.format(line.linewidth))
	print('dx:     {}.format(dx))
	print('dy:     {}.format(dy))
	print('Length: {} [px]'.format(line.length)
	print('Angle:  {} [rad]'.format(angle)
	print('     :  {} [degree]'.format(angle_degree)
	if return_dict:
		return {'dx': dx,
		'dy': dy,
		'length': length,
		'angle': angle,
		'angle_degree': angle_degree}

# extract_ROI_line moddified from thomasaarholt https://gist.github.com/thomasaarholt/a55c941e5dd3101c985bd2e4da7a1bc8
def extract_ROI_line(s, lineROI=None, hide=False, color="red"):
    """
    Plots a hyperspy signal and draws an interactive ROI on it on the top left tenth of the image.
    Can take a list of [x1, y1, x2, y2, linewidth] to set a known intial ROI.
    Returns a tuple of (roi, roi_signal). Use hide=True to not show the plot.
    """
    import hyperspy.api as hs

    if s.axes_manager.navigation_dimension < 2:
        x_axis = s.axes_manager[s.axes_manager.signal_indices_in_array[1]]
        y_axis = s.axes_manager[s.axes_manager.signal_indices_in_array[0]]
    else:
        x_axis = s.axes_manager[s.axes_manager.navigation_indices_in_array[1]]
        y_axis = s.axes_manager[s.axes_manager.navigation_indices_in_array[0]]

    if not lineROI:
        x1 = x_axis.axis[1]
        x2 = x_axis.axis[round(x_axis.size/10)]
        y1 = y_axis.axis[1]
        y2 = y_axis.axis[round(y_axis.size/10)]
        linewidth = (x_axis.axis[-1] - x_axis.axis[0]) / 20 + (y_axis.axis[-1] - y_axis.axis[0]) / 20
    else:
        [x1, y1, x2, y2, linewidth] = lineROI
    s.plot()
    roi = hs.roi.Line2DROI(x1, y1, x2, y2, linewidth)
    roi_signal = roi.interactive(s, color=color)
    roi_signal.plot()
    if hide:
        s._plot.close()
		
	print_line_info(roi)

    return roi, roi_signal