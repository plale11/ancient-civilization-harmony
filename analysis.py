def analyze_environment(df):
    print("\n=== Environment Types ===")
    environment_counts = df["environment_type"].value_counts()
    print(environment_counts)

    print("\nInterpretation:")
    print(
        "Environmental conditions such as river valleys, floodplains, and predictable "
        "flooding created the foundation for stable settlement and food production."
    )


def analyze_settlement(df):
    print("\n=== Settlement Types ===")
    settlement_counts = df["settlement_type"].value_counts()
    print(settlement_counts)

    print("\nInterpretation:")
    print(
        "Settlement type shows whether societies became permanent communities "
        "rather than remaining mobile hunter-gatherer groups."
    )


def analyze_food_system(df):
    print("\n=== Food Sources ===")
    print(df["food_source"].value_counts())

    print("\n=== Food Storage Systems ===")
    print(df["food_storage"].value_counts())

    print("\n=== Irrigation Systems ===")
    print(df["irrigation"].value_counts())

    print("\n=== Agriculture Systems ===")
    print(df["agriculture"].value_counts())

    print("\nInterpretation:")
    print(
        "Food production, storage, irrigation, and agriculture reveal how early "
        "civilizations moved beyond subsistence and developed stability."
    )


def analyze_community(df):
    print("\n=== Community Structures ===")
    print(df["community_structure"].value_counts())

    print("\n=== Labor Division ===")
    print(df["labor_division"].value_counts())

    print("\n=== Political Structure ===")
    print(df["political_structure"].value_counts())

    print("\nInterpretation:")
    print(
        "Community structure, labor division, and political systems suggest increasing "
        "social complexity, cooperation, and organization."
    )


def run_all_analysis(df):
    print("\n======================================")
    print(" Ancient Civilization Harmony Analysis ")
    print("======================================")

    analyze_environment(df)
    analyze_settlement(df)
    analyze_food_system(df)
    analyze_community(df)

    print("\n=== Pipeline Insight ===")
    print(
        "Environment influenced food systems; food systems supported permanent settlement; "
        "permanent settlement encouraged more complex communities, labor specialization, "
        "and political organization."
    )

    print("\n=== Overall Insight ===")
    print(
        "The dataset suggests that early river civilizations developed through a process "
        "of environmental adaptation, agricultural production, surplus storage, permanent "
        "settlement, and increasingly organized social life."
    )
