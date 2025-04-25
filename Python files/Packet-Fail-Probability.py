import pandas as pd

# Load the packet trace CSV (with encoding fix)
df = pd.read_csv("Packet Trace.csv", encoding="ISO-8859-1")

# Function to calculate fail probability (collided/successful)
def fail_probability(app_name, transmitter):
    filtered = df[
        (df["CONTROL_PACKET_TYPE/APP_NAME"] == app_name) &
        (df["TRANSMITTER_ID"] == transmitter)
    ]
    collided = (filtered["PACKET_STATUS"] == "Collided").sum()
    successful = filtered["PACKET_STATUS"].isin(["Successful", "Collided"]).sum()

    print(f"\n=== {app_name} from {transmitter} ===")
    print(f"Collided packets: {collided}")
    print(f"Successful packets: {successful}")

    if successful == 0:
        print("No successful packets — fail probability set to 0.0")
        return 0.0

    probability = collided / successful
    print(f"Fail Probability = {collided} / {successful} = {round(probability, 4)}")
    input("Press Enter to continue...\n")
    return round(probability, 4)

# Step-by-step calculations

# AP1STA1 and AP2STA2 (transmitted from ACCESSPOINT-3)
prob_ap1sta1 = fail_probability("AP1STA1", "ACCESSPOINT-3")
prob_ap2sta2 = fail_probability("AP2STA2", "ACCESSPOINT-4")
avg_ap = round((prob_ap1sta1 + prob_ap2sta2) / 2, 4)
print(f"Average Fail Probability (AP1STA1 & AP2STA2): ({prob_ap1sta1} + {prob_ap2sta2}) / 2 = {avg_ap}")
input("Press Enter to continue...\n")

# STA1AP1 and STA2AP2 (transmitted from STA-1 and STA-2 respectively)
prob_sta1ap1 = fail_probability("STA1AP1", "NODE-1")
prob_sta2ap2 = fail_probability("STA2AP2", "NODE-2")
avg_sta = round((prob_sta1ap1 + prob_sta2ap2) / 2, 4)
print(f"Average Fail Probability (STA1AP1 & STA2AP2): ({prob_sta1ap1} + {prob_sta2ap2}) / 2 = {avg_sta}")
input("Press Enter to exit...")
