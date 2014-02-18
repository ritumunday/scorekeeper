'''
Used for parsing through Moe's spreadsheet to find mismatched info.
It expectst that you will copy/paste the spreadsheet from the email directly
into src_text.
Usage:  (a, b, c) = build_tourney(src_text)
a = players
b = list of players who a[n] beat
c = list of players who a[n] lost to
TODO: need to add calculation for mismatches
'''

src_text = ''' 	W	L	Won On	Lost To
RP	 	2	 	Moe, Biyi
Robert	3	1	Kevin, German, Brandon	Chris,
Biyi	5	1	Chris, Kevin, Brandon, Daryl, RP, 	Moe,
Ritu	4	2	German, Brandon, Kevin, Daryl,	Jason, Chris
Daryl	3	2	German, Brandon, Kevin, 	Biyi, Ritu
Chris	6	1	Brandon, Robert, Kevin, Ritu, Jason, German	Biyi,
Jason	2	2	German, Ritu	Brandon, Chris
Kevin	2	5	German, Brandon, 	Robert, Biyi, Chris, Daryl, Ritu
Brandon	2	5	German, Jason,	Chris, Daryl, Biyi, Ritu, Robert
German	 	6		Kevin, Daryl, Jason, Kevin, Brandon, Ritu
Moe	2	 	Biyi, RP, 	 
Total	29	27	 	 
''' #copy Moe's spreadsheet into this

def build_tourney(src_text):
    lines = src_text.split('\n')
    #print(lines)
    x2 = [i.rsplit('\t', 1) for i in lines][1:] #drop headers
    total = x2[len(x2) - 2] #grab total calculations
    #print(total)
    x3 = x2[:len(x2) - 2] #cut off totals from data
    
    losses = [i[1] for i in x3] #list of string representing who you lost to
    x5 = [i[0].rsplit('\t', 1) for i in x3]
    wins = [i[1] for i in x5] #list of names of people you beat

    players = [i[0].split('\t', 1)[0] for i in x5]
    wins = [i.strip(',').split(',') for i in wins]
    losses = [i.strip(',').split(',') for i in losses]
    
    #strip leading/trailing spaces
    wins_clean = []
    for l in wins:
        wins_clean.append([i.strip() for i in l])
    losses_clean = []
    for l in losses:
        losses_clean.append([i.strip() for i in l])
    return (players, wins_clean, losses_clean)

def have_played(player, players, wins, losses):
    '''
    looks for which people $1 has played
    Returns a list of everyone $1 has played
    TODO: we might need logic for if a player's name is wrong
    '''
    p_idx = players.index(player)
    out_list = [i for i in wins[p_idx] + losses[p_idx] if i not in ('', ' ')]
    
    return out_list

def have_not_played(player, players, wins, losses):
    '''
    looks for who $1 has not played
    returns the list of players $1 has not played
    '''
    played_list =[i.upper() for i in have_played(player, players, wins, losses)]
    out_list = [i for i in players if i.upper() not in played_list]
    dummy = out_list.pop(out_list.index(player))
    return out_list

def compare_wins_losses(player, players, wins, losses):
    '''
    Double-checks wins/losses record for $1 against others players to ensure
    that data isn't incorrect.
    Returns true if everything is good, returns false if somehting is wrong
    '''
    #TODO
    
def needs_to_play_rpt(players, wins, losses):
    '''
    outputs a complete list of who needs to play who
    '''
    for p in players:
        out_l = have_not_played(p, players, wins, losses)
        print("%s needs to play these people:"%p)
        print(out_l)
