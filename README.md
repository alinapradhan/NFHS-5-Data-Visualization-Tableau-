# World Bank Countries Dashboard

An interactive Tableau dashboard analyzing World Bank country classifications by region, income group, and lending category.

## Overview

This dashboard provides comprehensive insights into World Bank member countries, featuring:

- **Top KPI Cards**: Key metrics including total countries, regions, income groups, and lending categories
- **Income Group Distribution**: Pie chart showing the distribution of countries across income classifications
- **Lending Category Analysis**: Bar chart displaying countries by World Bank lending eligibility
- **Regional Breakdown**: Horizontal bar chart showing number of countries per region
- **Cross-Analysis**: Stacked bar chart revealing income group composition within each region
- **Interactive Filters**: Dynamic filtering by region, income group, and lending category
- **Notes Section**: Contextual information and definitions for better understanding

## Data Source

**File**: `CLASS_2025_07_02.xlsx`

The Excel file contains three sheets:

1. **List of economies**: Primary dataset with 81 countries and their classifications
   - Country names
   - Regional assignments (7 regions)
   - Income group classifications (4 categories)
   - Lending category eligibility (4 types)

2. **Composition**: Regional summary data showing World Bank group mappings
   - Regional breakdowns by lending category
   - Country counts per classification

3. **Notes**: Definitions and contextual information
   - Income group definitions with GNI thresholds
   - Lending category explanations
   - Regional classification details
   - Data source information

## Dashboard Components

### KPI Cards
- **Total Countries**: 81 World Bank member countries
- **Regions**: 7 geographical regions
- **Income Groups**: 4 classification levels
- **Lending Categories**: 4 eligibility types

### Visualizations

1. **Income Group Distribution (Pie Chart)**
   - Shows percentage breakdown of countries by income level
   - Hover tooltips display exact counts and percentages

2. **Lending Category Distribution (Bar Chart)**
   - Vertical bar chart showing countries by lending eligibility
   - Color-coded by category for easy identification

3. **Countries per Region (Horizontal Bar Chart)**
   - Regional comparison of member country counts
   - Ordered from highest to lowest for easy ranking

4. **Income Groups by Region (Stacked Bar Chart)**
   - Cross-analysis showing income distribution within each region
   - Stacked format reveals regional economic patterns

### Interactive Features

- **Filter Panel**: Dynamic filters for Region, Income Group, and Lending Category
- **Hover Tooltips**: Additional metadata on hover for deeper insights
- **Cross-Filtering**: Selections in one chart filter related visualizations
- **Responsive Design**: Mobile-optimized layout for various screen sizes

## Classifications Explained

### Income Groups (by GNI per capita in 2024)
- **High income**: $13,845 or more
- **Upper middle income**: $4,516 - $13,844
- **Lower middle income**: $1,136 - $4,515
- **Low income**: $1,135 or less

### Lending Categories
- **IBRD**: International Bank for Reconstruction and Development
- **IDA**: International Development Association (grants and low-interest loans)
- **Blend**: Eligible for both IBRD and IDA resources
- **Not classified**: Not eligible for World Bank lending (typically high-income countries)

### Regions
- East Asia & Pacific
- Europe & Central Asia
- Latin America & Caribbean
- Middle East & North Africa
- North America
- South Asia
- Sub-Saharan Africa

## Usage Instructions

1. **Open Dashboard**: Load `World_Bank_Countries_Dashboard.twb` in Tableau Desktop or Tableau Reader
2. **Data Connection**: Ensure `CLASS_2025_07_02.xlsx` is in the same directory
3. **Interactive Exploration**: 
   - Use filter panel on the left to focus on specific regions or classifications
   - Hover over charts for detailed tooltips
   - Click on chart elements to cross-filter other visualizations
4. **Mobile Viewing**: Dashboard automatically adapts to smaller screens

## Technical Specifications

- **Tableau Version**: Compatible with Tableau 18.1 and later
- **Data Format**: Microsoft Excel (.xlsx)
- **Dashboard Size**: 1200x800 (desktop), responsive mobile layout
- **Color Scheme**: Clean Tableau default palette with high contrast
- **Performance**: Optimized for datasets up to 1000+ countries

## Files Included

- `World_Bank_Countries_Dashboard.twb` - Main Tableau workbook
- `CLASS_2025_07_02.xlsx` - Source data file
- `create_excel_data.py` - Python script to generate sample data
- `create_tableau_workbook.py` - Python script to generate Tableau workbook
- `README.md` - This documentation file

## Data Updates

To update the dashboard with new data:

1. Update the `CLASS_2025_07_02.xlsx` file with new country classifications
2. Refresh the data connection in Tableau
3. Re-publish if using Tableau Server/Online

## Insights and Analysis

The dashboard reveals key patterns in global development:

- **Regional Disparities**: Clear differences in income distribution across regions
- **Lending Patterns**: Concentration of IDA countries in Sub-Saharan Africa and South Asia
- **Development Trajectories**: Income group transitions over time (with historical data)
- **Geographic Clustering**: Similar income levels within regional groupings

## Support

For technical issues or questions about the dashboard:
- Check data file locations and permissions
- Verify Tableau version compatibility
- Consult Tableau documentation for advanced customization

---

*Last Updated: January 2025*
*Data Source: World Bank Country and Lending Groups Classification*