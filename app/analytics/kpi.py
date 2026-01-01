def calculate_kpis(df):
    df["profit"] = df["revenue"] - df["cost"]
    df["revenue_per_employee"] = df["revenue"] / df["employees"]

    return {
        "total_revenue": int(df["revenue"].sum()),
        "total_profit": int(df["profit"].sum()),
        "avg_customer_satisfaction": float(
            round(df["customer_satisfaction"].mean(), 2)
        ),
        "best_department": str(
            df.loc[df["profit"].idxmax(), "department"]
        )
    }
