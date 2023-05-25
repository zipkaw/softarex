from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestRegressor

class Model1RF:

    def __init__(self):
        self.model = None

    def fit(self, tr_x, tr_y, va_x, va_y):
        self.scaler = StandardScaler()
        self.scaler.fit(tr_x)
        tr_x = self.scaler.transform(tr_x)
        self.model = RandomForestRegressor(
            max_depth=5,
            n_estimators=100,
            random_state=10,
        )
        self.model.fit(tr_x,tr_y)
        
    def predict(self,x):
        x = self.scaler.transform(x)
        pred = self.model.predict(x)
        return pred

