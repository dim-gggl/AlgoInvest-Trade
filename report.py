from utils import load_actions
import csv


def content_of(row: dict) -> str:
    if not isinstance(row, dict):
        raise TypeError(f"{row=} {type(row)}")
    return row.values()


def get_file_name(file_path: str) -> str:
    return file_path.split('/')[-1] if '/' in file_path else file_path


def get_cleared_file_path(file_name: str) -> str:
    return f"data/scanned/CLEARED_{file_name}"


def get_report_file_path(file_name: str) -> str:
    return f"data/scanned/REPPORT_{file_name}"


def process_dirty_data(file_path: str) -> list:
    _, dirty_data = load_actions(file_path=file_path)
    # Return a list of dictionary rows
    return [content_of(row) for row in dirty_data]


def get_newlines(file_path: str, processed_dirty_data: list) -> list:
    newlines = []
    with open(file_path, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            if content_of(row) not in processed_dirty_data:
                newlines.append(content_of(row))
    return newlines


def write_cleared_file(cleared_file_path: str, newlines: list):
    with open(cleared_file_path, 'w') as file:
        writer = csv.DictWriter(file, ['name', 'price', 'profit'])
        writer.writerows(newlines)


def write_report_file(report_file_path: str, processed_dirty_data: list):
    with open(report_file_path, 'w') as r:
        try:
            r.writelines(processed_dirty_data)
        except TypeError:
            # En cas de TypeError (par exemple, si un dict est passé), on convertit chaque élément en chaîne formatée
            formatted_lines = [
                f"{row.get('name','')},{row.get('price','')},{row.get('profit','')}\n" if isinstance(row, dict) else str(row) for row in processed_dirty_data]
            r.writelines(formatted_lines)


def report_corrupted_data(file_path="data/Dataset_1.csv"):
    file_name = get_file_name(file_path)
    cleared_file_path = get_cleared_file_path(file_name)
    report_file_path = get_report_file_path(file_name)

    processed_dirty_data = process_dirty_data(file_path)
    newlines = get_newlines(file_path, processed_dirty_data)

    write_cleared_file(cleared_file_path, newlines)
    write_report_file(report_file_path, processed_dirty_data)


if __name__ == "__main__":
    report_corrupted_data()
