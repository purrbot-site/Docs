---
title: Einrichten
description: Wie du das Willkommenssystem einrichten kannst.
---

Der Willkommenskanal erlaubt es dir, Benutzer mit einer Nachricht und Bild zu begrüssen, wenn diese den Server betreten.

/// info | Hinweise
Bevor du den Kanal einrichtest, stelle sicher, dass du folgenden Dinge überprüft hast:

- Du hast `Server verwalten` Berechtigungen oder bist der Servereigentümer.
- Der Bot hat `Nachrichten senden` und `Dateien anhängen` Berechtigungen für den kanal, in welchem es die Willkommensnachrichten zeigen soll.

Der einfachheit halber werden die gezeigten Befehle den Standardpräfix (`p.`) verwenden.  
Wenn du einen anderen Präfix gesetzt hast, verwende diesen.
///

/// details | Video Tutorial (Englisch)
    type: youtube

Hier ist ein Video welcher die unten stehenden Schritte erklärt.

<iframe width="560" height="315" src="https://www.youtube.com/embed/vfhSj-4PF1A" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
///

## Schritt 1: Einen Kanal setzen {: #step-1 }

Du musst zuerst den Kanal setzen, bevor Leute begrüssen kannst.  
Um dies zu tun, führe `p.welcome channel set #kanal` aus, bei welchem `#kanal` der Kanal ist, welchen du zum begrüssen von Leuten verwenden willst.

Setze diese Einstellung mit `p.welcome channel reset` zurück.

## Schritt 2: Einen Hintergrund setzen {: #step-2 }

Setze einen Hintergrund welches im Bild verwendet wird.  
Der Befehl ist `p.welcome bg set <hintergrund>` wo `<hintergrund>` ein [gültiger Hintergrund](welcome-images.md#backgrounds) ist.

Setze diese Einstellung mit `p.welcome bg reset` zurück.

## Schritt 3: Ein Icon setzen {: #step-3 }

Du kannst ein Icon setzen, welches auf der rechten seite des Bildes angezeigt wird.  
Vewende `p.welcome icon set <icon>` wo `<icon>` ein [gültiges Icon](welcome-images.md#icons) ist.

Setze diese Einstellung mit `p.welcome icon reset` zurück.

## Schritt 4: Eine Schriftfarbe setzen {: #step-4 }

Die Standardschriftfarbe ist nicht auf allen Hintegründen sichtbar. Darum kannst du diese mit `p.welcome color set <farbe>` ändern.  
`<farbe>` muss entweder `hex:rrggbb`, `rgb:r,g,b` oder `random` sein.

Setze diese Einstellung mit `p.welcome color reset` zurück.

## Schritt 5: Eine Nachricht setzen {: #step-5 }

Du kannst deine ganz eigene Willkommensnachricht setzen, welche zusammen mit dem Bild gezeigt wird.  
Um dies zu tun, verwende `p.welcome msg set <nachricht>` wo `<nachricht>` alles sein kann, was du willst.

### Platzhalter { #placeholders }

| Platzhalter:                                | Beschreibung:                                                                       | Beispiel:        |
|---------------------------------------------|-------------------------------------------------------------------------------------|------------------|
| `{count}` / `{members}`                     | Die aktuelle Anzahl an Servermitgliedern auf dem Server.                            | 1000             |
| `{count_formatted}` / `{members_formatted}` | Die aktuelle Anzahl an Servermitgliedern auf dem Server, aber formatiert.           | 1,000            |
| `{guild}` / `{server}`                      | Der Servername.                                                                     | EinDiscord       |
| `{mention}`                                 | Erwähnung des Benutzers, welcher den Server betreten hat.                           | @EinBenutzer     |
| `{name}` / `{username}`                     | Name des Benutzers, welcher den Server betreten hat.                                | EinBenutzer      |
| `{c_mention:<id>}`                          | Erwähnung des angegebenen Kanals per ID. Funktioniert mit Text und Sprachkanälen.   | #EinKanal        |
| `{c_name:<id>}`                             | Name des angegebenen Kanals per ID. Funktioniert mit jedem Kanaltyp und Kategorien. | EinKanal         |
| `{r_mention:<id>}`                          | Erwähnung der angegebenen Rolle per ID.                                             | @EineRolle       |
| `{r_name:<id>}`                             | Name der angegebenen Rolle per ID.                                                  | EineRolle        |
| `{tag}`                                     | Der Tag des Benutzers, welcher den Server betreten hat.                             | EinBenutzer#1234 |

Setze diese Einstellung mit `p.welcome bg reset` zurück.

## Finaler Schritt: Testen {: #final-step }

Du kannst die aktuelle Nachricht und das aktuelle Bild sehen, indem du `p.welcome test` verwendest.  
Dies erstellt eine Nachricht ähnlich der, welche für beitretende Benutzer gezeigt wird.
