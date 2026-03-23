import pandas as pd
import uuid

def generate_csv(data):
    df = pd.DataFrame(data["table"])
    name = f"report_{uuid.uuid4().hex}.csv"
    df.to_csv(name, index=False)
    return name