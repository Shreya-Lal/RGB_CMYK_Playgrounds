###################################################################################
#                       COLOR SPACE CONVERSION PLAYGROUND                         #
###################################################################################
# Author        : Shreya Lal                                                      #
# Version       : 0.3                                                             #
# Date          : 17/May/2023                                                     #
# Modified By   : Shreya Lal                                                      #
# Modified Date : 11/June/2025                                                    #
# File Name     : cmyk_app.py                                                     # 
###################################################################################

import streamlit as st

# Configure page
st.set_page_config(
    page_title="Color Space Converter",
    page_icon="🎨",
    layout="wide",
    initial_sidebar_state="expanded"
)

def rgb_to_hex(r, g, b):
    return "#{:02x}{:02x}{:02x}".format(r, g, b).upper()

def rgb_to_cmyk(r, g, b):
    if (r, g, b) == (0, 0, 0):
        return 0, 0, 0, 100
    
    r_prime = r / 255
    g_prime = g / 255
    b_prime = b / 255
    
    k = 1 - max(r_prime, g_prime, b_prime)
    c = (1 - r_prime - k) / (1 - k)
    m = (1 - g_prime - k) / (1 - k)
    y = (1 - b_prime - k) / (1 - k)
    
    return round(c*100, 2), round(m*100, 2), round(y*100, 2), round(k*100, 2)

def cmyk_to_rgb(c, m, y, k):
    c = c / 100
    m = m / 100
    y = y / 100
    k = k / 100
    
    r = 255 * (1 - c) * (1 - k)
    g = 255 * (1 - m) * (1 - k)
    b = 255 * (1 - y) * (1 - k)
    
    return round(r), round(g), round(b)

# Component preview helper functions
def red_component(r):
    return f'rgb({r}, 0, 0)'

def green_component(g):
    return f'rgb(0, {g}, 0)'

def blue_component(b):
    return f'rgb(0, 0, {b})'

def cyan_component(c):
    r, g, b = cmyk_to_rgb(c, 0, 0, 0)
    return f'rgb({r}, {g}, {b})'

def magenta_component(m):
    r, g, b = cmyk_to_rgb(0, m, 0, 0)
    return f'rgb({r}, {g}, {b})'

def yellow_component(y):
    r, g, b = cmyk_to_rgb(0, 0, y, 0)
    return f'rgb({r}, {g}, {b})'

def black_component(k):
    r, g, b = cmyk_to_rgb(0, 0, 0, k)
    return f'rgb({r}, {g}, {b})'

# App layout
# st.title("Color Space Converter")
# st.icon("🎨")
#st.title("RGB ↔ CMYK Conversion Visualizer")
st.markdown("<h1 style='text-align: center; color: blue;'>RGB ↔ CMYK Conversion Visualizer</h1>", unsafe_allow_html=True)
#st.markdown('<p style="color:blue;"> <b>Developed by : Shreya Lal</p>', unsafe_allow_html=True)
st.caption('<h4 style="text-align: right; color: green;">Developed by : Shreya Lal</h4>', unsafe_allow_html=True)
#st.caption('<div style="text-align: right; font-size: 20px; color: green;">Developed by : Shreya Lal</div>', unsafe_allow_html=True)

# Custom CSS to increase tab size
font_css = """
<style>
    button[data-baseweb="tab"] > div[data-testid="stMarkdownContainer"] > p {
        font-size: 24px;  /* Adjust the font size as needed */
    }
</style>
"""
st.write(font_css, unsafe_allow_html=True)

tab1, tab2 = st.tabs(["RGB to CMYK", "CMYK to RGB"])

with tab1:
    st.header("RGB to CMYK  to HEX Code Conversion")
    # Red slider with component preview
    r = st.slider("Red", 0, 255, 50, key="r")
    st.markdown(f"""
    <div style="display: flex; align-items: center; gap: 10px; margin-top: -15px; margin-bottom: 20px">
        <div style="width: 30px; font-size: 12px;">Preview:</div>
        <div style="height: 25px; width: 25%; background: {red_component(r)}; border: 1px solid #ddd; border-radius: 4px"></div>
        <div style="height: 25px; width: 25%; background: {green_component(0)}; border: 1px solid #ddd; border-radius: 4px; opacity: 0.3"></div>
        <div style="height: 25px; width: 25%; background: {blue_component(0)}; border: 1px solid #ddd; border-radius: 4px; opacity: 0.3"></div>
    </div>
    """, unsafe_allow_html=True)
    
    # Green slider with component preview
    g = st.slider("Green", 0, 255, 100, key="g")
    st.markdown(f"""
    <div style="display: flex; align-items: center; gap: 10px; margin-top: -15px; margin-bottom: 20px">
        <div style="width: 30px; font-size: 12px;">Preview:</div>
        <div style="height: 25px; width: 25%; background: {red_component(0)}; border: 1px solid #ddd; border-radius: 4px; opacity: 0.3"></div>
        <div style="height: 25px; width: 25%; background: {green_component(g)}; border: 1px solid #ddd; border-radius: 4px"></div>
        <div style="height: 25px; width: 25%; background: {blue_component(0)}; border: 1px solid #ddd; border-radius: 4px; opacity: 0.3"></div>
    </div>
    """, unsafe_allow_html=True)
    
    # Blue slider with component preview
    b = st.slider("Blue", 0, 255, 150, key="b")
    st.markdown(f"""
    <div style="display: flex; align-items: center; gap: 10px; margin-top: -15px; margin-bottom: 20px">
        <div style="width: 30px; font-size: 12px;">Preview:</div>
        <div style="height: 25px; width: 25%; background: {red_component(0)}; border: 1px solid #ddd; border-radius: 4px; opacity: 0.3"></div>
        <div style="height: 25px; width: 25%; background: {green_component(0)}; border: 1px solid #ddd; border-radius: 4px; opacity: 0.3"></div>
        <div style="height: 25px; width: 25%; background: {blue_component(b)}; border: 1px solid #ddd; border-radius: 4px"></div>
    </div>
    """, unsafe_allow_html=True)
    
    c, m, y, k = rgb_to_cmyk(r, g, b)
    hex_code = rgb_to_hex(r, g, b)
    
    st.success(f"CMYK Values: C={c}%, M={m}%, Y={y}%, K={k}%")
    
    # Color display
    st.divider()
    st.header("Color Preview")
    st.markdown(
        f'<div style="height: 150px; background: rgb({r},{g},{b}); border-radius: 10px"></div>',
        unsafe_allow_html=True
    )
    #st.caption(f"RGB: ({r}, {g}, {b}) → CMYK Values: (C={c}%, M={m}%, Y={y}%, K={k}%)")
    st.markdown(
    f"""
    <p style="text-align: center; color: green; font-size: 16px;">
        RGB Values: ({r}, {g}, {b}) → CMYK Values: (C={c}%, M={m}%, Y={y}%, K={k}%)
    </p>
    """, 
    unsafe_allow_html=True
)

    # st.markdown(
    #     f'<div style="height: 150px; background: {hex_code}; border-radius: 10px"></div>',
    #     unsafe_allow_html=True
    # )
    
    # HEX display with color box
    st.subheader("HEX Code")
    st.code(hex_code, language="text")
    st.markdown(
        f'<div style="display: inline-block; padding: 0.5em; background: {hex_code}; '
        f'border: 1px solid #ccc; border-radius: 5px; margin-right: 10px;"></div>'
        f'<div style="display: inline-block; font-family: monospace; font-size: 1.2em;">{hex_code}</div>',
        unsafe_allow_html=True
    )

with tab2:
    st.header("CMYK to RGB  to HEX Code Conversion")
    # Cyan slider with component preview
    c_val = st.slider("Cyan", 0.0, 100.0, 25.0, key="c")
    st.markdown(f"""
    <div style="display: flex; align-items: center; gap: 10px; margin-top: -15px; margin-bottom: 20px">
        <div style="width: 30px; font-size: 12px;">Preview:</div>
        <div style="height: 25px; width: 25%; background: {cyan_component(c_val)}; border: 1px solid #ddd; border-radius: 4px"></div>
        <div style="height: 25px; width: 25%; background: {magenta_component(0)}; border: 1px solid #ddd; border-radius: 4px; opacity: 0.3"></div>
        <div style="height: 25px; width: 25%; background: {yellow_component(0)}; border: 1px solid #ddd; border-radius: 4px; opacity: 0.3"></div>
        <div style="height: 25px; width: 25%; background: {black_component(0)}; border: 1px solid #ddd; border-radius: 4px; opacity: 0.3"></div>
    </div>
    """, unsafe_allow_html=True)
    
    # Magenta slider with component preview
    m_val = st.slider("Magenta", 0.0, 100.0, 50.0, key="m")
    st.markdown(f"""
    <div style="display: flex; align-items: center; gap: 10px; margin-top: -15px; margin-bottom: 20px">
        <div style="width: 30px; font-size: 12px;">Preview:</div>
        <div style="height: 25px; width: 25%; background: {cyan_component(0)}; border: 1px solid #ddd; border-radius: 4px; opacity: 0.3"></div>
        <div style="height: 25px; width: 25%; background: {magenta_component(m_val)}; border: 1px solid #ddd; border-radius: 4px"></div>
        <div style="height: 25px; width: 25%; background: {yellow_component(0)}; border: 1px solid #ddd; border-radius: 4px; opacity: 0.3"></div>
        <div style="height: 25px; width: 25%; background: {black_component(0)}; border: 1px solid #ddd; border-radius: 4px; opacity: 0.3"></div>
    </div>
    """, unsafe_allow_html=True)
    
    # Yellow slider with component preview
    y_val = st.slider("Yellow", 0.0, 100.0, 75.0, key="y")
    st.markdown(f"""
    <div style="display: flex; align-items: center; gap: 10px; margin-top: -15px; margin-bottom: 20px">
        <div style="width: 30px; font-size: 12px;">Preview:</div>
        <div style="height: 25px; width: 25%; background: {cyan_component(0)}; border: 1px solid #ddd; border-radius: 4px; opacity: 0.3"></div>
        <div style="height: 25px; width: 25%; background: {magenta_component(0)}; border: 1px solid #ddd; border-radius: 4px; opacity: 0.3"></div>
        <div style="height: 25px; width: 25%; background: {yellow_component(y_val)}; border: 1px solid #ddd; border-radius: 4px"></div>
        <div style="height: 25px; width: 25%; background: {black_component(0)}; border: 1px solid #ddd; border-radius: 4px; opacity: 0.3"></div>
    </div>
    """, unsafe_allow_html=True)
    
    # Black slider with component preview
    k_val = st.slider("Black (Key)", 0.0, 100.0, 25.0, key="k")
    st.markdown(f"""
    <div style="display: flex; align-items: center; gap: 10px; margin-top: -15px; margin-bottom: 20px">
        <div style="width: 30px; font-size: 12px;">Preview:</div>
        <div style="height: 25px; width: 25%; background: {cyan_component(0)}; border: 1px solid #ddd; border-radius: 4px; opacity: 0.3"></div>
        <div style="height: 25px; width: 25%; background: {magenta_component(0)}; border: 1px solid #ddd; border-radius: 4px; opacity: 0.3"></div>
        <div style="height: 25px; width: 25%; background: {yellow_component(0)}; border: 1px solid #ddd; border-radius: 4px; opacity: 0.3"></div>
        <div style="height: 25px; width: 25%; background: {black_component(k_val)}; border: 1px solid #ddd; border-radius: 4px"></div>
    </div>
    """, unsafe_allow_html=True)
    
    r, g, b = cmyk_to_rgb(c_val, m_val, y_val, k_val)
    hex_code = rgb_to_hex(r, g, b)
    
    st.success(f"RGB Values: R={r}, G={g}, B={b}")
    
    # Color display
    st.divider()
    st.header("Final Color Preview")
    st.markdown(
        f'<div style="height: 150px; background: rgb({r},{g},{b}); border-radius: 10px"></div>',
        unsafe_allow_html=True
    )
    #st.caption(f"CMYK: ({c}%, {m}%, {y}%, {k}%)")
    st.markdown(
    f"""
    <p style="text-align: center; color: green; font-size: 16px;">
        CMYK Values: (C={c_val}%, M={m_val}%, Y={y_val}%, K={k_val}%) → RGB: ({r}, {g}, {b})
    </p>
    """, 
    unsafe_allow_html=True
)


    # st.markdown(
    #     f'<div style="height: 150px; background: {hex_code}; border-radius: 10px"></div>',
    #     unsafe_allow_html=True
    # )
    
    # HEX display with color box
    st.subheader("HEX Code")
    st.code(hex_code, language="text")
    st.markdown(
        f'<div style="display: inline-block; padding: 0.5em; background: {hex_code}; '
        f'border: 1px solid #ccc; border-radius: 5px; margin-right: 10px;"></div>'
        f'<div style="display: inline-block; font-family: monospace; font-size: 1.2em;">{hex_code}</div>',
        unsafe_allow_html=True
    )

    # Add some styling
st.markdown("""
    <style>
    div[data-baseweb="slider"] {
        margin-bottom: 5px;
    }
    .stSlider {
        margin-bottom: 5px;
    }
    </style>
""", unsafe_allow_html=True)

    # ====================
    # Theoretical Section
    # ====================
with st.expander("📚 Basic Explanation & Resources"):
        st.markdown("""
# RGB to CMYK Conversion Explained Simply 🌈➡️🖨️
### Step 1: Understanding RGB and CMYK

- RGB (Red, Green, Blue) is used for screens (like computers, TVs, phones). It's an additive color model: when you add all colors together, you get white.
- CMYK (Cyan, Magenta, Yellow, Key/Black) is used for printing. It's a subtractive color model (ink absorbs light): when you mix all colors, you get a dark brown (not true black), so we add a separate black (Key) to get true black and save ink.

### Step 2: Why Convert RGB to CMYK?
#### Screens vs. Paper:
- RGB colors are brighter because screens emit light. Ink on paper (printed materials) reflects light, so some RGB colors can’t be printed accurately (e.g., neon green).So the color models must be different.
- Avoid Surprises: An image that looks vibrant on screen might look dull in print if not converted first.
- Printer Requirements: Printers use physical CMYK inks, not light. They need separate instructions for each ink.
- RGB has a wider color range (gamut) than CMYK. Some bright RGB colors cannot be printed with CMYK inks. So we convert to avoid unexpected color shifts.

### Step 3: How Conversion Works 

- The conversion involves mathematical formulas to translate RGB values to CMYK percentages.
- Generally, we first convert RGB to CMY (Cyan, Magenta, Yellow) and then adjust to include black (K) and reduce the other inks.

#### Basic Conversion Steps:

1. Normalize the RGB values (0-255) to 0-1 range.
    - Example: R=255 becomes 1.0, R=0 becomes 0. 

2. Convert RGB to CMY: Each RGB color is "subtracted" from white:
    - Cyan = 1 - Red
    - Magenta = 1 - Green
    - Yellow = 1 - Blue

    🖨️ Example: Pure Red (RGB: 255, 0, 0) → Cyan = 0%, Magenta = 100%, Yellow = 100%.

3. Now, to introduce black (K):
We take the minimum of (C, M, Y) and set that as the black component (K). Then subtract that K value from each of C, M, Y to get the new values.

###### Why? 
- CMY alone makes muddy darks. Black ink (K) is added to make richer shadows and text.
- Because black can replace the common part of CMY to save ink and get a better black.
Example: Dark gray → Made with K only (not CMY mix).

🌟 Example:

Let's say we have: 

- C = 0.2, M = 0.5, Y = 0.3 -> then K = min(0.2,0.5,0.3)=0.2

Then subtract 0.2 from each: 

- C_new = 0.2 - 0.2 = 0
- M_new = 0.5 - 0.2 = 0.3
- Y_new = 0.3 - 0.2 = 0.1

So the CMYK is (0, 0.3, 0.1, 0.2) 

> But note: There are different methods (like using black generation and undercolor removal) and the actual conversion is more complex, but this is the basic idea.

### Step 4: Why Split into 4 Channels?

- In printing, we use four separate plates or passes (ink cartridges) for each color: one for Cyan, one for Magenta, one for Yellow, and one for Black.
Each channel is a "layer":
- The printer combines tiny dots of each ink to create all colors.

 🎨 Example:
- Green = Cyan + Yellow (no Magenta/Black).
- Deep Brown = All 4 inks in varying amounts.

- Each channel in CMYK represents the amount of that particular ink to be applied.
- By splitting, the printer can apply each ink in the right amount to create the desired color by overlaying these inks.
-Splitting ensures:
	- Precise ink control (no wasted ink).
	- Sharper details (e.g., text uses pure black)

### Step 5: How Printing Uses CMYK  🖨️
1. Separate the Image:
- The design is split into 4 grayscale layers (one per channel):
	- Cyan layer: Where cyan ink goes.
	- Magenta layer: Where magenta ink goes.
	- Yellow layer: Where yellow ink goes.
	- Black layer: Where black ink goes.

2. The printer lays down tiny dots of each ink (C, M, Y, K) in varying amounts and patterns (halftoning) to create the illusion of a full range of colors.
Halftoning:
- Each layer uses tiny dots (varying size/spacing) to simulate shades.
	- Example: 50% gray = 50% dots, 50% blank paper.

3. The dots are so small that the human eye blends the colors together.
Overlay Inks:
Paper passes through 4 rollers (C→M→Y→K). Dots blend optically:
👁️ Human eyes mix colors (e.g., Cyan + Yellow dots = Green).

4. The black (K) is used for text, deep shadows, and to reduce the total ink (so we don't waste CMY inks to make black).

Example: 

- If you want to print a green leaf, the printer might use a lot of cyan and yellow, a little magenta (or none) and no black.
- For a dark shadow, it might use all four inks but with more black.

### Step 6. Real-Life Example 🍎
- RGB "Bright Red" (255, 0, 0) on screen:
- Converted to CMYK: ≈ Cyan 0%, Magenta 100%, Yellow 100%, Black 0%.

------

> **Important Note:**  Because CMYK has a smaller color gamut than RGB, some colors (like very bright greens or blues) might look less vibrant when printed. Designers use color profiles and proofing to adjust.

#### Key Takeaways ✅

- RGB is for light (Light-based) → Digital screens.
- CMYK is for ink (Ink-based) → Printing. 
- We convert because printers use CMYK inks and we want the printed colors to be as close as possible to what we see on screen.
- We split into 4 channels because the printer uses 4 separate inks and each channel tells how much of that ink to put on the paper.
- The conversion process tries to match the color and also save ink by replacing overlapping CMY with black.
- Printers need separate instructions for each ink (C, M, Y, K) to layer them precisely.

💡 **Pro Tip:** Always design in CMYK for print projects!
Tools like Photoshop show a "CMYK Preview" to simulate printed colors.

------
                """)
        
        st.markdown("""
                    **Recommended Tutorials:**
                    - [CMYK Explanation](https://www.epackprinting.com/support/understanding-cmyk/)
                    - [Shreya's RGB to CMYK Conversion](https://github.com/Shreya-Lal/Image_Processing_using_OpencCV_Python/blob/main/Image_Processing_Fundamentals/color_conversion_python_scratch/RGB2CMYK.ipynb)
                 """)
        
st.markdown("<br><br>", unsafe_allow_html=True)

# Footer section
st.markdown("""
        <hr style="border:1px solid #ccc">
        <p style="text-align:center;">Powered by Streamlit | Developed by <strong>Shreya Lal</strong></p>
    """, unsafe_allow_html=True)
    