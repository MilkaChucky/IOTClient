# IoTClient
IoT kliens alkalmazás megvalósítása python nyelven.

## Fejlesztés
Amennyiben virtuális fejlesztő környezetet szeretnénk használni, hozzuk létre először azt, majd aktiváljuk:
```sh
$ python3 -m venv venv
$ source venv/bin/activate
```
Ezt követően, vagy az előző lépés kihagyásával (amennyiben globálisan akarjuk telepíteni a packaget), telepítsük a szükséges package-eket:
```sh
$ pip isntall -r requirements.txt
```

## Futtatás
A projekthez tartozó config.ini fájl egy példa fájl. Ennek alapján a felhasználó elkészítheti saját config.app.ini fájlját, amelyben megadott beállítások felülírják az alapértelmezett config.ini fájlban szereplő beállításokat.

> **Figyelem!** Amennyiben virtuális fejlesztő környezetet használunk, ne fejejtsük el azt aktiválni futtatás előtt a 
> ```sh
> $ source venv/bin/activate
> ``` 
> parancsal!

Az alkalmazás elindításához futtassuk a ```python IoTClient.py``` parancsot!
