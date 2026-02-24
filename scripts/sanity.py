import os
import sys
import platform
from importlib.metadata import version, PackageNotFoundError

PKGS = ["numpy", "pandas", "matplotlib", "scipy", "requests", "pytest", "jupyter", "ipykernel"]

def pkg_version(name: str) -> str:
    try:
        return version(name)
    except PackageNotFoundError:
        return "NOT FOUND"

def main():
    print("=== SANITY CHECK ===")
    print("Python:", sys.version.replace("\n", " "))
    print("Platform:", platform.platform())
    print("CWD:", os.getcwd())
    print("Executable:", sys.executable)
    print("\n=== PACKAGES ===")
    for p in PKGS:
        print(f"{p}: {pkg_version(p)}")

if __name__ == "__main__":
    main()
