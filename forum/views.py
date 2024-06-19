from django.shortcuts import render
from django.views.generic import DetailView, TemplateView
from .forms import *
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from forum.util.enums import *

def sort_hand(cards):
    def sort_key(card):
        value = i = 0
        match card[0]:
            case Height.TWO.value:
                value = 0
            case Height.THREE.value:
                value = 1
            case Height.FOUR.value:
                value = 2
            case Height.FIVE.value:
                value = 3
            case Height.SIX.value:
                value = 4
            case Height.SEVEN.value:
                value = 5
            case Height.EIGHT.value:
                value = 6
            case Height.NINE.value:
                value = 7
            case Height.TEN.value:
                value = 8
            case Height.JACK.value:
                value = 9
            case Height.QUEEN.value:
                value = 10
            case Height.KING.value:
                value = 11
            case Height.ACE.value:
                value = 12
        
        match card[1]:
            case Suit.CLUBS.value:
                i = 0
            case Suit.DIAMONDS.value:
                i = 1
            case Suit.HEARTS.value:
                i = 2
            case Suit.SPADES.value: 
                i = 3

        return value + 13 * i
    
    return sorted(cards, key=sort_key, reverse=True)

@login_required(login_url='login')
def forum(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.user_id = request.user
            new_post.save()
    else:
        form = PostForm()
    
    return render(request, 'forum/forum.html', {'form': form, 'posts': Post.objects.all()})

class selected_post(DetailView):
    model = Post
    template_name = 'forum/selected_post.html'
    context_object_name = 'post' # zmienna przekazana do szablonu z wybranym postem i jego danymi!


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['selected_post'] = self.get_object()
        context['form'] = CommentForm
        context['comments'] = Comment.objects.filter(post_id=self.get_object())
        
        cards = {'n': [], 'e': [], 's': [], 'w': []}
        post = self.object

        for side in cards.keys():
            for suit in ['clubs', 'diamonds', 'hearts', 'spades']:
                
                field_name = f'{side}_{suit}'
                cards_model = getattr(post, field_name, None)

                if cards_model != None:
                    color_length = min(len(cards_model), 13)
                    cards_model = cards_model[:color_length]

                    for height in cards_model:
                        # conversion to card symbol
                        if height == 'T':
                            height = '10'
                        if suit == 'clubs':
                            color = '♣'
                        elif suit == 'diamonds':
                            color = '♦'
                        elif suit == 'hearts':
                            color = '♥'
                        elif suit == 'spades':
                            color = '♠'
                        cards[side].append((height, color))
        
        for side in cards:
            cards[side] = sort_hand(cards[side])

        sorted_cards = {'n': [],'e': [],'s':[], 'w':[]}

        for i, card in enumerate(cards['n']):
            sorted_cards['n'].append((i, card))

        for i, card in enumerate(cards['s']):
            sorted_cards['s'].append((i, card))

        for i, card in enumerate(cards['e']):
            sorted_cards['e'].append((i, card))

        for i, card in enumerate(cards['w']):
            sorted_cards['w'].append((i, card))

        context['cards'] = sorted_cards

        return context

    def post(self, request, *args, **kwargs):

        self.object = self.get_object()

        comment_form = CommentForm(request.POST, request.FILES)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.user_id = request.user  
            new_comment.post_id = self.object  
            new_comment.save()

        return render(request, self.template_name, self.get_context_data())
    
class new_post(TemplateView):
    template_name = 'forum/new_post.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = PostForm()
        return context

    def post(self, request, *args, **kwargs):
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.user_id = request.user
            new_post.save()
        return render(request, self.template_name, self.get_context_data())