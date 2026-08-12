from wordcloud import WordCloud
import matplotlib.pyplot as plt


def create_wordcloud(text):

    wordcloud = WordCloud(
        width=900,
        height=500,
        background_color="white"
    ).generate(text)

    fig, ax = plt.subplots(figsize=(10, 5))

    ax.imshow(wordcloud, interpolation="bilinear")

    ax.axis("off")

    return fig