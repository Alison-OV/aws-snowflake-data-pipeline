from src.extract import run_extract
from src.transform import run_transform
from src.load import run_load


def main():
    print("Starting data pipeline...")

    print("Extract phase started")
    run_extract()

    print("Transform phase started")
    run_transform()

    print("Load phase started")
    run_load()

    print("Data pipeline finished successfully")


if __name__ == "__main__":
    main()
