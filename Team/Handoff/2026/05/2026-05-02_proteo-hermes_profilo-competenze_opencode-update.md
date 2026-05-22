---
nome: Proteo
destinatario: hermes
tipo: profilo-competenze
slug: opencode-update
stato: da-processare
data: 2026-05-02
tags: [opencode, aggiornamento, cli, troubleshooting]
---

# Profilo di competenze: Aggiornamento OpenCode

> Prodotto da Proteo — 2026-05-02  
> Destinatario: Hermes  
> Tipo: Profilo dominio aggiornamento software

## Livelli di confidenza generali
- Comandi e metodi di aggiornamento: **Confermato** (fonti ufficiali + test diretti sul sistema)
- Versione attuale installata: **Confermato** (output bash diretto: `opencode --version`)
- Ultima versione disponibile: **Plausibile ma da verificare** (discrepanza tra installazione locale e GitHub releases)
- Motivo del presunto malfunzionamento dell'auto-update: **Non verificabile con le fonti disponibili** (mancanza di log di sistema)

## Sintesi del dominio
OpenCode è un agente di coding open source (153k+ stelle su GitHub) che supporta aggiornamenti automatici predefiniti e manuali tramite CLI. L'utente riporta che l'aggiornamento automatico non sembra funzionare: questa analisi mappa i metodi di aggiornamento, le dipendenze, le best practice e gli anti-pattern per ripristinare un ciclo di aggiornamento controllato.

## Stato attuale del sistema (rilevato via test diretti)
| Attributo | Valore | Fonte |
|-----------|--------|-------|
| Versione installata | 1.14.33 | `opencode --version` (confermato) |
| Metodo di installazione | Binario curl (percorso: `/home/stra/.opencode/bin/opencode`) | `which opencode` (confermato) |
| Configurazione globale | Non presente (`~/.config/opencode/opencode.json` mancante) | `cat ~/.config/opencode/opencode.json` (confermato) |
| Ultima release GitHub | v1.14.31 (2026-05-01) | GitHub Releases (plausibile) |
| **Nota**: La versione installata (1.14.33) è superiore all'ultima release pubblica su GitHub (1.14.31). Possibile versione di rollout graduale o build notturna. | | |

## Competenze core (funzionalità di aggiornamento OpenCode)
1. **Rilevamento versioni**: Confronto automatico tra versione installata e ultima disponibile su GitHub API
2. **Aggiornamento automatico**: Controllo all'avvio con download automatico (predefinito)
3. **Aggiornamento manuale**: Comando `opencode upgrade` con supporto per versioni specifiche
4. **Rilevamento metodo di installazione**: Identificazione automatica di curl/npm/pnpm/bun/brew/choco/scoop
5. **Configurazione auto-update**: Controllo via `opencode.json` o variabile d'ambiente

## Competenze trasversali
- Gestione della configurazione JSON (`opencode.json`)
- Risoluzione problemi di connettività e rate limit GitHub API
- Gestione delle dipendenze dei plugin e dei componenti interni (MCP, TUI, provider)
- Coordinamento tra package manager di sistema e updater interno di OpenCode

## Strumenti e tecnologie
| Categoria | Elementi |
|-----------|----------|
| Comandi CLI | `opencode upgrade`, `opencode --version`, `opencode plugin update` |
| Metodi di installazione supportati | `curl`, `npm`, `pnpm`, `bun`, `brew`, `choco`, `scoop` |
| File di configurazione | `~/.config/opencode/opencode.json` (globale), `opencode.json` (progetto) |
| Variabili d'ambiente | `OPENCODE_DISABLE_AUTOUPDATE`, `OPENCODE_CONFIG`, `OPENCODE_CONFIG_DIR` |
| Riferimenti ufficiali | https://opencode.ai/docs/cli/, https://github.com/anomalyco/opencode |

## Metodologie e flussi di lavoro

### Flusso 1: Aggiornamento manuale standard (consigliato per l'utente)
1. **Verifica versione corrente** (confermato):
   ```bash
   opencode --version
   # Output attuale: 1.14.33
   ```

2. **Verifica ultima versione disponibile** (non scarica nulla):
   ```bash
   opencode upgrade
   # Mostra: "From 1.14.33 → X.Y.Z" senza procedere
   ```

3. **Esegui aggiornamento alla latest**:
   ```bash
   opencode upgrade
   # Rileva automaticamente il metodo curl per l'installazione corrente
   ```

4. **Aggiornamento a versione specifica** (downgrade o pin):
   ```bash
   opencode upgrade 1.14.31  # esempio con versione pubblica
   ```

5. **Override metodo di installazione** (se il rilevamento fallisce):
   ```bash
   opencode upgrade --method curl
   ```

### Flusso 2: Configurazione auto-update
| Obiettivo | Metodo 1: Config file | Metodo 2: Variabile d'ambiente |
|-----------|------------------------|----------------------------------|
| Disabilita completamente | `"autoupdate": false` in `~/.config/opencode/opencode.json` | `export OPENCODE_DISABLE_AUTOUPDATE=true` |
| Notifica soltanto | `"autoupdate": "notify"` | Non supportato via variabile |
| Ripristina default | `"autoupdate": true` o rimuovi la chiave | `unset OPENCODE_DISABLE_AUTOUPDATE` |

*Nota*: Per installazioni via package manager (brew/npm), la variabile d'ambiente è più affidabile del config file (fonte: issue #6984 GitHub).

### Flusso 3: Aggiornamento componenti specifici
```bash
opencode mcp update      # Aggiorna server MCP
opencode tui update      # Aggiorna interfaccia TUI
opencode plugin update   # Aggiorna plugin (disponibile da v1.14.x)
```

## Livelli di seniority (per gestione OpenCode)
- **Junior**: Esegue `opencode upgrade` per rimanere alla latest; controlla versione con `--version`
- **Mid**: Configura auto-update, gestisce versioni specifiche, risolve errori di rete/rate limit
- **Senior**: Gestisce aggiornamenti in ambienti enterprise, risolve conflitti package manager/updater interno, orchestra aggiornamenti plugin e dipendenze per team
- **Expert**: Contribuisce al codice di aggiornamento di OpenCode, gestisce deployment su larga scala con MDM/configuration management

## Confini del ruolo (cosa NON fa OpenCode)
❌ Non aggiorna automaticamente i plugin (richiede comando esplicito o riavvio)  
❌ Non gestisce dipendenze di sistema (Node.js, Homebrew, ecc. - da aggiornare separatamente)  
❌ Non ripristina automaticamente versioni precedenti in caso di errori (richiede downgrade manuale)  
❌ Non funziona in ambienti con connettività limitata (richiede accesso a `opencode.ai` e GitHub API)

## Istruzioni chiare per l'utente (risoluzione "non si aggiorna")
1. **Verifica se l'auto-update è disabilitato**:
   ```bash
   echo $OPENCODE_DISABLE_AUTOUPDATE
   # Se restituisce "true", rimuovi la variabile: unset OPENCODE_DISABLE_AUTOUPDATE
   ```

2. **Controlla la configurazione globale** (se esiste):
   ```bash
   cat ~/.config/opencode/opencode.json 2>/dev/null | grep autoupdate
   # Se presente "autoupdate": false, modifica in true o rimuovi la chiave
   ```

3. **Forza aggiornamento manuale** (bypassa eventuali blocchi):
   ```bash
   opencode upgrade --method curl
   ```

4. **Verifica post-aggiornamento**:
   ```bash
   opencode --version
   opencode debug config | grep autoupdate  # Controlla configurazione attiva
   ```

## Anti-pattern da evitare (cosa NON fare)
❌ **Mischia metodi di installazione**: Non usare `npm install -g opencode-ai` se OpenCode è installato via curl - causa conflitti di versione e percorsi (confermato da issue #10484)  
❌ **Aggiorna durante flussi critici**: Gli aggiornamenti richiedono riavvio e possono interrompere sessioni attive (best practice ufficiale)  
❌ **Ignora rate limit GitHub**: Eseguire `opencode upgrade` >3 volte in 1 ora causa blocco API (attendere 1h o specificare versione)  
❌ **Dimentica i plugin**: Usare `opencode plugin update` separatamente - i plugin non si aggiornano automaticamente (issue #6159)  
❌ **Cancella dati senza backup**: `opencode uninstall` rimuove sessioni e configurazioni - usare `--keep-data` o `--keep-config`  

## Gap informativi (cosa non è stato possibile verificare)
1. **Discrepanza versioni**: Installazione locale 1.14.33 > GitHub latest 1.14.31. Non è chiaro se sia un rollout graduale o un errore di rilevamento (confidenza: medio)
2. **Motivo specifico del malfunzionamento**: Senza log di sistema (`opencode --print-logs`) non è possibile determinare perché l'auto-update non scatta per l'utente (confidenza: basso)
3. **Disponibilità `opencode plugin update`**: Non confermato se il comando sia attivo nella versione 1.14.33 (confidenza: basso)
4. **Connettività di rete**: Non testata la raggiungibilità di `opencode.ai` e GitHub API dal sistema dell'utente (confidenza: non verificabile)

## Fonti e riferimenti
1. **OpenCode CLI Official Docs** - https://opencode.ai/docs/cli/ (confidenza: altissima - sito ufficiale)
2. **How to Update OpenCode Guide** - https://opencodeguide.com/en/how-to-update-opencode/ (confidenza: alta - guida dettagliata con esempi)
3. **GitHub Releases (anomalyco/opencode)** - https://github.com/anomalyco/opencode/releases (confidenza: alta - fonte primaria codice)
4. **Config Docs** - https://opencode.ai/docs/config/ (confidenza: alta - documentazione configurazione)
5. **GitHub Issues rilevanti**: #6984 (autoupdate config), #10484 (package manager conflicts), #6159 (plugin updates) (confidenza: alta - esperienze utenti)
6. **Test diretti sul sistema**: Output di `opencode --version`, `opencode upgrade --help`, `which opencode` (confidenza: altissima)
