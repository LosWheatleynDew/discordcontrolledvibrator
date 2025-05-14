import discord
from discord.ext import commands
import asyncio
import gpiozero

motor = gpiozero.PWMOutputDevice(pin=12, active_high=True, frequency=500)

#making sure the motor is off
enabl = gpiozero.DigitalOutputDevice(21)
motor.off()
enabl.off()

intents = discord.Intents.default()
intents.message_content = True

msgtodel = '' #the remote to be deleted when you can't get enough anymore
bot = commands.Bot(command_prefix="-=", intents=intents)
useronly = 'idofuser' #get the user's id for the tease command so you can be the only one to activate it unless you use letsplay~


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
    
    if str(ctx.message.author.id) == useronly: #is it you?
        await ctx.send("Okay master~")
        await asyncio.sleep(5)
        await potns(ctx)
    else:
        await ctx.send("bitch")



@bot.hybrid_command(name='letsplay', description="nnn")
async def potns(ctx):
    global msgtodel
    
    '''
    embed = discord.Embed(title='🟥🟥🟥OFF🟥🟥🟥', colour=0x86cecb, type="rich")
    embed.set_author(name=bot.user.display_name)
    embed.set_thumbnail(url=bot.user.display_avatar)

    embed.add_field(name="Intensity", value="Level 1", inline=True)
    embed.add_field(name="Functions", value="Constant", inline=True)
    '''

    msgtodel = await ctx.send(embed=update_embed(), view=ConstButtonz())
    
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
    


#these are global values so the embed functions and classes can read to each other
    
ntuo = False #toggle for the power on
selcVal = 1 #the type of function to be used
typeVal = ['Constant', "Pulse", "Wave"]
speedo = 1 #intensity for constants
freq = 1 #frequency of wave
onT = 1 #for pulsing when its on in seconds
offT = 1 #for pulsing when its off in seconds


def update_embed(): #this one updates embeds everytime a button is pressed FOR CONSTANT FUNCTION
        global typeVal, selcVal, ntuo, speedo
        if not ntuo: #if its False its off so we need this to be notted
            statnus = "🟥🟥🟥OFF🟥🟥🟥"
        else:
            statnus = "🟩🟩🟩ON🟩🟩🟩"

        embed = discord.Embed(title=statnus, colour=0x86cecb, type="rich")
        embed.set_author(name=bot.user.display_name)
        embed.set_thumbnail(url=bot.user.display_avatar)

        embed.add_field(name="Intensity", value="Level " + str(speedo), inline=True)
        embed.add_field(name="Function", value=typeVal[selcVal-1], inline=True)
        return embed

def update_embed2(): #this one updates embeds everytime a button is pressed FOR PULSE FUNCTION
        global typeVal, selcVal, ntuo, onT, offT
        if not ntuo: #if its False its off so we need this to be notted
            statnus = "🟥🟥🟥OFF🟥🟥🟥"
        else:
            statnus = "🟩🟩🟩ON🟩🟩🟩"

        embed = discord.Embed(title=statnus, colour=0x86cecb, type="rich")
        embed.set_author(name=bot.user.display_name)
        embed.set_thumbnail(url=bot.user.display_avatar)
        
        embed.add_field(name="On Time", value=str(onT) + " Second(s)", inline=True)
        embed.add_field(name="Off Time", value=str(offT) + " Second(s)", inline=True)
        embed.add_field(name="Function", value=typeVal[selcVal-1], inline=True)
        return embed

def update_embed3(): #this one updates embeds everytime a button is pressed FOR WAVE FUNCTION 
        global typeVal, selcVal, ntuo, freq
        if not ntuo: #if its False its off so we need this to be notted
            statnus = "🟥🟥🟥OFF🟥🟥🟥"
        else:
            statnus = "🟩🟩🟩ON🟩🟩🟩"

        embed = discord.Embed(title=statnus, colour=0x86cecb, type="rich")
        embed.set_author(name=bot.user.display_name)
        embed.set_thumbnail(url=bot.user.display_avatar)
        
        embed.add_field(name="Frequency", value=str(freq)+"hz",  inline=True)
        embed.add_field(name="Function", value=typeVal[selcVal-1], inline=True)
        return embed

class Select(discord.ui.Select): #the select option is the menu that allows the user to choose what type they want
    global selecVal, ntuo, speedo, freq, onT, offT
    typeVal = ['Constant', "Pulse", "Wave"]
    def __init__(self):
        options=[
            discord.SelectOption(label="Constant",emoji='📶',description="Constant Levels", default=(selcVal==1)),
            discord.SelectOption(label="Pulse",emoji='💓',description="Interminted Pulses (Square Wave)", default=(selcVal==2)),
            discord.SelectOption(label="Wave",emoji='🌊',description="Sine Waves", default=(selcVal==3))
            ]
        super().__init__(max_values=1,min_values=1,options=options)


    async def callback(self, interaction: discord.Interaction):
        global selcVal, ntuo, speedo, freq, onT, offT
        match self.values[0]:
            case 'Constant':
                #print("const")
                selcVal = 1
                if ntuo: #checks to see if the vibrator is already on if so update to its function
                    motor.on()
                    motor.value = float(speedo)/10
                await interaction.response.edit_message(embed=update_embed(),view=ConstButtonz())
            case 'Pulse':
                #print("pulse")
                selcVal = 2
                if ntuo:
                    motor.blink(onT,offT,0,0,None,True)
                await interaction.response.edit_message(embed=update_embed2(), view=PulseButtonz())
            case 'Wave':
                #print("wave")
                selcVal = 3
                if ntuo:
                    motor.pulse(1/(2*freq),1/(2*freq), None, True)
                await interaction.response.edit_message(embed=update_embed3(), view=WaveButtonz())


class PulseButtonz(discord.ui.View): #for pulses
    global selcVal, ntuo, freq, onT, offT

    def __init__(self, *, timeout=180):

        super().__init__(timeout=timeout)
        self.add_item(Select())  
    
    @discord.ui.button(label="<<<<<ON",style=discord.ButtonStyle.blurple) #On time dec
    async def dowON_button(self,interaction:discord.Interaction,button:discord.ui.Button):
        global onT, offT
        if onT > 0.25:
            onT -= 0.25
            motor.blink(onT,offT,0,0,None,True)
        await interaction.response.edit_message(embed=update_embed2(),view=self)
        
    @discord.ui.button(label="ON>>>>>",style=discord.ButtonStyle.blurple) #off time inc
    async def apuON_button(self,interaction:discord.Interaction,button:discord.ui.Button):
        global onT, offT
        if onT < 10:
            onT += 0.25
            motor.blink(onT,offT,0,0,None,True)
        await interaction.response.edit_message(embed=update_embed2(),view=self)
        
    @discord.ui.button(label="💚💚💚",style=discord.ButtonStyle.danger) # Toggle on or off
    async def toggle_button(self,interaction:discord.Interaction,button:discord.ui.Button):
        global ntuo, onT, offT
        if ntuo: #a toggle for seting ntuo boolean
            ntuo = False
            motor.off()
            enabl.off()
           
            await interaction.response.edit_message(embed=update_embed2(),view=self)
        else:
            ntuo = True
            
            enabl.on()
            motor.blink(onT,offT,0,0,None,True)
            await interaction.response.edit_message(embed=update_embed2(),view=self)
    
    @discord.ui.button(label="<<<<<OFF",style=discord.ButtonStyle.blurple) #off time dec
    async def dowOFF_button(self,interaction:discord.Interaction,button:discord.ui.Button):
        global onT, offT
        if offT > 0.25:
            offT -= 0.25
            motor.blink(onT,offT,0,0,None,True)
        await interaction.response.edit_message(embed=update_embed2(),view=self)
        
    @discord.ui.button(label="OFF>>>>>",style=discord.ButtonStyle.blurple) #off time inc
    async def apuOFF_button(self,interaction:discord.Interaction,button:discord.ui.Button):
        global onT, offT
        if offT < 10:
            offT += 0.25
            motor.blink(onT,offT,0,0,None,True)
        await interaction.response.edit_message(embed=update_embed2(),view=self)

class WaveButtonz(discord.ui.View): #sine waves
    global selcVal, ntuo, freq

    def __init__(self, *, timeout=180):

        super().__init__(timeout=timeout)
        self.add_item(Select())  

    @discord.ui.button(label="<<<<<",style=discord.ButtonStyle.blurple) # Decrease L=Dec
    async def apuuu_button(self,interaction:discord.Interaction,button:discord.ui.Button):
        global freq
        if freq > 0.25: #if the intensity is less than 1 then don't decrement 
            freq -= 0.25
            motor.pulse(1/(2*freq),1/(2*freq), None, True)
        await interaction.response.edit_message(embed=update_embed3(),view=self)

    @discord.ui.button(label="💚💚💚",style=discord.ButtonStyle.danger) # Toggle on or off
    async def toggle_button(self,interaction:discord.Interaction,button:discord.ui.Button):
        global ntuo, freq
        if ntuo: #a toggle for seting ntuo boolean
            ntuo = False
            motor.off()
            enabl.off()
           
            await interaction.response.edit_message(embed=update_embed3(),view=self)
        else:
            ntuo = True
            
            enabl.on()
            motor.pulse(1/(2*freq),1/(2*freq), None, True)
            await interaction.response.edit_message(embed=update_embed3(),view=self)



    @discord.ui.button(label=">>>>>",style=discord.ButtonStyle.blurple) # Increase R=Inc
    async def dow_button(self,interaction:discord.Interaction,button:discord.ui.Button):
        global freq
        if freq < 10: #only increase when its less than 10
            freq += 0.25
        motor.pulse(1/(2*freq),1/(2*freq), None, True)    
        await interaction.response.edit_message(embed=update_embed3(),view=self)    
        
        
class ConstButtonz(discord.ui.View):
    global selcVal, ntuo, speedo
    
    
   
    def __init__(self, *, timeout=180):

        super().__init__(timeout=timeout)
        self.add_item(Select())

    @discord.ui.button(label="<<<<<",style=discord.ButtonStyle.blurple) # Decrease L=Dec
    async def apuuu_button(self,interaction:discord.Interaction,button:discord.ui.Button):
        global speedo
        if speedo > 1: #if the intensity is less than 1 then don't decrement 
            speedo -= 1
            motor.value = float(speedo)/10
        await interaction.response.edit_message(embed=update_embed(),view=self)

    @discord.ui.button(label="💚💚💚",style=discord.ButtonStyle.danger) # Toggle on or off
    async def toggle_button(self,interaction:discord.Interaction,button:discord.ui.Button):
        global ntuo, speedo
        if ntuo: #a toggle for seting ntuo boolean
            ntuo = False
            motor.off()
            enabl.off()
            motor.value = float(speedo)/10
            await interaction.response.edit_message(embed=update_embed(),view=self)
        else:
            ntuo = True
            motor.on()
            enabl.on()
            motor.value = float(speedo)/10
            await interaction.response.edit_message(embed=update_embed(),view=self)


    @discord.ui.button(label=">>>>>",style=discord.ButtonStyle.blurple) # Increase R=Inc
    async def dow_button(self,interaction:discord.Interaction,button:discord.ui.Button):
        global speedo
        if speedo < 10: #only increase when its less than 10
            speedo += 1
            motor.value = float(speedo)/10
        await interaction.response.edit_message(embed=update_embed(),view=self)




bot.run('Token')