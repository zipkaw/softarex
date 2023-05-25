from sklearn.neighbors import KNeighborsRegressor
from sklearn.preprocessing import StandardScaler

class Model1KNN:

    def __init__(self):
        self.model = None

    def fit(self, tr_x, tr_y, va_x, va_y):
        self.scaler = StandardScaler()
        self.scaler.fit(tr_x)
        tr_x = self.scaler.transform(tr_x)
        self.model = KNeighborsRegressor(n_neighbors=5,
                                         #weights='uniform'
                                        )
        
        self.model.fit(tr_x,tr_y)
        
    def predict(self,x):
        x = self.scaler.transform(x)
        pred = self.model.predict(x)
        return pred
