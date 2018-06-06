# -*- coding: utf-8 -*-
"""
Created on Wed May 30 11:25:15 2018

@author: erhog
"""
import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm

import numpy as np

def plot_2axis(plots=None, colors=None, axis_labels=None , x_label='x [nm]', legend=None):#TODO: Try to make like image_logScale with ax, so that plot_2axis_grid is replaced
    fig = plt.figure()
    ax1 = fig.add_subplot(111)
    for i, signal in enumerate(plots[:-1]):
        ax1.plot(signal.axes_manager[0].axis, signal, color=colors[i],
                 label=signal.metadata.General.title)
    
    ax2 = ax1.twinx()
    ax2.plot(plots[-1].axes_manager[0].axis, plots[-1], color=colors[-1],
                 label=plots[-1].metadata.General.title)
    
    if axis_labels is not None:
        ax1.set_ylabel(axis_labels[0])
        ax2.set_ylabel(axis_labels[-1])
    
    lines1, labels1 = ax1.get_legend_handles_labels()
    lines2, labels2 = ax2.get_legend_handles_labels()
    if legend is not None:
        ax2.legend(lines1 + lines2,  legend, loc=0)
    else:
        ax2.legend(lines1 + lines2,  labels1+ labels2, loc=0)
    
    ax1.set_xlabel(x_label)
    
    plt.tight_layout()
    return fig

def plot_2axis_grid(plots, nrows, ncols, colors=None, axis_labels=None , x_label='x [nm]', legend=None):#TODO: Try to make like image_logScale with ax
    fig, ax1= plt.subplots(nrows=nrows, ncols=ncols)
    ax2 = []
    
    for i, ax in enumerate(ax1.flatten()):
        signal = plots[0][i]
        ax.plot(signal.axes_manager[0].axis, signal, color=colors[0],
                 label=signal.metadata.General.title)
    
        ax2.append(ax.twinx())
        ax2[i].plot(plots[-1][i].axes_manager[0].axis, plots[-1][i], color=colors[-1],
                     label=plots[-1][i].metadata.General.title)
        
        if axis_labels is not None:
            ax.set_ylabel(axis_labels[0][i])
            ax2[i].set_ylabel(axis_labels[-1][i])
        
        lines1, labels1 = ax.get_legend_handles_labels()
        lines2, labels2 = ax2[i].get_legend_handles_labels()
        if legend is not None:
            legend = np.array(legend)
            ax2[i].legend(lines1 + lines2,  legend.T[i], loc='upper right')
        elif legend=='auto':
            ax2[i].legend(lines1 + lines2,  labels1 + labels2, loc='upper right')
        
        ax.set_xlabel(x_label)
    
    plt.tight_layout()
    return fig
    
def image_logScale(s, vmin=1, ax=None, **kwargs):
    """
    Plots a log scale image with imShow.
    s: Hyperspy Signal
    vmin: float or int
        Minimimum signal value.  All values less than vmin are replace by vmin.
    
    ax:
        Axis to plot to.
    **kwarg:
        kwargs supplied to imshow.
    """
    axX = s.axes_manager[-1].axis
    axY = s.axes_manager[0].axis
    
    if 'origin' in kwargs and kwargs['origin']=='lower':
        extent = [axX.max(), axX.min(), axY.max(), axY.min()]
    else:
        extent = [axX.min(), axX.max(), axY.max(), axY.min()]

    if ax is None:
        ax = plt.gca()
        
    img = ax.imshow(np.where(s.data < vmin,vmin,s.data),
                     extent=extent,
                     norm=LogNorm(vmin=vmin), **kwargs)
    
    ax.set_xlabel(r'{} [{}]'.format(s.axes_manager[-1].name, s.axes_manager[-1].units))
    ax.set_ylabel(r'{} [{}]'.format(s.axes_manager[0].name, s.axes_manager[0].units))

def pccolormesh(s, ax=None, vmin=None, **kwargs):
    """
    """
    axX = s.axes_manager[-1].axis
    axY = s.axes_manager[0].axis
    if ax is None:
        ax = plt.gca()
    
    if isinstance(kwargs['norm'], LogNorm):
        if vmin is None:
            print('vmin is set to 1 with LogNorm unless otherwise supplied')
            vmin = 1
        img = ax.pcolormesh(*(axX,axY), np.where(s < vmin,vmin,s.data) , **kwargs)
    else:
        img = ax.pcolormesh(*(axX,axY), s, **kwargs)