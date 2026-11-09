import matlab.engine
import numpy as np
from pathlib import Path

MODEL_DIR = Path(__file__).resolve().parents[1] / "models"
MODEL_NAME = "Flowshield_Prototypefinal"

_eng = None  # one MATLAB engine, started on first use and reused


def _engine():
    #Start MATLAB once and reuse it for every run.
    global _eng
    if _eng is None:
        _eng = matlab.engine.start_matlab()
        _eng.addpath(str(MODEL_DIR), nargout=0)
        _eng.load_system(MODEL_NAME, nargout=0)
    return _eng


def shutdown():
    #Close the MATLAB engine (call when the app exits).
    global _eng
    if _eng is not None:
        _eng.quit()
        _eng = None


def _signal(eng, name):
    #Return (time, data) arrays for a logged signal in sim_result.logsout.
    eng.eval(f"s = sim_result.logsout.get('{name}');", nargout=0)
    times = np.asarray(eng.eval("s.Values.Time", nargout=1), dtype=float).flatten()
    data = np.asarray(eng.eval("s.Values.Data", nargout=1), dtype=float).flatten()
    return times, data


def _alert_level(urgent, warning):
    if urgent:
        return "Urgent"
    if warning:
        return "Warning"
    return "Normal"


def run_simulation(duration=3600, initial_volume=0.0):
    eng = _engine()

    # Push the GUI's initial volume into the V_t integrator for this run
    eng.set_param(
        f"{MODEL_NAME}/V_t",
        "InitialCondition",
        str(float(initial_volume)),
        nargout=0,
    )

    print("Running FlowShield simulation...")
    eng.workspace["sim_result"] = eng.sim(
        MODEL_NAME, "StopTime", str(duration), nargout=1
    )

    # Logged signals (urgent / warning / void_event must be logged in Simulink)
    times, volumes = _signal(eng, "bladder_volume")
    _, urgent = _signal(eng, "urgent")
    _, warning = _signal(eng, "warning")
    _, void_event = _signal(eng, "void_event")

    urgent_hits = np.where(urgent > 0)[0]

    return {
        "times": times.tolist(),
        "volumes": volumes.tolist(),
        "initial_volume": float(volumes[0]),
        "final_volume": float(volumes[-1]),
        "final_alert": _alert_level(urgent[-1] > 0, warning[-1] > 0),
        "peak_alert": _alert_level((urgent > 0).any(), (warning > 0).any()),
        "state": "Voiding" if void_event[-1] > 0 else "Filling",
        "time_to_urgent": float(times[urgent_hits[0]]) if urgent_hits.size else None,
        "duration": duration,
    }