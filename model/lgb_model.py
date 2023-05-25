import lightgbm as lgb

class Model1lgb:

    def __init__(self):
        self.model = None

    def fit(self, tr_x, tr_y, va_x, va_y):
        lgb_params = {'objective': 'rmse',
                  'random_state': 10,
                  'metric': 'rmse'}
        lgb_train = lgb.Dataset(tr_x, label=tr_y)
        lgb_eval = lgb.Dataset(va_x, label=va_y,reference=lgb_train)
        self.model = lgb.train(lgb_params, lgb_train, valid_sets=lgb_eval, num_boost_round=10000,early_stopping_rounds=50)

    def predict(self, x):
        pred = self.model.predict(x,num_iteration=self.model.best_iteration)
        return pred