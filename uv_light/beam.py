import pandas as pd
import pyarrow as pa

class Beam:
    def __init__(self):
        # Represent the beam with an arrow
        self.beam_pattern = pa.array(["--->", "--->", "--->", "--->"])

    def project_on(self, lens):
        # Convert pyarrow array to pandas DataFrame
        beam_frame = pd.DataFrame({'Beam': self.beam_pattern.to_pandas()})
        return lens.focus_beam(beam_frame)
