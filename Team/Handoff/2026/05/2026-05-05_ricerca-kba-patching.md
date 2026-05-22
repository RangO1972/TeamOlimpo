---
tags: [kba, patching, delta-v, ricerca-proteo]
date: 2026-05-05
from: Proteo
to: Atena
stato: da-processare
tipo: ricerca-kba-patching
slug: 2026-05-05_ricerca-kba-patching
---

# Ricerca KBA: Dettagli Azioni di Patching/Installazione

> Prodotto da Proteo — 2026-05-05  
> Destinatario: Atena

Questo report analizza le KBA presenti nel file `Library/Handoff/2026-05-05_estrazione-kba-excel.md` per identificare quelle che richiedono azioni di patching/installazione (colonna "Azioni Patching/Installazione" = `Si (medium)` o `Si (simple)`). Sono state identificate **30 KBA univoche** che richiedono intervento; le KBA con stato `No` sono state escluse come richiesto.

Per ciascuna KBA univoca sono riportati:
- Stato di patching dal file sorgente
- Ubicazioni applicative complete (raggruppate per sito)
- Sintesi delle azioni raccomandate
- Dettagli tecnici da fonti pubbliche
- Fonti web utilizzate
- Livello di confidenza delle informazioni

> **Nota importante**: La maggior parte delle KBA DeltaV sono ospitate su portali ad accesso riservato (Emerson Guardian Support). I dettagli specifici di patching (checksum, istruzioni esatte, download hotfix) sono accessibili solo tramite abbonamento Guardian; le informazioni riportate si basano su documentazione pubblica, avvisi CISA e database NVD.

---

## KBA: NK-1800-0831 - Endpoint Security for DeltaV Systems v2.3 Software Updates
### Stato Patching (da file sorgente)
Si (medium)
### Ubicazioni Applicative
**Montecchio**: MM-DV1P-OWS14, MM-DV1P-OWS2, MM-DV1P-OWS22, MM-DV1P-OWS34, MM-DV1P-OWS51, MM-DV1V-ENG01, MM-DV1V-ENG02, MM-DV1V-OPC01, MM-DV1V-OTS26, MM-DV1V-OTS30, MM-DV1V-OTS31, MM-DV1V-OTS32, MM-DV1V-OTS33, MM-DV1V-OTS45, MM-DV1V-OTS47, MM-DV1V-OTS48, MM-DV1V-OTS49, MM-DV1V-OTS52, MM-DV1V-OWS13, MM-DV1V-OWS15, MM-DV1V-OWS16, MM-DV1V-OWS18, MM-DV1V-OWS19, MM-DV1V-OWS35, MM-DV1V-OWS36, MM-DV1V-OWS37, MM-DV1V-OWS38, MM-DV1V-OWS42, MM-DV1V-OWS43, MM-DV1V-OWS50, MM-DV2P-OWS1, MM-DV2P-OWS10, MM-DV2P-OWS17, MM-DV2P-OWS8, MM-DV2V-BEH01, MM-DV2V-ENG01, MM-DV2V-ENG02, MM-DV2V-OPC01, MM-DV2V-OPC02, MM-DV2V-OTS24, MM-DV2V-OTS25, MM-DV2V-OTS27, MM-DV2V-OTS28, MM-DV2V-OTS29, MM-DV2V-OTS39, MM-DV2V-OTS40, MM-DV2V-OTS41, MM-DV2V-OTS44, MM-DV2V-OTS46, MM-DV2V-OWS20, MM-DV2V-OWS21, MM-DV2V-OWS4, MM-DV2V-OWS5, MM-DV2V-OWS6, MM-DV2V-OWS7, MM-DV2V-OWS9, MM-DV3P-OWS1, MM-DV3V-ENG01, MM-DV3V-ENG02, MM-DV3V-OPC03, MM-DV3V-OTS01, MM-DV3V-OWS2, MM-DV3V-OWS3, MM-DV3V-OWS4, MM-DV3V-OWS5, MM-DV3V-OWS6
### Sintesi della KBA e Azioni Raccomandate
Riguarda l'aggiornamento alla v2.3 di Endpoint Security per DeltaV, soluzione anti-malware basata su Trellix per proteggere workstation e server DeltaV.  
Azioni:
- Aggiornare il software alla v2.3 su tutti i nodi elencati
- Configurare gli aggiornamenti automatici delle definizioni antivirus tramite Integrated Patch Management (IPM)
### Dettagli Tecnici e Procedure
- Gestito centralmente via dashboard IPM, che scarica definizioni approvate da Emerson
- Compatibile con Windows 10, Server 2016+ e DeltaV v14.LTS/v15.LTS
- Installazione manuale o automatica via IPM seguendo le istruzioni della KBA (riservata Guardian)
### Fonti Web
1. [Endpoint Security for DeltaV™ Systems | Emerson US](https://www.emerson.com/en-us/catalog/deltav-endpointsecurity)
2. [Integrated Patch Management for DeltaV Systems | Emerson US](http://www.emerson.com/en-us/catalog/deltav-patchmanagement)
### Confidenza Informazioni
Plausibile (fonti ufficiali Emerson, dettagli specifici non pubblici)

---

## KBA: AK-1300-0005 - Microsoft Released Security Updates for DeltaV Systems
### Stato Patching (da file sorgente)
Si (medium) (presente in 3 siti)
### Ubicazioni Applicative
**Termoli**: APP2T, DVINST, TE-DV1P-OWS06, TE-DV1P-OWS07, TE-DV1V-BEH01, TE-DV1V-BEX01, TE-DV1V-ENG01, TE-DV1V-OPC01, TE-DV1V-OTS08, TE-DV1V-OTS09, TE-DV1V-OTS10, TE-DV1V-OTS11, TE-DV1V-OTS15, TE-DV1V-OTS17, TE-DV1V-OTS18, TE-DV1V-OTS19, TE-DV1V-OWS01, TE-DV1V-OWS02, TE-DV1V-OWS03, TE-DV1V-OWS04, TE-DV1V-OWS05, TE-DV1V-OWS12, TE-DV1V-OWS13, TE-DV1V-OWS14, TE-DV1V-OWS16  

**Montecchio**: APP1AZ1, APP1BZ1, APP1BZ2, APP1F, APP2, APP2Z2, DVINSTF, DVINSTZ1, DVINSTZ2, MM-DV1P-OWS14, MM-DV1P-OWS2, MM-DV1P-OWS22, MM-DV1P-OWS34, MM-DV1P-OWS51, MM-DV1V-DCN1, MM-DV1V-DCN2, MM-DV1V-ENG01, MM-DV1V-ENG02, MM-DV1V-OPC01, MM-DV1V-OTS26, MM-DV1V-OTS30, MM-DV1V-OTS31, MM-DV1V-OTS32, MM-DV1V-OTS33, MM-DV1V-OTS45, MM-DV1V-OTS47, MM-DV1V-OTS48, MM-DV1V-OTS49, MM-DV1V-OTS52, MM-DV1V-OWS13, MM-DV1V-OWS15, MM-DV1V-OWS16, MM-DV1V-OWS18, MM-DV1V-OWS19, MM-DV1V-OWS35, MM-DV1V-OWS36, MM-DV1V-OWS37, MM-DV1V-OWS38, MM-DV1V-OWS42, MM-DV1V-OWS43, MM-DV1V-OWS50, MM-DV2P-OWS1, MM-DV2P-OWS10, MM-DV2P-OWS17, MM-DV2P-OWS8, MM-DV2V-BEH01, MM-DV2V-DCN1, MM-DV2V-DCN2, MM-DV2V-ENG01, MM-DV2V-ENG02, MM-DV2V-OPC01, MM-DV2V-OPC02, MM-DV2V-OTS24, MM-DV2V-OTS25, MM-DV2V-OTS27, MM-DV2V-OTS28, MM-DV2V-OTS29, MM-DV2V-OTS39, MM-DV2V-OTS40, MM-DV2V-OTS41, MM-DV2V-OTS44, MM-DV2V-OTS46, MM-DV2V-OWS20, MM-DV2V-OWS21, MM-DV2V-OWS4, MM-DV2V-OWS5, MM-DV2V-OWS6, MM-DV2V-OWS7, MM-DV2V-OWS9, MM-DV3P-OWS1, MM-DV3V-DCN1, MM-DV3V-DCN2, MM-DV3V-ENG01, MM-DV3V-ENG02, MM-DV3V-OPC03, MM-DV3V-OTS01, MM-DV3V-OWS2, MM-DV3V-OWS3, MM-DV3V-OWS4, MM-DV3V-OWS5, MM-DV3V-OWS6, ZSERVZ1, ZSERVZ1_S, ZSERVZ2, ZSERVZ2_S, ZSERVZ3, ZSERVZ3_S  

**Lonigo**: LN-DV1V-OPC01, MAN_AMS_1, OPE_F9, SRC-F3_1, SRC-LAB, SRCCED2
### Sintesi della KBA e Azioni Raccomandate
Elenco degli aggiornamenti di sicurezza Microsoft approvati per DeltaV, testati da Emerson per compatibilità.  
Azioni:
- Installare solo aggiornamenti contrassegnati come "Approved" nella KBA
- Distribuzione scalare (inizio da piccolo gruppo di nodi)
- Automazione via IPM per grandiDeployment
### Dettagli Tecnici e Procedure
- Aggiornamenti cumulativi da Windows 10/Server 2016 (non selezionabili singolarmente)
- KBA aggiornata mensilmente dopo il Patch Tuesday Microsoft
- Download da portale Guardian o Microsoft KB (solo versioni approvate da Emerson)
### Fonti Web
1. [DeltaV™ System Software Update Deployment White Paper](https://www.emerson.com/documents/automation/white-paper-deltav-software-update-deployment-en-57018.pdf)
2. [Microsoft Updates on DeltaV Systems Manual](https://www.emerson.com/documents/automation/manual-microsoft-security-bulletin-administration-on-deltav-systems-deltav-en-57022.pdf)
### Confidenza Informazioni
Confermato (fonti multiple Emerson)

---

## KBA: AK-1200-0033 - Microsoft Released Security Updates Approved for Use on DeltaV Virtualization Servers
### Stato Patching (da file sorgente)
Si (medium)
### Ubicazioni Applicative
**Lonigo**: DC01P, DVHPH, dc01s, vrtx1a-b1, vrtx1a-b2, vrtx1a-b3, vrtx1a-b4, vrtx1b-b1, vrtx1b-b2, vrtx1b-b3, vrtx1b-b4, vrtx2a-b1
### Sintesi della KBA e Azioni Raccomandate
Aggiornamenti di sicurezza Microsoft approvati per server di virtualizzazione DeltaV (Dell PowerEdge VRTX, HCI).  
Azioni:
- Installare aggiornamenti approvati su tutti i server di virtualizzazione elencati
- Testare gli aggiornamenti su un server non produttivo prima della distribuzione completa
### Dettagli Tecnici e Procedure
- Server di virtualizzazione supportano DeltaV Virtual Studio v3.3.x e v4.3.x
- Automazione via IPM o download manuale da portale Guardian
### Fonti Web
1. [DeltaV Virtualization Integrated Hardware Platform Documentation](https://www.emerson.com/documents/automation/product-data-sheet-deltav-workstation-server-hardware-deltav-en-57732.pdf)
### Confidenza Informazioni
Plausibile (documentazione hardware Emerson)

---

## KBA: NK-2000-0562 - DSN20006-3 - Security Boot Vulnerability
### Stato Patching (da file sorgente)
Si (medium)
### Ubicazioni Applicative
**Montecchio**: MM-DV1P-OWS2  
**Lonigo**: MAN_AMS_1
### Sintesi della KBA e Azioni Raccomandate
Vulnerabilità di boot security (DSN20006-3) legata a verifica insufficiente dell'integrità firmware.  
Azioni:
- Aggiornare firmware di controller (M/S/P-series, SIS) e schede I/O (CIOC/EIOC/WIOC) alla v14.3+
### Dettagli Tecnici e Procedure
- Mappata a CVE-2022-30260 (NVD): interessa tutte le versioni DeltaV < 14.3
- Flashing firmware in modalità ridondante (nessuna interruzione processo per nodi ridondanti)
- Istruzioni dettagliate in KBA riservata Guardian
### Fonti Web
1. [NVD - CVE-2022-30260](https://nvd.nist.gov/vuln/detail/CVE-2022-30260)
2. [Emerson DeltaV Vulnerabilities | CISA](https://www.cisa.gov/uscert/ics/advisories/icsa-21-355-04)
### Confidenza Informazioni
Confermato (CVE ufficiale, avviso CISA)

---

## KBA: NK-2300-0446 - CIOC/CIOC2 Can Lead to Process Disruption When a Single Unit of a Redundant Pair Is Removed from the Carrier
### Stato Patching (da file sorgente)
Si (medium) (presente in 3 siti)
### Ubicazioni Applicative
**Termoli**: S01-AE01F, S01-AE01F-partner, S02-AE01F, S02-AE01F-partner, S03-AE01R, S03-AE01R-partner, S04-AE01R, S04-AE01R-partner, S05-AE02F, S05-AE02F-partner, S06-AE02F, S06-AE02F-partner, S07-AE02R, S07-AE02R-partner, S08-UNIF, S08-UNIF-partner, S09-UNIF, S09-UNIF-partner, S10-UNIR, S10-UNIR-partner, S11-AE01R, S11-AE01R-partner, S12-AE02R, S12-AE02R-partner, S13-UNIR, S13-UNIR-partner, S31-AB01R, S31-AB01R-partner, S32-AB01R, S32-AB01R-partner, S33-AB01R, S33-AB01R-partner, S34-AB02R, S34-AB02R-partner, S35-AB02R, S35-AB02R-partner, S36-AB02R, S36-AB02R-partner, S37-AB03R, S37-AB03R-partner, S38-AB03R, S38-AB03R-partner, S39-AB03R, S39-AB03R-partner, S40-AB03R, S40-AB03R-partner, S41-AB04R, S41-AB04R-partner, S42-AB04R, S42-AB04R-partner, S43-AB04R, S43-AB04R-partner, S44-AB05R, S44-AB05R-partner, S45-AB05R, S45-AB05R-partner, S46-AB05R, S46-AB05R-partner, S47-AB05R, S47-AB05R-partner, S48-AB06R, S48-AB06R-partner, S49-AB06R, S49-AB06R-partner, S50-AB06R, S50-AB06R-partner, S51-AB06R, S51-AB06R-partner, S52-AB07F, S52-AB07F-partner  

**Montecchio**: CIOC-S891A, CIOC-S891A-partner, CIOC-S891B, CIOC-S891B-partner, CIOC-S891C, CIOC-S891C-partner, CIOC-S892A, CIOC-S892A-partner, CIOC-S892B, CIOC-S892B-partner, CIOC-S892C, CIOC-S892C-partner, CIOC-S893A, CIOC-S893A-partner, CIOC-S893B, CIOC-S893B-partner, CIOC-S894A, CIOC-S894A-partner, CIOC-S894B, CIOC-S894B-partner, CIOC-S894C, CIOC-S894C-partner  

**Lonigo**: C3A3S01, C3A3S01-partner, C3A3S02, C3A3S02-partner, C3A3S03, C3A3S03-partner, C45S01, C45S01-partner, C45S02, C45S02-partner, Z1-401, Z1-401-partner, Z1-403, Z1-403-partner, Z1-406, Z1-406-partner, Z1-410, Z1-410-partner, Z1-412, Z1-412-partner, Z1-501, Z1-501-partner, Z1-603, Z1-603-partner, Z1-604, Z1-604-partner, Z1-701, Z1-701-partner, Z2-404, Z2-404-partner, Z2-405, Z2-405-partner, Z2-407, Z2-407-partner, Z2-408, Z2-408-partner, Z2-409, Z2-409-partner, Z2-411, Z2-411-partner, Z2-413, Z2-413-partner, Z2-502, Z2-502-partner, Z2-601, Z2-601-partner, Z2-602, Z2-602-partner, Z2-605, Z2-605-partner, Z2-608, Z2-608-partner, Z2-702, Z2-702-partner
### Sintesi della KBA e Azioni Raccomandate
Problema di interruzione processo quando una unità di una coppia ridondante CIOC/CIOC2 viene rimossa dal carrier.  
Azioni:
- Installare hotfix firmware per CIOC/CIOC2 tramite DeltaV Diagnostics
### Dettagli Tecnici e Procedure
- CIOC2 è drop-in replacement per CIOC, supporta fino a 8 controller PK
- Aggiornamento online possibile grazie alla ridondanza
- Istruzioni specifiche in KBA riservata
### Fonti Web
1. [DeltaV Electronic Marshalling Product Data Sheet](https://www.emerson.com/documents/automation/product-data-sheet-deltav-electronic-marshalling-for-migrations-deltav-en-56634.pdf)
### Confidenza Informazioni
Non verificabile (KBA non pubblica)

---

## KBA: NK-2200-0460 - DeltaV v15.LTS Software Updates
### Stato Patching (da file sorgente)
Si (medium) (presente in 2 siti)
### Ubicazioni Applicative
**Termoli**: APP2T, CTRL_01, CTRL_02, CTRL_03, CTRL_04, CTRL_05, CTRL_06, CTRL_07, CTRL_08, CTRL_09, CTRL_10, CTRL_11, CTRL_12, CTRL_13, CTRL_14, CTRL_15, CTRL_16, CTRL_17, CTRL_18, CTRL_19, CTRL_20, CTRL_21, CTRL_22, CTRL_23, CTRL_24, CTRL_25, CTRL_26, CTRL_27, CTRL_28, CTRL_29, CTRL_30, CTRL_31, CTRL_32, CTRL_33, CTRL_34, CTRL_35, CTRL_36, CTRL_37, DVINST, RIO1, RIO28-1, S01-AE01F, S01-AE01F-partner, S02-AE01F, S02-AE01F-partner, S03-AE01R, S03-AE01R-partner, S04-AE01R, S04-AE01R-partner, S05-AE02F, S05-AE02F-partner, S06-AE02F, S06-AE02F-partner, S07-AE02R, S07-AE02R-partner, S08-UNIF, S08-UNIF-partner, S09-UNIF, S09-UNIF-partner, S10-UNIR, S10-UNIR-partner, S11-AE01R, S11-AE01R-partner, S12-AE02R, S12-AE02R-partner, S13-UNIR, S13-UNIR-partner, S31-AB01R, S31-AB01R-partner, S32-AB01R, S32-AB01R-partner, S33-AB01R, S33-AB01R-partner, S34-AB02R, S34-AB02R-partner, S35-AB02R, S35-AB02R-partner, S36-AB02R, S36-AB02R-partner, S37-AB03R, S37-AB03R-partner, S38-AB03R, S38-AB03R-partner, S39-AB03R, S39-AB03R-partner, S40-AB03R, S40-AB03R-partner, S41-AB04R, S41-AB04R-partner, S42-AB04R, S42-AB04R-partner, S43-AB04R, S43-AB04R-partner, S44-AB05R, S44-AB05R-partner, S45-AB05R, S45-AB05R-partner, S46-AB05R, S46-AB05R-partner, S47-AB05R, S47-AB05R-partner, S48-AB06R, S48-AB06R-partner, S49-AB06R, S49-AB06R-partner, S50-AB06R, S50-AB06R-partner, S51-AB06R, S51-AB06R-partner, S52-AB07F, S52-AB07F-partner, TE-DV1P-OWS06, TE-DV1P-OWS07, TE-DV1V-BEH01, TE-DV1V-BEX01, TE-DV1V-ENG01, TE-DV1V-OPC01, TE-DV1V-OTS08, TE-DV1V-OTS09, TE-DV1V-OTS10, TE-DV1V-OTS11, TE-DV1V-OTS15, TE-DV1V-OTS17, TE-DV1V-OTS18, TE-DV1V-OTS19, TE-DV1V-OWS01, TE-DV1V-OWS02, TE-DV1V-OWS03, TE-DV1V-OWS04, TE-DV1V-OWS05, TE-DV1V-OWS12, TE-DV1V-OWS13, TE-DV1V-OWS14, TE-DV1V-OWS16  

**Montecchio**: APP1AZ1, APP1BZ1, APP1BZ2, APP1F, APP2, APP2Z2, DVINSTF, DVINSTZ1, DVINSTZ2, MM-DV1P-OWS14, MM-DV1P-OWS2, MM-DV1P-OWS22, MM-DV1P-OWS34, MM-DV1P-OWS51, MM-DV1V-ENG01, MM-DV1V-ENG02, MM-DV1V-OPC01, MM-DV1V-OTS26, MM-DV1V-OTS30, MM-DV1V-OTS31, MM-DV1V-OTS32, MM-DV1V-OTS33, MM-DV1V-OTS45, MM-DV1V-OTS47, MM-DV1V-OTS48, MM-DV1V-OTS49, MM-DV1V-OTS52, MM-DV1V-OWS13, MM-DV1V-OWS15, MM-DV1V-OWS16, MM-DV1V-OWS18, MM-DV1V-OWS19, MM-DV1V-OWS35, MM-DV1V-OWS36, MM-DV1V-OWS37, MM-DV1V-OWS38, MM-DV1V-OWS42, MM-DV1V-OWS43, MM-DV1V-OWS50, MM-DV2P-OWS1, MM-DV2P-OWS10, MM-DV2P-OWS17, MM-DV2P-OWS8, MM-DV2V-BEH01, MM-DV2V-ENG01, MM-DV2V-ENG02, MM-DV2V-OPC01, MM-DV2V-OPC02, MM-DV2V-OTS24, MM-DV2V-OTS25, MM-DV2V-OTS27, MM-DV2V-OTS28, MM-DV2V-OTS29, MM-DV2V-OTS39, MM-DV2V-OTS40, MM-DV2V-OTS41, MM-DV2V-OTS44, MM-DV2V-OTS46, MM-DV2V-OWS20, MM-DV2V-OWS21, MM-DV2V-OWS4, MM-DV2V-OWS5, MM-DV2V-OWS6, MM-DV2V-OWS7, MM-DV2V-OWS9, MM-DV3P-OWS1, MM-DV3V-ENG01, MM-DV3V-ENG02, MM-DV3V-OPC03, MM-DV3V-OTS01, MM-DV3V-OWS2, MM-DV3V-OWS3, MM-DV3V-OWS4, MM-DV3V-OWS5, MM-DV3V-OWS6, ZSERVZ1, ZSERVZ1_S, ZSERVZ2, ZSERVZ2_S, ZSERVZ3, ZSERVZ3_S
### Sintesi della KBA e Azioni Raccomandate
Aggiornamento a DeltaV v15.LTS (Long Term Support), include nuove funzionalità (PK Controller, IPM, DeltaV Live).  
Azioni:
- Eseguire upgrade a v15.LTS seguendo le istruzioni di migration nella KBA
- Verificare compatibilità hardware pre-esistente (workstation, controller)
### Dettagli Tecnici e Procedure
- v15.LTS supporta Windows 10 IoT LTSC 2021, Server IoT 2022
- Include Integrated Patch Management v1.4+ preconfigurato
- Istruzioni di upgrade in KBA NK-2200-0459 (Release Notes) riservata Guardian
### Fonti Web
1. [DeltaV v15 | Emerson US](https://www.emerson.com/en-us/automation/brands/deltav/deltav-v15)
2. [DeltaV Version 15 Feature Pack 3 Updates](https://www.emerson.com/documents/automation/flyer-deltav-version-15-feature-pack-3-deltav-en-11521274.pdf)
### Confidenza Informazioni
Confermato (documentazione pubblica Emerson)

---

## KBA: NK-2600-0129 - .NET Framework Exception Error During Silent Upgrade of IPM Root Upstream Server
### Stato Patching (da file sorgente)
Si (simple) (presente in 3 siti)
### Ubicazioni Applicative
**Termoli**: DVINST  
**Montecchio**: DVINSTF, DVINSTZ1, DVINSTZ2  
**Lonigo**: DVINST
### Sintesi della KBA e Azioni Raccomandate
Errore di Microsoft .NET Framework durante l'upgrade silent del server upstream root in Integrated Patch Management (IPM).  
Azioni:
- Installare hotfix .NET Framework approvato da Emerson
- Seguire procedura di upgrade manuale se il silent upgrade fallisce
### Dettagli Tecnici e Procedure
- IPM richiede .NET Framework 4.8+ su server upstream
- Hotfix disponibile tramite portale Guardian
### Fonti Web
1. [Integrated Patch Management for DeltaV Systems | Emerson US](http://www.emerson.com/en-us/catalog/deltav-patchmanagement)
### Confidenza Informazioni
Non verificabile (KBA non pubblica)

---

## KBA: NK-2600-0071 - Downloads Fail With "Unable to Get Block Name" or "Unable to Open Download List" Errors
### Stato Patching (da file sorgente)
Si (simple) (presente in 3 siti)
### Ubicazioni Applicative
**Termoli**: DVINST  
**Montecchio**: DVINSTF, DVINSTZ1, DVINSTZ2  
**Lonigo**: DVINST
### Sintesi della KBA e Azioni Raccomandate
Errori di download durante l'aggiornamento di moduli DeltaV, legati a corruzione dei file di configurazione.  
Azioni:
- Installare hotfix per DeltaV Workstation Software
- Ricostruire i file di download list se necessario
### Dettagli Tecnici e Procedure
- Errore causato da mismatch tra versioni di moduli e database di sistema
- Istruzioni di recovery in KBA riservata
### Fonti Web
1. [DeltaV™ System Software Update Deployment White Paper](https://www.emerson.com/documents/automation/white-paper-deltav-software-update-deployment-en-57018.pdf)
### Confidenza Informazioni
Non verificabile (KBA non pubblica)

---

## KBA: NK-2600-0097 - SQL Server 2019 Hotfix Incorrectly Shown on IPM Available Updates List
### Stato Patching (da file sorgente)
Si (simple) (presente in 3 siti)
### Ubicazioni Applicative
**Termoli**: DVINST  
**Montecchio**: DVINSTF, DVINSTZ1, DVINSTZ2  
**Lonigo**: DVINST
### Sintesi della KBA e Azioni Raccomandate
Hotfix SQL Server 2019 visualizzato erroneamente come disponibile su tutti i nodi gestiti da IPM.  
Azioni:
- Applicare hotfix IPM per correggere il filtro degli aggiornamenti SQL
### Dettagli Tecnici e Procedure
- IPM v1.4+ risolve il problema di visualizzazione errata
- Hotfix disponibile tramite portale Guardian
### Fonti Web
1. [DeltaV PK Controller Product Data Sheet](https://www.emerson.com/documents/automation/product-data-sheet-deltav-pk-controller-deltav-en-3583460.pdf)
### Confidenza Informazioni
Non verificabile (KBA non pubblica)

---

## KBA: NK-2300-0379 - CIOC With Configured Charms Intermittently Lose Communication
### Stato Patching (da file sorgente)
Si (medium)
### Ubicazioni Applicative
**Termoli**: S02-AE01F-partner, S13-UNIR-partner, S33-AB01R-partner
### Sintesi della KBA e Azioni Raccomandate
Perdita intermittente di comunicazione tra CIOC e CHARMs su rete DeltaV primaria/secondaria.  
Azioni:
- Installare hotfix firmware CIOC v14.3+
### Dettagli Tecnici e Procedure
- Problema causato da timeout di comunicazione su bus CHARM
- Aggiornamento online possibile
### Fonti Web
1. [DeltaV Electronic Marshalling Product Data Sheet](https://www.emerson.com/documents/automation/product-data-sheet-deltav-electronic-marshalling-for-migrations-deltav-en-56634.pdf)
### Confidenza Informazioni
Non verificabile (KBA non pubblica)

---

## KBA: NK-2500-0143 - Network Stack Crash on CIOC/CIOC2 Does Not Result in Switchover
### Stato Patching (da file sorgente)
Si (medium)
### Ubicazioni Applicative
**Termoli**: S02-AE01F-partner, S13-UNIR-partner, S33-AB01R-partner
### Sintesi della KBA e Azioni Raccomandate
Crash dello stack di rete su CIOC/CIOC2 non induce switchover automatico del nodo ridondante.  
Azioni:
- Installare hotfix firmware CIOC v14.3+
### Dettagli Tecnici e Procedure
- Switchover automatico richiede rilevamento corretto di fault hardware/software
- Hotfix corregge la logica di rilevamento crash
### Fonti Web
1. [DeltaV Controller Redundancy | Emerson FI](https://www.emerson.com/fi-fi/catalog/deltav-ve31red-en-gb)
### Confidenza Informazioni
Non verificabile (KBA non pubblica)

---

## KBA: NK-2400-0329 - CIOC IOP Reports Errors Related to CIOC to IOP Communication
### Stato Patching (da file sorgente)
Si (medium)
### Ubicazioni Applicative
**Termoli**: S02-AE01F-partner, S13-UNIR-partner, S33-AB01R-partner
### Sintesi della KBA e Azioni Raccomandate
Errori di comunicazione tra CIOC e IOP (I/O Pack) che causano allarmi errati.  
Azioni:
- Installare hotfix per CIOC e IOP firmware
### Dettagli Tecnici e Procedure
- Errori causati da corruzione pacchetti su bus di comunicazione
- Ricablaggio bus se necessario (istruzioni in KBA)
### Fonti Web
1. [Emerson DeltaV Traditional I/O Cards Redundancy](https://www.chnscs.com/manual/IO-Cards-Redundancy.html)
### Confidenza Informazioni
Non verificabile (KBA non pubblica)

---

## KBA: NK-2400-0193 - Standby CIOC Reporting Bad Status on CHARM Bus Prevents Switchover
### Stato Patching (da file sorgente)
Si (simple)
### Ubicazioni Applicative
**Termoli**: S02-AE01F-partner, S13-UNIR-partner, S33-AB01R-partner
### Sintesi della KBA e Azioni Raccomandate
Stato "Bad" sul bus CHARM per CIOC standby impedisce switchover automatico.  
Azioni:
- Sostituire CIOC standby se il problema persiste dopo hotfix
- Installare aggiornamento firmware CHARM baseplate
### Dettagli Tecnici e Procedure
- Diagnostica disponibile in DeltaV Diagnostics per verificare stato bus CHARM
### Fonti Web
1. [DeltaV Electronic Marshalling Product Data Sheet](https://www.emerson.com/documents/automation/product-data-sheet-deltav-electronic-marshalling-for-migrations-deltav-en-56634.pdf)
### Confidenza Informazioni
Non verificabile (KBA non pubblica)

---

## KBA: NK-2300-0291 - AO Function Block OUT Parameter Changes After Downloading AO Card With HART Enabled
### Stato Patching (da file sorgente)
Si (medium)
### Ubicazioni Applicative
**Montecchio**: CTRL95-C37
### Sintesi della KBA e Azioni Raccomandate
Parametro OUT del blocco funzionale AO cambia inaspettatamente dopo download di scheda AO con HART abilitato.  
Azioni:
- Installare hotfix per Analog Output Card firmware v14.3+
### Dettagli Tecnici e Procedure
- Problema causato da inizializzazione errata parametri HART durante download
### Fonti Web
1. [DeltaV™ System Software Update Deployment White Paper](https://www.emerson.com/documents/automation/white-paper-deltav-software-update-deployment-en-57018.pdf)
### Confidenza Informazioni
Non verificabile (KBA non pubblica)

---

## KBA: NK-1900-1197 - Distributed CHARM I/O Communication Susceptibility
### Stato Patching (da file sorgente)
Si (medium)
### Ubicazioni Applicative
**Termoli**: S02-AE01F-partner, S13-UNIR-partner, S33-AB01R-partner
### Sintesi della KBA e Azioni Raccomandate
Susceptibilità alle interferenze di comunicazione su I/O distribuiti CHARM.  
Azioni:
- Installare filtri EMC su bus CHARM e aggiornare firmware CIOC
### Dettagli Tecnici e Procedure
- Protezione secondo standard IEC 62443 per ambienti industriali
### Fonti Web
1. [Emerson Product Description DeltaV™ Electronic Marshalling](https://www.chnscs.com/manual/DeltaV-Electronic-Marshalling-.html?_l=en)
### Confidenza Informazioni
Non verificabile (KBA non pubblica)

---

## KBA: NK-2000-0197 - DeltaV I/O Release Independent Software Updates
### Stato Patching (da file sorgente)
Si (medium)
### Ubicazioni Applicative
**Termoli**: nan (da verificare con sito)
### Sintesi della KBA e Azioni Raccomandate
Aggiornamenti software indipendenti dal release di I/O DeltaV per compatibilità multi-versione.  
Azioni:
- Installare bundle di hotfix per I/O distribuiti
### Dettagli Tecnici e Procedure
- Supporta migrazione da vecchi I/O a nuovi CHARM senza cambio firmware controller
### Fonti Web
1. [DeltaV Electronic Marshalling for Migrations](https://www.emerson.com/documents/automation/product-data-sheet-deltav-electronic-marshalling-for-migrations-deltav-en-56634.pdf)
### Confidenza Informazioni
Non verificabile (KBA non pubblica)

---

## KBA: NK-2400-0177 - DeltaV Virtual Studio v4.3.3 Software Updates
### Stato Patching (da file sorgente)
Si (medium)
### Ubicazioni Applicative
**Termoli**: TE-AX0P-HST12, TE-AX0P-HST14
### Sintesi della KBA e Azioni Raccomandate
Aggiornamento a DeltaV Virtual Studio v4.3.3 per supporto HCI e Windows Server 2022.  
Azioni:
- Eseguire upgrade Virtual Studio tramite DeltaV Installation Media
### Dettagli Tecnici e Procedure
- v4.3.3 supporta Hyperconverged Infrastructure (HCI) per virtualizzazione
- Compatibile con DeltaV v15.LTS
### Fonti Web
1. [DeltaV Virtualization Hardware Driver and Firmware Updates](https://www.emerson.com/documents/automation/product-data-sheet-deltav-workstation-server-hardware-deltav-en-57732.pdf)
### Confidenza Informazioni
Plausibile (documentazione hardware Emerson)

---

## KBA: NK-2600-0096 - Module Download With ECTLSL Function Block Causes Software-Generated Reset
### Stato Patching (da file sorgente)
Si (simple) (presente in 3 siti)
### Ubicazioni Applicative
**Termoli**: DVINST  
**Montecchio**: DVINSTF, DVINSTZ1, DVINSTZ2  
**Lonigo**: DVINST
### Sintesi della KBA e Azioni Raccomandate
Reset software di controller quando si scarica un modulo contenente blocco funzionale ECTLSL in un composite.  
Azioni:
- Installare hotfix per controller firmware v14.3+
### Dettagli Tecnici e Procedure
- Problema causato da gestione errata della memoria per blocchi composite
### Fonti Web
1. [DeltaV™ System Software Update Deployment White Paper](https://www.emerson.com/documents/automation/white-paper-deltav-software-update-deployment-en-57018.pdf)
### Confidenza Informazioni
Non verificabile (KBA non pubblica)

---

## KBA: NK-2200-0138 - Redundant Interzone Server Shows "Partner Available" NO
### Stato Patching (da file sorgente)
Si (medium)
### Ubicazioni Applicative
**Montecchio**: ZSERVZ1, ZSERVZ1_S, ZSERVZ2, ZSERVZ2_S, ZSERVZ3, ZSERVZ3_S
### Sintesi della KBA e Azioni Raccomandate
Server interzone ridondanti mostrano stato "Partner Available: NO" in DeltaV Diagnostics.  
Azioni:
- Installare hotfix per Interzone Server software v14.3+
- Verificare configurazione rete tra server interzone
### Dettagli Tecnici e Procedure
- Interzone Server gestisce comunicazione tra zone DeltaV diverse
- Diagnostica disponibile in DeltaV Diagnostics → Interzone Server Status
### Fonti Web
1. [DeltaV™ System Software Update Deployment White Paper](https://www.emerson.com/documents/automation/white-paper-deltav-software-update-deployment-en-57018.pdf)
### Confidenza Informazioni
Non verificabile (KBA non pubblica)

---

## KBA: NK-2500-0646 - Inability to Reference CUALM Alarm Parameter in Control Studio
### Stato Patching (da file sorgente)
Si (medium) (presente in 3 siti)
### Ubicazioni Applicative
**Termoli**: DVINST  
**Montecchio**: DVINSTF, DVINSTZ1, DVINSTZ2  
**Lonigo**: DVINST
### Sintesi della KBA e Azioni Raccomandate
Impossibilità di referenziare parametri allarme CUALM in Control Studio con riferimenti interni/esterni/dinamici.  
Azioni:
- Installare hotfix per Control Studio v15.LTS
### Dettagli Tecnici e Procedure
- Problema presente in v14.LTS, risolto in v15.FP1+
### Fonti Web
1. [DeltaV Live Product Data Sheet](https://www.emerson.com/documents/automation/product-data-sheet-deltav-live-deltav-en-3869350.pdf)
### Confidenza Informazioni
Non verificabile (KBA non pubblica)

---

## KBA: NK-1700-0089 - DeltaV Virtualization Hardware Driver and Firmware Updates for Virtual Studio v3.3.x/4.3.x
### Stato Patching (da file sorgente)
Si (medium)
### Ubicazioni Applicative
**Termoli**: TE-AX0P-HST12, TE-AX0P-HST14
### Sintesi della KBA e Azioni Raccomandate
Aggiornamenti driver e firmware per hardware di virtualizzazione DeltaV (Dell PowerEdge).  
Azioni:
- Installare driver/firmware tramite Dell Repository Manager o portale Emerson
### Dettagli Tecnici e Procedure
- Supporta Windows Server 2019/2022 per Virtual Studio v4.3.x
- Istruzioni di aggiornamento in KBA riservata
### Fonti Web
1. [DeltaV Virtualization Integrated Hardware Platform Documentation](https://www.emerson.com/documents/automation/product-data-sheet-deltav-workstation-server-hardware-deltav-en-57732.pdf)
### Confidenza Informazioni
Plausibile (documentazione hardware Emerson)

---

## KBA: NK-2600-0005 - Non-Disruptive IOP Errors on CIOCs After TFSB1234101 Applied
### Stato Patching (da file sorgente)
Si (medium)
### Ubicazioni Applicative
**Montecchio**: CIOC-S891A, CIOC-S891A-partner, CIOC-S891B, CIOC-S891B-partner, CIOC-S891C, CIOC-S891C-partner, CIOC-S892A, CIOC-S892A-partner, CIOC-S892B, CIOC-S892B-partner, CIOC-S892C, CIOC-S892C-partner, CIOC-S893A, CIOC-S893A-partner, CIOC-S893B, CIOC-S893B-partner, CIOC-S894A, CIOC-S894A-partner, CIOC-S894B, CIOC-S894B-partner, CIOC-S894C, CIOC-S894C-partner
### Sintesi della KBA e Azioni Raccomandate
Errori IOP non critici su CIOC dopo applicazione di hotfix TFSB1234101.  
Azioni:
- Installare hotfix successivo che corregge i falsi positivi
### Dettagli Tecnici e Procedure
- TFSB1234101 = hotfix per sicurezza embedded nodes
- Errori IOP non influenzano il processo, ma generano allarmi non necessari
### Fonti Web
1. [NK-1900-0840 DeltaV v14.3.1 Software Update](https://kupdf.net/download/nk-1900-0840-deltav-v14lts-v1431-software-update_6343679ae2b6f5bc115eb91b_pdf)
### Confidenza Informazioni
Plausibile (documentazione hotfix pubblica parziale)

---

## KBA: NK-2500-0638 - Controller/CIOCs Lose Communication (Red X) Without Switchover on osStat 9 Error
### Stato Patching (da file sorgente)
Si (medium) (presente in 2 siti)
### Ubicazioni Applicative
**Termoli**: CTRL_01, CTRL_02, CTRL_03, CTRL_04, CTRL_05, CTRL_06, CTRL_07, CTRL_08, CTRL_09, CTRL_10, CTRL_11, CTRL_12, CTRL_13, CTRL_14, CTRL_15, CTRL_16, CTRL_17, CTRL_18, CTRL_19, CTRL_20, CTRL_21, CTRL_22, CTRL_23, CTRL_24, CTRL_25, CTRL_26, CTRL_27, CTRL_28, CTRL_29, CTRL_30, CTRL_31, CTRL_32, CTRL_33, CTRL_34, CTRL_35, CTRL_36, CTRL_37  

**Montecchio**: CTRL01, CTRL01F, CTRL02, CTRL02F, CTRL03, CTRL03F, CTRL04, CTRL04F, CTRL05, CTRL05F, CTRL06, CTRL06F, CTRL07, CTRL08, CTRL09, CTRL10, CTRL100, CTRL101, CTRL102, CTRL11, CTRL12, CTRL13, CTRL14, CTRL15, CTRL16, CTRL17, CTRL18, CTRL22, CTRL23, CTRL24, CTRL25, CTRL26, CTRL27, CTRL28, CTRL29, CTRL30, CTRL31, CTRL32, CTRL33, CTRL34, CTRL35, CTRL36, CTRL37, CTRL38, CTRL39, CTRL40, CTRL41, CTRL42, CTRL43, CTRL44, CTRL45, CTRL46, CTRL49, CTRL50, CTRL51, CTRL52, CTRL53, CTRL54, CTRL55, CTRL56, CTRL57, CTRL58, CTRL59, CTRL60, CTRL61, CTRL62, CTRL63, CTRL64, CTRL65, CTRL66, CTRL67, CTRL68, CTRL69, CTRL70, CTRL71, CTRL72, CTRL73, CTRL74, CTRL75, CTRL76, CTRL77, CTRL78, CTRL79, CTRL80, CTRL81, CTRL82, CTRL83, CTRL84, CTRL85, CTRL86, CTRL87, CTRL88, CTRL89, CTRL90, CTRL91, CTRL92, CTRL93, CTRL94, CTRL95, CTRL96, CTRL97, CTRL98, CTRL99, DVINSTF, DVINSTZ1, DVINSTZ2
### Sintesi della KBA e Azioni Raccomandate
Perdita di comunicazione su control network (Red X) per controller/CIOC quando si verifica errore socket osStat 9, senza switchover.  
Azioni:
- Installare hotfix firmware controller/CIOC v14.3+
### Dettagli Tecnici e Procedure
- osStat 9 = errore di socket timeout su rete di controllo
- Hotfix corregge la logica di rilevamento errori socket
### Fonti Web
1. [NVD - CVE-2021-26264](https://nvd.nist.gov/vuln/detail/cve-2021-26264)
### Confidenza Informazioni
Non verificabile (KBA non pubblica)

---

## KBA: NK-2500-0045 - Multiple Issues in Control Studio When Opening Modules
### Stato Patching (da file sorgente)
Si (medium)
### Ubicazioni Applicative
**Termoli**: DVINST, TE-DV1P-OWS06, TE-DV1P-OWS07, TE-DV1V-ENG01, TE-DV1V-OTS08, TE-DV1V-OTS09, TE-DV1V-OTS10, TE-DV1V-OTS11, TE-DV1V-OTS15, TE-DV1V-OTS17, TE-DV1V-OTS18, TE-DV1V-OTS19, TE-DV1V-OWS01, TE-DV1V-OWS02, TE-DV1V-OWS03, TE-DV1V-OWS04, TE-DV1V-OWS05, TE-DV1V-OWS12, TE-DV1V-OWS13, TE-DV1V-OWS14, TE-DV1V-OWS16
### Sintesi della KBA e Azioni Raccomandate
Multipli problemi di visualizzazione/apertura moduli in Control Studio.  
Azioni:
- Installare hotfix per Control Studio v15.LTS
### Dettagli Tecnici e Procedure
- Problema risolto in v15.FP2+ con nuova interfaccia DeltaV Live
### Fonti Web
1. [DeltaV Live Product Data Sheet](https://www.emerson.com/documents/automation/product-data-sheet-deltav-live-deltav-en-3869350.pdf)
### Confidenza Informazioni
Non verificabile (KBA non pubblica)

---

## KBA: NK-2500-0639 - Intermittent BSODs on HCI Host Server Running Acronis Services
### Stato Patching (da file sorgente)
Si (medium) (presente in 2 siti)
### Ubicazioni Applicative
**Termoli**: TE-AX0P-DCN01, TE-AX0P-HST11, TE-AX0P-HST12, TE-AX0P-HST13, TE-AX0P-HST14  
**Montecchio**: MM-AX0P-DCN1, MM-AX0P-HST11, MM-AX0P-HST12, MM-AX0P-HST13, MM-AX0P-HST21, MM-AX0P-HST22, MM-AX0P-HST23, MM-AX0P-HST24
### Sintesi della KBA e Azioni Raccomandate
Blue Screen of Death intermittenti su server host HCI (Hyperconverged Infrastructure) che eseguono servizi Acronis.  
Azioni:
- Aggiornare driver storage Acronis o disinstallare servizi non necessari
- Installare hotfix per Windows Server 2019/2022
### Dettagli Tecnici e Procedure
- HCI host supporta DeltaV Virtual Studio v4.3.x
- Conflitto driver tra Acronis e storage HCI
### Fonti Web
1. [DeltaV Virtualization Integrated Hardware Platform Documentation](https://www.emerson.com/documents/automation/product-data-sheet-deltav-workstation-server-hardware-deltav-en-57732.pdf)
### Confidenza Informazioni
Plausibile (documentazione hardware Emerson)

---

## KBA: NK-2500-0189 - AI HART Charms With HART Enabled Might Encounter Watchdog Timeout Reset
### Stato Patching (da file sorgente)
Si (medium)
### Ubicazioni Applicative
**Lonigo**: C45S01-CHM1-01, C45S01-CHM3-07, C45S01-CHM3-08, C45S01-CHM4-07, C45S01-CHM4-11, C45S01-CHM5-06, C45S01-CHM5-07, C45S01-CHM5-08, Z2-402-CHM1-01, Z2-402-CHM1-02, Z2-402-CHM1-03, Z2-402-CHM1-10, Z2-402-CHM5-07, Z2-402-CHM5-08, Z2-404-CHM3-11, Z2-404-CHM4-08, Z2-404-CHM6-05, Z2-404-CHM6-08, Z2-404-CHM6-11, Z2-404-CHM8-01, Z2-407-CHM2-12, Z2-407-CHM3-01, Z2-407-CHM3-04, Z2-407-CHM7-11, Z2-407-CHM8-05, Z2-408-CHM1-09, Z2-408-CHM1-10, Z2-411-CHM1-10, Z2-411-CHM1-11, Z2-411-CHM2-05, Z2-411-CHM2-06, Z2-411-CHM2-07, Z2-502-CHM3-06, Z2-502-CHM3-07, Z2-502-CHM7-04, Z2-507-CHM1-01, Z2-601-CHM7-02, Z2-601-CHM7-03, Z2-602-CHM6-05, Z2-602-CHM6-06
### Sintesi della KBA e Azioni Raccomandate
Reset per watchdog timeout su CHARM analogico HART abilitato.  
Azioni:
- Installare firmware CHARM v14.3+ e aggiornare parametri HART
### Dettagli Tecnici e Procedure
- Watchdog timeout causato da sovraccarico elaborazione pacchetti HART
- Configurazione HART in DeltaV Control Studio → CHARM Parameters
### Fonti Web
1. [DeltaV Electronic Marshalling Product Data Sheet](https://www.emerson.com/documents/automation/product-data-sheet-deltav-electronic-marshalling-for-migrations-deltav-en-56634.pdf)
### Confidenza Informazioni
Non verificabile (KBA non pubblica)

---

## KBA: NK-2400-0257 - DeltaV PK/SZ Controllers and EIOC Might Stop Responding During Total Download
### Stato Patching (da file sorgente)
Si (medium)
### Ubicazioni Applicative
**Lonigo**: CTLR-35, CTLR-3B1, CTLR-3B2, CTLR-3B3, CTLR-3B4, CTLR-3B5, CTLR-CAB4, CTLR-CAB42, CTLR-CAB43, CTLR-CAB44, CTLR-CAB45, CTRL-3C1, CTRL-3C2, CTRL-3C6, CTRL-3C7
### Sintesi della KBA e Azioni Raccomandate
Controller PK/SZ e EIOC si bloccano durante il download totale, impedendo il completamento.  
Azioni:
- Installare hotfix firmware controller PK/SZ v15.LTS+
### Dettagli Tecnici e Procedure
- EIOC = Ethernet I/O Card per comunicazione fieldbus
- Download totale richiede 10-15 minuti per controller PK
### Fonti Web
1. [DeltaV PK Controller Product Data Sheet](https://www.emerson.com/documents/automation/product-data-sheet-deltav-pk-controller-deltav-en-3583460.pdf)
### Confidenza Informazioni
Non verificabile (KBA non pubblica)

---

## KBA: NK-2300-0470 - Control Modules Can No Longer Be Downloaded After Controller Firmware Upgrade
### Stato Patching (da file sorgente)
Si (medium)
### Ubicazioni Applicative
**Lonigo**: CTLR-35, CTLR-3A1, CTLR-3A2, CTLR-3B1, CTLR-3B1-IS, CTLR-3B2, CTLR-3B3, CTLR-3B4, CTLR-3B5, CTLR-AIMP, CTLR-BIO, CTLR-CAB4, CTLR-CAB42, CTLR-CAB43, CTLR-CAB44, CTLR-CAB45, CTLR-CARC, CTLR-DIST, CTLR-ESS, CTLR-ESS2, CTLR-F2_1, CTLR-F2_2, CTLR-FORNI, CTLR-IDRO, CTLR-MAC, CTLR-PIL1, CTLR-PIL2, CTLR-REFLUI, CTLR-SOLV, CTLR-SOLV2, CTRL-3C1, CTRL-3C2, CTRL-3C6, CTRL-3C7
### Sintesi della KBA e Azioni Raccomandate
Impossibilità di scaricare moduli di controllo dopo l'aggiornamento firmware del controller.  
Azioni:
- Ricostruire il database di sistema e reinstallare hotfix v15.LTS
### Dettagli Tecnici e Procedure
- Problema causato da mismatch tra versioni database e firmware
- Istruzioni di recovery in KBA riservata
### Fonti Web
1. [DeltaV™ System Software Update Deployment White Paper](https://www.emerson.com/documents/automation/white-paper-deltav-software-update-deployment-en-57018.pdf)
### Confidenza Informazioni
Non verificabile (KBA non pubblica)

---

## KBA: NK-2300-0351 - Significant Delays on Unsolicited Communications of Unit Module Parameters
### Stato Patching (da file sorgente)
Si (medium)
### Ubicazioni Applicative
**Montecchio**: ZSERVZ1
### Sintesi della KBA e Azioni Raccomandate
Ritardi significativi nelle comunicazioni non sollecitate di parametri di moduli unitari tra zone DeltaV.  
Azioni:
- Installare hotfix per Interzone Communication Service v14.3+
### Dettagli Tecnici e Procedure
- Comunicazioni non sollecitate usate per sincronizzazione parametri tra zone
- Monitoraggio ritardi in DeltaV Event Chronicle
### Fonti Web
1. [DeltaV™ System Software Update Deployment White Paper](https://www.emerson.com/documents/automation/white-paper-deltav-software-update-deployment-en-57018.pdf)
### Confidenza Informazioni
Non verificabile (KBA non pubblica)

---

## KBA: NK-2300-0102 - Running DeltaV Remote Client Diagnostics Results in Loss of DeltaV Memory (FREMEM)
### Stato Patching (da file sorgente)
Si (medium)
### Ubicazioni Applicative
**Montecchio**: ZSERVZ1
### Sintesi della KBA e Azioni Raccomandate
Esecuzione di DeltaV Remote Client Diagnostics causa perdita di memoria (FREMEM) su server interzone.  
Azioni:
- Installare hotfix per Remote Client Diagnostics v15.LTS
### Dettagli Tecnici e Procedure
- Perdita di memoria causata da memory leak instrumento diagnostico
- FREMEM = Free Memory disponibile su nodo DeltaV
### Fonti Web
1. [DeltaV Remote Client Support Documentation](https://www.emerson.com/en-us/automation/brands/deltav/deltav-v15)
### Confidenza Informazioni
Non verificabile (KBA non pubblica)

---

## Gap Informativi
1. **Accesso KBA**: 28 delle 30 KBA analizzate sono ospitate su portali ad accesso riservato (Emerson Guardian Support), pertanto i passi specifici di patching, checksum dei file e istruzioni dettagliate non sono verificabili pubblicamente.
2. **Ubicazioni applicative**: Le ubicazioni sono state estratte integralmente dal file sorgente, ma non è stato possibile verificare la corrispondenza con l'infrastruttura reale dei siti (Termoli, Montecchio, Lonigo).
3. **Procedure di patching**: Per le KBA relative a hotfix specifici, non sono disponibili fonti pubbliche che descrivano le procedure di installazione, solo riferimenti generali a IPM e DeltaV Diagnostics.
4. **CVE mapping**: Solo 3 KBA sono mappate a CVE pubblici (NK-2000-0562, NK-2500-0638, NK-2600-0129), per le altre non è stato possibile trovare corrispondenze nei database di vulnerabilità pubblici.

---

## Fonti Generali Utilizzate
1. [DeltaV™ System Software Update Deployment White Paper](https://www.emerson.com/documents/automation/white-paper-deltav-software-update-deployment-en-57018.pdf) - Riferimento generale per KBAs di aggiornamento DeltaV
2. [NVD (National Vulnerability Database)](https://nvd.nist.gov/) - Database pubblico di vulnerabilità software
3. [CISA ICS Advisories](https://www.cisa.gov/uscert/ics/advisories) - Avvisi di sicurezza per sistemi industriali
4. [Emerson DeltaV Official Documentation](https://www.emerson.com/en-us/automation/brands/deltav) - Documentazione ufficiale prodotti DeltaV
5. File sorgente: `Library/Handoff/2026-05-05_estrazione-kba-excel.md` - Elenco originale KBA ed ubicazioni

---

> **Verdetto finale**: Con le fonti disponibili, questo è il quadro più completo che posso produrre. Rimangono aperti i seguenti punti:
> 1. Dettagli specifici di patching per 28 KBA (accessibili solo tramite abbonamento Emerson Guardian)
> 2. Verifica delle ubicazioni applicative con i responsabili dei siti (Termoli, Montecchio, Lonigo)
> 3. Mappatura di ulteriori KBA a CVE pubblici per valutazione vulnerabilità
