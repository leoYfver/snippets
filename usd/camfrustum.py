import hou
from pxr import Usd, UsdGeom, Sdf, Gf

node = hou.pwd()
stage = node.editableStage()

camera = stage.GetPrimAtPath('/camera/camera1')
cam = UsdGeom.Camera(camera).GetCamera()
frustum = cam.frustum
corners = frustum.ComputeCornersAtDistance(15)

x = 0

for i in corners:
        sphere = UsdGeom.Sphere.Define(stage, '/sphere'+'str(x)')
        sphere.AddTranslateOp().Set(i)
        x+=1
