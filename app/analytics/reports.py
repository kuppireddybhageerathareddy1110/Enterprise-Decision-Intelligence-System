def department_summary(df):
    df["profit"] = df["revenue"] - df["cost"]
    df["revenue_per_employee"] = df["revenue"] / df["employees"]

    return [
        {
            "department": str(row["department"]),
            "revenue": int(row["revenue"]),
            "cost": int(row["cost"]),
            "profit": int(row["profit"]),
            "revenue_per_employee": float(row["revenue_per_employee"])
        }
        for _, row in df.iterrows()
    ]
