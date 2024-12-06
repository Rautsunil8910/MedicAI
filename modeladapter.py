import gc
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import PCA
import numpy as np

class ModelAdapter:
    def __init__(self):
        self.model = None
        self.vectorizer = None
        self.pca = None
        self.loaded_state = False

    def load_model(self, model_path):
        """
        Load the trained model.
        """
        from joblib import load
        self.model = load(model_path)
        self.loaded_state = True

    def initialize(self):
        """
        Initialize vectorizer and PCA.
        """
        self.vectorizer = TfidfVectorizer(
            analyzer='word', stop_words='english', ngram_range=(1, 3),
            max_df=0.75, use_idf=True, smooth_idf=True, max_features=1000
        )
        self.pca = PCA(n_components=0.95)

    def apply(self, vectorizer, tfIdfMat, tfIdfMat_reduced):
        """
        Store vectorizer and PCA transformations.
        """
        self.vectorizer = vectorizer
        self.pca = tfIdfMat_reduced

    def predict(self, model, raw_text, lemmatized_text):
        """
        Make a prediction based on the input text.
        """
        if self.vectorizer is None or self.pca is None:
            raise ValueError("Vectorizer and PCA must be initialized first.")
        
        transformed_text = self.vectorizer.transform([lemmatized_text])
        reduced_features = self.pca.transform(transformed_text.toarray())
        return model.predict(reduced_features)

    def loaded(self):
        """
        Check if the model is loaded.
        """
        return self.loaded_state

# Create a global adapter instance
adapter = ModelAdapter()
