"""Emoji
Available Commands:
.emoji shrug
.emoji apple
.emoji :/
.emoji -_-"""

from telethon import events

import asyncio





@borg.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))

async def _(event):

    if event.fwd_from:

        return

    animation_interval = 4

    animation_ttl = range(0, 20)

    input_str = event.pattern_match.group(1)

    if input_str == "police":

        await event.edit(input_str)

        animation_chars = [
        
            "`Connecting To police Headquarters...`",
            "`Call Connected.`",
            "`police: Hello This is police HQ. Who is this?`",
            "`Me: Yo this is` @opgohil ,`Please Connect me to my lil bro,vishvdeep sinh`",
            "`User Authorised.`",
            "`Calling vishvdeep sinh`  `At +917943211234`",
            "`Private  Call Connected...`",
            "`Me: Hello Sir, Please report This user.`",    
            "`vishvdeep sinh: May I Know Who Is This?`",
            "`Me: Yo Brah, I Am` @opgohil ",
            "`vishvdeep sinh: OMG!!! Long time no see, Wassup Brother...\nI'll Make Sure That Guy reported and Get under arrest Within 24Hrs.`",
            "`Me: Thanks, See You Later Brah.`",
            "`vishvdeep sinh: Please Don't Thank Brah, police force Is Our's. Just Gimme A Call When You Become Free.`",
            "`Me: Is There Any Issue/Emergency???`",
            "`vishvdeep sinh: Yes bro, There Is A Bug In your software v69.6.9.\nI Am Not Able To Fix It. If Possible, Please Help Fix The Bug.`",
            "`Me: Send Me The App On My Account, I Will Fix The Bug & Send You.`",
            "`vishvdeep sinh: Sure Sur \nTC Bye Bye :)`",
            "`Private Call Disconnected.`"
        ]

        for i in animation_ttl:

            await asyncio.sleep(animation_interval)

            await event.edit(animation_chars[i % 20])
