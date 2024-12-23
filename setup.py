from setuptools import setup, find_packages

setup(
    name="Dynamic Interface Patcher",
    version="2.1.3",
    author="Cutleast",
    license="CC BY-NC-ND 4.0",
    description="A dynamic patching tool for Skyrim UI mods with strict permissions.",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "lz4",
        "pyperclip",
        "PySide6",
        "qtawesome",
        "qtpy",
        "rarfile",
        "jstyleson",
    ],
    entry_points={
        "gui_scripts": [ "dip=dynamic_interface_patcher:main" ]
    },
)
