import botconfig

def is_bloxad_admin(ctx):
    if ctx.message.author.id in botconfig.admins():
        return True
    return False
