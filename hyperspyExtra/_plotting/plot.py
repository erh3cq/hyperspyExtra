# -*- coding: utf-8 -*-
"""
Created on Wed May 30 11:25:15 2018

@author: erhog
"""
import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm

import numpy as np

def abc(axs, pos=[-.2, 1], end=')', title=False, **kwargs):
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    axs = axs.flatten()
    for i, ax in enumerate(axs):
        label = alpha[i]+end
        if title:
            ax.set_title(label, **kwargs)
        else:
            ax.text(pos[0], pos[1], label, transform=ax.transAxes,
                    fontweight='bold', va='top', ha='right', **kwargs)

def plot_2axis(plots, fig=None, ax=None, colors=None, axis_labels=None , x_label='x [nm]', legend=None, tight_layout=True):#TODO: Try to make like image_logScale with ax, so that plot_2axis_grid is replaced
    if fig is None:
        fig = plt.figure()
    if ax is None:
        ax = fig.add_subplot(111)
    
    for i, signal in enumerate(plots[:-1]):
        ax.plot(signal.axes_manager[0].axis, signal, color=colors[i],
                 label=signal.metadata.General.title)
    
    axR = ax.twinx()
    axR.plot(plots[-1].axes_manager[0].axis, plots[-1], color=colors[-1],
                 label=plots[-1].metadata.General.title)
    
    if axis_labels is not None:
        ax.set_ylabel(axis_labels[0])
        axR.set_ylabel(axis_labels[-1])
    
    lines1, labels1 = ax.get_legend_handles_labels()
    lines2, labels2 = axR.get_legend_handles_labels()
    if legend=='auto':
        axR.legend(lines1 + lines2,  labels1+ labels2, loc=0)
    elif legend is not None:
        axR.legend(lines1 + lines2,  legend, loc=0)
    
    ax.set_xlabel(x_label)
    
    if tight_layout:
        plt.tight_layout()
    
    if fig is None and ax is None:
        return fig, [ax, axR]

def plot_2axis_grid(plots, fig, axs, tight_layout=True, **kwargs):#TODO: Try to make like image_logScale with ax
    for i, ax in enumerate(axs.flatten()):
        plot_2axis([VP_max_E[i], HAADF[i]], fig=fig, ax=ax, **kwargs)
    if tight_layout:
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