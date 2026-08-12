import matplotlib.pyplot as plt

def create_bar_chart(stats):

    labels = [
        "Pages",
        "Words",
        "Characters",
        "Sentences",
        "Keywords"
    ]

    values = [
        stats["Pages"],
        stats["Words"],
        stats["Characters"],
        stats["Sentences"],
        stats["Keywords"]
    ]

    fig, ax = plt.subplots(figsize=(8,5))

    ax.bar(labels, values)

    ax.set_title("Document Statistics")

    return fig


def create_pie_chart(stats):

    labels = [
        "Words",
        "Characters",
        "Sentences"
    ]

    values = [
        stats["Words"],
        stats["Characters"],
        stats["Sentences"]
    ]

    fig, ax = plt.subplots(figsize=(6,6))

    ax.pie(
        values,
        labels=labels,
        autopct="%1.1f%%"
    )

    ax.set_title("Document Distribution")

    return fig