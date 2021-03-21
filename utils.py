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