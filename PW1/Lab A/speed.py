import time
import numpy as np
import decay

def simulate_pure_python(n_atoms, rate):
    atoms = n_atoms
    history = [atoms]
    import random
    while atoms > 0 and len(history) < 200:
        decayed = sum(1 for _ in range(atoms) if random.random() < rate)
        atoms -= decayed
        history.append(atoms)
    return history

n_atoms = 200000
rate = 0.4

# Замер Pure Python
t0 = time.perf_counter()
simulate_pure_python(n_atoms, rate)
t_python = time.perf_counter() - t0

# Замер NumPy (decay.py)
t0 = time.perf_counter()
decay.simulate(n_atoms, rate)
t_numpy = time.perf_counter() - t0

speedup = t_python / t_numpy if t_numpy > 0 else 0

print(f"Loop (pure Python): {t_python:.4f} s")
print(f"NumPy: {t_numpy:.4f} s")
print(f"Speed-up: {speedup:.2f}x faster")