import xml.etree.ElementTree as ET

# Load and parse the XML file
tree = ET.parse("Metrics.xml")
root = tree.getroot()
simulation_time=10

# Variables to store packets received
packets = {
    "AP1STA1": 0,
    "AP2STA2": 0,
    "STA1AP1": 0,
    "STA2AP2": 0
}

# Locate Application_Metrics and fetch packets
for menu in root.findall(".//MENU[@Name='Application_Metrics']"):
    for table in menu.findall("TABLE"):
        for tr in table.findall("TR"):
            app_name = tr.findall("TC")[1].attrib["Value"]
            received = int(tr.findall("TC")[6].attrib["Value"])
            if app_name in packets:
                packets[app_name] = received

# Perform calculations
answer1 = (packets["AP1STA1"] + packets["AP2STA2"]) / (simulation_time*2)
answer2 = (packets["STA1AP1"] + packets["STA2AP2"]) / (simulation_time*2)

# Print results with breaks
print("Packets Per Second: ((AP1STA1 + AP2STA2)/(simulation_time*2)):", answer1)

print("Packets Per Second: ((STA1AP1 + STA2AP2)/(simulation_time*2)):", answer2)
input("Press Enter to exit...")
