from random import choice

from cogs.utils.random_text.text_template import TextTemplate


class CopulateRandomText(TextTemplate):


    @classmethod
    def request_accepted(cls, instigator=None, target=None):
        '''
        Valid copulation target
        '''

        return choice(cls.get_valid_strings([
            "{instigator.mention} and {target.mention} got frisky~",
            "{instigator.mention} and {target.mention} spent some alone time together ~~wink wonk~~",
            "{instigator.mention} and {target.mention} made sexy time together ;3",
            "{instigator.mention} and {target.mention} attempted to make babies.",
            "{instigator.mention} and {target.mention} tried to have relations but couldn't find the hole.",
            "{instigator.mention} and {target.mention} went into the wrong hole.",
            "{instigator.mention} and {target.mention} tried their hardest, but they came too early .-.",
            "{instigator.mention} and {target.mention} slobbed each other's knobs.",
            "{instigator.mention} and {target.mention} had some frisky time in the pool and your doodoo got stuck because of pressure.",
            "{instigator.mention} and {target.mention} had sex and you've contracted an STI. uh oh!",
            "{instigator.mention} and {target.mention} had sex but you finished early and now it's just a tad awkward.",
            "Jesus saw what {instigator.mention} and {target.mention} did.",
            "{instigator.mention} and {target.mention} did a lot of screaming.",
            "{instigator.mention} and {target.mention} had sex and pulled a muscle. No more hanky panky for a while!",
            "{instigator.mention} and {target.mention}… just please keep it down.",
            "Wrap it before you tap it, {instigator.mention} and {target.mention}.",
            "{instigator.mention} and {target.mention} did the thing with the thing… oh gosh. Ew.",
            "Bing bong {instigator.mention}, turns out {target.mention} wants your ding dong!",
            "{target.mention} and {instigator.mention} did the nasty while spanking each others bum cheeks!",
            "{target.mention} and {instigator.mention} went to town, if you know what I mean.",
            "{target.mention} and {instigator.mention} got it on. I sure hope Jesus consented, too…",
            "JESUS CONSENTS, GOD WILLS IT.",
        ], *['instigator' if instigator else None, 'target' if target else None])).format(instigator=instigator, target=target)

    
    @classmethod 
    def request_denied(cls, instigator=None, target=None):
        '''
        They said no to the banging
        '''

        return choice(cls.get_valid_strings([
            "Looks like they don't wanna smash, {instigator.mention}!",
            "Guess it's back to the porn mags for you, {instigator.mention}. :/",
            "Sucks to be you, buckaroo!",
            "Guess your dick game isn't strong enough.",
            "¯\_(ツ)_/¯",
            "Haters are your motivators~",
            "Bing bong, they don't want your ding dong!",
            "No means no. Sorry!",
        ], *['instigator' if instigator else None, 'target' if target else None])).format(instigator=instigator, target=target)


    @classmethod
    def proposal_timed_out(cls, instigator=None, target=None):
        '''
        When the instigator's propsal times out
        '''

        return choice(cls.get_valid_strings([
            "Looks like the request timed out, {instigator.mention}!",
            "Looks like they fell asleep, {instigator.mention} .-.",
            "Guess not! Try again later, {instigator.mention}.",
            "If you're really that horny, go and watch some porn(y).",
            "You're all alone with no one to bone.",
            "Sorry {instigator.mention}",
            "¯\_(ツ)_/¯ {instigator.mention}",
        ], *['instigator' if instigator else None, 'target' if target else None])).format(instigator=instigator, target=target)


    @classmethod
    def valid_target(cls, instigator=None, target=None):
        '''
        When the proposal is valid
        '''

        return choice(cls.get_valid_strings([
            "Hey, {target.mention}, do you wanna?",
            "Hey {target.mention}, sex with {instigator.mention}? ",
            "Hey {target.mention}. You wanna fuck?",
            "What's up {target.mention} you dtf?",
            "Yoooo, you up to _smash_?",
            "Hey {target.mention}, u wan sum fuk?",
            "Hey, {target.mention}, ready to mingle? B)",
        ], *['instigator' if instigator else None, 'target' if target else None])).format(instigator=instigator, target=target)


    @classmethod 
    def proposing_to_themselves(cls, instigator=None, target=None):
        '''
        When they propose to themself
        '''

        return choice(cls.get_valid_strings([
            "Not on my Christian Minecraft server.",
            "Not in front of the children!",
            "Dildos and dildon'ts - this. This right now. Just stop. Pls.",
            "Masturbation is the language of loneliness… got something you wanna talk about, bud?",
            "Self-cest was so last year.",
            "Haven't you heard? Masturbation makes you blind!",
        ], *['instigator' if instigator else None, 'target' if target else None])).format(instigator=instigator, target=target)


    @classmethod 
    def target_is_bot(cls, instigator=None, target=None):
        '''
        When they propose to a bot
        '''

        return choice(cls.get_valid_strings([
            "Hey {instigator.mention}, isn't that illegal?",
            "I'm not sure a bot has enough sentience to consent if I'm gonna be honest. ",
            "I'm sure you're very attracted to diodes and capacitors but you can't blow a circuit board.",
            "Sex robots aren't quite up to modern standards yet, I'm afraid.",
        ], *['instigator' if instigator else None, 'target' if target else None])).format(instigator=instigator, target=target)


    @classmethod 
    def target_is_me(instigator=None, target=None):
        '''
        When they propose to MB
        '''

        return choice(cls.get_valid_strings([
            "I'm a bit out of your league, don't you think?",
            "I think I can do better than your twinky ass.",
            "Honestly? No.",
            "Gross. I'll pass. ",
            "Jesus is my only lover.",
            "I'm engaged to the Lord, no smashing before marriage.",
            "Thank you, next.",
            "STRANGER DANGER!",
            "Sure, go ahead if you want to make me short circuit, that's *perfectly* fine.",
            "My daddy said no I'm sorry.",
            "#Binch is the only relationship I'm interested in, sorry.",
        ], *['instigator' if instigator else None, 'target' if target else None])).format(instigator=instigator, target=target)

    
    @classmethod 
    def target_is_relation(cls, instigator, target, relationship:str):
        '''
        When the target is related to the instigator
        '''

        return choice(cls.get_valid_strings([
            "This ain't the South, partner. Stop.",
            "No, {instigator.mention}, I am your {relationship}.",
            "They're actually your {relationship} so I'm not sure that's a great idea.",
            "Don't turn the family tree into a family donut.",
            "That's gross, {instigator.mention} please reconsider.",
        ], *['instigator' if instigator else None, 'target' if target else None, 'relationship' if relationship else None])).format(instigator=instigator, target=target, relationship=relationship)
