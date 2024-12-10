# Bible_Text_Extraction
This is a small NLP project made in python to extract and search a specific word from Bible.

### Objective
The goal is to analyze and count the occurrences of a target word in the text of the Bible while providing relevant citations and verses where the word appears.

### Key Features
1. Data Loading:
> The app loads a dataset (bible_data_set.csv) containing Bible text and metadata like citations. It ensures the dataset is available and provides error feedback if not.
2. Text Preprocessing:
> The text is preprocessed to clean and normalize it:
> Converted to lowercase for uniformity.
> Special characters and punctuation are removed using regular expressions.
> Stopwords (common, non-informative words) are removed using NLTK's stopword corpus.
> Words are lemmatized (converted to their base forms) to group similar terms (e.g., "running" to "run").

3. Word Frequency Analysis:
>Users input a target word through the Streamlit interface.
>The app calculates and displays how many times the word appears in the dataset.
4. Contextual Exploration:
>The app scans the dataset for occurrences of the target word.
>For each instance, it displays the citation and corresponding text to provide context for the word's usage.
5.Interactive Interface:
>Built with Streamlit, the app provides a user-friendly, interactive experience:
>A text input field for entering the target word.
>Feedback messages to guide users (e.g., word count results, warnings for missing input).

## The UI :
![image](https://github.com/Kriz-Griffin/Bible_Text_Extraction/blob/9d782a9de1a79a1a26971eb8cd5e30026c5e9eb8/images/Screenshot%202024-12-10%20123520.png)

## Output
![image](https://github.com/Kriz-Griffin/Bible_Text_Extraction/blob/9d782a9de1a79a1a26971eb8cd5e30026c5e9eb8/images/Screenshot%202024-12-10%20123607.png)
