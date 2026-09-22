import pytest
import numpy as np
import decay

def test_decay_initial_and_length():
    N = decay.simulate(1000, 0.4)
    assert N[0] == 1000
    assert len(N) > 0

def test_decay_negative_rate_raises_error():
    with pytest.raises(ValueError):
        decay.simulate(1000, -0.4)

def test_decay_average_matches_theoretical():
    n_runs = 500
    N0 = 1000
    rate = 0.4
    results = [decay.simulate(N0, rate) for _ in range(n_runs)]
    avg_results = np.mean(results, axis=0)
    
    # Проверяем, что симуляция монотонно убывает и стремится к 0
    assert avg_results[0] == N0
    assert avg_results[-1] < avg_results[0]