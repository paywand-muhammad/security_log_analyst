import csv
Data = []
failed_counter = {}
with open("server_log.txt")as file:
    for line in file:
        Date,Address,Status,Bytes = line.rstrip().split(" - ")
        Info = {"IP": Address, "Status": Status, "Bytes": Bytes}
        if Status == "STATUS: FAILED":
            Data.append(Info)

            if Address not in failed_counter:
                failed_counter[Address] = 1
            else:
                failed_counter[Address] += 1
for Info in sorted(Data, key=lambda x:x["IP"]):
    print(f"{Info['IP']} - {Info['Status']} - {Info['Bytes']}")
for ip, score in failed_counter.items():
    if score >= 3:
        rsta = []
        with open("threat_report.csv", "w", newline="") as life:     
            rsta = csv.DictWriter(life, fieldnames=["IP", "Status", "Bytes"])
            attacker_info = [Info for Info in Data if Info["IP"] == ip][0]
            rsta.writerow(attacker_info)