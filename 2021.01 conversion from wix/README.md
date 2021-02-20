# Overview

Pende aveva questo sito: https://andreapendezzini.wordpress.com/ (che ore reindirizza a andreapendezzini.it).
Voleva aggiornare il sito, allora gli ho detto di farlo con Wix: https://andreapende.wixsite.com/sito 
Poi da Wix l'ho convertito in pagine statiche e messo su: https://puntonim.github.io/andreapendezzini.it/
Poi preso il dominio: https://andreapendezzini.it


# Come fare la conversione da sito Wix a pagine statiche

## Pre-requisiti: download da Wix

-   creare il sito su Wix
-   Wix usa react quindi caricare la pagina, cliccare in giro in modo che il js
    inizializzi tutti i componenti
-   inspect (con Chrome dev tools) e selezionare il tag <HTML>, click dx, edita e copia tutto
-   incolla il contenuto in `converter/html/index-desktop.html`
 
Stessa cosa per la versione mobile, ma quando ispezioni assicurati di vederlo in mobile.

## Trasformare Wix a static

Seguendo le istruzioni nei pre-requisiti abbiamo il sito Wix scaricato in `converter/html`.
Ora possiamo lanciare dei comandi per trasformare il sito in un vero sito statico:
```shell
$ cd converter
$ pipenv shell
$ pipenv install --dev
$ python parse.py
```
E verranno creati i files in `/docs`.
Pronti per un `git push`.


# Da fare

-   google analytics?
-   alt for images
-   download fonts?


