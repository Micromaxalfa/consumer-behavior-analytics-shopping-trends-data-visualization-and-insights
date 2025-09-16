"""
Interactive Dashboard for Consumer Behavior Analytics
===================================================

This script creates an interactive Plotly dashboard with multiple visualizations
for exploring consumer shopping trends data. The dashboard includes interactive
charts, filters, and detailed insights.
"""

import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import plotly.offline as pyo

class InteractiveDashboard:
    """
    Create interactive visualizations for consumer behavior analysis.
    """
    
    def __init__(self, data_path='data/shopping_trends.csv'):
        """Initialize the dashboard class and load data."""
        self.df = pd.read_csv(data_path)
        self.prepare_data()
    
    def prepare_data(self):
        """Prepare data for visualizations."""
        # Create customer segments
        purchase_freq_map = {
            'Weekly': 4, 'Bi-Weekly': 3, 'Monthly': 2, 'Quarterly': 1, 'Annually': 0
        }
        self.df['Freq_Score'] = self.df['Purchase Frequency'].map(purchase_freq_map)
        
        # Create customer segments
        conditions = [
            (self.df['Purchase Amount (USD)'] >= 200) & (self.df['Freq_Score'] >= 3),
            (self.df['Purchase Amount (USD)'] >= 100) & (self.df['Freq_Score'] >= 2),
            (self.df['Purchase Amount (USD)'] >= 50) & (self.df['Freq_Score'] >= 1),
        ]
        choices = ['High Value', 'Medium Value', 'Regular']
        self.df['Customer_Segment'] = np.select(conditions, choices, default='Low Value')
    
    def create_category_dashboard(self):
        """Create interactive category performance dashboard."""
        # Create subplot structure
        fig = make_subplots(
            rows=2, cols=2,
            subplot_titles=('Category Revenue Distribution', 'Purchase Volume by Category',
                          'Average Purchase Amount', 'Category Market Share'),
            specs=[[{"type": "bar"}, {"type": "bar"}],
                   [{"type": "bar"}, {"type": "pie"}]]
        )
        
        # Calculate metrics
        category_revenue = self.df.groupby('Category')['Purchase Amount (USD)'].sum().sort_values(ascending=False)
        category_counts = self.df['Category'].value_counts()
        category_avg = self.df.groupby('Category')['Purchase Amount (USD)'].mean().sort_values(ascending=False)
        
        # Revenue by category
        fig.add_trace(
            go.Bar(x=category_revenue.index, y=category_revenue.values,
                   name='Revenue', marker_color='lightblue'),
            row=1, col=1
        )
        
        # Purchase volume
        fig.add_trace(
            go.Bar(x=category_counts.index, y=category_counts.values,
                   name='Volume', marker_color='lightcoral'),
            row=1, col=2
        )
        
        # Average purchase amount
        fig.add_trace(
            go.Bar(x=category_avg.index, y=category_avg.values,
                   name='Avg Amount', marker_color='lightgreen'),
            row=2, col=1
        )
        
        # Market share pie chart
        fig.add_trace(
            go.Pie(labels=category_counts.index, values=category_counts.values,
                   name="Market Share"),
            row=2, col=2
        )
        
        # Update layout
        fig.update_layout(
            title_text="Interactive Category Performance Dashboard",
            title_x=0.5,
            height=800,
            showlegend=False
        )
        
        # Save as HTML
        pyo.plot(fig, filename='visualizations/interactive_category_dashboard.html', auto_open=False)
        return fig
    
    def create_demographic_insights(self):
        """Create interactive demographic analysis."""
        # Create scatter plot with multiple dimensions
        fig = px.scatter(
            self.df, 
            x='Purchase Amount (USD)', 
            y='Review Rating',
            size='Previous Purchases',
            color='Customer_Segment',
            facet_col='Gender',
            facet_row='Age',
            title='Customer Demographics & Purchase Behavior',
            hover_data=['Location', 'Category', 'Season']
        )
        
        fig.update_layout(height=1000)
        pyo.plot(fig, filename='visualizations/interactive_demographics.html', auto_open=False)
        return fig
    
    def create_seasonal_trends(self):
        """Create interactive seasonal analysis."""
        # Seasonal trends by category
        seasonal_category = self.df.groupby(['Season', 'Category'])['Purchase Amount (USD)'].sum().reset_index()
        
        fig = px.bar(
            seasonal_category,
            x='Season',
            y='Purchase Amount (USD)',
            color='Category',
            title='Seasonal Revenue Trends by Category',
            barmode='group'
        )
        
        fig.update_layout(height=600)
        pyo.plot(fig, filename='visualizations/interactive_seasonal_trends.html', auto_open=False)
        return fig
    
    def create_regional_analysis(self):
        """Create interactive regional performance map."""
        regional_data = self.df.groupby('Location').agg({
            'Purchase Amount (USD)': ['sum', 'mean', 'count'],
            'Review Rating': 'mean'
        }).round(2)
        
        regional_data.columns = ['Total_Revenue', 'Avg_Purchase', 'Num_Purchases', 'Avg_Rating']
        regional_data = regional_data.reset_index()
        
        # Create bubble chart
        fig = px.scatter(
            regional_data,
            x='Avg_Purchase',
            y='Avg_Rating',
            size='Total_Revenue',
            color='Num_Purchases',
            hover_name='Location',
            title='Regional Performance Analysis (Bubble size = Total Revenue)',
            labels={'Avg_Purchase': 'Average Purchase Amount (USD)',
                   'Avg_Rating': 'Average Customer Rating'}
        )
        
        fig.update_layout(height=600)
        pyo.plot(fig, filename='visualizations/interactive_regional_analysis.html', auto_open=False)
        return fig
    
    def create_customer_journey(self):
        """Create customer journey analysis."""
        # Customer lifetime value approximation
        customer_metrics = self.df.groupby('Customer ID').agg({
            'Purchase Amount (USD)': 'sum',
            'Previous Purchases': 'first',
            'Review Rating': 'mean',
            'Customer_Segment': 'first',
            'Age': 'first',
            'Gender': 'first'
        }).reset_index()
        
        customer_metrics['CLV_Estimate'] = customer_metrics['Purchase Amount (USD)'] * customer_metrics['Previous Purchases']
        
        # Create sunburst chart for customer segments
        fig = px.sunburst(
            self.df,
            path=['Customer_Segment', 'Age', 'Gender'],
            values='Purchase Amount (USD)',
            title='Customer Segmentation Hierarchy'
        )
        
        fig.update_layout(height=600)
        pyo.plot(fig, filename='visualizations/interactive_customer_journey.html', auto_open=False)
        return fig
    
    def create_comprehensive_dashboard(self):
        """Create a comprehensive multi-tab dashboard."""
        # Create main dashboard with key metrics
        fig = make_subplots(
            rows=3, cols=3,
            subplot_titles=(
                'Revenue by Category', 'Customer Segments', 'Seasonal Trends',
                'Geographic Distribution', 'Payment Methods', 'Age Demographics',
                'Purchase Frequency', 'Rating Distribution', 'Revenue Over Time'
            ),
            specs=[
                [{"type": "bar"}, {"type": "pie"}, {"type": "bar"}],
                [{"type": "bar"}, {"type": "pie"}, {"type": "bar"}],
                [{"type": "bar"}, {"type": "histogram"}, {"type": "scatter"}]
            ]
        )
        
        # 1. Revenue by Category
        category_revenue = self.df.groupby('Category')['Purchase Amount (USD)'].sum().sort_values(ascending=False)
        fig.add_trace(
            go.Bar(x=category_revenue.index, y=category_revenue.values, name='Category Revenue'),
            row=1, col=1
        )
        
        # 2. Customer Segments
        segment_counts = self.df['Customer_Segment'].value_counts()
        fig.add_trace(
            go.Pie(labels=segment_counts.index, values=segment_counts.values, name="Segments"),
            row=1, col=2
        )
        
        # 3. Seasonal Trends
        seasonal_revenue = self.df.groupby('Season')['Purchase Amount (USD)'].sum()
        fig.add_trace(
            go.Bar(x=seasonal_revenue.index, y=seasonal_revenue.values, name='Seasonal'),
            row=1, col=3
        )
        
        # 4. Geographic Distribution (Top 10)
        location_revenue = self.df.groupby('Location')['Purchase Amount (USD)'].sum().sort_values(ascending=False).head(10)
        fig.add_trace(
            go.Bar(x=location_revenue.index, y=location_revenue.values, name='Geographic'),
            row=2, col=1
        )
        
        # 5. Payment Methods
        payment_counts = self.df['Payment Method'].value_counts()
        fig.add_trace(
            go.Pie(labels=payment_counts.index, values=payment_counts.values, name="Payment"),
            row=2, col=2
        )
        
        # 6. Age Demographics
        age_counts = self.df['Age'].value_counts()
        fig.add_trace(
            go.Bar(x=age_counts.index, y=age_counts.values, name='Age Groups'),
            row=2, col=3
        )
        
        # 7. Purchase Frequency
        freq_counts = self.df['Purchase Frequency'].value_counts()
        fig.add_trace(
            go.Bar(x=freq_counts.index, y=freq_counts.values, name='Frequency'),
            row=3, col=1
        )
        
        # 8. Rating Distribution
        fig.add_trace(
            go.Histogram(x=self.df['Review Rating'], name='Ratings'),
            row=3, col=2
        )
        
        # 9. Revenue vs Previous Purchases
        fig.add_trace(
            go.Scatter(
                x=self.df['Previous Purchases'], 
                y=self.df['Purchase Amount (USD)'],
                mode='markers',
                name='Revenue vs Purchases'
            ),
            row=3, col=3
        )
        
        # Update layout
        fig.update_layout(
            title_text="Comprehensive Consumer Behavior Dashboard",
            title_x=0.5,
            height=1200,
            showlegend=False
        )
        
        # Save comprehensive dashboard
        pyo.plot(fig, filename='visualizations/comprehensive_dashboard.html', auto_open=False)
        return fig
    
    def generate_all_dashboards(self):
        """Generate all interactive dashboards."""
        print("Generating Interactive Dashboards...")
        print("-" * 40)
        
        dashboards = [
            ("Category Performance", self.create_category_dashboard),
            ("Demographics Insights", self.create_demographic_insights),
            ("Seasonal Trends", self.create_seasonal_trends),
            ("Regional Analysis", self.create_regional_analysis),
            ("Customer Journey", self.create_customer_journey),
            ("Comprehensive Dashboard", self.create_comprehensive_dashboard)
        ]
        
        for name, method in dashboards:
            try:
                method()
                print(f"✓ {name} dashboard created successfully")
            except Exception as e:
                print(f"✗ Error creating {name} dashboard: {str(e)}")
        
        print("\nAll interactive dashboards have been saved to the 'visualizations' folder!")
        print("Open the HTML files in your web browser to explore the interactive features.")

def main():
    """Main function to generate interactive dashboards."""
    dashboard = InteractiveDashboard()
    dashboard.generate_all_dashboards()

if __name__ == "__main__":
    main()