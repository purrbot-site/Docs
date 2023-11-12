---
title: Selbsthosting
description: Möchtest du den Bot selbst hosten? Diese Seite erklärt die Details.
---

[MIT-License]: https://github.com/Andre601/PurrBot/blob/master/LICENSE

[RethinkDB]: https://rethinkdb.com

[PurrBot.java]: https://github.com/purrbot-site/PurrBot/blob/master/src/main/java/site/purrbot/bot/PurrBot.java
[HttpUtil.java]: https://github.com/purrbot-site/PurrBot/blob/master/src/main/java/site/purrbot/bot/util/HttpUtil.java
[IDs.java]: https://github.com/Andre601/PurrBot/blob/master/src/main/java/site/purrbot/bot/constants/IDs.java
[Emotes.java]: https://github.com/Andre601/PurrBot/blob/master/src/main/java/site/purrbot/bot/constants/Emotes.java
[Roles.java]: https://github.com/Andre601/PurrBot/blob/master/src/main/java/site/purrbot/bot/constants/Roles.java
[Links.java]: https://github.com/Andre601/PurrBot/blob/master/src/main/java/site/purrbot/bot/constants/Links.java

[random.json]: https://github.com/Andre601/PurrBot/blob/master/src/main/resources/random.json
[data.json]: https://github.com/Andre601/PurrBot/blob/master/src/main/resources/data.json
[lang-files]: https://github.com/Andre601/PurrBot/blob/master/src/main/resources/lang

Einige von euch möchten eventuell den Bot auf ihrem eigenen VPS/Server hosten.  
Diese Seite erklärt, wie du den Bot für dich selber hosten kannst.

/// warning | Wichtig!
Durch das Selbsthosten des Bots erklärst du dich mit den folgenden Bedingungen einverstanden:

- Du follgst der [MIT Lizens][MIT-License] des Bots.
    - Das bedeutet, dass du Credits an den original Autor (Andre_601) gibst und den Code nicht als deinen eigenen ausgibst.
- Du akzeptierst und bestätigst, dass du keinen Support für deinen selbst gehosteten Bot erhälst.
///

## Vorraussetzungen { #requirements }
Bevor du den Bot hosten kannst musst du sicherstellen, dass die folgenden Vorraussetzungen erfüllt sind.

### RethinkDB
Du musst [RethinkDB] installiert und aktiv auf deinem Server haben, auf welchem der Bot später laufen wird.  
Dies beinhaltet das erstellen aller nötigen Datenbanken und Tabellen, welche du später in der config.json setzt.

### Java
Du musst **mindestens** Java 11 installiert und funktionsfähig haben. Neuere Versionen von Java sollten auch funktionieren.

### Einrichten { #setup }
Wenn du sichergestellt hast, dass die [Vorraussetzungen](#requirements) erfüllt sind, kannst du mit dem vorbereiten des Codes weitermachen.

### Klone das Repository {: #clone-repository }
Klone/Forke das PurrBot Repository, sofern du dies nicht bereits getan hast, und öffne es in deiner bevorzugten IDE.

### Mache änderungen am Code {: #change-code }
Du musst bestimmte Abschnitte des Codes ändern, um Fehler zu verhindern.  
Alternativ kannst du den "beta" Modus in der config.json auf `true` stellen, um den Bot im Beta-Modus zu benutzen, welche bestimmte Funktionen wie beispielsweise das posten von Statistiken auf Botlisten deaktiviert.

Wenn du änderungen am Code vornimmst, solltest du die folgenden Code-Zeilen in [PurrBot.java] entfernen oder auskommentieren:

```java title="PurrBot.java"
public void startUpdater(){
    scheduler.scheduleAtFixedRate(() -> {
        getShardManager().setActivity(Activity.of(
            Activity.ActivityType.WATCHING,
            getMessageUtil().getBotGame(getShardManager().getGuildCache().size())
        ));
        
        if(isBeta()) // (1)
            return;
        
        long guilds = getShardManager().getGuildCache().size();
        long shards = getShardManager().getShardCache().size();
        
        logger.info("Posting Guild Stats to Bot lists...");
        for(HttpUtil.BotList botList : HttpUtil.BotList.values()){
            getHttpUtil().postServerStats(
                "*Purr*",
                "6875",
                guilds,
                shards,
                botList,
                getFileManager().getString("config", botList.getTokenPath())
            ).whenComplete((botListResult, ex) -> {
                if(botListResult == null || !botListResult.isSuccess() || ex != null){
                    logger.warn("Error while posting Guild stats to bot list {}!", botList.getName());
                    if(botListResult == null){
                        logger.warn("BotListResult is null!");
                        return;
                    }
                    
                    if(ex != null){
                        ex.printStackTrace();
                        return;
                    }
                    
                    logger.info("Response Code: {}", botListResult.getResponseCode());
                    logger.info("Response Message: {}", botListResult.getResponseMessage());
                    return;
                }
                
                logger.info("Successfully posted stats to {}!", botListResult.getBotList());
            });
        }
    }, 1, 5, TimeUnit.MINUTES);
}
```

  1. Um das Posten auf Botlisten zu deaktivieren, setze den Bot entweder in den Beta-Modus durch die [`config.json`](#config) oder setze alles nach diesem if und vor `}, 1, 5, TimeUnits.MINUTES);` in Kommentare.  
  Du kannst auch die `BotList` Enum in der [`HttpUtil.java`][HttpUtil.java] aktualisieren um auf anderen Botlisten zu posten.

### Verschiedene Classes ändern {: #update-classes }
Du musst verschiedene Werte in bestimmten Classes ändern, um sicherzustellen, dass deine Version ohne Probleme funktioniert.  
Im detail musst du Inhalte folgender Classes ändern:

- [`IDs.java`][IDs.java] (Enthält verschiedene IDs von Benutzern und Gilden)
- [`Emotes.java`][Emotes.java] (Enthält verschiedene Emotes welche in Befehlen verwendet werden)
- [`Links.java`][Links.java] (Enthält verschiedene Links vom Bot)

### Jar Datei erstellen {: #build-jar }
Wenn du fertig mit deinen änderungen bist, vergiss nicht `gradlew clean shadowJar` auszuführen um eine geshadete Jar zu erstellen, welche alle nötigen Abhängigkeiten hat.

### Config.json {: #config }
Die `config.json` ist die Hauptdatei des Bots in welcher du verschiedenste informationen setzt, welche durch den Bot verwendet werden.  
Bei der ersten einrichtung wird es die Datei mit folgenden Standardwerten erstellen.

/// details | Standard config.json
    type: info

```json
{
  "bot-token": "TOKEN",
  
  "beta": false,
  "debug": false,
  
  "webhooks": {
    "guild": "guild-webhook-url",
    "log": "log-webhook-url"
  },
  
  "tokens": {
    "fluxpoint-dev": "fluxpoint-dev-token",
    
    "discord-bots-gg": "dbgg-token",
    "botlist-space": "botlist-token",
    "discordextremelist-xyz": "debl-token",
    "discordservices-net": "discordservices-net-token"
  },
  
  "database": {
    "ip": "127.0.0.1",
    "name": "DatabaseName",
    "guildTable": "GuildTable"
  }
}
```
///

Beachte dass du nicht werte für alle Optionen in der config.json setzen musst.
Sofern du die vorherigen Schritte zum vorbereiten des Bots befolgt hast, musst du nur die folgenen Optionen bearbeiten:

| Option:                | Value required:                                                                    |
|------------------------|------------------------------------------------------------------------------------|
| `bot-token`            | Gültiger Bot-Token deiner Applikation zum einloggen.                               |
| `webhooks.guild`       | Eine URL für einen Discord-Webhook zum loggen von beitritt und verlssaen des Bots. |
| `webhooks.log`         | Eine URL für einen Discord-Webhook zum loggen von Bot dis- und reconnects.         |
| `tokens.fluxpoint-dev` | Gültiger Berechtigungstoken für die Fluxpoint.dev API.                             |
| `database.ip`          | Domain/IP der RethinkDB Datenbank.                                                 |
| `database.name`        | Name der Datenbank, welche du erstellt hast.                                       |
| `database.guildTable`  | Name der Tabelle, welche du zum speichern von Gildeneinstellungen erstellt hast.   |

### Andere Dateien { #other-files }
Der Bot besitzt auch andere Dateien, welche du nach Herzenslust bearbeiten kannst.

- [`random.json`][random.json] enthält verschiedenste Nachrichten und Links welche für (oftmals) zufällige Antworten benutzt werden.
- [`data.json`][data.json] enthält Daten wie aktuelle Gilden-Blacklist, spezielle Benutzer und mehr.
- Verschiedenste [Sprachdateien][lang-files] welche für die verschiedenen Befehle des Bots verwendet werden.
