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
    st.caption(f"RGB: ({r}, {g}, {b})")
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
    
    r, g, b = cmyk_to_rgb(c, m, y, k)
    hex_code = rgb_to_hex(r, g, b)
    
    st.success(f"RGB Values: R={r}, G={g}, B={b}")
    
    # Color display
    st.divider()
    st.header("Final Color Preview")
    st.markdown(
        f'<div style="height: 150px; background: rgb({r},{g},{b}); border-radius: 10px"></div>',
        unsafe_allow_html=True
    )
    st.caption(f"CMYK: ({c}%, {m}%, {y}%, {k}%)")

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