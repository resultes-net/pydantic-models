OBJECT_STORAGE_CONTAINER = "resultes-results"


# The create variations job's results, used as input by the variations' jobs.
def get_simulation_zip_path(simulation_id: str) -> str:
    return f"results/{simulation_id}.zip"


def get_variation_zip_path(variation_id: str) -> str:
    return f"results/{variation_id}.zip"


# Holds the variation's single file results, like plots and the log file.
def get_variation_dir_path(variation_id: str) -> str:
    return f"results/{variation_id}/"


def get_variation_file_path(variation_id: str, relative_file_path: str) -> str:
    return f"{get_variation_dir_path(variation_id)}{relative_file_path}"
