# Data Projects
This is a place to share my personal projects and data explorations using Python.

### Image Classification with Garden Perennials

In this notebook I explored some machine learning techniques used in image classification - namely the torch ML library. In doing so I buillt a deep learning model to classify new images of garden perennials and the top 5 "classes" (i.e. flower species') that a new image would likely fall under.

### Anomaly Detection using Log Files

Anomaly detection has always been a subject of interest to me. In this project I extracted datestamps/timestamps from log files in order to find some insights. The crux of this project is that if an individual has an anomalous timestamp in relation to other users then that could possibly constitute something malicious. After manually performing this analysis in Part 1 of this notebook I involved Scikit-learn in Part 2 to automate recommendation on anomalous timestamps, based on the kurtosis (i.e. sharpness of a peak) of log-access data. The end result was a dataframe consisting of "high-risk" times of access, and an "anomaly score" for each suspicious timestamp.
