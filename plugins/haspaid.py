from util import hook, http


@hook.command
def haspaid(inp):
    ".haspaid <username> - checks if minecraft <username> has paid for the game"
    return " ".join([x for x in http.get("http://www.minecraft.net/haspaid.jsp", user=inp).splitlines() if x])
