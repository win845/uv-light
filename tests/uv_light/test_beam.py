from uv_light.beam import Beam
from uv_light.lens import Lens

def test_beam_project_on():
    actual = Beam().project_on(Lens())
    expected = "~~~|--->\n~~~|--->\n~~~|--->\n~~~|--->"
    assert actual == expected
