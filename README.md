
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