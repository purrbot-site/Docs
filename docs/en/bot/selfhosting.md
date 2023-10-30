---
title: Selfhosting
description: Want to selfhost the Bot? This page explains the details.
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

Some of you may want to selfhost the bot on your own VPS/server.  
This page explains how you can selfhost the bot for yourself.

!!! warning "Important!"
    By selfhosting the bot will you agree to the following terms:
	
    - You follow the [MIT-License] of the bot.
        - This means that you give credit to the original author (Andre_601) and won't claim this code as your own.
    - You aknowledge and agree that you won't receive any support for your selfhosted bot.

## Requirements
Before you can run the bot will you need to make sure that the following requirements are met.

### RethinkDB
You need to have [RethinkDB] installed and running on your server, where the bot will later run.  
This also includes creating databases and tables to later set in the config.json.

### Java
You need **at least** Java 11 to be installed and working. Newer versions of Java should work too.

## Setup
When you made sure, that the [requirements](#requirements) are met, can you continue with preparing the code.

### Clone the repository {: #clone-repository }
Clone/Fork the PurrBot repository, if you didn't already and open it in your preferred IDE.

### Make changes to code {: #change-code }
You need to alter specific parts of the code, to prevent errors from appearing.  
Alternatively could you set "beta" in the config.json to true, to set the bot as Beta-Bot, disabling certain functionalities such as posting stats to Bot Lists.

When making changes to the code should you remove or uncomment the following code-snippets in [PurrBot.java]:

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

1.  To disable posting to Bot list, either set the bot into beta mode through the [`config.json`](#config) or put everything after this if and before the `}, 1, 5, TimeUnit.MINUTES);` into comments.  
    You can also update the `BotList` enum in the [`HttpUtil,java`][HttpUtil.java] to post to different bot lists.

### Update some classes {: #update-classes }
You need to update values in specific classes to make your version work without issues.  
Namely you have to alter the content of the following classes:

- [`IDs.java`][IDs.java] (Contains various IDs of users or Guilds)
- [`Emotes.java`][Emotes.java] (Contains different emotes used in commands)
- [`Links.java`][Links.java] (Contains various links of the bot)

### Build jar file {: #build-jar }
When you're done with your changes, make sure to execute `gradlew clean shadowJar` to build a shaded jar containing all dependnencies required.

### Config.json {: #config }
The `config.json` is the core file of the bot in which you set various different information that will be used by the bot.  
On first startup will it generate with the below default values.

??? note "Default Config.json"
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

Note that you don't have to set values for every option in the config.json.  
If you followed the previous step on preparing the bot will you only need to set the following options:

| Option:                | Value required:                                                     |
| ---------------------- | ------------------------------------------------------------------- |
| `bot-token`            | Valid Bot-token of your Bot-application to login.                   |
| `webhooks.guild`       | A URL to a Discord webhook for logging joins and leaves of the bot. |
| `webhooks.log`         | A URL to a Discord webhook for logging dis/reconnects of the bot.   |
| `tokens.fluxpoint-dev` | Valid Authentication-token for the image-API of Fluxpoint.dev       |
| `database.ip`          | Domain/IP of the RethinkDB server.                                  |
| `database.name`        | Name of the database you created.                                   |
| `database.guildTable`  | Name of the table you created to store guild settings.              |

### Other files
The bot also has other files, which you can alter to your liking.

- [`random.json`][random.json] contains various messages and links used for (often) random responses.
- [`data.json`][data.json] contains data such as current guild blacklist, special users and more.
- Various [lang-files] used for the different command responses of the bot.
