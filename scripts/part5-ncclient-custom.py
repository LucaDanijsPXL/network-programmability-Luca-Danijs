from ncclient import manager
import xml.dom.minidom

# Device details
DEVICE = {
    'host': '192.168.56.101',
    'port': 830,
    'username': 'cisco',
    'password': 'cisco123!',
    'hostkey_verify': False
}

def main():
    # Connect to NETCONF device
    with manager.connect(**DEVICE) as m:
        print("# Connected to device via NETCONF\n")

        # Print supported YANG models/capabilities
        print("# Supported Capabilities (YANG models):")
        for capability in m.server_capabilities:
            print(capability)

        # Define new Loopback interface configuration
        netconf_newloop = """
        <config>
            <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
                <interface>
                    <Loopback>
                        <name>2</name>
                        <description>My second NETCONF loopback</description>
                        <ip>
                            <address>
                                <primary>
                                    <address>10.1.1.1</address>
                                    <mask>255.255.255.0</mask>
                                </primary>
                            </address>
                        </ip>
                    </Loopback>
                </interface>
            </native>
        </config>
        """

        # Push configuration to the device
        netconf_reply = m.edit_config(target="running", config=netconf_newloop)
        print("\n# Edit Config Reply:")
        print(xml.dom.minidom.parseString(netconf_reply.xml).toprettyxml())

        # Verify configuration with a filtered get
        netconf_filter = """
        <filter>
            <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
                <interface>
                    <Loopback/>
                </interface>
            </native>
        </filter>
        """

        netconf_reply = m.get_config(source="running", filter=netconf_filter)
        print("\n# Get Config Reply (Loopback Interfaces):")
        print(xml.dom.minidom.parseString(netconf_reply.xml).toprettyxml())

if __name__ == "__main__":
    main()
