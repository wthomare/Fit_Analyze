# -*- coding: utf-8 -*-
import wx
from wx.lib.embeddedimage import PyEmbeddedImage

# ***************** Catalog starts here *******************

catalog = {}
index = []

#----------------------------------------------------------------------
align_center = PyEmbeddedImage(
    "iVBORw0KGgoAAAANSUhEUgAAABAAAAAPCAYAAADtc08vAAAABHNCSVQICAgIfAhkiAAAADpJ"
    "REFUKJFjZGRiZqAEMFGkm4GBgQWZ8//f3//EaGJkYmaEsyn1Ags2QVwuQbaZNi4YDYMRGwYU"
    "ZyYAopsYTgbXQz4AAAAASUVORK5CYII=")
index.append('align_center')
catalog['align_center'] = align_center

#----------------------------------------------------------------------
align_left = PyEmbeddedImage(
    "iVBORw0KGgoAAAANSUhEUgAAABAAAAAPCAYAAADtc08vAAAABHNCSVQICAgIfAhkiAAAADxJ"
    "REFUKJFjZGRiZqAEMFGkm4GBgYWBgYHh/7+//4lRzMjEzIghRqkX8LoAm430dQExLhoNg2ER"
    "BhRnJgDCqhhOM7rMkQAAAABJRU5ErkJggg==")
index.append('align_left')
catalog['align_left'] = align_left

#----------------------------------------------------------------------
align_right = PyEmbeddedImage(
    "iVBORw0KGgoAAAANSUhEUgAAABAAAAAPCAYAAADtc08vAAAABHNCSVQICAgIfAhkiAAAADdJ"
    "REFUKJFjZGRiZqAEMFGkm4GBgQWb4P9/f/8To5mRiZmRkVIvYHUBsS6inQtGw2DEhQHFmQkA"
    "gowYTpdfxvkAAAAASUVORK5CYII=")
index.append('align_right')
catalog['align_right'] = align_right

#----------------------------------------------------------------------
aui_style = PyEmbeddedImage(
    "iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAAABHNCSVQICAgIfAhkiAAAAMFJ"
    "REFUWIXtlrENgzAUBQ/beAQWYAcGYYIkgyWZxz2lF0CiRwJBCmKJIlGq+DV+lS1ZutO39eSq"
    "MpaU5+O+kyGX661Ka3eG932fgw+wJwmTi/gtRcCdN9u2aQWWZdEKzPOsFVjXVSsguYJz++Wc"
    "QOI6gLZtAZimKQs88WKMh0CMMQv4UxxA0zQS+DiOh4D3XiIA7wkYo2tkB2Ct/XXuvwJ1XWsF"
    "5BOQv4FhGLQCXddJ4CEE/Y+oCBSBIlAEHByNpMoLu1w1qHGIod8AAAAASUVORK5CYII=")
index.append('aui_style')
catalog['aui_style'] = aui_style

#----------------------------------------------------------------------
auto_crop_selection = PyEmbeddedImage(
    "iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAAABHNCSVQICAgIfAhkiAAAAi5J"
    "REFUWIXFlz1r20AYx/+ns4PjR7jG1IgG2tIO/QAdkyyZOvcrlECnQujWT9AtFDIF+h06dcjU"
    "KaFTxg4dWwiIBNU1d8Y0Ol0H+8TpxUKKpOgPB7Is7vfoebtHjDkcXcrplA4AzOFYe0ED0Pd9"
    "zUwIdKQ0czhr/Y3XMjxWlAP3YVScAzpSOg0/9g8z95uS2Tc3CQ0cAE5vjuKH2zAmNsC42oYT"
    "d0Gc8OXvR+hI6TNx0pgRhpebhDpS+vTmCMQJ5LgAgOHamP3tN2giLwwvNwTM4eztw08ZOHG3"
    "LjejTAjs368ffEjAyaHGwIZXWAVn4qQVeIJnd0Jzne6O9ko/Q/vfM/fKLKQ7YVXRwaWeTAZw"
    "iUNIhSBYQn57WTk579SK6eBSP3lM2PG2MB71MJuHuPL/4ddvWdoIw+tVtRgAJpMBdrwtPH86"
    "gDftw7++BQAIqSAr7rWxCjZpuHuuXeIYj3rwpn28eLYNb9rHeNSDSxzD3fNSjcrwYg+UDcHi"
    "Yo+JRz/0bB7Gb+5f32I2DyGkwuJir/0QBMESV7TKneBPGOdAECwr79V5FRT2gTIrrw+gRP9A"
    "ug80NXzoSOmf4VcAgIwkpBKQSuKV+y6R6JnDqOnJpwhu8zaeBU3BF0rE84T9TOFEVNsAC74y"
    "SCQmK1uthMC43cClWnnEnjELJ6K6MnuZyUquPfHe+5wY/ZjDWe0yLHPsHvuHmVJE3eP4Lh7J"
    "+6+VKkgrD547EaHLb8Ou9B/kXYasrB2oNQAAAABJRU5ErkJggg==")
index.append('auto_crop_selection')
catalog['auto_crop_selection'] = auto_crop_selection

#----------------------------------------------------------------------
auto_crop_selection_small = PyEmbeddedImage(
    "iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAABHNCSVQICAgIfAhkiAAAASRJ"
    "REFUOI2lkzFLw1AUhb+XdOvQiiAqgqAgLeJSWo0RG+iiOBRcXV3t6OIPEHfnQPUPFERxExRK"
    "i7gLXUSoo4hDxuQ62AsSQxPaAw8u7753OOdwrwGECWEs2+S0AJAoFK3TIFEoAJZerDhz0uo0"
    "kSgUbWZBTtkOTmtseRvM3y0y6A65vrjPRGCphcvDG957n3iNTfJ2PquAXwWKQXfIR/+Ll6dX"
    "AAqOL9/949RMxFg28VN02+KcvEnRbSf29Z+VxFhwfClVPPYbM5QqHgXHHxvqVArMqEj0qRnU"
    "dtelWi8ThAFX57cYyzY6M4kWFBpgtV7m6GyPtZ2lf2/GEiiCMODx4Znl7Vl02FIziPsFpNVp"
    "yqq7IJkziOPvrmhtmHIbzUjOxPgBMl93hZvH4+AAAAAASUVORK5CYII=")
index.append('auto_crop_selection_small')
catalog['auto_crop_selection_small'] = auto_crop_selection_small

#----------------------------------------------------------------------
circle = PyEmbeddedImage(
    "iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAAABHNCSVQICAgIfAhkiAAAANtJ"
    "REFUWIXNV8sSxCAIA/z/T67d0864PiBQ2ZpbHQkxlGKZpVAEtV53+yxSOMLDqIA+oQVUkCnA"
    "m9grRDKTIxxLAUhykcKI1RrXtARagJXQGzsIWBF433KU50fALCjaXiinoBujmHG0udQu+AeE"
    "KO/0Gtc35xkODIsbT29xvu/Ajs9tFLVe9+BAhv0a9/sl6BcySzJv90TLLYgUPq8ERDllWE7H"
    "3Ym8ECJ7Yj2FNmvOcIAozwVr0p51JbOCESGPL6UIUU/o2QsLQIkRaK6pXZB1KW1x/s8pKijq"
    "1gcd75B9JbWfpAAAAABJRU5ErkJggg==")
index.append('circle')
catalog['circle'] = circle

#----------------------------------------------------------------------
circle_small = PyEmbeddedImage(
    "iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAABHNCSVQICAgIfAhkiAAAAHxJ"
    "REFUOI2lU0EOwCAIg/r/J6u7TKMVgWXcDG2paFVRxKrWal/PQFELpyzARC4WQjSVCYyZDtbG"
    "za6FQZbMvcHBDZARERFBtDSvWqt9OshMt7DwgCmx1U6WtC/9g/VjOoq6HymaLvJewXrfiDw4"
    "WxZuAfKC9TtMh0DkhusBDWJQP2fEFKMAAAAASUVORK5CYII=")
index.append('circle_small')
catalog['circle_small'] = circle_small

#----------------------------------------------------------------------
colours = PyEmbeddedImage(
    "iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAIAAACQkWg2AAAAA3NCSVQICAjb4U/gAAAAOklE"
    "QVQokWNgIBEwMjAwXJJiwpTQefgPU5CJlQGLUvxgRGpgYWBgiNiHReJu3H9s6hkHoR8GoQaS"
    "AQBoQQZvRwyakAAAAABJRU5ErkJggg==")
index.append('colours')
catalog['colours'] = colours

#----------------------------------------------------------------------
cross = PyEmbeddedImage(
    "iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAAABHNCSVQICAgIfAhkiAAAAO9J"
    "REFUWIXNl9sOAyEIRIHu/39xU/epiXVRhltSX3ZNZOZoDCCzvGge4/MeLBdTw9C0ZV0wf6vN"
    "NW1ZF+zmFebaXE5mFRCWNhMN0yR6J5ANCCIeOQkkhuVi+f5UQqDmRNMlrILwmP8AVEB4zR8A"
    "GYiIuQoQgYiaExHxmop3Jplx2pB6AkhghbkJkIVAYk2AKAQaAwF4ITxrYYCuAQNUp2IXQFcx"
    "ggAyuQAqx13mqMYWAE2v2QKmAnhzewbiARAtLFEItS33mmcgtm151MALcWzLvcIRiP9vyzvL"
    "sdmWdzYkZlte+UI+aattecfzfKd9AzzryGWicE3pAAAAAElFTkSuQmCC")
index.append('cross')
catalog['cross'] = cross

#----------------------------------------------------------------------
empty = PyEmbeddedImage(
    "iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAIAAACQkWg2AAAAA3NCSVQICAjb4U/gAAAANElE"
    "QVQokWNgIBEwMjAw/P//H84/efIkHtUWFhZMpNpAew0sDKjuNjc3H2gnjWqgiQaSAQBRvgke"
    "qvN6jAAAAABJRU5ErkJggg==")
index.append('empty')
catalog['empty'] = empty

#----------------------------------------------------------------------
expand_selection_h = PyEmbeddedImage(
    "iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAAABHNCSVQICAgIfAhkiAAAAVFJ"
    "REFUWIXtVjFuwzAMJCmjQGrv/UH27vlB9j4gyAvykC5eCz+gewbv3rvnB93lGihCsUNqQ1Ys"
    "x0nUJgZ8AGFapOgTKVFGJAW3BN306xOBURIQwyKGpU//UwIAAEgK66etXxRrdMewL83/VoKQ"
    "uL8SnNrN19i67OQ65Tr1070SuU6PSDYExLAUVdYiY0s93nfcbJtvflFlLRKIpEAMy8f3O5Ss"
    "oeQSvlhDaQ56yRo2T29NcDEsPhK2TQzL6+caYpVArGKIKYHHWlcJPD+8AJJCEsOy228HJjEc"
    "dvstiGE5+xgOLcFQEJLCebQcPCFUI5pHywNhJAW/vUCKKpNcpwIAR2L71borrp8ruU6lqLJW"
    "vKYESAoXsxXY77bY475VuX5d8xezVdvP7YR1Gofs9HNtXXGjvlWEhC/u/d0FpzBdx6ExzhL4"
    "/ooviTW+EkwEQuMHDB37+4Mc8HwAAAAASUVORK5CYII=")
index.append('expand_selection_h')
catalog['expand_selection_h'] = expand_selection_h

#----------------------------------------------------------------------
expand_selection_v = PyEmbeddedImage(
    "iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAAABHNCSVQICAgIfAhkiAAAATtJ"
    "REFUWIXtlzGOwjAQRb8dhISCRMkN6OnpKaho9gArWho6TkBHQ4v2ADRbpaCnp88NtlyJCAnF"
    "HqqAozhoPfEmIPElS04cj59mbE9GCBmAK9KKAEDIQHBtyCqLx2mEOI1uIBwJjgdIKzpedrl3"
    "w/YHyxPOAKQVHc5f1rFR59MZwgmAtKL9afPwm3F37gThDJD1v39XubFpb3k36gDQ+vPqhmHS"
    "ihJ9Kh13kROAqUQl3Km+AIoe4Ih9DK3G6jiGvsW+Cb1JyKDQABAA+q9+rtlCQFpRlQRTJpvd"
    "59wDVbLbI9nsNr4J3yEoDUH2MWlFvvq2dZ4zBHWKlQ19JiN2Ol7/zHLPi/6WZYcNEAZd7lRf"
    "AGH9AGbsQ1n0AKdSeq3f8gyiscLEhGisNDMh4jQCAAxaE3aFXOkq9lGeXwGxGs15gJjjygAA"
    "AABJRU5ErkJggg==")
index.append('expand_selection_v')
catalog['expand_selection_v'] = expand_selection_v

#----------------------------------------------------------------------
eye = PyEmbeddedImage(
    "iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAABHNCSVQICAgIfAhkiAAAAJNJ"
    "REFUOI3NkjEOwjAQBOdsoE7pwj+gyCP4f0HBD67gDUHJUkRGhkRIlgtYyZJ13h3pzmcWIj0K"
    "Xem/ABw+C1pmfQtYiLYLKEF3ByDnDGlaH++nuq4aZBYiWmYVQx0ez0cArrfHG6R4CkTu/jqA"
    "SJPGiwSDYFjvadKet3uI3S1Y2cSGIbIZYq3Wb9wAWvX7Ve4GPAEieGRem+OF/wAAAABJRU5E"
    "rkJggg==")
index.append('eye')
catalog['eye'] = eye

#----------------------------------------------------------------------
hexagon = PyEmbeddedImage(
    "iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAAABHNCSVQICAgIfAhkiAAAALNJ"
    "REFUWIXt180NgCAMBlALG7ILU7gLGxo9aWL4a/uV6KE9Q/sAxUoU4vZlBGRyjuXMsZxIDtLs"
    "QK/ofiRaCuCuVgJhAWYrRnZkCJAm1kCaAPSMJfNfAMuHi5vvAbQGawtzIHduohCrAVaFZ5D9"
    "SFRdRKuK93JDN6FFOMABDnCAAyoA2mSOopX7H5/j0UAEImpIpBPRwkOAFmLWlEoTL2vLuRBN"
    "YRVgBln+a9aDIK8rBLCICxjaeOXhD450AAAAAElFTkSuQmCC")
index.append('hexagon')
catalog['hexagon'] = hexagon

#----------------------------------------------------------------------
msw_style = PyEmbeddedImage(
    "iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAAABHNCSVQICAgIfAhkiAAAAOhJ"
    "REFUWIVjZGRiZkAGU3c8+c9AQ5DtIcOIzGdBtzzaSoCW9jMw7HjyH9kRjLAQmLrjyf8oS37a"
    "Wg4Fy45/hIcESgj8+UcX+1EAigN+/x1gB/yjafIbdQARDvg/AA5gZGRiZpi648l/D31+BkZG"
    "whqoAf7/Z2DYcRGSFRl7Nj36H2QuQh+b0cC6k28YmAbEZiTAwsDAwPD0xfMBsp4V4gAJUfGB"
    "sf/hO4gD/vwdgDIYCgaHA778+DOwDvg7EEUgsgPoVgLhcgDjiHfAaBQMuANGo2DAQ+De6+8D"
    "5oABb5CMOgDaJBu4NAAAvuND/BvGPIIAAAAASUVORK5CYII=")
index.append('msw_style')
catalog['msw_style'] = msw_style

#----------------------------------------------------------------------
position_left = PyEmbeddedImage(
    "iVBORw0KGgoAAAANSUhEUgAAABAAAAAPCAYAAADtc08vAAAABHNCSVQICAgIfAhkiAAAAExJ"
    "REFUKJHtkzEKwDAMA0/yx/z/P7XqVOiQDmmHLDEIBEKCGyy5yHmEDyeXACIX3YlcPP2dvQkI"
    "QEblqYFRuTuZGtgIG2EpguR/33gBsoRzDlCsBR0AAAAASUVORK5CYII=")
index.append('position_left')
catalog['position_left'] = position_left

#----------------------------------------------------------------------
position_top = PyEmbeddedImage(
    "iVBORw0KGgoAAAANSUhEUgAAABAAAAAPCAYAAADtc08vAAAABHNCSVQICAgIfAhkiAAAAFJJ"
    "REFUKJHtkzEKwDAMA092H5b//ylRppRCpzhToTd50RljJEXi0U0BRQrAiqQ1W5HszIABXAkr"
    "kltQCb8E3z1By1Llev5zF4/uONkO8AtAp22caOhgKT6Nla4AAAAASUVORK5CYII=")

index.append('position_top')
catalog['position_top'] = position_top

#----------------------------------------------------------------------
ribbon = PyEmbeddedImage(
    "iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAABHNCSVQICAgIfAhkiAAAAYxJ"
    "REFUOI19krtKA0EUhr8xMcYbRIJgk87KBSsRBK0UROMi6y3Wig+wpLQTLMUHsLNSBEVCIoKd"
    "gpAyEBBMISKIiDeSmLhqxiLuZrPjeqrhXH6+c/4RoiWAX2iGKQHyR9vCryf43+D4zBLWtwTw"
    "FRJeAs0wpbEQ5+4Jql8BIl1tTu385EARCXqHB0bihIKwuxH+zdZY2xQIIRibWgSQbpEWL1Jf"
    "j+S5VH/ryQp6ssLOuvS5gItAM0w5ObtMb1eRd6ueS221O0JVq41wKKhQOAT5o21xerzHQ7GV"
    "SGeDwI630ge1mlTuoKzQHQ5RsRppPVkhtdVOTcJb+UNZ4U8XVlfmuX385LX0xUu5UStkM4oL"
    "ioAtAqDP6Vzff3N1mXHW9PYqH0kzTDk0bhDpCJE63AdgQk/wWr+s/JdAM0zZPzzt4E7oCQDO"
    "Uvu4826RJhsHR+O8Ww3Pbx6KynqDo/EmkiYbcxdpYlFBIZtRBgvZDLGoIHeR/pvAFrHVNcOU"
    "sWi9r+Cp+d7AHbYTHnElfgAFJbH0Sf7mkQAAAABJRU5ErkJggg==")
index.append('ribbon')
catalog['ribbon'] = ribbon

#----------------------------------------------------------------------
selection_panel = PyEmbeddedImage(
    "iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAABHNCSVQICAgIfAhkiAAAAHlJ"
    "REFUOI3tk8EOwzAIQx+w307Dtu9u3UsS9bamuc4Ski8GjIyZByvwJTVA20CAnvBXb5SZAHp/"
    "vla3ol9cx666FWEemAeZqc7vVmbKzAMdu8zDZqx3zThiW28KdSvydsip6VfN30LYUhJHDrof"
    "gEvibvHR4CmWv/EExjdqKKO2QxEAAAAASUVORK5CYII=")
index.append('selection_panel')
catalog['selection_panel'] = selection_panel

#----------------------------------------------------------------------
square = PyEmbeddedImage(
    "iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAAABHNCSVQICAgIfAhkiAAAAEdJ"
    "REFUWIXt1zEOACAIQ9FC9P4HNinOuhsGPyNLXxoWouRS42RnOABJGvcic8bLQHsdN9feAAAA"
    "AAAAAAAAAAAAAILf8HvABvIMCjlFTCZ2AAAAAElFTkSuQmCC")
index.append('square')
catalog['square'] = square

#----------------------------------------------------------------------
triangle = PyEmbeddedImage(
    "iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAAABHNCSVQICAgIfAhkiAAAALFJ"
    "REFUWIXVl0EOgCAMBFvq/39s8ERCyCKwIJY9EYG2M9GDqsGETbzvKCKiZsrWCHT3RaEHSPTl"
    "etsAq0INgIhZC+cZyEnVTPMvgLFwloGSHq1HLZxjoEaPno1YOMNAix7t9Vrwb6CXHp3pseDb"
    "wCg9Otuy4NcAS4/uvFnwaWCWHt2tWfBnYBU9qoEs+DKwmh7VKi34MfAVPaqZ9/JhYObPhk3q"
    "eb1t7ohKlO30eX5/Bx4qMXoN5ex1NgAAAABJRU5ErkJggg==")
index.append('triangle')
catalog['triangle'] = triangle

#----------------------------------------------------------------------
actor = PyEmbeddedImage(
    b'iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAIAAACQkWg2AAAAA3NCSVQICAjb4U/gAAAAYElE'
    b'QVQokZ2QQQrAMAgETenD9uk+rQdBihkDxpOI4+663N0m9Yy2zezFqaRodn0AJOXev7+0NAYW'
    b'fumQgRViD2+BQp5HEbZk9J+TpUMxEOeLtxZIM8hUoFjfmTZ0V+PQH0LkMaB93pTRAAAAAElF'
    b'TkSuQmCC')

#----------------------------------------------------------------------
mondrian = PyEmbeddedImage(
    b'iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAAABHNCSVQICAgIfAhkiAAAAHFJ'
    b'REFUWIXt1jsKgDAQRdF7xY25cpcWC60kioI6Fm/ahHBCMh+BRmGMnAgEWnvPpzK8dvrFCCCA'
    b'coD8og4c5Lr6WB3Q3l1TBwLYPuF3YS1gn1HphgEEEABcKERrGy0E3B0HFJg7C1N/f/kTBBBA'
    b'+Vi+AMkgFEvBPD17AAAAAElFTkSuQmCC')
index.append('mondrian')
catalog['mondrian'] = mondrian

#----------------------------------------------------------------------
