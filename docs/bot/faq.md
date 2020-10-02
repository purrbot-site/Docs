[Discord]: https://purrbot.site/discord
[nekos.life]: https://nekos.life
[patreon]: https://patreon.com/andre_601
[invite]: https://purrbot.site/invite

This page contains commonly asked questions.  
Please read it carefully to prevent issues. If you can't find an answer to your question, feel free to join our [Discord] and ask there.

----
??? question "What are the default settings?"
    The bot has the following default settings:
    
    - Prefix: `.`
    - Welcome channel: `none`
    - Welcome background: [`color_white`](../welcome-images#color_white)
    - Welcome icon: [`purr`](../welcome-images#purr)
    - Welcome message: `Welcome {mention}!`
    - Language: `en (english)`

----
??? question "How do I use the welcome feature?"
    See the page about [setting up a welcome channel](../welcome-channel) for how you can do this.

----
??? question "From where are the images?"
    The images are hosted on our own site (https://purrbot.site) and provided through our [own API](/api).  
    We originally used the API from nekos.life but decided to move to a own one, for the simple reason of having more control over what images are shown.
    
    We constantly expand our collection of images and are happy over every submitted image from you, if they meet our requirements.  
    If you find images on our site, that break the ToS of Discord (i.e. depicting NSFW-Lolis), let us know about this, by either joining our [Discord server][discord] or sending an E-Mail at support@purrbot.site!  
    Please provide the full image-link when reporting it to us, so that we can properly remove it.

----
??? question "Who/What is \*Snuggle\* and can I invite her?"
    \*Snuggle\* is the Beta-Version of \*Purr\* and is used to test new commands/features before \*Purr\* is receiving them.  
    She **cannot** be invited through normal ways.  
    To invite her will you need to be a [Patreon Member][patreon] of the highest tier (Catnip) and contact Andre_601.  
    He will then join your Discord, where you want \*Snuggle\* to be and invites her (You need to temporary give him `manage server` permission for this).

----
??? question "Why does the bot not work with Administrator?"
    When you gave \*Purr\* the `Administrator` permission will she refuse to perform any command and send an error message instead.  
    This was essentially made to force people into setting permissions up properly, since just giving Administrator is not something good to do.
    If you don't want to manually set up \*Purr\* with all required permissions, invite her using [this invite][invite] to have a \*Purr\* role with all required permissions set up.

----
??? question "On what is the bot/website hosted?"
    The bot is hosted on a VPS running `Ubuntu 18.04` and with `Java 11 (OpenJDK)`.  
    It uses RethinkDB as database.
    
    The website is hosted on the same VPS using Nginx.

----
??? question "Why does the bot react with `:cancel:` when using a comman?"
    This will happen when the bot lacks the `Send Message` permission (But is able to react).  
    Please make sure to give the right permissions for the bot to work properly!
