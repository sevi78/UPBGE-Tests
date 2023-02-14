import bge

scene = bge.logic.getCurrentScene()
overlay_cam = scene.objects["OverlayCamera"]
main_cam = scene.objects["Camera"]
debug_text = scene.objects["DebugText"]

def addObjects(cont):
	owner = cont.owner
	adder = cont.actuators["Edit Object"]
	#adder.object = "Icosphere"
	#adder.instantAddObject()
	#obj = adder.objectLastCreated()
	
	obj = scene.addObject("Icosphere",owner,0.0)
	obj.worldPosition = [3.0,1.0,0.0]
	
	debug_string = "addObjects(cont): adding Objects: obj.visible is: " + str(obj) + ": " + str(obj.visible)
	debug_text["Text"] = debug_string
	print (debug_string)
	
def initializeMainCollection(cont):
	owner = cont.owner
	alw = cont.sensors["Always"]
	collection = cont.actuators["Collection"]
	
	# add overlay collection 
	if alw.positive:
		debug_string = "initializeMainCollection(cont): adding overlayCollection"
		debug_text["Text"] = debug_string
		print(debug_string)
		
		if not "init" in owner:
			cont.activate(collection)
			owner["init"] = True
	
def initializeOverlayCollection(cont):
	owner = cont.owner
	alw = cont.sensors["Always"]
	
	
	# add overlay collection 
	if alw.positive:
		debug_string = "initializeOverlayCollection(cont): calling addObjects(cont)"
		debug_text["Text"] = debug_string
		print (debug_string)
		
		if not "init" in owner:
			#print (dir(scene.active_camera))
			#scene.active_camera = overlay_cam
			#scene.active_camera.setViewport()
			addObjects(cont)
			#scene.active_camera = main_cam
			#scene.active_camera.setViewport()
			owner["init"] = True
	
	
	