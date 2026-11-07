
import matlab.engine
import numpy as np
from pathlib import Path

MODEL_DIR = Path(__file__).resolve().parents[1] / "models"
MODEL_NAME = "Flowshield_Prototypefinal"


def run_simulation(duration=3600):

    eng = matlab.engine.start_matlab()

    try:
        eng.addpath(str(MODEL_DIR), nargout=0)
        eng.load_system(MODEL_NAME, nargout=0)

        print("Running FlowShield simulation...")

        sim_out = eng.sim(
            MODEL_NAME,
            "StopTime",
            str(duration),
            nargout=1
        )

        eng.workspace["sim_result"] = sim_out

        # Extract bladder volume
        eng.eval(
            "volume_signal = sim_result.logsout.get('bladder_volume');",
            nargout=0
        )

        eng.eval(
            "volume_time = volume_signal.Values.Time;",
            nargout=0
        )

        eng.eval(
            "volume_data = volume_signal.Values.Data;",
            nargout=0
        )

        times = eng.eval("volume_time", nargout=1)
        volumes = eng.eval("volume_data", nargout=1)

        # Convert MATLAB arrays into NumPy arrays
        times = np.asarray(times, dtype=float).flatten().tolist()
        volumes = np.asarray(volumes, dtype=float).flatten().tolist()

        return {
            "times": times,
            "volumes": volumes,
            "initial_volume": volumes[0],
            "final_volume": volumes[-1],
            "duration": duration
        }

    finally:
        eng.quit()
