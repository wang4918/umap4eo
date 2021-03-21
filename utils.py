from osgeo import gdal
import numpy as np
import glob

def get_tif_as_array(path):
    s2 = gdal.Open(path)
    arr = []
    for i in range(1,s2.RasterCount+1):
        arr.append(np.array(s2.GetRasterBand(i).ReadAsArray()).flatten())

    return np.array(arr).T

def get_s2_tif_path(year, month, locid):
    return "C:/Users/QA/Documents/umap4eo/data/sentinel-2/{locid}/{locid}_{year}_{month}.tif".format(locid=locid[4:], year=year, month=month)


def get_planet_tif_path(year, month, locid):
    return glob.glob("C:/Users/QA/Documents/umap4eo/data/planet/{locid}/L3H-SR/{year}-{month}*".format(locid=locid, year=year, month=month))

def get_monthly_stack(year, month, locid):
    pathlist = get_planet_tif_path(year, month, locid)
    pathlist.append(get_s2_tif_path(year, month, locid))

    arrlist = []

    for path in pathlist:
        arrlist.append(get_tif_as_array(path))

    return np.hstack(arrlist)





#from utils import *

#monthlystack = get_monthly_stack("2018", "04", "10N/1311_3077_13")

#sns.set(style='white', rc={'figure.figsize':(10,8)})
#standard_embedding = umap.UMAP(random_state=42).fit_transform(monthlystack)

#plt.scatter(standard_embedding[:, 0], standard_embedding[:, 1],  s=0.1, cmap='Spectral');

#labels = hdbscan.HDBSCAN(
#    min_samples=10,
#    min_cluster_size=5000,
#).fit_predict(standard_embedding)
#plt.scatter(standard_embedding[:, 0], standard_embedding[:, 1], c = labels,  s=0.1, cmap='Spectral')