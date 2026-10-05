import enum as _enum
import typing as _tp

import pydantic as _pyd

import resultes_pydantic_models.common as _pcom
import resultes_pydantic_models.runner as _prunner

# Shared weather data live next to the systems code.
SHARED_OBJECT_STORAGE_CONTAINER = "resultes-static"
USER_UPLOADED_OBJECT_STORAGE_CONTAINER = "user-data"


@_enum.verify(_enum.UNIQUE)
class WeatherDataFormat(str, _enum.Enum):
    TM2 = "TM2"
    ISO = "ISO"


# The object store holds each weather data as a zip of the data file (named by
# `get_data_file_name`) and a readme describing it, so that users who download a
# project know which weather data it uses. Runner jobs extract it into a directory
# named `DIR_NAME`.
DIR_NAME = "selected_weather"
README_FILE_NAME = "README.md"

# ISO weather data are CSV files (like the ones checked into the systems code).
_FILE_EXTENSIONS: _tp.Final[_tp.Mapping[WeatherDataFormat, str]] = {
    WeatherDataFormat.TM2: "tm2",
    WeatherDataFormat.ISO: "csv",
}

WeatherDataName = _tp.Annotated[
    str, _pyd.StringConstraints(strip_whitespace=True, min_length=1, max_length=128)
]


class WeatherDataBase(_pyd.BaseModel):
    name: WeatherDataName
    file_name: _pcom.MaxLenStr


class GetWeatherData(WeatherDataBase):
    id: _pcom.MaxLenStr
    format: WeatherDataFormat

    # `None` means the weather data is shared between all users.
    user_id: _pcom.MaxLenStr | None


class CreateWeatherData(WeatherDataBase):
    format: _tp.Literal[WeatherDataFormat.TM2] = WeatherDataFormat.TM2
    contents: _pyd.Base64Str


def get_object_storage_input_file_path(
    weather_data: GetWeatherData,
) -> _prunner.ObjectStorageInputZipFilePath:
    container, path = _get_object_storage_container_and_path(weather_data)

    return _prunner.ObjectStorageInputZipFilePath(container=container, path=path)


def get_object_storage_output_file_path(
    weather_data: GetWeatherData,
) -> _prunner.ObjectStorageOutputZipFilePath:
    container, path = _get_object_storage_container_and_path(weather_data)

    return _prunner.ObjectStorageOutputZipFilePath(container=container, path=path)


def _get_object_storage_container_and_path(
    weather_data: GetWeatherData,
) -> tuple[str, str]:
    file_name = f"{weather_data.id}.zip"

    if weather_data.user_id is None:
        return SHARED_OBJECT_STORAGE_CONTAINER, f"weather-data/{file_name}"

    return (
        USER_UPLOADED_OBJECT_STORAGE_CONTAINER,
        f"{weather_data.user_id}/weather-data/{file_name}",
    )


def get_data_file_name(weather_data_format: WeatherDataFormat) -> str:
    extension = _FILE_EXTENSIONS[weather_data_format]

    return f"data.{extension}"
