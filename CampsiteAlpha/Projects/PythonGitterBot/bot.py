# based heavily on discord.py/ext/commands

import inspect
import traceback

# globals
cmds = {
    'triggers':{},
    'commands':{}
    }
prefix = '!'

# decorators

def command(name=None, cmd_type='command', aliases : str=[]):
    kind = cmd_type+'s'  # i lazy
    if kind not in cmds:
        raise RuntimeError('Invalid command type')
    for alias in aliases if name is None else aliases+[name]:
        if cmd_type == 'command' and len(alias.split())>1:
            raise RuntimeError('Command names must be only 1 word long')
        if alias in cmds[kind]:
            raise RuntimeError('{} {} already exists'.format(
                    cmd_type[0].upper()+cmd_type[1:],alias))
    def decorator(func):
        cname = func.__name__ if name is None else name
        if cname in cmds[kind]:
            raise RuntimeError('{} {} already exists'.format(
                    cmd_type[0].upper()+cmd_type[1:],cname))
        func.kind = cmd_type
        for alias in aliases+[cname]:
            cmds[kind][alias] = func
        return func
    return decorator

def trigger(*args, **kwargs):
    kwargs['cmd_type']='trigger'
    return command(*args, **kwargs)

# helpers

def process_command(func, argstr):
    sig = inspect.signature(func)
    params = sig.parameters.copy()
    words = argstr.split()
    args = []

    # kwargs = {} use when consume rest as string
    for name, param in params.items():
        while words:  # if *args, consume all words
            if param.kind == param.KEYWORD_ONLY:
                break

            word = words.pop(0)
            param_type = _get_param_type(param)
            if param_type is bool:
                args.append(_convert_to_bool(word))
            else:
                args.append(param_type(word))

            if param.kind == param.POSITIONAL_OR_KEYWORD:
                break

    func(*args)

# heavy adaption from https://github.com/Rapptz/discord.py/blob/master/discord/ext/commands/core.py
def _get_param_type(param):
    param_type = param.annotation
    # if no type specified
    if param_type is param.empty:
        # if there's a default check it's type.
        if param.default is not param.empty and param.default is not None:
            param_type = type(param.default)
        else:
            param_type = str  # assume string otherwise
    return param_type

# taken straight from https://github.com/Rapptz/discord.py/blob/master/discord/ext/commands/core.py
# cause I like the idea :3
def _convert_to_bool(argument):
    lowered = argument.lower()
    if lowered in ('yes', 'y', 'true', 't', '1', 'enable', 'on'):
        return True
    elif lowered in ('no', 'n', 'false', 'f', '0', 'disable', 'off'):
        return False
    else:
        raise RuntimeError(lowered + ' is not a recognised boolean option')

# commands

@command(name="hi")
def foo():
    print('hi')

@command()
def bar(s):
    print(s + ' <-- wassat?')

@command()
def ping():
    """you working?"""
    print('pong')

@command(name='sort')
def _sort(*words):
    """sort list of things"""
    print(' '.join(sorted(words)))

@command(name='sum')
def _sum(*numbers : float):
    """add all the numbers together"""
    print(sum(numbers))

@command(aliases=['now'])
def time():
    """current time"""
    from datetime import datetime
    print(datetime.now())

@command(aliases=['exit'])
def quit():
    """turn off the bot"""
    import sys
    sys.exit(0)

@command()
def tree(height : int=None):
    """prints a christmas tree of a certain height"""
    if height is None:
        from random import randint
        height = randint(0,10)
    print('\n'.join([' '*(height-i-1)+'*'*(2*i+1)
            for i in range(0,height)])+
            '\n'+' '*(height-1)+'H')

@command()
def help(command_or_trigger=None):
    """displays information about a command/trigger"""
    if command_or_trigger is None:
        print('Commands:\n')
        list_commands()
        print('\nTriggers:\n')
        list_triggers()
    else:
        helps = []
        for kind in sorted(cmds.keys()):
            if command_or_trigger in cmds[kind]:
                helps.append(format_help(cmds[kind][command_or_trigger],
                        command_or_trigger))
        if not helps:
            print(command_or_trigger+' is not a registered command or trigger')
        else:
            print('\n\n'.join(helps))

def format_help(command, name):
    msg = '(trigger) ' if command.kind == 'trigger' else prefix;
    msg += name + ' '
    sig = inspect.signature(command)
    params = sig.parameters.copy()
    for pname, param in params.items():
        pstr = ("{}={}".format(pname,param.default) if
                param.default is not param.empty else pname)
        if (param.default is not param.empty or
                param.kind == param.VAR_POSITIONAL):
            msg += "[{}]".format(pstr)
        else:
            msg += "<{}>".format(pstr)
    msg += '\n'
    msg += command.__doc__ or ''
    return msg

@command(name='commands')
def list_commands():
    print('\n'.join(sorted(cmds['commands'])))

@command(name='triggers')
def list_triggers():
    print('\n'.join(sorted(cmds['triggers'])))


# triggers - take care. args passed are in the order the user typed them

@trigger(aliases=['shit','bitch','trump'])
def fuck():
    """no cursing D:"""
    print('hey! no swearing!')

@trigger(name="christmas tree")
def c_tree(*msg):
    height = None
    for w in msg:
        try:
            height = int(w)
            break
        except:
            pass
    tree(height)

@trigger(name='quit')
def trigger_quit():
    print("No don't leave D:")

# should make an event instead of hacking it like this
@trigger(name='')
def on_message(*msg):
    import random
    if not random.randint(0,10):
        words = list(msg)
        random.shuffle(words)
        print(' '.join(words))

# input loop

print('\nBot is on \o/\n{} commands registered\n'
        '{} triggers registered\n'.format(
        len(cmds['commands']),len(cmds['triggers'])))

# if <prefix>command_name in input, process command.
# commands get rest of sentence as arg.
# else if trigger in msg, process trigger
# trigger can be part of a word in msg
while True:
    msg = input('> ')
    if msg.startswith(prefix):
        cmsg = msg[len(prefix):]
        cmd = cmsg.split()[0]

        if cmd in cmds['commands']:
            try:
                process_command(cmds['commands'][cmd],cmsg[len(cmd):])
            except Exception as e:
                print(traceback.print_exc())

    else:
        # going through triggers means we can have have multi-word triggers.
        # but it also means execution of triggers is non-deterministic
        # we're also deciding to only trigger on one per msg
        # for now, hacking in on_message. change into event later
        for kw in cmds['triggers'].keys():
            if kw.lower() in msg.lower():
                try:
                    process_command(cmds['triggers'][kw],msg)
                except Exception as e:
                    print(traceback.print_exc())
                if kw:  # on_message hack
                    break
