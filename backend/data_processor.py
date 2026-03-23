import pandas as pd
import os
import re
from data_store import uploaded_data

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


# =========================
# 📂 LOAD DATASET
# =========================
def load_dataset():
    name = uploaded_data.get("current", "students")
    path = os.path.join(BASE_DIR, "sample_data", f"{name}.csv")
    return pd.read_csv(path)


# =========================
# 🔥 MAIN PROCESS FUNCTION
# =========================
def process_data(query, raw_query):
    df = load_dataset()
    q = raw_query.lower()

    # =========================
    # 🔥 ADVANCED FILTERS (>, <, =, above, below)
    # =========================
    for col in df.columns:
        col_lower = col.lower()

        if col_lower in q:

            # 🔹 Comparison operators
            match = re.search(rf"{col_lower}\s*(>=|<=|>|<|=)\s*(\d+)", q)

            if match:
                operator = match.group(1)
                value = float(match.group(2))

                if operator == ">":
                    df = df[df[col] > value]
                elif operator == "<":
                    df = df[df[col] < value]
                elif operator == ">=":
                    df = df[df[col] >= value]
                elif operator == "<=":
                    df = df[df[col] <= value]
                elif operator == "=":
                    df = df[df[col] == value]

            # 🔹 Natural language (above / below)
            elif "above" in q or "greater than" in q:
                val_match = re.search(rf"{col_lower}.*?(\d+)", q)
                if val_match:
                    value = float(val_match.group(1))
                    df = df[df[col] > value]

            elif "below" in q or "less than" in q:
                val_match = re.search(rf"{col_lower}.*?(\d+)", q)
                if val_match:
                    value = float(val_match.group(1))
                    df = df[df[col] < value]

            # 🔹 Equality fallback (text-based filters)
            else:
                for val in df[col].unique():
                    if str(val).lower() in q:
                        df = df[df[col] == val]

    # =========================
    # 🔍 METRIC DETECTION
    # =========================
    metric = None

    for col in df.columns:
        if col.lower() in q:
            metric = col

    if "mark" in q:
        metric = "marks"

    if "attendance" in q:
        metric = "attendance"

    # fallback → last numeric column
    if not metric:
        numeric_cols = df.select_dtypes(include=['int64', 'float64']).columns
        if len(numeric_cols) > 0:
            metric = numeric_cols[-1]

    # =========================
    # 🔃 SORT ORDER DETECTION
    # =========================
    sort_order = None

    if any(word in q for word in ["ascending", "lowest", "increasing"]):
        sort_order = "asc"

    elif any(word in q for word in ["descending", "highest", "top"]):
        sort_order = "desc"

    # =========================
    # 🔢 LIMIT DETECTION (FIXED)
    # =========================
    limit = None

    match = re.search(r'\b(\d+)\b', q)
    if match:
        number = int(match.group(1))

        # 🚫 Avoid treating filter numbers as limit
        if any(word in q for word in ["top", "first", "top students"]):
            limit = number

    # =========================
    # 🔥 APPLY SORTING
    # =========================
    if metric and sort_order:
        df = df.sort_values(by=metric, ascending=(sort_order == "asc"))

    # =========================
    # 🔥 APPLY LIMIT
    # =========================
    if limit:
        df = df.head(limit)

    # =========================
    # 📊 RETURN RESULT
    # =========================
    return {
        "table": df.to_dict(orient="records"),
        "summary": None
    }