import bge
scene = bge.logic.getCurrentScene()

overlay_cam = scene.objects["OverlayCamera"]
main_cam = scene.objects["Camera"]
debug_text = scene.objects["DebugText"]

def setZoom(cont):
	wu = cont.sensors["MouseWU"]
	wd= cont.sensors["MouseWD"]
	if wu.positive:
		main_cam.ortho_scale += 1
	if wd.positive:
		main_cam.ortho_scale -= 1
	
	debug_string = "CameraHandler.setZoom(cont): main_cam.ortho_scale is: " + str(main_cam.ortho_scale)
	debug_text["Text"] = debug_string	
	print(debug_string)


def switchCameraView(cont):
	mb = cont.sensors["MouseMB"]
	
	if mb.positive :
		if scene.active_camera == main_cam:
			scene.active_camera = overlay_cam
		else:
			scene.active_camera = main_cam
			
		debug_string = "CameraHandler.switchCameraView(cont), active Camera is: " + str(scene.active_camera)
		debug_text["Text"] = debug_string
