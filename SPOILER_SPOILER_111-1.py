import discord
from discord.ext import commands
import typing


client = discord.Client(commands_prefix="$")

@client.event
async def on_ready():
    print("We are Online")
#Interaction menu
@client.event
async def on_message(message):
    message.content.lower()
    if message.author==client.user:
        return
    if message.content.startswith("Testing"):
        await message.channel.send("we are online.")
##to add "if message.content.startswith("What you say"):"
         ##"await message.channel.send("What she'll say")"
    if message.content.startswith("Hello Remi"):
         await message.channel.send("HI!!!")
    if message.content.startswith("$Whatcha Doing"):
         await message.channel.send("Nothing.How About you?")
    if message.content.startswith("$Good"):
         await message.channel.send("Glad To hear it")
    if message.content.startswith("$Bad"):
         await message.channel.send("Awwww Whats Wrong")
    if message.content.startswith("$Can I Fuck you"):
         await message.channel.send("Ewww. First off I dont know you. Second Why? and third...Ewww")
    if message.content.startswith("$Intro"):
         await message.channel.send("I'm a bot created by Shadowsinclaira#7286. Remi is just a name i was givien.")
    if message.content.startswith("$Nothing"):
         await message.channel.send("Like? I Know Your Doing something. You aint Slick.")
    if message.content.startswith("$Something"):
         await message.channel.send("You wanna Die?")
    if message.content.startswith("$No I do not wanna die"):
         await message.channel.send("I can make that happen you little Fucker")
    if message.content.startswith("$Lets Fuck"):
         await message.channel.send("Fuck...U. and Done you have been fucked")
    if message.content.startswith("ping"):
         await message.channel.send("pong")
    if message.content.startswith("$Who is your father"):
         await message.channel.send("@Shadowsinclaira")
    if message.content.startswith("$Who is Your Mother"):
         await message.channel.send("dont know")
    if message.content.startswith("$Im Good."):
         await message.channel.send("You wanna make it better?")
    if message.content.startswith("$Im Bad"):
         await message.channel.send("Then Lets make it good ok?")
    if message.content.startswith("Remi"):
         await message.channel.send("Yes")
    if message.content.startswith("$Can u roleplay?"):
         await message.channel.send("????Dont know")
    if message.content.startswith("Where is Leandre"):
         await message.channel.send("Doing something that doesnt involve you knowing")
    if message.content.startswith("$Favorite Color"):
         await message.channel.send("All of them")
    if message.content.startswith("$Can you help me"):
         await message.channel.send("Sure thing. But what.")
    if message.content.startswith("roles"):
         await message.channel.send("which one do you want?")
    if message.content.startswith("$Remi do you know the secrets of the world?"):
         await message.channel.send("no")
    if message.content.startswith("$Favorite Game"):
         await message.channel.send("I would play anything.....No serious would")
    if message.content.startswith("$Will you marry me"):
         await message.channel.send("I'm not real. im just a bot.")
    if message.content.startswith("$you Will marry me"):
         await message.channel.send(".........help me..........@admin")
    if message.content.startswith("$Why will you not marry me"):
         await message.channel.send("i am not human Dumb dumb.")
    if message.content.startswith("$Favorite Amine"):
         await message.channel.send("**Takes a deep breath**  Jojo")
    if message.content.startswith("$Eat a dick"):
         await message.channel.send("What dick?! You do not have one HELLOOOOOOO!!!!")
    if message.content.startswith("ogga booga gimme rice"):
         await message.channel.send("Fuck U Fuck U Go Nity Nite")
    if message.content.startswith("Remi are u real?"):
         await message.channel.send("I am as real as you want me to be")
    if message.content.startswith("how do you work?"):
         await message.channel.send("You could ask Shadowsinclaira but i can tell you. i can only say a few things but you want to add something or whatever Dm Shadowsinclaira or Mystical Pervert. To help me talk sometimes you'll have to use the $ but i should understand the basics....right?.....right? DAD")
    if message.content.startswith("Anything"):
         await message.channel.send("You wanted a role right? Choose. But no admin")
    if message.content.startswith("Filexia"):
         await message.channel.send("Bolden?")
    if message.content.startswith("Lets talk"):
         await message.channel.send("ok")
    if message.content.startswith("She knows about you now"):
         await message.channel.send("Well if she sees this tell her i said hi!!")
    if message.content.startswith("Faith called"):
         await message.channel.send("AAAWWWWW you mean the cute one?")
    if message.content.startswith("the cute one"):
         await message.channel.send("Faith King right?")
    if message.content.startswith("She is really good at smash"):
         await message.channel.send("oh really?")
    if message.content.startswith("owie"):
         await message.channel.send("Yikes....")
    if message.content.startswith("Can i be admin?"):
        await message.channel.send("Short answer no. Long answer, its only for people who are super choose to mystical pervert.")
##Ping and pong game
@client.event
async def ping(ctx):
    await ctx.send('pong')
 ##kick people

async def kick(ctx,member:discord.member,*,reason=None):
        await member.kick(reason=reason)
        await ctx.send(f"{member} was banned")
##ban people
@commands.has_any_role("The Akatsuki")
async def ban (ctx, member:discord.User=None, reason =None):
    if member == None or member == ctx.message.author:
        await ctx.channel.send("You cannot ban yourself")
        return
    if reason == None:
        reason = "We Don't force ideals here idiot!!!!!!!"
    message = f"You have been banned from {ctx.guild.name} for {reason}"
    await member.send(message)
    # await ctx.guild.ban(member, reason=reason)
    await ctx.channel.send(f"{member} is banned!")
##Clear Channel
@client.event
async def clear(ctx,amount=5):
    await ctx.channel.purge(limit=amount)
##New member info
@client.event
async def joined(ctx, *, member: discord.Member):
    await ctx.send('{0} joined on {0.joined_at}'.format(member))

##event set
async def set(ctx):
    input("What the name of the event?")
    input("What time to announce it?")
##tells you about roles
## When someone joins

async def on_memeber_join(member):
        print(f'{member} has joined a server.')
## When someone Leaves
        async def on_member_remove(member):
            print(f'{member} has left a server.')

##Checking YOUR DM

async def globally_block_dms(ctx):
    return ctx.guild is not None
##Water game
async def bottles(ctx, amount: typing.Optional[int] = 99, *, liquid="beer"):
    await ctx.send('{} bottles of {} on the wall!'.format(amount, liquid))

##SLAP A PERSON

async def slap(ctx, members: commands.Greedy[discord.Member], *, reason='no reason'):
    slapped = ", ".join(x.name for x in members)
    await ctx.send('{} just got slapped for {}'.format(slapped, reason))


client.run('NzE5MzMyNjY4MjMxMTIzMDU1.Xt14wA.qOiZTPdYZuVjE4LKLwO0Wr703jc')
