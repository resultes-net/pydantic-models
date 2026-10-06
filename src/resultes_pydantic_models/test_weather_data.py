import resultes_pydantic_models.weather_data as _pwd


def test_get_object_storage_input_file_path_of_shared_weather_data() -> None:
    weather_data = _pwd.GetWeatherData(
        id="c8a15e846e",
        name="Alpine",
        file_name="Alpine.csv",
        format=_pwd.WeatherDataFormat.ISO,
        user_id=None,
    )

    path = _pwd.get_object_storage_input_file_path(weather_data)

    assert path.container == "resultes-static"
    assert path.path == "weather-data/c8a15e846e.zip"


def test_get_object_storage_output_file_path_of_user_weather_data() -> None:
    weather_data = _pwd.GetWeatherData(
        id="5e0a17c3d2",
        name="My weather data",
        file_name="my-weather-data.tm2",
        format=_pwd.WeatherDataFormat.TM2,
        user_id="b4f29e7a01",
    )

    path = _pwd.get_object_storage_output_file_path(weather_data)

    assert path.container == "resultes-user-data"
    assert path.path == "b4f29e7a01/weather-data/5e0a17c3d2.zip"


def test_get_data_file_name() -> None:
    assert _pwd.get_data_file_name(_pwd.WeatherDataFormat.TM2) == "data.tm2"
    assert _pwd.get_data_file_name(_pwd.WeatherDataFormat.ISO) == "data.csv"
