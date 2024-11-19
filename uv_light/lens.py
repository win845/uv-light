import pandas as pd

class Lens:
    def focus_beam(self, beam_frame):
        # Add lens symbol to the DataFrame
        beam_frame['Lens'] = '~~~|'
        # Combine Beam and Lens columns into a single string representation
        beam_frame['Projection'] = beam_frame['Lens'] + beam_frame['Beam']
        return beam_frame['Projection'].to_string(index=False, header=False)
