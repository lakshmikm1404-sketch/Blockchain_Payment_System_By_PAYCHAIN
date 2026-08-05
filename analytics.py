import pandas as pd

def revenue_report():
    return pd.DataFrame(
        {
            "Month": ["Jan","Feb","Mar"],
            "Revenue": [2000,4500,8000]
        }
    )