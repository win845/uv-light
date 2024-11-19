from uv_light.lens import Lens
from uv_light.beam import Beam

if __name__ == "main":
    print(Beam().project_on(Lens()))
