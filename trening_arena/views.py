from django.shortcuts import render, redirect, HttpResponseRedirect
from django.urls import reverse
import random
from trening_arena.util.Hand import Hand
from .forms import WhatShouldOpen
from django.http import JsonResponse

def opening_bidding(hand):
    # dealer's position, 0 = E, 1 = S, 2 = W, 3 = N
    starting_position = hand.first_hand_num - 1

    # number of passes
    passes = hand.hand_num-1
    bidding = []
    for _ in range(starting_position):
        bidding.append(' ')

    for _ in range(passes):
        bidding.append('pass')

    return bidding

# global
# new_hand = Hand()

def opening(request):
    # hand_id = request.session.get('hand_id')
    hand_id = request.POST.get('hand_id') or request.GET.get('hand_id') or request.session.get('hand_id')

    title = 'Openings'

    if hand_id:
        try:
            new_hand = Hand(hand_id)
        except Hand.DoesNotExist:
            new_hand = Hand(hand_id)
    else:
        seed = random.randrange(100000)
        new_hand = Hand(seed)
        request.session['hand_id'] = seed

    bidding = opening_bidding(new_hand)
    bidding.append('user')
    # bidding.append('1♣')
    # bidding.append('1♦')
    # bidding.append('1♥')
    # bidding.append('1♠')
    # bidding.append('1NT')
    # bidding.append('x')
    # bidding.append('xx')
    cards = new_hand.sort_hand()

    for i, x in enumerate(cards):
        cards[i] = (i, (x[0].value, x[1].value))

    message = []
    what_should_open = correcting_message = ''
    opened_correctly = False
    form_sent = False

    if request.method == 'POST':
        form = WhatShouldOpen(request.POST)

        if form.is_valid():
            guess = form.cleaned_data['guess']
            what_should_open, correcting_message = new_hand.what_should_open()
            if guess == what_should_open:
                opened_correctly = True
                message.append('Poprawna odpowiedź!')
                form_sent = True
            else:
                message.append(('Poprawna odpowiedź: ', what_should_open))
                message.append(('Wytłumaczenie: ', correcting_message))
                opened_correctly = False
                form_sent = True
    else:
        form = WhatShouldOpen()


    context = {
        'title': title,
        'bidding': bidding,
        'cards': cards,
        'form':form,
        'opened_correctly':opened_correctly,
        'message':message,
        'form_sent':form_sent,
        'test':new_hand.is_strictly_balanced,
        'vulnerability':new_hand.vulnerability_colors
    }

    return render(request, 'opening.html', context)


def generate_new_hand_id(request):
    new_seed = random.randrange(100000)
    request.session['hand_id'] = new_seed
    # return HttpResponseRedirect(reverse('opening'), {'hand_id': new_seed})
    return redirect(reverse('opening') + f'?hand_id={new_seed}')
