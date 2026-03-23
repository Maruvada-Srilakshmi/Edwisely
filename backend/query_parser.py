import re
import pandas as pd
from data_store import uploaded_data

def extract_limit(q):
    m = re.search(r'top\s+(\d+)', q.lower())
    return int(m.group(1)) if m else None

def extract_aggregation(q):
    q = q.lower()
    if "average" in q: return "mean"
    if "sum" in q: return "sum"
    if "count" in q: return "count"
    return None

def extract_metric(query, cols):
    q = query.lower()

    # 🔥 FORCE detection
    if "mark" in q:
        return "marks"

    if "attendance" in q:
        return "attendance"

    for c in cols:
        if c.lower() in q:
            return c

    return None


def extract_sort_order(query):
    q = query.lower()

    if "ascending" in q or "lowest" in q or "increasing" in q:
        return "asc"

    if "descending" in q or "highest" in q or "decreasing" in q:
        return "desc"

    return None
  
def extract_filters(q, cols):
    filters = {}
    for c in cols:
        if c.lower() in q.lower():
            words = q.split()
            for w in words:
                if w.isdigit():
                    filters[c] = int(w)
    return filters

def parse_query(query, context):
    import pandas as pd
    from data_store import uploaded_data

    dataset = uploaded_data.get("current", "students")
    df = pd.read_csv(f"sample_data/{dataset}.csv")
    cols = df.columns.tolist()

    q = query.lower()

    # 🔥 METRIC DETECTION
    metric = None
    for c in cols:
        if c.lower() in q:
            metric = c

    if "mark" in q:
        metric = "marks"

    if "attendance" in q:
        metric = "attendance"

    # 🔥 SORT ORDER DETECTION
    sort_order = None
    if any(word in q for word in ["ascending", "lowest", "increasing"]):
        sort_order = "asc"

    if any(word in q for word in ["descending", "highest", "top"]):
        sort_order = "desc"

    # 🔥 LIMIT DETECTION
    import re
    match = re.search(r'\b(\d+)\b', q)
    limit = int(match.group(1)) if match and "top" in q else None

    return {
        "dataset": dataset,
        "filters": {},
        "metrics": metric,
        "aggregation": None,
        "limit": limit,
        "sort_order": sort_order,
        "raw_query": query  # 🔥 important
    }