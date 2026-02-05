from scipy import stats
import statsmodels.api as sm
import pandas as pd

class StatEngine:
    """
    Encapsulates statistical tests and modeling.
    """
    
    @staticmethod
    def run_ttest_ind(group_a, group_b, label_a, label_b):
        """Performs independent T-test between two groups."""
        t_stat, p_val = stats.ttest_ind(group_a, group_b, nan_policy='omit')
        
        significance = "SIGNIFICANT" if p_val < 0.05 else "NOT SIGNIFICANT"
        result_str = (
            f"T-Test ({label_a} vs {label_b}):\n"
            f"   -> P-Value: {p_val:.4f}\n"
            f"   -> Result: {significance} difference detected."
        )
        return result_str

    @staticmethod
    def run_anova(groups_dict):
        """Performs One-Way ANOVA on dictionary of groups {name: data}."""
        values = list(groups_dict.values())
        f_stat, p_val = stats.f_oneway(*values)
        
        significance = "SIGNIFICANT" if p_val < 0.05 else "NOT SIGNIFICANT"
        return (
            f"ANOVA Test:\n"
            f"   -> F-Stat: {f_stat:.2f}, P-Value: {p_val:.4f}\n"
            f"   -> Result: {significance} variance between groups."
        )

    @staticmethod
    def train_ols_regression(X, y):
        """Trains an OLS Regression model and returns the summary."""
        # Add constant for intercept (y = mx + b)
        X_const = sm.add_constant(X)
        model = sm.OLS(y, X_const).fit()
        return model