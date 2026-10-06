import resultes_pydantic_models.results as _pres


def test_get_simulation_zip_path() -> None:
    assert _pres.get_simulation_zip_path("c8a15e846e") == "results/c8a15e846e.zip"


def test_get_variation_zip_path() -> None:
    assert _pres.get_variation_zip_path("5e0a17c3d2") == "results/5e0a17c3d2.zip"


def test_get_variation_dir_path() -> None:
    assert _pres.get_variation_dir_path("5e0a17c3d2") == "results/5e0a17c3d2/"


def test_get_variation_file_path() -> None:
    path = _pres.get_variation_file_path("5e0a17c3d2", "plots/temperatures.png")

    assert path == "results/5e0a17c3d2/plots/temperatures.png"
