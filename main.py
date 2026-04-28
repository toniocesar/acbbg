import streamlit as st
import os

st.title("Rock AC")

# Album definitions with tracks
albums = {
    "1984": {
        "folder": "1984 SON M3",
        "images": [
            "CAPA  1984   ( acbbg) .jpg",
            "ANT 1984.jpg"
        ],
        "tracks": [
            ("FIND ME AWAY", "1- FIND ME AWAY acbbg.mp3"),
            ("NO TIME TO PRETEND", "2- NO TIME TO PRETEND acbbg.mp3"),
            ("FAR PLACE GIRL", "3- FAR PLACE GIRL acbbg.mp3"),
        ]
    },    
    "HOME 1995": {
        "folder": "DISC 1 HOM M3",
        "images": [
            "CAPA HOME 1 ( ACCBG) 1995.png",
            "CAPA HOME 1 ( ACCBG) 1995.png"],
        "tracks": [
            ("RAIN FOREST", "A1-RAIN FOREST acbbg.mp3"),
            ("FIRST TIMER", "A2-FIRST TIMER  acbbg.mp3"),
            ("REPRODUCTION", "A3-REPRODUCTION acbbg.mp3"),
            ("LOTTO", "A4-LOTTO  acbbg.mp3"),
            ("TANIT", "A5-TANIT  acbbg.mp3"),
            ("YOU ARE MY SUNSHINE", "A6-YOU ARE MY SUNSHINE acbbg.mp3"),
            ("THE WEIGHT OF A TON", "A7- THE WEIGHT OF A TON acbbg.mp3"),
            ("GIGOLO", "A8- GIGOLO acbbg.mp3"),
            ("BRIDGE BLUES", "A9- BRIDGE BLUES acbbg.mp3"),
            ("SYLENT WATCHER", "A10- SYLENT WATCHER acbbg.mp3"),
        ]
    },
    "FIRE IN YOUR HEART - 2001": {
        "folder": "FIRE IN YOUR HEART -- acbbg",
        "images": ["FIRE IN YOUR HEART - front.jpg",
                   "FIRE IN YOUR HEART - back.png"],
        "tracks": [
            ("JUST A SHAME", "B1- JUST A SHAME acbbg.mp3"),
            ("FIRE IN YOUR HEART", "B2- FIRE IN YOUR HEART acbbg.mp3"),
            ("POLITICIANS KNOW IT ALL", "B3- POLITITIANS KNOW IT ALL acbbg.mp3"),
            ("TANIT 2000", "B4-TANIT 2000 acbbg.mp3"),
            ("WAITING FOR KILLERS", "B5- WAITING FOR KILLERS acbbg.mp3"),
            ("DON'T SAY YOU LOVE ME", "B6- DON´T SAY YOU LOVE ME acbbg.mp3"),
            ("WEEK-END GIRL", "B7- WEEK-END GIRL acbbg.mp3"),
            ("WHY YOU TALKED TO ME", "B8- WHY YOU TALKED TO ME acbbg.mp3"),
            ("QUARANTINE", "B9- QUARANTINE acbbg.mp3"),
            ("MULTIPLIED BY TWO", "B91- MULTIPLIED BY TWO acbbg.mp3"),
            ("BETRAY YOU", "B92- BETRAY YOU acbbg.mp3"),
        ]
    },
    "MARAU - 2024": {
        "folder": "MARAU -- ( acbbg) 2019   ( TWIMC final edition)",
        "images": ["CAPA MARAU ( Twimc acbbg).png",
                   "CAPA MARAU ( Twimc acbbg).png"],
        "tracks": [
            ("MARAU", "T1-MARAU.mp3"),
            ("MOVED BY REVENGE", "T2-MOVED BY REVENGE.mp3"),
            ("NO DOUBT I'M LOSING YOU", "T3-NO DOUBT I´M LOSING YOU.mp3"),
            ("ENVIRONMENT CHALLENGE", "T4- ENVIROMENT CHALLENGE.mp3"),
            ("GOLD DIGGER", "T5 GOLD DIGGER.mp3"),
            ("EMBER IN THE FIRE", "T6 EMBER IN THE FIRE.mp3"),
            ("KATRINA", "T7 KATRINA.mp3"),
            ("A REAL SNAKE", "T8 A REAL SNAKE.mp3"),
            ("FIRST TIMER REVISIT", "T9- FIRST TIMER REVISIT.mp3"),
            ("CREEDENCE CLEARWATER REVIVAL II", "T91A-CREEDENCE CLEARWATER REVIVAL II acbbg.mp3"),
            ("THE WRONG SIDE OF THE ROAD", "T91B-THE WRONG SIDE OF THE ROAD acbbg.mp3"),
            ("NO ROBIN HOOD", "T92-NO ROBIN HOOD.mp3"),
            ("FIFTY", "T93-FIFTY.mp3"),
            ("THE PIMP II", "T94-THE PIMP II.mp3"),
            ("FAR FROM YOUR HEART", "T95-FAR FROM YOUR HEART  a.c.b.b.g.mp3"),
            ("I KNOW I WANT IT", "T96-I KNOW I WANT IT ( acbbg).mp3"),
        ]
    },
}

# Display each album
for album_name, album_data in albums.items():
    st.header(album_name)
    
    with st.container():
        col1, col2 = st.columns([1, 1])
        
        with col1:
            # Display images
            for image_file in album_data["images"]:
                image_path = rf"albums/{album_data['folder']}/{image_file}"
                if os.path.exists(image_path):
                    st.image(image_path)
        
        with col2:
            # Display tracks with checkboxes
            for track_name, track_file in album_data["tracks"]:
                selected = st.checkbox(track_name, key=f"{album_name}_{track_name}")
                if selected:
                    audio_path = rf"albums/{album_data['folder']}/{track_file}"
                    st.audio(audio_path)
    
    st.divider()

