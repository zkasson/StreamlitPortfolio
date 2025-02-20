import streamlit as st
from streamlit_option_menu import option_menu
import geopandas as gpd
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import leafmap.foliumap as leafmap
import folium
from folium import CircleMarker
from arcgis.gis import GIS
from arcgis import GeoAccessor, GeoSeriesAccessor
from streamlit_folium import st_folium

gis = GIS()

# Set up main configuration 
st.set_page_config(page_title='Zack Kasson - Portfolio', layout='wide')

# hide_decoration_bar_style = '''
#     <style>
#         header {visibility: hidden;}
#     </style>
# '''
# st.markdown(hide_decoration_bar_style, unsafe_allow_html=True)

# # # # # # # # # # # 
# # #   CUSTOM   # # #
# # # NAVIGATION # # #
# # #    BAR    # # #
# # # # # # # # # # # 

# Custom CSS to make the navigation bar full-width
custom_css = """
<style>
    .block-container {
        padding: 2.9rem;
        }

"""
# Inject custom CSS
st.markdown(custom_css, unsafe_allow_html=True)

# Top navigation bar
selected = option_menu(
    None, ["Home", "About", "Spatial CV", "Projects","Contact"],
    icons=['house', 'person-raised-hand', "globe-americas", 'journal-code','person-rolodex'],
    menu_icon="cast", default_index=0, orientation="horizontal",
    styles={
        "container": {"padding": "0!important", "background-color": "#8D8E8E"},
        "icon": {"color": "#F9DB6D", "font-size": "29px"},
        "nav-link": {"font-size": "25px", "text-align": "left", "margin": "0px", "--hover-color": "#eee"},
        "nav-link-selected": {"background-color": "#475B5A"},
    }
)


# # # # # # # # #
# # # HOME # # #
# # # PAGE # # #
# # # # # # # # #

if selected == "Home":
    st.markdown('''<h1 style='text-align: center; color: grey; font-size: 160px; font-family: \"Impact\", sans-serif; line-height: 1; 
                letter-spacing: 1rem; margin-bottom: 5px; padding-bottom: 0px;'>ZACK<br>KASSON</h1>'''
                , unsafe_allow_html=True)
    st.markdown('''<h1 style='text-align: center; color: grey; font-size: 18px; line-height: 1.2; font-family: "Roboto", sans-serif;
                 margin-top: 5px; padding-top: 0px;'>Spatial Analysis ● GIS Tool Developement ● Data Engineering</h1>''',
                 unsafe_allow_html=True)
    st.markdown("<img src='https://github.com/zkasson/StreamlitPortfolio/blob/main/Pictures/IMG_0463%20(2).jpg?raw=true' width='700' style='display: block; margin: 0 auto; border-radius: 20px;'>" , unsafe_allow_html=True)

# # # # # # # # #
# # # ABOUT # # #
# # # PAGE # # #
# # # # # # # # #
elif selected == "About":
    about_intro = "Hi! Thanks for visiting my portfolio! I am a dynamic and dedicated GIS professional with a deep passion for the intersection of technology and the natural world. Growing up near Cuyahoga Valley National Park, I developed a lasting love for nature and our connection with it. Coming from a family of technology professionals, I was naturally drawn to integrating technology to enhance and elevate my interests."
    about_intro2 ="As an avid climber, I started creating maps and analyzing LiDAR data to navigate remote walls and explore new climbing areas. The success of these projects fueled my drive to continue integrating technology with my love for nature and geography."
    
    
    st.markdown(
            f"<div style='text-align: left; color: grey; margin: 0 auto; margin-top: 40px; max-width: 1200px; margin-bottom: 20px; font-size: 26px; font-family: 'Roboto', sans-serif;'>{about_intro}<br><br>{about_intro2}</div>",
            unsafe_allow_html=True
        )
    about_title = "Words That Describe Me"
    st.markdown(f'''<h1 style='text-align: center; color: #F9DB6D; font-size: 48px; font-family: \"Impact\", sans-serif; line-height: 1; 
                letter-spacing: .4rem; margin-bottom: 80px; margin-top: 20px; padding-bottom: 0px;'>{about_title}</h1>'''
                , unsafe_allow_html=True)
    

    hobbyist_text = "Outside of work, I enjoy staying active outdoors. My main passion is climbing—I love its simplicity and the physical and mental challenges it brings. Strangely, much of my personal growth parallels lessons I’ve learned through climbing. I also enjoy surfing, reading memoirs, wildlife viewing, photography, traveling, and, most importantly, spending time with friends and family."
    curious_text = "I’m a naturally curious person—there’s no topic I don’t find interesting enough to explore further. My friends often tease me for “googling too much,” but it’s a habit that has fueled my ability to learn technical skills independently. I first discovered the value of self-teaching during my freshman calculus class, where my professor announced there would be no lectures, only recitations to ask questions. Though intimidating at first, this experience taught me how to learn on my own and sparked my curiosity. I realized that, with determination and the right resources, I could teach myself nearly anything. Living in an age where all the information I need is just a search away is something I’m incredibly grateful for. My curiosity and self-reliance have become defining traits. They drive me to seek out new knowledge, skills, and perspectives, always with the intent of applying what I learn."
    
    # Two columns 
    col1, col2 = st.columns(2)
    with col1:
        st.markdown(
            "<img src='https://github.com/zkasson/StreamlitPortfolio/blob/main/Pictures/IMG_3670.jpg?raw=true' width='700' style='display: block; margin: 10px auto; border-radius: 20px;'>",
            unsafe_allow_html=True
        )
        st.markdown("<p style='text-align: center; color: #F9DB6D; margin-bottom: 20px; margin-top: 20px;font-size: 36px; font-family: \"Impact\", sans-serif;'>Curious</p>", unsafe_allow_html=True)
        st.markdown(
            f"<div style='text-align: center; color: grey; margin: 0 auto; max-width: 700px;font-size: 26px; font-family: 'Roboto', sans-serif;'>{curious_text}</div>",
            unsafe_allow_html=True
        )

    with col2:
        st.markdown("<p style='text-align: center; color: #F9DB6D; margin-bottom: 20px; margin-top: 10px; font-size: 36px; font-family: \"Impact\", sans-serif;'>Hobbyist</p>", unsafe_allow_html=True)
        st.markdown(
            f"<div style='text-align: center; color: grey; margin: 0 auto; max-width: 700px;font-size: 26px; font-family: 'Roboto', sans-serif;'>{hobbyist_text}</div>",
            unsafe_allow_html=True
        )
        st.markdown(
            "<img src='https://github.com/zkasson/StreamlitPortfolio/blob/main/Pictures/zack%20graduation%20(3).jpg?raw=true' width='500' style='display: block; margin: 10px auto; margin-top: 40px; border-radius: 20px;'>",
            unsafe_allow_html=True
        )


# # # # # # # # #
# # # RESUME # # #
# # # PAGE # # #
# # # # # # # # #

elif selected == "Spatial CV":
    # Sidebar 
    st.sidebar.subheader("Click 'Next' to flip through my experience")
    basemap_selection = st.sidebar.selectbox('Select a basemap', ['openstreetmap','CartoDB.DarkMatter', 'CartoDB.Positron'])

    # Counter to track the current entry
    if 'counter' not in st.session_state:
        st.session_state.counter = 0
    col1, col2 = st.sidebar.columns([1, 1])  # Two buttons side-by-side

    if col1.button('Back'):
        st.session_state.counter += 1
        if st.session_state.counter >= 11:  # Reset after the last item
            st.session_state.counter = 0

    if col2.button('Next'):
        st.session_state.counter -= 1
        if st.session_state.counter <= -1:  # Reset to last item if underflow occurs
            st.session_state.counter = 10  

    # Read the GeoJSON file

    def read_json(url):
        return gpd.read_file(url)

    json_file = r'https://raw.githubusercontent.com/zkasson/StreamlitPortfolio/refs/heads/main/digitalResume.geojson'
    state_json = r'https://raw.githubusercontent.com/zkasson/StreamlitPortfolio/refs/heads/main/US_States%20(1).json'
    gdf = read_json(json_file)
    state_gdf = read_json(state_json)


    # Two columns 
    col1, col2 = st.columns(2)
    

    # If counter is 0, show all points from the GeoDataFrame (gdf)
    if st.session_state.counter == 0:
        #Create a column with the text if the counter is zero   
        spatial_cv_text = "If you’re anything like me, it helps to see things spatially! This is a quick web app I built to showcase some of my previous experiences on a map. I’m a firm believer that our experiences and the lessons we learn are often unique to the locations where they occur, and this tool helps illustrate the connection I’ve had with each of those experiences."
        with col1:
            st.markdown("<p style='text-align: center; color: #F9DB6D; margin-bottom: 20px; margin-top: 20px;font-size: 36px; font-family: \"Impact\", sans-serif;'>Our experiences are spatial!</p>", unsafe_allow_html=True)
            st.markdown(
                f"<div style='text-align: center; color: grey; margin: 0 auto; max-width: 700px;font-size: 26px; font-family: 'Roboto', sans-serif;'>{spatial_cv_text}</div>",
                unsafe_allow_html=True
            )
        

        # Get the bounds of the entire dataset
        bounds = gdf.total_bounds  # minx, miny, maxx, maxy
        center = [(bounds[1] + bounds[3]) / 2, (bounds[0] + bounds[2]) / 2]
        zoom_level = 3  

        # Create and display the map
        map = leafmap.Map(
        layers_control=True,
        draw_control=False,
        measure_control=False,
        fullscreen_control=False,
        center=center,
        zoom=zoom_level)

        # Add points for all locations
        for idx, row in gdf.iterrows():
            icon_name = row['Icon']
            coordinates = row.geometry.coords[0][::-1]  # Extract lat/lon

            # Use a folium DivIcon to create a pin-like marker
            folium.Marker(
                location=coordinates,
                icon=folium.DivIcon(
                    html=f"""
                    <div style="
                        position: relative;
                        width: 36px; height: 36px;
                        background: gray;
                        border-radius: 50%; /* Make it a circle */
                        box-shadow: 0 2px 6px rgba(0,0,0,0.2); /* Add a subtle shadow */
                        display: flex;
                        align-items: center;
                        justify-content: center;
                        transform: translate(-50%, -50%);
                    ">
                        <i class="fa fa-{icon_name}" style="font-size: 18px; color: white;"></i>
                    </div>
                    """
                ),
                popup=f"<b>{row['Name']}</b><br>{row['Description']}"
            ).add_to(map)
    else:
        # Display the current location based on the counter
        current_id = st.session_state.counter 
        current_location = gdf[gdf['ID'] == current_id]
        current_location_name = current_location['Name'].iloc[0]
        current_location_desc = current_location['Description'].iloc[0]
        current_location_exp = current_location['Experience'].iloc[0]
        current_location_zoom = float(current_location['zoom'].iloc[0]) 
        current_icon = current_location['Icon'].iloc[0]

        with col1:
            # Display details
            st.markdown(f"<p style='text-align: center; color: #F9DB6D; margin-bottom: 20px; margin-top: 20px;font-size: 36px; font-family: \"Impact\", sans-serif;'>{current_location_name}</p>", unsafe_allow_html=True)
            st.markdown(
                f"<div style='text-align: left; color: grey; margin: 0 auto; max-width: 700px;font-size: 26px; font-family: 'Roboto', sans-serif;'>{current_location_desc}</div>",
                unsafe_allow_html=True
            )
            st.write(' ')
            st.markdown(
                f"<div style='text-align: left; color: grey; margin: 0 auto; max-width: 700px;font-size: 26px; font-family: 'Roboto', sans-serif;'>I learned {current_location_exp}</div>",
                unsafe_allow_html=True
            )
        

        # Create and display the map
        map = leafmap.Map(
        layers_control=True,
        draw_control=False,
        measure_control=False,
        fullscreen_control=False,
        center=current_location.geometry.iloc[0].coords[0][::-1],
        zoom=current_location_zoom)

        # Add a single point for the current location
        for idx, row in current_location.iterrows():
            icon_name = row['Icon']
            coordinates = row.geometry.coords[0][::-1]  # Extract lat/lon

            # Use a folium DivIcon to create a pin-like marker
            folium.Marker(
                location=coordinates,
                icon=folium.DivIcon(
                    html=f"""
                    <div style="
                        position: relative;
                        width: 36px; height: 36px;
                        background: gray;
                        border-radius: 50%; /* Make it a circle */
                        box-shadow: 0 2px 6px rgba(0,0,0,0.2); /* Add a subtle shadow */
                        display: flex;
                        align-items: center;
                        justify-content: center;
                        transform: translate(-50%, -50%);
                    ">
                        <i class="fa fa-{icon_name}" style="font-size: 18px; color: white;"></i>
                    </div>
                    """
                ),
                popup=f"<b>{row['Name']}</b><br>{row['Description']}"
            ).add_to(map)

    #Add basemap
    map.add_basemap(basemap_selection)

    # Add state boundaries with a bold style
    map.add_gdf(
        gdf=state_gdf,
        layer_name='State Boundaries',
        style={
            'color': 'black',      
            'weight': .5,   
            'fill': False      
        },
        zoom_to_layer=False,
        info_mode=None  
    )

    with col2:
        st_folium(map, width=900, height=700)


# # # # # # # # #
# # # PROJECTS # # #
# # # PAGE # # #
# # # # # # # # #

elif selected == "Projects":
    # Define the project dictionary with keys as IDs and values as project names
    projects_dict = {
        0: "Website",
        1: "WildFire Dashboard",
        2: "Python Map",
        3: "Python Vizualization",
        4: "Open Source Surface Model",
        5: "ESRI Dashboard",
        6: "Web Developement",
        7: "Upcoming Projects"
    }

 

    # Sidebar content
    with st.sidebar:
        st.markdown('''<h1 style='text-align: left; color: grey; font-size: 25px;
                letter-spacing: .5rem; margin-bottom: 5px; padding-bottom: 0px;'>Select Project</h1>'''
                , unsafe_allow_html=True)


        # Render the option_menu using the updated project index
        project = option_menu(
            None,
            list(projects_dict.values()),  
            icons=["code", "map", "map", "code","map", "map", "code", "code"],
            menu_icon="cast",
            default_index=0,  # Use current for default index
            styles={
                "container": {"background-color": "black"},
                "icon": {"color": "white"},
                "nav-link": {"--hover-color": "#475B5A"},
                "nav-link-selected": {"background-color": "black","color": "#F9DB6D"},
                "nav-link-selected-icon": {"color": "#F9DB6D"},
            }
        )


        
    # # # Website # # #
    # # # Project # # #
    if project == "Website":
        st.markdown(f'''<h1 style='text-align: center; color: grey; font-size: 45px;
                letter-spacing: .5rem; margin-bottom: 5px; padding-bottom: 0px;'>{project}</h1>'''
                , unsafe_allow_html=True)
        website_desc = "I built this website from scratch, writing over 1,000 lines of code to bring it to life. It incorporates numerous Python libraries, including streamlit, geopandas, pandas, matplotlib, matplotlib.pyplot, leafmap, folium, and arcgis, to name a few."
        website_desc2 = "Additionally, I’ve incorporated JavaScript, CSS, and HTML to enhance functionality and design. This project showcases my ability to code and integrate spatial concepts, such as spatial joins and visualizations, into a user-friendly interface."
        website_desc3 = "You can take a look at the GitHub repository for the code"
        st.markdown(
            f"""
            <div style='text-align: left; color: grey; margin: 0 auto; margin-top: 40px; max-width: 1200px; margin-bottom: 20px; font-size: 26px; font-family: "Roboto", sans-serif;'>
                {website_desc}<br><br>
                {website_desc2}<br><br>
                {website_desc3} <a href='https://github.com/zkasson/StreamlitPortfolio/tree/main' style='color: blue; text-decoration: none;'>here</a>
            </div>
            """,
            unsafe_allow_html=True
            )
    # # # Wildfire # # #
    # # # Project # # #
    elif project == "WildFire Dashboard":
        st.markdown(f'''<h1 style='text-align: center; color: grey; font-size: 45px; 
                letter-spacing: .5rem; margin-bottom: 5px; padding-bottom: 0px; padding-right: 250px;'>{project}</h1>'''
                , unsafe_allow_html=True)
        # # # Set Up SideBar Selection # # #
        with st.sidebar:
            area_option = ["Canadian Wildfires","US Wildfires"]
            area_selection = st.sidebar.segmented_control(
                "**Area Selction**", area_option, selection_mode="single"
            )


        # # # Canadian Wildfires # # # 
        if area_selection == 'Canadian Wildfires':
            with st.sidebar:
                st.markdown('''<p style='text-align: center; 
                         color: #F9DB6D; 
                         font-size: 16px; 
                         background-color: rgba(249, 219, 109, 0.1);
                         letter-spacing: .1rem; 
                         margin-bottom: 0px; 
                         padding-bottom: 6px; 
                         padding-top: 6px; 
                         margin-bottom: 15px; 
                         margin-top: 5px; 
                         border-radius: 20px;
                         border: 2px solid #F9DB6D;' >
                Explore Active Wildfire in Canada
            </p>''', 
            unsafe_allow_html=True)

                # Dictionary to map agency codes to province names
            agency_to_province = {
                'ab': 'Alberta',
                'bc': 'British Columbia',
                'mb': 'Manitoba',
                'nb': 'New Brunswick',
                'nl': 'Newfoundland and Labrador',
                'ns': 'Nova Scotia',
                'on': 'Ontario',
                'pe': 'Prince Edward Island',
                'nt': 'Northwest Territories',
                'qc': 'Quebec',
                'sk': 'Saskatchewan',
                'yt': 'Yukon'
            }
            @st.cache_data
            def read_fl(item_id):
                living_atlas_item = gis.content.get(item_id)
                feature_layer = living_atlas_item.layers[0]
                sdf = feature_layer.query(where="1=1", out_sr=4326).sdf
                return sdf
            @st.cache_data
            def read_json(url):
                provs_gdf = gpd.read_file(url)
                return provs_gdf


            # Retrieve Wildfire layer and create SDF & Retrieve territories layer and create SDF
            item_id = "21638fcd54d14a25b6f1affdef812146"
            json_file = 'https://raw.githubusercontent.com/zkasson/StreamlitPortfolio/refs/heads/main/CanadaProvinces%20(1).geojson'
            wildfire_sdf = read_fl(item_id)
            provs_gdf = read_json(json_file)

            # Filter and create Province column, Map from agency to province
            canada_wildfire_sdf = wildfire_sdf[(wildfire_sdf['Agency'] != 'conus') & (wildfire_sdf['Agency'] != 'ak')]
            canada_wildfire_sdf['Province'] = wildfire_sdf['Agency'].map(agency_to_province)
            canada_wildfire_sdf = canada_wildfire_sdf.drop(columns=['Agency'])


            # Create dropdown for provinces and basemaps
            provinces = provs_gdf['Province'].unique()
            with st.sidebar:
                province = st.sidebar.selectbox('Select a Province', provinces)
                basemap_selection = st.sidebar.selectbox('Select a basemap', ['CartoDB.Positron', 'CartoDB.DarkMatter', 'openstreetmap'])


            # Map different stages of control
            stage_of_control_mapping = {
                'BH': 'Being Held',
                'OC': 'Out of Control',
                'UC': 'Under Control',
                'Pre': 'Prescribed'
            }
            canada_wildfire_sdf['Stage_of_Control'] = canada_wildfire_sdf['Stage_of_Control'].replace(stage_of_control_mapping)
            bh_color = '#ffff00'
            oc_color = '#ff0000'
            uc_color = '#008000'
            pre_color = "#ffffff"

            # Group by Province and Stage_of_Control, then sum Hectares__Ha_
            area_sdf = canada_wildfire_sdf.groupby(['Province', 'Stage_of_Control'])['Hectares__Ha_'].sum().reset_index()
            area_sdf = area_sdf.pivot(index='Province', columns='Stage_of_Control', values='Hectares__Ha_').fillna(0)
            area_sdf.columns.name = None

            # Create unit variable and engineer data to use correct unit
            with st.sidebar:
                unit = st.sidebar.radio(
                    "Select a Unit",
                    ['Hectares', 'Acres']
                )
            conversion_factor = 2.47105
            def correct_unit(area_sdf,unit_df):
                if unit_df == 'Hectares':  
                    area_final = area_sdf 
                    return area_final
                elif unit_df == 'Acres':
                    area_final = area_sdf
                    columns_to_convert = ['Prescribed', 'Being Held', 'Out of Control', 'Under Control']
                    for col in columns_to_convert:
                        if col in area_final.columns:
                            area_final[col] = area_final[col] * conversion_factor
                    return area_final
                else:
                    # Handle unexpected unit cases
                    raise ValueError(f"Unsupported unit: {unit_df}")
            area_final = correct_unit(area_sdf,unit)


            # Dynamically select only the columns present in the DataFrame
            available_columns = [col for col in ['Being Held', 'Out of Control', 'Prescribed', 'Under Control'] if col in area_final.columns]
            area_final = area_final.reset_index().melt(id_vars=['Province'], 
                                                            value_vars=available_columns,
                                                            var_name='Stage_of_Control', 
                                                            value_name='Area')

            # Filter data for the selected province
            area_final = area_final[area_final['Province'] == province]

            no_fires_bool = area_final['Area'].dropna().empty
            if no_fires_bool:
                rounded_upper_limit =5000
            else:
                # Calculate the upper limit for the y-axis
                max_sh = area_final['Area'].max()  # Find the max value in the area column
                upper_limit = max_sh + (max_sh/10) 
                rounded_upper_limit = round(upper_limit / 100) * 100 if upper_limit > 99 else 100


            if no_fires_bool:
                with st.sidebar:
                    st.sidebar.write(f'**There are no ongoing fires in {province}**')
            else:
                # # # Create Chart # # # 
                colors = {
                    "Being Held": "orange",
                    "Out of Control": "red",
                    "Under Control": "green",
                    "Prescribed": "yellow"  
                }
                area_final["Color"] = area_final["Stage_of_Control"].map(colors)

                # Create the plot
                fig, ax = plt.subplots(1, 1,dpi=100)
                bars = ax.bar(
                    area_final["Stage_of_Control"],
                    area_final["Area"],
                    color=area_final["Color"]
                )

                # Customize the plot
                ax.set_ylabel(f'Area ({unit})')
                ax.set_xlabel('Control Stage')
                ax.set_title(f'{unit} of fire within {province}')
                ax.set_ylim(0, rounded_upper_limit)

                ax.yaxis.set_major_formatter(matplotlib.ticker.StrMethodFormatter("{x:,.0f}"))

                for bar, area in zip(bars, area_final["Area"]):
                    ax.text(
                        bar.get_x() + bar.get_width() / 2,  # x-coordinate
                        bar.get_height() + rounded_upper_limit * 0.02,  # y-coordinate
                        f'{area:,.0f} {unit}', 
                        ha='center',  
                        va='bottom',  
                        fontsize=10  
                    )
                # Display the plot within sidebar
                plt.tight_layout()
                with st.sidebar:
                    stats = st.sidebar.pyplot(fig, use_container_width=True)


            # # # M A P # # #
            # # # Create the map for Canadian Wildfires # # #
            canada_wildfire_gdf = gpd.GeoDataFrame(canada_wildfire_sdf, geometry='SHAPE')
            canada_wildfire_gdf['Start_Date'] = canada_wildfire_gdf['Start_Date'].dt.strftime('%Y-%m-%d')

            selected_prov_gdf = provs_gdf[provs_gdf['Province'] == province]
        
            def get_marker_size(Hectares):
                if Hectares < 5000:
                    return 6
                elif Hectares < 80000:
                    return 9
                elif Hectares < 250000:
                    return 14
                elif Hectares < 450000:
                    return 19
                else:
                    return 24
            canada_wildfire_gdf['Hectares__Ha_'] = canada_wildfire_gdf['Hectares__Ha_'].fillna(0)
            canada_wildfire_gdf['marker_size'] = canada_wildfire_gdf['Hectares__Ha_'].apply(get_marker_size)


            # Ensure geometries are Point types
            canada_wildfire_gdf['latitude'] = canada_wildfire_gdf.geometry.y
            canada_wildfire_gdf['longitude'] = canada_wildfire_gdf.geometry.x

            #Create Map
            zoom = 4.7
            if province == 'Yukon Territory':
                zoom = 4
            elif province == 'Northwest Territories':
                zoom = 2.8
            elif province == 'Nunavut':
                zoom = 2.5
            elif province == 'Quebec':
                zoom = 4
            centroid = selected_prov_gdf.geometry.centroid.iloc[0]
            map = folium.Map(location=[centroid.y, centroid.x], zoom_start=zoom)
            folium.TileLayer(f'{basemap_selection}').add_to(map)
            # Add the state GeoDataFrame
            folium.GeoJson(
                provs_gdf,
                name="Province",  
                style_function=lambda x: {
                    'color': '#B2BEB5',  
                    'fillColor': '#B2BEB5', 
                    'fillOpacity': 0.3,
                    'weight': 1
                },
                tooltip=folium.GeoJsonTooltip(fields=["Province"], aliases=["Province:"]),
            ).add_to(map)
            folium.GeoJson(
            selected_prov_gdf,
            name="Selected Province",
            style_function=lambda x: {
                'color': 'black',  
                'fillColor': '#B2BEB5', 
                'fillOpacity': 0.2,
                'weight': 2.5
            },
            tooltip=folium.GeoJsonTooltip(fields=["Province"], aliases=["Province:"]),
            ).add_to(map) 

            
            # Path to your fire icon image
            fire_icon_path = "https://github.com/zkasson/StreamlitPortfolio/blob/main/Fire2.png?raw=true"

            # Add Wildfires
            for _, row in canada_wildfire_gdf.iterrows():
                # Dynamically set the icon size based on marker_size
                fire_icon = folium.CustomIcon(
                    fire_icon_path,
                    icon_size=(row['marker_size'] * 2, row['marker_size'] * 2)  # Scale size dynamically
                )

                folium.Marker(
                    location=(row['latitude'], row['longitude']),
                    icon=fire_icon,  # Custom fire icon with dynamic size
                    tooltip=f"Hectares: {row['Hectares__Ha_']}"
                ).add_to(map)
            # Render the map in Streamlit
            st.components.v1.html(map._repr_html_(), height=1200,width = 1200)



        # # # United States Wildfires # # # 
        else:
            with st.sidebar:
                    st.markdown('''<p style='text-align: center; 
                            color: #F9DB6D; 
                            font-size: 16px; 
                            background-color: rgba(249, 219, 109, 0.1);
                            letter-spacing: .1rem; 
                            margin-bottom: 0px; 
                            padding-bottom: 6px; 
                            padding-top: 6px; 
                            margin-bottom: 15px; 
                            margin-top: 5px; 
                            border-radius: 20px;
                            border: 2px solid #F9DB6D;' >
                    Explore Active Wildfire in the US
                </p>''', 
                unsafe_allow_html=True)

            # Dictionary to map orgin codes to state names, desired columns, Map fire types
            origin_to_state = {
                'US-AL': 'Alabama','US-AK': 'Alaska','US-AZ': 'Arizona','US-AR': 'Arkansas','US-CA': 'California','US-CO': 'Colorado','US-CT': 'Connecticut',
                'US-DE': 'Delaware', 'US-FL': 'Florida', 'US-GA': 'Georgia','US-HI': 'Hawaii','US-ID': 'Idaho','US-IL': 'Illinois','US-IN': 'Indiana',
                'US-IA': 'Iowa','US-KS': 'Kansas','US-KY': 'Kentucky','US-LA': 'Louisiana','US-ME': 'Maine','US-MD': 'Maryland','US-MA': 'Massachusetts','US-MI': 'Michigan','US-MN': 'Minnesota',
                'US-MS': 'Mississippi','US-MO': 'Missouri','US-MT': 'Montana','US-NE': 'Nebraska','US-NV': 'Nevada','US-NH': 'New Hampshire','US-NJ': 'New Jersey','US-NM': 'New Mexico',
                'US-NY': 'New York','US-NC': 'North Carolina','US-ND': 'North Dakota','US-OH': 'Ohio','US-OK': 'Oklahoma','US-OR': 'Oregon','US-PA': 'Pennsylvania',
                'US-RI': 'Rhode Island','US-SC': 'South Carolina','US-SD': 'South Dakota','US-TN': 'Tennessee','US-TX': 'Texas','US-UT': 'Utah','US-VT': 'Vermont',
                'US-VA': 'Virginia','US-WA': 'Washington','US-WV': 'West Virginia','US-WI': 'Wisconsin','US-WY': 'Wyoming','US-DC': 'District of Columbia','US-PR': 'Puerto Rico'
            }
            desired_columns = [
                "OBJECTID","IncidentName","IncidentTypeCategory","DailyAcres","PercentContained","FireDiscoveryDateTime","DiscoveryAcres",
                "POOCounty","POOState","FireCause","TotalIncidentPersonnel","ResidencesDestroyed","OtherStructuresDestroyed","Injuries","SHAPE"
            ]
            fire_type = {
                'WF': 'Contained',
                'RX': 'Prescribed'
                }

            json_file = r'https://raw.githubusercontent.com/zkasson/StreamlitPortfolio/refs/heads/main/US_States%20(1).json'
            item_id = "d957997ccee7408287a963600a77f61f"

            def read_json(url):
                prov_gdf = gpd.read_file(url)
                return prov_gdf
            def read_fl(item_id):
                living_atlas_item = gis.content.get(item_id)
                feature_layer = living_atlas_item.layers[0]
                sdf = feature_layer.query(where="1=1", out_sr=4326).sdf
                return sdf

            # Read in data
            state_gdf = read_json(json_file)
            wildfire_sdf = read_fl(item_id)

            # Create dropdown for States and basemap
            states = state_gdf['State'].unique()
            with st.sidebar:
                state = st.sidebar.selectbox('Select a State', states)
                basemap_selection = st.sidebar.selectbox('Select a basemap', ['CartoDB.Positron', 'CartoDB.DarkMatter', 'openstreetmap'])

            # Data Engineering of wild fires
            wildfire_sdf = wildfire_sdf[desired_columns]
            wildfire_sdf['State'] = wildfire_sdf['POOState'].map(origin_to_state)
            wildfire_sdf = wildfire_sdf.drop(columns=['POOState'])
            wildfire_sdf['Type'] = wildfire_sdf['IncidentTypeCategory'].map(fire_type)
            wildfire_sdf = wildfire_sdf.drop(columns=['IncidentTypeCategory'])

            def update_type(row):
                if row['Type'] == 'Prescribed':
                    return 'Prescribed'
                elif pd.isna(row['PercentContained']):
                    return 'Unknown Containment'
                elif 0 < row['PercentContained'] < 100:
                    return 'Actively Containing'
                elif row['PercentContained'] == 0:
                    return 'Uncontained'
                else:
                    return row['Type']
            wildfire_sdf['Type'] = wildfire_sdf.apply(update_type, axis=1)

            # Group by State and Type, then sum Acres
            area_sdf = wildfire_sdf.groupby(['State', 'Type'])['DailyAcres'].sum().reset_index()
            area_sdf = area_sdf.pivot(index='State', columns='Type', values='DailyAcres').fillna(0)
            area_sdf.columns.name = None

            # Create unit variable and engineer data to use correct unit
            with st.sidebar:
                unit = st.sidebar.radio(
                    "Select a Unit",
                    ['Acres', 'Hectares']
                )
            conversion_factor = 2.47105
            def correct_unit(area_sdf,unit_df):
                if unit_df == 'Acres':  
                    area_final = area_sdf 
                    return area_final
                elif unit_df == 'Hectares':
                    area_final = area_sdf
                    columns_to_convert = ['Actively Containing', 'Contained', 'Uncontained', 'Unknown Containment','Prescribed']
                    for col in columns_to_convert:
                        if col in area_final.columns:
                            area_final[col] = area_final[col] / conversion_factor
                    return area_final
                else:
                    # Handle unexpected unit cases
                    raise ValueError(f"Unsupported unit: {unit_df}")
            area_final = correct_unit(area_sdf,unit)

            # Dynamically select only the columns present in the DataFrame
            available_columns = [col for col in ['Contained', 'Actively Containing', 'Prescribed', 'Uncontained','Unknown Containment'] if col in area_final.columns]
            area_final = area_final.reset_index().melt(id_vars=['State'], 
                                                            value_vars=available_columns,
                                                            var_name='Type', 
                                                            value_name='Area')
            
            # Filter data for the selected state
            area_final = area_final[area_final['State'] == state]
            no_fires_bool = area_final['Area'].dropna().empty

            if area_final['Area'].dropna().empty:
                rounded_upper_limit =5000
            else:
                # Calculate the upper limit for the y-axis
                max_sh = area_final['Area'].max()  # Find the max value in the area column
                upper_limit = max_sh + (max_sh / 10) if max_sh > 0 else 1000
                rounded_upper_limit = round(upper_limit / 100) * 100 if upper_limit > 99 else 100

            # # # Create Chart # # #
            if no_fires_bool:
                with st.sidebar:
                    st.sidebar.write(f'**There are no ongoing fires in {state}**')
            else:
                colors = {
                    "Actively Containing": "orange",
                    "Uncontained": "red",
                    "Contained": "green",
                    "Prescribed": "#CCCC00",
                    "Unknown Containment": "gray"  
                }
                area_final["Color"] = area_final["Type"].map(colors)

                # Create the plot
                fig, ax = plt.subplots(1, 1)
                bars = ax.bar(
                    area_final["Type"],
                    area_final["Area"],
                    color=area_final["Color"]
                )
                # Customize the plot
                plt.xticks(rotation=15, ha='right') 
                ax.set_ylabel(f'Area ({unit})', fontsize=14, fontweight='bold') 
                ax.set_xlabel('Control Stage', fontsize=14, fontweight='bold')
                ax.set_title(f'{unit} of fire within {state} by control stage')
                ax.set_ylim(0, rounded_upper_limit)

                ax.yaxis.set_major_formatter(matplotlib.ticker.StrMethodFormatter("{x:,.0f}"))

                for bar, area in zip(bars, area_final["Area"]):
                    # Calculate y position for the annotation text
                    text_y = bar.get_height() + 0.02 * rounded_upper_limit  
                    text_y = min(text_y, rounded_upper_limit)  
                    ax.text(
                        bar.get_x() + bar.get_width() / 2, # x-position 
                        text_y, # y-position 
                        f'{area:,.0f} {unit}',  
                        ha='center',  
                        va='bottom',  
                        fontsize=10  
                    )
                # Display the plot
                plt.tight_layout()
                with st.sidebar:
                    stats = st.sidebar.pyplot(fig, use_container_width=True)


            # # # M A P # # #
            # # # US WILDFIRES # # #

            # # # Finish layers for Map # # #
            wildfire_gdf = gpd.GeoDataFrame(wildfire_sdf, geometry='SHAPE')
            wildfire_gdf['Start_Date'] = wildfire_gdf['FireDiscoveryDateTime'].dt.strftime('%Y-%m-%d')
            wildfire_gdf = wildfire_gdf.drop(columns=['FireDiscoveryDateTime'])
            selected_state_gdf = state_gdf[state_gdf['State'] == state]
        
            def get_marker_size(daily_acres):
                if daily_acres < 1000:
                    return 6
                elif daily_acres < 10000:
                    return 9
                elif daily_acres < 50000:
                    return 14
                elif daily_acres < 300000:
                    return 19
                else:
                    return 24
            wildfire_gdf['DailyAcres'] = wildfire_gdf['DailyAcres'].fillna(0)
            wildfire_gdf['marker_size'] = wildfire_gdf['DailyAcres'].apply(get_marker_size)


            # Ensure geometries are Point types
            wildfire_gdf['latitude'] = wildfire_gdf.geometry.y
            wildfire_gdf['longitude'] = wildfire_gdf.geometry.x

            # Create Map
            zoom = 6
            if state == 'Alaska':
                zoom = 4 
            elif state == 'Texas':
                zoom = 4.7
            centroid = selected_state_gdf.geometry.centroid.iloc[0]
            map = folium.Map(location=[centroid.y, centroid.x], zoom_start=zoom)
            folium.TileLayer(f'{basemap_selection}').add_to(map)
            # Add the state GeoDataFrame
            folium.GeoJson(
                state_gdf,
                name="State",  # Layer name for toggle
                style_function=lambda x: {
                    'color': '#B2BEB5',  # Border color
                    'fillColor': '#B2BEB5',  # Fill color
                    'fillOpacity': 0.3,
                    'weight': 0.5
                },
                tooltip=folium.GeoJsonTooltip(fields=["State"], aliases=["State:"]),
            ).add_to(map)
            folium.GeoJson(
            selected_state_gdf,
            name="Selected State",
            style_function=lambda x: {
                'color': 'black',  # Border color
                'fillColor': '#B2BEB5',  # Fill color for selected state
                'fillOpacity': 0.2,
                'weight': 2.5
            },
            tooltip=folium.GeoJsonTooltip(fields=["State"], aliases=["State:"]),
            ).add_to(map) 

            
            # Path to your fire icon image
            fire_icon_path = "https://github.com/zkasson/StreamlitPortfolio/blob/main/Fire2.png?raw=true"

            # Add Wildfires
            for _, row in wildfire_gdf.iterrows():
                # Dynamically set the icon size based on marker_size
                fire_icon = folium.CustomIcon(
                    fire_icon_path,
                    icon_size=(row['marker_size'] * 2, row['marker_size'] * 2)  # Scale size dynamically
                )

                folium.Marker(
                    location=(row['latitude'], row['longitude']),
                    icon=fire_icon,  # Custom fire icon with dynamic size
                    tooltip=f"Acres: {row['DailyAcres']}"
                ).add_to(map)
            # Render the map in Streamlit
            st.components.v1.html(map._repr_html_(), height=1200,width = 1200)

    # # # Amazon Map# # # #
    # # # Project # # #
    elif project =="Python Map":
        st.markdown(f'''<h1 style='text-align: center; color: grey; font-size: 45px; 
                letter-spacing: .5rem; margin-bottom: 5px; padding-bottom: 40px;'>Python Map Project</h1>'''
                , unsafe_allow_html=True)
        options = ["Map", "Code"]

        amazon_map = st.sidebar.segmented_control("Selection:", options, selection_mode="single")
        
        code = """
# Set Up
import geopandas as gpd
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import os
import requests
import zipfile
data_folder = 'data'
output_folder = 'output'

# Create Folder for data and output if they do not already exist
if not os.path.exists(data_folder):
    os.mkdir(data_folder)
if not os.path.exists(output_folder):
    os.mkdir(output_folder)

# Define a function to download data from a URL
def download(url):
    filename = os.path.join(data_folder, os.path.basename(url))
    if not os.path.exists(filename):
        with requests.get(url, stream=True, allow_redirects=True) as r:
            with open(filename, 'wb') as f:
                for chunk in r.iter_content(chunk_size=8192):
                    f.write(chunk)
        print('Downloaded', filename)

# URLs and files for downloading
data_url = 'https://github.com/spatialthoughts/python-dataviz-web/releases/download/'
hydrorivers_file = 'hydrorivers_100.gpkg'
hydrorivers_url = data_url + 'hydrosheds/'
countries_file = 'ne_10m_admin_0_countries_ind.zip'
countries_url = data_url + 'naturalearth/'
download(hydrorivers_url + hydrorivers_file)
download(countries_url + countries_file)

# Create gdf of the countries and filter to only India
countries_filepath = os.path.join(data_folder, countries_file)
country_gdf = gpd.read_file(countries_filepath)
country = 'Brazil'
selected_country = country_gdf[(country_gdf['SOVEREIGNT'] == country)&(country_gdf['TYPE'] != 'Dependency')]

# Create gdf of river network while also clipping it to the shap of India
hydrorivers_filepath = os.path.join(data_folder, hydrorivers_file)
river_gdf = gpd.read_file(hydrorivers_filepath, mask=selected_country)
river_gdf.head(4)

# Create a width scale based on upland area
original_min = 10
original_max = 4000
target_min = 0.1
target_max = 0.9
scaled = (river_gdf['UPLAND_SKM'] - original_min) / (original_max - original_min)
river_gdf['width'] = scaled.clip(0, 1) * (target_max - target_min) + target_min
river_gdf_final = river_gdf.sort_values(['UPLAND_SKM', 'width'])[
    ['MAIN_RIV', 'UPLAND_SKM', 'width', 'geometry']]
river_gdf_final.head(4)

fig, ax = plt.subplots(figsize=(10, 10))
title = f'Rivers of {country}'

river_gdf_final.plot(ax=ax,column='MAIN_RIV',categorical=True, linewidth=river_gdf_final['width'])
fig.set_facecolor((0,0,0))
ax.set_title(title, color='white', fontsize=30)
ax.set_axis_off()
output_path = os.path.join(output_folder, 'RiversOfBrazil.jpg')
plt.savefig(output_path, dpi=300)
plt.show()
"""
        if amazon_map == "Code":
            st.code(code, language="python")
        else:
            st.markdown("<img src='https://github.com/zkasson/StreamlitPortfolio/blob/main/RiversOfBrazil.jpg?raw=true' width='700' style='display: block; margin: 0 auto; border-radius: 20px;'>" , unsafe_allow_html=True)
        
    # # # Python Vizualization # # #
    # # # PROJECT # # #       
    elif project == "Python Vizualization":   
        st.markdown(f'''<h1 style='text-align: center; color: grey; font-size: 45px; 
                letter-spacing: .5rem; margin-bottom: 5px; padding-bottom: 40px;'>Matplotlib Project</h1>'''
                , unsafe_allow_html=True)
        options = ["Map", "Code"]

        python_viz_option = st.sidebar.segmented_control("Selection:", options, selection_mode="single")
        
        code = """
# Set Up
from google.colab import drive
import pandas as pds
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import matplotlib.colors as mcolors
import colorcet as cc
import os

data_folder = 'data'
output_folder = 'output'

if not os.path.exists(data_folder):
    os.mkdir(data_folder)
if not os.path.exists(output_folder):
    os.mkdir(output_folder)

# Download data
drive.mount('/content/drive')
df = pds.read_excel('/content/drive/My Drive/Colab Notebooks/Portfolio/US_Temp_Data.xlsx')
df.head(4)

# Create function to convert Celsius to Fahrenheit
def celsius_to_fahr(temp_celsius):
    return 9/5 * temp_celsius + 32

# Create a dictionary and a lambda function in order to reformat data in the format: YEARMO
months = {'Jan': '01', 'Feb': '02', 'Mar': '03', 'Apr': '04',
          'May': '05', 'Jun': '06', 'Jul': '07', 'Aug': '08',
          'Sep': '09', 'Oct': '10', 'Nov': '11', 'Dec': '12'}

to_date = lambda x: x.pop('Year').astype(str) + x.pop('Month').map(months)

# Melt data from long table to tall table
data = (df.melt(id_vars='Year', var_name='Month', value_name='Temp').assign(Date=to_date).set_index('Date').sort_index().reset_index())

# Format the data to make seperate column for the Month and Year
data["Year"] = data["Date"].str.slice(start=0,stop=4).astype(int)
data["Month"] = data["Date"].str.slice(start=4,stop=6).astype(int)
data = data.reindex(columns=['Year', 'Month', 'Temp'])

#  convert temperatures from Celsius to Fahrenheit
data['Temp'] = round(celsius_to_fahr(data["Temp"]),1)
data.head(4)

# # Create variable for yearly average
yearly_data = round(data.groupby("Year").mean().sort_values("Year", ascending = True),2)
yearly_data = yearly_data.rename(columns={'Temp':'Yearly_Temp'})
yearly_data = yearly_data.drop('Month', axis=1)
# # # # Create variable for monthly average across all years
# monthly_temps = round(data.groupby("Month").mean().sort_values("Month", ascending = True),2)
# monthly_temps = monthly_temps.rename(columns={'Temp':'Monthly_Avg'})
yearly_data

# Create a figure represetning the change in yearly temperature average
fig, ax1 = plt.subplots(1,1, figsize=(15,15))
fig.patch.set_facecolor('black')
ax1.set_facecolor('black')
y = yearly_data["Yearly_Temp"]
x = yearly_data.index.values
myLocator = mticker.MultipleLocator(5)
ax1.xaxis.set_major_locator(myLocator)


# Normalize data for color mapping
norm = plt.Normalize(y.min(), y.max())
# Use the 'fire' colormap from colorcet
cmap = cc.cm.bkr

# Plot with color-changing line
for i in range(len(x) - 1):
    ax1.plot(x[i:i+2], y.iloc[i:i+2], color=cmap(norm(y.iloc[i + 1])), linewidth=5)

ax1.set_xlabel('Year', fontsize=20, color='white')
ax1.set_ylabel('Temperature (°F)', fontsize=20, color='white')
ax1.set_title('Global Yearly Temperature Average from 1901 to 2021', fontsize=24, color='white')
for label in ax1.xaxis.get_ticklabels():
    label.set_rotation(45)
    label.set_color('white')
    label.set_fontsize(14)
for label in ax1.yaxis.get_ticklabels():
    label.set_color('white')
    label.set_fontsize(14)
ax1.grid(True,alpha=0.3)
output_path = os.path.join(output_folder, 'YearlyTemp.png')
plt.savefig(output_path,dpi=100)
"""
        if python_viz_option == "Code":
            st.code(code, language="python")
        else:
            st.markdown("<img src='https://github.com/zkasson/StreamlitPortfolio/blob/main/YearlyTemp.png?raw=true' width='700' style='display: block; margin: 0 auto; border-radius: 20px;'>" , unsafe_allow_html=True)
    
    # # # Surface Model # # #
    # # # PROJECT # # #
    elif project == "Open Source Surface Model": 
        st.markdown(f'''<h1 style='text-align: center; color: grey; font-size: 45px; 
                letter-spacing: .5rem; margin-bottom: 5px; padding-bottom: 40px;'>Rasterio Project</h1>'''
                , unsafe_allow_html=True)
        options = ["Map", "Code"]

        surface_model_option = st.sidebar.segmented_control("Selection:", options, selection_mode="single")
        
        code = """
# Set Up
import os
import rioxarray as rxr
from rioxarray.merge import merge_arrays
import matplotlib.pyplot as plt
data_folder = 'data'
output_folder = 'output'
#Create Folder for data and output if they do not already exist
if not os.path.exists(data_folder):
    os.mkdir(data_folder)
if not os.path.exists(output_folder):
    os.mkdir(output_folder)
# Define a function to download data from a URL using
def download(url):
    filename = os.path.join(data_folder, os.path.basename(url))
    if not os.path.exists(filename):
        from urllib.request import urlretrieve
        local, _ = urlretrieve(url, filename)
        print('Downloaded ' + local)
srtm_tiles = [
  'N27E086.hgt',
  'N27E087.hgt',
  'N28E086.hgt',
  'N28E087.hgt'
]
data_url = 'https://github.com/spatialthoughts/python-dataviz-web/releases/' \
  'download/srtm/'
for tile in srtm_tiles:
  url = '{}/{}'.format(data_url, tile)
  download(url)

  # Use Rasterio to connect to elevation data
datasets = []
for tile in srtm_tiles:
    path = os.path.join(data_folder, tile)
    rds = rxr.open_rasterio(path)
    # connect to first band
    band = rds.sel(band=1)
    datasets.append(band)

# Plot 4 DEMs
fig, axes = plt.subplots(1, 4)
fig.set_size_inches(15,3)
for index, ax in enumerate(axes.flat):
    da = datasets[index]
    im = da.plot.imshow(ax=ax, cmap='viridis')
    filename = srtm_tiles[index]
    ax.set_title(filename)
    ax.set_aspect('equal') # maintain aspect ratio

plt.tight_layout()
plt.show()

# # # We want to be able to view as a merged DEM # # #
merged = merge_arrays(datasets, method='first')
# Find the maximum point within the DEM
max_da = merged.where(merged==merged.max(), drop=True).squeeze()
# Assign coordinates and height to variables
max_x = max_da.x.values
max_y = max_da.y.values
max_elev = int(max_da.values)
print(f'Mt. Everest is located at {max_x.round(6)} E, {max_y.round(6)} N and is {max_elev} meters above sea level.')
"""
        code1 = """
# Plot DEM with annotation of Mt. Everests location
fig, ax = plt.subplots(1, 1)
fig.set_size_inches(12, 10)
merged.plot.imshow(ax=ax, cmap='inferno', add_labels=False)
ax.plot(max_x, max_y, '^k', markersize=11)
ax.annotate('Mt. Everest (elevation:{}m)'.format(max_elev),
            xy=(max_x, max_y), xycoords='data',
            xytext=(10, 0), textcoords='offset points',
            arrowprops=None,
            zorder=10
            )
CS = ax.contour(merged.x, merged.y, merged.values, levels=10, colors='gray', linewidths=0.5,zorder=1)
plt.tight_layout()
output_path = os.path.join(output_folder, 'DEM_MtEverest.jpg')
plt.savefig(output_path, dpi=300)
plt.show()
"""
        code_return = "Mt. Everest is located at 86.925556 E, 27.988889 N and is 8748 meters above sea level."
        if surface_model_option == "Code":
            st.code(code, language="python")
            st.markdown(
            f"<div style='text-align: left; color: grey; margin: 0 auto; margin-top: 5px; max-width: 1200px; margin-bottom: 20px; font-size: 26px; font-family: 'Roboto', sans-serif;'>{code_return}</div>",
            unsafe_allow_html=True
        )
            st.code(code1, language="python")
        else:
            st.markdown("<img src='https://github.com/zkasson/StreamlitPortfolio/blob/main/DEM_MtEverest.jpg?raw=true' width='1000' style='display: block; margin: 0 auto; border-radius: 20px;'>" , unsafe_allow_html=True) 
    
    
    # # # ESRI Dashboard # # #
    # # # PROJECT # # #
    elif project == "ESRI Dashboard": 
        st.markdown(f'''<h1 style='text-align: center; color: grey; font-size: 45px; 
                letter-spacing: .5rem; margin-bottom: 5px; padding-bottom: 10px;'>ESRI Dashboard Project</h1>'''
                , unsafe_allow_html=True)
        options = ["Map", "Code"]

        esri_dashboard_option = st.sidebar.segmented_control("Selection:", options, selection_mode="single")
        
        code = """
//StateName
var stateName = $feature.STATE_NAME;

// Intersect
var droughtInState = Intersects($feature, FeatureSetByName($map, 'Drought Assignment - ZK'));

// Check if any droughts intersect the state
if (Count(droughtInState) == 0) {
    return 'There are no droughts in the state of ' + stateName + '.';
} else {
    // Count the number of droughts in the state
    var droughtCount = Count(droughtInState);
    return 'There are ' + Text(droughtCount) + ' droughts in the state of ' + stateName + '.';
}



// Access Layer
var droughtLayer = FeatureSetByPortalItem("6aa5cf1992554a8b856b44d22d302b47", 0);
// Create Counter
var totalAcresBySeverity = {
    Mild: 0,
    Moderate: 0,
    Severe: 0,
    Extreme: 0
};
// loop through drought points
for (var drought in droughtLayer) {
    // Check if the drought geometry is ongoing
    if (Lower(Trim(drought.ongoing)) == "yes") {
        var severity = Lower(Trim(drought.severity));
        var landArea = drought.land_area;

        // Use HasValue to check if severity = drought.severity then add to the count 
        if (HasValue(totalAcresBySeverity, severity)) {
            totalAcresBySeverity[severity] += landArea;
        }
    }
}

// Create an array of dictionaries for featureSet
var features = [];

// Push dictionary to features. include severity
for (var severity in totalAcresBySeverity) {
    Push(features, {
        attributes: {
            Severity: severity,
            TotalDroughtAcres: totalAcresBySeverity[severity]
        }
    });
}

// Define featureSet schema
var resultFeatureSet = {
    fields: [
        { name: "Severity", type: "esriFieldTypeString", alias: "Severity" },
        { name: "TotalDroughtAcres", type: "esriFieldTypeDouble", alias: "Total Drought Acres" }
    ],
    geometryType: "",
    features: features
};

// Return featureSet
return FeatureSet(resultFeatureSet);
"""
        esri_dashboard_background = "This is some of the Arcade code I used for the dashboard:"
        if esri_dashboard_option == "Code":
            st.markdown(
            f"<div style='text-align: center; color: grey; margin: 0 auto; margin-top: 0px; max-width: 1200px; margin-bottom: 20px; font-size: 26px; font-family: 'Roboto', sans-serif;'>{esri_dashboard_background}</div>",
            unsafe_allow_html=True)
            st.code(code, language="python")
            
        else:
            st.markdown("<img src='https://github.com/zkasson/StreamlitPortfolio/blob/main/EsriDashboard.png?raw=true' width='1200' style='display: block; margin: 0 auto; border-radius: 20px;'>" , unsafe_allow_html=True) 
    
    # # # WEB DEV # # #
    # # # PROJECT # # #
    elif project == "Web Developement":  
        web_dev_background = "I developed a full-stack web application using Next.js for the frontend, leveraging its server-side rendering (SSR) and static site generation (SSG) capabilities to enhance performance and SEO. I integrated an interactive map using the ArcGIS API SDK, enabling advanced geospatial visualization and data rendering. The backend is built with Node.js, where I designed and implemented RESTful APIs for efficient data retrieval and manipulation. For data storage, I utilized MongoDB, ensuring a scalable and flexible NoSQL database solution."
        st.markdown("<img src='https://github.com/zkasson/StreamlitPortfolio/blob/main/CartoTick.jpg?raw=true' width='1100' style='display: block; margin: 0 auto; border-radius: 20px;'>" , unsafe_allow_html=True) 
        st.markdown(
            f"<div style='text-align: center; color: grey; margin: 0 auto; margin-top: 0px; max-width: 1100px; margin-bottom: 20px; font-size: 26px; font-family: 'Roboto', sans-serif;'>{web_dev_background}</div>",
            unsafe_allow_html=True
        )
    
    elif project == "Upcoming Projects":
        st.markdown(f'''<h1 style='text-align: center; color: grey; font-size: 45px;
                letter-spacing: .5rem; margin-bottom: 5px; padding-bottom: 0px;'>{project}</h1>'''
                , unsafe_allow_html=True)
        upcoming = "I have many more examples of my work, and I’m in the process of slowly adding them to my current portfolio. In the meantime, ENJOY!"
        st.markdown(
            f"<div style='text-align: left; color: grey; margin: 0 auto; margin-top: 40px; max-width: 1200px; margin-bottom: 20px; font-size: 26px; font-family: 'Roboto', sans-serif;'>{upcoming}</div>",
            unsafe_allow_html=True
        )



# # # # # # # # #
# # # CONTACT # # #
# # # PAGE # # #
# # # # # # # # #

elif selected == "Contact":
    st.markdown('''<h1 style='text-align: center; color: grey; font-size: 100px; font-family: \"Impact\", sans-serif; line-height: 1; 
                letter-spacing: 1rem; margin-bottom: 5px; padding-bottom: 0px;'>Contact Me</h1>'''
                , unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        st.markdown(
            "<img src='https://github.com/zkasson/StreamlitPortfolio/blob/main/Pictures/IMG_88632.jpg?raw=true' width='700' style='display: block; margin: 10px auto; margin-top: 40px; border-radius: 20px;'>",
            unsafe_allow_html=True
        )

    with col2:
        st.markdown('''<h1 style='text-align: right; color: #F9DB6D; font-size: 36px; line-height: 1.2; font-family: "Roboto", sans-serif;
                    margin-top: 230px; max-width: 600px; padding-top: 0px;'>Zack Kasson <br> <br> Zack.kasson@gmail.com <br> <br> 330-523-8956 <br> <br> Sedro-Woolley, WA</h1>''',
                    unsafe_allow_html=True)
        
    st.markdown('''<h1 style='text-align: center; color: grey; font-size: 100px; font-family: \"Impact\", sans-serif; line-height: 1; 
                letter-spacing: 1rem; margin-bottom: 5px; margin-top: 30px; padding-bottom: 0px;'>References</h1>'''
                , unsafe_allow_html=True)
    

    col3, col4, col5, col6 = st.columns(4)
    
    with col3:
        st.markdown('''<h1 style='text-align: left; color: grey; font-size: 28px; line-height: 1.2; font-family: "Roboto", sans-serif;
                    margin-top: 30px; max-width: 600px; padding-top: 0px;'>Nicki Ozaki (HST) <br> <br>Kupu <br> <br>Nicki.ozaki@kupuhawaii.org <br> <br> 808.735.1221 ext. 1038</h1>''',
                    unsafe_allow_html=True)
    with col4:
        st.markdown('''<h1 style='text-align: left; color: grey; font-size: 28px; line-height: 1.2; font-family: "Roboto", sans-serif;
                    margin-top: 30px; max-width: 600px; padding-top: 0px;'>Mark Vroman (PST)<br> <br>Hampton Lumber <br> <br>Vroman@hamptonlumber.com <br> <br> 503-559-4079</h1>''',
                    unsafe_allow_html=True)
    with col5:
        st.markdown('''<h1 style='text-align: left; color: grey; font-size: 28px; line-height: 1.2; font-family: "Roboto", sans-serif;
                    margin-top: 30px; max-width: 600px; padding-top: 0px;'>Paul Lulay (PST)<br> <br>Hampton Lumber <br> <br>paullulay@hamptonlumber.com<br> <br>971-707-2549</h1>''',
                    unsafe_allow_html=True)
    with col6:
        st.markdown('''<h1 style='text-align: left; color: grey; font-size: 28px; line-height: 1.2; font-family: "Roboto", sans-serif;
                    margin-top: 30px; max-width: 600px; padding-top: 0px;'>Pamela Machuga (EST)<br> <br> National Park Service<br> <br>Pam_machuga@nps.gov <br> <br> 440-343-7035</h1>''',
                    unsafe_allow_html=True)
