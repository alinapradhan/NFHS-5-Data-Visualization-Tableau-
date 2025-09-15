#!/usr/bin/env python3
"""
Create the CLASS_2025_07_02.xlsx file with required sheets and data structure
for the Tableau dashboard project.
"""

import pandas as pd
import numpy as np
from openpyxl import Workbook
from openpyxl.utils.dataframe import dataframe_to_rows

# Sample data for World Bank economies classification
def create_economies_data():
    """Create the List of economies sheet data"""
    
    # Define regions, income groups, and lending categories
    regions = ['East Asia & Pacific', 'Europe & Central Asia', 'Latin America & Caribbean', 
               'Middle East & North Africa', 'North America', 'South Asia', 'Sub-Saharan Africa']
    
    income_groups = ['High income', 'Upper middle income', 'Lower middle income', 'Low income']
    
    lending_categories = ['IBRD', 'IDA', 'Blend', 'Not classified']
    
    # Create sample countries data
    countries_data = [
        # North America
        ('United States', 'North America', 'High income', 'Not classified'),
        ('Canada', 'North America', 'High income', 'Not classified'),
        
        # Europe & Central Asia
        ('Germany', 'Europe & Central Asia', 'High income', 'Not classified'),
        ('France', 'Europe & Central Asia', 'High income', 'Not classified'),
        ('United Kingdom', 'Europe & Central Asia', 'High income', 'Not classified'),
        ('Italy', 'Europe & Central Asia', 'High income', 'Not classified'),
        ('Spain', 'Europe & Central Asia', 'High income', 'Not classified'),
        ('Poland', 'Europe & Central Asia', 'High income', 'IBRD'),
        ('Turkey', 'Europe & Central Asia', 'Upper middle income', 'IBRD'),
        ('Russian Federation', 'Europe & Central Asia', 'Upper middle income', 'IBRD'),
        ('Kazakhstan', 'Europe & Central Asia', 'Upper middle income', 'IBRD'),
        ('Ukraine', 'Europe & Central Asia', 'Lower middle income', 'Blend'),
        ('Georgia', 'Europe & Central Asia', 'Upper middle income', 'Blend'),
        
        # East Asia & Pacific
        ('Japan', 'East Asia & Pacific', 'High income', 'Not classified'),
        ('Korea, Rep.', 'East Asia & Pacific', 'High income', 'Not classified'),
        ('Australia', 'East Asia & Pacific', 'High income', 'Not classified'),
        ('New Zealand', 'East Asia & Pacific', 'High income', 'Not classified'),
        ('China', 'East Asia & Pacific', 'Upper middle income', 'IBRD'),
        ('Thailand', 'East Asia & Pacific', 'Upper middle income', 'IBRD'),
        ('Malaysia', 'East Asia & Pacific', 'Upper middle income', 'IBRD'),
        ('Indonesia', 'East Asia & Pacific', 'Upper middle income', 'IBRD'),
        ('Philippines', 'East Asia & Pacific', 'Lower middle income', 'IBRD'),
        ('Vietnam', 'East Asia & Pacific', 'Lower middle income', 'Blend'),
        ('Cambodia', 'East Asia & Pacific', 'Lower middle income', 'IDA'),
        ('Myanmar', 'East Asia & Pacific', 'Lower middle income', 'IDA'),
        ('Papua New Guinea', 'East Asia & Pacific', 'Lower middle income', 'Blend'),
        
        # South Asia
        ('India', 'South Asia', 'Lower middle income', 'Blend'),
        ('Bangladesh', 'South Asia', 'Lower middle income', 'IDA'),
        ('Pakistan', 'South Asia', 'Lower middle income', 'Blend'),
        ('Sri Lanka', 'South Asia', 'Upper middle income', 'Blend'),
        ('Nepal', 'South Asia', 'Lower middle income', 'IDA'),
        ('Afghanistan', 'South Asia', 'Low income', 'IDA'),
        ('Bhutan', 'South Asia', 'Upper middle income', 'IDA'),
        ('Maldives', 'South Asia', 'Upper middle income', 'IDA'),
        
        # Latin America & Caribbean
        ('Chile', 'Latin America & Caribbean', 'High income', 'IBRD'),
        ('Uruguay', 'Latin America & Caribbean', 'High income', 'IBRD'),
        ('Argentina', 'Latin America & Caribbean', 'Upper middle income', 'IBRD'),
        ('Brazil', 'Latin America & Caribbean', 'Upper middle income', 'IBRD'),
        ('Mexico', 'Latin America & Caribbean', 'Upper middle income', 'IBRD'),
        ('Colombia', 'Latin America & Caribbean', 'Upper middle income', 'IBRD'),
        ('Peru', 'Latin America & Caribbean', 'Upper middle income', 'IBRD'),
        ('Ecuador', 'Latin America & Caribbean', 'Upper middle income', 'IBRD'),
        ('Guatemala', 'Latin America & Caribbean', 'Upper middle income', 'IBRD'),
        ('Honduras', 'Latin America & Caribbean', 'Lower middle income', 'IDA'),
        ('Nicaragua', 'Latin America & Caribbean', 'Lower middle income', 'IDA'),
        ('Bolivia', 'Latin America & Caribbean', 'Lower middle income', 'Blend'),
        ('Haiti', 'Latin America & Caribbean', 'Lower middle income', 'IDA'),
        
        # Middle East & North Africa
        ('Saudi Arabia', 'Middle East & North Africa', 'High income', 'Not classified'),
        ('United Arab Emirates', 'Middle East & North Africa', 'High income', 'Not classified'),
        ('Kuwait', 'Middle East & North Africa', 'High income', 'Not classified'),
        ('Qatar', 'Middle East & North Africa', 'High income', 'Not classified'),
        ('Bahrain', 'Middle East & North Africa', 'High income', 'Not classified'),
        ('Israel', 'Middle East & North Africa', 'High income', 'Not classified'),
        ('Iran, Islamic Rep.', 'Middle East & North Africa', 'Upper middle income', 'Not classified'),
        ('Jordan', 'Middle East & North Africa', 'Upper middle income', 'IBRD'),
        ('Lebanon', 'Middle East & North Africa', 'Upper middle income', 'IBRD'),
        ('Tunisia', 'Middle East & North Africa', 'Upper middle income', 'IBRD'),
        ('Algeria', 'Middle East & North Africa', 'Upper middle income', 'IBRD'),
        ('Morocco', 'Middle East & North Africa', 'Lower middle income', 'IBRD'),
        ('Egypt, Arab Rep.', 'Middle East & North Africa', 'Lower middle income', 'Blend'),
        ('Yemen, Rep.', 'Middle East & North Africa', 'Low income', 'IDA'),
        
        # Sub-Saharan Africa
        ('South Africa', 'Sub-Saharan Africa', 'Upper middle income', 'IBRD'),
        ('Botswana', 'Sub-Saharan Africa', 'Upper middle income', 'IBRD'),
        ('Mauritius', 'Sub-Saharan Africa', 'Upper middle income', 'IBRD'),
        ('Namibia', 'Sub-Saharan Africa', 'Upper middle income', 'IBRD'),
        ('Gabon', 'Sub-Saharan Africa', 'Upper middle income', 'IBRD'),
        ('Ghana', 'Sub-Saharan Africa', 'Lower middle income', 'Blend'),
        ('Kenya', 'Sub-Saharan Africa', 'Lower middle income', 'Blend'),
        ('Nigeria', 'Sub-Saharan Africa', 'Lower middle income', 'Blend'),
        ('Senegal', 'Sub-Saharan Africa', 'Lower middle income', 'IDA'),
        ('Tanzania', 'Sub-Saharan Africa', 'Lower middle income', 'IDA'),
        ('Uganda', 'Sub-Saharan Africa', 'Low income', 'IDA'),
        ('Rwanda', 'Sub-Saharan Africa', 'Lower middle income', 'IDA'),
        ('Ethiopia', 'Sub-Saharan Africa', 'Low income', 'IDA'),
        ('Mali', 'Sub-Saharan Africa', 'Low income', 'IDA'),
        ('Burkina Faso', 'Sub-Saharan Africa', 'Low income', 'IDA'),
        ('Niger', 'Sub-Saharan Africa', 'Low income', 'IDA'),
        ('Chad', 'Sub-Saharan Africa', 'Low income', 'IDA'),
        ('Madagascar', 'Sub-Saharan Africa', 'Low income', 'IDA'),
        ('Mozambique', 'Sub-Saharan Africa', 'Low income', 'IDA'),
        ('Malawi', 'Sub-Saharan Africa', 'Low income', 'IDA'),
    ]
    
    df = pd.DataFrame(countries_data, columns=['Country', 'Region', 'Income Group', 'Lending Category'])
    return df

def create_composition_data():
    """Create the composition sheet data for World Bank group mappings by region"""
    
    composition_data = [
        ('East Asia & Pacific', 'IBRD', 6),
        ('East Asia & Pacific', 'IDA', 3),
        ('East Asia & Pacific', 'Blend', 2),
        ('East Asia & Pacific', 'Not classified', 4),
        
        ('Europe & Central Asia', 'IBRD', 7),
        ('Europe & Central Asia', 'IDA', 0),
        ('Europe & Central Asia', 'Blend', 2),
        ('Europe & Central Asia', 'Not classified', 4),
        
        ('Latin America & Caribbean', 'IBRD', 9),
        ('Latin America & Caribbean', 'IDA', 4),
        ('Latin America & Caribbean', 'Blend', 1),
        ('Latin America & Caribbean', 'Not classified', 0),
        
        ('Middle East & North Africa', 'IBRD', 5),
        ('Middle East & North Africa', 'IDA', 1),
        ('Middle East & North Africa', 'Blend', 1),
        ('Middle East & North Africa', 'Not classified', 7),
        
        ('North America', 'IBRD', 0),
        ('North America', 'IDA', 0),
        ('North America', 'Blend', 0),
        ('North America', 'Not classified', 2),
        
        ('South Asia', 'IBRD', 0),
        ('South Asia', 'IDA', 4),
        ('South Asia', 'Blend', 3),
        ('South Asia', 'Not classified', 0),
        
        ('Sub-Saharan Africa', 'IBRD', 5),
        ('Sub-Saharan Africa', 'IDA', 13),
        ('Sub-Saharan Africa', 'Blend', 2),
        ('Sub-Saharan Africa', 'Not classified', 0),
    ]
    
    df = pd.DataFrame(composition_data, columns=['Region', 'Lending Category', 'Number of Countries'])
    return df

def create_notes_data():
    """Create the notes sheet with definitions and contextual information"""
    
    notes_data = [
        ('Term', 'Definition'),
        ('Income Group', 'World Bank classification based on Gross National Income (GNI) per capita'),
        ('High income', 'GNI per capita of $13,845 or more in 2024'),
        ('Upper middle income', 'GNI per capita between $4,516 and $13,844 in 2024'),
        ('Lower middle income', 'GNI per capita between $1,136 and $4,515 in 2024'),
        ('Low income', 'GNI per capita of $1,135 or less in 2024'),
        ('IBRD', 'International Bank for Reconstruction and Development - provides loans and grants to creditworthy low- and middle-income countries'),
        ('IDA', 'International Development Association - provides grants and low to zero-interest loans to the world\'s poorest countries'),
        ('Blend', 'Countries eligible for both IBRD and IDA resources'),
        ('Not classified', 'Countries not eligible for World Bank lending (typically high-income countries)'),
        ('Region', 'World Bank geographical classification for operational purposes'),
        ('East Asia & Pacific', 'Countries in East Asia, Southeast Asia, and Pacific Island nations'),
        ('Europe & Central Asia', 'European countries and former Soviet Union states in Central Asia'),
        ('Latin America & Caribbean', 'Countries in Central and South America, and Caribbean islands'),
        ('Middle East & North Africa', 'Countries in the Middle East and North African region'),
        ('North America', 'United States and Canada'),
        ('South Asia', 'Countries in the Indian subcontinent and surrounding areas'),
        ('Sub-Saharan Africa', 'African countries south of the Sahara Desert'),
        ('Dashboard Purpose', 'This dashboard provides an overview of World Bank member countries by region, income classification, and lending eligibility'),
        ('Data Source', 'World Bank Country and Lending Groups Classification (CLASS_2025_07_02)'),
        ('Last Updated', 'July 2, 2025'),
    ]
    
    df = pd.DataFrame(notes_data[1:], columns=notes_data[0])
    return df

def main():
    """Create the Excel file with all required sheets"""
    
    # Create the Excel file
    with pd.ExcelWriter('/home/runner/work/tableau-project-/tableau-project-/CLASS_2025_07_02.xlsx', 
                       engine='openpyxl') as writer:
        
        # Create List of economies sheet
        economies_df = create_economies_data()
        economies_df.to_excel(writer, sheet_name='List of economies', index=False)
        
        # Create composition sheet
        composition_df = create_composition_data()
        composition_df.to_excel(writer, sheet_name='composition', index=False)
        
        # Create notes sheet
        notes_df = create_notes_data()
        notes_df.to_excel(writer, sheet_name='notes', index=False)
    
    print("Excel file 'CLASS_2025_07_02.xlsx' created successfully!")
    print(f"List of economies: {len(economies_df)} countries")
    print(f"Composition: {len(composition_df)} regional mappings")
    print(f"Notes: {len(notes_df)} definitions")

if __name__ == "__main__":
    main()