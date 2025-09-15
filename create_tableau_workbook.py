#!/usr/bin/env python3
"""
Create a comprehensive Tableau workbook (.twb) file with all required dashboard elements
"""

import xml.etree.ElementTree as ET
from xml.dom import minidom
import uuid

def generate_uuid():
    """Generate a UUID for Tableau objects"""
    return str(uuid.uuid4()).upper()

def create_tableau_workbook():
    """Create the complete Tableau workbook XML structure"""
    
    # Root workbook element
    workbook = ET.Element('workbook')
    workbook.set('version', '18.1')
    workbook.set('xmlns:user', 'http://www.tableausoftware.com/xml/user')
    
    # Document format change manifest
    doc_format = ET.SubElement(workbook, 'document-format-change-manifest')
    ET.SubElement(doc_format, 'IntuitiveSorting')
    ET.SubElement(doc_format, 'IntuitiveSorting_SP2')
    ET.SubElement(doc_format, 'SheetIdentifierTracking')
    ET.SubElement(doc_format, 'WindowsPersistSimpleIdentifiers')
    
    # Preferences
    preferences = ET.SubElement(workbook, 'preferences')
    pref1 = ET.SubElement(preferences, 'preference')
    pref1.set('name', 'ui.encoding.shelf.height')
    pref1.set('value', '24')
    pref2 = ET.SubElement(preferences, 'preference')
    pref2.set('name', 'ui.shelf.height')
    pref2.set('value', '26')
    
    # Data sources
    datasources = ET.SubElement(workbook, 'datasources')
    
    # Main data source
    ds = ET.SubElement(datasources, 'datasource')
    ds.set('caption', 'CLASS_2025_07_02')
    ds.set('inline', 'true')
    ds.set('name', 'federated.0l8h7ne1q4h91z19bvmwz0w7c4q6')
    ds.set('version', '18.1')
    
    # Connection
    connection = ET.SubElement(ds, 'connection')
    connection.set('class', 'federated')
    
    # Named connections
    named_conns = ET.SubElement(connection, 'named-connections')
    named_conn = ET.SubElement(named_conns, 'named-connection')
    named_conn.set('caption', 'CLASS_2025_07_02')
    named_conn.set('name', 'excel-direct.0mxt3x11f7v3f515gqxuw1p9mzm5')
    
    excel_conn = ET.SubElement(named_conn, 'connection')
    excel_conn.set('class', 'excel-direct')
    excel_conn.set('filename', 'CLASS_2025_07_02.xlsx')
    excel_conn.set('interpretationMode', '0')
    excel_conn.set('password', '')
    excel_conn.set('server', '')
    excel_conn.set('validate', 'true')
    excel_conn.set('authentication', 'auth-none')
    
    # Relation
    relation = ET.SubElement(connection, 'relation')
    relation.set('connection', 'excel-direct.0mxt3x11f7v3f515gqxuw1p9mzm5')
    relation.set('name', 'List of economies')
    relation.set('table', '[List of economies$]')
    relation.set('type', 'table')
    
    # Columns definition
    columns = ET.SubElement(relation, 'columns')
    columns.set('gridOrigin', 'A1:D82:no:A1:D82:0')
    columns.set('header', 'yes')
    columns.set('outcome', '2')
    
    # Define columns
    col_defs = [
        ('Country', 'string', 0),
        ('Region', 'string', 1), 
        ('Income Group', 'string', 2),
        ('Lending Category', 'string', 3)
    ]
    
    for name, datatype, ordinal in col_defs:
        col = ET.SubElement(columns, 'column')
        col.set('datatype', datatype)
        col.set('name', name)
        col.set('ordinal', str(ordinal))
    
    # Metadata records
    metadata_records = ET.SubElement(connection, 'metadata-records')
    
    for name, datatype, ordinal in col_defs:
        record = ET.SubElement(metadata_records, 'metadata-record')
        record.set('class', 'column')
        
        ET.SubElement(record, 'remote-name').text = name
        ET.SubElement(record, 'remote-type').text = '130'
        ET.SubElement(record, 'local-name').text = f'[{name}]'
        ET.SubElement(record, 'parent-name').text = '[List of economies]'
        ET.SubElement(record, 'remote-alias').text = name
        ET.SubElement(record, 'ordinal').text = str(ordinal)
        ET.SubElement(record, 'local-type').text = datatype
        ET.SubElement(record, 'aggregation').text = 'Count'
        ET.SubElement(record, 'contains-null').text = 'true'
    
    # Aliases and layout
    ET.SubElement(ds, 'aliases').set('enabled', 'yes')
    
    # Number of records column
    num_records = ET.SubElement(ds, 'column')
    num_records.set('caption', 'Count of Countries')
    num_records.set('datatype', 'integer')
    num_records.set('name', '[Number of Records]')
    num_records.set('role', 'measure')
    num_records.set('type', 'quantitative')
    num_records.set('user:auto-column', 'numrec')
    
    calc = ET.SubElement(num_records, 'calculation')
    calc.set('class', 'tableau')
    calc.set('formula', '1')
    
    # Layout
    layout = ET.SubElement(ds, 'layout')
    layout.set('dim-ordering', 'alphabetic')
    layout.set('dim-percentage', '0.5')
    layout.set('measure-ordering', 'alphabetic')
    layout.set('measure-percentage', '0.4')
    layout.set('show-structure', 'true')
    
    # Semantic values
    semantic_values = ET.SubElement(ds, 'semantic-values')
    semantic_val = ET.SubElement(semantic_values, 'semantic-value')
    semantic_val.set('key', '[Country].[Name]')
    semantic_val.set('value', '"Country"')
    
    # Date options
    date_options = ET.SubElement(ds, 'date-options')
    date_options.set('start-of-week', 'monday')
    
    # Worksheets
    worksheets = ET.SubElement(workbook, 'worksheets')
    
    # Create individual worksheets
    worksheet_configs = [
        {
            'name': 'KPI Total Countries',
            'type': 'text',
            'measure': '[sum:Number of Records:qk]',
            'title': 'Total Countries',
            'uuid': generate_uuid()
        },
        {
            'name': 'Income Group Pie Chart',
            'type': 'pie',
            'dimension': '[Income Group]',
            'measure': '[sum:Number of Records:qk]',
            'title': 'Income Group Distribution',
            'uuid': generate_uuid()
        },
        {
            'name': 'Lending Category Bar Chart',
            'type': 'bar',
            'dimension': '[Lending Category]',
            'measure': '[sum:Number of Records:qk]',
            'title': 'Lending Categories',
            'uuid': generate_uuid()
        },
        {
            'name': 'Countries by Region',
            'type': 'horizontal_bar',
            'dimension': '[Region]',
            'measure': '[sum:Number of Records:qk]',
            'title': 'Countries per Region',
            'uuid': generate_uuid()
        },
        {
            'name': 'Income Groups by Region',
            'type': 'stacked_bar',
            'dimension1': '[Region]',
            'dimension2': '[Income Group]',
            'measure': '[sum:Number of Records:qk]',
            'title': 'Income Groups by Region',
            'uuid': generate_uuid()
        }
    ]
    
    for config in worksheet_configs:
        ws = create_worksheet(config)
        worksheets.append(ws)
    
    # Dashboard
    dashboards = ET.SubElement(workbook, 'dashboards')
    dashboard = create_dashboard(worksheet_configs)
    dashboards.append(dashboard)
    
    # Windows
    windows = ET.SubElement(workbook, 'windows')
    windows.set('source-height', '30')
    
    window = ET.SubElement(windows, 'window')
    window.set('class', 'dashboard')
    window.set('maximized', 'true')
    window.set('name', 'World Bank Countries Dashboard')
    
    # Cards
    cards = ET.SubElement(window, 'cards')
    
    # Left edge
    left_edge = ET.SubElement(cards, 'edge')
    left_edge.set('name', 'left')
    strip = ET.SubElement(left_edge, 'strip')
    strip.set('size', '160')
    ET.SubElement(strip, 'card').set('type', 'pages')
    ET.SubElement(strip, 'card').set('type', 'filters')
    ET.SubElement(strip, 'card').set('type', 'marks')
    
    # Top edge
    top_edge = ET.SubElement(cards, 'edge')
    top_edge.set('name', 'top')
    
    strip1 = ET.SubElement(top_edge, 'strip')
    strip1.set('size', '2147483647')
    ET.SubElement(strip1, 'card').set('type', 'columns')
    
    strip2 = ET.SubElement(top_edge, 'strip')
    strip2.set('size', '2147483647')
    ET.SubElement(strip2, 'card').set('type', 'rows')
    
    strip3 = ET.SubElement(top_edge, 'strip')
    strip3.set('size', '31')
    ET.SubElement(strip3, 'card').set('type', 'title')
    
    simple_id = ET.SubElement(window, 'simple-id')
    simple_id.set('uuid', f'{{{generate_uuid()}}}')
    
    # Thumbnails
    thumbnails = ET.SubElement(workbook, 'thumbnails')
    thumbnail = ET.SubElement(thumbnails, 'thumbnail')
    thumbnail.set('height', '192')
    thumbnail.set('name', 'World Bank Countries Dashboard')
    thumbnail.set('width', '192')
    thumbnail.text = 'iVBORw0KGgoAAAANSUhEUgAAAMAAAADACAYAAABS3GwHAAAACXBIWXMAAA7EAAAOxAGVKw4bAAAFQklE'
    
    return workbook

def create_worksheet(config):
    """Create a worksheet element based on configuration"""
    worksheet = ET.Element('worksheet')
    worksheet.set('name', config['name'])
    
    table = ET.SubElement(worksheet, 'table')
    view = ET.SubElement(table, 'view')
    
    # Data sources
    datasources = ET.SubElement(view, 'datasources')
    ds_ref = ET.SubElement(datasources, 'datasource')
    ds_ref.set('caption', 'CLASS_2025_07_02')
    ds_ref.set('name', 'federated.0l8h7ne1q4h91z19bvmwz0w7c4q6')
    
    # Data source dependencies
    ds_deps = ET.SubElement(view, 'datasource-dependencies')
    ds_deps.set('datasource', 'federated.0l8h7ne1q4h91z19bvmwz0w7c4q6')
    
    # Add column dependencies based on worksheet type
    if config['type'] == 'text':
        # For KPI cards
        col = ET.SubElement(ds_deps, 'column')
        col.set('caption', 'Count of Countries')
        col.set('datatype', 'integer')
        col.set('name', '[Number of Records]')
        col.set('role', 'measure')
        col.set('type', 'quantitative')
        col.set('user:auto-column', 'numrec')
        
        calc = ET.SubElement(col, 'calculation')
        calc.set('class', 'tableau')
        calc.set('formula', '1')
        
        col_instance = ET.SubElement(ds_deps, 'column-instance')
        col_instance.set('column', '[Number of Records]')
        col_instance.set('derivation', 'Sum')
        col_instance.set('name', '[sum:Number of Records:qk]')
        col_instance.set('pivot', 'key')
        col_instance.set('type', 'quantitative')
    
    elif config['type'] in ['pie', 'bar', 'horizontal_bar']:
        # For single dimension charts
        dim_col = ET.SubElement(ds_deps, 'column')
        dim_col.set('datatype', 'string')
        dim_col.set('name', config['dimension'])
        dim_col.set('role', 'dimension')
        dim_col.set('type', 'nominal')
        
        measure_col = ET.SubElement(ds_deps, 'column')
        measure_col.set('caption', 'Count of Countries')
        measure_col.set('datatype', 'integer')
        measure_col.set('name', '[Number of Records]')
        measure_col.set('role', 'measure')
        measure_col.set('type', 'quantitative')
        measure_col.set('user:auto-column', 'numrec')
        
        calc = ET.SubElement(measure_col, 'calculation')
        calc.set('class', 'tableau')
        calc.set('formula', '1')
        
        # Column instances
        dim_instance = ET.SubElement(ds_deps, 'column-instance')
        dim_instance.set('column', config['dimension'])
        dim_instance.set('derivation', 'None')
        dim_instance.set('name', f'[none:{config["dimension"].replace("[", "").replace("]", "")}:nk]')
        dim_instance.set('pivot', 'key')
        dim_instance.set('type', 'nominal')
        
        measure_instance = ET.SubElement(ds_deps, 'column-instance')
        measure_instance.set('column', '[Number of Records]')
        measure_instance.set('derivation', 'Sum')
        measure_instance.set('name', '[sum:Number of Records:qk]')
        measure_instance.set('pivot', 'key')
        measure_instance.set('type', 'quantitative')
    
    elif config['type'] == 'stacked_bar':
        # For stacked bar charts with two dimensions
        for dim in [config['dimension1'], config['dimension2']]:
            dim_col = ET.SubElement(ds_deps, 'column')
            dim_col.set('datatype', 'string')
            dim_col.set('name', dim)
            dim_col.set('role', 'dimension')
            dim_col.set('type', 'nominal')
            
            dim_instance = ET.SubElement(ds_deps, 'column-instance')
            dim_instance.set('column', dim)
            dim_instance.set('derivation', 'None')
            dim_instance.set('name', f'[none:{dim.replace("[", "").replace("]", "")}:nk]')
            dim_instance.set('pivot', 'key')
            dim_instance.set('type', 'nominal')
        
        measure_col = ET.SubElement(ds_deps, 'column')
        measure_col.set('caption', 'Count of Countries')
        measure_col.set('datatype', 'integer')
        measure_col.set('name', '[Number of Records]')
        measure_col.set('role', 'measure')
        measure_col.set('type', 'quantitative')
        measure_col.set('user:auto-column', 'numrec')
        
        calc = ET.SubElement(measure_col, 'calculation')
        calc.set('class', 'tableau')
        calc.set('formula', '1')
        
        measure_instance = ET.SubElement(ds_deps, 'column-instance')
        measure_instance.set('column', '[Number of Records]')
        measure_instance.set('derivation', 'Sum')
        measure_instance.set('name', '[sum:Number of Records:qk]')
        measure_instance.set('pivot', 'key')
        measure_instance.set('type', 'quantitative')
    
    # Aggregation
    aggregation = ET.SubElement(view, 'aggregation')
    aggregation.set('value', 'true')
    
    # Style
    style = ET.SubElement(table, 'style')
    
    # Panes
    panes = ET.SubElement(table, 'panes')
    pane = ET.SubElement(panes, 'pane')
    pane.set('selection-relaxation-option', 'selection-relaxation-allow')
    
    pane_view = ET.SubElement(pane, 'view')
    breakdown = ET.SubElement(pane_view, 'breakdown')
    breakdown.set('value', 'auto')
    
    # Mark
    mark = ET.SubElement(pane, 'mark')
    if config['type'] == 'text':
        mark.set('class', 'Text')
    elif config['type'] == 'pie':
        mark.set('class', 'Pie')
    else:
        mark.set('class', 'Bar')
    
    # Encodings
    encodings = ET.SubElement(pane, 'encodings')
    
    if config['type'] == 'text':
        text = ET.SubElement(encodings, 'text')
        text.set('column', '[federated.0l8h7ne1q4h91z19bvmwz0w7c4q6].[sum:Number of Records:qk]')
    elif config['type'] == 'pie':
        color = ET.SubElement(encodings, 'color')
        color.set('column', f'[federated.0l8h7ne1q4h91z19bvmwz0w7c4q6].[none:{config["dimension"].replace("[", "").replace("]", "")}:nk]')
        size = ET.SubElement(encodings, 'size')
        size.set('column', '[federated.0l8h7ne1q4h91z19bvmwz0w7c4q6].[sum:Number of Records:qk]')
        text = ET.SubElement(encodings, 'text')
        text.set('column', '[federated.0l8h7ne1q4h91z19bvmwz0w7c4q6].[sum:Number of Records:qk]')
    elif config['type'] in ['bar', 'horizontal_bar']:
        color = ET.SubElement(encodings, 'color')
        color.set('column', f'[federated.0l8h7ne1q4h91z19bvmwz0w7c4q6].[none:{config["dimension"].replace("[", "").replace("]", "")}:nk]')
    elif config['type'] == 'stacked_bar':
        color = ET.SubElement(encodings, 'color')
        color.set('column', f'[federated.0l8h7ne1q4h91z19bvmwz0w7c4q6].[none:{config["dimension2"].replace("[", "").replace("]", "")}:nk]')
    
    # Style for mark
    mark_style = ET.SubElement(pane, 'style')
    style_rule = ET.SubElement(mark_style, 'style-rule')
    style_rule.set('element', 'mark')
    
    format1 = ET.SubElement(style_rule, 'format')
    format1.set('attr', 'mark-labels-show')
    format1.set('value', 'true')
    
    format2 = ET.SubElement(style_rule, 'format')
    format2.set('attr', 'mark-labels-cull')
    format2.set('value', 'true')
    
    if config['type'] == 'text':
        format3 = ET.SubElement(style_rule, 'format')
        format3.set('attr', 'font-size')
        format3.set('value', '24')
        
        format4 = ET.SubElement(style_rule, 'format')
        format4.set('attr', 'font-weight')
        format4.set('value', 'bold')
    
    # Rows and Cols
    rows = ET.SubElement(table, 'rows')
    cols = ET.SubElement(table, 'cols')
    
    if config['type'] in ['bar', 'horizontal_bar']:
        if config['type'] == 'horizontal_bar':
            rows.text = f'[federated.0l8h7ne1q4h91z19bvmwz0w7c4q6].[none:{config["dimension"].replace("[", "").replace("]", "")}:nk]'
            cols.text = '[federated.0l8h7ne1q4h91z19bvmwz0w7c4q6].[sum:Number of Records:qk]'
        else:
            cols.text = f'[federated.0l8h7ne1q4h91z19bvmwz0w7c4q6].[none:{config["dimension"].replace("[", "").replace("]", "")}:nk]'
            rows.text = '[federated.0l8h7ne1q4h91z19bvmwz0w7c4q6].[sum:Number of Records:qk]'
    elif config['type'] == 'stacked_bar':
        rows.text = f'[federated.0l8h7ne1q4h91z19bvmwz0w7c4q6].[none:{config["dimension1"].replace("[", "").replace("]", "")}:nk]'
        cols.text = '[federated.0l8h7ne1q4h91z19bvmwz0w7c4q6].[sum:Number of Records:qk]'
    
    # Simple ID
    simple_id = ET.SubElement(worksheet, 'simple-id')
    simple_id.set('uuid', f'{{{config["uuid"]}}}')
    
    return worksheet

def create_dashboard(worksheet_configs):
    """Create the main dashboard element"""
    dashboard = ET.Element('dashboard')
    dashboard.set('name', 'World Bank Countries Dashboard')
    
    # Style
    style = ET.SubElement(dashboard, 'style')
    
    # Size
    size = ET.SubElement(dashboard, 'size')
    size.set('maxheight', '800')
    size.set('maxwidth', '1200')
    size.set('minheight', '600')
    size.set('minwidth', '800')
    
    # Zones
    zones = ET.SubElement(dashboard, 'zones')
    
    # Title zone
    title_zone = ET.SubElement(zones, 'zone')
    title_zone.set('h', '60')
    title_zone.set('id', '1')
    title_zone.set('type', 'text')
    title_zone.set('w', '1200')
    title_zone.set('x', '0')
    title_zone.set('y', '0')
    
    title_style = ET.SubElement(title_zone, 'zone-style')
    format_attrs = [
        ('border-color', '#000000'),
        ('border-style', 'none'),
        ('border-width', '0'),
        ('margin', '4')
    ]
    for attr, val in format_attrs:
        fmt = ET.SubElement(title_style, 'format')
        fmt.set('attr', attr)
        fmt.set('value', val)
    
    text = ET.SubElement(title_zone, 'text')
    run = ET.SubElement(text, 'run')
    run.set('bold', 'true')
    run.set('fontsize', '18')
    run.text = 'World Bank Countries Dashboard'
    
    # Filter zone
    filter_zone = ET.SubElement(zones, 'zone')
    filter_zone.set('h', '100')
    filter_zone.set('id', '2')
    filter_zone.set('name', 'Filters')
    filter_zone.set('w', '300')
    filter_zone.set('x', '0')
    filter_zone.set('y', '60')
    
    filter_style = ET.SubElement(filter_zone, 'zone-style')
    border_attrs = [
        ('border-color', '#e6e6e6'),
        ('border-style', 'solid'),
        ('border-width', '1'),
        ('margin', '4')
    ]
    for attr, val in border_attrs:
        fmt = ET.SubElement(filter_style, 'format')
        fmt.set('attr', attr)
        fmt.set('value', val)
    
    # KPI zone
    kpi_zone = ET.SubElement(zones, 'zone')
    kpi_zone.set('h', '120')
    kpi_zone.set('id', '3')
    kpi_zone.set('name', 'KPI Cards')
    kpi_zone.set('w', '900')
    kpi_zone.set('x', '300')
    kpi_zone.set('y', '60')
    
    kpi_style = ET.SubElement(kpi_zone, 'zone-style')
    for attr, val in border_attrs:
        fmt = ET.SubElement(kpi_style, 'format')
        fmt.set('attr', attr)
        fmt.set('value', val)
    
    # Chart zones
    chart_configs = [
        {'h': '280', 'id': '4', 'name': 'Income Group Pie Chart', 'w': '400', 'x': '0', 'y': '180'},
        {'h': '280', 'id': '5', 'name': 'Lending Category Bar Chart', 'w': '400', 'x': '400', 'y': '180'},
        {'h': '280', 'id': '6', 'name': 'Countries by Region', 'w': '400', 'x': '800', 'y': '180'},
        {'h': '280', 'id': '7', 'name': 'Income Groups by Region', 'w': '900', 'x': '0', 'y': '460'},
    ]
    
    for config in chart_configs:
        chart_zone = ET.SubElement(zones, 'zone')
        for key, val in config.items():
            chart_zone.set(key, val)
        
        chart_style = ET.SubElement(chart_zone, 'zone-style')
        for attr, val in border_attrs:
            fmt = ET.SubElement(chart_style, 'format')
            fmt.set('attr', attr)
            fmt.set('value', val)
    
    # Notes zone
    notes_zone = ET.SubElement(zones, 'zone')
    notes_zone.set('h', '60')
    notes_zone.set('id', '8')
    notes_zone.set('name', 'Notes')
    notes_zone.set('w', '300')
    notes_zone.set('x', '900')
    notes_zone.set('y', '460')
    
    notes_style = ET.SubElement(notes_zone, 'zone-style')
    for attr, val in border_attrs:
        fmt = ET.SubElement(notes_style, 'format')
        fmt.set('attr', attr)
        fmt.set('value', val)
    
    notes_text = ET.SubElement(notes_zone, 'text')
    notes_run = ET.SubElement(notes_text, 'run')
    notes_run.set('fontsize', '10')
    notes_run.text = 'Data Source: World Bank Country Classifications (CLASS_2025_07_02). Hover over charts for detailed tooltips with additional metadata.'
    
    # Device layouts for responsive design
    device_layouts = ET.SubElement(dashboard, 'devicelayouts')
    phone_layout = ET.SubElement(device_layouts, 'devicelayout')
    phone_layout.set('auto-generated', 'true')
    phone_layout.set('name', 'Phone')
    
    phone_size = ET.SubElement(phone_layout, 'size')
    phone_size.set('maxheight', '700')
    phone_size.set('minheight', '700')
    phone_size.set('sizing-mode', 'vscroll')
    
    phone_zones = ET.SubElement(phone_layout, 'zones')
    
    # Phone responsive zones (stacked vertically)
    phone_zone_configs = [
        {'h': '60', 'id': '1', 'type': 'text', 'w': '350', 'x': '0', 'y': '0'},
        {'h': '100', 'id': '2', 'w': '350', 'x': '0', 'y': '60'},
        {'h': '120', 'id': '3', 'w': '350', 'x': '0', 'y': '160'},
        {'h': '280', 'id': '4', 'w': '350', 'x': '0', 'y': '280'},
        {'h': '280', 'id': '5', 'w': '350', 'x': '0', 'y': '560'},
        {'h': '280', 'id': '6', 'w': '350', 'x': '0', 'y': '840'},
        {'h': '280', 'id': '7', 'w': '350', 'x': '0', 'y': '1120'},
        {'h': '60', 'id': '8', 'w': '350', 'x': '0', 'y': '1400'},
    ]
    
    for config in phone_zone_configs:
        phone_zone = ET.SubElement(phone_zones, 'zone')
        for key, val in config.items():
            phone_zone.set(key, val)
    
    # Simple ID
    simple_id = ET.SubElement(dashboard, 'simple-id')
    simple_id.set('uuid', f'{{{generate_uuid()}}}')
    
    return dashboard

def main():
    """Generate the complete Tableau workbook file"""
    workbook = create_tableau_workbook()
    
    # Convert to string and format
    rough_string = ET.tostring(workbook, 'unicode')
    reparsed = minidom.parseString(rough_string)
    pretty_string = reparsed.toprettyxml(indent="  ")
    
    # Clean up extra whitespace
    lines = [line for line in pretty_string.split('\n') if line.strip()]
    formatted_xml = '\n'.join(lines)
    
    # Write to file
    with open('/home/runner/work/tableau-project-/tableau-project-/World_Bank_Countries_Dashboard.twb', 'w', encoding='utf-8') as f:
        f.write(formatted_xml)
    
    print("Tableau workbook created successfully!")
    print("File: World_Bank_Countries_Dashboard.twb")
    print("This workbook includes:")
    print("- Connection to CLASS_2025_07_02.xlsx")
    print("- KPI cards for key metrics")
    print("- Pie chart for income group distribution") 
    print("- Bar charts for lending categories and regional distribution")
    print("- Stacked bar chart showing income groups by region")
    print("- Interactive dashboard with filters")
    print("- Responsive design for mobile devices")
    print("- Clean Tableau styling with hover tooltips")

if __name__ == "__main__":
    main()