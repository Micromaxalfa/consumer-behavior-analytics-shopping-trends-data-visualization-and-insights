"""
Consumer Behavior Analytics - Shopping Trends Analysis
=====================================================

This script provides comprehensive analysis of consumer shopping behavior using
the shopping_trends.csv dataset. It includes data exploration, descriptive statistics,
and various visualizations to understand purchasing patterns, demographics, and
business insights.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import warnings
warnings.filterwarnings('ignore')

# Set style for matplotlib/seaborn
plt.style.use('default')
sns.set_palette("husl")

class ConsumerBehaviorAnalytics:
    """
    A comprehensive class for analyzing consumer shopping behavior data.
    """
    
    def __init__(self, data_path='data/shopping_trends.csv'):
        """Initialize the analytics class and load data."""
        self.data_path = data_path
        self.df = None
        self.load_data()
        
    def load_data(self):
        """Load and perform initial data validation."""
        try:
            self.df = pd.read_csv(self.data_path)
            print(f"Data loaded successfully! Shape: {self.df.shape}")
        except FileNotFoundError:
            print(f"Error: Could not find {self.data_path}")
            return None
    
    def data_overview(self):
        """Provide comprehensive data overview and basic statistics."""
        print("="*60)
        print("DATA OVERVIEW AND EXPLORATION")
        print("="*60)
        
        print(f"Dataset Shape: {self.df.shape}")
        print(f"Total Records: {len(self.df)}")
        print(f"Total Features: {len(self.df.columns)}")
        
        print("\n" + "="*30)
        print("COLUMN INFORMATION")
        print("="*30)
        print(self.df.info())
        
        print("\n" + "="*30)
        print("FIRST 5 RECORDS")
        print("="*30)
        print(self.df.head())
        
        print("\n" + "="*30)
        print("MISSING VALUES")
        print("="*30)
        missing_data = self.df.isnull().sum()
        missing_percent = (missing_data / len(self.df)) * 100
        missing_summary = pd.DataFrame({
            'Missing Count': missing_data,
            'Missing Percentage': missing_percent
        })
        print(missing_summary[missing_summary['Missing Count'] > 0])
        
        if missing_summary['Missing Count'].sum() == 0:
            print("No missing values found in the dataset!")
    
    def descriptive_statistics(self):
        """Generate comprehensive descriptive statistics."""
        print("\n" + "="*60)
        print("DESCRIPTIVE STATISTICS")
        print("="*60)
        
        # Numerical variables
        numerical_cols = ['Purchase Amount (USD)', 'Review Rating', 'Previous Purchases']
        
        print("\nNUMERICAL VARIABLES SUMMARY:")
        print("-" * 40)
        print(self.df[numerical_cols].describe())
        
        # Categorical variables
        categorical_cols = ['Age', 'Gender', 'Category', 'Location', 'Season', 
                          'Subscription Status', 'Payment Method', 'Purchase Frequency']
        
        print("\nCATEGORICAL VARIABLES SUMMARY:")
        print("-" * 40)
        for col in categorical_cols:
            print(f"\n{col}:")
            print(self.df[col].value_counts().head())
    
    def category_performance_analysis(self):
        """Analyze category performance with visualizations."""
        print("\n" + "="*60)
        print("CATEGORY PERFORMANCE ANALYSIS")
        print("="*60)
        
        # Create figure with subplots
        fig, axes = plt.subplots(2, 2, figsize=(15, 12))
        fig.suptitle('Category Performance Analysis', fontsize=16, fontweight='bold')
        
        # 1. Revenue by Category (Bar Chart)
        category_revenue = self.df.groupby('Category')['Purchase Amount (USD)'].sum().sort_values(ascending=False)
        category_revenue.plot(kind='bar', ax=axes[0,0], color='skyblue')
        axes[0,0].set_title('Total Revenue by Category')
        axes[0,0].set_xlabel('Category')
        axes[0,0].set_ylabel('Total Revenue (USD)')
        axes[0,0].tick_params(axis='x', rotation=45)
        
        # 2. Number of Purchases by Category (Bar Chart)
        category_counts = self.df['Category'].value_counts()
        category_counts.plot(kind='bar', ax=axes[0,1], color='lightcoral')
        axes[0,1].set_title('Number of Purchases by Category')
        axes[0,1].set_xlabel('Category')
        axes[0,1].set_ylabel('Number of Purchases')
        axes[0,1].tick_params(axis='x', rotation=45)
        
        # 3. Average Purchase Amount by Category
        avg_purchase = self.df.groupby('Category')['Purchase Amount (USD)'].mean().sort_values(ascending=False)
        avg_purchase.plot(kind='bar', ax=axes[1,0], color='lightgreen')
        axes[1,0].set_title('Average Purchase Amount by Category')
        axes[1,0].set_xlabel('Category')
        axes[1,0].set_ylabel('Average Purchase Amount (USD)')
        axes[1,0].tick_params(axis='x', rotation=45)
        
        # 4. Category Market Share (Pie Chart)
        market_share = self.df['Category'].value_counts()
        axes[1,1].pie(market_share.values, labels=market_share.index, autopct='%1.1f%%')
        axes[1,1].set_title('Market Share by Category')
        
        plt.tight_layout()
        plt.savefig('visualizations/category_performance.png', dpi=300, bbox_inches='tight')
        plt.show()
        
        # Print insights
        print(f"Top performing category by revenue: {category_revenue.index[0]} (${category_revenue.iloc[0]:,.2f})")
        print(f"Most popular category by volume: {category_counts.index[0]} ({category_counts.iloc[0]} purchases)")
        print(f"Highest average purchase amount: {avg_purchase.index[0]} (${avg_purchase.iloc[0]:.2f})")
    
    def seasonal_analysis(self):
        """Analyze seasonal trends and patterns."""
        print("\n" + "="*60)
        print("SEASONAL DEMAND ANALYSIS")
        print("="*60)
        
        # Create seasonal analysis plots
        fig, axes = plt.subplots(2, 2, figsize=(15, 12))
        fig.suptitle('Seasonal Demand Analysis', fontsize=16, fontweight='bold')
        
        # 1. Total Sales by Season
        seasonal_revenue = self.df.groupby('Season')['Purchase Amount (USD)'].sum()
        seasonal_revenue.plot(kind='bar', ax=axes[0,0], color='orange')
        axes[0,0].set_title('Total Revenue by Season')
        axes[0,0].set_xlabel('Season')
        axes[0,0].set_ylabel('Total Revenue (USD)')
        
        # 2. Number of Purchases by Season
        seasonal_counts = self.df['Season'].value_counts()
        seasonal_counts.plot(kind='bar', ax=axes[0,1], color='purple')
        axes[0,1].set_title('Number of Purchases by Season')
        axes[0,1].set_xlabel('Season')
        axes[0,1].set_ylabel('Number of Purchases')
        
        # 3. Category performance by season (heatmap)
        season_category = pd.crosstab(self.df['Season'], self.df['Category'])
        sns.heatmap(season_category, annot=True, fmt='d', ax=axes[1,0], cmap='YlOrRd')
        axes[1,0].set_title('Category Purchases by Season')
        
        # 4. Average purchase amount by season
        avg_seasonal = self.df.groupby('Season')['Purchase Amount (USD)'].mean()
        avg_seasonal.plot(kind='line', marker='o', ax=axes[1,1], color='green', linewidth=2)
        axes[1,1].set_title('Average Purchase Amount by Season')
        axes[1,1].set_xlabel('Season')
        axes[1,1].set_ylabel('Average Purchase Amount (USD)')
        axes[1,1].grid(True, alpha=0.3)
        
        plt.tight_layout()
        plt.savefig('visualizations/seasonal_analysis.png', dpi=300, bbox_inches='tight')
        plt.show()
        
        # Print insights
        best_season = seasonal_revenue.idxmax()
        print(f"Best performing season: {best_season} (${seasonal_revenue[best_season]:,.2f})")
        print(f"Peak shopping season: {seasonal_counts.idxmax()} ({seasonal_counts.max()} purchases)")
    
    def demographic_analysis(self):
        """Analyze customer demographics and purchasing patterns."""
        print("\n" + "="*60)
        print("DEMOGRAPHIC ANALYSIS")
        print("="*60)
        
        # Create demographic analysis plots
        fig, axes = plt.subplots(2, 3, figsize=(18, 12))
        fig.suptitle('Customer Demographics Analysis', fontsize=16, fontweight='bold')
        
        # 1. Gender Distribution
        gender_counts = self.df['Gender'].value_counts()
        axes[0,0].pie(gender_counts.values, labels=gender_counts.index, autopct='%1.1f%%')
        axes[0,0].set_title('Customer Gender Distribution')
        
        # 2. Age Group Distribution
        age_counts = self.df['Age'].value_counts()
        age_counts.plot(kind='bar', ax=axes[0,1], color='teal')
        axes[0,1].set_title('Customer Age Distribution')
        axes[0,1].set_xlabel('Age Group')
        axes[0,1].set_ylabel('Number of Customers')
        axes[0,1].tick_params(axis='x', rotation=45)
        
        # 3. Purchase Amount by Gender
        gender_spending = self.df.groupby('Gender')['Purchase Amount (USD)'].mean()
        gender_spending.plot(kind='bar', ax=axes[0,2], color='coral')
        axes[0,2].set_title('Average Spending by Gender')
        axes[0,2].set_xlabel('Gender')
        axes[0,2].set_ylabel('Average Purchase Amount (USD)')
        
        # 4. Purchase Amount by Age Group
        age_spending = self.df.groupby('Age')['Purchase Amount (USD)'].mean().sort_values(ascending=False)
        age_spending.plot(kind='bar', ax=axes[1,0], color='gold')
        axes[1,0].set_title('Average Spending by Age Group')
        axes[1,0].set_xlabel('Age Group')
        axes[1,0].set_ylabel('Average Purchase Amount (USD)')
        axes[1,0].tick_params(axis='x', rotation=45)
        
        # 5. Category preferences by Gender
        gender_category = pd.crosstab(self.df['Gender'], self.df['Category'])
        sns.heatmap(gender_category, annot=True, fmt='d', ax=axes[1,1], cmap='Blues')
        axes[1,1].set_title('Category Preferences by Gender')
        
        # 6. Location Distribution (Top 10)
        location_counts = self.df['Location'].value_counts().head(10)
        location_counts.plot(kind='bar', ax=axes[1,2], color='lightblue')
        axes[1,2].set_title('Top 10 Customer Locations')
        axes[1,2].set_xlabel('Location')
        axes[1,2].set_ylabel('Number of Customers')
        axes[1,2].tick_params(axis='x', rotation=45)
        
        plt.tight_layout()
        plt.savefig('visualizations/demographic_analysis.png', dpi=300, bbox_inches='tight')
        plt.show()
        
        # Print insights
        top_spending_gender = gender_spending.idxmax()
        top_spending_age = age_spending.index[0]
        print(f"Highest spending gender: {top_spending_gender} (${gender_spending[top_spending_gender]:.2f})")
        print(f"Highest spending age group: {top_spending_age} (${age_spending.iloc[0]:.2f})")
    
    def regional_analysis(self):
        """Analyze regional differences and patterns."""
        print("\n" + "="*60)
        print("REGIONAL ANALYSIS")
        print("="*60)
        
        # Regional performance metrics
        regional_metrics = self.df.groupby('Location').agg({
            'Purchase Amount (USD)': ['sum', 'mean', 'count'],
            'Review Rating': 'mean'
        }).round(2)
        
        regional_metrics.columns = ['Total_Revenue', 'Avg_Purchase', 'Num_Purchases', 'Avg_Rating']
        regional_metrics = regional_metrics.sort_values('Total_Revenue', ascending=False)
        
        # Create regional analysis plots
        fig, axes = plt.subplots(2, 2, figsize=(15, 12))
        fig.suptitle('Regional Performance Analysis', fontsize=16, fontweight='bold')
        
        # 1. Total Revenue by Location (Top 10)
        top_revenue = regional_metrics['Total_Revenue'].head(10)
        top_revenue.plot(kind='bar', ax=axes[0,0], color='navy')
        axes[0,0].set_title('Top 10 Locations by Total Revenue')
        axes[0,0].set_xlabel('Location')
        axes[0,0].set_ylabel('Total Revenue (USD)')
        axes[0,0].tick_params(axis='x', rotation=45)
        
        # 2. Average Purchase Amount by Location (Top 10)
        top_avg = regional_metrics['Avg_Purchase'].head(10)
        top_avg.plot(kind='bar', ax=axes[0,1], color='darkgreen')
        axes[0,1].set_title('Top 10 Locations by Average Purchase')
        axes[0,1].set_xlabel('Location')
        axes[0,1].set_ylabel('Average Purchase Amount (USD)')
        axes[0,1].tick_params(axis='x', rotation=45)
        
        # 3. Number of Purchases by Location (Top 10)
        top_volume = regional_metrics['Num_Purchases'].head(10)
        top_volume.plot(kind='bar', ax=axes[1,0], color='maroon')
        axes[1,0].set_title('Top 10 Locations by Purchase Volume')
        axes[1,0].set_xlabel('Location')
        axes[1,0].set_ylabel('Number of Purchases')
        axes[1,0].tick_params(axis='x', rotation=45)
        
        # 4. Average Rating by Location (Top 10)
        top_rating = regional_metrics['Avg_Rating'].head(10)
        top_rating.plot(kind='bar', ax=axes[1,1], color='purple')
        axes[1,1].set_title('Top 10 Locations by Average Rating')
        axes[1,1].set_xlabel('Location')
        axes[1,1].set_ylabel('Average Rating')
        axes[1,1].tick_params(axis='x', rotation=45)
        
        plt.tight_layout()
        plt.savefig('visualizations/regional_analysis.png', dpi=300, bbox_inches='tight')
        plt.show()
        
        print("TOP 5 REGIONS BY TOTAL REVENUE:")
        print(regional_metrics[['Total_Revenue', 'Num_Purchases', 'Avg_Purchase']].head())
    
    def customer_segmentation_analysis(self):
        """Perform customer segmentation based on purchasing behavior."""
        print("\n" + "="*60)
        print("CUSTOMER SEGMENTATION ANALYSIS")
        print("="*60)
        
        # Create customer segments based on purchase behavior
        # Define segments based on purchase frequency and amount
        purchase_freq_map = {
            'Weekly': 4, 'Bi-Weekly': 3, 'Monthly': 2, 'Quarterly': 1, 'Annually': 0
        }
        
        self.df['Freq_Score'] = self.df['Purchase Frequency'].map(purchase_freq_map)
        
        # Create segments
        conditions = [
            (self.df['Purchase Amount (USD)'] >= 200) & (self.df['Freq_Score'] >= 3),
            (self.df['Purchase Amount (USD)'] >= 100) & (self.df['Freq_Score'] >= 2),
            (self.df['Purchase Amount (USD)'] >= 50) & (self.df['Freq_Score'] >= 1),
        ]
        
        choices = ['High Value', 'Medium Value', 'Regular']
        self.df['Customer_Segment'] = np.select(conditions, choices, default='Low Value')
        
        # Create segmentation analysis plots
        fig, axes = plt.subplots(2, 2, figsize=(15, 12))
        fig.suptitle('Customer Segmentation Analysis', fontsize=16, fontweight='bold')
        
        # 1. Segment Distribution
        segment_counts = self.df['Customer_Segment'].value_counts()
        axes[0,0].pie(segment_counts.values, labels=segment_counts.index, autopct='%1.1f%%')
        axes[0,0].set_title('Customer Segment Distribution')
        
        # 2. Average Purchase by Segment
        segment_avg = self.df.groupby('Customer_Segment')['Purchase Amount (USD)'].mean()
        segment_avg.plot(kind='bar', ax=axes[0,1], color='lightcoral')
        axes[0,1].set_title('Average Purchase Amount by Segment')
        axes[0,1].set_xlabel('Customer Segment')
        axes[0,1].set_ylabel('Average Purchase Amount (USD)')
        
        # 3. Segment by Age Group
        segment_age = pd.crosstab(self.df['Customer_Segment'], self.df['Age'])
        sns.heatmap(segment_age, annot=True, fmt='d', ax=axes[1,0], cmap='Oranges')
        axes[1,0].set_title('Customer Segments by Age Group')
        
        # 4. Subscription Status by Segment
        segment_sub = pd.crosstab(self.df['Customer_Segment'], self.df['Subscription Status'])
        segment_sub.plot(kind='bar', ax=axes[1,1], color=['skyblue', 'orange'])
        axes[1,1].set_title('Subscription Status by Segment')
        axes[1,1].set_xlabel('Customer Segment')
        axes[1,1].set_ylabel('Number of Customers')
        axes[1,1].legend(title='Subscription Status')
        
        plt.tight_layout()
        plt.savefig('visualizations/customer_segmentation.png', dpi=300, bbox_inches='tight')
        plt.show()
        
        # Print segment insights
        print("CUSTOMER SEGMENT SUMMARY:")
        segment_summary = self.df.groupby('Customer_Segment').agg({
            'Purchase Amount (USD)': ['mean', 'sum', 'count'],
            'Review Rating': 'mean',
            'Previous Purchases': 'mean'
        }).round(2)
        print(segment_summary)
    
    def payment_and_shipping_analysis(self):
        """Analyze payment methods and shipping preferences."""
        print("\n" + "="*60)
        print("PAYMENT & SHIPPING ANALYSIS")
        print("="*60)
        
        # Create payment and shipping analysis plots
        fig, axes = plt.subplots(2, 2, figsize=(15, 12))
        fig.suptitle('Payment Methods & Shipping Preferences', fontsize=16, fontweight='bold')
        
        # 1. Payment Method Distribution
        payment_counts = self.df['Payment Method'].value_counts()
        axes[0,0].pie(payment_counts.values, labels=payment_counts.index, autopct='%1.1f%%')
        axes[0,0].set_title('Payment Method Distribution')
        
        # 2. Shipping Type Preferences
        shipping_counts = self.df['Shipping Type'].value_counts()
        shipping_counts.plot(kind='bar', ax=axes[0,1], color='lightgreen')
        axes[0,1].set_title('Shipping Type Preferences')
        axes[0,1].set_xlabel('Shipping Type')
        axes[0,1].set_ylabel('Number of Orders')
        axes[0,1].tick_params(axis='x', rotation=45)
        
        # 3. Average Purchase by Payment Method
        payment_avg = self.df.groupby('Payment Method')['Purchase Amount (USD)'].mean()
        payment_avg.plot(kind='bar', ax=axes[1,0], color='gold')
        axes[1,0].set_title('Average Purchase by Payment Method')
        axes[1,0].set_xlabel('Payment Method')
        axes[1,0].set_ylabel('Average Purchase Amount (USD)')
        axes[1,0].tick_params(axis='x', rotation=45)
        
        # 4. Discount Usage Analysis
        discount_usage = self.df['Discount Applied'].value_counts()
        axes[1,1].pie(discount_usage.values, labels=discount_usage.index, autopct='%1.1f%%')
        axes[1,1].set_title('Discount Usage Distribution')
        
        plt.tight_layout()
        plt.savefig('visualizations/payment_shipping_analysis.png', dpi=300, bbox_inches='tight')
        plt.show()
        
        # Calculate discount impact
        discount_impact = self.df.groupby('Discount Applied')['Purchase Amount (USD)'].mean()
        print("DISCOUNT IMPACT ON PURCHASE AMOUNT:")
        print(discount_impact)
    
    def generate_business_insights(self):
        """Generate comprehensive business insights and recommendations."""
        print("\n" + "="*60)
        print("BUSINESS INSIGHTS & RECOMMENDATIONS")
        print("="*60)
        
        # Key Performance Indicators
        total_revenue = self.df['Purchase Amount (USD)'].sum()
        avg_order_value = self.df['Purchase Amount (USD)'].mean()
        total_customers = self.df['Customer ID'].nunique()
        avg_rating = self.df['Review Rating'].mean()
        
        print("KEY PERFORMANCE INDICATORS:")
        print("-" * 30)
        print(f"Total Revenue: ${total_revenue:,.2f}")
        print(f"Average Order Value: ${avg_order_value:.2f}")
        print(f"Total Customers: {total_customers:,}")
        print(f"Average Customer Rating: {avg_rating:.2f}/5")
        
        # Top insights
        top_category = self.df.groupby('Category')['Purchase Amount (USD)'].sum().idxmax()
        top_location = self.df.groupby('Location')['Purchase Amount (USD)'].sum().idxmax()
        top_age_group = self.df.groupby('Age')['Purchase Amount (USD)'].mean().idxmax()
        peak_season = self.df.groupby('Season')['Purchase Amount (USD)'].sum().idxmax()
        
        print(f"\nTOP PERFORMERS:")
        print("-" * 30)
        print(f"Most profitable category: {top_category}")
        print(f"Top revenue location: {top_location}")
        print(f"Highest spending age group: {top_age_group}")
        print(f"Peak sales season: {peak_season}")
        
        # Generate recommendations
        print(f"\nBUSINESS RECOMMENDATIONS:")
        print("-" * 30)
        print("1. CATEGORY STRATEGY:")
        print(f"   - Focus marketing efforts on {top_category} category")
        print("   - Consider expanding product lines in high-performing categories")
        
        print("2. DEMOGRAPHIC TARGETING:")
        print(f"   - Target {top_age_group} age group for premium products")
        print("   - Develop age-specific marketing campaigns")
        
        print("3. SEASONAL OPTIMIZATION:")
        print(f"   - Increase inventory and marketing spend during {peak_season}")
        print("   - Plan promotional campaigns around seasonal peaks")
        
        print("4. REGIONAL EXPANSION:")
        print(f"   - Consider expanding operations in {top_location}")
        print("   - Analyze successful strategies from top-performing regions")
        
        print("5. CUSTOMER RETENTION:")
        print("   - Implement loyalty programs for high-value customers")
        print("   - Focus on improving customer satisfaction (current rating: {:.2f}/5)".format(avg_rating))
    
    def run_complete_analysis(self):
        """Run the complete consumer behavior analysis."""
        print("Starting Comprehensive Consumer Behavior Analysis...")
        print("=" * 80)
        
        # Create visualizations directory if it doesn't exist
        import os
        if not os.path.exists('visualizations'):
            os.makedirs('visualizations')
        
        # Run all analysis modules
        self.data_overview()
        self.descriptive_statistics()
        self.category_performance_analysis()
        self.seasonal_analysis()
        self.demographic_analysis()
        self.regional_analysis()
        self.customer_segmentation_analysis()
        self.payment_and_shipping_analysis()
        self.generate_business_insights()
        
        print("\n" + "="*80)
        print("ANALYSIS COMPLETE!")
        print("="*80)
        print("All visualizations have been saved to the 'visualizations' folder.")
        print("Review the insights above to make data-driven business decisions.")

def main():
    """Main function to run the analysis."""
    # Initialize the analytics class
    analyzer = ConsumerBehaviorAnalytics()
    
    # Run complete analysis
    analyzer.run_complete_analysis()

if __name__ == "__main__":
    main()