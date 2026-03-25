from hardware.xray_tube import XRayTube
from hardware.detector_panel import DetectorPanel
from imaging.exposure_engine import ExposureEngine

tube = XRayTube()
detector = DetectorPanel()

engine = ExposureEngine(tube, detector)

tube.warmup()

image = engine.capture()

print("Image size:")
print(len(image), "x", len(image[0]))

print("Sample pixel:")
print(image[0][0])
