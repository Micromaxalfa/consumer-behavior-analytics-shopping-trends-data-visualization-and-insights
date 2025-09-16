# Consumer Behavior Analytics - Shopping Trends Data Visualization and Insights

A comprehensive data analytics project that analyzes consumer shopping behavior using the shopping_trends.csv dataset. This project provides in-depth data exploration, descriptive statistics, and a variety of visualizations including bar charts, pie charts, line plots, and interactive dashboards to understand category performance, seasonal demand, regional differences, demographics, and purchasing patterns.

## 🚀 Features

- **Comprehensive Data Analysis**: Complete data exploration with descriptive statistics
- **Static Visualizations**: Professional-grade charts using Matplotlib and Seaborn
- **Interactive Dashboards**: Dynamic HTML dashboards using Plotly
- **Customer Segmentation**: Advanced segmentation based on purchasing behavior
- **Business Insights**: Actionable recommendations for data-driven decisions
- **Regional Analysis**: Geographic performance comparisons
- **Seasonal Trends**: Temporal pattern analysis
- **Demographic Insights**: Age, gender, and location-based analysis

## 📊 Generated Visualizations

### Static Charts (PNG)
- **Category Performance Analysis**: Revenue, volume, and market share by product category
- **Seasonal Analysis**: Demand patterns across different seasons
- **Demographic Analysis**: Customer distribution and spending patterns by demographics
- **Regional Analysis**: Geographic performance and customer distribution
- **Customer Segmentation**: Advanced customer grouping based on behavior
- **Payment & Shipping Analysis**: Payment methods and shipping preferences

### Interactive Dashboards (HTML)
- **Category Performance Dashboard**: Interactive category metrics with drill-down capabilities
- **Demographics Insights**: Multi-dimensional scatter plots with filters
- **Seasonal Trends**: Dynamic seasonal analysis by category
- **Regional Analysis**: Interactive bubble charts for geographic insights
- **Customer Journey**: Sunburst charts for segmentation hierarchy
- **Comprehensive Dashboard**: All-in-one dashboard with key metrics

## 🛠️ Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/Micromaxalfa/consumer-behavior-analytics-shopping-trends-data-visualization-and-insights.git
   cd consumer-behavior-analytics-shopping-trends-data-visualization-and-insights
   ```

2. **Install required dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## 📈 Usage

### 1. Generate Sample Dataset (Optional)
If you need to create a new dataset:
```bash
python generate_dataset.py
```

### 2. Run Complete Analysis
Execute the main analysis script to generate all static visualizations and insights:
```bash
python consumer_behavior_analysis.py
```

### 3. Generate Interactive Dashboards
Create interactive HTML dashboards:
```bash
python interactive_dashboard.py
```

### 4. View Results
- Static charts are saved in the `visualizations/` folder as PNG files
- Interactive dashboards are saved as HTML files in the `visualizations/` folder
- Open HTML files in your web browser for interactive exploration

## 📁 Project Structure

```
├── data/
│   └── shopping_trends.csv          # Main dataset
├── visualizations/                  # Generated charts and dashboards
│   ├── category_performance.png
│   ├── seasonal_analysis.png
│   ├── demographic_analysis.png
│   ├── regional_analysis.png
│   ├── customer_segmentation.png
│   ├── payment_shipping_analysis.png
│   ├── interactive_category_dashboard.html
│   ├── interactive_demographics.html
│   ├── interactive_seasonal_trends.html
│   ├── interactive_regional_analysis.html
│   ├── interactive_customer_journey.html
│   └── comprehensive_dashboard.html
├── analysis/                        # Analysis scripts (optional organization)
├── consumer_behavior_analysis.py    # Main analysis script
├── interactive_dashboard.py         # Interactive dashboard generator
├── generate_dataset.py             # Dataset generation script
├── requirements.txt                # Python dependencies
└── README.md                       # This file
```

## 📊 Dataset Schema

The shopping_trends.csv dataset contains the following columns:

| Column | Description | Type |
|--------|-------------|------|
| Customer ID | Unique customer identifier | Integer |
| Age | Customer age group | Categorical |
| Gender | Customer gender | Categorical |
| Item Purchased | Specific item bought | Text |
| Category | Product category | Categorical |
| Purchase Amount (USD) | Purchase value in USD | Float |
| Location | Customer location | Categorical |
| Size | Product size (when applicable) | Categorical |
| Color | Product color (when applicable) | Categorical |
| Season | Purchase season | Categorical |
| Review Rating | Customer rating (1-5) | Integer |
| Subscription Status | Customer subscription status | Boolean |
| Payment Method | Payment method used | Categorical |
| Shipping Type | Shipping preference | Categorical |
| Discount Applied | Whether discount was applied | Boolean |
| Promo Code Used | Whether promo code was used | Boolean |
| Previous Purchases | Number of previous purchases | Integer |
| Purchase Frequency | Purchase frequency pattern | Categorical |

## 🎯 Key Insights and Business Recommendations

The analysis provides insights in several key areas:

### 1. Category Performance
- **Electronics** generates the highest revenue per transaction
- **Home & Garden** has the highest purchase volume
- Focus marketing efforts on high-performing categories

### 2. Seasonal Trends
- **Winter** shows peak sales performance
- Different categories show varying seasonal patterns
- Plan inventory and promotions around seasonal peaks

### 3. Customer Demographics
- **18-25 age group** shows highest average spending
- Gender-based preferences vary significantly across categories
- Target demographics with personalized marketing

### 4. Regional Analysis
- **Texas** leads in total revenue generation
- Regional preferences show distinct patterns
- Consider regional expansion opportunities

### 5. Customer Segmentation
- **High Value** customers contribute significantly to revenue
- Different segments show distinct behavioral patterns
- Implement targeted retention strategies

## 🔧 Dependencies

- **pandas** >= 1.5.0: Data manipulation and analysis
- **numpy** >= 1.21.0: Numerical computing
- **matplotlib** >= 3.5.0: Static plotting
- **seaborn** >= 0.11.0: Statistical visualization
- **plotly** >= 5.0.0: Interactive visualizations
- **scipy** >= 1.9.0: Scientific computing
- **scikit-learn** >= 1.1.0: Machine learning utilities

## 📝 Customization

### Adding New Analysis
To add new analysis modules:

1. Create new methods in the `ConsumerBehaviorAnalytics` class
2. Add visualization generation code
3. Include insights in the business recommendations section

### Modifying Visualizations
- Edit the plotting functions in `consumer_behavior_analysis.py`
- Customize colors, styles, and layouts
- Add new chart types as needed

### Creating Custom Dashboards
- Extend the `InteractiveDashboard` class
- Add new Plotly visualizations
- Combine multiple charts in subplots

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/new-analysis`)
3. Commit your changes (`git commit -am 'Add new analysis feature'`)
4. Push to the branch (`git push origin feature/new-analysis`)
5. Create a Pull Request

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 🙏 Acknowledgments

- Dataset inspired by real-world shopping trends
- Visualization techniques based on best practices in data analytics
- Interactive dashboards powered by Plotly

## 📞 Support

For questions, suggestions, or issues:
- Open an issue on GitHub
- Review the documentation
- Check existing visualizations for examples

---

**Note**: This project is designed for educational and analytical purposes. The dataset is synthetically generated to demonstrate various data analysis techniques and visualization methods.