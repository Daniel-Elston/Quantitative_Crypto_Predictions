import pandas as pd
import numpy as np


class FeatureEngineer:
    def __init__(
        self,
        df:pd.DataFrame,
        feature_cols_for_eng:list,
        mmean_periods:int,
        ror_col:str
        ):
        
        self.df = df
        self.feature_cols_for_eng = feature_cols_for_eng
        self.mmean_periods = mmean_periods
        self.ror_col = ror_col
        
        
    def get_rate_of_return(
        self
        ):
        
        self.df['rate_of_return'] = self.df[self.ror_col].pct_change()
        self.df['rate_of_return'].fillna(method='bfill', inplace=True)
        return self.df
    
    
    def get_market_means_ratios(
        self
        ):
        
        for col in self.feature_cols_for_eng:
            self.df[f'{col}_mmean'] = self.df[col].rolling(window=self.mmean_periods).mean()
            self.df[f'{col}_mmean'].fillna(method='bfill', inplace=True)
            
            self.df[f'{col}_mmean_ratio'] = self.df[col] / self.df[f'{col}_mmean']
            self.df[f'{col}_mmean_ratio'].fillna(method='bfill', inplace=True)
        return self.df
        
        
    def get_sma_ema(
        self,
        ):
        
        for col in self.feature_cols_for_eng:
            self.df[f'{col}_sma'] = self.df[col].rolling(window=self.mmean_periods).mean()
            self.df[f'{col}_sma'].fillna(method='bfill', inplace=True)
            
            self.df[f'{col}_ema'] = self.df[col].ewm(span=self.mmean_periods, adjust=False).mean()
            self.df[f'{col}_ema'].fillna(method='bfill', inplace=True)
        return self.df
    
    
    def get_percentage_change(
        self,
        ):

        for col in self.feature_cols_for_eng:
            self.df[f'{col}_pct_change'] = self.df[col].pct_change()
            self.df[f'{col}_pct_change'].fillna(method='bfill', inplace=True)
        return self.df