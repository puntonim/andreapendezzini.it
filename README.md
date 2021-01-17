# Urls

https://andreapendezzini.it
https://andreapende.wixsite.com/sito 
https://puntonim.github.io/andreapendezzini.it/

DNS Record
```
@ 1800 IN A 185.199.108.153
@ 1800 IN A 185.199.109.153
@ 1800 IN A 185.199.110.153
@ 1800 IN A 185.199.111.153
www 1800 IN CNAME andreapendezzini.it.
```

# Come fare

-   creare il sito su Wix
-   Wix usa react quindi caricare la pagina, cliccare in giro in modo che il js
    inizializzi tutti i componenti
-   inspect (con Chrome dev tools) e selezionare il tag <HTML>, click dx, edita e copia tutto
-   incolla il contenuto in script/html/index-desktop.html
  
Stessa cosa per la versione mobile, ma quando ispezioni assicurati di vederlo in mobile.
Poi lancia:
```shell
$ cd scripts
$ pipenv shell
$ pipenv install --dev
$ python parse.py
```
E verranno creati i files in docs.
Pronti per essere pushati.


# Da fare

-   google analytics?
-   alt for images
-   download fonts?



# Copyright

Copyright 2021 Andrea Pendezzini and puntonim (https://github.com/puntonim). No License.
