from sklearn.base import TransformerMixin 

      #Custom transformer using spaCy 
class predictors(TransformerMixin):
    def transform(self, X, **transform_params):
        return [self.clean_text(text) for text in X]
    def fit(self, X, y, **fit_params):
        return self
    def get_params(self, deep=True):
        return {}

    # Basic function to clean the text 
    def clean_text(self, text):     
        return text.strip().lower()