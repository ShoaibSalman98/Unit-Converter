

import streamlit as st  
st.markdown(
        """ <style>
            body{
                background-color: #1e1e2f;
                color:white;
            }
            .stApp{
                background: linear-gradient(135deg, #bcbcbc, #cfe2f3);
                padding: 30px;
                border-radius: 15px;
                box-shadow: 0 10px 30px rgba(0, 0, 0, 0.3);

            }
            h1{
                text-align: center;
                font-size: 36px;
                margin-bottom: 30px;
                text-transform: uppercase;
                letter-spacing: 2px;
                font-weight: bold;
                color: white;
                
            }
            .stButton>button{
                background: linear-gradient(45deg, #0b5394, #351c75);
                color: white;
                border: none;
                font-size: 18px;
                padding: 10px 20px;
                border-radius: 10px;
                cursor: pointer;
                transition: background 0.3s ease;
                box-shadow: 0 5px 15px rgba(0, 201, 255, 0.4);
            }
            .stButton>button:hover {
                background: linear-gradient(45deg, #92fe9d, #cfe2f3);
                transform: scale(1.05);
            }
            .result-box{
                background: rgba(255, 255, 255, 0.1);
                font-size: 24px;
                font-weight: bold;
                text-align: center;
                padding: 25px;
                border-radius: 10px;
                margin-top: 20px;
                box-shadow: 0 5px 15px rgba(0, 201, 210, 0.4);
            }
            .footer{
                text-align: center;
                padding: 20px;
                margin-top: 50px;
                font-size: 14px;
                color: red;
            }
            
            </style>
            """
            , 
            unsafe_allow_html=True)

# Title and description.

st.markdown("<h1>Unit Converter</h1>", unsafe_allow_html=True)
            
st.write("Unit Converter through you can convert your unit to another unit")

# Sidebar Menu.
conversion_type = st.sidebar.selectbox("Select Conversion Type", ["Length", "Weight", "Temperature", "Time", "Volume", "Area", "Speed"])
value = st.number_input("Enter the value to convert", value=0.0, min_value=0.0, step=0.1)
col1, col2 = st.columns(2)

# Conversion Logic.
        
            
def length_conversion(from_unit, to_unit, value):
            length_units = {'Meters': 1, 'Kilometers': 0.001, 'Centimeters': 100, 'Milimeters': 1000, 'Miles': 0.000621371, 'Yards': 1.09361, 'Feet': 3.28084, 'Inches': 39.3701}
            
            return (value / length_units[from_unit]) * length_units[to_unit]    
        
def weight_conversion(from_unit, to_unit, value):
            weight_units = {"Kilograms": 1, "Grams": 0.001, "Miligrams": 1000, "Pounds": 2.20462, "Ounces": 35.274}
            
            return (value / weight_units[from_unit]) * weight_units[to_unit]
        
def temperature_conversion(from_unit, to_unit, value):
            temperature_units = {'Celsius': 1, 'Fahrenheit': 1.8, 'Kelvin': 1}
            
            return (value - temperature_units[from_unit]) * temperature_units[to_unit]
        
def time_conversion(from_unit, to_unit, value):
            time_units = {'Seconds': 1, 'Minutes': 60, 'Hours': 3600, 'Days': 86400, 'Weeks': 604800, 'Months': 2629746, 'Years': 31556952}
            value_in_seconds = value * time_units[from_unit]
            
            return value_in_seconds / time_units[to_unit]
        
def volume_conversion(from_unit, to_unit, value):
            volume_units = {'Liters': 1, 'Mililiters': 1000, 'Cubic Meters': 1, 'Cubic Feet': 35.3147, 'Gallons': 0.264172, 'Quarts': 1.05669, 'Pints': 2.11338, 'Cups': 4.22675, 'Tablespoons': 67.628, 'Teaspoons': 202.884}
            
            return (value / volume_units[from_unit]) * volume_units[to_unit]
        
def area_conversion(from_unit, to_unit, value):
            area_units = {'Square Meters': 1, 'Square Kilometers': 0.000001, 'Square Feet': 10.7639, 'Square Miles': 0.000000386102, 'Acres': 0.000247105, 'Hectares': 0.0001}
            
            return (value / area_units[from_unit]) * area_units[to_unit]
        
def speed_conversion(from_unit, to_unit, value):
            speed_units = {'Meters per second': 1, 'Kilometers per hour': 3.6, 'Miles per hour': 2.23694, 'Feet per second': 3.28, 'Knots': 1.94384}
            
            return (value / speed_units[from_unit]) * speed_units[to_unit]
        

# Conversion Logic.
if conversion_type == "Length":
    with col1:
        from_unit = st.selectbox ("From", ["Meters", "Kilometers", "Centimiters", "Milimeters", "Miles", "Yards", "Feet", "Inches"])
    with col2:
        to_unit = st.selectbox ("To", ["Meters", "Kilometers", "Centimiters", "Milimeters", "Miles", "Yards", "Feet", "Inches"])
        
elif conversion_type == "Weight":
    with col1:
        from_unit = st.selectbox ("From", ["Kilograms", "Grams", "Miligrams", "Pounds", "Ounces"])
    with col2:
        to_unit = st.selectbox ("To", ["Kilograms", "Grams","Miligrams", "Pounds", "Ounces"])
    
elif conversion_type == "Temperature":
    with col1:
        from_unit = st.selectbox ("From", ["Celsius", "Fahrenheit", "Kelvin"])
    with col2:
        to_unit = st.selectbox ("To", ["Celsius", "Fahrenheit", "Kelvin"])
        
elif conversion_type == "Time":
    with col1:
        from_unit = st.selectbox ("From", ["Seconds", "Minutes", "Hours", "Days", "Weeks", "Months", "Years"])
    with col2:
        to_unit = st.selectbox ("To", ["Seconds", "Minutes", "Hours", "Days", "Weeks", "Months", "Years"])
        
elif conversion_type == "Volume":
    with col1:
        from_unit = st.selectbox ("From", ["Liters", "Mililiters", "Cubic Meters", "Cubic Feet", "Gallons", "Quarts", "Pints", "Cups", "Tablespoons", "Teaspoons"])
    with col2:
        to_unit = st.selectbox ("To", ["Liters", "Mililiters", "Cubic Meters", "Cubic Feet", "Gallons", "Quarts", "Pints", "Cups", "Tablespoons", "Teaspoons"])
        
elif conversion_type == "Area":
    with col1:
        from_unit = st.selectbox ("From", ["Square Meters", "Square Kilometers", "Square Feet", "Square Miles", "Acres", "Hectares"])
    with col2:
        to_unit = st.selectbox ("To", ["Square Meters", "Square Kilometers", "Square Feet", "Square Miles", "Acres", "Hectares"])
        
elif conversion_type == "Speed":
    with col1:
        from_unit = st.selectbox ("From", ["Meters per second", "Kilometers per hour", "Miles per hour", "Feet per second", "Knots"])
    with col2:
        to_unit = st.selectbox ("To", ["Meters per second", "Kilometers per hour", "Miles per hour", "Feet per second", "Knots"])
        

    # button to perform the conversion
if st.button("Convert"):
        if conversion_type == "Length":
            result = length_conversion(from_unit, to_unit, value)
        elif conversion_type == "Weight":
            result = weight_conversion(from_unit, to_unit, value)
        elif conversion_type == "Temperature":
            result = temperature_conversion(from_unit, to_unit, value)
        elif conversion_type == "Time":
            result = time_conversion(from_unit, to_unit, value)
        elif conversion_type == "Volume":
            result = volume_conversion(from_unit, to_unit, value)
        elif conversion_type == "Area":
            result = area_conversion(from_unit, to_unit, value)
        elif conversion_type == "Speed":
            result = speed_conversion(from_unit, to_unit, value)
        else:
            result="Conversion type not supported"

            
        
        
        st.markdown(f"<div class='result-box'>{value} {from_unit} = {result:.4f} {to_unit}</div>", unsafe_allow_html=True)
        
        st.markdown("<div class='footer'>Created By Shoaib Salman </div>",  unsafe_allow_html=True )






