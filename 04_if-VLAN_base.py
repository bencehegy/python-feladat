# Create a simple IF function that compares nativeVLAN and dataVLAN values and prints result.

def compare_vlans(nativeVLAN, dataVLAN):
    if nativeVLAN == dataVLAN:
        print("The native VLAN and data VLAN are the same.")
    else:
        print("The native VLAN and data VLAN are different.")

# Example usage
nativeVLAN = 10
dataVLAN = 20

compare_vlans(nativeVLAN, dataVLAN)