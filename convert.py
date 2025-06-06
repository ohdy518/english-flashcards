import csv
import json
import sys

def convert_csv_to_js(input_csv_path, output_js_path=None):
    """
    Reads a CSV with columns: Word, Fig. of speech, Definition
    and writes a JS file that exports an array of objects:
      { word: "...", fos: "...", def: "..." }
    If output_js_path is None, the result is printed to stdout.
    """
    # Read all rows into a list
    with open(input_csv_path, newline='', encoding='utf-8-sig') as f:
        reader = csv.DictReader(f)
        rows = list(reader)

    # Prepare the JS lines
    lines = []
    lines.append("export const words = [")
    for i, row in enumerate(rows):
        w = row.get("Word", "").strip()
        fos = row.get("Fig. of speech", "").strip()
        d = row.get("Definition", "").strip()

        # Use json.dumps to quote and escape each field correctly
        word_js = json.dumps(w, ensure_ascii=False)
        fos_js  = json.dumps(fos, ensure_ascii=False)
        def_js  = json.dumps(d, ensure_ascii=False)

        comma = "," if i < len(rows) - 1 else ""
        lines.append(f"  {{word: {word_js}, fos: {fos_js}, def: {def_js}}}{comma}")

    lines.append("];")

    output = "\n".join(lines)

    if not output_js_path:
        output_js_path = "./src/lib/wordlist.js"

    if output_js_path:
        with open(output_js_path, "w", encoding="utf-8") as out:
            out.write(output)
    else:
        print(output)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python convert.py <input.csv> [output.js]")
        sys.exit(1)

    input_csv = sys.argv[1]
    output_js = sys.argv[2] if len(sys.argv) > 2 else None
    convert_csv_to_js(input_csv, output_js)
