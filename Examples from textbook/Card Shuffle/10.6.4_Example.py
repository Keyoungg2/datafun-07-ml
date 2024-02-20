from deck import DeckOfCards
from pathlib import Path
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

deck_of_cards = DeckOfCards()

# Create the Base `Path` for Each Image
path = Path('.').joinpath('card_images')

# Create the `Figure` and `Axes` Objects
figure, axes_list = plt.subplots(nrows=4, ncols=13)

# Configure the `Axes` Objects and Display the Images
for axes in axes_list.ravel():
    axes.get_xaxis().set_visible(False)
    axes.get_yaxis().set_visible(False)
    image_name = deck_of_cards.deal_card().image_name
    img = mpimg.imread(str(path.joinpath(image_name).resolve()))
    axes.imshow(img)

# Maximize the Image Sizes
figure.tight_layout()

### Shuffle and Re-Deal the Deck
deck_of_cards.shuffle()

for axes in axes_list.ravel():
    axes.get_xaxis().set_visible(False)
    axes.get_yaxis().set_visible(False)
    image_name = deck_of_cards.deal_card().image_name
    img = mpimg.imread(str(path.joinpath(image_name).resolve()))
    axes.imshow(img)

# Display the plots
plt.show()
