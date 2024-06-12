import streamlit as st
import pandas as pd
from textblob import TextBlob
import matplotlib.pyplot as plt
st.set_option('deprecation.showPyplotGlobalUse', False)
def main():
    st.title("Sentiment Analysis")
    uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

    if uploaded_file is not None:
        comments_df = pd.read_csv(uploaded_file)
        st.write(comments_df)

        csv = comments_df.to_csv(index=False)
        # Load comments from CSV file
        comments_df = pd.read_csv("sent_ana.csv")

# Assuming the column name containing reviews is 'comment', adjust it if different
        sentiments = comments_df["comment"].apply(lambda x: TextBlob(str(x)).sentiment.polarity)

# Classify sentiments into positive, neutral, and negative
        positive_comments = sum(sentiments > 0)
        neutral_comments = sum(sentiments == 0)
        negative_comments = sum(sentiments < 0)

# Plotting
        labels = ['Positive', 'Neutral', 'Negative']
        sizes = [positive_comments, neutral_comments, negative_comments]

# Option A: Using Hexadecimal Codes
        colors = ['#99F999', '#FFFF00', '#FF9999']

# Option B: Using Named Colors
# colors = ['green', 'gray', 'red']

# Bar chart
        plt.subplot(1, 2, 2)
        plt.bar(labels, sizes, color=colors)
        plt.title('Sentiment Analysis')
        plt.xlabel('Sentiment')
        plt.ylabel('graph')

# Adjust layout and display plot
        plt.tight_layout()
        st.pyplot()
        #st.write(plt.show())
        
if __name__ == "__main__":
    main()