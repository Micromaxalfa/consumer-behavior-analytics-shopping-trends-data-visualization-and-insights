"""
Test Script for Consumer Behavior Analytics
==========================================

This script validates that all components of the consumer behavior analytics
project are working correctly.
"""

import os
import pandas as pd
import sys

def test_data_loading():
    """Test if the dataset loads correctly."""
    try:
        df = pd.read_csv('data/shopping_trends.csv')
        print(f"✓ Dataset loaded successfully: {df.shape}")
        return True
    except Exception as e:
        print(f"✗ Failed to load dataset: {e}")
        return False

def test_analysis_modules():
    """Test if analysis modules can be imported."""
    try:
        from consumer_behavior_analysis import ConsumerBehaviorAnalytics
        from interactive_dashboard import InteractiveDashboard
        print("✓ Analysis modules imported successfully")
        return True
    except Exception as e:
        print(f"✗ Failed to import analysis modules: {e}")
        return False

def test_visualizations_exist():
    """Test if visualization files exist."""
    required_files = [
        'visualizations/category_performance.png',
        'visualizations/seasonal_analysis.png',
        'visualizations/demographic_analysis.png',
        'visualizations/regional_analysis.png',
        'visualizations/customer_segmentation.png',
        'visualizations/payment_shipping_analysis.png',
        'visualizations/comprehensive_dashboard.html'
    ]
    
    missing_files = []
    for file_path in required_files:
        if not os.path.exists(file_path):
            missing_files.append(file_path)
    
    if not missing_files:
        print(f"✓ All {len(required_files)} visualization files exist")
        return True
    else:
        print(f"✗ Missing visualization files: {missing_files}")
        return False

def test_project_structure():
    """Test if project structure is correct."""
    required_dirs = ['data', 'visualizations']
    required_files = [
        'requirements.txt',
        'consumer_behavior_analysis.py',
        'interactive_dashboard.py',
        'generate_dataset.py',
        'README.md'
    ]
    
    missing_items = []
    
    # Check directories
    for directory in required_dirs:
        if not os.path.exists(directory):
            missing_items.append(f"Directory: {directory}")
    
    # Check files
    for file_path in required_files:
        if not os.path.exists(file_path):
            missing_items.append(f"File: {file_path}")
    
    if not missing_items:
        print("✓ Project structure is correct")
        return True
    else:
        print(f"✗ Missing project items: {missing_items}")
        return False

def main():
    """Run all tests."""
    print("Running Consumer Behavior Analytics Tests...")
    print("=" * 50)
    
    tests = [
        ("Project Structure", test_project_structure),
        ("Data Loading", test_data_loading),
        ("Analysis Modules", test_analysis_modules),
        ("Visualizations", test_visualizations_exist)
    ]
    
    passed = 0
    total = len(tests)
    
    for test_name, test_func in tests:
        print(f"\nTesting {test_name}:")
        if test_func():
            passed += 1
    
    print("\n" + "=" * 50)
    print(f"Test Results: {passed}/{total} tests passed")
    
    if passed == total:
        print("🎉 All tests passed! The project is ready to use.")
        return 0
    else:
        print("⚠️ Some tests failed. Please check the issues above.")
        return 1

if __name__ == "__main__":
    sys.exit(main())