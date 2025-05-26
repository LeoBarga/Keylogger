# Python Keylogger (Solo a scopo educativo)

Questo progetto implementa un semplice **keylogger** in Python utilizzando la libreria `pynput`. Il programma registra i tasti premuti dall'utente e li salva in un file di log (`log.txt`) all'interno di una cartella designata.

> ⚠️ **ATTENZIONE**  
> Questo script è stato realizzato **esclusivamente per scopi educativi e di test su dispositivi propri**.  
> L'utilizzo di un keylogger per monitorare attività di altri utenti **senza il loro consenso è illegale** in molte giurisdizioni.  
> **L'autore declina ogni responsabilità per usi impropri di questo codice.**

---

## Funzionalità

- Registra ogni tasto premuto sulla tastiera
- Riconosce e formatta correttamente tasti speciali (`Spazio`, `Enter`, `Tab`, ecc.)
- Salva i log in un file locale (`log.txt`)  
  _(Percorso di default: `C:\Iltuopercorso`, modificabile nel codice)_

---

## Requisiti

- Python 3.x
- Libreria [`pynput`](https://pypi.org/project/pynput/)

Per installare `pynput`, esegui il comando:

```bash
pip install pynput
```

---

## Utilizzo

1. Clona il repository o copia il codice nel tuo ambiente locale.
2. (Facoltativo) Modifica il percorso di salvataggio del file di log nel codice, se necessario.
3. Esegui lo script Python:

```bash
python keylogger.py
```

Il programma inizierà a registrare le battiture e a scriverle nel file `log.txt`.

> ❌ Premi `Ctrl+C` per interrompere manualmente il programma.

---

## Note

- Il file di log viene creato automaticamente se non esiste.
- Per motivi di sicurezza, **non condividere né eseguire** questo codice su dispositivi di cui non hai il controllo completo.

---

## Disclaimer legale

Questo software è fornito **esclusivamente a fini didattici**.  
L'uso non autorizzato per raccogliere dati personali può costituire **violazione delle leggi sulla privacy**.  
Utilizzalo **solo su sistemi di tua proprietà** o con il **consenso esplicito** del proprietario.
