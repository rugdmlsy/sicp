"""Typing test implementation"""

from utils import *
from ucb import main, interact, trace
from datetime import datetime

HW_SOURCE_FILE = 'cats.py'

###########
# Phase 1 #
###########


def choose(paragraphs, select, k):
    """Return the Kth paragraph from PARAGRAPHS for which SELECT called on the
    paragraph returns true. If there are fewer than K such paragraphs, return
    the empty string.

    >>> ps = ['short', 'really long', 'tiny']
    >>> s = lambda p: len(p) <= 5
    >>> choose(ps, s, 0)
    'short'
    >>> choose(ps, s, 1)
    'tiny'
    >>> choose(ps, s, 2)
    ''
    """
    # BEGIN PROBLEM 1
    for i in paragraphs:
        if select(i):
            k-=1
            if k<0:
                return i
    return ''
    # END PROBLEM 1


def about(topic):
    """Return a select function that returns whether a paragraph contains one
    of the words in TOPIC.

    >>> about_dogs = about(['dog', 'dogs', 'pup', 'puppy'])
    >>> choose(['Cute Dog!', 'That is a cat.', 'Nice pup!'], about_dogs, 0)
    'Cute Dog!'
    >>> choose(['Cute Dog!', 'That is a cat.', 'Nice pup.'], about_dogs, 1)
    'Nice pup.'
    >>> dogs = about(['dogs', 'hounds'])
    >>> dogs('"DOGS" stands for Department of Geophysical Science.')
    True
    >>> dogs("Do gs and ho unds don't count")
    False
    """
    assert all([lower(x) == x for x in topic]), 'topics should be lowercase.'
    # BEGIN PROBLEM 2
    def select(para):
        a=split(remove_punctuation(lower(para)))
        return any(i in topic for i in a)
    return select
    # END PROBLEM 2


def accuracy(typed, reference):
    """Return the accuracy (percentage of words typed correctly) of TYPED
    when compared to the prefix of REFERENCE that was typed.

    >>> accuracy('Cute Dog!', 'Cute Dog.')
    50.0
    >>> accuracy('A Cute Dog!', 'Cute Dog.')
    0.0
    >>> accuracy('cute Dog.', 'Cute Dog.')
    50.0
    >>> accuracy('Cute Dog. I say!', 'Cute Dog.')
    50.0
    >>> accuracy('Cute', 'Cute Dog.')
    100.0
    >>> accuracy('', 'Cute Dog.')
    0.0
    >>> accuracy("12345", "12345")
    100.0
    >>> accuracy("a  b  c  d", "b  a  c  d")
    50.0
    >>> accuracy("Cat", "cat")
    0.0
    >>> accuracy("cats.", "cats")
    0.0
    """
    typed_words = split(typed)
    reference_words = split(reference)
    # BEGIN PROBLEM 3
    if not typed:
        return 0.0
    i=0
    s=0
    while i<min(len(typed_words),len(reference_words)):
        if typed_words[i]==reference_words[i]:
            s+=1
        i+=1
    return s*100/len(typed_words)
    # END PROBLEM 3


def wpm(typed, elapsed):
    """Return the words-per-minute (WPM) of the TYPED string.
    
    >>> wpm("12345", 3)
    20.0
    >>> wpm("", 10)
    0.0
    >>> wpm("a b c", 20)
    3.0
    """
    assert elapsed > 0, 'Elapsed time must be positive'
    # BEGIN PROBLEM 4
    return len(list(typed))/5/elapsed*60
    # END PROBLEM 4


def autocorrect(user_word, valid_words, diff_function, limit):
    """Returns the element of VALID_WORDS that has the smallest difference
    from USER_WORD. Instead returns USER_WORD if that difference is greater
    than LIMIT.

    >>> abs_diff = lambda w1, w2, limit: abs(len(w2) - len(w1))
    >>> autocorrect("cul", ["culture", "cult", "cultivate"], abs_diff, 10)
    'cult'
    >>> autocorrect("cul", ["culture", "cult", "cultivate"], abs_diff, 0)
    'cul'
    >>> autocorrect("wor", ["worry", "car", "part"], abs_diff, 10)
    'car'
    """
    # BEGIN PROBLEM 5
    if user_word in valid_words:
        return user_word
    ans=valid_words[0]
    s=diff_function(user_word,valid_words[0],limit)
    for i in valid_words:
        if s>diff_function(user_word,i,limit):
            ans=i
            s=diff_function(user_word,i,limit)
    if s>limit:
        return user_word
    return ans
    # END PROBLEM 5


def sphinx_swap(start, goal, limit):
    """A diff function for autocorrect that determines how many letters
    in START need to be substituted to create GOAL, then adds the difference in
    their lengths.

    >>> big_limit = 10
    >>> sphinx_swap("car", "cad", big_limit)
    1
    >>> sphinx_swap("this", "that", big_limit)
    2
    >>> sphinx_swap("one", "two", big_limit)
    3
    >>> sphinx_swap("awful", "awesome", 3) > 3
    True
    >>> sphinx_swap("awful", "awesome", 4) > 4
    True
    >>> from construct_check import check
    >>> # ban while or for loops
    >>> check(HW_SOURCE_FILE, 'missing_digits', ['While', 'For'])
    True
    """
    # BEGIN PROBLEM 6
    s=list(start)
    g=list(goal)
    def count(s,g):
        if min(len(s),len(g))==0:
            return max(len(s),len(g))
        if s[0]==g[0]:
            return count(s[1:],g[1:])
        return 1+count(s[1:],g[1:])
    return count(s,g)
    # END PROBLEM 6


def feline_fixes(start, goal, limit):
    """A diff function that computes the edit distance from START to GOAL.
    
    >>> big_limit = 10
    >>> feline_fixes("cats", "scat", big_limit)       # cats -> scats -> scat
    2
    >>> feline_fixes("purng", "purring", big_limit)   # purng -> purrng -> purring
    2
    >>> feline_fixes("ckiteus", "kittens", big_limit) # ckiteus -> kiteus -> kitteus -> kittens
    3
    >>> limit = 2
    >>> feline_fixes("ckiteus", "kittens", limit) > limit
    True
    >>> sphinx_swap("ckiteusabcdefghijklm", "kittensnopqrstuvwxyz", limit) > limit
    True
    """
    if limit<0:
        if start==goal:
            return 0
        return 1
    elif min(len(start),len(goal))==0:
        return abs(len(start)-len(goal))
    elif start[0]==goal[0]:
        return feline_fixes(start[1:],goal[1:],limit)
    else:
        add_diff = lambda x,y:y[0]+x
        remove_diff = lambda x:x[1:] 
        substitute_diff = lambda y:y[0]+start[1:]
        return 1+min(feline_fixes(add_diff(start,goal)[1:],goal[1:],limit-1),feline_fixes(remove_diff(start)[1:],goal[1:],limit-1),feline_fixes(substitute_diff(goal)[1:],goal[1:],limit-1))

def final_diff(start, goal, limit):
    """A diff function. If you implement this function, it will be used."""
    assert False, 'Remove this line to use your final_diff function'


###########
# Phase 3 #
###########


def report_progress(typed, prompt, id, send):
    """Send a report of your id and progress so far to the multiplayer server.
    
    >>> typed = ['I', 'have', 'begun']
    >>> prompt = ['I', 'have', 'begun', 'to', 'type']
    >>> print_progress = lambda d: print('ID:', d['id'], 'Progress:', d['progress'])
    >>> print_progress({'id': 1, 'progress': 0.6})
    ID: 1 Progress: 0.6
    >>> report_progress(typed, prompt, 1, print_progress) # print_progress is called on the report
    ID: 1 Progress: 0.6
    0.6
    >>> report_progress(['I', 'begun'], prompt, 2, print_progress)
    ID: 2 Progress: 0.2
    0.2
    >>> report_progress(['I', 'hve', 'begun', 'to', 'type'], prompt, 3, print_progress)
    ID: 3 Progress: 0.2
    0.2
    """
    # BEGIN PROBLEM 8
    i=0
    while i<len(typed) and typed[i]==prompt[i]:
        i+=1
    progress=i/len(prompt)
    send({'id':id,'progress':progress})
    return progress
    # END PROBLEM 8


def fastest_words_report(times_per_player, words):
    """Return a text description of the fastest words typed by each player."""
    game = time_per_word(times_per_player, words)
    fastest = fastest_words(game)
    report = ''
    for i in range(len(fastest)):
        words = ','.join(fastest[i])
        report += 'Player {} typed these fastest: {}\n'.format(i + 1, words)
    return report


def time_per_word(times_per_player, words):
    """Given timing data, return a game data abstraction, which contains a list
    of words and the amount of time each player took to type each word.

    Arguments:
        times_per_player: A list of lists of timestamps including the time
                          the player started typing, followed by the time
                          the player finished typing each word.
        words: a list of words, in the order they are typed.

    >>> p = [[1, 4, 6, 7], [0, 4, 6, 9]]
    >>> words = ['This', 'is', 'fun']
    >>> game = time_per_word(p, words)
    >>> all_words(game)
    ['This', 'is', 'fun']
    >>> all_times(game)
    [[3, 2, 1], [4, 2, 3]]
    >>> p = [[0, 2, 3], [2, 4, 7]]
    >>> game = time_per_word(p, ['hello', 'world'])
    >>> word_at(game, 1)
    'world'
    >>> all_times(game)
    [[2, 1], [2, 3]]
    >>> time(game, 0, 1)
    1
    """
    # BEGIN PROBLEM 9
    game=[words]
    p=[]
    for i in times_per_player:
        s=[]
        j=1
        while j<len(i):
            s+=[i[j]-i[j-1]]
            j+=1
        p+=[s]
    game+=[p]
    return game
    # END PROBLEM 9


def fastest_words(game):
    """Return a list of lists of which words each player typed fastest.

    Arguments:
        game: a game data abstraction as returned by time_per_word.
    Returns:
        a list of lists containing which words each player typed fastest

    >>> p0 = [2, 2, 3]
    >>> p1 = [6, 1, 2]
    >>> fastest_words(game(['What', 'great', 'luck'], [p0, p1]))
    [['What'], ['great', 'luck']]
    >>> p0 = [2, 2, 3]
    >>> p1 = [6, 1, 3]
    >>> fastest_words(game(['What', 'great', 'luck'], [p0, p1]))  # with a tie, choose the first player
    [['What', 'luck'], ['great']]
    >>> p2 = [4, 3, 1]
    >>> fastest_words(game(['What', 'great', 'luck'], [p0, p1, p2]))
    [['What'], ['great'], ['luck']]
    """
    players = range(len(all_times(game)))  # An index for each player
    words = range(len(all_words(game)))    # An index for each word
    # BEGIN PROBLEM 10
    i=0
    final=[]
    for i in players:
        final+=[[]]
    i=0
    for i in words:
        s=game[1][0][i]
        b=0
        for j in players:
            if game[1][j][i]<s:
                s=game[1][j][i]
                b=j
        final[b]+=[word_at(game,i)]
    return final
    # END PROBLEM 10


def game(words, times):
    """A data abstraction containing all words typed and their times."""
    assert all([type(w) == str for w in words]), 'words should be a list of strings'
    assert all([type(t) == list for t in times]), 'times should be a list of lists'
    assert all([isinstance(i, (int, float)) for t in times for i in t]), 'times lists should contain numbers'
    assert all([len(t) == len(words) for t in times]), 'There should be one word per time.'
    return [words, times]


def word_at(game, word_index):
    """A selector function that gets the word with index word_index"""
    assert 0 <= word_index < len(game[0]), "word_index out of range of words"
    return game[0][word_index]


def all_words(game):
    """A selector function for all the words in the game"""
    return game[0]


def all_times(game):
    """A selector function for all typing times for all players"""
    return game[1]


def time(game, player_num, word_index):
    """A selector function for the time it took player_num to type the word at word_index"""
    assert word_index < len(game[0]), "word_index out of range of words"
    assert player_num < len(game[1]), "player_num out of range of players"
    return game[1][player_num][word_index]


def game_string(game):
    """A helper function that takes in a game object and returns a string representation of it"""
    return "game(%s, %s)" % (game[0], game[1])

enable_multiplayer = False  # Change to True when you


##########################
# Command Line Interface #
##########################


def run_typing_test(topics):
    """Measure typing speed and accuracy on the command line."""
    paragraphs = lines_from_file('data/sample_paragraphs.txt')
    select = lambda p: True
    if topics:
        select = about(topics)
    i = 0
    while True:
        reference = choose(paragraphs, select, i)
        if not reference:
            print('No more paragraphs about', topics, 'are available.')
            return
        print('Type the following paragraph and then press enter/return.')
        print('If you only type part of it, you will be scored only on that part.\n')
        print(reference)
        print()

        start = datetime.now()
        typed = input()
        if not typed:
            print('Goodbye.')
            return
        print()

        elapsed = (datetime.now() - start).total_seconds()
        print("Nice work!")
        print('Words per minute:', wpm(typed, elapsed))
        print('Accuracy:        ', accuracy(typed, reference))

        print('\nPress enter/return for the next paragraph or type q to quit.')
        if input().strip() == 'q':
            return
        i += 1


@main
def run(*args):
    """Read in the command-line argument and calls corresponding functions."""
    import argparse
    parser = argparse.ArgumentParser(description="Typing Test")
    parser.add_argument('topic', help="Topic word", nargs='*')
    parser.add_argument('-t', help="Run typing test", action='store_true')

    args = parser.parse_args()
    if args.t:
        run_typing_test(args.topic)