import discord
from discord.ext import commands
import asyncio
import gpiozero

motor = gpiozero.PWMOutputDevice(pin=12, active_high=True, frequency=500)
 
enabl = gpiozero.DigitalOutputDevice(21)
motor.off()
enabl.off()

intents = discord.Intents.default()
intents.message_content = True

msgtodel = '' #the remote to be deleted when you can't get enough anymore
bot = commands.Bot(command_prefix="-=", intents=intents)
useronly = 'urselfonlyuwu'


async def status_task():
    while(True):
        await asyncio.sleep(60)
        await bot.change_presence(status=discord.Status.online, activity=discord.Game("with your ass UwO~"))



@bot.event
async def on_ready():
    print("Ready to get dominated?")
    for server in bot.guilds:
        await bot.tree.sync(guild=discord.Object(id=server.id))
    bot.loop.create_task(status_task())
    await bot.change_presence(status=discord.Status.online, activity=discord.Game("with your ass UwO~"))



@bot.hybrid_command(name='tease', description="okay~ you really want to do this eh?")
async def sutato(ctx):
    global useronly
    print("huh")
    if str(ctx.message.author.id) == useronly: #is it you?
        await ctx.send("Okay master~")
        await asyncio.sleep(5)
        await potns(ctx)
    else:
        await ctx.send("bitch")



@bot.hybrid_command(name='letsplay', description="nnn")
async def potns(ctx):
    global msgtodel
    
    embed = discord.Embed(title='🟥🟥🟥OFF🟥🟥🟥', colour=0x86cecb, type="rich")
    embed.set_author(name=bot.user.display_name)
    embed.set_thumbnail(url=bot.user.display_avatar)

    embed.add_field(name="Intensity", value="Level 1", inline=True)
    embed.add_field(name="Functions", value="Constant", inline=True)

    msgtodel = await ctx.send(embed=embed, view=Buttonz())
    
    '''
    view = discord.ui.View() # Establish an instance of the discord.ui.View class
    style = discord.ButtonStyle.blurple  # The button will be gray in color
    item = discord.ui.Button(style=style, label="Read the docs!")  # Create an item to pass into the view class.
    view.add_item(item=item)  # Add that item into the view class
    await ctx.send("This message has buttons!", view=view)  # Send your message with a button.
    '''


@bot.hybrid_command(name='onigiri', description='you pussy, you stopped it')
async def stopuuu(ctx):
    global msgtodel, motor, enabl
    motor.off()
    enabl.off()
    await msgtodel.delete()
    await ctx.send("Did you came? If not, its punishment time")

class Buttonz(discord.ui.View):
    ntuo = False #toggle for the power on
    speedo = 1 #intensity

    def __init__(self, *, timeout=180):
        
        super().__init__(timeout=timeout)
    
    def update_embed(self): #this one updates embeds everytime a button is pressed
        global speedo, ntuo
        if not self.ntuo: #if its False its off so we need this to be notted
            statnus = "🟥🟥🟥OFF🟥🟥🟥"
        else:
            statnus = "🟩🟩🟩ON🟩🟩🟩"

        embed = discord.Embed(title=statnus, colour=0x86cecb, type="rich")
        embed.set_author(name=bot.user.display_name)
        embed.set_thumbnail(url=bot.user.display_avatar)

        embed.add_field(name="Intensity", value="Level " + str(self.speedo), inline=True)
        embed.add_field(name="Functions", value="Constant", inline=True)
        return embed

    @discord.ui.button(label="<<<<<",style=discord.ButtonStyle.blurple) # Decrease L=Dec
    async def apuuu_button(self,interaction:discord.Interaction,button:discord.ui.Button):
        global speedo
        if self.speedo > 1: #if the intensity is less than 1 then don't decrement 
            self.speedo -= 1
            motor.value = float(self.speedo)/10
        await interaction.response.edit_message(embed=self.update_embed(),view=self)

    @discord.ui.button(label="💚💚💚",style=discord.ButtonStyle.danger) # Toggle on or off
    async def toggle_button(self,interaction:discord.Interaction,button:discord.ui.Button):
        global ntuo, speedo
        if self.ntuo: #a toggle for seting ntuo boolean
            self.ntuo = False
            motor.off()
            enabl.off()
            motor.value = float(self.speedo)/10
            await interaction.response.edit_message(embed=self.update_embed(),view=self)
        else:
            self.ntuo = True
            motor.on()
            enabl.on()
            motor.value = float(self.speedo)/10
            await interaction.response.edit_message(embed=self.update_embed(),view=self)



    @discord.ui.button(label=">>>>>",style=discord.ButtonStyle.blurple) # Increase R=Inc
    async def dow_button(self,interaction:discord.Interaction,button:discord.ui.Button):
        global speedo
        if self.speedo < 10: #only increase when its less than 10
            self.speedo += 1
            motor.value = float(self.speedo)/10
        await interaction.response.edit_message(embed=self.update_embed(),view=self)

    '''
    @discord.ui.button(label="AFJKLAFLK",style=discord.ButtonStyle.blurple) # or .primary
    async def testUI_button(self,interaction:discord.Interaction,button:discord.ui.Button):
        embed = discord.Embed(title="🟥🟥🟥OFF🟥🟥🟥", colour=0x86cecb, type="rich")
        embed.set_author(name=bot.user.display_name)
        embed.set_thumbnail(url=bot.user.display_avatar)

        embed.add_field(name="Intensity", value="Level 5", inline=True)
        embed.add_field(name="Functions", value="Constant", inline=True)

        await interaction.response.edit_message(embed=embed,view=self)
    '''


bot.run('token')