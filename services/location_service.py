class LocationService:
    # Comprehensive location database for Indian destinations
    LOCATION_DATABASE = {
        "Goa": {
            "attractions": [
                {"name": "Calangute Beach", "type": "beach", "description": "Popular beach with water sports"},
                {"name": "Anjuna Beach", "type": "beach", "description": "Famous for flea market and hippie culture"},
                {"name": "Fort Aguada", "type": "fort", "description": "17th-century Portuguese fort with lighthouse"},
                {"name": "Basilica of Bom Jesus", "type": "church", "description": "UNESCO World Heritage Site with St. Francis Xavier's remains"},
                {"name": "Dudhsagar Falls", "type": "waterfall", "description": "Spectacular waterfall in Western Ghats"},
                {"name": "Arambol Beach", "type": "beach", "description": "Peaceful beach with natural beauty"},
                {"name": "Chapora Fort", "type": "fort", "description": "Historic fort with panoramic views"},
                {"name": "Anjuna Flea Market", "type": "market", "description": "Weekly market for handicrafts and souvenirs"}
            ],
            "restaurants": [
                {"name": "Gunpowder", "cuisine": "Indian-Portuguese", "description": "Authentic Goan cuisine"},
                {"name": "Cafe Delmar", "cuisine": "Multi-cuisine", "description": "Beachfront dining"},
                {"name": "Bomra's", "cuisine": "Seafood", "description": "Fresh seafood specialties"}
            ],
            "hotels": [
                {"name": "The Leela Goa", "type": "luxury", "area": "Cavelossim"},
                {"name": "Park Hyatt Goa", "type": "luxury", "area": "Resort & Spa"},
                {"name": "Citrus Goa", "type": "boutique", "area": "Arpora"}
            ]
        },
        "Kerala": {
            "attractions": [
                {"name": "Alleppey Backwaters", "type": "backwater", "description": "Houseboat cruises through palm-fringed canals"},
                {"name": "Munnar Tea Gardens", "type": "hill_station", "description": "Rolling tea plantations and misty hills"},
                {"name": "Periyar Wildlife Sanctuary", "type": "wildlife", "description": "Tiger reserve with boat safaris"},
                {"name": "Fort Kochi", "type": "historical", "description": "Colonial architecture and Chinese fishing nets"},
                {"name": "Wayanad Wildlife", "type": "wildlife", "description": "Wildlife sanctuaries and trekking"},
                {"name": "Kovalam Beach", "type": "beach", "description": "Three beautiful crescent beaches"},
                {"name": "Athirappilly Falls", "type": "waterfall", "description": "Largest waterfall in Kerala"},
                {"name": "Marari Beach", "type": "beach", "description": "Unspoiled beach with luxury resorts"}
            ],
            "restaurants": [
                {"name": "Dal Roti", "cuisine": "Indian", "description": "Traditional Kerala cuisine"},
                {"name": "Fusion Bay", "cuisine": "Multi-cuisine", "description": "Modern dining with backwater views"},
                {"name": "The Rice Boat", "cuisine": "Kerala", "description": "Authentic local flavors"}
            ],
            "hotels": [
                {"name": "The Leela Kovalam", "type": "luxury", "area": "Beach Resort"},
                {"name": "Taj Malabar", "type": "luxury", "area": "Kochi"},
                {"name": "Abad Harmonia", "type": "boutique", "area": "Vagamon"}
            ]
        },
        "Rajasthan": {
            "attractions": [
                {"name": "Amber Fort", "type": "fort", "description": "Magnificent hilltop fort with palaces"},
                {"name": "City Palace Jaipur", "type": "palace", "description": "Royal residence with museums"},
                {"name": "Hawa Mahal", "type": "palace", "description": "Palace of Winds with 953 windows"},
                {"name": "Jantar Mantar", "type": "observatory", "description": "Ancient astronomical instruments"},
                {"name": "Udaipur City Palace", "type": "palace", "description": "Largest palace complex in Rajasthan"},
                {"name": "Lake Pichola", "type": "lake", "description": "Picturesque lake with island palaces"},
                {"name": "Jaisalmer Fort", "type": "fort", "description": "Golden fort in Thar Desert"},
                {"name": "Ranthambore National Park", "type": "wildlife", "description": "Famous for tiger safaris"}
            ],
            "restaurants": [
                {"name": "Chokhi Dhani", "cuisine": "Rajasthani", "description": "Cultural dining experience"},
                {"name": "Suvarna Mahal", "cuisine": "Royal", "description": "Palace dining with traditional food"},
                {"name": "The Rajput Room", "cuisine": "Rajasthani", "description": "Authentic royal cuisine"}
            ],
            "hotels": [
                {"name": "The Oberoi Rajvilas", "type": "luxury", "area": "Jaipur"},
                {"name": "Taj Lake Palace", "type": "luxury", "area": "Udaipur"},
                {"name": "Sujan Rajmahal", "type": "palace", "area": "Jaipur"}
            ]
        },
        "Himachal Pradesh": {
            "attractions": [
                {"name": "Shimla Mall Road", "type": "street", "description": "Colonial architecture and shopping"},
                {"name": "Manali Valley", "type": "valley", "description": "Picturesque valley with mountains"},
                {"name": "Rohtang Pass", "type": "pass", "description": "Mountain pass with snow activities"},
                {"name": "Dharamshala Monastery", "type": "monastery", "description": "Tibetan Buddhist monastery"},
                {"name": "Kullu Valley", "type": "valley", "description": "Apple orchards and temples"},
                {"name": "Chail Palace", "type": "palace", "description": "Former royal residence"},
                {"name": "Great Himalayan National Park", "type": "national_park", "description": "UNESCO site with wildlife"},
                {"name": "Narkanda", "type": "hill_station", "description": "Apple country with scenic views"}
            ],
            "restaurants": [
                {"name": "The Mall Road Cafe", "cuisine": "Continental", "description": "European-style cafe"},
                {"name": "Johnson's Cafe", "cuisine": "Multi-cuisine", "description": "Historic cafe in Shimla"},
                {"name": "Tibetan Kitchen", "cuisine": "Tibetan", "description": "Authentic Tibetan food"}
            ],
            "hotels": [
                {"name": "The Oberoi Cecil", "type": "luxury", "area": "Shimla"},
                {"name": "Manuallaya", "type": "boutique", "area": "Manali"},
                {"name": "Wildflower Hall", "type": "luxury", "area": "Shimla"}
            ]
        },
        "Uttarakhand": {
            "attractions": [
                {"name": "Rishikesh", "type": "spiritual", "description": "Yoga capital with Ganges river"},
                {"name": "Mussoorie", "type": "hill_station", "description": "Queen of Hills with colonial charm"},
                {"name": "Nainital", "type": "lake", "description": "Lake city with mountain views"},
                {"name": "Valley of Flowers", "type": "valley", "description": "UNESCO site with alpine flowers"},
                {"name": "Hemkund Sahib", "type": "pilgrimage", "description": "Sikh pilgrimage site"},
                {"name": "Auli", "type": "ski_resort", "description": "Asia's finest ski destination"},
                {"name": "Jim Corbett National Park", "type": "wildlife", "description": "First national park of India"},
                {"name": "Badrinath Temple", "type": "temple", "description": "Ancient Hindu temple"}
            ],
            "restaurants": [
                {"name": "The 6th Element", "cuisine": "Continental", "description": "Rooftop dining in Rishikesh"},
                {"name": "Sher-e-Punjab", "cuisine": "Punjabi", "description": "Traditional Punjabi food"},
                {"name": "Sakley's Restaurant", "cuisine": "Multi-cuisine", "description": "Local specialties"}
            ],
            "hotels": [
                {"name": "Ananda in the Himalayas", "type": "luxury", "area": "Rishikesh"},
                {"name": "The Zostel", "type": "budget", "area": "Rishikesh"},
                {"name": "Jim's Jungle Retreat", "type": "eco", "area": "Corbett"}
            ]
        },
        "Mumbai": {
            "attractions": [
                {"name": "Gateway of India", "type": "monument", "description": "Iconic arch monument"},
                {"name": "Marine Drive", "type": "promenade", "description": "Queen's Necklace seafront"},
                {"name": "Elephanta Caves", "type": "caves", "description": "UNESCO site with rock-cut sculptures"},
                {"name": "Chhatrapati Shivaji Terminus", "type": "railway", "description": "UNESCO World Heritage Site"},
                {"name": "Juhu Beach", "type": "beach", "description": "Popular beach with street food"},
                {"name": "Siddhivinayak Temple", "type": "temple", "description": "Popular Hindu temple"},
                {"name": "Colaba Causeway", "type": "market", "description": "Street shopping and antiques"},
                {"name": "Haji Ali Dargah", "type": "dargah", "description": "Islamic shrine on sea"}
            ],
            "restaurants": [
                {"name": "The Table", "cuisine": "Modern Indian", "description": "Contemporary Indian cuisine"},
                {"name": "Bombay Canteen", "cuisine": "Street Food", "description": "Authentic Mumbai street food"},
                {"name": "Aer", "cuisine": "Fine Dining", "description": "Four Seasons rooftop restaurant"}
            ],
            "hotels": [
                {"name": "The Taj Mahal Palace", "type": "luxury", "area": "Colaba"},
                {"name": "The Oberoi Mumbai", "type": "luxury", "area": "Nariman Point"},
                {"name": "Trishara", "type": "boutique", "area": "Fort"}
            ]
        },
        "Delhi": {
            "attractions": [
                {"name": "Red Fort", "type": "fort", "description": "UNESCO site, Mughal architecture"},
                {"name": "India Gate", "type": "monument", "description": "War memorial with gardens"},
                {"name": "Qutub Minar", "type": "minaret", "description": "Tallest brick minaret in world"},
                {"name": "Humayun's Tomb", "type": "tomb", "description": "Mughal architecture masterpiece"},
                {"name": "Lotus Temple", "type": "temple", "description": "Bahai House of Worship"},
                {"name": "Akshardham Temple", "type": "temple", "description": "Modern Hindu temple complex"},
                {"name": "Chandni Chowk", "type": "market", "description": "Historic market with street food"},
                {"name": "Rashtrapati Bhavan", "type": "presidential", "description": "President's residence"}
            ],
            "restaurants": [
                {"name": "Karim's", "cuisine": "Mughlai", "description": "Historic restaurant since 1913"},
                {"name": "Indian Accent", "cuisine": "Modern Indian", "description": "Michelin-starred Indian cuisine"},
                {"name": "The Spice Route", "cuisine": "Regional Indian", "description": "Pan-India culinary journey"}
            ],
            "hotels": [
                {"name": "The Imperial", "type": "luxury", "area": "Janpath"},
                {"name": "ITC Maurya", "type": "luxury", "area": "Sardar Patel Marg"},
                {"name": "The Lodhi", "type": "boutique", "area": "Lodhi Road"}
            ]
        },
        "Agra": {
            "attractions": [
                {"name": "Taj Mahal", "type": "mausoleum", "description": "UNESCO World Heritage Site"},
                {"name": "Agra Fort", "type": "fort", "description": "Red sandstone Mughal fort"},
                {"name": "Fatehpur Sikri", "type": "city", "description": "Abandoned Mughal city"},
                {"name": "Itmad-ud-Daulah", "type": "tomb", "description": "Baby Taj with intricate marble work"},
                {"name": "Mehtab Bagh", "type": "garden", "description": "Moonlight garden across Yamuna"},
                {"name": "Kinari Bazaar", "type": "market", "description": "Marble crafts and souvenirs"},
                {"name": "Jama Masjid", "type": "mosque", "description": "Largest mosque in India"},
                {"name": "Sikandra", "type": "tomb", "description": "Akbar's tomb with mixed architecture"}
            ],
            "restaurants": [
                {"name": "Dasaprakash", "cuisine": "South Indian", "description": "Famous for fresh idlis"},
                {"name": "Peshawri", "cuisine": "North Indian", "description": "Taj Hotel's iconic restaurant"},
                {"name": "Chaat Corner", "cuisine": "Street Food", "description": "Local Agra street food"}
            ],
            "hotels": [
                {"name": "The Oberoi Amarvilas", "type": "luxury", "area": "Taj View"},
                {"name": "ITC Mughal", "type": "luxury", "area": "Agra"},
                {"name": "Trident Agra", "type": "business", "area": "Fatehabad Road"}
            ]
        },
        "Varanasi": {
            "attractions": [
                {"name": "Dashashwamedh Ghat", "type": "ghat", "description": "Main ghat for evening aarti"},
                {"name": "Assi Ghat", "type": "ghat", "description": "Southernmost ghat with temples"},
                {"name": "Kashi Vishwanath Temple", "type": "temple", "description": "Golden temple dedicated to Shiva"},
                {"name": "Sarnath", "type": "archaeological", "description": "Buddhist pilgrimage site"},
                {"name": "Ramanagar Fort", "type": "fort", "description": "Royal residence across Ganges"},
                {"name": "Tulsi Manas Temple", "type": "temple", "description": "Temple dedicated to Lord Rama"},
                {"name": "Banaras Hindu University", "type": "university", "description": "Asia's largest residential university"},
                {"name": "Alamgir Mosque", "type": "mosque", "description": "17th-century mosque"}
            ],
            "restaurants": [
                {"name": "Beni Prasad", "cuisine": "Sweets", "description": "Famous for Banarasi pedas"},
                {"name": "Kashi Chat Bhandar", "cuisine": "Street Food", "description": "Authentic street food"},
                {"name": "Ramana Cafe", "cuisine": "Cafe", "description": "Modern cafe with Ganges view"}
            ],
            "hotels": [
                {"name": "Taj Ganges", "type": "luxury", "area": "Varanasi"},
                {"name": "Ramada Plaza JHV", "type": "business", "area": "JHV"},
                {"name": "Hotel Ganges View", "type": "boutique", "area": "Assi Ghat"}
            ]
        },
        "Jaipur": {
            "attractions": [
                {"name": "Amber Fort", "type": "fort", "description": "Hilltop fort with palaces"},
                {"name": "City Palace", "type": "palace", "description": "Royal residence with museums"},
                {"name": "Hawa Mahal", "type": "palace", "description": "Palace of Winds"},
                {"name": "Jantar Mantar", "type": "observatory", "description": "Ancient astronomical instruments"},
                {"name": "Nahargarh Fort", "type": "fort", "description": "Fort with city views"},
                {"name": "Jaigarh Fort", "type": "fort", "description": "Fort with world's largest cannon"},
                {"name": "Albert Hall Museum", "type": "museum", "description": "Victoria and Albert style museum"},
                {"name": "Birla Temple", "type": "temple", "description": "White marble temple"}
            ],
            "restaurants": [
                {"name": "Suvarna Mahal", "cuisine": "Rajasthani", "description": "Palace dining experience"},
                {"name": "Chokhi Dhani", "cuisine": "Rajasthani", "description": "Cultural village restaurant"},
                {"name": "The Rajput Room", "cuisine": "Royal", "description": "Traditional royal cuisine"}
            ],
            "hotels": [
                {"name": "Rambagh Palace", "type": "luxury", "area": "Jaipur"},
                {"name": "The Oberoi Rajvilas", "type": "luxury", "area": "Jaipur"},
                {"name": "Sujan Rajmahal", "type": "palace", "area": "Jaipur"}
            ]
        },
        "Udaipur": {
            "attractions": [
                {"name": "City Palace", "type": "palace", "description": "Largest palace complex in Rajasthan"},
                {"name": "Lake Pichola", "type": "lake", "description": "Picturesque lake with island palaces"},
                {"name": "Jag Mandir", "type": "palace", "description": "Lake palace with marble elephants"},
                {"name": "Saheliyon ki Bari", "type": "garden", "description": "Garden of the Maidens"},
                {"name": "Fateh Sagar Lake", "type": "lake", "description": "Artificial lake with islands"},
                {"name": "Monsoon Palace", "type": "palace", "description": "Hilltop palace with city views"},
                {"name": "Bagore ki Haveli", "type": "haveli", "description": "Museum showcasing royal lifestyle"},
                {"name": "Ahar Museum", "type": "museum", "description": "Archaeological museum"}
            ],
            "restaurants": [
                {"name": "Jagat Niwas Palace", "cuisine": "Multi-cuisine", "description": "Palace dining"},
                {"name": "Ambrai", "cuisine": "Rajasthani", "description": "Traditional Rajasthani food"},
                {"name": "Udaivilas", "cuisine": "Modern Indian", "description": "Luxury resort dining"}
            ],
            "hotels": [
                {"name": "Taj Lake Palace", "type": "luxury", "area": "Lake Pichola"},
                {"name": "The Oberoi Udaivilas", "type": "luxury", "area": "Udaipur"},
                {"name": "Shiv Niwas Palace", "type": "heritage", "area": "City Palace"}
            ]
        },
        "Pondicherry": {
            "attractions": [
                {"name": "Promenade Beach", "type": "beach", "description": "Seaside promenade with French architecture"},
                {"name": "Auroville", "type": "spiritual", "description": "International township and Matrimandir"},
                {"name": "Sri Aurobindo Ashram", "type": "ashram", "description": "Spiritual center founded by Sri Aurobindo"},
                {"name": "French Quarter", "type": "colonial", "description": "White Town with French colonial buildings"},
                {"name": "Paradise Beach", "type": "beach", "description": "Uncrowded beach near Auroville"},
                {"name": "Pondicherry Museum", "type": "museum", "description": "Museum with bronze sculptures"},
                {"name": "Serenity Beach", "type": "beach", "description": "Quiet beach for relaxation"},
                {"name": "Chunnambar Boat House", "type": "boathouse", "description": "Backwater boat rides"}
            ],
            "restaurants": [
                {"name": "Le Club", "cuisine": "French", "description": "Authentic French cuisine"},
                {"name": "Satsanga", "cuisine": "Multi-cuisine", "description": "Ashram canteen"},
                {"name": "Le Dupleix", "cuisine": "French-Indian", "description": "Colonial-style dining"}
            ],
            "hotels": [
                {"name": "Palais de Mahe", "type": "boutique", "area": "French Quarter"},
                {"name": "The Promenade", "type": "boutique", "area": "Beachfront"},
                {"name": "Hotel de l'Orient", "type": "heritage", "area": "French Quarter"}
            ]
        },
        "Shimla": {
            "attractions": [
                {"name": "Mall Road", "type": "street", "description": "Colonial shopping street"},
                {"name": "Jakhu Temple", "type": "temple", "description": "Ancient temple with Hanuman statue"},
                {"name": "Christ Church", "type": "church", "description": "Gothic architecture church"},
                {"name": "Vice Regal Lodge", "type": "lodge", "description": "Former viceroy's residence"},
                {"name": "Summer Hill", "type": "hill", "description": "Pine-covered hill with views"},
                {"name": "Annandale", "type": "grounds", "description": "Grounds for picnics and walks"},
                {"name": "Tara Devi Temple", "type": "temple", "description": "Temple with panoramic views"},
                {"name": "Himachal State Museum", "type": "museum", "description": "Museum showcasing local culture"}
            ],
            "restaurants": [
                {"name": "Indian Coffee House", "cuisine": "Continental", "description": "Historic cafe"},
                {"name": "Wake n Bake", "cuisine": "Cafe", "description": "Modern cafe with views"},
                {"name": "The Mall Road Cafe", "cuisine": "Multi-cuisine", "description": "Street-side dining"}
            ],
            "hotels": [
                {"name": "The Oberoi Cecil", "type": "luxury", "area": "Shimla"},
                {"name": "Wildflower Hall", "type": "luxury", "area": "Shimla"},
                {"name": "Clarkes Hotel", "type": "heritage", "area": "Shimla"}
            ]
        },
        "Manali": {
            "attractions": [
                {"name": "Solang Valley", "type": "valley", "description": "Adventure sports and snow activities"},
                {"name": "Rohtang Pass", "type": "pass", "description": "Mountain pass with glaciers"},
                {"name": "Hadimba Temple", "type": "temple", "description": "Ancient wooden temple"},
                {"name": "Vashisht Hot Springs", "type": "springs", "description": "Natural hot water springs"},
                {"name": "Manu Temple", "type": "temple", "description": "Temple dedicated to sage Manu"},
                {"name": "Old Manali", "type": "village", "description": "Picturesque village with cafes"},
                {"name": "Great Himalayan National Park", "type": "park", "description": "UNESCO site with wildlife"},
                {"name": "Bhrigu Lake", "type": "lake", "description": "Sacred lake at high altitude"}
            ],
            "restaurants": [
                {"name": "Johnson's Cafe", "cuisine": "Continental", "description": "Historic cafe"},
                {"name": "The Lazy Dog Lounge", "cuisine": "Cafe", "description": "Modern cafe with pizzas"},
                {"name": "Tibetan Kitchen", "cuisine": "Tibetan", "description": "Authentic Tibetan food"}
            ],
            "hotels": [
                {"name": "Manuallaya", "type": "boutique", "area": "Manali"},
                {"name": "The Himalayan", "type": "luxury", "area": "Manali"},
                {"name": "Apple View", "type": "boutique", "area": "Manali"}
            ]
        },
        "Leh Ladakh": {
            "attractions": [
                {"name": "Pangong Lake", "type": "lake", "description": "High-altitude brackish lake"},
                {"name": "Nubra Valley", "type": "valley", "description": "Valley with sand dunes and Bactrian camels"},
                {"name": "Thiksey Monastery", "type": "monastery", "description": "Largest monastery in Ladakh"},
                {"name": "Hemis Monastery", "type": "monastery", "description": "Famous for Hemis Festival"},
                {"name": "Magnetic Hill", "type": "phenomenon", "description": "Optical illusion hill"},
                {"name": "Khardung La", "type": "pass", "description": "World's highest motorable pass"},
                {"name": "Leh Palace", "type": "palace", "description": "Former royal residence"},
                {"name": "Shanti Stupa", "type": "stupa", "description": "Peace Pagoda with city views"}
            ],
            "restaurants": [
                {"name": "Gesmo", "cuisine": "Ladakhi", "description": "Traditional Ladakhi cuisine"},
                {"name": "Summer Harvest", "cuisine": "Continental", "description": "European-style cafe"},
                {"name": "Namza Cafe", "cuisine": "Tibetan", "description": "Tibetan and Chinese food"}
            ],
            "hotels": [
                {"name": "The Grand Dragon", "type": "luxury", "area": "Leh"},
                {"name": "Spic n Span", "type": "boutique", "area": "Leh"},
                {"name": "Hotel Ladakh", "type": "heritage", "area": "Leh"}
            ]
        },
        "Kashmir": {
            "attractions": [
                {"name": "Dal Lake", "type": "lake", "description": "Urban lake with houseboats"},
                {"name": "Shalimar Bagh", "type": "garden", "description": "Mughal garden with fountains"},
                {"name": "Nishat Bagh", "type": "garden", "description": "Terraced Mughal garden"},
                {"name": "Pahalgam", "type": "valley", "description": "Valley for trekking and skiing"},
                {"name": "Gulmarg", "type": "resort", "description": "Ski resort with gondola"},
                {"name": "Sonamarg", "type": "valley", "description": "Meadow of gold with glaciers"},
                {"name": "Chashme Shahi", "type": "garden", "description": "Royal spring garden"},
                {"name": "Hazratbal Shrine", "type": "shrine", "description": "Islamic shrine on Dal Lake"}
            ],
            "restaurants": [
                {"name": "Ahdoos", "cuisine": "Kashmiri", "description": "Traditional Kashmiri cuisine"},
                {"name": "Mughal Darbar", "cuisine": "Mughlai", "description": "Royal Mughal food"},
                {"name": "The Floating Cafe", "cuisine": "Continental", "description": "Houseboat dining"}
            ],
            "hotels": [
                {"name": "Vivanta Dal View", "type": "luxury", "area": "Srinagar"},
                {"name": "The Lalit Grand Palace", "type": "luxury", "area": "Srinagar"},
                {"name": "Houseboats", "type": "unique", "area": "Dal Lake"}
            ]
        },
        "Bangalore": {
            "attractions": [
                {"name": "Lalbagh Botanical Garden", "type": "garden", "description": "Largest botanical garden in India"},
                {"name": "Cubbon Park", "type": "park", "description": "Green lung of the city"},
                {"name": "Vidhana Soudha", "type": "building", "description": "Seat of Karnataka legislature"},
                {"name": "Bangalore Palace", "type": "palace", "description": "Tudor-style palace"},
                {"name": "ISKCON Temple", "type": "temple", "description": "Hare Krishna temple"},
                {"name": "Commercial Street", "type": "market", "description": "Shopping district"},
                {"name": "MG Road", "type": "street", "description": "Main commercial street"},
                {"name": "Nandi Hills", "type": "hill", "description": "Hill station near Bangalore"}
            ],
            "restaurants": [
                {"name": "Koshy's", "cuisine": "Continental", "description": "Historic restaurant"},
                {"name": "Toit", "cuisine": "Brewpub", "description": "Microbrewery and pub"},
                {"name": "Karavalli", "cuisine": "Coastal", "description": "Authentic coastal cuisine"}
            ],
            "hotels": [
                {"name": "The Oberoi", "type": "luxury", "area": "Bangalore"},
                {"name": "ITC Gardenia", "type": "luxury", "area": "Bangalore"},
                {"name": "The Leela Palace", "type": "luxury", "area": "Bangalore"}
            ]
        },
        "Chennai": {
            "attractions": [
                {"name": "Marina Beach", "type": "beach", "description": "Second longest urban beach in world"},
                {"name": "Kapaleeshwarar Temple", "type": "temple", "description": "Dravidian architecture temple"},
                {"name": "Fort St. George", "type": "fort", "description": "British fort and museum"},
                {"name": "San Thome Basilica", "type": "church", "description": "Cathedral with St. Thomas tomb"},
                {"name": "Government Museum", "type": "museum", "description": "Natural history and art museum"},
                {"name": "T. Nagar Shopping", "type": "market", "description": "Popular shopping district"},
                {"name": "Valluvar Kottam", "type": "monument", "description": "Monument to Tamil poet"},
                {"name": "Guindy National Park", "type": "park", "description": "Urban national park"}
            ],
            "restaurants": [
                {"name": "Murugan Idli Shop", "cuisine": "South Indian", "description": "Famous for idlis"},
                {"name": "The Bombay Canteen", "cuisine": "Street Food", "description": "Modern Indian street food"},
                {"name": "Benjarong", "cuisine": "Thai", "description": "Authentic Thai cuisine"}
            ],
            "hotels": [
                {"name": "ITC Grand Chola", "type": "luxury", "area": "Chennai"},
                {"name": "The Leela Palace", "type": "luxury", "area": "Chennai"},
                {"name": "Taj Coromandel", "type": "luxury", "area": "Chennai"}
            ]
        },
        "Kolkata": {
            "attractions": [
                {"name": "Victoria Memorial", "type": "memorial", "description": "White marble monument"},
                {"name": "Howrah Bridge", "type": "bridge", "description": "Iconic cantilever bridge"},
                {"name": "Kalighat Temple", "type": "temple", "description": "Famous Kali temple"},
                {"name": "South City Mall", "type": "mall", "description": "Largest mall in East India"},
                {"name": "Marble Palace", "type": "palace", "description": "19th-century palace with art"},
                {"name": "St. Paul's Cathedral", "type": "church", "description": "Gothic cathedral"},
                {"name": "New Market", "type": "market", "description": "Historic market complex"},
                {"name": "Princep Ghat", "type": "ghat", "description": "Riverside promenade"}
            ],
            "restaurants": [
                {"name": "6 Ballygunge Place", "cuisine": "Bengali", "description": "Authentic Bengali cuisine"},
                {"name": "Trincas", "cuisine": "Chinese", "description": "Historic Chinese restaurant"},
                {"name": "Barbecue", "cuisine": "Continental", "description": "Classic restaurant since 1934"}
            ],
            "hotels": [
                {"name": "The Oberoi Grand", "type": "luxury", "area": "Kolkata"},
                {"name": "ITC Royal Bengal", "type": "luxury", "area": "Kolkata"},
                {"name": "Taj Bengal", "type": "luxury", "area": "Kolkata"}
            ]
        },
        "Ayodhya": {
            "attractions": [
                {"name": "Ram Janmabhoomi Temple", "type": "temple", "description": "Birthplace of Lord Rama"},
                {"name": "Hanuman Garhi", "type": "temple", "description": "Temple dedicated to Hanuman"},
                {"name": "Kanak Bhawan Temple", "type": "temple", "description": "Temple with golden idols"},
                {"name": "Nageshwarnath Temple", "type": "temple", "description": "Ancient Shiva temple"},
                {"name": "Guptar Ghat", "type": "ghat", "description": "Sacred ghat on Sarayu River"},
                {"name": "Ramkot Fort", "type": "fort", "description": "Ancient fort walls"},
                {"name": "Treta Ke Thakur", "type": "temple", "description": "Temple marking Vishnu's incarnation"},
                {"name": "Janki Mahal", "type": "palace", "description": "Palace associated with Sita"}
            ],
            "restaurants": [
                {"name": "Ramana's Garden Cafe", "cuisine": "Cafe", "description": "Modern cafe with local flavors"},
                {"name": "Bansi Vihar", "cuisine": "Vegetarian", "description": "Traditional vegetarian food"},
                {"name": "Hotel Ramakrishna", "cuisine": "North Indian", "description": "Local cuisine"}
            ],
            "hotels": [
                {"name": "Hotel Ramakrishna", "type": "budget", "area": "Ayodhya"},
                {"name": "Hotel Sita", "type": "mid-range", "area": "Ayodhya"},
                {"name": "Clarks Inn", "type": "business", "area": "Ayodhya"}
            ]
        },
        "Dehradun": {
            "attractions": [
                {"name": "Robber's Cave (Guchhupani)", "type": "cave", "description": "Natural limestone cave with underground waterfalls"},
                {"name": "Sahastradhara", "type": "waterfall", "description": "Sulfur springs and waterfall with therapeutic waters"},
                {"name": "Forest Research Institute", "type": "museum", "description": "Largest museum of its kind with colonial architecture"},
                {"name": "Clock Tower", "type": "monument", "description": "Historic clock tower in the city center"},
                {"name": "Tapkeshwar Temple", "type": "temple", "description": "Ancient cave temple dedicated to Lord Shiva"},
                {"name": "Malsi Deer Park", "type": "park", "description": "Wildlife park with deer and other animals"},
                {"name": "Rajaji National Park", "type": "national_park", "description": "Tiger reserve and wildlife sanctuary"},
                {"name": "Mindrolling Monastery", "type": "monastery", "description": "Largest Buddhist monastery in India"}
            ],
            "restaurants": [
                {"name": "Ellora's", "cuisine": "Multi-cuisine", "description": "Popular restaurant with local and international dishes"},
                {"name": "The Good Earth", "cuisine": "Cafe", "description": "Organic cafe with healthy food options"},
                {"name": "Chakrata Road Food Street", "cuisine": "Street Food", "description": "Local street food and Garhwali cuisine"}
            ],
            "hotels": [
                {"name": "Hotel Madhuban", "type": "heritage", "area": "Hathibarkala"},
                {"name": "The Orchard", "type": "boutique", "area": "Rajpur Road"},
                {"name": "Ramana Residency", "type": "business", "area": "Rajpur Road"}
            ]
        }
    }

    @staticmethod
    def get_location_data(destination):
        """Get location data for a specific destination"""
        # First check if we have specific data for this destination
        data = LocationService.LOCATION_DATABASE.get(destination, {})

        # If no specific data exists, generate generic but detailed data
        if not data:
            data = LocationService._generate_generic_location_data(destination)

        return data

    @staticmethod
    def _generate_generic_location_data(destination):
        """Generate generic location data for any destination"""
        # Common attraction types that work for most destinations
        generic_attractions = [
            {"name": f"City Center of {destination}", "type": "urban", "description": "Explore the heart of the city with local markets and architecture"},
            {"name": f"Local Museum in {destination}", "type": "cultural", "description": "Discover the history and culture through exhibits and artifacts"},
            {"name": f"Scenic Park in {destination}", "type": "nature", "description": "Relax in green spaces with walking paths and picnic areas"},
            {"name": f"Historic District of {destination}", "type": "historical", "description": "Walk through preserved areas showcasing the city's heritage"},
            {"name": f"Local Market in {destination}", "type": "market", "description": "Experience authentic shopping and local crafts"},
            {"name": f"Nature Spot near {destination}", "type": "nature", "description": "Enjoy outdoor activities and scenic views"},
            {"name": f"Cultural Site in {destination}", "type": "cultural", "description": "Visit important landmarks and learn about local traditions"},
            {"name": f"Waterfront Area of {destination}", "type": "waterfront", "description": "Enjoy views and activities by the water"}
        ]

        # Common restaurant types
        generic_restaurants = [
            {"name": f"Traditional Restaurant in {destination}", "cuisine": "Local", "description": "Authentic local cuisine and specialties"},
            {"name": f"Modern Cafe in {destination}", "cuisine": "International", "description": "Contemporary dining with global influences"},
            {"name": f"Street Food Vendor in {destination}", "cuisine": "Street Food", "description": "Try popular local street food and snacks"},
            {"name": f"Fine Dining in {destination}", "cuisine": "Fusion", "description": "Elegant dining experience with creative dishes"}
        ]

        # Generic hotels
        generic_hotels = [
            {"name": f"Central Hotel in {destination}", "type": "mid-range", "area": "City Center"},
            {"name": f"Boutique Stay in {destination}", "type": "boutique", "area": "Historic District"},
            {"name": f"Luxury Resort in {destination}", "type": "luxury", "area": "Scenic Area"}
        ]

        return {
            "attractions": generic_attractions,
            "restaurants": generic_restaurants,
            "hotels": generic_hotels
        }

    @staticmethod
    def get_attractions(destination, limit=None):
        """Get attractions for a destination"""
        data = LocationService.get_location_data(destination)
        attractions = data.get('attractions', [])
        if limit:
            attractions = attractions[:limit]
        return attractions

    @staticmethod
    def get_restaurants(destination, limit=None):
        """Get restaurants for a destination"""
        data = LocationService.get_location_data(destination)
        restaurants = data.get('restaurants', [])
        if limit:
            restaurants = restaurants[:limit]
        return restaurants

    @staticmethod
    def get_hotels(destination, limit=None):
        """Get hotels for a destination"""
        data = LocationService.get_location_data(destination)
        hotels = data.get('hotels', [])
        if limit:
            hotels = hotels[:limit]
        return hotels