import api
import pandas as pd

# --  Pull latest attack data from Torn API
faction_attacks_full = api.get("faction_attacks_full")
faction_attacks_dict = faction_attacks_full["attacks"]

# -- Convert attacks dict to DataFrame
faction_attacks = pd.DataFrame.from_dict(faction_attacks_dict)

# -- Drop stealthed / incomplete attacks
faction_attacks.dropna(inplace=True)

# -- Extract attacker/defender IDs and faction IDs
faction_attacks["attacker_id"] = faction_attacks["attacker"].apply(
    lambda x: x.get("id") if isinstance(x, dict) else None
)
faction_attacks["attacker_faction_id"] = faction_attacks["attacker"].apply(
    lambda x: x.get("faction_id") if isinstance(x, dict) else None
)
faction_attacks["defender_id"] = faction_attacks["defender"].apply(
    lambda x: x.get("id") if isinstance(x, dict) else None
)
faction_attacks["defender_faction_id"] = faction_attacks["defender"].apply(
    lambda x: x.get("faction_id") if isinstance(x, dict) else None
)
faction_attacks.drop(columns=["attacker", "defender"], inplace=True)

# -- Ensure attack IDs are strings
faction_attacks["id"] = faction_attacks["id"].astype(str)

print(faction_attacks.head())