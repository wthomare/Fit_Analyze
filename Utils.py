# -*- coding: utf-8 -*-

import images
import wx

def getErrorInfo(exc_info):
    import traceback
    errMsg = str(exc_info[1])
    errMsg += "\n\n-------------------\n"
    if exc_info[0] is not None:
        errMsg += "Error : %s" %exc_info[0] + "\n"
    if exc_info[1] is not None:
        errMsg += "Msg : %s" %exc_info[1] + "\n"
    if exc_info[2] is not None:
        errMsg += "Trace :\n"
        for el in traceback.extract_tb(exc_info[2]):
            errMsg = errMsg + str(el) + "\n"
    return errMsg

   
    
def CreateBitmap(imgName, x=48, y=47):
    """
    Import and convert an embedded image into a bitmap image
    """
    bmp = getattr(images, imgName).Bitmap
    bmp = scale_bitmap(bmp, x, y)
    return bmp

def scale_bitmap(bitmap, width, height):
    """
    rescale an bitmap image to a given width and heigth
    """
    image = bitmap.ConvertToImage()
    image = image.Scale(width, height, wx.IMAGE_QUALITY_HIGH)
    result = wx.Bitmap(image)
    return result