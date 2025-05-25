import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random

# Page configuration
st.set_page_config(
    page_title="Mediterranean Gateway - Cultural Tourism",
    page_icon="🏛️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS with Mediterranean theme
st.markdown("""
<style>
    .main-header {
        font-size: 3.5rem;
        font-weight: bold;
        background: linear-gradient(45deg, #FF6B35, #F7931E, #FFD23F);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        margin-bottom: 2rem;
    }
    .feature-card {
        background: linear-gradient(135deg, #FF6B35 0%, #F7931E 100%);
        padding: 2rem;
        border-radius: 15px;
        color: white;
        margin: 1rem 0;
        box-shadow: 0 8px 32px rgba(247, 147, 30, 0.3);
    }
    .culture-card {
        background: linear-gradient(135deg, #4ECDC4 0%, #2ECC71 100%);
        padding: 1.5rem;
        border-radius: 12px;
        color: white;
        margin: 0.5rem 0;
    }
    .metric-card {
        background: #fef7ed;
        padding: 1.5rem;
        border-radius: 12px;
        border-left: 5px solid #FF6B35;
        box-shadow: 0 4px 16px rgba(255, 107, 53, 0.1);
    }
    .sidebar .sidebar-content {
        background: linear-gradient(180deg, #FF6B35 0%, #F7931E 100%);
    }
    .rtl-text {
        direction: rtl;
        text-align: right;
    }
    .heritage-site {
        background: #f8f9fa;
        padding: 1rem;
        margin: 0.5rem 0;
        border-radius: 8px;
        border-left: 4px solid #FF6B35;
    }
</style>
""", unsafe_allow_html=True)

# Multi-language support
languages = {
    "العربية": "ar",
    "English": "en", 
    "Türkçe": "tr",
    "Ελληνικά": "el",
    "Italiano": "it",
    "Español": "es"
}

# Comprehensive text translations
texts = {
    "ar": {
        "title": "بوابة المتوسط - السياحة الثقافية",
        "subtitle": "اكتشف كنوز البحر الأبيض المتوسط الثقافية والتراثية",
        "home": "الرئيسية",
        "planner": "مخطط الرحلة الثقافية",
        "heritage": "مواقع التراث",
        "experiences": "التجارب المحلية",
        "stays": "إقامة أصيلة",
        "insights": "رؤى ثقافية",
        "booking": "مركز الحجز",
        "navigation": "التنقل",
        "language": "اللغة",
        "heritage_sites": "مواقع التراث",
        "cultural_experiences": "التجارب الثقافية",
        "cultural_rating": "التقييم الثقافي",
        "cultural_explorers": "المستكشفون الثقافيون",
        "featured_regions": "المناطق الثقافية المميزة",
        "unesco_sites": "مواقع اليونسكو",
        "best_season": "أفضل موسم ثقافي",
        "avg_tour": "متوسط الجولة الثقافية",
        "heritage_rating": "تقييم التراث",
        "heritage_map": "خريطة التراث الثقافي المتوسطي",
        "experience_categories": "فئات التجارب الثقافية",
        "ancient_civilizations": "الحضارات القديمة",
        "ancient_desc": "استكشف المعابد اليونانية والمدرجات الرومانية والأهرامات المصرية مع علماء الآثار",
        "art_architecture": "الفن والعمارة",
        "art_desc": "روائع عصر النهضة والفن الإسلامي والفسيفساء البيزنطية مع مؤرخي الفن المحليين",
        "culinary_heritage": "التراث الطهي",
        "culinary_desc": "دروس الطبخ التقليدي وتذوق النبيذ وجولات تاريخ الطعام",
        "from": "من",
        "day": "يوم",
        "cultural_preferences": "التفضيلات الثقافية",
        "budget": "الميزانية",
        "duration": "مدة الرحلة",
        "days": "أيام",
        "cultural_interests": "الاهتمامات الثقافية",
        "ancient_history": "التاريخ القديم",
        "religious_heritage": "التراث الديني",
        "museums": "الفن والمتاحف",
        "architecture": "العمارة",
        "traditional_crafts": "الحرف التقليدية",
        "folk_music": "الموسيقى والرقص الشعبي",
        "culinary_traditions": "التقاليد الطهوية",
        "archaeological_sites": "المواقع الأثرية",
        "local_festivals": "المهرجانات المحلية",
        "traditional_markets": "الأسواق التقليدية",
        "cultural_depth": "العمق الثقافي",
        "surface_explorer": "مستكشف سطحي - المعالم الشهيرة",
        "culture_enthusiast": "عاشق الثقافة - تجارب أعمق",
        "heritage_scholar": "باحث التراث - دراسة شاملة",
        "preferred_regions": "المناطق المفضلة",
        "greek_islands": "الجزر اليونانية",
        "turkish_coast": "الساحل التركي",
        "egyptian_nile": "النيل المصري",
        "italian_peninsula": "شبه الجزيرة الإيطالية",
        "spanish_coast": "الساحل الإسباني",
        "moroccan_cities": "المدن المغربية",
        "french_riviera": "الريفييرا الفرنسية",
        "croatian_coast": "الساحل الكرواتي",
        "group_type": "نوع المجموعة",
        "solo_explorer": "مستكشف منفرد",
        "couple": "زوجان",
        "family": "عائلة مع أطفال",
        "friends": "مجموعة أصدقاء",
        "study_group": "مجموعة دراسية ثقافية",
        "create_journey": "إنشاء رحلة ثقافية",
        "cultural_odyssey": "رحلة ثقافية يونانية لمدة 10 أيام",
        "location": "الموقع",
        "cultural_focus": "التركيز الثقافي",
        "experience": "التجربة",
        "cost": "التكلفة",
        "total_cost": "إجمالي تكلفة التجربة الثقافية",
        "remaining": "متبقي للإقامة والوجبات",
        "cultural_insights_summary": "الرؤى الثقافية",
        "visited": "تم زيارتها",
        "historical_periods": "الفترات التاريخية",
        "covered": "مغطاة",
        "cultural_activities": "الأنشطة الثقافية",
        "included": "مشملة"
    },
    "en": {
        "title": "Mediterranean Gateway",
        "subtitle": "Discover Cultural & Heritage Treasures of the Mediterranean",
        "home": "Home",
        "planner": "Cultural Planner",
        "heritage": "Heritage Sites",
        "experiences": "Local Experiences",
        "stays": "Authentic Stays",
        "insights": "Cultural Insights",
        "booking": "Booking Hub",
        "navigation": "Navigation",
        "language": "Language",
        "heritage_sites": "Heritage Sites",
        "cultural_experiences": "Cultural Experiences",
        "cultural_rating": "Cultural Rating",
        "cultural_explorers": "Cultural Explorers",
        "featured_regions": "Featured Mediterranean Cultural Regions",
        "unesco_sites": "UNESCO Sites",
        "best_season": "Best Cultural Season",
        "avg_tour": "Avg Cultural Tour",
        "heritage_rating": "Heritage Rating",
        "heritage_map": "Mediterranean Cultural Heritage Map",
        "experience_categories": "Cultural Experience Categories",
        "ancient_civilizations": "Ancient Civilizations",
        "ancient_desc": "Explore Greek temples, Roman amphitheaters, and Egyptian pyramids with expert archaeologists",
        "art_architecture": "Art & Architecture",
        "art_desc": "Renaissance masterpieces, Islamic art, and Byzantine mosaics with local art historians",
        "culinary_heritage": "Culinary Heritage",
        "culinary_desc": "Traditional cooking classes, wine tastings, and food history tours",
        "from": "From",
        "day": "day",
        "cultural_preferences": "Cultural Preferences",
        "budget": "Budget",
        "duration": "Trip Duration",
        "days": "days",
        "cultural_interests": "Cultural Interests",
        "ancient_history": "Ancient History",
        "religious_heritage": "Religious Heritage",
        "museums": "Art & Museums",
        "architecture": "Architecture",
        "traditional_crafts": "Traditional Crafts",
        "folk_music": "Folk Music & Dance",
        "culinary_traditions": "Culinary Traditions",
        "archaeological_sites": "Archaeological Sites",
        "local_festivals": "Local Festivals",
        "traditional_markets": "Traditional Markets",
        "cultural_depth": "Cultural Depth",
        "surface_explorer": "Surface Explorer - Popular highlights",
        "culture_enthusiast": "Culture Enthusiast - Deeper experiences",
        "heritage_scholar": "Heritage Scholar - Immersive study",
        "preferred_regions": "Preferred Regions",
        "greek_islands": "Greek Islands",
        "turkish_coast": "Turkish Coast",
        "egyptian_nile": "Egyptian Nile",
        "italian_peninsula": "Italian Peninsula",
        "spanish_coast": "Spanish Coast",
        "moroccan_cities": "Moroccan Cities",
        "french_riviera": "French Riviera",
        "croatian_coast": "Croatian Coast",
        "group_type": "Group Type",
        "solo_explorer": "Solo Cultural Explorer",
        "couple": "Couple",
        "family": "Family with Children",
        "friends": "Friends Group",
        "study_group": "Cultural Study Group",
        "create_journey": "Create Cultural Journey",
        "cultural_odyssey": "10-Day Greek Cultural Odyssey",
        "location": "Location",
        "cultural_focus": "Cultural Focus",
        "experience": "Experience",
        "cost": "Cost",
        "total_cost": "Total Cultural Experience Cost",
        "remaining": "remaining for accommodation & meals",
        "cultural_insights_summary": "Cultural Insights",
        "visited": "visited",
        "historical_periods": "Historical Periods",
        "covered": "covered",
        "cultural_activities": "Cultural Activities",
        "included": "included"
    }
}

# Sidebar for navigation
with st.sidebar:
    st.image("https://images.unsplash.com/photo-1544737151307-6073c4b46e6d?w=300&h=200&fit=crop", 
             caption="Mediterranean Gateway", width=250)
    
    selected_lang = st.selectbox("🌍 Language / اللغة", list(languages.keys()))
    lang_code = languages[selected_lang]
    
    # RTL support for Arabic
    if lang_code == "ar":
        st.markdown('<div class="rtl-text">', unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Get current language text
    t = texts.get(lang_code, texts["en"])
    
    page = st.radio(f"📍 {t['navigation']}", [
        f"🏛️ {t['home']}",
        f"🗺️ {t['planner']}", 
        f"🏺 {t['heritage']}",
        f"🎭 {t['experiences']}",
        f"🏨 {t['stays']}",
        f"📊 {t['insights']}",
        f"💳 {t['booking']}"
    ])

# Main content based on page selection
if page == f"🏛️ {t['home']}":
    if lang_code == "ar":
        st.markdown(f'<h1 class="main-header rtl-text">{t["title"]}</h1>', unsafe_allow_html=True)
        st.markdown(f'<h3 style="text-align: center; color: #666;" class="rtl-text">{t["subtitle"]}</h3>', unsafe_allow_html=True)
    else:
        st.markdown(f'<h1 class="main-header">{t["title"]}</h1>', unsafe_allow_html=True)
        st.markdown(f'<h3 style="text-align: center; color: #666;">{t["subtitle"]}</h3>', unsafe_allow_html=True)
    
    # Hero metrics
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric(f"🏛️ {t['heritage_sites']}", "342", delta="18 new")
    with col2:
        st.metric(f"🎭 {t['cultural_experiences']}", "156", delta="12 added")
    with col3:
        st.metric(f"⭐ {t['cultural_rating']}", "4.9/5", delta="0.1")
    with col4:
        st.metric(f"🌍 {t['cultural_explorers']}", "23,567", delta="451")
    
    st.markdown("---")
    
    # Featured Mediterranean regions
    st.subheader(f"🌟 {t['featured_regions']}")
    
    # Translate table headers and data based on language
    if lang_code == "ar":
        regions_data = {
            'المنطقة': ['اليونان', 'تركيا', 'مصر', 'إيطاليا', 'إسبانيا', 'المغرب'],
            f'{t["unesco_sites"]}': [18, 19, 7, 58, 49, 9],
            'التجارب الثقافية': ['الآثار القديمة', 'التراث البيزنطي', 'عجائب الفراعنة', 'فن عصر النهضة', 'العمارة المورية', 'التقاليد البربرية'],
            f'{t["best_season"]}': ['أبر-أكت', 'مايو-سبت', 'أكت-أبر', 'أبر-أكت', 'مار-نوف', 'أكت-مايو'],
            f'{t["avg_tour"]} (EUR)': [850, 720, 690, 950, 780, 650],
            f'{t["heritage_rating"]}': [4.9, 4.8, 4.9, 4.9, 4.7, 4.8]
        }
    else:
        regions_data = {
            'Region': ['Greece', 'Turkey', 'Egypt', 'Italy', 'Spain', 'Morocco'],
            f'{t["unesco_sites"]}': [18, 19, 7, 58, 49, 9],
            'Cultural Experiences': ['Ancient Ruins', 'Byzantine Heritage', 'Pharaonic Wonders', 'Renaissance Art', 'Moorish Architecture', 'Berber Traditions'],
            f'{t["best_season"]}': ['Apr-Oct', 'May-Sep', 'Oct-Apr', 'Apr-Oct', 'Mar-Nov', 'Oct-May'],
            f'{t["avg_tour"]} (EUR)': [850, 720, 690, 950, 780, 650],
            f'{t["heritage_rating"]}': [4.9, 4.8, 4.9, 4.9, 4.7, 4.8]
        }
    
    df_regions = pd.DataFrame(regions_data)
    st.dataframe(df_regions, use_container_width=True)
    
    # Heritage sites showcase (instead of map)
    st.subheader(f"📍 {t['heritage_map']}")
    
    heritage_locations = [
        {"city": "Athens", "country": "Greece", "sites": 8, "score": 95},
        {"city": "Cairo", "country": "Egypt", "sites": 15, "score": 98},
        {"city": "Rome", "country": "Italy", "sites": 22, "score": 99},
        {"city": "Istanbul", "country": "Turkey", "sites": 12, "score": 87},
        {"city": "Madrid", "country": "Spain", "sites": 18, "score": 89},
        {"city": "Casablanca", "country": "Morocco", "sites": 6, "score": 85}
    ]
    
    for location in heritage_locations:
        col1, col2, col3 = st.columns([2, 1, 1])
        with col1:
            st.markdown(f"**🏛️ {location['city']}, {location['country']}**")
        with col2:
            st.metric(f"{t['heritage_sites']}", location['sites'])
        with col3:
            st.metric("Cultural Score", f"{location['score']}/100")
    
    # Cultural experience categories
    st.subheader(f"🎭 {t['experience_categories']}")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        euro_symbol = "€"
        if lang_code == "ar":
            st.markdown(f"""
            <div class="culture-card rtl-text">
                <h4>🏛️ {t['ancient_civilizations']}</h4>
                <p>{t['ancient_desc']}</p>
                <strong>{t['from']} {euro_symbol}120/{t['day']}</strong>
            </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown(f"""
            <div class="culture-card">
                <h4>🏛️ {t['ancient_civilizations']}</h4>
                <p>{t['ancient_desc']}</p>
                <strong>{t['from']} {euro_symbol}120/{t['day']}</strong>
            </div>
            """, unsafe_allow_html=True)
    
    with col2:
        if lang_code == "ar":
            st.markdown(f"""
            <div class="culture-card rtl-text">
                <h4>🎨 {t['art_architecture']}</h4>
                <p>{t['art_desc']}</p>
                <strong>{t['from']} {euro_symbol}95/{t['day']}</strong>
            </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown(f"""
            <div class="culture-card">
                <h4>🎨 {t['art_architecture']}</h4>
                <p>{t['art_desc']}</p>
                <strong>{t['from']} {euro_symbol}95/{t['day']}</strong>
            </div>
            """, unsafe_allow_html=True)
    
    with col3:
        if lang_code == "ar":
            st.markdown(f"""
            <div class="culture-card rtl-text">
                <h4>🍷 {t['culinary_heritage']}</h4>
                <p>{t['culinary_desc']}</p>
                <strong>{t['from']} {euro_symbol}80/{t['day']}</strong>
            </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown(f"""
            <div class="culture-card">
                <h4>🍷 {t['culinary_heritage']}</h4>
                <p>{t['culinary_desc']}</p>
                <strong>{t['from']} {euro_symbol}80/{t['day']}</strong>
            </div>
            """, unsafe_allow_html=True)

elif page == f"🗺️ {t['planner']}":
    st.header(f"🗺️ {t['planner']}")
    st.markdown("Create personalized cultural journeys across the Mediterranean" if lang_code == "en" else "إنشاء رحلات ثقافية شخصية عبر البحر الأبيض المتوسط")
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.subheader(t['cultural_preferences'])
        
        budget = st.slider(f"💰 {t['budget']} (EUR)", 800, 8000, 2500)
        duration = st.slider(f"📅 {t['duration']} ({t['days']})", 5, 28, 10)
        
        cultural_interests = st.multiselect(f"🏛️ {t['cultural_interests']}", [
            t["ancient_history"], t["religious_heritage"], t["museums"], t["architecture"],
            t["traditional_crafts"], t["folk_music"], t["culinary_traditions"], 
            t["archaeological_sites"], t["local_festivals"], t["traditional_markets"]
        ], default=[t["ancient_history"], t["museums"]])
        
        travel_depth = st.radio(f"📚 {t['cultural_depth']}", [
            t["surface_explorer"],
            t["culture_enthusiast"], 
            t["heritage_scholar"]
        ])
        
        preferred_regions = st.multiselect(f"🌍 {t['preferred_regions']}", [
            t["greek_islands"], t["turkish_coast"], t["egyptian_nile"], t["italian_peninsula"],
            t["spanish_coast"], t["moroccan_cities"], t["french_riviera"], t["croatian_coast"]
        ], default=[t["greek_islands"]])
        
        group_type = st.selectbox(f"👥 {t['group_type']}", [
            t["solo_explorer"], t["couple"], t["family"], 
            t["friends"], t["study_group"]
        ])
    
    with col2:
        st.subheader("Generated Cultural Itinerary" if lang_code == "en" else "مسار رحلة ثقافية مُولَّد")
        
        if st.button(f"🚀 {t['create_journey']}"):
            with st.spinner("Crafting your personalized cultural experience..." if lang_code == "en" else "إعداد تجربتك الثقافية الشخصية..."):
                import time
                time.sleep(3)
                
                st.success("✅ Your Mediterranean cultural journey is ready!" if lang_code == "en" else "✅ رحلتك الثقافية المتوسطية جاهزة!")
                
                # Sample cultural itinerary
                st.markdown(f"### 🏛️ {t['cultural_odyssey']}")
                
                euro_symbol = "€"
                if lang_code == "ar":
                    cultural_itinerary = [
                        {"اليوم": 1, "الموقع": "أثينا", "التركيز الثقافي": "الأكروبوليس والأغورا القديمة", "التجربة": "جولة أثرية مع مؤرخ", "التكلفة": f"{euro_symbol}180"},
                        {"اليوم": 2, "الموقع": "أثينا", "التركيز الثقافي": "المتحف الأثري الوطني", "التجربة": "جولة خاصة مع أمين المتحف", "التكلفة": f"{euro_symbol}120"},
                        {"اليوم": 3, "الموقع": "دلفي", "التركيز الثقافي": "وحي دلفي", "التجربة": "ورشة الدين اليوناني القديم", "التكلفة": f"{euro_symbol}200"},
                        {"اليوم": 4, "الموقع": "ميتيورا", "التركيز الثقافي": "الأديرة البيزنطية", "التجربة": "الفن والعمارة الأرثوذكسية", "التكلفة": f"{euro_symbol}150"},
                        {"اليوم": 5, "الموقع": "ثيسالونيكي", "التركيز الثقافي": "الكنائس البيزنطية", "التجربة": "جولة التراث العالمي لليونسكو", "التكلفة": f"{euro_symbol}140"}
                    ]
                else:
                    cultural_itinerary = [
                        {"Day": 1, "Location": "Athens", "Cultural Focus": "Acropolis & Ancient Agora", "Experience": "Archaeological tour with historian", "Cost": f"{euro_symbol}180"},
                        {"Day": 2, "Location": "Athens", "Cultural Focus": "National Archaeological Museum", "Experience": "Private curator-led tour", "Cost": f"{euro_symbol}120"},
                        {"Day": 3, "Location": "Delphi", "Cultural Focus": "Oracle of Delphi", "Experience": "Ancient Greek religion workshop", "Cost": f"{euro_symbol}200"},
                        {"Day": 4, "Location": "Meteora", "Cultural Focus": "Byzantine Monasteries", "Experience": "Orthodox art & architecture", "Cost": f"{euro_symbol}150"},
                        {"Day": 5, "Location": "Thessaloniki", "Cultural Focus": "Byzantine Churches", "Experience": "UNESCO World Heritage tour", "Cost": f"{euro_symbol}140"}
                    ]
                
                df_cultural_itinerary = pd.DataFrame(cultural_itinerary)
                st.dataframe(df_cultural_itinerary, use_container_width=True)
                
                total_cultural_cost = sum([int(item[list(item.keys())[-1]].replace(euro_symbol, "")) for item in cultural_itinerary])
                st.metric(f"💰 {t['total_cost']}", f"{euro_symbol}{total_cultural_cost}", 
                         delta=f"{euro_symbol}{budget-total_cultural_cost} {t['remaining']}")
                
                # Cultural insights
                st.markdown(f"### 📚 {t['cultural_insights_summary']}")
                col_a, col_b, col_c = st.columns(3)
                with col_a:
                    st.metric(f"🏛️ {t['unesco_sites']}", "12", t['visited'])
                with col_b:
                    st.metric(f"📜 {t['historical_periods']}", "6", t['covered'])
                with col_c:
                    st.metric(f"🎭 {t['cultural_activities']}", "15", t['included'])

elif page == f"🏺 {t['heritage']}":
    st.header(f"🏺 {t['heritage']}")
    st.markdown("Explore authenticated cultural treasures across the Mediterranean" if lang_code == "en" else "استكشف الكنوز الثقافية الموثقة عبر البحر الأبيض المتوسط")
    
    # Heritage sites with detailed information
    heritage_sites = [
        {
            "name": "Acropolis of Athens" if lang_code == "en" else "أكروبوليس أثينا",
            "country": "Greece" if lang_code == "en" else "اليونان",
            "year": 1987,
            "description": "Symbol of democracy and Western civilization" if lang_code == "en" else "رمز الديمقراطية والحضارة الغربية",
            "rating": 4.9
        },
        {
            "name": "Pyramids of Giza" if lang_code == "en" else "أهرامات الجيزة",
            "country": "Egypt" if lang_code == "en" else "مصر",
            "year": 1979,
            "description": "Last surviving Wonder of Ancient World" if lang_code == "en" else "آخر عجائب الدنيا السبع الباقية",
            "rating": 4.9
        },
        {
            "name": "Hagia Sophia" if lang_code == "en" else "آيا صوفيا",
            "country": "Turkey" if lang_code == "en" else "تركيا",
            "year": 1985,
            "description": "Masterpiece of Byzantine architecture" if lang_code == "en" else "تحفة العمارة البيزنطية",
            "rating": 4.8
        }
    ]
    
    for site in heritage_sites:
        with st.container():
            st.markdown(f"""
            <div class="heritage-site">
                <h4>🏛️ {site['name']}</h4>
                <p><strong>📍 {'Country' if lang_code == 'en' else 'البلد'}:</strong> {site['country']}</p>
                <p><strong>🏆 {'UNESCO Year' if lang_code == 'en' else 'سنة اليونسكو'}:</strong> {site['year']}</p>
                <p><strong>📚 {'Description' if lang_code == 'en' else 'الوصف'}:</strong> {site['description']}</p>
                <p><strong>⭐ {'Rating' if lang_code == 'en' else 'التقييم'}:</strong> {site['rating']}/5</p>
            </div>
            """, unsafe_allow_html=True)
            
            if st.button(f"{'Book Tour' if lang_code == 'en' else 'احجز جولة'}", key=f"book_{site['name']}"):
                st.success(f"✅ {'Tour booked successfully!' if lang_code == 'en' else 'تم حجز الجولة بنجاح!'}")

else:
    st.header("🚧 Page Under Development")
    st.info("This page is being developed. Please check back soon!" if lang_code == "en" else "هذه الصفحة قيد التطوير. يرجى المراجعة قريباً!")
    st.markdown(f"### {'Available Pages' if lang_code == 'en' else 'الصفحات المتاحة'}:")
    st.markdown(f"- ✅ {t['home']}")
    st.markdown(f"- ✅ {t['planner']}")
    st.markdown(f"- ✅ {t['heritage']}")
    st.markdown(f"- 🚧 {t['experiences']} ({'Coming Soon' if lang_code == 'en' else 'قريباً'})")
    st.markdown(f"- 🚧 {t['stays']} ({'Coming Soon' if lang_code == 'en' else 'قريباً'})")
    st.markdown(f"- 🚧 {t['insights']} ({'Coming Soon' if lang_code == 'en' else 'قريباً'})")
    st.markdown(f"- 🚧 {t['booking']} ({'Coming Soon' if lang_code == 'en' else 'قريباً'})")

# Footer with proper language support
st.markdown("---")
if lang_code == "ar":
    st.markdown("""
    <div style='text-align: center; color: #666; padding: 2rem;' class='rtl-text'>
        <h4>🏛️ بوابة المتوسط</h4>
        <p>بوابتك لاستكشاف كنوز البحر الأبيض المتوسط الثقافية | اتصل بنا: info@medgateway.com</p>
        <p>🌍 متوفر باللغات: العربية • English • Türkçe • Ελληνικά • Italiano • Español</p>
    </div>
    """, unsafe_allow_html=True)
else:
    st.markdown("""
    <div style='text-align: center; color: #666; padding: 2rem;'>
        <h4>🏛️ Mediterranean Gateway</h4>
        <p>Your gateway to Mediterranean cultural treasures | Contact: info@medgateway.com</p>
        <p>🌍 Available in: العربية • English • Türkçe • Ελληνικά • Italiano • Español</p>
    </div>
    """, unsafe_allow_html=True)