# -*- coding: utf-8 -*-
"""
Created on Sat Sep 21 15:24:30 2019

@author: jerem
"""
from pandas import read_csv
from matplotlib import pyplot
# load dataset
#dataset = read_csv('thirdd.csv')
dataset = read_csv('thc.csv', header=0, index_col=0)
values = dataset.values
# specify columns to plot
groups = [0, 1, 2, 3, 4]
i = 1
# plot each column
pyplot.figure()
for group in groups:
    pyplot.subplot(len(groups), 1, i)
    pyplot.plot(values[:, group])
    pyplot.title(dataset.columns[group], y=0.5, loc='right')
    i += 1
pyplot.show()
