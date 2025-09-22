import streamlit as st
import math
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
import pandas as pd
from utils.common import create_tool_header, show_progress_bar, add_to_recent
from utils.file_handler import FileHandler


def display_tools():
    """Display all science and math tools"""

    tool_categories = {
        "Basic Math": [
            "Calculator", "Unit Converter", "Percentage Calculator", "Fraction Calculator", "Ratio Calculator"
        ],
        "Algebra": [
            "Equation Solver", "Quadratic Formula", "System of Equations", "Polynomial Calculator",
            "Logarithm Calculator"
        ],
        "Geometry": [
            "Area Calculator", "Volume Calculator", "Perimeter Calculator", "Triangle Calculator", "Circle Calculator"
        ],
        "Trigonometry": [
            "Trigonometric Functions", "Angle Converter", "Law of Cosines", "Law of Sines", "Unit Circle"
        ],
        "Calculus": [
            "Derivative Calculator", "Integral Calculator", "Limit Calculator", "Series Calculator", "Function Plotter"
        ],
        "Statistics": [
            "Descriptive Statistics", "Probability Calculator", "Distribution Calculator", "Hypothesis Testing",
            "Confidence Intervals"
        ],
        "Physics": [
            "Motion Calculator", "Force Calculator", "Energy Calculator", "Wave Calculator", "Electricity Calculator"
        ],
        "Chemistry": [
            "Molecular Weight", "Chemical Equation Balancer", "pH Calculator", "Concentration Calculator", "Gas Laws"
        ],
        "Engineering": [
            "Ohm's Law Calculator", "Beam Calculator", "Stress Calculator", "Fluid Mechanics", "Heat Transfer"
        ],
        "Number Theory": [
            "Prime Numbers", "GCD/LCM Calculator", "Factorization", "Number Base Converter", "Fibonacci Sequence"
        ]
    }

    selected_category = st.selectbox("Select Science/Math Tool Category", list(tool_categories.keys()))
    selected_tool = st.selectbox("Select Tool", tool_categories[selected_category])

    st.markdown("---")

    add_to_recent(f"Science/Math Tools - {selected_tool}")

    # Display selected tool
    if selected_tool == "Calculator":
        advanced_calculator()
    elif selected_tool == "Unit Converter":
        unit_converter()
    elif selected_tool == "Quadratic Formula":
        quadratic_formula()
    elif selected_tool == "Area Calculator":
        area_calculator()
    elif selected_tool == "Trigonometric Functions":
        trig_functions()
    elif selected_tool == "Function Plotter":
        function_plotter()
    elif selected_tool == "Descriptive Statistics":
        descriptive_statistics()
    elif selected_tool == "Motion Calculator":
        motion_calculator()
    elif selected_tool == "Molecular Weight":
        molecular_weight()
    elif selected_tool == "Prime Numbers":
        prime_numbers()
    elif selected_tool == "Percentage Calculator":
        percentage_calculator()
    elif selected_tool == "Fraction Calculator":
        fraction_calculator()
    elif selected_tool == "Ratio Calculator":
        ratio_calculator()
    elif selected_tool == "Equation Solver":
        equation_solver()
    elif selected_tool == "System of Equations":
        system_of_equations()
    elif selected_tool == "Polynomial Calculator":
        polynomial_calculator()
    elif selected_tool == "Logarithm Calculator":
        logarithm_calculator()
    elif selected_tool == "Hypothesis Testing":
        hypothesis_testing()
    elif selected_tool == "Probability Calculator":
        probability_calculator()
    elif selected_tool == "Distribution Calculator":
        distribution_calculator()
    elif selected_tool == "Confidence Intervals":
        confidence_intervals()
    else:
        st.info(f"{selected_tool} tool is being implemented. Please check back soon!")


def advanced_calculator():
    """Advanced scientific calculator"""
    create_tool_header("Advanced Calculator", "Perform complex mathematical calculations", "🧮")

    # Calculator interface
    st.markdown("### 🧮 Scientific Calculator")

    expression = st.text_input("Enter mathematical expression:", placeholder="2 + 3 * sin(pi/4)")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("**Available Functions:**")
        st.write("Basic: +, -, *, /, **, (), abs()")
        st.write("Trigonometric: sin(), cos(), tan(), asin(), acos(), atan()")
        st.write("Logarithmic: log(), log10(), ln() (natural log)")
        st.write("Other: sqrt(), exp(), factorial(), pi, e")

    with col2:
        st.markdown("**Examples:**")
        st.code("2 + 3 * 4")
        st.code("sin(pi/2)")
        st.code("log(100)")
        st.code("sqrt(16)")
        st.code("2**3")

    if expression and st.button("Calculate"):
        result = calculate_expression(expression)
        if result is not None:
            st.success(f"**Result:** {result}")
        else:
            st.error("Invalid expression. Please check your syntax.")


def calculate_expression(expression):
    """Safely evaluate mathematical expressions"""
    try:
        # Replace common mathematical functions
        expression = expression.replace("ln(", "log(")
        expression = expression.replace("factorial(", "math.factorial(")
        expression = expression.replace("pi", "math.pi")
        expression = expression.replace("e", "math.e")

        # Add math. prefix to functions
        math_functions = ["sin", "cos", "tan", "asin", "acos", "atan", "log", "log10",
                          "sqrt", "exp", "abs", "floor", "ceil"]
        for func in math_functions:
            expression = expression.replace(f"{func}(", f"math.{func}(")

        # Evaluate safely
        allowed_names = {
            "__builtins__": {},
            "math": math,
        }

        result = eval(expression, allowed_names)
        return result
    except:
        return None


def unit_converter():
    """Convert between different units"""
    create_tool_header("Unit Converter", "Convert between various units of measurement", "📏")

    category = st.selectbox("Unit Category:", [
        "Length", "Weight/Mass", "Temperature", "Area", "Volume", "Speed", "Energy", "Pressure"
    ])

    if category == "Length":
        convert_length()
    elif category == "Weight/Mass":
        convert_weight()
    elif category == "Temperature":
        convert_temperature()
    elif category == "Area":
        convert_area()
    elif category == "Volume":
        convert_volume()
    elif category == "Speed":
        convert_speed()
    else:
        st.info(f"{category} conversion coming soon!")


def convert_length():
    """Convert length units"""
    st.markdown("### 📏 Length Conversion")

    value = st.number_input("Enter value:", value=1.0)

    col1, col2 = st.columns(2)
    with col1:
        from_unit = st.selectbox("From:",
                                 ["meters", "kilometers", "centimeters", "millimeters", "inches", "feet", "yards",
                                  "miles"])
    with col2:
        to_unit = st.selectbox("To:", ["meters", "kilometers", "centimeters", "millimeters", "inches", "feet", "yards",
                                       "miles"])

    if st.button("Convert"):
        result = convert_length_units(value, from_unit, to_unit)
        st.success(f"{value} {from_unit} = {result:.6f} {to_unit}")


def convert_length_units(value, from_unit, to_unit):
    """Convert between length units"""
    # Convert to meters first
    to_meters = {
        "meters": 1,
        "kilometers": 1000,
        "centimeters": 0.01,
        "millimeters": 0.001,
        "inches": 0.0254,
        "feet": 0.3048,
        "yards": 0.9144,
        "miles": 1609.344
    }

    meters = value * to_meters[from_unit]
    result = meters / to_meters[to_unit]
    return result


def convert_weight():
    """Convert weight units"""
    st.markdown("### ⚖️ Weight/Mass Conversion")

    value = st.number_input("Enter value:", value=1.0)

    col1, col2 = st.columns(2)
    with col1:
        from_unit = st.selectbox("From:", ["kilograms", "grams", "pounds", "ounces", "tons", "stones"])
    with col2:
        to_unit = st.selectbox("To:", ["kilograms", "grams", "pounds", "ounces", "tons", "stones"])

    if st.button("Convert"):
        result = convert_weight_units(value, from_unit, to_unit)
        st.success(f"{value} {from_unit} = {result:.6f} {to_unit}")


def convert_weight_units(value, from_unit, to_unit):
    """Convert between weight units"""
    # Convert to kilograms first
    to_kg = {
        "kilograms": 1,
        "grams": 0.001,
        "pounds": 0.453592,
        "ounces": 0.0283495,
        "tons": 1000,
        "stones": 6.35029
    }

    kg = value * to_kg[from_unit]
    result = kg / to_kg[to_unit]
    return result


def convert_temperature():
    """Convert temperature units"""
    st.markdown("### 🌡️ Temperature Conversion")

    value = st.number_input("Enter temperature:", value=0.0)

    col1, col2 = st.columns(2)
    with col1:
        from_unit = st.selectbox("From:", ["Celsius", "Fahrenheit", "Kelvin"])
    with col2:
        to_unit = st.selectbox("To:", ["Celsius", "Fahrenheit", "Kelvin"])

    if st.button("Convert"):
        result = convert_temperature_units(value, from_unit, to_unit)
        st.success(f"{value}° {from_unit} = {result:.2f}° {to_unit}")


def convert_temperature_units(value, from_unit, to_unit):
    """Convert between temperature units"""
    # Convert to Celsius first
    if from_unit == "Fahrenheit":
        celsius = (value - 32) * 5 / 9
    elif from_unit == "Kelvin":
        celsius = value - 273.15
    else:  # Celsius
        celsius = value

    # Convert from Celsius to target
    if to_unit == "Fahrenheit":
        return celsius * 9 / 5 + 32
    elif to_unit == "Kelvin":
        return celsius + 273.15
    else:  # Celsius
        return celsius


def convert_area():
    """Convert area units"""
    create_tool_header("Area Converter", "Convert between different area units", "📐")

    st.markdown("### 📐 Area Unit Conversion")

    # Area conversion factors (to square meters)
    area_units = {
        "Square Meters (m²)": 1.0,
        "Square Kilometers (km²)": 1000000.0,
        "Square Centimeters (cm²)": 0.0001,
        "Square Millimeters (mm²)": 0.000001,
        "Square Inches (in²)": 0.00064516,
        "Square Feet (ft²)": 0.092903,
        "Square Yards (yd²)": 0.836127,
        "Square Miles (mi²)": 2589988.11,
        "Acres": 4046.86,
        "Hectares (ha)": 10000.0,
        "Square Rods": 25.2929,
        "Square Chains": 404.686,
        "Barns (nuclear)": 1e-28
    }

    col1, col2, col3 = st.columns(3)

    with col1:
        value = st.number_input("Value to convert:", value=1.0, step=0.1, format="%.6f")

    with col2:
        from_unit = st.selectbox("From unit:", list(area_units.keys()))

    with col3:
        to_unit = st.selectbox("To unit:", list(area_units.keys()))

    if st.button("Convert Area"):
        # Convert to square meters first, then to target unit
        meters_squared = value * area_units[from_unit]
        result = meters_squared / area_units[to_unit]

        st.markdown("### 🎯 Conversion Result")
        st.success(f"**{value:,.6f} {from_unit} = {result:,.6f} {to_unit}**")

        # Show intermediate conversion
        st.info(f"Intermediate: {meters_squared:,.6f} m²")

        # Show conversion factor
        factor = area_units[from_unit] / area_units[to_unit]
        st.info(f"Conversion factor: 1 {from_unit} = {factor:,.6f} {to_unit}")

    # Quick conversion table for common units
    with st.expander("🔍 Quick Reference Table"):
        st.markdown("**Common Area Conversions (1 unit =):**")
        ref_conversions = [
            ("1 m²", "10.764 ft²", "1.196 yd²", "1550 in²"),
            ("1 km²", "100 hectares", "247.1 acres", "0.386 mi²"),
            ("1 hectare", "10,000 m²", "2.471 acres", "107,639 ft²"),
            ("1 acre", "4,047 m²", "43,560 ft²", "4,840 yd²"),
            ("1 ft²", "144 in²", "0.111 yd²", "0.0929 m²"),
            ("1 yd²", "9 ft²", "1,296 in²", "0.836 m²")
        ]

        for conversion in ref_conversions:
            st.markdown(f"- {conversion[0]} = {conversion[1]} = {conversion[2]} = {conversion[3]}")


def convert_volume():
    """Convert volume units"""
    create_tool_header("Volume Converter", "Convert between different volume units", "🧪")

    st.markdown("### 🧪 Volume Unit Conversion")

    # Volume conversion factors (to cubic meters)
    volume_units = {
        "Cubic Meters (m³)": 1.0,
        "Cubic Kilometers (km³)": 1e9,
        "Cubic Centimeters (cm³)": 1e-6,
        "Cubic Millimeters (mm³)": 1e-9,
        "Liters (L)": 0.001,
        "Milliliters (mL)": 1e-6,
        "Cubic Inches (in³)": 1.6387064e-5,
        "Cubic Feet (ft³)": 0.0283168,
        "Cubic Yards (yd³)": 0.764555,
        "US Gallons (gal)": 0.00378541,
        "US Quarts (qt)": 0.000946353,
        "US Pints (pt)": 0.000473176,
        "US Cups": 0.000236588,
        "US Fluid Ounces (fl oz)": 2.95735e-5,
        "US Tablespoons (tbsp)": 1.47868e-5,
        "US Teaspoons (tsp)": 4.92892e-6,
        "Imperial Gallons (UK gal)": 0.00454609,
        "Imperial Quarts (UK qt)": 0.00113652,
        "Imperial Pints (UK pt)": 0.000568261,
        "Imperial Fluid Ounces (UK fl oz)": 2.84131e-5,
        "Barrels (Oil, 42 gal)": 0.158987,
        "Barrels (US, 31.5 gal)": 0.119241
    }

    col1, col2, col3 = st.columns(3)

    with col1:
        value = st.number_input("Value to convert:", value=1.0, step=0.001, format="%.6f", key="volume_value")

    with col2:
        from_unit = st.selectbox("From unit:", list(volume_units.keys()), key="volume_from")

    with col3:
        to_unit = st.selectbox("To unit:", list(volume_units.keys()), key="volume_to")

    if st.button("Convert Volume"):
        # Convert to cubic meters first, then to target unit
        cubic_meters = value * volume_units[from_unit]
        result = cubic_meters / volume_units[to_unit]

        st.markdown("### 🎯 Conversion Result")
        st.success(f"**{value:,.6f} {from_unit} = {result:,.6f} {to_unit}**")

        # Show intermediate conversion
        st.info(f"Intermediate: {cubic_meters:,.9f} m³")

        # Show conversion factor
        factor = volume_units[from_unit] / volume_units[to_unit]
        st.info(f"Conversion factor: 1 {from_unit} = {factor:,.6f} {to_unit}")

        # Additional helpful information
        if "Liters" in to_unit or "mL" in to_unit:
            liters = cubic_meters * 1000
            st.info(f"Also equals: {liters:,.3f} liters")

        if "Gallons" in to_unit:
            us_gallons = cubic_meters / 0.00378541
            st.info(f"Also equals: {us_gallons:,.3f} US gallons")

    # Quick conversion tables
    with st.expander("🔍 Quick Reference Tables"):
        st.markdown("**Metric Volume Conversions:**")
        metric_conversions = [
            ("1 m³", "1,000 L", "1,000,000 mL", "1,000,000 cm³"),
            ("1 L", "1,000 mL", "1,000 cm³", "0.001 m³"),
            ("1 mL", "1 cm³", "0.001 L", "0.000001 m³")
        ]

        for conversion in metric_conversions:
            st.markdown(f"- {conversion[0]} = {conversion[1]} = {conversion[2]} = {conversion[3]}")

        st.markdown("**US Liquid Conversions:**")
        us_conversions = [
            ("1 gallon", "4 quarts", "8 pints", "16 cups"),
            ("1 quart", "2 pints", "4 cups", "32 fl oz"),
            ("1 pint", "2 cups", "16 fl oz", "32 tbsp"),
            ("1 cup", "8 fl oz", "16 tbsp", "48 tsp")
        ]

        for conversion in us_conversions:
            st.markdown(f"- {conversion[0]} = {conversion[1]} = {conversion[2]} = {conversion[3]}")


def convert_speed():
    """Convert speed units"""
    create_tool_header("Speed Converter", "Convert between different speed and velocity units", "🏃")

    st.markdown("### 🏃 Speed Unit Conversion")

    # Speed conversion factors (to meters per second)
    speed_units = {
        "Meters per Second (m/s)": 1.0,
        "Kilometers per Hour (km/h)": 1 / 3.6,
        "Miles per Hour (mph)": 0.44704,
        "Feet per Second (ft/s)": 0.3048,
        "Knots (nautical)": 0.514444,
        "Mach (speed of sound)": 343.0,
        "Speed of Light (c)": 299792458.0,
        "Centimeters per Second (cm/s)": 0.01,
        "Inches per Second (in/s)": 0.0254,
        "Yards per Second (yd/s)": 0.9144,
        "Kilometers per Second (km/s)": 1000.0,
        "Miles per Second (mi/s)": 1609.34,
        "Furlongs per Fortnight": 1.663095e-4
    }

    col1, col2, col3 = st.columns(3)

    with col1:
        value = st.number_input("Value to convert:", value=1.0, step=0.001, format="%.6f", key="speed_value")

    with col2:
        from_unit = st.selectbox("From unit:", list(speed_units.keys()), key="speed_from")

    with col3:
        to_unit = st.selectbox("To unit:", list(speed_units.keys()), key="speed_to")

    if st.button("Convert Speed"):
        # Convert to m/s first, then to target unit
        meters_per_second = value * speed_units[from_unit]
        result = meters_per_second / speed_units[to_unit]

        st.markdown("### 🎯 Conversion Result")
        st.success(f"**{value:,.6f} {from_unit} = {result:,.6f} {to_unit}**")

        # Show intermediate conversion
        st.info(f"Intermediate: {meters_per_second:,.6f} m/s")

        # Show conversion factor
        factor = speed_units[from_unit] / speed_units[to_unit]
        st.info(f"Conversion factor: 1 {from_unit} = {factor:,.6f} {to_unit}")

        # Additional helpful conversions
        col1, col2, col3 = st.columns(3)
        with col1:
            kmh = meters_per_second * 3.6
            st.metric("km/h", f"{kmh:.2f}")
        with col2:
            mph = meters_per_second / 0.44704
            st.metric("mph", f"{mph:.2f}")
        with col3:
            knots = meters_per_second / 0.514444
            st.metric("knots", f"{knots:.2f}")

        # Speed categories for context
        if meters_per_second > 0:
            st.markdown("### 📊 Speed Context")

            speed_categories = [
                ("Walking speed", 1.4, "👶"),
                ("Running speed", 5.0, "🏃"),
                ("Bicycle speed", 8.3, "🚴"),
                ("Car speed (city)", 13.9, "🚗"),
                ("Car speed (highway)", 27.8, "🛣️"),
                ("High-speed train", 83.3, "🚄"),
                ("Commercial aircraft", 250.0, "✈️"),
                ("Speed of sound", 343.0, "💥"),
                ("Escape velocity (Earth)", 11180.0, "🚀")
            ]

            closest_category = None
            min_ratio = float('inf')

            for category, speed, emoji in speed_categories:
                ratio = abs(meters_per_second - speed) / speed
                if ratio < min_ratio:
                    min_ratio = ratio
                    closest_category = (category, speed, emoji)

            if closest_category and min_ratio < 2.0:  # Within 200% of reference speed
                category, ref_speed, emoji = closest_category
                st.info(f"{emoji} **Comparable to:** {category} (~{ref_speed:.1f} m/s)")

    # Quick conversion table
    with st.expander("🔍 Quick Reference Table"):
        st.markdown("**Common Speed Conversions:**")
        common_conversions = [
            ("1 m/s", "3.6 km/h", "2.237 mph", "1.944 knots"),
            ("1 km/h", "0.278 m/s", "0.621 mph", "0.540 knots"),
            ("1 mph", "0.447 m/s", "1.609 km/h", "0.869 knots"),
            ("1 knot", "0.514 m/s", "1.852 km/h", "1.151 mph"),
            ("1 ft/s", "0.305 m/s", "1.097 km/h", "0.682 mph"),
            ("Mach 1", "343 m/s", "1,235 km/h", "767 mph")
        ]

        for conversion in common_conversions:
            st.markdown(f"- {conversion[0]} = {conversion[1]} = {conversion[2]} = {conversion[3]}")

        st.markdown("**Reference Speeds:**")
        st.markdown("- 🚶 Walking: ~5 km/h (1.4 m/s)")
        st.markdown("- 🏃 Running: ~18 km/h (5 m/s)")
        st.markdown("- 🚴 Cycling: ~30 km/h (8.3 m/s)")
        st.markdown("- 🚗 City driving: ~50 km/h (13.9 m/s)")
        st.markdown("- 🛣️ Highway: ~100 km/h (27.8 m/s)")
        st.markdown("- ✈️ Commercial jet: ~900 km/h (250 m/s)")
        st.markdown("- 💥 Sound: 1,235 km/h (343 m/s)")
        st.markdown("- 🌍 Earth escape: ~40,300 km/h (11,180 m/s)")


def quadratic_formula():
    """Solve quadratic equations"""
    create_tool_header("Quadratic Formula", "Solve quadratic equations ax² + bx + c = 0", "📐")

    st.markdown("### Quadratic Equation: ax² + bx + c = 0")

    col1, col2, col3 = st.columns(3)
    with col1:
        a = st.number_input("Coefficient a:", value=1.0)
    with col2:
        b = st.number_input("Coefficient b:", value=0.0)
    with col3:
        c = st.number_input("Coefficient c:", value=0.0)

    if a != 0 and st.button("Solve"):
        discriminant = b ** 2 - 4 * a * c

        st.markdown(f"### Equation: {a}x² + {b}x + {c} = 0")
        st.markdown(f"**Discriminant (Δ):** {discriminant}")

        if discriminant > 0:
            x1 = (-b + math.sqrt(discriminant)) / (2 * a)
            x2 = (-b - math.sqrt(discriminant)) / (2 * a)
            st.success(f"**Two real solutions:**")
            st.write(f"x₁ = {x1:.6f}")
            st.write(f"x₂ = {x2:.6f}")
        elif discriminant == 0:
            x = -b / (2 * a)
            st.success(f"**One real solution:**")
            st.write(f"x = {x:.6f}")
        else:
            real_part = -b / (2 * a)
            imaginary_part = math.sqrt(-discriminant) / (2 * a)
            st.success(f"**Two complex solutions:**")
            st.write(f"x₁ = {real_part:.6f} + {imaginary_part:.6f}i")
            st.write(f"x₂ = {real_part:.6f} - {imaginary_part:.6f}i")
    elif a == 0:
        st.error("Coefficient 'a' cannot be zero for a quadratic equation")


def equation_solver():
    """Solve various types of equations"""
    create_tool_header("Equation Solver", "Solve linear, quadratic, and other equations", "🔍")

    equation_type = st.selectbox("Select equation type:", [
        "Linear Equation (ax + b = 0)",
        "Quadratic Equation (ax² + bx + c = 0)",
        "Cubic Equation (ax³ + bx² + cx + d = 0)",
        "General Polynomial",
        "Exponential Equation",
        "Logarithmic Equation"
    ])

    if equation_type == "Linear Equation (ax + b = 0)":
        st.markdown("### 📏 Linear Equation: ax + b = 0")

        col1, col2 = st.columns(2)
        with col1:
            a = st.number_input("Coefficient a:", value=2.0)
        with col2:
            b = st.number_input("Constant b:", value=5.0)

        if st.button("Solve Linear"):
            if a != 0:
                x = -b / a
                st.success(f"**Solution: x = {x:.6f}**")
                st.info(f"Verification: {a}({x:.6f}) + {b} = {a * x + b:.6f}")
            else:
                if b == 0:
                    st.success("**Solution: Any real number (infinitely many solutions)**")
                else:
                    st.error("**No solution (inconsistent equation)**")

    elif equation_type == "Quadratic Equation (ax² + bx + c = 0)":
        st.markdown("### 📐 Quadratic Equation: ax² + bx + c = 0")
        st.info("Note: This is the same as the dedicated Quadratic Formula tool")

        col1, col2, col3 = st.columns(3)
        with col1:
            a = st.number_input("Coefficient a:", value=1.0, key="quad_a")
        with col2:
            b = st.number_input("Coefficient b:", value=0.0, key="quad_b")
        with col3:
            c = st.number_input("Coefficient c:", value=0.0, key="quad_c")

        if a != 0 and st.button("Solve Quadratic"):
            discriminant = b ** 2 - 4 * a * c

            st.markdown(f"**Discriminant (Δ):** {discriminant}")

            if discriminant > 0:
                x1 = (-b + math.sqrt(discriminant)) / (2 * a)
                x2 = (-b - math.sqrt(discriminant)) / (2 * a)
                st.success(f"**Two real solutions:**")
                st.write(f"x₁ = {x1:.6f}")
                st.write(f"x₂ = {x2:.6f}")
            elif discriminant == 0:
                x = -b / (2 * a)
                st.success(f"**One real solution: x = {x:.6f}**")
            else:
                real_part = -b / (2 * a)
                imaginary_part = math.sqrt(-discriminant) / (2 * a)
                st.success(f"**Two complex solutions:**")
                st.write(f"x₁ = {real_part:.6f} + {imaginary_part:.6f}i")
                st.write(f"x₂ = {real_part:.6f} - {imaginary_part:.6f}i")
        elif a == 0:
            st.error("Coefficient 'a' cannot be zero for a quadratic equation")

    elif equation_type == "Cubic Equation (ax³ + bx² + cx + d = 0)":
        st.markdown("### 🔶 Cubic Equation: ax³ + bx² + cx + d = 0")

        col1, col2, col3, col4 = st.columns(4)
        with col1:
            a = st.number_input("Coefficient a:", value=1.0, key="cubic_a")
        with col2:
            b = st.number_input("Coefficient b:", value=0.0, key="cubic_b")
        with col3:
            c = st.number_input("Coefficient c:", value=0.0, key="cubic_c")
        with col4:
            d = st.number_input("Constant d:", value=0.0, key="cubic_d")

        if a != 0 and st.button("Solve Cubic"):
            st.info("**Solving cubic equations using numerical methods...**")

            # Use numpy to find roots
            try:
                import numpy as np
                coefficients = [a, b, c, d]
                roots = np.roots(coefficients)

                st.success("**Solutions found:**")
                for i, root in enumerate(roots, 1):
                    if np.isreal(root):
                        st.write(f"x₍{i}₎ = {root.real:.6f}")
                    else:
                        st.write(f"x₍{i}₎ = {root.real:.6f} + {root.imag:.6f}i")

            except ImportError:
                st.error("NumPy is required for cubic equation solving")
        elif a == 0:
            st.error("Coefficient 'a' cannot be zero for a cubic equation")

    else:
        st.info(f"Advanced equation solving for {equation_type} is under development.")
        st.write("For complex polynomial equations, consider using dedicated mathematical software.")


def system_of_equations():
    """Solve systems of linear equations"""
    create_tool_header("System of Equations", "Solve systems of linear equations", "🔗")

    system_type = st.selectbox("Select system type:", [
        "2x2 System (2 equations, 2 unknowns)",
        "3x3 System (3 equations, 3 unknowns)",
        "Matrix Input"
    ])

    if system_type == "2x2 System (2 equations, 2 unknowns)":
        st.markdown("### 🔗 2×2 System of Linear Equations")
        st.markdown("**Format:**")
        st.markdown("- Equation 1: a₁x + b₁y = c₁")
        st.markdown("- Equation 2: a₂x + b₂y = c₂")

        st.markdown("**Enter coefficients:**")

        col1, col2, col3 = st.columns(3)
        with col1:
            st.markdown("**Equation 1:**")
            a1 = st.number_input("a₁ (coefficient of x):", value=2.0, key="a1")
            b1 = st.number_input("b₁ (coefficient of y):", value=3.0, key="b1")
            c1 = st.number_input("c₁ (constant):", value=8.0, key="c1")

        with col2:
            st.markdown("**Equation 2:**")
            a2 = st.number_input("a₂ (coefficient of x):", value=1.0, key="a2")
            b2 = st.number_input("b₂ (coefficient of y):", value=-1.0, key="b2")
            c2 = st.number_input("c₂ (constant):", value=1.0, key="c2")

        with col3:
            st.markdown("**System Preview:**")
            st.write(f"{a1}x + {b1}y = {c1}")
            st.write(f"{a2}x + {b2}y = {c2}")

        if st.button("Solve 2x2 System"):
            # Calculate determinant
            det = a1 * b2 - a2 * b1

            if abs(det) > 1e-10:  # Non-zero determinant
                x = (c1 * b2 - c2 * b1) / det
                y = (a1 * c2 - a2 * c1) / det

                st.success("**Unique solution found:**")
                st.write(f"**x = {x:.6f}**")
                st.write(f"**y = {y:.6f}**")

                # Verification
                st.markdown("**Verification:**")
                eq1_check = a1 * x + b1 * y
                eq2_check = a2 * x + b2 * y
                st.info(f"Equation 1: {a1}({x:.6f}) + {b1}({y:.6f}) = {eq1_check:.6f} ≈ {c1}")
                st.info(f"Equation 2: {a2}({x:.6f}) + {b2}({y:.6f}) = {eq2_check:.6f} ≈ {c2}")

            else:
                # Check if system is inconsistent or has infinitely many solutions
                if abs(a1 * c2 - a2 * c1) < 1e-10 and abs(b1 * c2 - b2 * c1) < 1e-10:
                    st.success("**Infinitely many solutions** (dependent equations)")
                else:
                    st.error("**No solution** (inconsistent system)")

    elif system_type == "3x3 System (3 equations, 3 unknowns)":
        st.markdown("### 🔗 3×3 System of Linear Equations")
        st.markdown("**Format:**")
        st.markdown("- Equation 1: a₁x + b₁y + c₁z = d₁")
        st.markdown("- Equation 2: a₂x + b₂y + c₂z = d₂")
        st.markdown("- Equation 3: a₃x + b₃y + c₃z = d₃")

        # Create input fields for 3x3 system
        eq_cols = st.columns(3)

        with eq_cols[0]:
            st.markdown("**Equation 1:**")
            a1 = st.number_input("a₁:", value=2.0, key="3x3_a1")
            b1 = st.number_input("b₁:", value=1.0, key="3x3_b1")
            c1 = st.number_input("c₁:", value=1.0, key="3x3_c1")
            d1 = st.number_input("d₁:", value=8.0, key="3x3_d1")

        with eq_cols[1]:
            st.markdown("**Equation 2:**")
            a2 = st.number_input("a₂:", value=1.0, key="3x3_a2")
            b2 = st.number_input("b₂:", value=2.0, key="3x3_b2")
            c2 = st.number_input("c₂:", value=1.0, key="3x3_c2")
            d2 = st.number_input("d₂:", value=9.0, key="3x3_d2")

        with eq_cols[2]:
            st.markdown("**Equation 3:**")
            a3 = st.number_input("a₃:", value=1.0, key="3x3_a3")
            b3 = st.number_input("b₃:", value=1.0, key="3x3_b3")
            c3 = st.number_input("c₃:", value=2.0, key="3x3_c3")
            d3 = st.number_input("d₃:", value=10.0, key="3x3_d3")

        st.markdown("**System Preview:**")
        st.write(f"{a1}x + {b1}y + {c1}z = {d1}")
        st.write(f"{a2}x + {b2}y + {c2}z = {d2}")
        st.write(f"{a3}x + {b3}y + {c3}z = {d3}")

        if st.button("Solve 3x3 System"):
            try:
                import numpy as np

                # Create coefficient matrix and constants vector
                A = np.array([[a1, b1, c1], [a2, b2, c2], [a3, b3, c3]])
                b = np.array([d1, d2, d3])

                # Calculate determinant
                det = np.linalg.det(A)

                if abs(det) > 1e-10:
                    # Solve using numpy
                    solution = np.linalg.solve(A, b)
                    x, y, z = solution

                    st.success("**Unique solution found:**")
                    st.write(f"**x = {x:.6f}**")
                    st.write(f"**y = {y:.6f}**")
                    st.write(f"**z = {z:.6f}**")

                    # Verification
                    st.markdown("**Verification:**")
                    check = np.dot(A, solution)
                    for i, (computed, expected) in enumerate(zip(check, b), 1):
                        st.info(f"Equation {i}: {computed:.6f} ≈ {expected}")

                else:
                    st.error("**No unique solution** (determinant = 0)")

            except ImportError:
                st.error("NumPy is required for 3x3 system solving")
            except np.linalg.LinAlgError:
                st.error("**Singular matrix** - no unique solution exists")

    else:
        st.info("Matrix input method is under development. Use the structured input methods above.")


def polynomial_calculator():
    """Perform polynomial calculations"""
    create_tool_header("Polynomial Calculator", "Work with polynomials", "🔢")

    operation = st.selectbox("Select operation:", [
        "Evaluate Polynomial",
        "Add Polynomials",
        "Subtract Polynomials",
        "Multiply Polynomials",
        "Find Roots",
        "Derivative",
        "Integral"
    ])

    if operation == "Evaluate Polynomial":
        st.markdown("### 📊 Evaluate Polynomial")
        st.markdown("Enter polynomial coefficients from highest to lowest degree")
        st.markdown("Example: For 2x³ + 3x² - 5x + 1, enter [2, 3, -5, 1]")

        # Input polynomial coefficients
        degree = st.selectbox("Polynomial degree:", list(range(1, 6)), index=2)

        coefficients = []
        cols = st.columns(degree + 1)

        for i in range(degree + 1):
            with cols[i]:
                power = degree - i
                if power == 0:
                    label = "Constant term:"
                elif power == 1:
                    label = "x coefficient:"
                else:
                    label = f"x^{power} coefficient:"

                coeff = st.number_input(label, value=1.0 if i == 0 else 0.0, key=f"poly_coeff_{i}")
                coefficients.append(coeff)

        x_value = st.number_input("Evaluate at x =", value=1.0)

        if st.button("Evaluate"):
            # Create polynomial string
            poly_terms = []
            for i, coeff in enumerate(coefficients):
                power = degree - i
                if coeff != 0:
                    if power == 0:
                        poly_terms.append(f"{coeff}")
                    elif power == 1:
                        poly_terms.append(f"{coeff}x" if coeff != 1 else "x")
                    else:
                        poly_terms.append(f"{coeff}x^{power}" if coeff != 1 else f"x^{power}")

            poly_str = " + ".join(poly_terms).replace("+ -", "- ")

            # Evaluate polynomial
            result = sum(coeff * (x_value ** (degree - i)) for i, coeff in enumerate(coefficients))

            st.success(f"**Polynomial:** P(x) = {poly_str}")
            st.success(f"**P({x_value}) = {result:.6f}**")

    elif operation in ["Add Polynomials", "Subtract Polynomials"]:
        st.markdown(f"### ➕ {operation}")
        st.markdown("Enter coefficients for two polynomials")

        max_degree = st.selectbox("Maximum degree:", list(range(1, 5)), index=2)

        st.markdown("**First Polynomial:**")
        coeffs1 = []
        cols1 = st.columns(max_degree + 1)
        for i in range(max_degree + 1):
            with cols1[i]:
                power = max_degree - i
                coeff = st.number_input(f"x^{power}:" if power > 0 else "Constant:",
                                        value=0.0, key=f"p1_coeff_{i}")
                coeffs1.append(coeff)

        st.markdown("**Second Polynomial:**")
        coeffs2 = []
        cols2 = st.columns(max_degree + 1)
        for i in range(max_degree + 1):
            with cols2[i]:
                power = max_degree - i
                coeff = st.number_input(f"x^{power}:" if power > 0 else "Constant:",
                                        value=0.0, key=f"p2_coeff_{i}")
                coeffs2.append(coeff)

        if st.button(f"{operation.split()[0]}"):
            if operation == "Add Polynomials":
                result_coeffs = [c1 + c2 for c1, c2 in zip(coeffs1, coeffs2)]
                op_symbol = "+"
            else:
                result_coeffs = [c1 - c2 for c1, c2 in zip(coeffs1, coeffs2)]
                op_symbol = "-"

            # Create polynomial strings
            def create_poly_string(coeffs, degree):
                terms = []
                for i, coeff in enumerate(coeffs):
                    power = degree - i
                    if abs(coeff) > 1e-10:  # Non-zero coefficient
                        if power == 0:
                            terms.append(f"{coeff}")
                        elif power == 1:
                            terms.append(f"{coeff}x" if abs(coeff) != 1 else ("x" if coeff > 0 else "-x"))
                        else:
                            terms.append(f"{coeff}x^{power}" if abs(coeff) != 1 else (
                                f"x^{power}" if coeff > 0 else f"-x^{power}"))
                return " + ".join(terms).replace("+ -", "- ") if terms else "0"

            poly1_str = create_poly_string(coeffs1, max_degree)
            poly2_str = create_poly_string(coeffs2, max_degree)
            result_str = create_poly_string(result_coeffs, max_degree)

            st.success(f"**First polynomial:** {poly1_str}")
            st.success(f"**Second polynomial:** {poly2_str}")
            st.success(f"**Result:** ({poly1_str}) {op_symbol} ({poly2_str}) = {result_str}")

    else:
        st.info(f"{operation} is under development.")
        st.write("Coming soon: Advanced polynomial operations including roots finding, derivatives, and integrals.")


def logarithm_calculator():
    """Calculate logarithms and exponentials"""
    create_tool_header("Logarithm Calculator", "Calculate logarithms and exponentials", "📊")

    calc_type = st.selectbox("Select calculation type:", [
        "Natural Logarithm (ln)",
        "Common Logarithm (log₁₀)",
        "Logarithm with Custom Base",
        "Exponential (eˣ)",
        "Power (aˣ)",
        "Logarithmic Properties",
        "Change of Base Formula"
    ])

    if calc_type == "Natural Logarithm (ln)":
        st.markdown("### 🌿 Natural Logarithm (ln)")
        st.markdown("Calculate ln(x) where the base is e ≈ 2.71828")

        x = st.number_input("Enter x (must be positive):", value=10.0, min_value=1e-10)

        if st.button("Calculate ln(x)"):
            if x > 0:
                result = math.log(x)
                st.success(f"**ln({x}) = {result:.6f}**")
                st.info(f"This means: e^{result:.6f} = {x}")

                # Show special values
                if abs(x - 1) < 1e-10:
                    st.info("Special case: ln(1) = 0")
                elif abs(x - math.e) < 1e-3:
                    st.info("Special case: ln(e) = 1")
            else:
                st.error("Natural logarithm is only defined for positive numbers")

    elif calc_type == "Common Logarithm (log₁₀)":
        st.markdown("### 🔟 Common Logarithm (log₁₀)")
        st.markdown("Calculate log₁₀(x) where the base is 10")

        x = st.number_input("Enter x (must be positive):", value=100.0, min_value=1e-10, key="log10_x")

        if st.button("Calculate log₁₀(x)"):
            if x > 0:
                result = math.log10(x)
                st.success(f"**log₁₀({x}) = {result:.6f}**")
                st.info(f"This means: 10^{result:.6f} = {x}")

                # Show special values
                if abs(x - 1) < 1e-10:
                    st.info("Special case: log₁₀(1) = 0")
                elif abs(x - 10) < 1e-10:
                    st.info("Special case: log₁₀(10) = 1")
                elif abs(x - 100) < 1e-10:
                    st.info("Special case: log₁₀(100) = 2")
            else:
                st.error("Common logarithm is only defined for positive numbers")

    elif calc_type == "Logarithm with Custom Base":
        st.markdown("### 🎛️ Logarithm with Custom Base")
        st.markdown("Calculate log_b(x) for any base b")

        col1, col2 = st.columns(2)
        with col1:
            base = st.number_input("Base (b):", value=2.0, min_value=1e-10, key="custom_base")
        with col2:
            x = st.number_input("Value (x):", value=8.0, min_value=1e-10, key="custom_x")

        if st.button("Calculate log_b(x)"):
            if x > 0 and base > 0 and abs(base - 1) > 1e-10:
                result = math.log(x) / math.log(base)
                st.success(f"**log_{base}({x}) = {result:.6f}**")
                st.info(f"This means: {base}^{result:.6f} = {x}")

                # Verification
                verification = base ** result
                st.info(f"Verification: {base}^{result:.6f} = {verification:.6f}")
            else:
                if x <= 0:
                    st.error("Value x must be positive")
                elif base <= 0:
                    st.error("Base must be positive")
                elif abs(base - 1) <= 1e-10:
                    st.error("Base cannot be 1")

    elif calc_type == "Exponential (eˣ)":
        st.markdown("### 🚀 Exponential Function (eˣ)")
        st.markdown("Calculate e^x where e ≈ 2.71828")

        x = st.number_input("Enter exponent x:", value=1.0, key="exp_x")

        if st.button("Calculate eˣ"):
            result = math.exp(x)
            st.success(f"**e^{x} = {result:.6f}**")

            # Show related logarithm
            if result > 0:
                ln_result = math.log(result)
                st.info(f"Related: ln({result:.6f}) = {ln_result:.6f}")

            # Special cases
            if abs(x) < 1e-10:
                st.info("Special case: e⁰ = 1")
            elif abs(x - 1) < 1e-10:
                st.info(f"Special case: e¹ = e ≈ {math.e:.6f}")

    elif calc_type == "Power (aˣ)":
        st.markdown("### ⚡ Power Function (aˣ)")
        st.markdown("Calculate a^x for any base a and exponent x")

        col1, col2 = st.columns(2)
        with col1:
            base = st.number_input("Base (a):", value=2.0, key="power_base")
        with col2:
            exponent = st.number_input("Exponent (x):", value=3.0, key="power_exp")

        if st.button("Calculate aˣ"):
            try:
                if base > 0:
                    result = base ** exponent
                    st.success(f"**{base}^{exponent} = {result:.6f}**")

                    # Show related logarithm if result is positive
                    if result > 0 and base > 1e-10 and abs(base - 1) > 1e-10:
                        log_result = math.log(result) / math.log(base)
                        st.info(f"Related: log_{base}({result:.6f}) = {log_result:.6f}")

                elif base == 0:
                    if exponent > 0:
                        st.success(f"**0^{exponent} = 0**")
                    elif exponent == 0:
                        st.error("0^0 is undefined")
                    else:
                        st.error("0 raised to negative power is undefined")
                else:
                    # Negative base
                    if exponent == int(exponent):  # Integer exponent
                        result = base ** exponent
                        st.success(f"**{base}^{int(exponent)} = {result:.6f}**")
                    else:
                        st.error("Powers of negative numbers with non-integer exponents involve complex numbers")

            except (OverflowError, ValueError) as e:
                st.error(f"Calculation error: {str(e)}")

    elif calc_type == "Logarithmic Properties":
        st.markdown("### 📐 Logarithmic Properties Calculator")
        st.markdown("Demonstrate and calculate using logarithmic properties")

        property_type = st.selectbox("Select property:", [
            "Product Rule: log(ab) = log(a) + log(b)",
            "Quotient Rule: log(a/b) = log(a) - log(b)",
            "Power Rule: log(aⁿ) = n·log(a)",
            "Change of Base: log_b(x) = log(x)/log(b)"
        ])

        if property_type == "Product Rule: log(ab) = log(a) + log(b)":
            st.markdown("**Product Rule Demonstration**")

            col1, col2 = st.columns(2)
            with col1:
                a = st.number_input("Value a:", value=3.0, min_value=1e-10, key="prod_a")
            with col2:
                b = st.number_input("Value b:", value=4.0, min_value=1e-10, key="prod_b")

            if st.button("Demonstrate Product Rule"):
                log_a = math.log10(a)
                log_b = math.log10(b)
                log_ab = math.log10(a * b)
                sum_logs = log_a + log_b

                st.success("**Product Rule Verification:**")
                st.write(f"log₁₀({a}) = {log_a:.6f}")
                st.write(f"log₁₀({b}) = {log_b:.6f}")
                st.write(f"log₁₀({a} × {b}) = log₁₀({a * b}) = {log_ab:.6f}")
                st.write(f"log₁₀({a}) + log₁₀({b}) = {log_a:.6f} + {log_b:.6f} = {sum_logs:.6f}")
                st.info(f"Difference: {abs(log_ab - sum_logs):.10f} (should be ≈ 0)")

        elif property_type == "Quotient Rule: log(a/b) = log(a) - log(b)":
            st.markdown("**Quotient Rule Demonstration**")

            col1, col2 = st.columns(2)
            with col1:
                a = st.number_input("Value a:", value=12.0, min_value=1e-10, key="quot_a")
            with col2:
                b = st.number_input("Value b:", value=3.0, min_value=1e-10, key="quot_b")

            if st.button("Demonstrate Quotient Rule"):
                log_a = math.log10(a)
                log_b = math.log10(b)
                log_ab = math.log10(a / b)
                diff_logs = log_a - log_b

                st.success("**Quotient Rule Verification:**")
                st.write(f"log₁₀({a}) = {log_a:.6f}")
                st.write(f"log₁₀({b}) = {log_b:.6f}")
                st.write(f"log₁₀({a} ÷ {b}) = log₁₀({a / b:.6f}) = {log_ab:.6f}")
                st.write(f"log₁₀({a}) - log₁₀({b}) = {log_a:.6f} - {log_b:.6f} = {diff_logs:.6f}")
                st.info(f"Difference: {abs(log_ab - diff_logs):.10f} (should be ≈ 0)")

        elif property_type == "Power Rule: log(aⁿ) = n·log(a)":
            st.markdown("**Power Rule Demonstration**")

            col1, col2 = st.columns(2)
            with col1:
                a = st.number_input("Base a:", value=2.0, min_value=1e-10, key="pow_a")
            with col2:
                n = st.number_input("Exponent n:", value=3.0, key="pow_n")

            if st.button("Demonstrate Power Rule"):
                log_a = math.log10(a)
                a_to_n = a ** n
                log_an = math.log10(a_to_n)
                n_log_a = n * log_a

                st.success("**Power Rule Verification:**")
                st.write(f"log₁₀({a}) = {log_a:.6f}")
                st.write(f"{a}^{n} = {a_to_n:.6f}")
                st.write(f"log₁₀({a}^{n}) = log₁₀({a_to_n:.6f}) = {log_an:.6f}")
                st.write(f"{n} × log₁₀({a}) = {n} × {log_a:.6f} = {n_log_a:.6f}")
                st.info(f"Difference: {abs(log_an - n_log_a):.10f} (should be ≈ 0)")

    elif calc_type == "Change of Base Formula":
        st.markdown("### 🔄 Change of Base Formula")
        st.markdown("Convert log_b(x) to natural or common logarithms")
        st.markdown("**Formula:** log_b(x) = log(x) / log(b) = ln(x) / ln(b)")

        col1, col2 = st.columns(2)
        with col1:
            base = st.number_input("Original base (b):", value=3.0, min_value=1e-10, key="change_base")
        with col2:
            x = st.number_input("Value (x):", value=27.0, min_value=1e-10, key="change_x")

        new_base = st.selectbox("Convert to:", ["Natural logarithm (ln)", "Common logarithm (log₁₀)"])

        if st.button("Apply Change of Base"):
            if new_base == "Natural logarithm (ln)":
                result = math.log(x) / math.log(base)
                formula_num = math.log(x)
                formula_den = math.log(base)

                st.success(f"**log_{base}({x}) = ln({x}) / ln({base})**")
                st.write(f"= {formula_num:.6f} / {formula_den:.6f}")
                st.write(f"= {result:.6f}")

            else:  # Common logarithm
                result = math.log10(x) / math.log10(base)
                formula_num = math.log10(x)
                formula_den = math.log10(base)

                st.success(f"**log_{base}({x}) = log₁₀({x}) / log₁₀({base})**")
                st.write(f"= {formula_num:.6f} / {formula_den:.6f}")
                st.write(f"= {result:.6f}")

            # Verification
            verification = base ** result
            st.info(f"Verification: {base}^{result:.6f} = {verification:.6f} ≈ {x}")


def area_calculator():
    """Calculate areas of various shapes"""
    create_tool_header("Area Calculator", "Calculate areas of geometric shapes", "📐")

    shape = st.selectbox("Select shape:", [
        "Rectangle", "Square", "Triangle", "Circle", "Parallelogram", "Trapezoid", "Ellipse"
    ])

    if shape == "Rectangle":
        calculate_rectangle_area()
    elif shape == "Square":
        calculate_square_area()
    elif shape == "Triangle":
        calculate_triangle_area()
    elif shape == "Circle":
        calculate_circle_area()
    elif shape == "Parallelogram":
        calculate_parallelogram_area()
    elif shape == "Trapezoid":
        calculate_trapezoid_area()
    elif shape == "Ellipse":
        calculate_ellipse_area()


def calculate_rectangle_area():
    """Calculate rectangle area"""
    st.markdown("### 📐 Rectangle Area")

    col1, col2 = st.columns(2)
    with col1:
        length = st.number_input("Length:", min_value=0.0, value=5.0)
    with col2:
        width = st.number_input("Width:", min_value=0.0, value=3.0)

    if st.button("Calculate Area"):
        area = length * width
        perimeter = 2 * (length + width)
        st.success(f"**Area:** {area} square units")
        st.info(f"**Perimeter:** {perimeter} units")


def calculate_square_area():
    """Calculate square area"""
    st.markdown("### ⬜ Square Area")

    side = st.number_input("Side length:", min_value=0.0, value=4.0)

    if st.button("Calculate Area"):
        area = side ** 2
        perimeter = 4 * side
        diagonal = side * math.sqrt(2)
        st.success(f"**Area:** {area} square units")
        st.info(f"**Perimeter:** {perimeter} units")
        st.info(f"**Diagonal:** {diagonal:.6f} units")


def calculate_triangle_area():
    """Calculate triangle area"""
    st.markdown("### 🔺 Triangle Area")

    method = st.selectbox("Calculation method:", ["Base and Height", "Three Sides (Heron's Formula)"])

    if method == "Base and Height":
        col1, col2 = st.columns(2)
        with col1:
            base = st.number_input("Base:", min_value=0.0, value=6.0)
        with col2:
            height = st.number_input("Height:", min_value=0.0, value=4.0)

        if st.button("Calculate Area"):
            area = 0.5 * base * height
            st.success(f"**Area:** {area} square units")

    else:  # Three Sides
        col1, col2, col3 = st.columns(3)
        with col1:
            a = st.number_input("Side a:", min_value=0.0, value=3.0)
        with col2:
            b = st.number_input("Side b:", min_value=0.0, value=4.0)
        with col3:
            c = st.number_input("Side c:", min_value=0.0, value=5.0)

        if st.button("Calculate Area"):
            # Check if triangle is valid
            if a + b > c and b + c > a and a + c > b:
                s = (a + b + c) / 2  # Semi-perimeter
                area = math.sqrt(s * (s - a) * (s - b) * (s - c))
                st.success(f"**Area:** {area:.6f} square units")
                st.info(f"**Perimeter:** {a + b + c} units")
            else:
                st.error("Invalid triangle! The sum of any two sides must be greater than the third side.")


def calculate_circle_area():
    """Calculate circle area"""
    st.markdown("### ⭕ Circle Area")

    radius = st.number_input("Radius:", min_value=0.0, value=5.0)

    if st.button("Calculate Area"):
        area = math.pi * radius ** 2
        circumference = 2 * math.pi * radius
        diameter = 2 * radius
        st.success(f"**Area:** {area:.6f} square units")
        st.info(f"**Circumference:** {circumference:.6f} units")
        st.info(f"**Diameter:** {diameter} units")


def calculate_parallelogram_area():
    """Calculate parallelogram area"""
    st.markdown("### ▱ Parallelogram Area")

    col1, col2 = st.columns(2)
    with col1:
        base = st.number_input("Base:", min_value=0.0, value=6.0)
    with col2:
        height = st.number_input("Height:", min_value=0.0, value=4.0)

    if st.button("Calculate Area"):
        area = base * height
        st.success(f"**Area:** {area} square units")


def calculate_trapezoid_area():
    """Calculate trapezoid area"""
    st.markdown("### 🔺 Trapezoid Area")

    col1, col2, col3 = st.columns(3)
    with col1:
        base1 = st.number_input("Base 1:", min_value=0.0, value=5.0)
    with col2:
        base2 = st.number_input("Base 2:", min_value=0.0, value=3.0)
    with col3:
        height = st.number_input("Height:", min_value=0.0, value=4.0)

    if st.button("Calculate Area"):
        area = 0.5 * (base1 + base2) * height
        st.success(f"**Area:** {area} square units")


def calculate_ellipse_area():
    """Calculate ellipse area"""
    st.markdown("### ⬭ Ellipse Area")

    col1, col2 = st.columns(2)
    with col1:
        a = st.number_input("Semi-major axis (a):", min_value=0.0, value=5.0)
    with col2:
        b = st.number_input("Semi-minor axis (b):", min_value=0.0, value=3.0)

    if st.button("Calculate Area"):
        area = math.pi * a * b
        st.success(f"**Area:** {area:.6f} square units")


def trig_functions():
    """Calculate trigonometric functions"""
    create_tool_header("Trigonometric Functions", "Calculate sin, cos, tan and their inverses", "📐")

    angle_unit = st.selectbox("Angle unit:", ["Degrees", "Radians"])
    angle = st.number_input("Enter angle:", value=45.0 if angle_unit == "Degrees" else math.pi / 4)

    if st.button("Calculate"):
        if angle_unit == "Degrees":
            rad_angle = math.radians(angle)
        else:
            rad_angle = angle

        try:
            sin_val = math.sin(rad_angle)
            cos_val = math.cos(rad_angle)
            tan_val = math.tan(rad_angle)

            col1, col2, col3 = st.columns(3)

            with col1:
                st.metric("sin", f"{sin_val:.6f}")
                if abs(sin_val) <= 1:
                    asin_val = math.degrees(math.asin(sin_val)) if angle_unit == "Degrees" else math.asin(sin_val)
                    st.metric("arcsin", f"{asin_val:.6f}")

            with col2:
                st.metric("cos", f"{cos_val:.6f}")
                if abs(cos_val) <= 1:
                    acos_val = math.degrees(math.acos(cos_val)) if angle_unit == "Degrees" else math.acos(cos_val)
                    st.metric("arccos", f"{acos_val:.6f}")

            with col3:
                if abs(tan_val) < 1e10:  # Avoid displaying very large numbers
                    st.metric("tan", f"{tan_val:.6f}")
                else:
                    st.metric("tan", "undefined")

                atan_val = math.degrees(math.atan(tan_val)) if angle_unit == "Degrees" else math.atan(tan_val)
                st.metric("arctan", f"{atan_val:.6f}")

        except Exception as e:
            st.error(f"Error in calculation: {str(e)}")


def function_plotter():
    """Plot mathematical functions"""
    create_tool_header("Function Plotter", "Plot mathematical functions", "📈")

    function = st.text_input("Enter function f(x):", value="x**2", placeholder="x**2, sin(x), exp(x)")

    col1, col2 = st.columns(2)
    with col1:
        x_min = st.number_input("X minimum:", value=-10.0)
        x_max = st.number_input("X maximum:", value=10.0)

    with col2:
        num_points = st.slider("Number of points:", 100, 1000, 500)

    if function and st.button("Plot Function"):
        plot_function(function, x_min, x_max, num_points)


def plot_function(function, x_min, x_max, num_points):
    """Plot mathematical function"""
    try:
        x = np.linspace(x_min, x_max, num_points)

        # Replace common functions for numpy
        func_str = function.replace("^", "**")
        func_str = func_str.replace("ln(", "np.log(")
        func_str = func_str.replace("log(", "np.log10(")
        func_str = func_str.replace("sin(", "np.sin(")
        func_str = func_str.replace("cos(", "np.cos(")
        func_str = func_str.replace("tan(", "np.tan(")
        func_str = func_str.replace("exp(", "np.exp(")
        func_str = func_str.replace("sqrt(", "np.sqrt(")
        func_str = func_str.replace("abs(", "np.abs(")
        func_str = func_str.replace("pi", "np.pi")
        func_str = func_str.replace("e", "np.e")

        # Evaluate function
        allowed_names = {
            "x": x,
            "np": np,
            "__builtins__": {},
        }

        y = eval(func_str, allowed_names)

        # Create plot
        fig, ax = plt.subplots(figsize=(10, 6))
        ax.plot(x, y, linewidth=2)
        ax.grid(True, alpha=0.3)
        ax.set_xlabel("x")
        ax.set_ylabel(f"f(x) = {function}")
        ax.set_title(f"Plot of f(x) = {function}")

        # Add axis lines
        ax.axhline(y=0, color='k', linewidth=0.5)
        ax.axvline(x=0, color='k', linewidth=0.5)

        plt.tight_layout()
        st.pyplot(fig)
        plt.close(fig)

    except Exception as e:
        st.error(f"Error plotting function: {str(e)}")
        st.info("Make sure to use valid Python/NumPy syntax. Examples: x**2, np.sin(x), np.exp(x)")


def descriptive_statistics():
    """Calculate descriptive statistics"""
    create_tool_header("Descriptive Statistics", "Calculate statistical measures", "📊")

    data_input_method = st.selectbox("Data input method:", ["Manual Entry", "Upload File"])

    if data_input_method == "Manual Entry":
        data_text = st.text_area("Enter numbers (separated by commas or spaces):",
                                 placeholder="1, 2, 3, 4, 5 or 1 2 3 4 5")

        if data_text and st.button("Calculate Statistics"):
            try:
                # Parse data
                data = []
                for item in data_text.replace(',', ' ').split():
                    try:
                        data.append(float(item))
                    except ValueError:
                        continue

                if data:
                    calculate_stats(data)
                else:
                    st.error("No valid numbers found in input")

            except Exception as e:
                st.error(f"Error parsing data: {str(e)}")

    else:  # Upload File
        uploaded_file = FileHandler.upload_files(['csv', 'txt'], accept_multiple=False)

        if uploaded_file:
            try:
                if uploaded_file[0].name.endswith('.csv'):
                    df = FileHandler.process_csv_file(uploaded_file[0])
                    if df is not None:
                        numeric_cols = df.select_dtypes(include=[np.number]).columns

                        if len(numeric_cols) > 0:
                            selected_col = st.selectbox("Select column:", numeric_cols)
                            if st.button("Calculate Statistics"):
                                data = df[selected_col].dropna().tolist()
                                calculate_stats(data)
                        else:
                            st.error("No numeric columns found in CSV file")
                    else:
                        st.error("Error reading CSV file")
                else:
                    content = FileHandler.process_text_file(uploaded_file[0])
                    if st.button("Calculate Statistics"):
                        data = []
                        for line in content.split('\n'):
                            for item in line.replace(',', ' ').split():
                                try:
                                    data.append(float(item))
                                except ValueError:
                                    continue

                        if data:
                            calculate_stats(data)
                        else:
                            st.error("No valid numbers found in file")

            except Exception as e:
                st.error(f"Error processing file: {str(e)}")


def calculate_stats(data):
    """Calculate and display statistics"""
    if not data:
        st.error("No data provided")
        return

    data = np.array(data)

    # Basic statistics
    st.markdown("### 📊 Descriptive Statistics")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("Count", len(data))
        st.metric("Mean", f"{np.mean(data):.4f}")

    with col2:
        st.metric("Median", f"{np.median(data):.4f}")
        st.metric("Mode", f"{stats.mode(data)[0]:.4f}")

    with col3:
        st.metric("Std Dev", f"{np.std(data, ddof=1):.4f}")
        st.metric("Variance", f"{np.var(data, ddof=1):.4f}")

    with col4:
        st.metric("Min", f"{np.min(data):.4f}")
        st.metric("Max", f"{np.max(data):.4f}")

    # Quartiles
    st.markdown("### 📈 Quartiles")
    q1 = np.percentile(data, 25)
    q2 = np.percentile(data, 50)  # Median
    q3 = np.percentile(data, 75)
    iqr = q3 - q1

    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Q1 (25%)", f"{q1:.4f}")
    with col2:
        st.metric("Q2 (50%)", f"{q2:.4f}")
    with col3:
        st.metric("Q3 (75%)", f"{q3:.4f}")
    with col4:
        st.metric("IQR", f"{iqr:.4f}")

    # Histogram
    st.markdown("### 📊 Data Distribution")
    fig1, ax1 = plt.subplots(figsize=(10, 6))
    ax1.hist(data, bins=min(30, len(data) // 2), alpha=0.7, color='skyblue', edgecolor='black')
    ax1.set_xlabel("Value")
    ax1.set_ylabel("Frequency")
    ax1.set_title("Histogram of Data")
    ax1.grid(True, alpha=0.3)
    st.pyplot(fig1)
    plt.close(fig1)

    # Box plot
    fig2, ax2 = plt.subplots(figsize=(10, 4))
    ax2.boxplot(data, vert=False)
    ax2.set_xlabel("Value")
    ax2.set_title("Box Plot of Data")
    ax2.grid(True, alpha=0.3)
    st.pyplot(fig2)
    plt.close(fig2)


def motion_calculator():
    """Calculate motion physics"""
    create_tool_header("Motion Calculator", "Calculate motion and kinematics", "🚀")

    motion_type = st.selectbox("Motion type:", [
        "Uniform Motion", "Uniformly Accelerated Motion", "Projectile Motion", "Circular Motion"
    ])

    if motion_type == "Uniform Motion":
        calculate_uniform_motion()
    elif motion_type == "Uniformly Accelerated Motion":
        calculate_accelerated_motion()
    elif motion_type == "Projectile Motion":
        calculate_projectile_motion()
    elif motion_type == "Circular Motion":
        calculate_circular_motion()


def calculate_uniform_motion():
    """Calculate uniform motion"""
    st.markdown("### 🚗 Uniform Motion: v = d/t")

    # Input two values, calculate the third
    col1, col2, col3 = st.columns(3)

    with col1:
        distance = st.number_input("Distance (m):", value=0.0, help="Leave as 0 to calculate")
    with col2:
        time = st.number_input("Time (s):", value=0.0, help="Leave as 0 to calculate")
    with col3:
        velocity = st.number_input("Velocity (m/s):", value=0.0, help="Leave as 0 to calculate")

    if st.button("Calculate"):
        # Count non-zero values
        values = [distance, time, velocity]
        non_zero_count = sum(1 for v in values if v != 0)

        if non_zero_count == 2:
            if distance == 0:
                distance = velocity * time
                st.success(f"**Distance:** {distance} m")
            elif time == 0:
                time = distance / velocity if velocity != 0 else 0
                st.success(f"**Time:** {time} s")
            elif velocity == 0:
                velocity = distance / time if time != 0 else 0
                st.success(f"**Velocity:** {velocity} m/s")
        else:
            st.error("Please provide exactly 2 values and leave the third as 0 to calculate")


def calculate_accelerated_motion():
    """Calculate uniformly accelerated motion"""
    st.markdown("### 🏎️ Uniformly Accelerated Motion")

    st.markdown("**Equations:**")
    st.latex(r"v = u + at")
    st.latex(r"s = ut + \frac{1}{2}at^2")
    st.latex(r"v^2 = u^2 + 2as")

    col1, col2 = st.columns(2)

    with col1:
        u = st.number_input("Initial velocity (u) m/s:", value=0.0)
        v = st.number_input("Final velocity (v) m/s:", value=0.0, help="Leave as 0 if unknown")
        a = st.number_input("Acceleration (a) m/s²:", value=0.0, help="Leave as 0 if unknown")

    with col2:
        t = st.number_input("Time (t) s:", value=0.0, help="Leave as 0 if unknown")
        s = st.number_input("Displacement (s) m:", value=0.0, help="Leave as 0 if unknown")

    if st.button("Calculate"):
        # Try different equations based on known values
        if t != 0 and a != 0:
            v_calc = u + a * t
            s_calc = u * t + 0.5 * a * t ** 2
            st.success(f"**Final velocity:** {v_calc} m/s")
            st.success(f"**Displacement:** {s_calc} m")
        elif v != 0 and a != 0:
            t_calc = (v - u) / a if a != 0 else 0
            s_calc = (v ** 2 - u ** 2) / (2 * a) if a != 0 else 0
            st.success(f"**Time:** {t_calc} s")
            st.success(f"**Displacement:** {s_calc} m")
        else:
            st.error("Please provide sufficient known values")


def calculate_projectile_motion():
    """Calculate projectile motion"""
    create_tool_header("Projectile Motion Calculator",
                       "Calculate trajectory, range, height, and time for projectile motion", "🚀")

    st.markdown("### 🎯 Projectile Motion Parameters")

    # Show key equations
    with st.expander("📚 Key Equations"):
        st.markdown("**Horizontal Motion:**")
        st.latex(r"x = v_0 \cos(\theta) \cdot t")
        st.latex(r"v_x = v_0 \cos(\theta)")

        st.markdown("**Vertical Motion:**")
        st.latex(r"y = v_0 \sin(\theta) \cdot t - \frac{1}{2}gt^2")
        st.latex(r"v_y = v_0 \sin(\theta) - gt")

        st.markdown("**Key Results:**")
        st.latex(r"\text{Time of flight: } T = \frac{2v_0 \sin(\theta)}{g}")
        st.latex(r"\text{Maximum range: } R = \frac{v_0^2 \sin(2\theta)}{g}")
        st.latex(r"\text{Maximum height: } H = \frac{v_0^2 \sin^2(\theta)}{2g}")

    # Input parameters
    col1, col2, col3 = st.columns(3)

    with col1:
        v0 = st.number_input("Initial velocity (v₀) m/s:", min_value=0.0, value=20.0, step=0.1)
        angle_deg = st.number_input("Launch angle (degrees):", min_value=0.0, max_value=90.0, value=45.0, step=0.1)
        g = st.number_input("Gravity (g) m/s²:", value=9.81, step=0.01)

    with col2:
        h0 = st.number_input("Initial height (h₀) m:", value=0.0, step=0.1)
        target_x = st.number_input("Target horizontal distance (m):", value=0.0, step=0.1,
                                   help="Optional: Calculate time to reach this distance")
        target_y = st.number_input("Target height (m):", value=0.0, step=0.1,
                                   help="Optional: Calculate time to reach this height")

    with col3:
        calculation_type = st.selectbox("Calculation Type:", [
            "Complete Trajectory", "Time to Target", "Velocity at Time", "Position at Time"
        ])
        specific_time = 1.0  # Default value
        if calculation_type in ["Velocity at Time", "Position at Time"]:
            specific_time = st.number_input("Specific time (s):", min_value=0.0, value=1.0, step=0.1)

    if st.button("Calculate Projectile Motion"):
        import math

        # Convert angle to radians
        angle_rad = math.radians(angle_deg)

        # Calculate velocity components
        vx0 = v0 * math.cos(angle_rad)
        vy0 = v0 * math.sin(angle_rad)

        if calculation_type == "Complete Trajectory":
            # Calculate key trajectory parameters
            time_of_flight = (vy0 + math.sqrt(vy0 ** 2 + 2 * g * h0)) / g
            max_height = h0 + (vy0 ** 2) / (2 * g)
            max_range = vx0 * time_of_flight
            time_to_max_height = vy0 / g

            # Results
            st.markdown("### 📊 Trajectory Results")

            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric("Time of Flight", f"{time_of_flight:.2f} s")
                st.metric("Maximum Height", f"{max_height:.2f} m")
            with col2:
                st.metric("Maximum Range", f"{max_range:.2f} m")
                st.metric("Time to Max Height", f"{time_to_max_height:.2f} s")
            with col3:
                st.metric("Horizontal Velocity", f"{vx0:.2f} m/s")
                st.metric("Initial Vertical Velocity", f"{vy0:.2f} m/s")

            # Generate trajectory data for plotting
            import numpy as np
            t_points = np.linspace(0, time_of_flight, 100)
            x_points = vx0 * t_points
            y_points = h0 + vy0 * t_points - 0.5 * g * t_points ** 2

            # Create trajectory plot
            try:
                import matplotlib.pyplot as plt
                fig, ax = plt.subplots(figsize=(10, 6))
                ax.plot(x_points, y_points, 'b-', linewidth=2, label='Trajectory')
                ax.axhline(y=0, color='k', linestyle='-', alpha=0.3, label='Ground')
                ax.scatter([max_range], [0], color='red', s=100, label='Landing Point', zorder=5)
                ax.scatter([vx0 * time_to_max_height], [max_height], color='green', s=100, label='Maximum Height',
                           zorder=5)

                ax.set_xlabel('Horizontal Distance (m)')
                ax.set_ylabel('Height (m)')
                ax.set_title(f'Projectile Trajectory (v₀={v0} m/s, θ={angle_deg}°)')
                ax.grid(True, alpha=0.3)
                ax.legend()
                ax.set_ylim(bottom=0)

                st.pyplot(fig)
                plt.close(fig)
            except ImportError:
                st.info("Install matplotlib to see trajectory visualization")

        elif calculation_type == "Time to Target":
            if target_x > 0:
                time_to_target_x = target_x / vx0
                y_at_target_x = h0 + vy0 * time_to_target_x - 0.5 * g * time_to_target_x ** 2

                st.success(f"**Time to reach x = {target_x} m:** {time_to_target_x:.2f} s")
                st.success(f"**Height at that distance:** {y_at_target_x:.2f} m")

            if target_y >= h0:
                # Solve quadratic equation: h0 + vy0*t - 0.5*g*t² = target_y
                a = -0.5 * g
                b = vy0
                c = h0 - target_y
                discriminant = b ** 2 - 4 * a * c

                if discriminant >= 0:
                    t1 = (-b + math.sqrt(discriminant)) / (2 * a)
                    t2 = (-b - math.sqrt(discriminant)) / (2 * a)

                    valid_times = [t for t in [t1, t2] if t >= 0]

                    if valid_times:
                        st.success(
                            f"**Time(s) to reach y = {target_y} m:** {', '.join([f'{t:.2f} s' for t in valid_times])}")
                        for t in valid_times:
                            x_at_time = vx0 * t
                            st.info(f"At t = {t:.2f} s: horizontal distance = {x_at_time:.2f} m")
                    else:
                        st.error("Target height not reachable")
                else:
                    st.error("Target height not reachable")

        elif calculation_type == "Velocity at Time":
            if specific_time >= 0:
                vx_t = vx0  # Horizontal velocity remains constant
                vy_t = vy0 - g * specific_time
                v_magnitude = math.sqrt(vx_t ** 2 + vy_t ** 2)
                v_angle = math.degrees(math.atan2(vy_t, vx_t))

                st.markdown(f"### 🏃 Velocity at t = {specific_time} s")
                col1, col2 = st.columns(2)
                with col1:
                    st.metric("Horizontal Velocity", f"{vx_t:.2f} m/s")
                    st.metric("Vertical Velocity", f"{vy_t:.2f} m/s")
                with col2:
                    st.metric("Total Velocity", f"{v_magnitude:.2f} m/s")
                    st.metric("Velocity Angle", f"{v_angle:.1f}°")

        elif calculation_type == "Position at Time":
            if specific_time >= 0:
                x_t = vx0 * specific_time
                y_t = h0 + vy0 * specific_time - 0.5 * g * specific_time ** 2

                st.markdown(f"### 📍 Position at t = {specific_time} s")
                col1, col2 = st.columns(2)
                with col1:
                    st.metric("Horizontal Position", f"{x_t:.2f} m")
                with col2:
                    st.metric("Vertical Position", f"{y_t:.2f} m")

                if y_t < 0:
                    st.warning("⚠️ Projectile has hit the ground before this time!")


def calculate_circular_motion():
    """Calculate circular motion"""
    create_tool_header("Circular Motion Calculator", "Calculate velocity, acceleration, and forces in circular motion",
                       "🌀")

    st.markdown("### ⭕ Circular Motion Parameters")

    # Show key equations
    with st.expander("📚 Key Equations"):
        st.markdown("**Linear and Angular Relationships:**")
        st.latex(r"v = \omega r")
        st.latex(r"\omega = \frac{2\pi}{T} = 2\pi f")

        st.markdown("**Centripetal Acceleration and Force:**")
        st.latex(r"a_c = \frac{v^2}{r} = \omega^2 r")
        st.latex(r"F_c = m a_c = \frac{mv^2}{r} = m\omega^2 r")

        st.markdown("**Where:**")
        st.markdown("- v = linear velocity, ω = angular velocity")
        st.markdown("- r = radius, T = period, f = frequency")
        st.markdown("- aᶜ = centripetal acceleration, Fᶜ = centripetal force")

    # Input parameters
    motion_type = st.selectbox("Motion Type:", [
        "Uniform Circular Motion", "Vertical Circular Motion", "Conical Pendulum", "Banked Curve"
    ])

    if motion_type == "Uniform Circular Motion":
        col1, col2, col3 = st.columns(3)

        with col1:
            st.markdown("**Given Parameters:**")
            input_type = st.selectbox("Calculate from:", [
                "Linear velocity and radius", "Angular velocity and radius",
                "Period and radius", "Frequency and radius"
            ])

        with col2:
            # Initialize all variables with defaults
            v = 10.0
            omega_input = 2.0
            T = 1.0
            f = 1.0

            if "Linear velocity" in input_type:
                v = st.number_input("Linear velocity (v) m/s:", min_value=0.0, value=10.0, step=0.1)
            if "Angular velocity" in input_type:
                omega_input = st.number_input("Angular velocity (ω) rad/s:", min_value=0.0, value=2.0, step=0.1)
            if "Period" in input_type:
                T = st.number_input("Period (T) s:", min_value=0.001, value=1.0, step=0.1)
            if "Frequency" in input_type:
                f = st.number_input("Frequency (f) Hz:", min_value=0.001, value=1.0, step=0.1)

            r = st.number_input("Radius (r) m:", min_value=0.001, value=5.0, step=0.1)

        with col3:
            mass = st.number_input("Mass (m) kg:", min_value=0.001, value=1.0, step=0.1, help="For force calculations")
            include_forces = st.checkbox("Calculate forces", value=True)

        if st.button("Calculate Uniform Circular Motion"):
            import math

            # Initialize variables
            omega = 0.0

            # Calculate missing parameters based on input
            if "Linear velocity" in input_type:
                omega = v / r
                T = 2 * math.pi / omega
                f = 1 / T
            elif "Angular velocity" in input_type:
                omega = omega_input
                v = omega * r
                T = 2 * math.pi / omega
                f = 1 / T
            elif "Period" in input_type:
                omega = 2 * math.pi / T
                v = omega * r
                f = 1 / T
            elif "Frequency" in input_type:
                omega = 2 * math.pi * f
                v = omega * r
                T = 1 / f

            # Calculate accelerations and forces
            ac = v ** 2 / r  # or omega**2 * r
            Fc = 0.0  # Initialize

            if include_forces:
                Fc = mass * ac

            # Display results
            st.markdown("### 📊 Motion Results")

            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric("Linear Velocity", f"{v:.2f} m/s")
                st.metric("Angular Velocity", f"{omega:.3f} rad/s")
            with col2:
                st.metric("Period", f"{T:.3f} s")
                st.metric("Frequency", f"{f:.3f} Hz")
            with col3:
                st.metric("Centripetal Acceleration", f"{ac:.2f} m/s²")
                if include_forces:
                    st.metric("Centripetal Force", f"{Fc:.2f} N")

            # Additional calculations
            st.markdown("### 🔢 Additional Information")
            col1, col2 = st.columns(2)
            with col1:
                circumference = 2 * math.pi * r
                st.info(f"**Circumference:** {circumference:.2f} m")
                st.info(f"**Angular velocity in RPM:** {omega * 60 / (2 * math.pi):.1f} RPM")
            with col2:
                if include_forces:
                    st.info(f"**Weight of object:** {mass * 9.81:.2f} N")
                    st.info(f"**Fc/Weight ratio:** {Fc / (mass * 9.81):.2f}")

    elif motion_type == "Vertical Circular Motion":
        st.markdown("### 🎡 Vertical Circular Motion")
        col1, col2 = st.columns(2)

        with col1:
            r_vert = st.number_input("Radius (r) m:", min_value=0.001, value=2.0, step=0.1, key="vert_r")
            v_vert = st.number_input("Speed (v) m/s:", min_value=0.0, value=5.0, step=0.1, key="vert_v")
            mass_vert = st.number_input("Mass (m) kg:", min_value=0.001, value=1.0, step=0.1, key="vert_m")

        with col2:
            g = st.number_input("Gravity (g) m/s²:", value=9.81, step=0.01, key="vert_g")
            position = st.selectbox("Calculate forces at:", ["Top of circle", "Bottom of circle", "Side of circle"])

        if st.button("Calculate Vertical Circular Motion"):
            import math

            # Minimum speed for complete loop
            v_min_top = math.sqrt(g * r_vert)

            # Centripetal acceleration
            ac_vert = v_vert ** 2 / r_vert

            # Forces at different positions
            if position == "Top of circle":
                # At top: Fc = mg + N (both point toward center)
                N_top = mass_vert * ac_vert - mass_vert * g
                st.markdown("### 🔝 Forces at Top of Circle")
                col1, col2 = st.columns(2)
                with col1:
                    st.metric("Normal Force", f"{N_top:.2f} N")
                    st.metric("Weight", f"{mass_vert * g:.2f} N")
                with col2:
                    st.metric("Centripetal Force", f"{mass_vert * ac_vert:.2f} N")
                    st.metric("Minimum Speed for Loop", f"{v_min_top:.2f} m/s")

                if N_top < 0:
                    st.error(f"⚠️ Speed too low! Object will fall. Minimum speed: {v_min_top:.2f} m/s")
                else:
                    st.success("✅ Object maintains contact with track")

            elif position == "Bottom of circle":
                # At bottom: Fc = N - mg (N points up, mg points down)
                N_bottom = mass_vert * ac_vert + mass_vert * g
                st.markdown("### 🔽 Forces at Bottom of Circle")
                col1, col2 = st.columns(2)
                with col1:
                    st.metric("Normal Force", f"{N_bottom:.2f} N")
                    st.metric("Weight", f"{mass_vert * g:.2f} N")
                with col2:
                    st.metric("Centripetal Force", f"{mass_vert * ac_vert:.2f} N")
                    st.metric("Apparent Weight", f"{N_bottom:.2f} N")

                g_force = N_bottom / (mass_vert * g)
                st.info(f"**G-force experienced:** {g_force:.2f} g")

            elif position == "Side of circle":
                # At side: Fc = N (horizontal), weight is separate
                N_side = mass_vert * ac_vert
                st.markdown("### ↔️ Forces at Side of Circle")
                col1, col2 = st.columns(2)
                with col1:
                    st.metric("Normal Force (horizontal)", f"{N_side:.2f} N")
                    st.metric("Weight (vertical)", f"{mass_vert * g:.2f} N")
                with col2:
                    st.metric("Centripetal Force", f"{mass_vert * ac_vert:.2f} N")
                    resultant = math.sqrt(N_side ** 2 + (mass_vert * g) ** 2)
                    st.metric("Resultant Force", f"{resultant:.2f} N")

    elif motion_type == "Conical Pendulum":
        st.markdown("### 🎪 Conical Pendulum")
        col1, col2 = st.columns(2)

        with col1:
            L = st.number_input("String length (L) m:", min_value=0.001, value=1.0, step=0.1)
            theta_deg = st.number_input("Angle with vertical (θ) degrees:", min_value=0.1, max_value=89.9, value=30.0,
                                        step=0.1)
            mass_pendulum = st.number_input("Mass (m) kg:", min_value=0.001, value=0.5, step=0.1, key="pendulum_m")

        with col2:
            g_pendulum = st.number_input("Gravity (g) m/s²:", value=9.81, step=0.01, key="pendulum_g")

        if st.button("Calculate Conical Pendulum"):
            import math

            theta_rad = math.radians(theta_deg)
            r_pendulum = L * math.sin(theta_rad)
            h = L * math.cos(theta_rad)  # Height below pivot

            # Period and angular velocity
            T_pendulum = 2 * math.pi * math.sqrt(h / g_pendulum)
            omega_pendulum = 2 * math.pi / T_pendulum
            v_pendulum = omega_pendulum * r_pendulum

            # Forces
            tension = mass_pendulum * g_pendulum / math.cos(theta_rad)
            centripetal_force = tension * math.sin(theta_rad)

            st.markdown("### 📊 Conical Pendulum Results")

            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric("Radius of circle", f"{r_pendulum:.3f} m")
                st.metric("Height below pivot", f"{h:.3f} m")
            with col2:
                st.metric("Period", f"{T_pendulum:.3f} s")
                st.metric("Linear speed", f"{v_pendulum:.3f} m/s")
            with col3:
                st.metric("String tension", f"{tension:.2f} N")
                st.metric("Centripetal force", f"{centripetal_force:.2f} N")

    elif motion_type == "Banked Curve":
        st.markdown("### 🛣️ Banked Curve")
        col1, col2 = st.columns(2)

        with col1:
            r_bank = st.number_input("Radius of curve (r) m:", min_value=0.001, value=50.0, step=1.0)
            bank_angle_deg = st.number_input("Banking angle (θ) degrees:", min_value=0.0, max_value=45.0, value=15.0,
                                             step=0.1)
            mu = st.number_input("Coefficient of friction (μ):", min_value=0.0, max_value=2.0, value=0.3, step=0.01)

        with col2:
            mass_car = st.number_input("Mass of vehicle (m) kg:", min_value=1.0, value=1500.0, step=10.0)
            g_bank = st.number_input("Gravity (g) m/s²:", value=9.81, step=0.01, key="bank_g")

        if st.button("Calculate Banked Curve"):
            import math

            bank_angle_rad = math.radians(bank_angle_deg)

            # Speed for no friction needed
            v_no_friction = math.sqrt(g_bank * r_bank * math.tan(bank_angle_rad))

            # Maximum safe speeds
            numerator_max = g_bank * r_bank * (math.sin(bank_angle_rad) + mu * math.cos(bank_angle_rad))
            denominator_max = math.cos(bank_angle_rad) - mu * math.sin(bank_angle_rad)

            numerator_min = g_bank * r_bank * (math.sin(bank_angle_rad) - mu * math.cos(bank_angle_rad))
            denominator_min = math.cos(bank_angle_rad) + mu * math.sin(bank_angle_rad)

            if denominator_max > 0:
                v_max = math.sqrt(numerator_max / denominator_max)
            else:
                v_max = float('inf')

            if denominator_min > 0 and numerator_min > 0:
                v_min = math.sqrt(numerator_min / denominator_min)
            else:
                v_min = 0

            st.markdown("### 📊 Banked Curve Results")

            col1, col2 = st.columns(2)
            with col1:
                st.metric("Speed (no friction needed)", f"{v_no_friction:.1f} m/s ({v_no_friction * 3.6:.1f} km/h)")
                st.metric("Minimum safe speed", f"{v_min:.1f} m/s ({v_min * 3.6:.1f} km/h)")
            with col2:
                if v_max != float('inf'):
                    st.metric("Maximum safe speed", f"{v_max:.1f} m/s ({v_max * 3.6:.1f} km/h)")
                else:
                    st.metric("Maximum safe speed", "No limit")

                st.info(f"**Banking angle:** {bank_angle_deg}°")
                st.info(f"**Friction coefficient:** {mu}")


def molecular_weight():
    """Calculate molecular weight"""
    create_tool_header("Molecular Weight Calculator", "Calculate molecular weight of compounds", "⚛️")

    # Common atomic weights
    atomic_weights = {
        'H': 1.008, 'He': 4.003, 'Li': 6.941, 'Be': 9.012, 'B': 10.811,
        'C': 12.011, 'N': 14.007, 'O': 15.999, 'F': 18.998, 'Ne': 20.180,
        'Na': 22.990, 'Mg': 24.305, 'Al': 26.982, 'Si': 28.086, 'P': 30.974,
        'S': 32.065, 'Cl': 35.453, 'Ar': 39.948, 'K': 39.098, 'Ca': 40.078,
        'Fe': 55.845, 'Cu': 63.546, 'Zn': 65.380, 'Br': 79.904, 'I': 126.905
    }

    st.markdown("### ⚛️ Enter Chemical Formula")
    formula = st.text_input("Chemical formula:", placeholder="H2O, NaCl, C6H12O6", value="H2O")

    if formula and st.button("Calculate Molecular Weight"):
        mol_weight = calculate_molecular_weight(formula, atomic_weights)
        if mol_weight:
            st.success(f"**Molecular weight of {formula}:** {mol_weight:.3f} g/mol")
        else:
            st.error("Invalid chemical formula or unknown elements")

    # Show available elements
    with st.expander("Available Elements"):
        cols = st.columns(5)
        elements = list(atomic_weights.keys())
        for i, element in enumerate(elements):
            with cols[i % 5]:
                st.write(f"**{element}:** {atomic_weights[element]}")


def calculate_molecular_weight(formula, atomic_weights):
    """Calculate molecular weight from chemical formula"""
    import re

    try:
        # Find all element-number pairs
        pattern = r'([A-Z][a-z]?)(\d*)'
        matches = re.findall(pattern, formula)

        total_weight = 0

        for element, count in matches:
            if element in atomic_weights:
                count = int(count) if count else 1
                total_weight += atomic_weights[element] * count
            else:
                return None  # Unknown element

        return total_weight
    except:
        return None


def prime_numbers():
    """Generate and check prime numbers"""
    create_tool_header("Prime Numbers", "Generate and check prime numbers", "🔢")

    option = st.selectbox("Choose option:", [
        "Check if number is prime",
        "Generate prime numbers up to N",
        "Find prime factors"
    ])

    if option == "Check if number is prime":
        number = st.number_input("Enter number:", min_value=2, value=17, step=1)

        if st.button("Check Prime"):
            if is_prime(int(number)):
                st.success(f"✅ {int(number)} is a prime number!")
            else:
                st.error(f"❌ {int(number)} is not a prime number")

    elif option == "Generate prime numbers up to N":
        n = st.number_input("Generate primes up to:", min_value=2, value=100, step=1)

        if st.button("Generate Primes"):
            primes = generate_primes(int(n))
            st.success(f"Found {len(primes)} prime numbers up to {int(n)}")

            # Display primes in columns
            cols = st.columns(5)
            for i, prime in enumerate(primes):
                with cols[i % 5]:
                    st.write(prime)

    elif option == "Find prime factors":
        number = st.number_input("Enter number to factor:", min_value=2, value=60, step=1)

        if st.button("Find Prime Factors"):
            factors = prime_factors(int(number))
            st.success(f"Prime factors of {int(number)}: {factors}")

            # Show factorization
            factor_str = " × ".join(map(str, factors))
            st.write(f"**Factorization:** {int(number)} = {factor_str}")


def is_prime(n):
    """Check if a number is prime"""
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True


def generate_primes(n):
    """Generate all prime numbers up to n using Sieve of Eratosthenes"""
    if n < 2:
        return []

    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False

    for i in range(2, int(math.sqrt(n)) + 1):
        if sieve[i]:
            for j in range(i * i, n + 1, i):
                sieve[j] = False

    return [i for i in range(2, n + 1) if sieve[i]]


def prime_factors(n):
    """Find prime factors of a number"""
    factors = []
    d = 2

    while d * d <= n:
        while n % d == 0:
            factors.append(d)
            n //= d
        d += 1

    if n > 1:
        factors.append(n)

    return factors


def percentage_calculator():
    """Calculate percentages and percentage operations"""
    create_tool_header("Percentage Calculator", "Calculate percentages, increases, decreases, and more", "📊")

    calculation_type = st.selectbox("Calculation type:", [
        "Basic Percentage", "Percentage Increase/Decrease", "Percentage of a Number",
        "What Percent is X of Y", "Percentage Change", "Percentage Point Difference"
    ])

    if calculation_type == "Basic Percentage":
        st.markdown("### 📊 Basic Percentage: Part/Whole × 100")

        col1, col2 = st.columns(2)
        with col1:
            part = st.number_input("Part (numerator):", value=25.0)
        with col2:
            whole = st.number_input("Whole (denominator):", value=100.0)

        if st.button("Calculate Percentage") and whole != 0:
            percentage = (part / whole) * 100
            st.success(f"**{part} is {percentage:.2f}% of {whole}**")

            # Additional info
            st.info(f"Formula: ({part} ÷ {whole}) × 100 = {percentage:.2f}%")
            if percentage > 100:
                st.warning(f"Result is greater than 100% (part is larger than whole)")

    elif calculation_type == "Percentage Increase/Decrease":
        st.markdown("### 📈 Percentage Increase/Decrease")

        col1, col2 = st.columns(2)
        with col1:
            original = st.number_input("Original value:", value=100.0)
        with col2:
            new_value = st.number_input("New value:", value=120.0)

        if st.button("Calculate Change") and original != 0:
            change = new_value - original
            percentage_change = (change / original) * 100

            if percentage_change > 0:
                st.success(f"**Increase of {percentage_change:.2f}%**")
                st.write(f"Value increased from {original} to {new_value}")
                st.write(f"Absolute increase: {change}")
            elif percentage_change < 0:
                st.success(f"**Decrease of {abs(percentage_change):.2f}%**")
                st.write(f"Value decreased from {original} to {new_value}")
                st.write(f"Absolute decrease: {abs(change)}")
            else:
                st.info("**No change (0%)**")

            st.info(f"Formula: (({new_value} - {original}) ÷ {original}) × 100 = {percentage_change:.2f}%")

    elif calculation_type == "Percentage of a Number":
        st.markdown("### 🔢 Find X% of a Number")

        col1, col2 = st.columns(2)
        with col1:
            percentage = st.number_input("Percentage (%):", value=25.0)
        with col2:
            number = st.number_input("Number:", value=200.0)

        if st.button("Calculate Result"):
            result = (percentage / 100) * number
            st.success(f"**{percentage}% of {number} = {result}**")
            st.info(f"Formula: ({percentage} ÷ 100) × {number} = {result}")

    elif calculation_type == "What Percent is X of Y":
        st.markdown("### ❓ What Percent is X of Y?")

        col1, col2 = st.columns(2)
        with col1:
            x = st.number_input("X (part):", value=50.0)
        with col2:
            y = st.number_input("Y (whole):", value=200.0)

        if st.button("Calculate Percentage") and y != 0:
            percentage = (x / y) * 100
            st.success(f"**{x} is {percentage:.2f}% of {y}**")
            st.info(f"Formula: ({x} ÷ {y}) × 100 = {percentage:.2f}%")

    elif calculation_type == "Percentage Change":
        st.markdown("### 🔄 Percentage Change Between Values")

        col1, col2 = st.columns(2)
        with col1:
            value1 = st.number_input("Value 1:", value=80.0)
        with col2:
            value2 = st.number_input("Value 2:", value=100.0)

        if st.button("Calculate Change") and value1 != 0:
            change = abs(value2 - value1)
            percentage_change = (change / value1) * 100

            direction = "increase" if value2 > value1 else "decrease" if value2 < value1 else "no change"

            st.success(f"**{percentage_change:.2f}% {direction}**")
            st.write(f"From {value1} to {value2}")
            st.write(f"Absolute change: {change}")
            st.info(f"Formula: |{value2} - {value1}| ÷ {value1} × 100 = {percentage_change:.2f}%")

    elif calculation_type == "Percentage Point Difference":
        st.markdown("### 📏 Percentage Point Difference")
        st.write("*Difference between two percentages (not percentage change)*")

        col1, col2 = st.columns(2)
        with col1:
            percent1 = st.number_input("First percentage (%):", value=65.0)
        with col2:
            percent2 = st.number_input("Second percentage (%):", value=75.0)

        if st.button("Calculate Point Difference"):
            point_difference = abs(percent2 - percent1)
            st.success(f"**{point_difference:.1f} percentage points difference**")
            st.write(f"From {percent1}% to {percent2}%")
            st.info(f"Formula: |{percent2}% - {percent1}%| = {point_difference:.1f} percentage points")

            # Show comparison with percentage change
            if percent1 != 0:
                percentage_change = ((percent2 - percent1) / percent1) * 100
                st.warning(f"Note: This is different from percentage change ({percentage_change:.1f}%)")


def fraction_calculator():
    """Calculate fraction operations"""
    from fractions import Fraction
    create_tool_header("Fraction Calculator", "Perform operations with fractions", "🍰")

    operation_type = st.selectbox("Operation type:", [
        "Add Fractions", "Subtract Fractions", "Multiply Fractions", "Divide Fractions",
        "Simplify Fraction", "Convert to Decimal", "Convert to Percentage", "Mixed Number Operations"
    ])

    if operation_type in ["Add Fractions", "Subtract Fractions", "Multiply Fractions", "Divide Fractions"]:
        st.markdown(f"### 🧮 {operation_type}")

        col1, col2 = st.columns(2)

        with col1:
            st.markdown("**First Fraction:**")
            num1 = st.number_input("Numerator 1:", value=1, step=1, key="num1")
            den1 = st.number_input("Denominator 1:", value=2, step=1, key="den1")

        with col2:
            st.markdown("**Second Fraction:**")
            num2 = st.number_input("Numerator 2:", value=1, step=1, key="num2")
            den2 = st.number_input("Denominator 2:", value=3, step=1, key="den2")

        if st.button(f"{operation_type.split()[0]}") and den1 != 0 and den2 != 0:
            frac1 = Fraction(int(num1), int(den1))
            frac2 = Fraction(int(num2), int(den2))

            # Initialize variables
            result = None
            operation_symbol = ""

            if operation_type == "Add Fractions":
                result = frac1 + frac2
                operation_symbol = "+"
            elif operation_type == "Subtract Fractions":
                result = frac1 - frac2
                operation_symbol = "-"
            elif operation_type == "Multiply Fractions":
                result = frac1 * frac2
                operation_symbol = "×"
            elif operation_type == "Divide Fractions":
                if frac2 != 0:
                    result = frac1 / frac2
                    operation_symbol = "÷"
                else:
                    st.error("Cannot divide by zero!")
                    return

            # Only proceed if we have a valid result
            if result is not None and operation_symbol:
                st.success(f"**{frac1} {operation_symbol} {frac2} = {result}**")

                # Show decimal equivalent
                decimal_result = float(result)
                st.info(f"Decimal equivalent: {decimal_result:.6f}")

                # Show percentage if meaningful
                percentage = decimal_result * 100
                st.info(f"As percentage: {percentage:.2f}%")

                # Show step-by-step for addition/subtraction
                if operation_type in ["Add Fractions", "Subtract Fractions"]:
                    lcm_den = abs(den1 * den2) // math.gcd(int(abs(den1)), int(abs(den2)))
                    equiv_num1 = int(num1 * lcm_den / den1)
                    equiv_num2 = int(num2 * lcm_den / den2)

                    st.markdown("**Step-by-step:**")
                    st.write(f"1. Find common denominator: {lcm_den}")
                    st.write(f"2. Convert fractions: {equiv_num1}/{lcm_den} {operation_symbol} {equiv_num2}/{lcm_den}")
                    if operation_type == "Add Fractions":
                        final_num = equiv_num1 + equiv_num2
                    else:
                        final_num = equiv_num1 - equiv_num2
                    st.write(f"3. Calculate: {final_num}/{lcm_den}")
                    st.write(f"4. Simplify: {result}")

    elif operation_type == "Simplify Fraction":
        st.markdown("### ✨ Simplify Fraction")

        col1, col2 = st.columns(2)
        with col1:
            numerator = st.number_input("Numerator:", value=12, step=1)
        with col2:
            denominator = st.number_input("Denominator:", value=18, step=1)

        if st.button("Simplify") and denominator != 0:
            original = Fraction(int(numerator), int(denominator))
            gcd_value = math.gcd(int(abs(numerator)), int(abs(denominator)))

            st.success(f"**{int(numerator)}/{int(denominator)} = {original}**")

            if gcd_value > 1:
                st.info(f"Greatest Common Divisor (GCD): {gcd_value}")
                st.info(f"Simplified by dividing both by {gcd_value}")
            else:
                st.info("Fraction is already in simplest form")

            # Show decimal and percentage
            decimal_value = float(original)
            st.info(f"Decimal: {decimal_value:.6f}")
            st.info(f"Percentage: {decimal_value * 100:.2f}%")

    elif operation_type == "Convert to Decimal":
        st.markdown("### 🔢 Convert Fraction to Decimal")

        col1, col2 = st.columns(2)
        with col1:
            numerator = st.number_input("Numerator:", value=3, step=1, key="conv_num")
        with col2:
            denominator = st.number_input("Denominator:", value=8, step=1, key="conv_den")

        if st.button("Convert to Decimal") and denominator != 0:
            fraction = Fraction(int(numerator), int(denominator))
            decimal_value = float(fraction)

            st.success(f"**{fraction} = {decimal_value}**")

            # Check if it's a repeating decimal
            if len(str(decimal_value)) > 10:
                st.info(f"Rounded decimal: {decimal_value:.10f}")

            # Show as percentage too
            percentage = decimal_value * 100
            st.info(f"As percentage: {percentage:.2f}%")

    elif operation_type == "Convert to Percentage":
        st.markdown("### 📊 Convert Fraction to Percentage")

        col1, col2 = st.columns(2)
        with col1:
            numerator = st.number_input("Numerator:", value=3, step=1, key="perc_num")
        with col2:
            denominator = st.number_input("Denominator:", value=4, step=1, key="perc_den")

        if st.button("Convert to Percentage") and denominator != 0:
            fraction = Fraction(int(numerator), int(denominator))
            decimal_value = float(fraction)
            percentage = decimal_value * 100

            st.success(f"**{fraction} = {percentage:.2f}%**")
            st.info(f"Calculation: ({numerator} ÷ {denominator}) × 100 = {percentage:.2f}%")
            st.info(f"Decimal equivalent: {decimal_value:.6f}")

    elif operation_type == "Mixed Number Operations":
        st.markdown("### 🔄 Mixed Number Operations")

        col1, col2 = st.columns(2)

        with col1:
            st.markdown("**Convert Mixed Number to Improper Fraction:**")
            whole = st.number_input("Whole number:", value=2, step=1)
            num_mixed = st.number_input("Numerator:", value=3, step=1, key="mixed_num")
            den_mixed = st.number_input("Denominator:", value=4, step=1, key="mixed_den")

            if st.button("Convert to Improper") and den_mixed != 0:
                improper_num = int(whole * den_mixed + num_mixed)
                improper_fraction = Fraction(improper_num, int(den_mixed))

                st.success(f"**{int(whole)} {int(num_mixed)}/{int(den_mixed)} = {improper_fraction}**")
                st.info(f"Calculation: ({int(whole)} × {int(den_mixed)} + {int(num_mixed)}) / {int(den_mixed)}")
                st.info(
                    f"= ({int(whole * den_mixed)} + {int(num_mixed)}) / {int(den_mixed)} = {improper_num}/{int(den_mixed)}")

        with col2:
            st.markdown("**Convert Improper Fraction to Mixed Number:**")
            imp_num = st.number_input("Improper numerator:", value=11, step=1, key="imp_num")
            imp_den = st.number_input("Denominator:", value=4, step=1, key="imp_den")

            if st.button("Convert to Mixed") and imp_den != 0:
                whole_part = int(imp_num) // int(imp_den)
                remainder = int(imp_num) % int(imp_den)

                if remainder == 0:
                    st.success(f"**{int(imp_num)}/{int(imp_den)} = {whole_part}**")
                    st.info("This is a whole number (no fractional part)")
                else:
                    # Simplify the fractional part
                    frac_part = Fraction(remainder, int(imp_den))
                    st.success(f"**{int(imp_num)}/{int(imp_den)} = {whole_part} {frac_part}**")
                    st.info(f"Calculation: {int(imp_num)} ÷ {int(imp_den)} = {whole_part} remainder {remainder}")


def ratio_calculator():
    """Calculate ratios and proportions"""
    create_tool_header("Ratio Calculator", "Work with ratios, proportions, and scaling", "⚖️")

    calculation_type = st.selectbox("Calculation type:", [
        "Simplify Ratio", "Equivalent Ratios", "Proportion Solver", "Scale Factor",
        "Ratio to Percentage", "Part-to-Whole Ratios", "Golden Ratio"
    ])

    if calculation_type == "Simplify Ratio":
        st.markdown("### ✨ Simplify Ratio")

        col1, col2 = st.columns(2)
        with col1:
            a = st.number_input("First number:", value=12.0)
        with col2:
            b = st.number_input("Second number:", value=18.0)

        if st.button("Simplify Ratio") and a != 0 and b != 0:
            # Find GCD
            gcd_value = math.gcd(int(abs(a)), int(abs(b)))
            simplified_a = int(a / gcd_value)
            simplified_b = int(b / gcd_value)

            st.success(f"**{int(a)}:{int(b)} = {simplified_a}:{simplified_b}**")

            if gcd_value > 1:
                st.info(f"Both numbers divided by GCD: {gcd_value}")
            else:
                st.info("Ratio is already in simplest form")

            # Show as fraction and decimal
            ratio_decimal = a / b
            st.info(f"As decimal: {ratio_decimal:.4f}")
            st.info(f"Meaning: for every {simplified_a} of the first, there are {simplified_b} of the second")

    elif calculation_type == "Equivalent Ratios":
        st.markdown("### 🔄 Find Equivalent Ratios")

        col1, col2, col3 = st.columns(3)
        with col1:
            ratio_a = st.number_input("Ratio A:", value=3.0)
        with col2:
            ratio_b = st.number_input("Ratio B:", value=4.0)
        with col3:
            multiplier = st.number_input("Multiply by:", value=2.0, min_value=0.1)

        if st.button("Generate Equivalent Ratios"):
            new_a = ratio_a * multiplier
            new_b = ratio_b * multiplier

            st.success(f"**{ratio_a}:{ratio_b} = {new_a}:{new_b}**")

            # Show several equivalent ratios
            st.markdown("**More equivalent ratios:**")
            for mult in [0.5, 1.5, 2, 3, 5]:
                equiv_a = ratio_a * mult
                equiv_b = ratio_b * mult
                st.write(f"× {mult}: {equiv_a}:{equiv_b}")

    elif calculation_type == "Proportion Solver":
        st.markdown("### 🧮 Solve Proportions: A:B = C:X")

        col1, col2, col3 = st.columns(3)
        with col1:
            A = st.number_input("A:", value=3.0)
            B = st.number_input("B:", value=4.0)
        with col2:
            C = st.number_input("C:", value=6.0)
            solve_for = st.selectbox("Solve for:", ["X (fourth term)", "C (third term)", "B (second term)"])
        with col3:
            X_given = 8.0  # Default value
            if solve_for == "X (fourth term)":
                st.write("Solving: A:B = C:X")
            elif solve_for == "C (third term)":
                X_given = st.number_input("X:", value=8.0, key="x_for_c")
                st.write("Solving: A:B = C:X")
            elif solve_for == "B (second term)":
                X_given = st.number_input("X:", value=8.0, key="x_for_b")
                st.write("Solving: A:B = C:X")

        if st.button("Solve Proportion"):
            if solve_for == "X (fourth term)" and B != 0:
                X = (C * B) / A
                st.success(f"**{A}:{B} = {C}:{X:.3f}**")
                st.info(f"Formula: X = (C × B) / A = ({C} × {B}) / {A} = {X:.3f}")

            elif solve_for == "C (third term)" and B != 0:
                C_solved = (A * X_given) / B
                st.success(f"**{A}:{B} = {C_solved:.3f}:{X_given}**")
                st.info(f"Formula: C = (A × X) / B = ({A} × {X_given}) / {B} = {C_solved:.3f}")

            elif solve_for == "B (second term)" and A != 0:
                B_solved = (C * X_given) / A
                st.success(f"**{A}:{B_solved:.3f} = {C}:{X_given}**")
                st.info(f"Formula: B = (C × X) / A = ({C} × {X_given}) / {A} = {B_solved:.3f}")

    elif calculation_type == "Scale Factor":
        st.markdown("### 📏 Scale Factor Calculator")

        col1, col2 = st.columns(2)
        with col1:
            st.markdown("**Original Dimensions:**")
            orig_length = st.number_input("Original length:", value=10.0)
            orig_width = st.number_input("Original width:", value=8.0)

        with col2:
            scale_method = st.selectbox("Scale by:", ["Scale Factor", "New Length", "New Width"])

            if scale_method == "Scale Factor":
                scale_factor = st.number_input("Scale factor:", value=1.5, min_value=0.01)
            elif scale_method == "New Length":
                new_length = st.number_input("New length:", value=15.0)
            elif scale_method == "New Width":
                new_width = st.number_input("New width:", value=12.0)

        if st.button("Calculate Scaling"):
            # Initialize variables to defaults
            scale_factor = 1.0
            new_length = orig_length
            new_width = orig_width
            calculated_width = orig_width
            calculated_length = orig_length

            if scale_method == "Scale Factor":
                new_length = orig_length * scale_factor
                new_width = orig_width * scale_factor
                st.success(f"**New dimensions: {new_length:.2f} × {new_width:.2f}**")
                st.info(f"Scale factor: {scale_factor}× (each dimension multiplied by {scale_factor})")

            elif scale_method == "New Length" and orig_length != 0:
                scale_factor = new_length / orig_length
                calculated_width = orig_width * scale_factor
                new_width = calculated_width  # Update for area calculation
                st.success(f"**Scale factor: {scale_factor:.3f}×**")
                st.success(f"**New dimensions: {new_length:.2f} × {calculated_width:.2f}**")
                st.info(f"To maintain proportions, width becomes {calculated_width:.2f}")

            elif scale_method == "New Width" and orig_width != 0:
                scale_factor = new_width / orig_width
                calculated_length = orig_length * scale_factor
                new_length = calculated_length  # Update for area calculation
                st.success(f"**Scale factor: {scale_factor:.3f}×**")
                st.success(f"**New dimensions: {calculated_length:.2f} × {new_width:.2f}**")
                st.info(f"To maintain proportions, length becomes {calculated_length:.2f}")

            # Show area scaling
            orig_area = orig_length * orig_width
            new_area = new_length * new_width
            area_scale = scale_factor ** 2

            st.info(f"Area scaling: {orig_area:.2f} → {new_area:.2f} (×{area_scale:.3f})")

    elif calculation_type == "Ratio to Percentage":
        st.markdown("### 📊 Convert Ratio to Percentages")

        st.write("Enter ratio parts (e.g., for 3:4:5, enter three values)")

        num_parts = st.selectbox("Number of parts:", [2, 3, 4, 5])
        parts = []

        cols = st.columns(num_parts)
        for i in range(num_parts):
            with cols[i]:
                part = st.number_input(f"Part {i + 1}:", value=float(i + 1), min_value=0.0, key=f"part_{i}")
                parts.append(part)

        if st.button("Convert to Percentages") and all(p > 0 for p in parts):
            total = sum(parts)
            percentages = [(part / total) * 100 for part in parts]

            st.success("**Ratio to Percentages:**")
            ratio_str = ":".join([str(int(p)) if p.is_integer() else str(p) for p in parts])
            st.write(f"Ratio: {ratio_str}")

            for i, (part, percent) in enumerate(zip(parts, percentages)):
                st.write(f"Part {i + 1}: {part} → {percent:.2f}%")

            st.info(f"Total: {total} → 100%")

            # Show visual representation
            st.markdown("**Visual representation:**")
            for i, percent in enumerate(percentages):
                bar_length = int(percent / 2)  # Scale for display
                bar = "█" * bar_length
                st.write(f"Part {i + 1}: {bar} {percent:.1f}%")

    elif calculation_type == "Part-to-Whole Ratios":
        st.markdown("### 🎯 Part-to-Whole Ratios")

        col1, col2 = st.columns(2)
        with col1:
            part = st.number_input("Part:", value=25.0)
            whole = st.number_input("Whole:", value=100.0)

        with col2:
            ratio_format = st.selectbox("Show ratio as:", ["Part:Whole", "Part:Remaining", "Simplified"])

        if st.button("Calculate Ratios") and whole != 0 and part <= whole:
            remaining = whole - part

            if ratio_format == "Part:Whole":
                # Simplify part:whole
                gcd_pw = math.gcd(int(abs(part)), int(abs(whole)))
                simp_part = int(part / gcd_pw)
                simp_whole = int(whole / gcd_pw)
                st.success(f"**Part to Whole: {simp_part}:{simp_whole}**")

            elif ratio_format == "Part:Remaining":
                # Simplify part:remaining
                if remaining > 0:
                    gcd_pr = math.gcd(int(abs(part)), int(abs(remaining)))
                    simp_part = int(part / gcd_pr)
                    simp_remaining = int(remaining / gcd_pr)
                    st.success(f"**Part to Remaining: {simp_part}:{simp_remaining}**")
                else:
                    st.success(f"**Part equals whole (no remainder)**")

            elif ratio_format == "Simplified":
                # Show both ratios
                gcd_pw = math.gcd(int(abs(part)), int(abs(whole)))
                simp_part_w = int(part / gcd_pw)
                simp_whole_w = int(whole / gcd_pw)

                st.success(f"**Part:Whole = {simp_part_w}:{simp_whole_w}**")

                if remaining > 0:
                    gcd_pr = math.gcd(int(abs(part)), int(abs(remaining)))
                    simp_part_r = int(part / gcd_pr)
                    simp_remaining_r = int(remaining / gcd_pr)
                    st.success(f"**Part:Remaining = {simp_part_r}:{simp_remaining_r}**")

            # Show percentages
            part_percent = (part / whole) * 100
            remaining_percent = (remaining / whole) * 100

            st.info(f"As percentages: {part_percent:.1f}% : {remaining_percent:.1f}%")
            st.info(f"Decimal ratio: {part / whole:.4f} : {remaining / whole:.4f}")

        elif part > whole:
            st.error("Part cannot be greater than whole!")

    elif calculation_type == "Golden Ratio":
        st.markdown("### ✨ Golden Ratio Calculator")
        st.write("The golden ratio (φ) ≈ 1.618033988749...")

        golden_ratio = (1 + math.sqrt(5)) / 2

        calculation_method = st.selectbox("Calculate:", [
            "Golden Rectangle", "Golden Spiral", "Fibonacci and Golden Ratio", "Golden Ratio Properties"
        ])

        if calculation_method == "Golden Rectangle":
            width = st.number_input("Width:", value=10.0, min_value=0.1)

            if st.button("Calculate Golden Rectangle"):
                height = width / golden_ratio
                st.success(f"**Golden Rectangle dimensions:**")
                st.write(f"Width: {width}")
                st.write(f"Height: {height:.4f}")
                st.write(f"Ratio: {width / height:.6f} ≈ φ")

                st.info(f"Golden ratio φ = {golden_ratio:.10f}")

        elif calculation_method == "Fibonacci and Golden Ratio":
            n_terms = st.slider("Number of Fibonacci terms:", 5, 20, 10)

            if st.button("Calculate Fibonacci Ratios"):
                # Generate Fibonacci sequence
                fib = [0, 1]
                for i in range(2, n_terms):
                    fib.append(fib[i - 1] + fib[i - 2])

                st.success("**Fibonacci sequence and ratios:**")

                ratios = []
                for i in range(2, n_terms):
                    if fib[i - 1] != 0:
                        ratio = fib[i] / fib[i - 1]
                        ratios.append(ratio)
                        st.write(f"F({i}) / F({i - 1}) = {fib[i]} / {fib[i - 1]} = {ratio:.8f}")

                if ratios:
                    final_ratio = ratios[-1]
                    difference = abs(final_ratio - golden_ratio)
                    st.info(f"**Final ratio: {final_ratio:.8f}**")
                    st.info(f"**Golden ratio: {golden_ratio:.8f}**")
                    st.info(f"**Difference: {difference:.8f}**")

        elif calculation_method == "Golden Ratio Properties":
            st.success("**Golden Ratio Properties:**")
            st.write(f"φ = {golden_ratio:.10f}")
            st.write(f"φ² = {golden_ratio ** 2:.10f}")
            st.write(f"1/φ = {1 / golden_ratio:.10f}")
            st.write(f"φ - 1 = {golden_ratio - 1:.10f}")

            st.markdown("**Mathematical relationships:**")
            st.write("• φ² = φ + 1")
            st.write("• φ = (1 + √5) / 2")
            st.write("• 1/φ = φ - 1")
            st.write("• φ ≈ 1.618...")

            # Verify the relationships
            st.info("**Verification:**")
            st.write(f"φ² = {golden_ratio ** 2:.6f}, φ + 1 = {golden_ratio + 1:.6f}")
            st.write(f"1/φ = {1 / golden_ratio:.6f}, φ - 1 = {golden_ratio - 1:.6f}")


def hypothesis_testing():
    """Comprehensive hypothesis testing tool"""
    create_tool_header("Hypothesis Testing", "Perform various statistical hypothesis tests", "📊")

    test_type = st.selectbox("Select Test Type:", [
        "One-Sample t-test", "Two-Sample t-test", "Paired t-test", "Chi-Square Test",
        "Normality Tests", "One-Way ANOVA", "Mann-Whitney U Test", "Wilcoxon Signed-Rank Test"
    ])

    if test_type == "Chi-Square Test":
        chi_square_test()
    elif test_type == "Normality Tests":
        normality_tests()
    elif test_type == "One-Sample t-test":
        one_sample_ttest()
    elif test_type == "Two-Sample t-test":
        two_sample_ttest()
    elif test_type == "Paired t-test":
        paired_ttest()
    elif test_type == "One-Way ANOVA":
        one_way_anova()
    elif test_type == "Mann-Whitney U Test":
        mann_whitney_test()
    elif test_type == "Wilcoxon Signed-Rank Test":
        wilcoxon_test()


def chi_square_test():
    """Chi-square test for independence and goodness of fit"""
    st.markdown("### 🔍 Chi-Square Test")

    test_subtype = st.selectbox("Test Type:", ["Goodness of Fit", "Test of Independence"])

    if test_subtype == "Goodness of Fit":
        st.markdown("#### Test if observed frequencies match expected distribution")

        # Data input methods
        input_method = st.selectbox("Data Input Method:", ["Manual Entry", "Upload File"])

        if input_method == "Manual Entry":
            observed_text = st.text_area("Observed frequencies (comma-separated):",
                                         placeholder="20, 15, 25, 10", value="20, 15, 25, 10")
            expected_text = st.text_area("Expected frequencies (comma-separated):",
                                         placeholder="18, 18, 18, 18", value="18, 18, 18, 18")

            if observed_text and expected_text and st.button("Run Chi-Square Goodness of Fit"):
                try:
                    observed = [float(x.strip()) for x in observed_text.split(',')]
                    expected = [float(x.strip()) for x in expected_text.split(',')]

                    if len(observed) != len(expected):
                        st.error("Observed and expected frequencies must have the same length")
                        return

                    if any(e <= 0 for e in expected):
                        st.error("Expected frequencies must be positive")
                        return

                    # Perform chi-square test
                    chi2_stat, p_value = stats.chisquare(observed, expected)
                    degrees_freedom = len(observed) - 1

                    # Display results
                    st.markdown("### 📊 Chi-Square Goodness of Fit Results")

                    col1, col2, col3 = st.columns(3)
                    with col1:
                        st.metric("Chi-Square Statistic", f"{chi2_stat:.4f}")
                    with col2:
                        st.metric("p-value", f"{p_value:.4f}")
                    with col3:
                        st.metric("Degrees of Freedom", degrees_freedom)

                    # Interpretation
                    alpha = st.slider("Significance Level (α):", 0.01, 0.10, 0.05, 0.01)

                    if p_value < alpha:
                        st.error(f"🚫 **Reject null hypothesis** (p = {p_value:.4f} < α = {alpha})")
                        st.write("The observed frequencies significantly differ from expected frequencies.")
                    else:
                        st.success(f"✅ **Fail to reject null hypothesis** (p = {p_value:.4f} ≥ α = {alpha})")
                        st.write("The observed frequencies do not significantly differ from expected frequencies.")

                    # Show data comparison
                    st.markdown("### 📈 Data Comparison")
                    comparison_df = pd.DataFrame({
                        'Category': [f'Category {i + 1}' for i in range(len(observed))],
                        'Observed': observed,
                        'Expected': expected,
                        'Residual': [o - e for o, e in zip(observed, expected)]
                    })
                    st.dataframe(comparison_df)

                    # Critical value
                    critical_value = stats.chi2.ppf(1 - alpha, degrees_freedom)
                    st.info(f"Critical value at α = {alpha}: {critical_value:.4f}")

                except ValueError as e:
                    st.error(f"Error parsing data: {str(e)}")

        else:  # File upload
            uploaded_file = FileHandler.upload_files(['csv'], accept_multiple=False)
            if uploaded_file:
                df = FileHandler.process_csv_file(uploaded_file[0])
                if df is not None:
                    numeric_cols = df.select_dtypes(include=[np.number]).columns.tolist()
                    if len(numeric_cols) >= 2:
                        col1, col2 = st.columns(2)
                        with col1:
                            observed_col = st.selectbox("Observed frequencies column:", numeric_cols)
                        with col2:
                            expected_col = st.selectbox("Expected frequencies column:",
                                                        [col for col in numeric_cols if col != observed_col])

                        if st.button("Run Chi-Square Test from File"):
                            observed = df[observed_col].dropna().tolist()
                            expected = df[expected_col].dropna().tolist()

                            if len(observed) == len(expected):
                                chi2_stat, p_value = stats.chisquare(observed, expected)
                                degrees_freedom = len(observed) - 1

                                st.markdown("### 📊 Results")
                                st.write(f"Chi-Square Statistic: {chi2_stat:.4f}")
                                st.write(f"p-value: {p_value:.4f}")
                                st.write(f"Degrees of Freedom: {degrees_freedom}")
                            else:
                                st.error("Columns must have the same number of valid values")
                    else:
                        st.error("Need at least 2 numeric columns for the test")

    elif test_subtype == "Test of Independence":
        st.markdown("#### Test if two categorical variables are independent")

        # Contingency table input
        st.markdown("**Enter Contingency Table Data:**")

        rows = st.number_input("Number of rows:", min_value=2, max_value=10, value=2)
        cols = st.number_input("Number of columns:", min_value=2, max_value=10, value=2)

        st.markdown("Enter the observed frequencies for each cell:")

        # Create input grid
        contingency_table = []
        for i in range(int(rows)):
            row_data = []
            cols_input = st.columns(int(cols))
            for j in range(int(cols)):
                with cols_input[j]:
                    value = st.number_input(f"Row {i + 1}, Col {j + 1}:",
                                            min_value=0.0, value=10.0,
                                            key=f"cell_{i}_{j}")
                    row_data.append(value)
            contingency_table.append(row_data)

        if st.button("Run Chi-Square Test of Independence"):
            try:
                # Convert to numpy array
                observed = np.array(contingency_table)

                # Perform chi-square test
                chi2_stat, p_value, dof, expected = stats.chi2_contingency(observed)

                # Display results
                st.markdown("### 📊 Chi-Square Test of Independence Results")

                col1, col2, col3 = st.columns(3)
                with col1:
                    st.metric("Chi-Square Statistic", f"{chi2_stat:.4f}")
                with col2:
                    st.metric("p-value", f"{p_value:.4f}")
                with col3:
                    st.metric("Degrees of Freedom", dof)

                # Interpretation
                alpha = st.slider("Significance Level (α):", 0.01, 0.10, 0.05, 0.01, key="indep_alpha")

                if p_value < alpha:
                    st.error(f"🚫 **Reject null hypothesis** (p = {p_value:.4f} < α = {alpha})")
                    st.write("The variables are **NOT independent** - there is a significant association.")
                else:
                    st.success(f"✅ **Fail to reject null hypothesis** (p = {p_value:.4f} ≥ α = {alpha})")
                    st.write("The variables appear to be **independent** - no significant association.")

                # Show observed vs expected
                st.markdown("### 📈 Observed vs Expected Frequencies")

                col1, col2 = st.columns(2)
                with col1:
                    st.markdown("**Observed:**")
                    st.dataframe(pd.DataFrame(observed))
                with col2:
                    st.markdown("**Expected:**")
                    st.dataframe(pd.DataFrame(expected.round(2)))

                # Critical value
                critical_value = stats.chi2.ppf(1 - alpha, dof)
                st.info(f"Critical value at α = {alpha}: {critical_value:.4f}")

            except Exception as e:
                st.error(f"Error in calculation: {str(e)}")


def normality_tests():
    """Various tests for normality"""
    st.markdown("### 🔔 Normality Tests")
    st.write("Test if your data follows a normal distribution")

    # Data input
    data_input_method = st.selectbox("Data Input Method:", ["Manual Entry", "Upload File", "Generate Sample Data"])

    data = None

    if data_input_method == "Manual Entry":
        data_text = st.text_area("Enter data (comma or space separated):",
                                 placeholder="1.2, 2.3, 1.8, 2.1, 1.9, 2.4, 1.7")

        if data_text:
            try:
                # Parse data
                data = []
                for item in data_text.replace(',', ' ').split():
                    try:
                        data.append(float(item))
                    except ValueError:
                        continue

                if len(data) < 3:
                    st.warning("Need at least 3 data points for normality tests")
                    data = None
            except Exception as e:
                st.error(f"Error parsing data: {str(e)}")
                data = None

    elif data_input_method == "Upload File":
        uploaded_file = FileHandler.upload_files(['csv', 'txt'], accept_multiple=False)
        if uploaded_file:
            try:
                if uploaded_file[0].name.endswith('.csv'):
                    df = FileHandler.process_csv_file(uploaded_file[0])
                    if df is not None:
                        numeric_cols = df.select_dtypes(include=[np.number]).columns
                        if len(numeric_cols) > 0:
                            selected_col = st.selectbox("Select column for normality test:", numeric_cols)
                            data = df[selected_col].dropna().tolist()
                        else:
                            st.error("No numeric columns found")
                else:
                    content = FileHandler.process_text_file(uploaded_file[0])
                    data = []
                    for line in content.split('\n'):
                        for item in line.replace(',', ' ').split():
                            try:
                                data.append(float(item))
                            except ValueError:
                                continue
            except Exception as e:
                st.error(f"Error processing file: {str(e)}")

    elif data_input_method == "Generate Sample Data":
        st.markdown("**Generate sample data for testing:**")

        col1, col2, col3 = st.columns(3)
        with col1:
            distribution = st.selectbox("Distribution:", ["Normal", "Uniform", "Exponential", "Chi-Square"])
        with col2:
            n_samples = st.number_input("Sample size:", min_value=10, max_value=1000, value=100)
        with col3:
            random_seed = st.number_input("Random seed:", value=42)

        if st.button("Generate Data"):
            np.random.seed(int(random_seed))

            if distribution == "Normal":
                data = np.random.normal(0, 1, int(n_samples)).tolist()
            elif distribution == "Uniform":
                data = np.random.uniform(0, 1, int(n_samples)).tolist()
            elif distribution == "Exponential":
                data = np.random.exponential(1, int(n_samples)).tolist()
            elif distribution == "Chi-Square":
                data = np.random.chisquare(5, int(n_samples)).tolist()

            st.success(f"Generated {len(data)} data points from {distribution} distribution")

    # Perform normality tests if data is available
    if data and len(data) >= 3:
        st.markdown("### 📊 Normality Test Results")

        # Select tests to perform
        st.markdown("**Select tests to perform:**")
        col1, col2, col3 = st.columns(3)

        with col1:
            run_shapiro = st.checkbox("Shapiro-Wilk Test", value=True)
        with col2:
            run_anderson = st.checkbox("Anderson-Darling Test", value=True)
        with col3:
            run_ks = st.checkbox("Kolmogorov-Smirnov Test", value=True)

        if st.button("Run Normality Tests"):
            data_array = np.array(data)

            # Basic statistics
            st.markdown("### 📈 Data Summary")
            col1, col2, col3, col4 = st.columns(4)
            with col1:
                st.metric("Sample Size", len(data))
            with col2:
                st.metric("Mean", f"{np.mean(data_array):.4f}")
            with col3:
                st.metric("Std Dev", f"{np.std(data_array, ddof=1):.4f}")
            with col4:
                st.metric("Skewness", f"{stats.skew(data_array):.4f}")

            # Significance level
            alpha = st.slider("Significance Level (α):", 0.01, 0.10, 0.05, 0.01, key="norm_alpha")

            # Run selected tests
            results = []

            if run_shapiro and len(data) <= 5000:  # Shapiro-Wilk has size limitations
                try:
                    stat, p_val = stats.shapiro(data_array)
                    results.append(["Shapiro-Wilk", stat, p_val, "Tests if data comes from normal distribution"])
                except Exception as e:
                    st.warning(f"Shapiro-Wilk test failed: {str(e)}")
            elif run_shapiro:
                st.warning("Shapiro-Wilk test is not reliable for samples > 5000. Skipping.")

            if run_anderson:
                try:
                    result = stats.anderson(data_array, dist='norm')
                    # Use 5% critical value (index 2: 1%, 2.5%, 5%, 10%, 15%)
                    critical_val = result.critical_values[2]
                    p_val = 0.05 if result.statistic > critical_val else 0.1  # Approximation
                    results.append(
                        ["Anderson-Darling", result.statistic, p_val, "Tests goodness of fit to normal distribution"])
                except Exception as e:
                    st.warning(f"Anderson-Darling test failed: {str(e)}")

            if run_ks:
                try:
                    # Standardize data for KS test against standard normal
                    standardized = (data_array - np.mean(data_array)) / np.std(data_array, ddof=1)
                    stat, p_val = stats.kstest(standardized, 'norm')
                    results.append(["Kolmogorov-Smirnov", stat, p_val, "Tests if data follows specified distribution"])
                except Exception as e:
                    st.warning(f"Kolmogorov-Smirnov test failed: {str(e)}")

            # Display results
            if results:
                st.markdown("### 🔍 Test Results")

                results_df = pd.DataFrame(results, columns=['Test', 'Statistic', 'p-value', 'Description'])
                st.dataframe(results_df)

                # Interpretation
                st.markdown("### 💡 Interpretation")

                for test_name, statistic, p_value, description in results:
                    if p_value < alpha:
                        st.error(f"**{test_name}**: Reject normality (p = {p_value:.4f} < α = {alpha})")
                    else:
                        st.success(f"**{test_name}**: Fail to reject normality (p = {p_value:.4f} ≥ α = {alpha})")

                # Overall conclusion
                significant_tests = sum(1 for _, _, p_val, _ in results if p_val < alpha)
                total_tests = len(results)

                st.markdown("### 🎯 Overall Conclusion")
                if significant_tests == 0:
                    st.success("✅ **Data appears to be normally distributed** (all tests fail to reject normality)")
                elif significant_tests == total_tests:
                    st.error("🚫 **Data does NOT appear to be normally distributed** (all tests reject normality)")
                else:
                    st.warning(f"⚠️ **Mixed results** ({significant_tests}/{total_tests} tests reject normality)")
                    st.write("Consider the context and requirements of your analysis.")

                # Visual analysis
                st.markdown("### 📊 Visual Analysis")

                # Create plots
                fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(12, 10))

                # Histogram with normal overlay
                ax1.hist(data_array, bins=min(30, len(data) // 5), density=True, alpha=0.7, color='skyblue',
                         edgecolor='black')
                x_norm = np.linspace(min(data_array), max(data_array), 100)
                y_norm = stats.norm.pdf(x_norm, np.mean(data_array), np.std(data_array, ddof=1))
                ax1.plot(x_norm, y_norm, 'r-', linewidth=2, label='Normal Distribution')
                ax1.set_title('Histogram with Normal Overlay')
                ax1.set_xlabel('Value')
                ax1.set_ylabel('Density')
                ax1.legend()
                ax1.grid(True, alpha=0.3)

                # Q-Q plot
                stats.probplot(data_array, dist="norm", plot=ax2)
                ax2.set_title('Q-Q Plot (vs Normal)')
                ax2.grid(True, alpha=0.3)

                # Box plot
                ax3.boxplot(data_array)
                ax3.set_title('Box Plot')
                ax3.set_ylabel('Value')
                ax3.grid(True, alpha=0.3)

                # Empirical CDF vs Normal CDF
                sorted_data = np.sort(data_array)
                empirical_cdf = np.arange(1, len(sorted_data) + 1) / len(sorted_data)
                theoretical_cdf = stats.norm.cdf(sorted_data, np.mean(data_array), np.std(data_array, ddof=1))

                ax4.plot(sorted_data, empirical_cdf, 'b-', label='Empirical CDF', linewidth=2)
                ax4.plot(sorted_data, theoretical_cdf, 'r--', label='Normal CDF', linewidth=2)
                ax4.set_title('Empirical vs Theoretical CDF')
                ax4.set_xlabel('Value')
                ax4.set_ylabel('Cumulative Probability')
                ax4.legend()
                ax4.grid(True, alpha=0.3)

                plt.tight_layout()
                st.pyplot(fig)
                plt.close(fig)


def one_sample_ttest():
    """One-sample t-test"""
    st.markdown("#### One-Sample t-test")
    st.write("Test if the mean of a sample differs from a hypothesized population mean")

    # Data input
    data_text = st.text_area("Enter sample data (comma or space separated):",
                             placeholder="23.1, 24.5, 22.8, 25.2, 23.9")

    hypothesized_mean = st.number_input("Hypothesized population mean (μ₀):", value=24.0)

    # Alternative hypothesis
    alternative = st.selectbox("Alternative hypothesis:",
                               ["two-sided", "greater", "less"])

    if data_text and st.button("Run One-Sample t-test"):
        try:
            # Parse data
            data = []
            for item in data_text.replace(',', ' ').split():
                try:
                    data.append(float(item))
                except ValueError:
                    continue

            if len(data) < 2:
                st.error("Need at least 2 data points")
                return

            # Perform t-test
            t_stat, p_value = stats.ttest_1samp(data, hypothesized_mean, alternative=alternative)

            # Calculate additional statistics
            sample_mean = np.mean(data)
            sample_std = np.std(data, ddof=1)
            sample_size = len(data)
            degrees_freedom = sample_size - 1

            # Standard error and confidence interval
            se = sample_std / np.sqrt(sample_size)
            alpha = st.slider("Significance Level (α):", 0.01, 0.10, 0.05, 0.01, key="ttest1_alpha")
            confidence_level = 1 - alpha
            t_critical = stats.t.ppf(1 - alpha / 2, degrees_freedom)

            margin_error = t_critical * se
            ci_lower = sample_mean - margin_error
            ci_upper = sample_mean + margin_error

            # Display results
            st.markdown("### 📊 One-Sample t-test Results")

            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric("Sample Mean", f"{sample_mean:.4f}")
                st.metric("Sample Size", sample_size)
            with col2:
                st.metric("t-statistic", f"{t_stat:.4f}")
                st.metric("p-value", f"{p_value:.4f}")
            with col3:
                st.metric("Degrees of Freedom", degrees_freedom)
                st.metric("Standard Error", f"{se:.4f}")

            # Confidence interval
            st.info(f"**{confidence_level * 100:.0f}% Confidence Interval:** [{ci_lower:.4f}, {ci_upper:.4f}]")

            # Interpretation
            if p_value < alpha:
                st.error(f"🚫 **Reject null hypothesis** (p = {p_value:.4f} < α = {alpha})")
                if alternative == "two-sided":
                    st.write(f"The sample mean ({sample_mean:.4f}) significantly differs from μ₀ = {hypothesized_mean}")
                elif alternative == "greater":
                    st.write(
                        f"The sample mean ({sample_mean:.4f}) is significantly greater than μ₀ = {hypothesized_mean}")
                else:
                    st.write(f"The sample mean ({sample_mean:.4f}) is significantly less than μ₀ = {hypothesized_mean}")
            else:
                st.success(f"✅ **Fail to reject null hypothesis** (p = {p_value:.4f} ≥ α = {alpha})")
                st.write(f"Insufficient evidence that the sample mean differs from μ₀ = {hypothesized_mean}")

            # Effect size (Cohen's d)
            cohens_d = (sample_mean - hypothesized_mean) / sample_std
            st.info(f"**Effect size (Cohen's d):** {cohens_d:.4f}")

            if abs(cohens_d) < 0.2:
                effect_interpretation = "small"
            elif abs(cohens_d) < 0.5:
                effect_interpretation = "small to medium"
            elif abs(cohens_d) < 0.8:
                effect_interpretation = "medium to large"
            else:
                effect_interpretation = "large"

            st.write(f"Effect size interpretation: {effect_interpretation}")

        except ValueError as e:
            st.error(f"Error parsing data: {str(e)}")


def two_sample_ttest():
    """Two-sample t-test"""
    st.markdown("#### Two-Sample t-test")
    st.write("Compare means of two independent groups")

    # Equal variances assumption
    equal_var = st.checkbox("Assume equal variances (Welch's t-test if unchecked)", value=True)

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("**Group 1 Data:**")
        data1_text = st.text_area("Enter data for group 1:",
                                  placeholder="20.1, 21.5, 19.8, 22.2", key="group1")

    with col2:
        st.markdown("**Group 2 Data:**")
        data2_text = st.text_area("Enter data for group 2:",
                                  placeholder="18.5, 19.2, 17.8, 20.1", key="group2")

    alternative = st.selectbox("Alternative hypothesis:",
                               ["two-sided", "greater", "less"], key="ttest2_alt")

    if data1_text and data2_text and st.button("Run Two-Sample t-test"):
        try:
            # Parse data
            data1 = [float(x.strip()) for x in data1_text.replace(',', ' ').split() if x.strip()]
            data2 = [float(x.strip()) for x in data2_text.replace(',', ' ').split() if x.strip()]

            if len(data1) < 2 or len(data2) < 2:
                st.error("Need at least 2 data points in each group")
                return

            # Perform t-test
            t_stat, p_value = stats.ttest_ind(data1, data2, equal_var=equal_var, alternative=alternative)

            # Calculate statistics
            mean1, mean2 = np.mean(data1), np.mean(data2)
            std1, std2 = np.std(data1, ddof=1), np.std(data2, ddof=1)
            n1, n2 = len(data1), len(data2)

            # Display results
            st.markdown("### 📊 Two-Sample t-test Results")

            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric("Group 1 Mean", f"{mean1:.4f}")
                st.metric("Group 1 Size", n1)
            with col2:
                st.metric("Group 2 Mean", f"{mean2:.4f}")
                st.metric("Group 2 Size", n2)
            with col3:
                st.metric("Mean Difference", f"{mean1 - mean2:.4f}")
                st.metric("t-statistic", f"{t_stat:.4f}")

            st.metric("p-value", f"{p_value:.4f}")

            # Interpretation
            alpha = st.slider("Significance Level (α):", 0.01, 0.10, 0.05, 0.01, key="ttest2_alpha")

            if p_value < alpha:
                st.error(f"🚫 **Reject null hypothesis** (p = {p_value:.4f} < α = {alpha})")
                st.write("There is a significant difference between the group means.")
            else:
                st.success(f"✅ **Fail to reject null hypothesis** (p = {p_value:.4f} ≥ α = {alpha})")
                st.write("No significant difference between the group means.")

            # Effect size
            pooled_std = np.sqrt(((n1 - 1) * std1 ** 2 + (n2 - 1) * std2 ** 2) / (n1 + n2 - 2))
            cohens_d = (mean1 - mean2) / pooled_std
            st.info(f"**Effect size (Cohen's d):** {cohens_d:.4f}")

        except ValueError as e:
            st.error(f"Error parsing data: {str(e)}")


def paired_ttest():
    """Paired t-test"""
    st.markdown("#### Paired t-test")
    st.write("Compare means of paired observations (before/after, matched pairs)")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("**Before/Group 1:**")
        before_text = st.text_area("Enter before measurements:",
                                   placeholder="85, 90, 78, 92, 88", key="before")

    with col2:
        st.markdown("**After/Group 2:**")
        after_text = st.text_area("Enter after measurements:",
                                  placeholder="82, 88, 76, 90, 85", key="after")

    if before_text and after_text and st.button("Run Paired t-test"):
        try:
            # Parse data
            before = [float(x.strip()) for x in before_text.replace(',', ' ').split() if x.strip()]
            after = [float(x.strip()) for x in after_text.replace(',', ' ').split() if x.strip()]

            if len(before) != len(after):
                st.error("Before and after measurements must have the same number of values")
                return

            if len(before) < 2:
                st.error("Need at least 2 paired observations")
                return

            # Perform paired t-test
            t_stat, p_value = stats.ttest_rel(before, after)

            # Calculate differences
            differences = np.array(before) - np.array(after)
            mean_diff = np.mean(differences)
            std_diff = np.std(differences, ddof=1)
            n_pairs = len(differences)

            # Display results
            st.markdown("### 📊 Paired t-test Results")

            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric("Mean Before", f"{np.mean(before):.4f}")
                st.metric("Mean After", f"{np.mean(after):.4f}")
            with col2:
                st.metric("Mean Difference", f"{mean_diff:.4f}")
                st.metric("t-statistic", f"{t_stat:.4f}")
            with col3:
                st.metric("p-value", f"{p_value:.4f}")
                st.metric("Sample Size", n_pairs)

            # Interpretation
            alpha = st.slider("Significance Level (α):", 0.01, 0.10, 0.05, 0.01, key="paired_alpha")

            if p_value < alpha:
                st.error(f"🚫 **Reject null hypothesis** (p = {p_value:.4f} < α = {alpha})")
                st.write("There is a significant difference between before and after measurements.")
            else:
                st.success(f"✅ **Fail to reject null hypothesis** (p = {p_value:.4f} ≥ α = {alpha})")
                st.write("No significant difference between before and after measurements.")

            # Show differences
            st.markdown("### 📈 Paired Differences")
            diff_df = pd.DataFrame({
                'Pair': range(1, n_pairs + 1),
                'Before': before,
                'After': after,
                'Difference': differences
            })
            st.dataframe(diff_df)

        except ValueError as e:
            st.error(f"Error parsing data: {str(e)}")


def one_way_anova():
    """One-way ANOVA"""
    st.markdown("#### One-Way ANOVA")
    st.write("Compare means of three or more independent groups")

    # Number of groups
    num_groups = st.number_input("Number of groups:", min_value=3, max_value=10, value=3)

    # Data input for each group
    groups_data = []
    group_names = []

    cols = st.columns(min(int(num_groups), 3))  # Max 3 columns for layout

    for i in range(int(num_groups)):
        col_idx = i % 3
        with cols[col_idx]:
            st.markdown(f"**Group {i + 1}:**")
            group_name = st.text_input(f"Group {i + 1} name:", value=f"Group {i + 1}", key=f"group_name_{i}")
            group_data_text = st.text_area(f"Data for {group_name}:",
                                           placeholder="20.1, 21.5, 19.8", key=f"group_data_{i}")

            group_names.append(group_name)
            if group_data_text:
                try:
                    group_data = [float(x.strip()) for x in group_data_text.replace(',', ' ').split() if x.strip()]
                    groups_data.append(group_data)
                except ValueError:
                    groups_data.append([])
            else:
                groups_data.append([])

    if st.button("Run One-Way ANOVA"):
        # Check if all groups have data
        valid_groups = [group for group in groups_data if len(group) >= 2]

        if len(valid_groups) < 3:
            st.error("Need at least 3 groups with at least 2 observations each")
            return

        try:
            # Perform ANOVA
            f_stat, p_value = stats.f_oneway(*valid_groups)

            # Calculate group statistics
            group_means = [np.mean(group) for group in valid_groups]
            group_stds = [np.std(group, ddof=1) for group in valid_groups]
            group_sizes = [len(group) for group in valid_groups]

            # Degrees of freedom
            df_between = len(valid_groups) - 1
            df_within = sum(group_sizes) - len(valid_groups)
            df_total = sum(group_sizes) - 1

            # Display results
            st.markdown("### 📊 One-Way ANOVA Results")

            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric("F-statistic", f"{f_stat:.4f}")
            with col2:
                st.metric("p-value", f"{p_value:.4f}")
            with col3:
                st.metric("Groups", len(valid_groups))

            # Degrees of freedom
            st.write(f"**Degrees of freedom:** Between groups = {df_between}, Within groups = {df_within}")

            # Group statistics
            st.markdown("### 📈 Group Statistics")
            stats_df = pd.DataFrame({
                'Group': [group_names[i] for i in range(len(valid_groups))],
                'Mean': group_means,
                'Std Dev': group_stds,
                'Size': group_sizes
            })
            st.dataframe(stats_df)

            # Interpretation
            alpha = st.slider("Significance Level (α):", 0.01, 0.10, 0.05, 0.01, key="anova_alpha")

            if p_value < alpha:
                st.error(f"🚫 **Reject null hypothesis** (p = {p_value:.4f} < α = {alpha})")
                st.write("At least one group mean is significantly different from the others.")
                st.info("Consider post-hoc tests to determine which groups differ.")
            else:
                st.success(f"✅ **Fail to reject null hypothesis** (p = {p_value:.4f} ≥ α = {alpha})")
                st.write("No significant differences found between group means.")

        except Exception as e:
            st.error(f"Error in ANOVA calculation: {str(e)}")


def mann_whitney_test():
    """Mann-Whitney U test (non-parametric alternative to two-sample t-test)"""
    st.markdown("#### Mann-Whitney U Test")
    st.write("Non-parametric test to compare two independent groups (alternative to two-sample t-test)")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("**Group 1:**")
        group1_text = st.text_area("Enter data for group 1:",
                                   placeholder="15, 18, 20, 22, 25", key="mw_group1")

    with col2:
        st.markdown("**Group 2:**")
        group2_text = st.text_area("Enter data for group 2:",
                                   placeholder="12, 14, 16, 19, 21", key="mw_group2")

    alternative = st.selectbox("Alternative hypothesis:",
                               ["two-sided", "greater", "less"], key="mw_alt")

    if group1_text and group2_text and st.button("Run Mann-Whitney U Test"):
        try:
            # Parse data
            group1 = [float(x.strip()) for x in group1_text.replace(',', ' ').split() if x.strip()]
            group2 = [float(x.strip()) for x in group2_text.replace(',', ' ').split() if x.strip()]

            if len(group1) < 1 or len(group2) < 1:
                st.error("Each group must have at least 1 observation")
                return

            # Perform Mann-Whitney U test
            u_stat, p_value = stats.mannwhitneyu(group1, group2, alternative=alternative)

            # Calculate additional statistics
            median1, median2 = np.median(group1), np.median(group2)
            n1, n2 = len(group1), len(group2)

            # Display results
            st.markdown("### 📊 Mann-Whitney U Test Results")

            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric("Group 1 Median", f"{median1:.4f}")
                st.metric("Group 1 Size", n1)
            with col2:
                st.metric("Group 2 Median", f"{median2:.4f}")
                st.metric("Group 2 Size", n2)
            with col3:
                st.metric("U-statistic", f"{u_stat:.4f}")
                st.metric("p-value", f"{p_value:.4f}")

            # Interpretation
            alpha = st.slider("Significance Level (α):", 0.01, 0.10, 0.05, 0.01, key="mw_alpha")

            if p_value < alpha:
                st.error(f"🚫 **Reject null hypothesis** (p = {p_value:.4f} < α = {alpha})")
                st.write("There is a significant difference in the distributions of the two groups.")
            else:
                st.success(f"✅ **Fail to reject null hypothesis** (p = {p_value:.4f} ≥ α = {alpha})")
                st.write("No significant difference in the distributions of the two groups.")

            # Effect size (r = Z / sqrt(N))
            z_score = stats.norm.ppf(1 - p_value / 2)  # Approximation
            r_effect_size = z_score / np.sqrt(n1 + n2)
            st.info(f"**Effect size (r):** {r_effect_size:.4f}")

        except ValueError as e:
            st.error(f"Error parsing data: {str(e)}")


def wilcoxon_test():
    """Wilcoxon signed-rank test (non-parametric alternative to paired t-test)"""
    st.markdown("#### Wilcoxon Signed-Rank Test")
    st.write("Non-parametric test for paired observations (alternative to paired t-test)")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("**Before/Condition 1:**")
        before_text = st.text_area("Enter before measurements:",
                                   placeholder="15, 18, 20, 22, 25", key="wilcox_before")

    with col2:
        st.markdown("**After/Condition 2:**")
        after_text = st.text_area("Enter after measurements:",
                                  placeholder="14, 16, 18, 20, 23", key="wilcox_after")

    if before_text and after_text and st.button("Run Wilcoxon Signed-Rank Test"):
        try:
            # Parse data
            before = [float(x.strip()) for x in before_text.replace(',', ' ').split() if x.strip()]
            after = [float(x.strip()) for x in after_text.replace(',', ' ').split() if x.strip()]

            if len(before) != len(after):
                st.error("Before and after measurements must have the same number of values")
                return

            if len(before) < 1:
                st.error("Need at least 1 paired observation")
                return

            # Perform Wilcoxon signed-rank test
            w_stat, p_value = stats.wilcoxon(before, after)

            # Calculate additional statistics
            differences = np.array(before) - np.array(after)
            median_before, median_after = np.median(before), np.median(after)
            median_diff = np.median(differences)
            n_pairs = len(differences)

            # Display results
            st.markdown("### 📊 Wilcoxon Signed-Rank Test Results")

            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric("Median Before", f"{median_before:.4f}")
                st.metric("Median After", f"{median_after:.4f}")
            with col2:
                st.metric("Median Difference", f"{median_diff:.4f}")
                st.metric("W-statistic", f"{w_stat:.4f}")
            with col3:
                st.metric("p-value", f"{p_value:.4f}")
                st.metric("Sample Size", n_pairs)

            # Interpretation
            alpha = st.slider("Significance Level (α):", 0.01, 0.10, 0.05, 0.01, key="wilcox_alpha")

            if p_value < alpha:
                st.error(f"🚫 **Reject null hypothesis** (p = {p_value:.4f} < α = {alpha})")
                st.write("There is a significant difference between before and after measurements.")
            else:
                st.success(f"✅ **Fail to reject null hypothesis** (p = {p_value:.4f} ≥ α = {alpha})")
                st.write("No significant difference between before and after measurements.")

            # Show differences
            st.markdown("### 📈 Paired Differences")
            diff_df = pd.DataFrame({
                'Pair': range(1, n_pairs + 1),
                'Before': before,
                'After': after,
                'Difference': differences
            })
            st.dataframe(diff_df)

        except ValueError as e:
            st.error(f"Error parsing data: {str(e)}")


def probability_calculator():
    """Calculate various probabilities"""
    create_tool_header("Probability Calculator", "Calculate probabilities and combinatorics", "🎲")

    calc_type = st.selectbox("Calculation Type:", [
        "Basic Probability", "Conditional Probability", "Combinatorics",
        "Bayes' Theorem", "Probability Distributions"
    ])

    if calc_type == "Basic Probability":
        st.markdown("### 🎯 Basic Probability Calculations")

        prob_type = st.selectbox("Type:", ["Single Event", "Union of Events", "Intersection of Events"])

        if prob_type == "Single Event":
            favorable = st.number_input("Favorable outcomes:", min_value=0, value=1)
            total = st.number_input("Total possible outcomes:", min_value=1, value=6)

            if st.button("Calculate Probability"):
                probability = favorable / total
                st.success(f"**P(Event) = {probability:.4f} = {probability * 100:.2f}%**")
                st.write(f"Odds in favor: {favorable}:{total - favorable}")
                st.write(f"Odds against: {total - favorable}:{favorable}")

        elif prob_type == "Union of Events":
            st.write("P(A ∪ B) = P(A) + P(B) - P(A ∩ B)")

            col1, col2, col3 = st.columns(3)
            with col1:
                p_a = st.number_input("P(A):", min_value=0.0, max_value=1.0, value=0.3, step=0.01)
            with col2:
                p_b = st.number_input("P(B):", min_value=0.0, max_value=1.0, value=0.4, step=0.01)
            with col3:
                p_ab = st.number_input("P(A ∩ B):", min_value=0.0, max_value=1.0, value=0.1, step=0.01)

            if st.button("Calculate Union"):
                p_union = p_a + p_b - p_ab
                if p_union <= 1.0:
                    st.success(f"**P(A ∪ B) = {p_union:.4f} = {p_union * 100:.2f}%**")
                else:
                    st.error("Result exceeds 1.0. Check your input values.")

        elif prob_type == "Intersection of Events":
            independence = st.radio("Are the events independent?", ["Yes", "No"])

            if independence == "Yes":
                st.write("P(A ∩ B) = P(A) × P(B)")
                col1, col2 = st.columns(2)
                with col1:
                    p_a = st.number_input("P(A):", min_value=0.0, max_value=1.0, value=0.3, step=0.01, key="indep_a")
                with col2:
                    p_b = st.number_input("P(B):", min_value=0.0, max_value=1.0, value=0.4, step=0.01, key="indep_b")

                if st.button("Calculate Intersection"):
                    p_intersection = p_a * p_b
                    st.success(f"**P(A ∩ B) = {p_intersection:.4f} = {p_intersection * 100:.2f}%**")
            else:
                st.write("P(A ∩ B) = P(A) × P(B|A)")
                col1, col2 = st.columns(2)
                with col1:
                    p_a = st.number_input("P(A):", min_value=0.0, max_value=1.0, value=0.3, step=0.01, key="dep_a")
                with col2:
                    p_b_given_a = st.number_input("P(B|A):", min_value=0.0, max_value=1.0, value=0.6, step=0.01)

                if st.button("Calculate Intersection"):
                    p_intersection = p_a * p_b_given_a
                    st.success(f"**P(A ∩ B) = {p_intersection:.4f} = {p_intersection * 100:.2f}%**")

    elif calc_type == "Combinatorics":
        st.markdown("### 🔢 Combinatorics Calculations")

        combo_type = st.selectbox("Type:", ["Permutations", "Combinations", "Factorial"])

        if combo_type == "Permutations":
            st.write("P(n,r) = n! / (n-r)!")

            col1, col2 = st.columns(2)
            with col1:
                n = st.number_input("n (total items):", min_value=0, value=10)
            with col2:
                r = st.number_input("r (items to arrange):", min_value=0, value=3)

            if st.button("Calculate Permutations"):
                if r <= n:
                    result = math.perm(int(n), int(r))
                    st.success(f"**P({int(n)},{int(r)}) = {result:,}**")
                    st.write(f"There are {result:,} ways to arrange {int(r)} items from {int(n)} total items")
                else:
                    st.error("r cannot be greater than n")

        elif combo_type == "Combinations":
            st.write("C(n,r) = n! / (r!(n-r)!)")

            col1, col2 = st.columns(2)
            with col1:
                n = st.number_input("n (total items):", min_value=0, value=10, key="comb_n")
            with col2:
                r = st.number_input("r (items to choose):", min_value=0, value=3, key="comb_r")

            if st.button("Calculate Combinations"):
                if r <= n:
                    result = math.comb(int(n), int(r))
                    st.success(f"**C({int(n)},{int(r)}) = {result:,}**")
                    st.write(f"There are {result:,} ways to choose {int(r)} items from {int(n)} total items")
                else:
                    st.error("r cannot be greater than n")

        elif combo_type == "Factorial":
            n = st.number_input("Calculate factorial of:", min_value=0, value=5)

            if st.button("Calculate Factorial"):
                if n <= 20:  # Prevent extremely large calculations
                    result = math.factorial(int(n))
                    st.success(f"**{int(n)}! = {result:,}**")
                else:
                    st.warning("Factorial calculation limited to n ≤ 20 for display purposes")


def distribution_calculator():
    """Calculate probabilities for various statistical distributions"""
    create_tool_header("Distribution Calculator", "Calculate probabilities for statistical distributions", "📊")

    distribution = st.selectbox("Select Distribution:", [
        "Normal Distribution", "Binomial Distribution", "Poisson Distribution",
        "Student's t-Distribution", "Chi-Square Distribution", "F-Distribution"
    ])

    if distribution == "Normal Distribution":
        st.markdown("### 🔔 Normal Distribution")

        col1, col2 = st.columns(2)
        with col1:
            mean = st.number_input("Mean (μ):", value=0.0)
            std = st.number_input("Standard Deviation (σ):", min_value=0.01, value=1.0)

        with col2:
            calc_type = st.selectbox("Calculate:",
                                     ["P(X ≤ x)", "P(X ≥ x)", "P(a ≤ X ≤ b)", "Find x for given probability"])

        if calc_type == "P(X ≤ x)":
            x = st.number_input("x value:", value=0.0)
            if st.button("Calculate"):
                prob = stats.norm.cdf(x, mean, std)
                st.success(f"**P(X ≤ {x}) = {prob:.4f} = {prob * 100:.2f}%**")

        elif calc_type == "P(X ≥ x)":
            x = st.number_input("x value:", value=0.0, key="norm_geq")
            if st.button("Calculate"):
                prob = 1 - stats.norm.cdf(x, mean, std)
                st.success(f"**P(X ≥ {x}) = {prob:.4f} = {prob * 100:.2f}%**")

        elif calc_type == "P(a ≤ X ≤ b)":
            col1, col2 = st.columns(2)
            with col1:
                a = st.number_input("Lower bound (a):", value=-1.0)
            with col2:
                b = st.number_input("Upper bound (b):", value=1.0)

            if st.button("Calculate"):
                prob = stats.norm.cdf(b, mean, std) - stats.norm.cdf(a, mean, std)
                st.success(f"**P({a} ≤ X ≤ {b}) = {prob:.4f} = {prob * 100:.2f}%**")

        elif calc_type == "Find x for given probability":
            prob = st.number_input("Probability:", min_value=0.01, max_value=0.99, value=0.95)
            if st.button("Calculate"):
                x = stats.norm.ppf(prob, mean, std)
                st.success(f"**x = {x:.4f}** (such that P(X ≤ x) = {prob})")

    elif distribution == "Binomial Distribution":
        st.markdown("### 🎲 Binomial Distribution")

        col1, col2 = st.columns(2)
        with col1:
            n = st.number_input("Number of trials (n):", min_value=1, value=10)
            p = st.number_input("Probability of success (p):", min_value=0.0, max_value=1.0, value=0.5)

        with col2:
            calc_type = st.selectbox("Calculate:", ["P(X = k)", "P(X ≤ k)", "P(X ≥ k)"])
            k = st.number_input("Number of successes (k):", min_value=0, value=5)

        if st.button("Calculate Binomial"):
            if calc_type == "P(X = k)":
                prob = stats.binom.pmf(int(k), int(n), p)
                st.success(f"**P(X = {int(k)}) = {prob:.4f} = {prob * 100:.2f}%**")
            elif calc_type == "P(X ≤ k)":
                prob = stats.binom.cdf(int(k), int(n), p)
                st.success(f"**P(X ≤ {int(k)}) = {prob:.4f} = {prob * 100:.2f}%**")
            elif calc_type == "P(X ≥ k)":
                prob = 1 - stats.binom.cdf(int(k) - 1, int(n), p)
                st.success(f"**P(X ≥ {int(k)}) = {prob:.4f} = {prob * 100:.2f}%**")

            # Show distribution info
            mean_binom = n * p
            var_binom = n * p * (1 - p)
            st.info(f"Distribution mean: {mean_binom:.2f}, variance: {var_binom:.2f}")


def confidence_intervals():
    """Calculate confidence intervals"""
    create_tool_header("Confidence Intervals", "Calculate confidence intervals for various parameters", "📏")

    interval_type = st.selectbox("Interval Type:", [
        "Mean (σ known)", "Mean (σ unknown)", "Proportion", "Difference of Means", "Difference of Proportions"
    ])

    if interval_type == "Mean (σ known)":
        st.markdown("### 📊 Confidence Interval for Mean (σ known)")

        col1, col2 = st.columns(2)
        with col1:
            sample_mean = st.number_input("Sample mean (x̄):", value=25.0)
            pop_std = st.number_input("Population std dev (σ):", min_value=0.01, value=5.0)
        with col2:
            n = st.number_input("Sample size (n):", min_value=1, value=30)
            confidence = st.selectbox("Confidence level:", [90, 95, 99], index=1)

        if st.button("Calculate CI for Mean"):
            alpha = 1 - confidence / 100
            z_critical = stats.norm.ppf(1 - alpha / 2)

            margin_error = z_critical * (pop_std / np.sqrt(n))
            ci_lower = sample_mean - margin_error
            ci_upper = sample_mean + margin_error

            st.success(f"**{confidence}% Confidence Interval: [{ci_lower:.4f}, {ci_upper:.4f}]**")
            st.write(f"Margin of error: ±{margin_error:.4f}")
            st.write(f"Critical z-value: ±{z_critical:.4f}")

    elif interval_type == "Mean (σ unknown)":
        st.markdown("### 📊 Confidence Interval for Mean (σ unknown)")

        col1, col2 = st.columns(2)
        with col1:
            sample_mean = st.number_input("Sample mean (x̄):", value=25.0, key="mean_unknown")
            sample_std = st.number_input("Sample std dev (s):", min_value=0.01, value=5.0)
        with col2:
            n = st.number_input("Sample size (n):", min_value=2, value=30, key="n_unknown")
            confidence = st.selectbox("Confidence level:", [90, 95, 99], index=1, key="conf_unknown")

        if st.button("Calculate CI for Mean (t-dist)"):
            alpha = 1 - confidence / 100
            df = n - 1
            t_critical = stats.t.ppf(1 - alpha / 2, df)

            margin_error = t_critical * (sample_std / np.sqrt(n))
            ci_lower = sample_mean - margin_error
            ci_upper = sample_mean + margin_error

            st.success(f"**{confidence}% Confidence Interval: [{ci_lower:.4f}, {ci_upper:.4f}]**")
            st.write(f"Margin of error: ±{margin_error:.4f}")
            st.write(f"Critical t-value: ±{t_critical:.4f} (df = {df})")

    elif interval_type == "Proportion":
        st.markdown("### 📊 Confidence Interval for Proportion")

        col1, col2 = st.columns(2)
        with col1:
            x = st.number_input("Number of successes (x):", min_value=0, value=60)
            n = st.number_input("Sample size (n):", min_value=1, value=100, key="prop_n")
        with col2:
            confidence = st.selectbox("Confidence level:", [90, 95, 99], index=1, key="prop_conf")

        if st.button("Calculate CI for Proportion"):
            p_hat = x / n
            alpha = 1 - confidence / 100
            z_critical = stats.norm.ppf(1 - alpha / 2)

            # Standard error
            se = np.sqrt(p_hat * (1 - p_hat) / n)
            margin_error = z_critical * se

            ci_lower = max(0, p_hat - margin_error)
            ci_upper = min(1, p_hat + margin_error)

            st.success(f"**{confidence}% Confidence Interval: [{ci_lower:.4f}, {ci_upper:.4f}]**")
            st.write(f"Sample proportion: {p_hat:.4f} = {p_hat * 100:.2f}%")
            st.write(f"Margin of error: ±{margin_error:.4f}")
            st.write(f"Standard error: {se:.4f}")