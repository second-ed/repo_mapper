from pathlib import Path

import pytest

from src.repo_map.io import write_file


@pytest.fixture(scope="module", autouse=True)
def get_path_to_main():
    return str(Path(__file__).parents[1].joinpath("src/repo_map/__main__.py")).replace(
        "\\", "/"
    )


@pytest.fixture(scope="module", autouse=True)
def get_mock_data_path():
    return str(Path(__file__).parents[1].joinpath("mock_data")).replace("\\", "/")


@pytest.fixture(scope="module", autouse=True)
def get_mock_data_readme_path():
    return str(Path(__file__).parents[1].joinpath("mock_data/README.md")).replace(
        "\\", "/"
    )


@pytest.fixture(scope="module", autouse=True)
def overwrite_readme(get_mock_data_readme_path):
    write_file(get_mock_data_readme_path, "# mock data\nthis is a readme for mock data")


VALID_MAP_ALL_FILES = """# generated repo map
```
└── mock_data
    ├── src
    │   ├── __init__.py
    │   └── main.py
    ├── tests
    │   └── __init__.py
    ├── README.md
    └── some.toml
```"""

VALID_MAP_PY_ONLY = """# generated repo map
```
└── mock_data
    ├── src
    │   ├── __init__.py
    │   └── main.py
    └── tests
        └── __init__.py
```"""


VALID_MAP_TOML_ONLY = """# generated repo map
```
└── mock_data
    └── some.toml
```"""


VALID_MAP_PY_MD_ONLY = """# generated repo map
```
└── mock_data
    ├── src
    │   ├── __init__.py
    │   └── main.py
    ├── tests
    │   └── __init__.py
    └── README.md
```"""

VALID_MAP_NO_SRC_DIR = """# generated repo map
```
└── mock_data
    ├── tests
    │   └── __init__.py
    ├── README.md
    └── some.toml
```"""
