# main.py
import json
import argparse
from receipt_parser import file_io as io_mod
from receipt_parser import gpt

def sanitize_amount(data):
    """Normalize the 'amount' field by removing '$' and converting to float.

    Args:
        data: Dictionary containing receipt fields.

    Returns:
        The same dictionary, with 'amount' converted to float when possible.
    """
    amount = data.get("amount")

    if amount is None:
        return data

    if isinstance(amount, str):
        amount = amount.strip().replace("$", "").strip()

    try:
        data["amount"] = float(amount)
    except (ValueError, TypeError):
        # If conversion fails, keep original value (or set to None)
        pass

    return data

def process_directory(dirpath):
    """Process all receipt images in a directory.

    Args:
        dirpath: Path to the directory containing receipt images.

    Returns:
        A dictionary mapping each filename to the extracted receipt data.
    """
    results = {}
    for name, path in io_mod.list_files(dirpath):
        image_b64 = io_mod.encode_file(path)
        data = gpt.extract_receipt_info(image_b64)
        data = sanitize_amount(data)
        results[name] = data
    return results


def main():
    """Parse command-line arguments and run the receipt processing."""
    parser = argparse.ArgumentParser()
    parser.add_argument("dirpath")
    parser.add_argument("--print", action="store_true")
    args = parser.parse_args()

    data = process_directory(args.dirpath)
    if args.print:
        print(json.dumps(data, indent=2))

if __name__ == "__main__":
    main()

