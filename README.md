
# 🧰 Part 1

## 📥 Stap 1: Download VirtualBox
Download en installeer **VirtualBox** via de officiële website.

## 📦 Stap 2: Importeren van de DevCasc VM
Download de **DEVCASC VM** en importeer deze in VirtualBox.

## 🧪 Geïnstalleerde Applicaties

Hieronder zie je een overzicht van de vooraf geïnstalleerde applicaties:

![Geïnstalleerde apps](afbeeldingen/image-1.png)

## Accounts aanmaken

DEVNET Account aanmaken.

WEBEX Account aanmaken

## Afsluiten VM

## 🔒 De VM afsluiten via de GUI

1. Open het **File** menu in **VirtualBox**  
2. Kies **Close...**
3. Selecteer **Save the machine state**
4. Klik op **OK**

### Overige afsluitopties

- **Send the shutdown signal**  
  → Dit simuleert het indrukken van de aan/uit-knop van een fysieke computer.

- **Power off the machine**  
  → Dit simuleert het plotseling uittrekken van de stekker (niet aanbevolen).

---

## 🧑‍💻 De VM afsluiten via de CLI

Je kunt de VM ook afsluiten vanuit de terminal binnen de VM:

```bash
sudo shutdown -h now
```

---
## WEBEX installeren
- Download Webex voor gekozen VM

- NOTE: ik kon dit niet installeren omdat ik geen wachtwoord had

# 🧰 Part 2

## Screenshots:

![alt text](afbeeldingen/image.png)

![alt text](afbeeldingen/image-2.png)

![alt text](afbeeldingen/image-6.png)

![alt text](afbeeldingen/image-5.png)

![alt text](afbeeldingen/image-7.png)

![alt text](afbeeldingen/image-8.png)

![alt text](afbeeldingen/image-9.png)

## Info:
Het installeren van de CSR1000V was beetje verwarrend omdat ik de disk niet juist gemount kreeg maar uiteindelijk via reset werkte het wel.

Het dashboard is ook volledig toegankelijk vanuit mijn PC en niet alleen uit de VMs

IP address: 192.168.56.101

## Commands 

```bash
ping 192.168.56.101

ssh cisco@192.168.56.101

password: cisco123!
```

# 🧰 Part 3

## Scripts

![alt text](afbeeldingen/image-10.png)

Scripts 1-10 zijn de bovenstaande scripts deze kunnen perfect uitgevoerd worden en gecontrolleerd worden in het device met afhankelijk van het script

CUSTOM-SCRIPT-3B is een script dat bijvoorbeeld zoals in de oefeningen onze VLANS en subnets zet, met kleine aanpassingen worden deze dus correct gezet automatisch.

## Findings

Het is een heel krachtig en gemakkelijk gebruiksmiddel om veel en snel werk te leveren voor switches en routers te installeren of initialiseren. Dit geeft veel mogelijkheden om tegelijk en snel of zelfs apart en nauwkerig te werken. Je kan zeer makkelijk en snelle backups maken of grote configuraties maken.

# 🧰 Part 4

## Tool
Pyang is een tool om yang files leesbaarder te maken voor mensen.

### YANG-bestanden dienen voor het definiëren van data modellen voor netwerkapparatuur en -diensten. Concreet:

- Structuur beschrijven van netwerkconfiguratie
Ze geven aan welke instellingen een apparaat of service kan hebben (bijv. interfaces, IP-adressen, routing).
Voorbeeld: een YANG-model kan specificeren dat een interface een naam, type en IP-adres moet hebben.

### Standaardisatie en interoperabiliteit
- Door een gestandaardiseerd model kunnen verschillende systemen dezelfde configuratie interpreteren. Dit is vooral belangrijk bij netwerkautomatisering (bijv. via NETCONF of RESTCONF).

### Validatie van configuratie
- YANG-bestanden helpen software te controleren of configuraties correct zijn, voordat ze worden toegepast.Ondersteuning van automatisering Tools kunnen YANG gebruiken om automatisch netwerkapparaten te configureren, zonder dat een engineer alles handmatig moet invoeren.

# 🧰 Part 5

## Screenshots
![alt text](afbeeldingen/image-11.png)

![alt text](afbeeldingen/image-12.png)

![alt text](afbeeldingen/image-13.png)

![alt text](afbeeldingen/image-14.png)

![alt text](afbeeldingen/image-15.png)

```bash
<?xml version="1.0" encoding="UTF-8"?>
<rpc-reply
  xmlns="urn:ietf:params:xml:ns:netconf:base:1.0" message-id="103">
  <data>
    <interfaces
      xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
      <interface>
        <name>GigabitEthernet1</name>
        <description>Configured_by_Script</description>
        <type
          xmlns:ianaift="urn:ietf:params:xml:ns:yang:iana-if-type">ianaift:ethernetCsmacd
        </type>
        <enabled>true</enabled>
        <ipv4
          xmlns="urn:ietf:params:xml:ns:yang:ietf-ip">
        </ipv4>
        <ipv6
          xmlns="urn:ietf:params:xml:ns:yang:ietf-ip">
        </ipv6>
      </interface>
      <interface>
        <name>Loopback100</name>
        <description>Configured_by_Netmiko</description>
        <type
          xmlns:ianaift="urn:ietf:params:xml:ns:yang:iana-if-type">ianaift:softwareLoopback
        </type>
        <enabled>true</enabled>
        <ipv4
          xmlns="urn:ietf:params:xml:ns:yang:ietf-ip">
          <address>
            <ip>100.100.100.1</ip>
            <netmask>255.255.255.255</netmask>
          </address>
        </ipv4>
        <ipv6
          xmlns="urn:ietf:params:xml:ns:yang:ietf-ip">
        </ipv6>
      </interface>
      <interface>
        <name>Loopback200</name>
        <description>External_Config</description>
        <type
          xmlns:ianaift="urn:ietf:params:xml:ns:yang:iana-if-type">ianaift:softwareLoopback
        </type>
        <enabled>true</enabled>
        <ipv4
          xmlns="urn:ietf:params:xml:ns:yang:ietf-ip">
          <address>
            <ip>200.200.200.1</ip>
            <netmask>255.255.255.255</netmask>
          </address>
        </ipv4>
        <ipv6
          xmlns="urn:ietf:params:xml:ns:yang:ietf-ip">
        </ipv6>
      </interface>
    </interfaces>
  </data></rpc-reply>]]>]]>
```

![alt text](afbeeldingen/image-16.png)

![alt text](afbeeldingen/image-17.png)

![alt text](afbeeldingen/image-18.png)

![alt text](afbeeldingen/image-19.png)

![alt text](afbeeldingen/image-20.png)

![alt text](afbeeldingen/image-21.png)

![alt text](afbeeldingen/image-22.png)

![alt text](afbeeldingen/image-23.png)

![alt text](afbeeldingen/image-24.png)

```bash devasc@labvm:~/Desktop/netconf$ python3 ncclient-netconf.py
<?xml version="1.0" ?>
<rpc-reply xmlns="urn:ietf:params:xml:ns:netconf:base:1.0" xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0" message-id="urn:uuid:22732fd5-e4a0-4b8c-991c-21caf837d1e5">
	<ok/>
</rpc-reply>
```

![alt text](afbeeldingen/image-25.png)

![alt text](afbeeldingen/image-26.png)

![alt text](afbeeldingen/image-27.png)

![alt text](afbeeldingen/image-28.png)

![alt text](afbeeldingen/image-29.png)

## Important findings
Deze methode is makkelijk te gebruiken om configuraties te maken en editen. python scripts + het gebruik van AI maakt het makkelijk snel.

# 🧰 Part 6

## Screenshots
![alt text](afbeeldingen/image-30.png)

![alt text](afbeeldingen/image-31.png)

![alt text](afbeeldingen/image-32.png)

![alt text](afbeeldingen/image-33.png)

![alt text](afbeeldingen/image-34.png)

![alt text](afbeeldingen/image-35.png)

![alt text](afbeeldingen/image-36.png)

![alt text](afbeeldingen/image-37.png)

![alt text](afbeeldingen/image-38.png)

![alt text](afbeeldingen/image-39.png)

![alt text](afbeeldingen/image-40.png)

## Findings

Het gebruik maken van API is wel gemakkelijk maar wat er gebruikt is in part 5 is gemakkelijker en beter automatiseerbaar maal wel slechter leesbaar. Beide methodes zijn goed en makkelijk te gebruiken

# 🧰 LAB 4 TASK 38

## Roadblocks

Url van OSPF werkte meerdere keren niet zat een fout in.

Bij aanpassen eerst van Interface gigtabit 1 veranderde ik het IP waardoor ping en ssh niet meer werkte. Dit heeft mij enorm lang geduurd om uit te vogelen.

Github op public moeten zetten zodat de Single source of truth kan bereikt worden.


## Screenshots
![alt text](afbeeldingen/image-41.png)

## Script endpoints:
```bash
Hostname:
  PUT  /data/Cisco-IOS-XE-native:native/hostname

Interfaces:
  GET  /data/ietf-interfaces:interfaces
  PUT  /data/ietf-interfaces:interfaces/interface={name}

OSPF:
  GET  /data/.../router/Cisco-IOS-XE-ospf:ospf
  PUT  /data/.../router/Cisco-IOS-XE-ospf:ospf={id}
  ```

## Script Artchitectuur

```bash
┌─────────────┐
│   GitHub    │  ← Single Source of Truth
│(config.json)│
└──────┬──────┘
       │ HTTP GET
       ↓
┌─────────────────┐
│  Python Script  │
│ restconf-lab4.py│
└──────┬──────────┘
       │ RESTCONF PUT/PATCH
       │ (HTTPS over port 443)
       ↓
┌─────────────────┐
│  Cisco IOS-XE   │
│   CSR1000v      │
│ (192.168.56.101)│
└─────────────────┘
```

