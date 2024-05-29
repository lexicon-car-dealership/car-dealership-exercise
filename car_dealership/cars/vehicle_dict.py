from pathlib import Path
print('Running' if __name__ == '__main__' else 'Importing', Path(__file__).resolve())
vehicles = [
  {
    "year": 2020,
    "manufacturer_name": "Audi",
    "model_name": "Q3",
    "car_type": "SUV"
  },
  {
    "year": 2020,
    "manufacturer_name": "Chevrolet",
    "model_name": "Malibu",
    "car_type": "Sedan"
  },
  {
    "year": 2020,
    "manufacturer_name": "Cadillac",
    "model_name": "Escalade ESV",
    "car_type": "SUV"
  },
  {
    "year": 2020,
    "manufacturer_name": "Chevrolet",
    "model_name": "Corvette",
    "car_type": "Coupe, Convertible"
  },
  {
    "year": 2020,
    "manufacturer_name": "Acura",
    "model_name": "RLX",
    "car_type": "Sedan"
  },
  {
    "year": 2020,
    "manufacturer_name": "Chevrolet",
    "model_name": "Silverado 2500 HD Crew Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2020,
    "manufacturer_name": "BMW",
    "model_name": "3 Series",
    "car_type": "Sedan"
  },
  {
    "year": 2020,
    "manufacturer_name": "Chrysler",
    "model_name": "Pacifica",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2020,
    "manufacturer_name": "Chevrolet",
    "model_name": "Colorado Crew Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2020,
    "manufacturer_name": "BMW",
    "model_name": "X3",
    "car_type": "SUV"
  },
  {
    "year": 2020,
    "manufacturer_name": "Acura",
    "model_name": "TLX",
    "car_type": "Sedan"
  },
  {
    "year": 2020,
    "manufacturer_name": "Chevrolet",
    "model_name": "Silverado 3500 HD Crew Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2020,
    "manufacturer_name": "BMW",
    "model_name": "7 Series",
    "car_type": "Sedan"
  },
  {
    "year": 2020,
    "manufacturer_name": "Ford",
    "model_name": "Fusion",
    "car_type": "Sedan"
  },
  {
    "year": 2020,
    "manufacturer_name": "Buick",
    "model_name": "Envision",
    "car_type": "SUV"
  },
  {
    "year": 2020,
    "manufacturer_name": "Audi",
    "model_name": "SQ5",
    "car_type": "SUV"
  },
  {
    "year": 2020,
    "manufacturer_name": "Audi",
    "model_name": "R8",
    "car_type": "Coupe, Convertible"
  },
  {
    "year": 2020,
    "manufacturer_name": "Chevrolet",
    "model_name": "Traverse",
    "car_type": "SUV"
  },
  {
    "year": 2020,
    "manufacturer_name": "Acura",
    "model_name": "MDX",
    "car_type": "SUV"
  },
  {
    "year": 2020,
    "manufacturer_name": "INFINITI",
    "model_name": "QX80",
    "car_type": "SUV"
  },
  {
    "year": 2020,
    "manufacturer_name": "Buick",
    "model_name": "Encore",
    "car_type": "SUV"
  },
  {
    "year": 2020,
    "manufacturer_name": "GMC",
    "model_name": "Sierra 2500 HD Crew Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2020,
    "manufacturer_name": "Honda",
    "model_name": "Insight",
    "car_type": "Sedan"
  },
  {
    "year": 2020,
    "manufacturer_name": "Cadillac",
    "model_name": "XT6",
    "car_type": "SUV"
  },
  {
    "year": 2020,
    "manufacturer_name": "Cadillac",
    "model_name": "XT5",
    "car_type": "SUV"
  },
  {
    "year": 2020,
    "manufacturer_name": "Cadillac",
    "model_name": "XT4",
    "car_type": "SUV"
  },
  {
    "year": 2020,
    "manufacturer_name": "Buick",
    "model_name": "Enclave",
    "car_type": "SUV"
  },
  {
    "year": 2020,
    "manufacturer_name": "Audi",
    "model_name": "Q5",
    "car_type": "SUV"
  },
  {
    "year": 2020,
    "manufacturer_name": "Hyundai",
    "model_name": "Santa Fe",
    "car_type": "SUV"
  },
  {
    "year": 2020,
    "manufacturer_name": "Ford",
    "model_name": "EcoSport",
    "car_type": "SUV"
  },
  {
    "year": 2020,
    "manufacturer_name": "Ford",
    "model_name": "Escape",
    "car_type": "SUV"
  },
  {
    "year": 2020,
    "manufacturer_name": "Ford",
    "model_name": "Mustang",
    "car_type": "Coupe, Convertible"
  },
  {
    "year": 2020,
    "manufacturer_name": "Hyundai",
    "model_name": "Sonata",
    "car_type": "Sedan"
  },
  {
    "year": 2020,
    "manufacturer_name": "Ford",
    "model_name": "Edge",
    "car_type": "SUV"
  },
  {
    "year": 2020,
    "manufacturer_name": "Chevrolet",
    "model_name": "Camaro",
    "car_type": "Convertible"
  },
  {
    "year": 2020,
    "manufacturer_name": "Hyundai",
    "model_name": "Kona Electric",
    "car_type": "SUV"
  },
  {
    "year": 2020,
    "manufacturer_name": "Chevrolet",
    "model_name": "Equinox",
    "car_type": "SUV"
  },
  {
    "year": 2020,
    "manufacturer_name": "GMC",
    "model_name": "Sierra 3500 HD Crew Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2020,
    "manufacturer_name": "Jeep",
    "model_name": "Gladiator",
    "car_type": "Pickup"
  },
  {
    "year": 2020,
    "manufacturer_name": "BMW",
    "model_name": "X7",
    "car_type": "SUV"
  },
  {
    "year": 2020,
    "manufacturer_name": "Cadillac",
    "model_name": "CT6-V",
    "car_type": "Sedan"
  },
  {
    "year": 2020,
    "manufacturer_name": "Audi",
    "model_name": "A7",
    "car_type": "Sedan"
  },
  {
    "year": 2020,
    "manufacturer_name": "Chevrolet",
    "model_name": "Blazer",
    "car_type": "SUV"
  },
  {
    "year": 2020,
    "manufacturer_name": "Ford",
    "model_name": "F150 SuperCrew Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2020,
    "manufacturer_name": "Chevrolet",
    "model_name": "Suburban",
    "car_type": "SUV"
  },
  {
    "year": 2020,
    "manufacturer_name": "Honda",
    "model_name": "Civic",
    "car_type": "Hatchback, Sedan, Coupe"
  },
  {
    "year": 2020,
    "manufacturer_name": "Jeep",
    "model_name": "Compass",
    "car_type": "SUV"
  },
  {
    "year": 2020,
    "manufacturer_name": "Cadillac",
    "model_name": "Escalade",
    "car_type": "SUV"
  },
  {
    "year": 2020,
    "manufacturer_name": "Chrysler",
    "model_name": "Voyager",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2020,
    "manufacturer_name": "Honda",
    "model_name": "Accord Hybrid",
    "car_type": "Sedan"
  },
  {
    "year": 2020,
    "manufacturer_name": "GMC",
    "model_name": "Terrain",
    "car_type": "SUV"
  },
  {
    "year": 2020,
    "manufacturer_name": "Chevrolet",
    "model_name": "Spark",
    "car_type": "Hatchback"
  },
  {
    "year": 2020,
    "manufacturer_name": "GMC",
    "model_name": "Sierra 1500 Crew Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2020,
    "manufacturer_name": "Hyundai",
    "model_name": "NEXO",
    "car_type": "SUV"
  },
  {
    "year": 2020,
    "manufacturer_name": "Hyundai",
    "model_name": "Veloster",
    "car_type": "Coupe"
  },
  {
    "year": 2020,
    "manufacturer_name": "Chevrolet",
    "model_name": "Silverado 1500 Crew Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2020,
    "manufacturer_name": "Genesis",
    "model_name": "G70",
    "car_type": "Sedan"
  },
  {
    "year": 2020,
    "manufacturer_name": "Cadillac",
    "model_name": "CT5",
    "car_type": "Sedan"
  },
  {
    "year": 2020,
    "manufacturer_name": "Honda",
    "model_name": "Odyssey",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2020,
    "manufacturer_name": "Hyundai",
    "model_name": "Elantra GT",
    "car_type": "Hatchback"
  },
  {
    "year": 2020,
    "manufacturer_name": "Acura",
    "model_name": "RDX",
    "car_type": "SUV"
  },
  {
    "year": 2020,
    "manufacturer_name": "GMC",
    "model_name": "Yukon XL",
    "car_type": "SUV"
  },
  {
    "year": 2020,
    "manufacturer_name": "Ford",
    "model_name": "Ranger SuperCab",
    "car_type": "Pickup"
  },
  {
    "year": 2020,
    "manufacturer_name": "Ford",
    "model_name": "Expedition MAX",
    "car_type": "SUV"
  },
  {
    "year": 2020,
    "manufacturer_name": "Hyundai",
    "model_name": "Kona",
    "car_type": "SUV"
  },
  {
    "year": 2020,
    "manufacturer_name": "INFINITI",
    "model_name": "QX50",
    "car_type": "SUV"
  },
  {
    "year": 2020,
    "manufacturer_name": "Dodge",
    "model_name": "Durango",
    "car_type": "SUV"
  },
  {
    "year": 2020,
    "manufacturer_name": "GMC",
    "model_name": "Yukon",
    "car_type": "SUV"
  },
  {
    "year": 2020,
    "manufacturer_name": "Hyundai",
    "model_name": "Palisade",
    "car_type": "SUV"
  },
  {
    "year": 2020,
    "manufacturer_name": "Honda",
    "model_name": "Ridgeline",
    "car_type": "Pickup"
  },
  {
    "year": 2020,
    "manufacturer_name": "Jeep",
    "model_name": "Cherokee",
    "car_type": "SUV"
  },
  {
    "year": 2020,
    "manufacturer_name": "Chevrolet",
    "model_name": "Bolt EV",
    "car_type": "Hatchback"
  },
  {
    "year": 2020,
    "manufacturer_name": "Ford",
    "model_name": "Expedition",
    "car_type": "SUV"
  },
  {
    "year": 2020,
    "manufacturer_name": "Hyundai",
    "model_name": "Elantra",
    "car_type": "Sedan"
  },
  {
    "year": 2020,
    "manufacturer_name": "Honda",
    "model_name": "Passport",
    "car_type": "SUV"
  },
  {
    "year": 2020,
    "manufacturer_name": "Dodge",
    "model_name": "Charger",
    "car_type": "Sedan"
  },
  {
    "year": 2020,
    "manufacturer_name": "Honda",
    "model_name": "Accord",
    "car_type": "Sedan"
  },
  {
    "year": 2020,
    "manufacturer_name": "INFINITI",
    "model_name": "QX60",
    "car_type": "SUV"
  },
  {
    "year": 2020,
    "manufacturer_name": "Hyundai",
    "model_name": "Venue",
    "car_type": "SUV"
  },
  {
    "year": 2020,
    "manufacturer_name": "Honda",
    "model_name": "Pilot",
    "car_type": "SUV"
  },
  {
    "year": 2020,
    "manufacturer_name": "Jeep",
    "model_name": "Grand Cherokee",
    "car_type": "SUV"
  },
  {
    "year": 2020,
    "manufacturer_name": "Chevrolet",
    "model_name": "Tahoe",
    "car_type": "SUV"
  },
  {
    "year": 2020,
    "manufacturer_name": "GMC",
    "model_name": "Acadia",
    "car_type": "SUV"
  },
  {
    "year": 2020,
    "manufacturer_name": "Chevrolet",
    "model_name": "Impala",
    "car_type": "Sedan"
  },
  {
    "year": 2020,
    "manufacturer_name": "Honda",
    "model_name": "CR-V",
    "car_type": "SUV"
  },
  {
    "year": 2020,
    "manufacturer_name": "BMW",
    "model_name": "X5",
    "car_type": "SUV"
  },
  {
    "year": 2020,
    "manufacturer_name": "INFINITI",
    "model_name": "Q60",
    "car_type": "Coupe"
  },
  {
    "year": 2020,
    "manufacturer_name": "Ford",
    "model_name": "Ranger SuperCrew",
    "car_type": "Pickup"
  },
  {
    "year": 2020,
    "manufacturer_name": "Chevrolet",
    "model_name": "Trax",
    "car_type": "SUV"
  },
  {
    "year": 2020,
    "manufacturer_name": "Hyundai",
    "model_name": "Ioniq Plug-in Hybrid",
    "car_type": "Hatchback"
  },
  {
    "year": 2020,
    "manufacturer_name": "Jaguar",
    "model_name": "E-PACE",
    "car_type": "SUV"
  },
  {
    "year": 2020,
    "manufacturer_name": "Hyundai",
    "model_name": "Tucson",
    "car_type": "SUV"
  },
  {
    "year": 2020,
    "manufacturer_name": "Ford",
    "model_name": "Explorer",
    "car_type": "SUV"
  },
  {
    "year": 2020,
    "manufacturer_name": "Honda",
    "model_name": "HR-V",
    "car_type": "SUV"
  },
  {
    "year": 2020,
    "manufacturer_name": "Jaguar",
    "model_name": "I-PACE",
    "car_type": "SUV"
  },
  {
    "year": 2020,
    "manufacturer_name": "INFINITI",
    "model_name": "Q50",
    "car_type": "Sedan"
  },
  {
    "year": 2020,
    "manufacturer_name": "Genesis",
    "model_name": "G80",
    "car_type": "Sedan"
  },
  {
    "year": 2020,
    "manufacturer_name": "Jaguar",
    "model_name": "F-PACE",
    "car_type": "SUV"
  },
  {
    "year": 2020,
    "manufacturer_name": "Jeep",
    "model_name": "Renegade",
    "car_type": "SUV"
  },
  {
    "year": 2020,
    "manufacturer_name": "Hyundai",
    "model_name": "Accent",
    "car_type": "Sedan"
  },
  {
    "year": 2020,
    "manufacturer_name": "Jaguar",
    "model_name": "F-TYPE",
    "car_type": "Convertible"
  },
  {
    "year": 2020,
    "manufacturer_name": "Jeep",
    "model_name": "Wrangler",
    "car_type": "SUV"
  },
  {
    "year": 2020,
    "manufacturer_name": "Kia",
    "model_name": "Sorento",
    "car_type": "SUV"
  },
  {
    "year": 2020,
    "manufacturer_name": "Kia",
    "model_name": "Rio",
    "car_type": "Sedan, Hatchback"
  },
  {
    "year": 2020,
    "manufacturer_name": "Land Rover",
    "model_name": "Discovery Sport",
    "car_type": "SUV"
  },
  {
    "year": 2020,
    "manufacturer_name": "Kia",
    "model_name": "Sedona",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2020,
    "manufacturer_name": "Kia",
    "model_name": "Optima",
    "car_type": "Sedan"
  },
  {
    "year": 2020,
    "manufacturer_name": "Kia",
    "model_name": "Sportage",
    "car_type": "SUV"
  },
  {
    "year": 2020,
    "manufacturer_name": "Kia",
    "model_name": "Optima Hybrid",
    "car_type": "Sedan"
  },
  {
    "year": 2020,
    "manufacturer_name": "Kia",
    "model_name": "Optima Plug-in Hybrid",
    "car_type": "Sedan"
  },
  {
    "year": 2020,
    "manufacturer_name": "Land Rover",
    "model_name": "Range Rover Evoque",
    "car_type": "SUV"
  },
  {
    "year": 2020,
    "manufacturer_name": "Kia",
    "model_name": "Telluride",
    "car_type": "SUV"
  },
  {
    "year": 2020,
    "manufacturer_name": "Kia",
    "model_name": "Forte",
    "car_type": "Sedan"
  },
  {
    "year": 2020,
    "manufacturer_name": "Jeep",
    "model_name": "Wrangler Unlimited",
    "car_type": "SUV"
  },
  {
    "year": 2020,
    "manufacturer_name": "Kia",
    "model_name": "Soul",
    "car_type": "Wagon"
  },
  {
    "year": 2020,
    "manufacturer_name": "Land Rover",
    "model_name": "Range Rover Sport",
    "car_type": "SUV"
  },
  {
    "year": 2020,
    "manufacturer_name": "Land Rover",
    "model_name": "Range Rover",
    "car_type": "SUV"
  },
  {
    "year": 2020,
    "manufacturer_name": "Kia",
    "model_name": "Stinger",
    "car_type": "Sedan"
  },
  {
    "year": 2020,
    "manufacturer_name": "Land Rover",
    "model_name": "Discovery",
    "car_type": "SUV"
  },
  {
    "year": 2020,
    "manufacturer_name": "Land Rover",
    "model_name": "Range Rover Velar",
    "car_type": "SUV"
  },
  {
    "year": 2020,
    "manufacturer_name": "Lexus",
    "model_name": "ES",
    "car_type": "Sedan"
  },
  {
    "year": 2020,
    "manufacturer_name": "Lexus",
    "model_name": "LC",
    "car_type": "Coupe"
  },
  {
    "year": 2020,
    "manufacturer_name": "Lexus",
    "model_name": "LX",
    "car_type": "SUV"
  },
  {
    "year": 2020,
    "manufacturer_name": "Lexus",
    "model_name": "RC",
    "car_type": "Coupe"
  },
  {
    "year": 2020,
    "manufacturer_name": "Lexus",
    "model_name": "GX",
    "car_type": "SUV"
  },
  {
    "year": 2020,
    "manufacturer_name": "Lexus",
    "model_name": "IS",
    "car_type": "Sedan"
  },
  {
    "year": 2020,
    "manufacturer_name": "Lexus",
    "model_name": "GS",
    "car_type": "Sedan"
  },
  {
    "year": 2020,
    "manufacturer_name": "Lexus",
    "model_name": "LS",
    "car_type": "Sedan"
  },
  {
    "year": 2020,
    "manufacturer_name": "Lexus",
    "model_name": "UX",
    "car_type": "SUV"
  },
  {
    "year": 2020,
    "manufacturer_name": "Mercedes-Benz",
    "model_name": "GLS",
    "car_type": "SUV"
  },
  {
    "year": 2020,
    "manufacturer_name": "Mercedes-Benz",
    "model_name": "CLA",
    "car_type": "Sedan"
  },
  {
    "year": 2020,
    "manufacturer_name": "Mitsubishi",
    "model_name": "Outlander Sport",
    "car_type": "SUV"
  },
  {
    "year": 2020,
    "manufacturer_name": "Lincoln",
    "model_name": "MKZ",
    "car_type": "Sedan"
  },
  {
    "year": 2020,
    "manufacturer_name": "Lincoln",
    "model_name": "Aviator",
    "car_type": "SUV"
  },
  {
    "year": 2020,
    "manufacturer_name": "Lexus",
    "model_name": "NX",
    "car_type": "SUV"
  },
  {
    "year": 2020,
    "manufacturer_name": "MAZDA",
    "model_name": "CX-30",
    "car_type": "SUV"
  },
  {
    "year": 2020,
    "manufacturer_name": "Mitsubishi",
    "model_name": "Eclipse Cross",
    "car_type": "SUV"
  },
  {
    "year": 2020,
    "manufacturer_name": "MAZDA",
    "model_name": "MAZDA3",
    "car_type": "Sedan, Hatchback"
  },
  {
    "year": 2020,
    "manufacturer_name": "Mitsubishi",
    "model_name": "Mirage G4",
    "car_type": "Sedan"
  },
  {
    "year": 2020,
    "manufacturer_name": "Lincoln",
    "model_name": "Navigator",
    "car_type": "SUV"
  },
  {
    "year": 2020,
    "manufacturer_name": "Nissan",
    "model_name": "Armada",
    "car_type": "SUV"
  },
  {
    "year": 2020,
    "manufacturer_name": "MAZDA",
    "model_name": "CX-5",
    "car_type": "SUV"
  },
  {
    "year": 2020,
    "manufacturer_name": "Lincoln",
    "model_name": "Corsair",
    "car_type": "SUV"
  },
  {
    "year": 2020,
    "manufacturer_name": "Lincoln",
    "model_name": "Navigator L",
    "car_type": "SUV"
  },
  {
    "year": 2020,
    "manufacturer_name": "Mercedes-Benz",
    "model_name": "G-Class",
    "car_type": "SUV"
  },
  {
    "year": 2020,
    "manufacturer_name": "Lincoln",
    "model_name": "Nautilus",
    "car_type": "SUV"
  },
  {
    "year": 2020,
    "manufacturer_name": "Lexus",
    "model_name": "RX",
    "car_type": "SUV"
  },
  {
    "year": 2020,
    "manufacturer_name": "Nissan",
    "model_name": "Kicks",
    "car_type": "SUV"
  },
  {
    "year": 2020,
    "manufacturer_name": "Nissan",
    "model_name": "Murano",
    "car_type": "SUV"
  },
  {
    "year": 2020,
    "manufacturer_name": "MAZDA",
    "model_name": "MAZDA6",
    "car_type": "Sedan"
  },
  {
    "year": 2020,
    "manufacturer_name": "Mercedes-Benz",
    "model_name": "C-Class",
    "car_type": "Convertible, Sedan, Coupe"
  },
  {
    "year": 2020,
    "manufacturer_name": "Nissan",
    "model_name": "NV3500 HD Passenger",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2020,
    "manufacturer_name": "Mercedes-Benz",
    "model_name": "GLA",
    "car_type": "SUV"
  },
  {
    "year": 2020,
    "manufacturer_name": "MAZDA",
    "model_name": "CX-9",
    "car_type": "SUV"
  },
  {
    "year": 2020,
    "manufacturer_name": "Nissan",
    "model_name": "NV1500 Cargo",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2020,
    "manufacturer_name": "Mercedes-Benz",
    "model_name": "E-Class",
    "car_type": "Coupe, Wagon, Sedan, Convertible"
  },
  {
    "year": 2020,
    "manufacturer_name": "MINI",
    "model_name": "Countryman",
    "car_type": "SUV"
  },
  {
    "year": 2020,
    "manufacturer_name": "Mercedes-Benz",
    "model_name": "GLE",
    "car_type": "SUV"
  },
  {
    "year": 2020,
    "manufacturer_name": "Nissan",
    "model_name": "Maxima",
    "car_type": "Sedan"
  },
  {
    "year": 2020,
    "manufacturer_name": "Nissan",
    "model_name": "370Z",
    "car_type": "Coupe"
  },
  {
    "year": 2020,
    "manufacturer_name": "Mercedes-Benz",
    "model_name": "GLC",
    "car_type": "SUV"
  },
  {
    "year": 2020,
    "manufacturer_name": "Mitsubishi",
    "model_name": "Mirage",
    "car_type": "Hatchback"
  },
  {
    "year": 2020,
    "manufacturer_name": "Nissan",
    "model_name": "Altima",
    "car_type": "Sedan"
  },
  {
    "year": 2020,
    "manufacturer_name": "Nissan",
    "model_name": "GT-R",
    "car_type": "Coupe"
  },
  {
    "year": 2020,
    "manufacturer_name": "Mitsubishi",
    "model_name": "Outlander",
    "car_type": "SUV"
  },
  {
    "year": 2020,
    "manufacturer_name": "Mitsubishi",
    "model_name": "Outlander PHEV",
    "car_type": "SUV"
  },
  {
    "year": 2020,
    "manufacturer_name": "Nissan",
    "model_name": "NV3500 HD Cargo",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2020,
    "manufacturer_name": "Porsche",
    "model_name": "Panamera",
    "car_type": "Sedan"
  },
  {
    "year": 2020,
    "manufacturer_name": "Porsche",
    "model_name": "Taycan",
    "car_type": "Sedan"
  },
  {
    "year": 2020,
    "manufacturer_name": "Nissan",
    "model_name": "Pathfinder",
    "car_type": "SUV"
  },
  {
    "year": 2020,
    "manufacturer_name": "Nissan",
    "model_name": "Rogue",
    "car_type": "SUV"
  },
  {
    "year": 2020,
    "manufacturer_name": "Nissan",
    "model_name": "NV200",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2020,
    "manufacturer_name": "Porsche",
    "model_name": "911",
    "car_type": "Convertible"
  },
  {
    "year": 2020,
    "manufacturer_name": "Nissan",
    "model_name": "Rogue Sport",
    "car_type": "SUV"
  },
  {
    "year": 2020,
    "manufacturer_name": "Porsche",
    "model_name": "Macan",
    "car_type": "SUV"
  },
  {
    "year": 2020,
    "manufacturer_name": "Porsche",
    "model_name": "Cayenne Coupe",
    "car_type": "SUV"
  },
  {
    "year": 2020,
    "manufacturer_name": "Porsche",
    "model_name": "Cayenne",
    "car_type": "SUV"
  },
  {
    "year": 2020,
    "manufacturer_name": "Nissan",
    "model_name": "NV2500 HD Cargo",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2020,
    "manufacturer_name": "Ram",
    "model_name": "3500 Crew Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2020,
    "manufacturer_name": "Ram",
    "model_name": "1500 Crew Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2020,
    "manufacturer_name": "Subaru",
    "model_name": "BRZ",
    "car_type": "Coupe"
  },
  {
    "year": 2020,
    "manufacturer_name": "Nissan",
    "model_name": "Versa",
    "car_type": "Sedan"
  },
  {
    "year": 2020,
    "manufacturer_name": "Toyota",
    "model_name": "Avalon",
    "car_type": "Sedan"
  },
  {
    "year": 2020,
    "manufacturer_name": "Subaru",
    "model_name": "WRX",
    "car_type": "Sedan"
  },
  {
    "year": 2020,
    "manufacturer_name": "Toyota",
    "model_name": "Camry",
    "car_type": "Sedan"
  },
  {
    "year": 2020,
    "manufacturer_name": "Subaru",
    "model_name": "Impreza",
    "car_type": "Wagon, Sedan"
  },
  {
    "year": 2020,
    "manufacturer_name": "Subaru",
    "model_name": "Ascent",
    "car_type": "SUV"
  },
  {
    "year": 2020,
    "manufacturer_name": "Subaru",
    "model_name": "Legacy",
    "car_type": "Sedan"
  },
  {
    "year": 2020,
    "manufacturer_name": "Toyota",
    "model_name": "Corolla Hatchback",
    "car_type": "Hatchback"
  },
  {
    "year": 2020,
    "manufacturer_name": "Subaru",
    "model_name": "Crosstrek",
    "car_type": "SUV"
  },
  {
    "year": 2020,
    "manufacturer_name": "Toyota",
    "model_name": "Corolla",
    "car_type": "Sedan"
  },
  {
    "year": 2020,
    "manufacturer_name": "Toyota",
    "model_name": "86",
    "car_type": "Coupe"
  },
  {
    "year": 2020,
    "manufacturer_name": "Subaru",
    "model_name": "Forester",
    "car_type": "SUV"
  },
  {
    "year": 2020,
    "manufacturer_name": "Toyota",
    "model_name": "Avalon Hybrid",
    "car_type": "Sedan"
  },
  {
    "year": 2020,
    "manufacturer_name": "Ram",
    "model_name": "2500 Crew Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2020,
    "manufacturer_name": "Toyota",
    "model_name": "4Runner",
    "car_type": "SUV"
  },
  {
    "year": 2020,
    "manufacturer_name": "Subaru",
    "model_name": "Outback",
    "car_type": "SUV"
  },
  {
    "year": 2020,
    "manufacturer_name": "Toyota",
    "model_name": "C-HR",
    "car_type": "SUV"
  },
  {
    "year": 2020,
    "manufacturer_name": "Toyota",
    "model_name": "Camry Hybrid",
    "car_type": "Sedan"
  },
  {
    "year": 2020,
    "manufacturer_name": "Toyota",
    "model_name": "Corolla Hybrid",
    "car_type": "Sedan"
  },
  {
    "year": 2020,
    "manufacturer_name": "Toyota",
    "model_name": "GR Supra",
    "car_type": "Coupe"
  },
  {
    "year": 2020,
    "manufacturer_name": "Toyota",
    "model_name": "Highlander",
    "car_type": "SUV"
  },
  {
    "year": 2020,
    "manufacturer_name": "Toyota",
    "model_name": "Prius",
    "car_type": "Hatchback"
  },
  {
    "year": 2020,
    "manufacturer_name": "Toyota",
    "model_name": "Prius Prime",
    "car_type": "Hatchback"
  },
  {
    "year": 2020,
    "manufacturer_name": "Toyota",
    "model_name": "RAV4",
    "car_type": "SUV"
  },
  {
    "year": 2020,
    "manufacturer_name": "Toyota",
    "model_name": "Tacoma Access Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2020,
    "manufacturer_name": "Toyota",
    "model_name": "Sienna",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2020,
    "manufacturer_name": "Toyota",
    "model_name": "Land Cruiser",
    "car_type": "SUV"
  },
  {
    "year": 2020,
    "manufacturer_name": "Toyota",
    "model_name": "Yaris",
    "car_type": "Sedan"
  },
  {
    "year": 2020,
    "manufacturer_name": "Toyota",
    "model_name": "RAV4 Hybrid",
    "car_type": "SUV"
  },
  {
    "year": 2020,
    "manufacturer_name": "Toyota",
    "model_name": "Highlander Hybrid",
    "car_type": "SUV"
  },
  {
    "year": 2020,
    "manufacturer_name": "Toyota",
    "model_name": "Sequoia",
    "car_type": "SUV"
  },
  {
    "year": 2020,
    "manufacturer_name": "Toyota",
    "model_name": "Tundra Double Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2020,
    "manufacturer_name": "Toyota",
    "model_name": "Tacoma Double Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2020,
    "manufacturer_name": "Toyota",
    "model_name": "Tundra CrewMax",
    "car_type": "Pickup"
  },
  {
    "year": 2020,
    "manufacturer_name": "Volkswagen",
    "model_name": "Passat",
    "car_type": "Sedan"
  },
  {
    "year": 2020,
    "manufacturer_name": "Toyota",
    "model_name": "Yaris Hatchback",
    "car_type": "Hatchback"
  },
  {
    "year": 2019,
    "manufacturer_name": "Acura",
    "model_name": "MDX Sport Hybrid",
    "car_type": "SUV"
  },
  {
    "year": 2019,
    "manufacturer_name": "Acura",
    "model_name": "RLX Sport Hybrid",
    "car_type": "Sedan"
  },
  {
    "year": 2019,
    "manufacturer_name": "Audi",
    "model_name": "A6",
    "car_type": "Sedan"
  },
  {
    "year": 2020,
    "manufacturer_name": "Volvo",
    "model_name": "XC40",
    "car_type": "SUV"
  },
  {
    "year": 2019,
    "manufacturer_name": "Audi",
    "model_name": "Q5",
    "car_type": "SUV"
  },
  {
    "year": 2019,
    "manufacturer_name": "Audi",
    "model_name": "A4",
    "car_type": "Sedan"
  },
  {
    "year": 2019,
    "manufacturer_name": "Audi",
    "model_name": "Q7",
    "car_type": "SUV"
  },
  {
    "year": 2019,
    "manufacturer_name": "Audi",
    "model_name": "Q8",
    "car_type": "SUV"
  },
  {
    "year": 2019,
    "manufacturer_name": "Audi",
    "model_name": "RS 5",
    "car_type": "Sedan, Coupe"
  },
  {
    "year": 2019,
    "manufacturer_name": "Acura",
    "model_name": "MDX",
    "car_type": "SUV"
  },
  {
    "year": 2019,
    "manufacturer_name": "Acura",
    "model_name": "NSX",
    "car_type": "Coupe"
  },
  {
    "year": 2019,
    "manufacturer_name": "Audi",
    "model_name": "A7",
    "car_type": "Sedan"
  },
  {
    "year": 2019,
    "manufacturer_name": "Alfa Romeo",
    "model_name": "4C Spider",
    "car_type": "Convertible"
  },
  {
    "year": 2020,
    "manufacturer_name": "Volvo",
    "model_name": "XC60",
    "car_type": "SUV"
  },
  {
    "year": 2019,
    "manufacturer_name": "Acura",
    "model_name": "RDX",
    "car_type": "SUV"
  },
  {
    "year": 2020,
    "manufacturer_name": "Volkswagen",
    "model_name": "Tiguan",
    "car_type": "SUV"
  },
  {
    "year": 2020,
    "manufacturer_name": "Volvo",
    "model_name": "XC90",
    "car_type": "SUV1992"
  },
  {
    "year": 2019,
    "manufacturer_name": "Audi",
    "model_name": "A8",
    "car_type": "Sedan"
  },
  {
    "year": 2019,
    "manufacturer_name": "BMW",
    "model_name": "4 Series",
    "car_type": "Convertible, Sedan, Coupe"
  },
  {
    "year": 2019,
    "manufacturer_name": "Acura",
    "model_name": "TLX",
    "car_type": "Sedan"
  },
  {
    "year": 2019,
    "manufacturer_name": "Acura",
    "model_name": "ILX",
    "car_type": "Sedan"
  },
  {
    "year": 2019,
    "manufacturer_name": "BMW",
    "model_name": "2 Series",
    "car_type": "Coupe, Convertible"
  },
  {
    "year": 2019,
    "manufacturer_name": "Audi",
    "model_name": "A3",
    "car_type": "Convertible, Sedan"
  },
  {
    "year": 2019,
    "manufacturer_name": "Audi",
    "model_name": "S5",
    "car_type": "Sedan, Coupe, Convertible"
  },
  {
    "year": 2019,
    "manufacturer_name": "Audi",
    "model_name": "A4 allroad",
    "car_type": "Wagon"
  },
  {
    "year": 2019,
    "manufacturer_name": "Audi",
    "model_name": "e-tron",
    "car_type": "SUV"
  },
  {
    "year": 2020,
    "manufacturer_name": "Volkswagen",
    "model_name": "Jetta",
    "car_type": "Sedan"
  },
  {
    "year": 2019,
    "manufacturer_name": "Audi",
    "model_name": "Q3",
    "car_type": "SUV"
  },
  {
    "year": 2019,
    "manufacturer_name": "Audi",
    "model_name": "RS 3",
    "car_type": "Sedan"
  },
  {
    "year": 2019,
    "manufacturer_name": "Alfa Romeo",
    "model_name": "Stelvio",
    "car_type": "SUV"
  },
  {
    "year": 2019,
    "manufacturer_name": "Alfa Romeo",
    "model_name": "Giulia",
    "car_type": "Sedan"
  },
  {
    "year": 2019,
    "manufacturer_name": "Audi",
    "model_name": "A5",
    "car_type": "Coupe, Sedan, Convertible"
  },
  {
    "year": 2019,
    "manufacturer_name": "Acura",
    "model_name": "RLX",
    "car_type": "Sedan"
  },
  {
    "year": 2019,
    "manufacturer_name": "Audi",
    "model_name": "S3",
    "car_type": "Sedan"
  },
  {
    "year": 2019,
    "manufacturer_name": "Audi",
    "model_name": "S4",
    "car_type": "Sedan"
  },
  {
    "year": 2019,
    "manufacturer_name": "BMW",
    "model_name": "3 Series",
    "car_type": "Sedan, Wagon"
  },
  {
    "year": 2019,
    "manufacturer_name": "Audi",
    "model_name": "SQ5",
    "car_type": "SUV"
  },
  {
    "year": 2019,
    "manufacturer_name": "BMW",
    "model_name": "5 Series",
    "car_type": "Sedan"
  },
  {
    "year": 2019,
    "manufacturer_name": "BMW",
    "model_name": "M5",
    "car_type": "Sedan"
  },
  {
    "year": 2019,
    "manufacturer_name": "BMW",
    "model_name": "i8",
    "car_type": "Convertible, Coupe"
  },
  {
    "year": 2019,
    "manufacturer_name": "BMW",
    "model_name": "8 Series",
    "car_type": "Coupe, Convertible"
  },
  {
    "year": 2019,
    "manufacturer_name": "BMW",
    "model_name": "M6",
    "car_type": "Coupe"
  },
  {
    "year": 2019,
    "manufacturer_name": "BMW",
    "model_name": "i3",
    "car_type": "Hatchback"
  },
  {
    "year": 2019,
    "manufacturer_name": "BMW",
    "model_name": "7 Series",
    "car_type": "Sedan"
  },
  {
    "year": 2019,
    "manufacturer_name": "BMW",
    "model_name": "X3",
    "car_type": "SUV"
  },
  {
    "year": 2019,
    "manufacturer_name": "BMW",
    "model_name": "6 Series",
    "car_type": "Sedan"
  },
  {
    "year": 2019,
    "manufacturer_name": "BMW",
    "model_name": "M4",
    "car_type": "Coupe, Convertible"
  },
  {
    "year": 2019,
    "manufacturer_name": "Audi",
    "model_name": "TT",
    "car_type": "Coupe"
  },
  {
    "year": 2019,
    "manufacturer_name": "Cadillac",
    "model_name": "Escalade",
    "car_type": "SUV"
  },
  {
    "year": 2019,
    "manufacturer_name": "Buick",
    "model_name": "Regal Sportback",
    "car_type": "Sedan"
  },
  {
    "year": 2019,
    "manufacturer_name": "BMW",
    "model_name": "X6 M",
    "car_type": "SUV"
  },
  {
    "year": 2019,
    "manufacturer_name": "BMW",
    "model_name": "X2",
    "car_type": "SUV"
  },
  {
    "year": 2019,
    "manufacturer_name": "Cadillac",
    "model_name": "CTS-V",
    "car_type": "Sedan"
  },
  {
    "year": 2019,
    "manufacturer_name": "BMW",
    "model_name": "X1",
    "car_type": "SUV"
  },
  {
    "year": 2019,
    "manufacturer_name": "BMW",
    "model_name": "X6",
    "car_type": "SUV"
  },
  {
    "year": 2019,
    "manufacturer_name": "BMW",
    "model_name": "X4",
    "car_type": "SUV"
  },
  {
    "year": 2019,
    "manufacturer_name": "Chevrolet",
    "model_name": "Camaro",
    "car_type": "Coupe, Convertible"
  },
  {
    "year": 2019,
    "manufacturer_name": "Cadillac",
    "model_name": "Escalade ESV",
    "car_type": "SUV"
  },
  {
    "year": 2019,
    "manufacturer_name": "Chevrolet",
    "model_name": "Blazer",
    "car_type": "SUV"
  },
  {
    "year": 2019,
    "manufacturer_name": "Cadillac",
    "model_name": "CT6",
    "car_type": "Sedan"
  },
  {
    "year": 2019,
    "manufacturer_name": "BMW",
    "model_name": "X5",
    "car_type": "SUV"
  },
  {
    "year": 2019,
    "manufacturer_name": "Buick",
    "model_name": "Regal TourX",
    "car_type": "Wagon"
  },
  {
    "year": 2019,
    "manufacturer_name": "Chevrolet",
    "model_name": "Colorado Crew Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2019,
    "manufacturer_name": "Chevrolet",
    "model_name": "Bolt EV",
    "car_type": "Hatchback"
  },
  {
    "year": 2019,
    "manufacturer_name": "Cadillac",
    "model_name": "CT6-V",
    "car_type": "Sedan"
  },
  {
    "year": 2019,
    "manufacturer_name": "BMW",
    "model_name": "M2",
    "car_type": "Coupe"
  },
  {
    "year": 2019,
    "manufacturer_name": "BMW",
    "model_name": "X7",
    "car_type": "SUV"
  },
  {
    "year": 2019,
    "manufacturer_name": "Buick",
    "model_name": "Envision",
    "car_type": "SUV"
  },
  {
    "year": 2019,
    "manufacturer_name": "Buick",
    "model_name": "Cascada",
    "car_type": "Convertible"
  },
  {
    "year": 2019,
    "manufacturer_name": "Cadillac",
    "model_name": "XT5",
    "car_type": "SUV"
  },
  {
    "year": 2019,
    "manufacturer_name": "Cadillac",
    "model_name": "XT4",
    "car_type": "SUV"
  },
  {
    "year": 2019,
    "manufacturer_name": "Buick",
    "model_name": "Encore",
    "car_type": "SUV"
  },
  {
    "year": 2019,
    "manufacturer_name": "Buick",
    "model_name": "Enclave",
    "car_type": "SUV"
  },
  {
    "year": 2019,
    "manufacturer_name": "Cadillac",
    "model_name": "CTS",
    "car_type": "Sedan"
  },
  {
    "year": 2019,
    "manufacturer_name": "Chevrolet",
    "model_name": "Cruze",
    "car_type": "Sedan, Hatchback"
  },
  {
    "year": 2019,
    "manufacturer_name": "Chevrolet",
    "model_name": "Equinox",
    "car_type": "SUV"
  },
  {
    "year": 2019,
    "manufacturer_name": "Chevrolet",
    "model_name": "Corvette",
    "car_type": "Coupe, Convertible"
  },
  {
    "year": 2019,
    "manufacturer_name": "BMW",
    "model_name": "Z4",
    "car_type": "Convertible"
  },
  {
    "year": 2019,
    "manufacturer_name": "Cadillac",
    "model_name": "XTS",
    "car_type": "Sedan"
  },
  {
    "year": 2019,
    "manufacturer_name": "Buick",
    "model_name": "LaCrosse",
    "car_type": "Sedan"
  },
  {
    "year": 2019,
    "manufacturer_name": "Cadillac",
    "model_name": "ATS-V",
    "car_type": "Coupe"
  },
  {
    "year": 2019,
    "manufacturer_name": "Cadillac",
    "model_name": "ATS",
    "car_type": "Coupe"
  },
  {
    "year": 2019,
    "manufacturer_name": "Chevrolet",
    "model_name": "Express 2500 Cargo",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2019,
    "manufacturer_name": "Chevrolet",
    "model_name": "Colorado Extended Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2019,
    "manufacturer_name": "Chevrolet",
    "model_name": "Express 2500 Passenger",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2019,
    "manufacturer_name": "Chevrolet",
    "model_name": "Express 3500 Passenger",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2019,
    "manufacturer_name": "Chevrolet",
    "model_name": "Impala",
    "car_type": "Sedan"
  },
  {
    "year": 2019,
    "manufacturer_name": "Chevrolet",
    "model_name": "Silverado 2500 HD Crew Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2019,
    "manufacturer_name": "Chevrolet",
    "model_name": "Malibu",
    "car_type": "Sedan"
  },
  {
    "year": 2019,
    "manufacturer_name": "Chevrolet",
    "model_name": "Silverado 2500 HD Double Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2019,
    "manufacturer_name": "Chevrolet",
    "model_name": "Silverado 1500 Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2019,
    "manufacturer_name": "Chevrolet",
    "model_name": "Express 3500 Cargo",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2019,
    "manufacturer_name": "Chevrolet",
    "model_name": "Silverado 1500 LD Double Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2019,
    "manufacturer_name": "Chevrolet",
    "model_name": "Silverado 2500 HD Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2019,
    "manufacturer_name": "Chevrolet",
    "model_name": "Silverado 1500 Crew Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2019,
    "manufacturer_name": "Chevrolet",
    "model_name": "Silverado 1500 Double Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2019,
    "manufacturer_name": "Chevrolet",
    "model_name": "Sonic",
    "car_type": "Sedan, Hatchback"
  },
  {
    "year": 2019,
    "manufacturer_name": "Chevrolet",
    "model_name": "Spark",
    "car_type": "Hatchback"
  },
  {
    "year": 2019,
    "manufacturer_name": "Chevrolet",
    "model_name": "Silverado 3500 HD Crew Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2019,
    "manufacturer_name": "Chrysler",
    "model_name": "Pacifica Hybrid",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2019,
    "manufacturer_name": "Dodge",
    "model_name": "Durango",
    "car_type": "SUV"
  },
  {
    "year": 2019,
    "manufacturer_name": "Dodge",
    "model_name": "Charger",
    "car_type": "Sedan"
  },
  {
    "year": 2019,
    "manufacturer_name": "Chevrolet",
    "model_name": "Suburban",
    "car_type": "SUV"
  },
  {
    "year": 2019,
    "manufacturer_name": "Chevrolet",
    "model_name": "Trax",
    "car_type": "SUV"
  },
  {
    "year": 2019,
    "manufacturer_name": "Dodge",
    "model_name": "Challenger",
    "car_type": "Coupe"
  },
  {
    "year": 2019,
    "manufacturer_name": "Chevrolet",
    "model_name": "Tahoe",
    "car_type": "SUV"
  },
  {
    "year": 2019,
    "manufacturer_name": "Ford",
    "model_name": "EcoSport",
    "car_type": "SUV"
  },
  {
    "year": 2019,
    "manufacturer_name": "FIAT",
    "model_name": "500L",
    "car_type": "Hatchback"
  },
  {
    "year": 2019,
    "manufacturer_name": "Chevrolet",
    "model_name": "Volt",
    "car_type": "Sedan"
  },
  {
    "year": 2019,
    "manufacturer_name": "Chrysler",
    "model_name": "Pacifica",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2019,
    "manufacturer_name": "FIAT",
    "model_name": "500e",
    "car_type": "Hatchback"
  },
  {
    "year": 2019,
    "manufacturer_name": "FIAT",
    "model_name": "500",
    "car_type": "Hatchback"
  },
  {
    "year": 2019,
    "manufacturer_name": "Dodge",
    "model_name": "Journey",
    "car_type": "SUV"
  },
  {
    "year": 2019,
    "manufacturer_name": "Ford",
    "model_name": "F150 Super Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2019,
    "manufacturer_name": "Chevrolet",
    "model_name": "Suburban 3500HD",
    "car_type": "SUV"
  },
  {
    "year": 2019,
    "manufacturer_name": "Dodge",
    "model_name": "Grand Caravan Passenger",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2019,
    "manufacturer_name": "Chrysler",
    "model_name": "300",
    "car_type": "Sedan"
  },
  {
    "year": 2019,
    "manufacturer_name": "FIAT",
    "model_name": "500c",
    "car_type": "Convertible"
  },
  {
    "year": 2019,
    "manufacturer_name": "Ford",
    "model_name": "Expedition MAX",
    "car_type": "SUV"
  },
  {
    "year": 2019,
    "manufacturer_name": "Ford",
    "model_name": "Edge",
    "car_type": "SUV"
  },
  {
    "year": 2019,
    "manufacturer_name": "Chevrolet",
    "model_name": "Traverse",
    "car_type": "SUV"
  },
  {
    "year": 2019,
    "manufacturer_name": "Ford",
    "model_name": "Escape",
    "car_type": "SUV"
  },
  {
    "year": 2019,
    "manufacturer_name": "FIAT",
    "model_name": "500 Abarth",
    "car_type": "Hatchback"
  },
  {
    "year": 2019,
    "manufacturer_name": "Ford",
    "model_name": "Expedition",
    "car_type": "SUV"
  },
  {
    "year": 2019,
    "manufacturer_name": "FIAT",
    "model_name": "124 Spider",
    "car_type": "Convertible"
  },
  {
    "year": 2019,
    "manufacturer_name": "Ford",
    "model_name": "F150 SuperCrew Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2019,
    "manufacturer_name": "Ford",
    "model_name": "F250 Super Duty Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2019,
    "manufacturer_name": "FIAT",
    "model_name": "500X",
    "car_type": "SUV"
  },
  {
    "year": 2019,
    "manufacturer_name": "FIAT",
    "model_name": "500c Abarth",
    "car_type": "Convertible"
  },
  {
    "year": 2019,
    "manufacturer_name": "Ford",
    "model_name": "Explorer",
    "car_type": "SUV"
  },
  {
    "year": 2019,
    "manufacturer_name": "Ford",
    "model_name": "F150 Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2019,
    "manufacturer_name": "Ford",
    "model_name": "F450 Super Duty Crew Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2019,
    "manufacturer_name": "Ford",
    "model_name": "F350 Super Duty Crew Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2019,
    "manufacturer_name": "Ford",
    "model_name": "Fiesta",
    "car_type": "Hatchback, Sedan"
  },
  {
    "year": 2019,
    "manufacturer_name": "Ford",
    "model_name": "F250 Super Duty Crew Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2019,
    "manufacturer_name": "Ford",
    "model_name": "Ranger SuperCab",
    "car_type": "Pickup"
  },
  {
    "year": 2019,
    "manufacturer_name": "Ford",
    "model_name": "F350 Super Duty Super Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2019,
    "manufacturer_name": "Ford",
    "model_name": "Flex",
    "car_type": "SUV"
  },
  {
    "year": 2019,
    "manufacturer_name": "Ford",
    "model_name": "Fusion",
    "car_type": "Sedan"
  },
  {
    "year": 2019,
    "manufacturer_name": "Ford",
    "model_name": "Transit 150 Van",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2019,
    "manufacturer_name": "GMC",
    "model_name": "Canyon Crew Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2019,
    "manufacturer_name": "Genesis",
    "model_name": "G90",
    "car_type": "Sedan"
  },
  {
    "year": 2019,
    "manufacturer_name": "Ford",
    "model_name": "Fusion Energi",
    "car_type": "Sedan"
  },
  {
    "year": 2019,
    "manufacturer_name": "Ford",
    "model_name": "Transit Connect Cargo",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2019,
    "manufacturer_name": "Ford",
    "model_name": "Transit 150 Wagon",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2019,
    "manufacturer_name": "Ford",
    "model_name": "Transit 350 Van",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2019,
    "manufacturer_name": "Ford",
    "model_name": "Ranger SuperCrew",
    "car_type": "Pickup"
  },
  {
    "year": 2019,
    "manufacturer_name": "Ford",
    "model_name": "Mustang",
    "car_type": "Coupe, Convertible"
  },
  {
    "year": 2019,
    "manufacturer_name": "Ford",
    "model_name": "F250 Super Duty Super Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2019,
    "manufacturer_name": "GMC",
    "model_name": "Sierra 1500 Double Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2019,
    "manufacturer_name": "Ford",
    "model_name": "Transit 250 Van",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2019,
    "manufacturer_name": "Ford",
    "model_name": "Transit 350 Wagon",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2019,
    "manufacturer_name": "Ford",
    "model_name": "Transit Connect Passenger",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2019,
    "manufacturer_name": "Freightliner",
    "model_name": "Sprinter 2500 Cargo",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2019,
    "manufacturer_name": "Ford",
    "model_name": "Taurus",
    "car_type": "Sedan"
  },
  {
    "year": 2019,
    "manufacturer_name": "GMC",
    "model_name": "Sierra 1500 Crew Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2019,
    "manufacturer_name": "GMC",
    "model_name": "Sierra 1500 Limited Double Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2019,
    "manufacturer_name": "GMC",
    "model_name": "Yukon XL",
    "car_type": "SUV"
  },
  {
    "year": 2019,
    "manufacturer_name": "Honda",
    "model_name": "CR-V",
    "car_type": "SUV"
  },
  {
    "year": 2019,
    "manufacturer_name": "Genesis",
    "model_name": "G80",
    "car_type": "Sedan"
  },
  {
    "year": 2019,
    "manufacturer_name": "GMC",
    "model_name": "Acadia",
    "car_type": "SUV"
  },
  {
    "year": 2019,
    "manufacturer_name": "Honda",
    "model_name": "Clarity Electric",
    "car_type": "Sedan"
  },
  {
    "year": 2019,
    "manufacturer_name": "GMC",
    "model_name": "Sierra 2500 HD Double Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2019,
    "manufacturer_name": "GMC",
    "model_name": "Sierra 2500 HD Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2019,
    "manufacturer_name": "Genesis",
    "model_name": "G70",
    "car_type": "Sedan"
  },
  {
    "year": 2019,
    "manufacturer_name": "GMC",
    "model_name": "Sierra 3500 HD Crew Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2019,
    "manufacturer_name": "GMC",
    "model_name": "Canyon Extended Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2019,
    "manufacturer_name": "GMC",
    "model_name": "Sierra 1500 Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2019,
    "manufacturer_name": "Honda",
    "model_name": "Civic Type R",
    "car_type": "Hatchback"
  },
  {
    "year": 2019,
    "manufacturer_name": "GMC",
    "model_name": "Yukon",
    "car_type": "SUV"
  },
  {
    "year": 2019,
    "manufacturer_name": "GMC",
    "model_name": "Terrain",
    "car_type": "SUV"
  },
  {
    "year": 2019,
    "manufacturer_name": "Honda",
    "model_name": "Civic",
    "car_type": "Coupe, Sedan, Hatchback"
  },
  {
    "year": 2019,
    "manufacturer_name": "GMC",
    "model_name": "Sierra 2500 HD Crew Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2019,
    "manufacturer_name": "Honda",
    "model_name": "Accord",
    "car_type": "Sedan"
  },
  {
    "year": 2019,
    "manufacturer_name": "Honda",
    "model_name": "Accord Hybrid",
    "car_type": "Sedan"
  },
  {
    "year": 2019,
    "manufacturer_name": "Honda",
    "model_name": "Clarity Fuel Cell",
    "car_type": "Sedan"
  },
  {
    "year": 2019,
    "manufacturer_name": "Honda",
    "model_name": "HR-V",
    "car_type": "SUV"
  },
  {
    "year": 2019,
    "manufacturer_name": "Honda",
    "model_name": "Clarity Plug-in Hybrid",
    "car_type": "Sedan"
  },
  {
    "year": 2019,
    "manufacturer_name": "Honda",
    "model_name": "Insight",
    "car_type": "Sedan"
  },
  {
    "year": 2019,
    "manufacturer_name": "Honda",
    "model_name": "Passport",
    "car_type": "SUV"
  },
  {
    "year": 2019,
    "manufacturer_name": "Honda",
    "model_name": "Ridgeline",
    "car_type": "Pickup"
  },
  {
    "year": 2019,
    "manufacturer_name": "Honda",
    "model_name": "Pilot",
    "car_type": "SUV"
  },
  {
    "year": 2019,
    "manufacturer_name": "Honda",
    "model_name": "Fit",
    "car_type": "Hatchback"
  },
  {
    "year": 2019,
    "manufacturer_name": "Honda",
    "model_name": "Odyssey",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2019,
    "manufacturer_name": "Hyundai",
    "model_name": "Accent",
    "car_type": "Sedan"
  },
  {
    "year": 2019,
    "manufacturer_name": "Hyundai",
    "model_name": "Ioniq Electric",
    "car_type": "Hatchback"
  },
  {
    "year": 2019,
    "manufacturer_name": "Hyundai",
    "model_name": "Sonata Hybrid",
    "car_type": "Sedan"
  },
  {
    "year": 2019,
    "manufacturer_name": "Hyundai",
    "model_name": "Elantra",
    "car_type": "Sedan"
  },
  {
    "year": 2019,
    "manufacturer_name": "Hyundai",
    "model_name": "Ioniq Plug-in Hybrid",
    "car_type": "Hatchback"
  },
  {
    "year": 2019,
    "manufacturer_name": "INFINITI",
    "model_name": "Q60",
    "car_type": "Coupe"
  },
  {
    "year": 2019,
    "manufacturer_name": "Hyundai",
    "model_name": "Sonata",
    "car_type": "Sedan"
  },
  {
    "year": 2019,
    "manufacturer_name": "Hyundai",
    "model_name": "NEXO",
    "car_type": "SUV"
  },
  {
    "year": 2019,
    "manufacturer_name": "Hyundai",
    "model_name": "Kona",
    "car_type": "SUV"
  },
  {
    "year": 2019,
    "manufacturer_name": "Hyundai",
    "model_name": "Kona Electric",
    "car_type": "SUV"
  },
  {
    "year": 2019,
    "manufacturer_name": "Hyundai",
    "model_name": "Elantra GT",
    "car_type": "Hatchback"
  },
  {
    "year": 2019,
    "manufacturer_name": "INFINITI",
    "model_name": "Q50",
    "car_type": "Sedan"
  },
  {
    "year": 2019,
    "manufacturer_name": "Hyundai",
    "model_name": "Ioniq Hybrid",
    "car_type": "Hatchback"
  },
  {
    "year": 2019,
    "manufacturer_name": "Hyundai",
    "model_name": "Sonata Plug-in Hybrid",
    "car_type": "Sedan"
  },
  {
    "year": 2019,
    "manufacturer_name": "Hyundai",
    "model_name": "Santa Fe",
    "car_type": "SUV"
  },
  {
    "year": 2019,
    "manufacturer_name": "INFINITI",
    "model_name": "Q70",
    "car_type": "Sedan"
  },
  {
    "year": 2019,
    "manufacturer_name": "INFINITI",
    "model_name": "QX60",
    "car_type": "SUV"
  },
  {
    "year": 2019,
    "manufacturer_name": "Hyundai",
    "model_name": "Veloster",
    "car_type": "Coupe"
  },
  {
    "year": 2019,
    "manufacturer_name": "INFINITI",
    "model_name": "QX80",
    "car_type": "SUV"
  },
  {
    "year": 2019,
    "manufacturer_name": "INFINITI",
    "model_name": "QX50",
    "car_type": "SUV"
  },
  {
    "year": 2019,
    "manufacturer_name": "Hyundai",
    "model_name": "Tucson",
    "car_type": "SUV"
  },
  {
    "year": 2019,
    "manufacturer_name": "Jaguar",
    "model_name": "I-PACE",
    "car_type": "SUV"
  },
  {
    "year": 2019,
    "manufacturer_name": "INFINITI",
    "model_name": "QX30",
    "car_type": "SUV"
  },
  {
    "year": 2019,
    "manufacturer_name": "Jaguar",
    "model_name": "XE",
    "car_type": "Sedan"
  },
  {
    "year": 2019,
    "manufacturer_name": "Kia",
    "model_name": "Sedona",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2019,
    "manufacturer_name": "Kia",
    "model_name": "Niro",
    "car_type": "Wagon"
  },
  {
    "year": 2019,
    "manufacturer_name": "Jaguar",
    "model_name": "E-PACE",
    "car_type": "SUV"
  },
  {
    "year": 2019,
    "manufacturer_name": "Jeep",
    "model_name": "Compass",
    "car_type": "SUV"
  },
  {
    "year": 2019,
    "manufacturer_name": "Jeep",
    "model_name": "Grand Cherokee",
    "car_type": "SUV"
  },
  {
    "year": 2019,
    "manufacturer_name": "Jeep",
    "model_name": "Renegade",
    "car_type": "SUV"
  },
  {
    "year": 2019,
    "manufacturer_name": "Jaguar",
    "model_name": "F-PACE",
    "car_type": "SUV"
  },
  {
    "year": 2019,
    "manufacturer_name": "Jeep",
    "model_name": "Cherokee",
    "car_type": "SUV"
  },
  {
    "year": 2019,
    "manufacturer_name": "Jaguar",
    "model_name": "XF",
    "car_type": "Wagon, Sedan"
  },
  {
    "year": 2019,
    "manufacturer_name": "Jaguar",
    "model_name": "F-TYPE",
    "car_type": "Coupe, Convertible"
  },
  {
    "year": 2019,
    "manufacturer_name": "Jaguar",
    "model_name": "XJ",
    "car_type": "Sedan"
  },
  {
    "year": 2019,
    "manufacturer_name": "Kia",
    "model_name": "Forte",
    "car_type": "Sedan"
  },
  {
    "year": 2019,
    "manufacturer_name": "Jeep",
    "model_name": "Wrangler Unlimited",
    "car_type": "SUV"
  },
  {
    "year": 2019,
    "manufacturer_name": "Jeep",
    "model_name": "Wrangler",
    "car_type": "SUV"
  },
  {
    "year": 2019,
    "manufacturer_name": "Kia",
    "model_name": "Niro Plug-in Hybrid",
    "car_type": "Wagon"
  },
  {
    "year": 2019,
    "manufacturer_name": "Kia",
    "model_name": "Optima Hybrid",
    "car_type": "Sedan"
  },
  {
    "year": 2019,
    "manufacturer_name": "Kia",
    "model_name": "Cadenza",
    "car_type": "Sedan"
  },
  {
    "year": 2019,
    "manufacturer_name": "Kia",
    "model_name": "K900",
    "car_type": "Sedan"
  },
  {
    "year": 2019,
    "manufacturer_name": "Kia",
    "model_name": "Niro EV",
    "car_type": "Wagon"
  },
  {
    "year": 2019,
    "manufacturer_name": "Kia",
    "model_name": "Optima",
    "car_type": "Sedan"
  },
  {
    "year": 2019,
    "manufacturer_name": "Kia",
    "model_name": "Optima Plug-in Hybrid",
    "car_type": "Sedan"
  },
  {
    "year": 2019,
    "manufacturer_name": "Kia",
    "model_name": "Stinger",
    "car_type": "Sedan"
  },
  {
    "year": 2019,
    "manufacturer_name": "Kia",
    "model_name": "Rio",
    "car_type": "Sedan, Hatchback"
  },
  {
    "year": 2019,
    "manufacturer_name": "Land Rover",
    "model_name": "Discovery",
    "car_type": "SUV"
  },
  {
    "year": 2019,
    "manufacturer_name": "Kia",
    "model_name": "Sorento",
    "car_type": "SUV"
  },
  {
    "year": 2019,
    "manufacturer_name": "Kia",
    "model_name": "Sportage",
    "car_type": "SUV"
  },
  {
    "year": 2019,
    "manufacturer_name": "Land Rover",
    "model_name": "Range Rover Sport",
    "car_type": "SUV"
  },
  {
    "year": 2019,
    "manufacturer_name": "Lexus",
    "model_name": "GX",
    "car_type": "SUV"
  },
  {
    "year": 2019,
    "manufacturer_name": "Kia",
    "model_name": "Soul",
    "car_type": "Wagon"
  },
  {
    "year": 2019,
    "manufacturer_name": "Lexus",
    "model_name": "GS",
    "car_type": "Sedan"
  },
  {
    "year": 2019,
    "manufacturer_name": "Land Rover",
    "model_name": "Range Rover Velar",
    "car_type": "SUV"
  },
  {
    "year": 2019,
    "manufacturer_name": "Land Rover",
    "model_name": "Range Rover Evoque",
    "car_type": "SUV"
  },
  {
    "year": 2019,
    "manufacturer_name": "Lexus",
    "model_name": "LC",
    "car_type": "Coupe"
  },
  {
    "year": 2019,
    "manufacturer_name": "Kia",
    "model_name": "Soul EV",
    "car_type": "Wagon"
  },
  {
    "year": 2019,
    "manufacturer_name": "Lexus",
    "model_name": "NX",
    "car_type": "SUV"
  },
  {
    "year": 2019,
    "manufacturer_name": "Lexus",
    "model_name": "RC",
    "car_type": "Coupe"
  },
  {
    "year": 2019,
    "manufacturer_name": "Lexus",
    "model_name": "IS",
    "car_type": "Sedan"
  },
  {
    "year": 2019,
    "manufacturer_name": "Lexus",
    "model_name": "ES",
    "car_type": "Sedan"
  },
  {
    "year": 2019,
    "manufacturer_name": "Land Rover",
    "model_name": "Discovery Sport",
    "car_type": "SUV"
  },
  {
    "year": 2019,
    "manufacturer_name": "Land Rover",
    "model_name": "Range Rover",
    "car_type": "SUV"
  },
  {
    "year": 2019,
    "manufacturer_name": "Lincoln",
    "model_name": "MKZ",
    "car_type": "Sedan"
  },
  {
    "year": 2019,
    "manufacturer_name": "Maserati",
    "model_name": "Levante",
    "car_type": "SUV"
  },
  {
    "year": 2019,
    "manufacturer_name": "MAZDA",
    "model_name": "MX-5 Miata RF",
    "car_type": "Convertible"
  },
  {
    "year": 2019,
    "manufacturer_name": "Lexus",
    "model_name": "LX",
    "car_type": "SUV"
  },
  {
    "year": 2019,
    "manufacturer_name": "MAZDA",
    "model_name": "CX-9",
    "car_type": "SUV"
  },
  {
    "year": 2019,
    "manufacturer_name": "MAZDA",
    "model_name": "MX-5 Miata",
    "car_type": "Convertible"
  },
  {
    "year": 2019,
    "manufacturer_name": "MAZDA",
    "model_name": "CX-5",
    "car_type": "SUV"
  },
  {
    "year": 2019,
    "manufacturer_name": "Lexus",
    "model_name": "UX",
    "car_type": "SUV"
  },
  {
    "year": 2019,
    "manufacturer_name": "Mercedes-Benz",
    "model_name": "CLA",
    "car_type": "Sedan"
  },
  {
    "year": 2019,
    "manufacturer_name": "Lincoln",
    "model_name": "Continental",
    "car_type": "Sedan"
  },
  {
    "year": 2019,
    "manufacturer_name": "Lincoln",
    "model_name": "MKT",
    "car_type": "SUV"
  },
  {
    "year": 2019,
    "manufacturer_name": "Lincoln",
    "model_name": "Navigator L",
    "car_type": "SUV"
  },
  {
    "year": 2019,
    "manufacturer_name": "Lincoln",
    "model_name": "Nautilus",
    "car_type": "SUV"
  },
  {
    "year": 2019,
    "manufacturer_name": "Mercedes-Benz",
    "model_name": "GLC",
    "car_type": "SUV"
  },
  {
    "year": 2019,
    "manufacturer_name": "Lexus",
    "model_name": "RX",
    "car_type": "SUV"
  },
  {
    "year": 2019,
    "manufacturer_name": "MAZDA",
    "model_name": "CX-3",
    "car_type": "SUV"
  },
  {
    "year": 2019,
    "manufacturer_name": "Lincoln",
    "model_name": "MKC",
    "car_type": "SUV"
  },
  {
    "year": 2019,
    "manufacturer_name": "Mercedes-Benz",
    "model_name": "A-Class",
    "car_type": "Sedan"
  },
  {
    "year": 2019,
    "manufacturer_name": "MAZDA",
    "model_name": "MAZDA6",
    "car_type": "Sedan"
  },
  {
    "year": 2019,
    "manufacturer_name": "MAZDA",
    "model_name": "MAZDA3",
    "car_type": "Sedan, Hatchback"
  },
  {
    "year": 2019,
    "manufacturer_name": "Mercedes-Benz",
    "model_name": "C-Class",
    "car_type": "Convertible, Sedan, Coupe"
  },
  {
    "year": 2019,
    "manufacturer_name": "Lexus",
    "model_name": "LS",
    "car_type": "Sedan"
  },
  {
    "year": 2019,
    "manufacturer_name": "Maserati",
    "model_name": "Ghibli",
    "car_type": "Sedan"
  },
  {
    "year": 2019,
    "manufacturer_name": "Mercedes-Benz",
    "model_name": "Mercedes-AMG C-Class",
    "car_type": "Sedan, Convertible, Coupe"
  },
  {
    "year": 2019,
    "manufacturer_name": "Mercedes-Benz",
    "model_name": "GLS",
    "car_type": "SUV"
  },
  {
    "year": 2019,
    "manufacturer_name": "Mercedes-Benz",
    "model_name": "G-Class",
    "car_type": "SUV"
  },
  {
    "year": 2019,
    "manufacturer_name": "Lincoln",
    "model_name": "Navigator",
    "car_type": "SUV"
  },
  {
    "year": 2019,
    "manufacturer_name": "Mercedes-Benz",
    "model_name": "GLA",
    "car_type": "SUV"
  },
  {
    "year": 2019,
    "manufacturer_name": "Mercedes-Benz",
    "model_name": "E-Class",
    "car_type": "Coupe, Sedan, Wagon, Convertible"
  },
  {
    "year": 2019,
    "manufacturer_name": "Mercedes-Benz",
    "model_name": "CLS",
    "car_type": "Sedan"
  },
  {
    "year": 2019,
    "manufacturer_name": "Mercedes-Benz",
    "model_name": "Mercedes-AMG CLA",
    "car_type": "Sedan"
  },
  {
    "year": 2019,
    "manufacturer_name": "Mercedes-Benz",
    "model_name": "GLC Coupe",
    "car_type": "SUV"
  },
  {
    "year": 2019,
    "manufacturer_name": "Mercedes-Benz",
    "model_name": "Mercedes-AMG CLS",
    "car_type": "Sedan"
  },
  {
    "year": 2019,
    "manufacturer_name": "Hyundai",
    "model_name": "Santa Fe XL",
    "car_type": "SUV"
  },
  {
    "year": 2019,
    "manufacturer_name": "Mercedes-Benz",
    "model_name": "GLE",
    "car_type": "SUV"
  },
  {
    "year": 2019,
    "manufacturer_name": "Mercedes-Benz",
    "model_name": "Mercedes-AMG E-Class",
    "car_type": "Coupe, Convertible, Sedan, Wagon"
  },
  {
    "year": 2019,
    "manufacturer_name": "Mercedes-Benz",
    "model_name": "Mercedes-AMG GLE",
    "car_type": "SUV"
  },
  {
    "year": 2019,
    "manufacturer_name": "Mercedes-Benz",
    "model_name": "Mercedes-AMG G-Class",
    "car_type": "SUV"
  },
  {
    "year": 2019,
    "manufacturer_name": "Mercedes-Benz",
    "model_name": "Mercedes-AMG GLA",
    "car_type": "SUV"
  },
  {
    "year": 2019,
    "manufacturer_name": "Mercedes-Benz",
    "model_name": "Mercedes-AMG S-Class",
    "car_type": "Sedan, Coupe, Convertible"
  },
  {
    "year": 2019,
    "manufacturer_name": "Mercedes-Benz",
    "model_name": "SL",
    "car_type": "Convertible"
  },
  {
    "year": 2019,
    "manufacturer_name": "Mercedes-Benz",
    "model_name": "Mercedes-AMG GT",
    "car_type": "Coupe, Sedan, Convertible"
  },
  {
    "year": 2019,
    "manufacturer_name": "Mitsubishi",
    "model_name": "Mirage G4",
    "car_type": "Sedan"
  },
  {
    "year": 2019,
    "manufacturer_name": "Mercedes-Benz",
    "model_name": "Metris Passenger",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2019,
    "manufacturer_name": "Mercedes-Benz",
    "model_name": "Mercedes-AMG GLE Coupe",
    "car_type": "SUV"
  },
  {
    "year": 2019,
    "manufacturer_name": "Mercedes-Benz",
    "model_name": "Mercedes-Maybach S-Class",
    "car_type": "Sedan"
  },
  {
    "year": 2019,
    "manufacturer_name": "Mitsubishi",
    "model_name": "Outlander PHEV",
    "car_type": "SUV"
  },
  {
    "year": 2019,
    "manufacturer_name": "Mercedes-Benz",
    "model_name": "Mercedes-AMG GLC Coupe",
    "car_type": "SUV"
  },
  {
    "year": 2019,
    "manufacturer_name": "Mercedes-Benz",
    "model_name": "Sprinter 2500 Cargo",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2019,
    "manufacturer_name": "MINI",
    "model_name": "Convertible",
    "car_type": "Convertible"
  },
  {
    "year": 2019,
    "manufacturer_name": "Mercedes-Benz",
    "model_name": "S-Class",
    "car_type": "Coupe, Sedan, Convertible"
  },
  {
    "year": 2019,
    "manufacturer_name": "Mercedes-Benz",
    "model_name": "Metris Cargo",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2019,
    "manufacturer_name": "Mercedes-Benz",
    "model_name": "SLC",
    "car_type": "Convertible"
  },
  {
    "year": 2019,
    "manufacturer_name": "Mitsubishi",
    "model_name": "Eclipse Cross",
    "car_type": "SUV"
  },
  {
    "year": 2019,
    "manufacturer_name": "Mercedes-Benz",
    "model_name": "Mercedes-AMG SLC",
    "car_type": "Convertible"
  },
  {
    "year": 2019,
    "manufacturer_name": "Mercedes-Benz",
    "model_name": "Mercedes-AMG GLC",
    "car_type": "SUV"
  },
  {
    "year": 2019,
    "manufacturer_name": "Nissan",
    "model_name": "370Z",
    "car_type": "Coupe, Convertible"
  },
  {
    "year": 2019,
    "manufacturer_name": "Mercedes-Benz",
    "model_name": "Mercedes-AMG SL",
    "car_type": "Convertible"
  },
  {
    "year": 2019,
    "manufacturer_name": "MINI",
    "model_name": "Hardtop 2 Door",
    "car_type": "Hatchback"
  },
  {
    "year": 2019,
    "manufacturer_name": "MINI",
    "model_name": "Countryman",
    "car_type": "SUV"
  },
  {
    "year": 2019,
    "manufacturer_name": "Mitsubishi",
    "model_name": "Mirage",
    "car_type": "Hatchback"
  },
  {
    "year": 2019,
    "manufacturer_name": "MINI",
    "model_name": "Hardtop 4 Door",
    "car_type": "Hatchback"
  },
  {
    "year": 2019,
    "manufacturer_name": "MINI",
    "model_name": "Clubman",
    "car_type": "Hatchback"
  },
  {
    "year": 2019,
    "manufacturer_name": "Mercedes-Benz",
    "model_name": "Mercedes-AMG GLS",
    "car_type": "SUV"
  },
  {
    "year": 2019,
    "manufacturer_name": "Mitsubishi",
    "model_name": "Outlander",
    "car_type": "SUV"
  },
  {
    "year": 2019,
    "manufacturer_name": "Nissan",
    "model_name": "Pathfinder",
    "car_type": "SUV"
  },
  {
    "year": 2019,
    "manufacturer_name": "Nissan",
    "model_name": "TITAN XD Crew Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2019,
    "manufacturer_name": "Nissan",
    "model_name": "GT-R",
    "car_type": "Coupe"
  },
  {
    "year": 2019,
    "manufacturer_name": "Nissan",
    "model_name": "NV1500 Cargo",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2019,
    "manufacturer_name": "Nissan",
    "model_name": "Maxima",
    "car_type": "Sedan"
  },
  {
    "year": 2019,
    "manufacturer_name": "Nissan",
    "model_name": "NV2500 HD Cargo",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2019,
    "manufacturer_name": "Nissan",
    "model_name": "Altima",
    "car_type": "Sedan"
  },
  {
    "year": 2019,
    "manufacturer_name": "Nissan",
    "model_name": "Titan Crew Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2019,
    "manufacturer_name": "Porsche",
    "model_name": "718 Boxster",
    "car_type": "Convertible"
  },
  {
    "year": 2019,
    "manufacturer_name": "Nissan",
    "model_name": "Versa",
    "car_type": "Sedan"
  },
  {
    "year": 2019,
    "manufacturer_name": "Nissan",
    "model_name": "Frontier King Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2019,
    "manufacturer_name": "Nissan",
    "model_name": "Frontier Crew Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2019,
    "manufacturer_name": "Nissan",
    "model_name": "Armada",
    "car_type": "SUV"
  },
  {
    "year": 2019,
    "manufacturer_name": "Nissan",
    "model_name": "NV3500 HD Cargo",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2019,
    "manufacturer_name": "Nissan",
    "model_name": "NV200",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2019,
    "manufacturer_name": "Nissan",
    "model_name": "Rogue Sport",
    "car_type": "SUV"
  },
  {
    "year": 2019,
    "manufacturer_name": "Mitsubishi",
    "model_name": "Outlander Sport",
    "car_type": "SUV"
  },
  {
    "year": 2019,
    "manufacturer_name": "Nissan",
    "model_name": "Kicks",
    "car_type": "SUV"
  },
  {
    "year": 2019,
    "manufacturer_name": "Nissan",
    "model_name": "LEAF",
    "car_type": "Hatchback"
  },
  {
    "year": 2019,
    "manufacturer_name": "Nissan",
    "model_name": "Sentra",
    "car_type": "Sedan"
  },
  {
    "year": 2019,
    "manufacturer_name": "Nissan",
    "model_name": "Murano",
    "car_type": "SUV"
  },
  {
    "year": 2019,
    "manufacturer_name": "Nissan",
    "model_name": "TITAN Single Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2019,
    "manufacturer_name": "Nissan",
    "model_name": "NV200 Taxi",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2019,
    "manufacturer_name": "Nissan",
    "model_name": "NV3500 HD Passenger",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2019,
    "manufacturer_name": "Nissan",
    "model_name": "Titan King Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2019,
    "manufacturer_name": "Nissan",
    "model_name": "Rogue",
    "car_type": "SUV"
  },
  {
    "year": 2019,
    "manufacturer_name": "Nissan",
    "model_name": "TITAN XD Single Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2019,
    "manufacturer_name": "Nissan",
    "model_name": "Versa Note",
    "car_type": "Hatchback"
  },
  {
    "year": 2019,
    "manufacturer_name": "Ram",
    "model_name": "2500 Mega Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2019,
    "manufacturer_name": "Nissan",
    "model_name": "TITAN XD King Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2019,
    "manufacturer_name": "Porsche",
    "model_name": "Cayenne",
    "car_type": "SUV"
  },
  {
    "year": 2019,
    "manufacturer_name": "Ram",
    "model_name": "1500 Crew Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2019,
    "manufacturer_name": "Ram",
    "model_name": "1500 Classic Quad Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2019,
    "manufacturer_name": "Porsche",
    "model_name": "Macan",
    "car_type": "SUV"
  },
  {
    "year": 2019,
    "manufacturer_name": "Porsche",
    "model_name": "911",
    "car_type": "Coupe, Convertible"
  },
  {
    "year": 2019,
    "manufacturer_name": "Ram",
    "model_name": "1500 Classic Crew Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2019,
    "manufacturer_name": "Ram",
    "model_name": "1500 Classic Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2019,
    "manufacturer_name": "Porsche",
    "model_name": "Panamera",
    "car_type": "Sedan"
  },
  {
    "year": 2019,
    "manufacturer_name": "Porsche",
    "model_name": "718 Cayman",
    "car_type": "Coupe"
  },
  {
    "year": 2019,
    "manufacturer_name": "Ram",
    "model_name": "1500 Quad Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2019,
    "manufacturer_name": "Ram",
    "model_name": "2500 Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2019,
    "manufacturer_name": "Ram",
    "model_name": "3500 Crew Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2019,
    "manufacturer_name": "Ram",
    "model_name": "3500 Mega Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2019,
    "manufacturer_name": "Subaru",
    "model_name": "Crosstrek",
    "car_type": "SUV"
  },
  {
    "year": 2019,
    "manufacturer_name": "Ram",
    "model_name": "2500 Crew Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2019,
    "manufacturer_name": "Ram",
    "model_name": "ProMaster Cargo Van",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2019,
    "manufacturer_name": "Ram",
    "model_name": "ProMaster City",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2019,
    "manufacturer_name": "Ram",
    "model_name": "ProMaster Window Van",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2019,
    "manufacturer_name": "Subaru",
    "model_name": "WRX",
    "car_type": "Sedan"
  },
  {
    "year": 2019,
    "manufacturer_name": "Subaru",
    "model_name": "BRZ",
    "car_type": "Coupe"
  },
  {
    "year": 2019,
    "manufacturer_name": "Subaru",
    "model_name": "Impreza",
    "car_type": "Sedan, Wagon"
  },
  {
    "year": 2019,
    "manufacturer_name": "Toyota",
    "model_name": "4Runner",
    "car_type": "SUV"
  },
  {
    "year": 2019,
    "manufacturer_name": "Tesla",
    "model_name": "Model X",
    "car_type": "SUV"
  },
  {
    "year": 2019,
    "manufacturer_name": "Subaru",
    "model_name": "Legacy",
    "car_type": "Sedan"
  },
  {
    "year": 2019,
    "manufacturer_name": "Toyota",
    "model_name": "Corolla Hatchback",
    "car_type": "Hatchback"
  },
  {
    "year": 2019,
    "manufacturer_name": "Tesla",
    "model_name": "Model 3",
    "car_type": "Sedan"
  },
  {
    "year": 2019,
    "manufacturer_name": "Subaru",
    "model_name": "Forester",
    "car_type": "SUV"
  },
  {
    "year": 2019,
    "manufacturer_name": "Toyota",
    "model_name": "86",
    "car_type": "Coupe"
  },
  {
    "year": 2019,
    "manufacturer_name": "Ram",
    "model_name": "3500 Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2019,
    "manufacturer_name": "Toyota",
    "model_name": "Land Cruiser",
    "car_type": "SUV"
  },
  {
    "year": 2019,
    "manufacturer_name": "Tesla",
    "model_name": "Model S",
    "car_type": "Sedan"
  },
  {
    "year": 2019,
    "manufacturer_name": "Subaru",
    "model_name": "Ascent",
    "car_type": "SUV"
  },
  {
    "year": 2019,
    "manufacturer_name": "Toyota",
    "model_name": "Highlander Hybrid",
    "car_type": "SUV"
  },
  {
    "year": 2019,
    "manufacturer_name": "Toyota",
    "model_name": "Camry Hybrid",
    "car_type": "Sedan"
  },
  {
    "year": 2019,
    "manufacturer_name": "Toyota",
    "model_name": "Highlander",
    "car_type": "SUV"
  },
  {
    "year": 2019,
    "manufacturer_name": "Subaru",
    "model_name": "Outback",
    "car_type": "SUV"
  },
  {
    "year": 2019,
    "manufacturer_name": "Toyota",
    "model_name": "Camry",
    "car_type": "Sedan"
  },
  {
    "year": 2019,
    "manufacturer_name": "Toyota",
    "model_name": "C-HR",
    "car_type": "SUV"
  },
  {
    "year": 2019,
    "manufacturer_name": "Toyota",
    "model_name": "Avalon",
    "car_type": "Sedan"
  },
  {
    "year": 2019,
    "manufacturer_name": "Toyota",
    "model_name": "Corolla",
    "car_type": "Sedan"
  },
  {
    "year": 2019,
    "manufacturer_name": "Toyota",
    "model_name": "Avalon Hybrid",
    "car_type": "Sedan"
  },
  {
    "year": 2019,
    "manufacturer_name": "Toyota",
    "model_name": "Mirai",
    "car_type": "Sedan"
  },
  {
    "year": 2019,
    "manufacturer_name": "Toyota",
    "model_name": "RAV4",
    "car_type": "SUV"
  },
  {
    "year": 2019,
    "manufacturer_name": "Toyota",
    "model_name": "Prius",
    "car_type": "Hatchback"
  },
  {
    "year": 2019,
    "manufacturer_name": "Toyota",
    "model_name": "Yaris",
    "car_type": "Sedan"
  },
  {
    "year": 2019,
    "manufacturer_name": "Toyota",
    "model_name": "Tundra CrewMax",
    "car_type": "Pickup"
  },
  {
    "year": 2019,
    "manufacturer_name": "Volkswagen",
    "model_name": "Atlas",
    "car_type": "SUV"
  },
  {
    "year": 2019,
    "manufacturer_name": "Toyota",
    "model_name": "RAV4 Hybrid",
    "car_type": "SUV"
  },
  {
    "year": 2019,
    "manufacturer_name": "Toyota",
    "model_name": "Sequoia",
    "car_type": "SUV"
  },
  {
    "year": 2019,
    "manufacturer_name": "Toyota",
    "model_name": "Prius c",
    "car_type": "Hatchback"
  },
  {
    "year": 2019,
    "manufacturer_name": "Toyota",
    "model_name": "Tundra Double Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2019,
    "manufacturer_name": "Toyota",
    "model_name": "Tacoma Access Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2019,
    "manufacturer_name": "Toyota",
    "model_name": "Prius Prime",
    "car_type": "Hatchback"
  },
  {
    "year": 2019,
    "manufacturer_name": "Toyota",
    "model_name": "Tacoma Double Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2019,
    "manufacturer_name": "Toyota",
    "model_name": "Sienna",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2019,
    "manufacturer_name": "Volkswagen",
    "model_name": "Golf SportWagen",
    "car_type": "Wagon"
  },
  {
    "year": 2019,
    "manufacturer_name": "Volkswagen",
    "model_name": "Arteon",
    "car_type": "Sedan"
  },
  {
    "year": 2019,
    "manufacturer_name": "Volkswagen",
    "model_name": "Jetta",
    "car_type": "Sedan"
  },
  {
    "year": 2019,
    "manufacturer_name": "Volkswagen",
    "model_name": "Passat",
    "car_type": "Sedan"
  },
  {
    "year": 2019,
    "manufacturer_name": "Volkswagen",
    "model_name": "e-Golf",
    "car_type": "Hatchback"
  },
  {
    "year": 2019,
    "manufacturer_name": "Volkswagen",
    "model_name": "Golf",
    "car_type": "Hatchback"
  },
  {
    "year": 2019,
    "manufacturer_name": "Volkswagen",
    "model_name": "Golf GTI",
    "car_type": "Hatchback"
  },
  {
    "year": 2019,
    "manufacturer_name": "Volkswagen",
    "model_name": "Jetta GLI",
    "car_type": "Sedan"
  },
  {
    "year": 2019,
    "manufacturer_name": "Volkswagen",
    "model_name": "Beetle",
    "car_type": "Convertible, Coupe, Hatchback"
  },
  {
    "year": 2019,
    "manufacturer_name": "Volkswagen",
    "model_name": "Golf Alltrack",
    "car_type": "Wagon"
  },
  {
    "year": 2019,
    "manufacturer_name": "Volvo",
    "model_name": "S60",
    "car_type": "Sedan"
  },
  {
    "year": 2019,
    "manufacturer_name": "Volkswagen",
    "model_name": "Golf R",
    "car_type": "Hatchback"
  },
  {
    "year": 2019,
    "manufacturer_name": "Volvo",
    "model_name": "V60",
    "car_type": "Wagon"
  },
  {
    "year": 2019,
    "manufacturer_name": "Volvo",
    "model_name": "V90",
    "car_type": "Wagon"
  },
  {
    "year": 2019,
    "manufacturer_name": "Volvo",
    "model_name": "S90",
    "car_type": "Sedan"
  },
  {
    "year": 2019,
    "manufacturer_name": "Volvo",
    "model_name": "XC90",
    "car_type": "SUV2020"
  },
  {
    "year": 2019,
    "manufacturer_name": "Volkswagen",
    "model_name": "Tiguan",
    "car_type": "SUV"
  },
  {
    "year": 2019,
    "manufacturer_name": "Volvo",
    "model_name": "XC60",
    "car_type": "SUV"
  },
  {
    "year": 2019,
    "manufacturer_name": "Volvo",
    "model_name": "XC40",
    "car_type": "SUV"
  },
  {
    "year": 2018,
    "manufacturer_name": "Acura",
    "model_name": "ILX",
    "car_type": "Sedan"
  },
  {
    "year": 2018,
    "manufacturer_name": "Alfa Romeo",
    "model_name": "4C Spider",
    "car_type": "Convertible"
  },
  {
    "year": 2018,
    "manufacturer_name": "Acura",
    "model_name": "RLX",
    "car_type": "Sedan"
  },
  {
    "year": 2018,
    "manufacturer_name": "Acura",
    "model_name": "TLX",
    "car_type": "Sedan"
  },
  {
    "year": 2018,
    "manufacturer_name": "Aston Martin",
    "model_name": "Vanquish S",
    "car_type": "Convertible, Coupe"
  },
  {
    "year": 2018,
    "manufacturer_name": "Acura",
    "model_name": "MDX",
    "car_type": "SUV"
  },
  {
    "year": 2018,
    "manufacturer_name": "Audi",
    "model_name": "Q3",
    "car_type": "SUV"
  },
  {
    "year": 2018,
    "manufacturer_name": "Audi",
    "model_name": "A3",
    "car_type": "Sedan, Convertible"
  },
  {
    "year": 2018,
    "manufacturer_name": "Acura",
    "model_name": "RLX Sport Hybrid",
    "car_type": "Sedan"
  },
  {
    "year": 2018,
    "manufacturer_name": "Alfa Romeo",
    "model_name": "Giulia",
    "car_type": "Sedan"
  },
  {
    "year": 2018,
    "manufacturer_name": "Alfa Romeo",
    "model_name": "4C",
    "car_type": "Coupe"
  },
  {
    "year": 2018,
    "manufacturer_name": "Aston Martin",
    "model_name": "DB11",
    "car_type": "Coupe"
  },
  {
    "year": 2018,
    "manufacturer_name": "Acura",
    "model_name": "RDX",
    "car_type": "SUV"
  },
  {
    "year": 2018,
    "manufacturer_name": "Acura",
    "model_name": "MDX Sport Hybrid",
    "car_type": "SUV"
  },
  {
    "year": 2018,
    "manufacturer_name": "Audi",
    "model_name": "A7",
    "car_type": "Sedan"
  },
  {
    "year": 2018,
    "manufacturer_name": "Audi",
    "model_name": "A4 allroad",
    "car_type": "Wagon"
  },
  {
    "year": 2018,
    "manufacturer_name": "Audi",
    "model_name": "A4",
    "car_type": "Sedan"
  },
  {
    "year": 2018,
    "manufacturer_name": "Acura",
    "model_name": "NSX",
    "car_type": "Coupe"
  },
  {
    "year": 2018,
    "manufacturer_name": "Alfa Romeo",
    "model_name": "Stelvio",
    "car_type": "SUV"
  },
  {
    "year": 2018,
    "manufacturer_name": "Audi",
    "model_name": "Q5",
    "car_type": "SUV"
  },
  {
    "year": 2018,
    "manufacturer_name": "Audi",
    "model_name": "A3 Sportback e-tron",
    "car_type": "Wagon"
  },
  {
    "year": 2018,
    "manufacturer_name": "Audi",
    "model_name": "A5",
    "car_type": "Coupe, Convertible, Sedan"
  },
  {
    "year": 2018,
    "manufacturer_name": "Audi",
    "model_name": "A6",
    "car_type": "Sedan"
  },
  {
    "year": 2018,
    "manufacturer_name": "Audi",
    "model_name": "R8",
    "car_type": "Coupe, Convertible"
  },
  {
    "year": 2018,
    "manufacturer_name": "Audi",
    "model_name": "A8",
    "car_type": "Sedan"
  },
  {
    "year": 2018,
    "manufacturer_name": "Audi",
    "model_name": "Q7",
    "car_type": "SUV"
  },
  {
    "year": 2018,
    "manufacturer_name": "Audi",
    "model_name": "RS 3",
    "car_type": "Sedan"
  },
  {
    "year": 2018,
    "manufacturer_name": "Audi",
    "model_name": "S4",
    "car_type": "Sedan"
  },
  {
    "year": 2018,
    "manufacturer_name": "Audi",
    "model_name": "SQ5",
    "car_type": "SUV"
  },
  {
    "year": 2018,
    "manufacturer_name": "Audi",
    "model_name": "S3",
    "car_type": "Sedan"
  },
  {
    "year": 2018,
    "manufacturer_name": "Audi",
    "model_name": "S7",
    "car_type": "Sedan"
  },
  {
    "year": 2018,
    "manufacturer_name": "Audi",
    "model_name": "S6",
    "car_type": "Sedan"
  },
  {
    "year": 2018,
    "manufacturer_name": "Audi",
    "model_name": "S8",
    "car_type": "Sedan"
  },
  {
    "year": 2018,
    "manufacturer_name": "Audi",
    "model_name": "RS 7",
    "car_type": "Sedan"
  },
  {
    "year": 2018,
    "manufacturer_name": "Audi",
    "model_name": "RS 5",
    "car_type": "Coupe"
  },
  {
    "year": 2018,
    "manufacturer_name": "Audi",
    "model_name": "TT",
    "car_type": "Coupe, Convertible"
  },
  {
    "year": 2018,
    "manufacturer_name": "Audi",
    "model_name": "S5",
    "car_type": "Sedan, Coupe, Convertible"
  },
  {
    "year": 2018,
    "manufacturer_name": "Bentley",
    "model_name": "Bentayga",
    "car_type": "SUV"
  },
  {
    "year": 2018,
    "manufacturer_name": "BMW",
    "model_name": "4 Series",
    "car_type": "Coupe, Sedan, Convertible"
  },
  {
    "year": 2018,
    "manufacturer_name": "BMW",
    "model_name": "M5",
    "car_type": "Sedan"
  },
  {
    "year": 2018,
    "manufacturer_name": "BMW",
    "model_name": "2 Series",
    "car_type": "Coupe, Convertible"
  },
  {
    "year": 2018,
    "manufacturer_name": "BMW",
    "model_name": "M4",
    "car_type": "Convertible, Coupe"
  },
  {
    "year": 2018,
    "manufacturer_name": "BMW",
    "model_name": "X3",
    "car_type": "SUV"
  },
  {
    "year": 2018,
    "manufacturer_name": "BMW",
    "model_name": "7 Series",
    "car_type": "Sedan"
  },
  {
    "year": 2018,
    "manufacturer_name": "BMW",
    "model_name": "6 Series",
    "car_type": "Sedan, Convertible"
  },
  {
    "year": 2018,
    "manufacturer_name": "Bentley",
    "model_name": "Flying Spur",
    "car_type": "Sedan"
  },
  {
    "year": 2018,
    "manufacturer_name": "BMW",
    "model_name": "M3",
    "car_type": "Sedan"
  },
  {
    "year": 2018,
    "manufacturer_name": "Bentley",
    "model_name": "Continental",
    "car_type": "Convertible"
  },
  {
    "year": 2018,
    "manufacturer_name": "BMW",
    "model_name": "M6",
    "car_type": "Coupe, Convertible"
  },
  {
    "year": 2018,
    "manufacturer_name": "Buick",
    "model_name": "Cascada",
    "car_type": "Convertible"
  },
  {
    "year": 2018,
    "manufacturer_name": "BMW",
    "model_name": "3 Series",
    "car_type": "Sedan, Wagon"
  },
  {
    "year": 2018,
    "manufacturer_name": "Bentley",
    "model_name": "Mulsanne",
    "car_type": "Sedan"
  },
  {
    "year": 2018,
    "manufacturer_name": "BMW",
    "model_name": "X2",
    "car_type": "SUV"
  },
  {
    "year": 2018,
    "manufacturer_name": "BMW",
    "model_name": "X5 M",
    "car_type": "SUV"
  },
  {
    "year": 2018,
    "manufacturer_name": "BMW",
    "model_name": "X6",
    "car_type": "SUV"
  },
  {
    "year": 2018,
    "manufacturer_name": "BMW",
    "model_name": "i3",
    "car_type": "Hatchback"
  },
  {
    "year": 2018,
    "manufacturer_name": "BMW",
    "model_name": "M2",
    "car_type": "Coupe"
  },
  {
    "year": 2018,
    "manufacturer_name": "BMW",
    "model_name": "X4",
    "car_type": "SUV"
  },
  {
    "year": 2018,
    "manufacturer_name": "BMW",
    "model_name": "X5",
    "car_type": "SUV"
  },
  {
    "year": 2018,
    "manufacturer_name": "BMW",
    "model_name": "X1",
    "car_type": "SUV"
  },
  {
    "year": 2018,
    "manufacturer_name": "Buick",
    "model_name": "Enclave",
    "car_type": "SUV"
  },
  {
    "year": 2018,
    "manufacturer_name": "Buick",
    "model_name": "Envision",
    "car_type": "SUV"
  },
  {
    "year": 2018,
    "manufacturer_name": "BMW",
    "model_name": "5 Series",
    "car_type": "Sedan"
  },
  {
    "year": 2018,
    "manufacturer_name": "Buick",
    "model_name": "LaCrosse",
    "car_type": "Sedan"
  },
  {
    "year": 2018,
    "manufacturer_name": "Buick",
    "model_name": "Encore",
    "car_type": "SUV"
  },
  {
    "year": 2018,
    "manufacturer_name": "BMW",
    "model_name": "X6 M",
    "car_type": "SUV"
  },
  {
    "year": 2018,
    "manufacturer_name": "Buick",
    "model_name": "Regal Sportback",
    "car_type": "Sedan"
  },
  {
    "year": 2018,
    "manufacturer_name": "Buick",
    "model_name": "Regal TourX",
    "car_type": "Wagon"
  },
  {
    "year": 2018,
    "manufacturer_name": "Cadillac",
    "model_name": "CT6",
    "car_type": "Sedan"
  },
  {
    "year": 2018,
    "manufacturer_name": "Cadillac",
    "model_name": "CTS",
    "car_type": "Sedan"
  },
  {
    "year": 2018,
    "manufacturer_name": "Cadillac",
    "model_name": "ATS-V",
    "car_type": "Coupe, Sedan"
  },
  {
    "year": 2018,
    "manufacturer_name": "Chevrolet",
    "model_name": "Colorado Crew Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2018,
    "manufacturer_name": "Chevrolet",
    "model_name": "Bolt EV",
    "car_type": "Hatchback"
  },
  {
    "year": 2018,
    "manufacturer_name": "Chevrolet",
    "model_name": "Camaro",
    "car_type": "Coupe, Convertible"
  },
  {
    "year": 2018,
    "manufacturer_name": "Chevrolet",
    "model_name": "Express 2500 Passenger",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2018,
    "manufacturer_name": "Cadillac",
    "model_name": "ATS",
    "car_type": "Coupe, Sedan"
  },
  {
    "year": 2018,
    "manufacturer_name": "Chevrolet",
    "model_name": "Colorado Extended Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2018,
    "manufacturer_name": "Cadillac",
    "model_name": "CTS-V",
    "car_type": "Sedan"
  },
  {
    "year": 2018,
    "manufacturer_name": "Cadillac",
    "model_name": "Escalade ESV",
    "car_type": "SUV"
  },
  {
    "year": 2018,
    "manufacturer_name": "Cadillac",
    "model_name": "XT5",
    "car_type": "SUV"
  },
  {
    "year": 2018,
    "manufacturer_name": "Cadillac",
    "model_name": "XTS",
    "car_type": "Sedan"
  },
  {
    "year": 2018,
    "manufacturer_name": "Cadillac",
    "model_name": "Escalade",
    "car_type": "SUV"
  },
  {
    "year": 2018,
    "manufacturer_name": "Chevrolet",
    "model_name": "City Express",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2018,
    "manufacturer_name": "Chevrolet",
    "model_name": "Cruze",
    "car_type": "Sedan, Hatchback"
  },
  {
    "year": 2018,
    "manufacturer_name": "Chevrolet",
    "model_name": "Spark",
    "car_type": "Hatchback"
  },
  {
    "year": 2018,
    "manufacturer_name": "Chevrolet",
    "model_name": "Silverado 1500 Crew Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2018,
    "manufacturer_name": "Chevrolet",
    "model_name": "Express 3500 Passenger",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2018,
    "manufacturer_name": "Chevrolet",
    "model_name": "Equinox",
    "car_type": "SUV"
  },
  {
    "year": 2018,
    "manufacturer_name": "Chevrolet",
    "model_name": "Silverado 1500 Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2018,
    "manufacturer_name": "Chevrolet",
    "model_name": "Express 2500 Cargo",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2018,
    "manufacturer_name": "Chevrolet",
    "model_name": "Silverado 2500 HD Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2018,
    "manufacturer_name": "Chevrolet",
    "model_name": "Silverado 3500 HD Double Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2018,
    "manufacturer_name": "Chevrolet",
    "model_name": "Corvette",
    "car_type": "Coupe, Convertible"
  },
  {
    "year": 2018,
    "manufacturer_name": "Chevrolet",
    "model_name": "Impala",
    "car_type": "Sedan"
  },
  {
    "year": 2018,
    "manufacturer_name": "Chevrolet",
    "model_name": "Express 3500 Cargo",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2018,
    "manufacturer_name": "Chevrolet",
    "model_name": "Malibu",
    "car_type": "Sedan"
  },
  {
    "year": 2018,
    "manufacturer_name": "Chevrolet",
    "model_name": "Silverado 2500 HD Crew Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2018,
    "manufacturer_name": "Chevrolet",
    "model_name": "Silverado 2500 HD Double Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2018,
    "manufacturer_name": "Chevrolet",
    "model_name": "Sonic",
    "car_type": "Sedan, Hatchback"
  },
  {
    "year": 2018,
    "manufacturer_name": "Chrysler",
    "model_name": "300",
    "car_type": "Sedan"
  },
  {
    "year": 2018,
    "manufacturer_name": "Chevrolet",
    "model_name": "Traverse",
    "car_type": "SUV"
  },
  {
    "year": 2018,
    "manufacturer_name": "Dodge",
    "model_name": "Grand Caravan Passenger",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2018,
    "manufacturer_name": "Chrysler",
    "model_name": "Pacifica",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2018,
    "manufacturer_name": "Chevrolet",
    "model_name": "Silverado 1500 Double Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2018,
    "manufacturer_name": "Chevrolet",
    "model_name": "Silverado 3500 HD Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2018,
    "manufacturer_name": "Dodge",
    "model_name": "Journey",
    "car_type": "SUV"
  },
  {
    "year": 2018,
    "manufacturer_name": "Chevrolet",
    "model_name": "Trax",
    "car_type": "SUV"
  },
  {
    "year": 2018,
    "manufacturer_name": "Chevrolet",
    "model_name": "Suburban",
    "car_type": "SUV"
  },
  {
    "year": 2018,
    "manufacturer_name": "Chevrolet",
    "model_name": "Silverado 3500 HD Crew Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2018,
    "manufacturer_name": "Ferrari",
    "model_name": "GTC4Lusso",
    "car_type": "Hatchback"
  },
  {
    "year": 2018,
    "manufacturer_name": "Ferrari",
    "model_name": "488 GTB",
    "car_type": "Coupe"
  },
  {
    "year": 2018,
    "manufacturer_name": "Chrysler",
    "model_name": "Pacifica Hybrid",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2018,
    "manufacturer_name": "Chevrolet",
    "model_name": "Suburban 3500HD",
    "car_type": "SUV"
  },
  {
    "year": 2018,
    "manufacturer_name": "Dodge",
    "model_name": "Durango",
    "car_type": "SUV"
  },
  {
    "year": 2018,
    "manufacturer_name": "Dodge",
    "model_name": "Challenger",
    "car_type": "Coupe"
  },
  {
    "year": 2018,
    "manufacturer_name": "Chevrolet",
    "model_name": "Volt",
    "car_type": "Sedan"
  },
  {
    "year": 2018,
    "manufacturer_name": "FIAT",
    "model_name": "124 Spider",
    "car_type": "Convertible"
  },
  {
    "year": 2018,
    "manufacturer_name": "Chevrolet",
    "model_name": "Tahoe",
    "car_type": "SUV"
  },
  {
    "year": 2018,
    "manufacturer_name": "Dodge",
    "model_name": "Charger",
    "car_type": "Sedan"
  },
  {
    "year": 2018,
    "manufacturer_name": "Ferrari",
    "model_name": "812 Superfast",
    "car_type": "Coupe"
  },
  {
    "year": 2018,
    "manufacturer_name": "Ferrari",
    "model_name": "Portofino",
    "car_type": "Convertible"
  },
  {
    "year": 2018,
    "manufacturer_name": "FIAT",
    "model_name": "500e",
    "car_type": "Hatchback"
  },
  {
    "year": 2018,
    "manufacturer_name": "FIAT",
    "model_name": "500 Abarth",
    "car_type": "Hatchback"
  },
  {
    "year": 2018,
    "manufacturer_name": "Ferrari",
    "model_name": "488 Spider",
    "car_type": "Convertible"
  },
  {
    "year": 2018,
    "manufacturer_name": "FIAT",
    "model_name": "500c",
    "car_type": "Convertible"
  },
  {
    "year": 2018,
    "manufacturer_name": "FIAT",
    "model_name": "500",
    "car_type": "Hatchback"
  },
  {
    "year": 2018,
    "manufacturer_name": "Ford",
    "model_name": "F150 Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2018,
    "manufacturer_name": "Ford",
    "model_name": "Edge",
    "car_type": "SUV"
  },
  {
    "year": 2018,
    "manufacturer_name": "FIAT",
    "model_name": "500c Abarth",
    "car_type": "Convertible"
  },
  {
    "year": 2018,
    "manufacturer_name": "Ford",
    "model_name": "Escape",
    "car_type": "SUV"
  },
  {
    "year": 2018,
    "manufacturer_name": "Ford",
    "model_name": "C-MAX Hybrid",
    "car_type": "Wagon"
  },
  {
    "year": 2018,
    "manufacturer_name": "Ford",
    "model_name": "Expedition MAX",
    "car_type": "SUV"
  },
  {
    "year": 2018,
    "manufacturer_name": "Ford",
    "model_name": "F150 SuperCrew Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2018,
    "manufacturer_name": "Ford",
    "model_name": "F350 Super Duty Super Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2018,
    "manufacturer_name": "Ford",
    "model_name": "F250 Super Duty Super Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2018,
    "manufacturer_name": "FIAT",
    "model_name": "500L",
    "car_type": "Hatchback"
  },
  {
    "year": 2018,
    "manufacturer_name": "FIAT",
    "model_name": "500X",
    "car_type": "SUV"
  },
  {
    "year": 2018,
    "manufacturer_name": "Ford",
    "model_name": "Expedition",
    "car_type": "SUV"
  },
  {
    "year": 2018,
    "manufacturer_name": "Ford",
    "model_name": "F350 Super Duty Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2018,
    "manufacturer_name": "Ford",
    "model_name": "F250 Super Duty Crew Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2018,
    "manufacturer_name": "Ford",
    "model_name": "EcoSport",
    "car_type": "SUV"
  },
  {
    "year": 2018,
    "manufacturer_name": "Ford",
    "model_name": "F150 Super Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2018,
    "manufacturer_name": "Ford",
    "model_name": "Explorer",
    "car_type": "SUV"
  },
  {
    "year": 2018,
    "manufacturer_name": "Ford",
    "model_name": "Fiesta",
    "car_type": "Hatchback, Sedan"
  },
  {
    "year": 2018,
    "manufacturer_name": "Ford",
    "model_name": "F250 Super Duty Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2018,
    "manufacturer_name": "Ford",
    "model_name": "F350 Super Duty Crew Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2018,
    "manufacturer_name": "Ford",
    "model_name": "Transit 350 Wagon",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2018,
    "manufacturer_name": "Ford",
    "model_name": "Fusion",
    "car_type": "Sedan"
  },
  {
    "year": 2018,
    "manufacturer_name": "Ford",
    "model_name": "Transit 150 Wagon",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2018,
    "manufacturer_name": "Ford",
    "model_name": "F450 Super Duty Crew Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2018,
    "manufacturer_name": "Ford",
    "model_name": "Transit 150 Van",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2018,
    "manufacturer_name": "Ford",
    "model_name": "Focus",
    "car_type": "Sedan, Hatchback"
  },
  {
    "year": 2018,
    "manufacturer_name": "Ford",
    "model_name": "Transit Connect Cargo",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2018,
    "manufacturer_name": "Ford",
    "model_name": "Transit 350 HD Van",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2018,
    "manufacturer_name": "Ford",
    "model_name": "Fusion Energi",
    "car_type": "Sedan"
  },
  {
    "year": 2018,
    "manufacturer_name": "Ford",
    "model_name": "Flex",
    "car_type": "SUV"
  },
  {
    "year": 2018,
    "manufacturer_name": "Ford",
    "model_name": "Mustang",
    "car_type": "Convertible, Coupe"
  },
  {
    "year": 2018,
    "manufacturer_name": "Freightliner",
    "model_name": "Sprinter 2500 Cargo",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2018,
    "manufacturer_name": "Freightliner",
    "model_name": "Sprinter 2500 Crew",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2018,
    "manufacturer_name": "Ford",
    "model_name": "Transit 250 Van",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2018,
    "manufacturer_name": "Freightliner",
    "model_name": "Sprinter 3500 Cargo",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2018,
    "manufacturer_name": "Ford",
    "model_name": "Transit Connect Passenger",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2018,
    "manufacturer_name": "Ford",
    "model_name": "Transit 350 Van",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2018,
    "manufacturer_name": "Freightliner",
    "model_name": "Sprinter WORKER Cargo",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2018,
    "manufacturer_name": "Ford",
    "model_name": "Taurus",
    "car_type": "Sedan"
  },
  {
    "year": 2018,
    "manufacturer_name": "Freightliner",
    "model_name": "Sprinter 3500XD Cargo",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2018,
    "manufacturer_name": "Freightliner",
    "model_name": "Sprinter 2500 Passenger",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2018,
    "manufacturer_name": "GMC",
    "model_name": "Acadia",
    "car_type": "SUV"
  },
  {
    "year": 2018,
    "manufacturer_name": "Genesis",
    "model_name": "G80",
    "car_type": "Sedan"
  },
  {
    "year": 2018,
    "manufacturer_name": "GMC",
    "model_name": "Sierra 1500 Crew Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2018,
    "manufacturer_name": "GMC",
    "model_name": "Canyon Extended Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2018,
    "manufacturer_name": "Genesis",
    "model_name": "G90",
    "car_type": "Sedan"
  },
  {
    "year": 2018,
    "manufacturer_name": "GMC",
    "model_name": "Savana 2500 Passenger",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2018,
    "manufacturer_name": "GMC",
    "model_name": "Savana 3500 Passenger",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2018,
    "manufacturer_name": "GMC",
    "model_name": "Canyon Crew Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2018,
    "manufacturer_name": "GMC",
    "model_name": "Savana 3500 Cargo",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2018,
    "manufacturer_name": "GMC",
    "model_name": "Sierra 3500 HD Crew Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2018,
    "manufacturer_name": "GMC",
    "model_name": "Sierra 2500 HD Crew Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2018,
    "manufacturer_name": "GMC",
    "model_name": "Savana 2500 Cargo",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2018,
    "manufacturer_name": "GMC",
    "model_name": "Sierra 2500 HD Double Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2018,
    "manufacturer_name": "GMC",
    "model_name": "Sierra 3500 HD Double Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2018,
    "manufacturer_name": "Honda",
    "model_name": "Accord",
    "car_type": "Sedan"
  },
  {
    "year": 2018,
    "manufacturer_name": "GMC",
    "model_name": "Terrain",
    "car_type": "SUV"
  },
  {
    "year": 2018,
    "manufacturer_name": "GMC",
    "model_name": "Sierra 2500 HD Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2018,
    "manufacturer_name": "GMC",
    "model_name": "Yukon",
    "car_type": "SUV"
  },
  {
    "year": 2018,
    "manufacturer_name": "GMC",
    "model_name": "Sierra 1500 Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2018,
    "manufacturer_name": "GMC",
    "model_name": "Sierra 1500 Double Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2018,
    "manufacturer_name": "Honda",
    "model_name": "Accord Hybrid",
    "car_type": "Sedan"
  },
  {
    "year": 2018,
    "manufacturer_name": "GMC",
    "model_name": "Sierra 3500 HD Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2018,
    "manufacturer_name": "Honda",
    "model_name": "Civic Type R",
    "car_type": "Hatchback"
  },
  {
    "year": 2018,
    "manufacturer_name": "Hyundai",
    "model_name": "Santa Fe Sport",
    "car_type": "SUV"
  },
  {
    "year": 2018,
    "manufacturer_name": "Hyundai",
    "model_name": "Ioniq Hybrid",
    "car_type": "Hatchback"
  },
  {
    "year": 2018,
    "manufacturer_name": "Honda",
    "model_name": "HR-V",
    "car_type": "SUV"
  },
  {
    "year": 2018,
    "manufacturer_name": "Honda",
    "model_name": "Fit",
    "car_type": "Hatchback"
  },
  {
    "year": 2018,
    "manufacturer_name": "Honda",
    "model_name": "Civic",
    "car_type": "Coupe, Hatchback, Sedan"
  },
  {
    "year": 2018,
    "manufacturer_name": "GMC",
    "model_name": "Yukon XL",
    "car_type": "SUV"
  },
  {
    "year": 2018,
    "manufacturer_name": "Hyundai",
    "model_name": "Ioniq Plug-in Hybrid",
    "car_type": "Hatchback"
  },
  {
    "year": 2018,
    "manufacturer_name": "Hyundai",
    "model_name": "Ioniq Electric",
    "car_type": "Hatchback"
  },
  {
    "year": 2018,
    "manufacturer_name": "Honda",
    "model_name": "Clarity Plug-in Hybrid",
    "car_type": "Sedan"
  },
  {
    "year": 2018,
    "manufacturer_name": "Hyundai",
    "model_name": "Elantra GT",
    "car_type": "Hatchback"
  },
  {
    "year": 2018,
    "manufacturer_name": "Hyundai",
    "model_name": "Accent",
    "car_type": "Sedan"
  },
  {
    "year": 2018,
    "manufacturer_name": "Honda",
    "model_name": "Clarity Fuel Cell",
    "car_type": "Sedan"
  },
  {
    "year": 2018,
    "manufacturer_name": "Honda",
    "model_name": "Pilot",
    "car_type": "SUV"
  },
  {
    "year": 2018,
    "manufacturer_name": "Honda",
    "model_name": "Odyssey",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2018,
    "manufacturer_name": "Hyundai",
    "model_name": "Sonata Hybrid",
    "car_type": "Sedan"
  },
  {
    "year": 2018,
    "manufacturer_name": "Honda",
    "model_name": "CR-V",
    "car_type": "SUV"
  },
  {
    "year": 2018,
    "manufacturer_name": "Honda",
    "model_name": "Clarity Electric",
    "car_type": "Sedan"
  },
  {
    "year": 2018,
    "manufacturer_name": "Honda",
    "model_name": "Ridgeline",
    "car_type": "Pickup"
  },
  {
    "year": 2018,
    "manufacturer_name": "INFINITI",
    "model_name": "Q50",
    "car_type": "Sedan"
  },
  {
    "year": 2018,
    "manufacturer_name": "Hyundai",
    "model_name": "Elantra",
    "car_type": "Sedan"
  },
  {
    "year": 2018,
    "manufacturer_name": "Jeep",
    "model_name": "Renegade",
    "car_type": "SUV"
  },
  {
    "year": 2018,
    "manufacturer_name": "INFINITI",
    "model_name": "QX60",
    "car_type": "SUV"
  },
  {
    "year": 2018,
    "manufacturer_name": "Hyundai",
    "model_name": "Santa Fe",
    "car_type": "SUV"
  },
  {
    "year": 2018,
    "manufacturer_name": "Hyundai",
    "model_name": "Sonata Plug-in Hybrid",
    "car_type": "Sedan"
  },
  {
    "year": 2018,
    "manufacturer_name": "Jaguar",
    "model_name": "F-PACE",
    "car_type": "SUV"
  },
  {
    "year": 2018,
    "manufacturer_name": "Hyundai",
    "model_name": "Sonata",
    "car_type": "Sedan"
  },
  {
    "year": 2018,
    "manufacturer_name": "Jaguar",
    "model_name": "XF",
    "car_type": "Sedan, Wagon"
  },
  {
    "year": 2018,
    "manufacturer_name": "Jaguar",
    "model_name": "XJ",
    "car_type": "Sedan"
  },
  {
    "year": 2018,
    "manufacturer_name": "INFINITI",
    "model_name": "QX80",
    "car_type": "SUV"
  },
  {
    "year": 2018,
    "manufacturer_name": "Hyundai",
    "model_name": "Tucson",
    "car_type": "SUV"
  },
  {
    "year": 2018,
    "manufacturer_name": "INFINITI",
    "model_name": "Q60",
    "car_type": "Coupe"
  },
  {
    "year": 2018,
    "manufacturer_name": "Jaguar",
    "model_name": "E-PACE",
    "car_type": "SUV"
  },
  {
    "year": 2018,
    "manufacturer_name": "INFINITI",
    "model_name": "Q70",
    "car_type": "Sedan"
  },
  {
    "year": 2018,
    "manufacturer_name": "Hyundai",
    "model_name": "Kona",
    "car_type": "SUV"
  },
  {
    "year": 2018,
    "manufacturer_name": "Jaguar",
    "model_name": "XE",
    "car_type": "Sedan"
  },
  {
    "year": 2018,
    "manufacturer_name": "Jeep",
    "model_name": "Wrangler Unlimited",
    "car_type": "SUV"
  },
  {
    "year": 2018,
    "manufacturer_name": "Jeep",
    "model_name": "Cherokee",
    "car_type": "SUV"
  },
  {
    "year": 2018,
    "manufacturer_name": "Jaguar",
    "model_name": "F-TYPE",
    "car_type": "Convertible, Coupe"
  },
  {
    "year": 2018,
    "manufacturer_name": "Kia",
    "model_name": "Sorento",
    "car_type": "SUV"
  },
  {
    "year": 2018,
    "manufacturer_name": "Kia",
    "model_name": "Forte5",
    "car_type": "Hatchback"
  },
  {
    "year": 2018,
    "manufacturer_name": "Kia",
    "model_name": "Optima Hybrid",
    "car_type": "Sedan"
  },
  {
    "year": 2018,
    "manufacturer_name": "Kia",
    "model_name": "Forte",
    "car_type": "Sedan"
  },
  {
    "year": 2018,
    "manufacturer_name": "Kia",
    "model_name": "Cadenza",
    "car_type": "Sedan"
  },
  {
    "year": 2018,
    "manufacturer_name": "Jeep",
    "model_name": "Wrangler",
    "car_type": "SUV"
  },
  {
    "year": 2018,
    "manufacturer_name": "Kia",
    "model_name": "Soul EV",
    "car_type": "Wagon"
  },
  {
    "year": 2018,
    "manufacturer_name": "Jeep",
    "model_name": "Grand Cherokee",
    "car_type": "SUV"
  },
  {
    "year": 2018,
    "manufacturer_name": "Kia",
    "model_name": "Niro Plug-in Hybrid",
    "car_type": "Wagon"
  },
  {
    "year": 2018,
    "manufacturer_name": "Lexus",
    "model_name": "LX",
    "car_type": "SUV"
  },
  {
    "year": 2018,
    "manufacturer_name": "INFINITI",
    "model_name": "QX30",
    "car_type": "SUV"
  },
  {
    "year": 2018,
    "manufacturer_name": "Kia",
    "model_name": "Optima Plug-in Hybrid",
    "car_type": "Sedan"
  },
  {
    "year": 2018,
    "manufacturer_name": "Kia",
    "model_name": "Soul",
    "car_type": "Wagon"
  },
  {
    "year": 2018,
    "manufacturer_name": "Land Rover",
    "model_name": "Discovery",
    "car_type": "SUV"
  },
  {
    "year": 2018,
    "manufacturer_name": "Kia",
    "model_name": "Stinger",
    "car_type": "Sedan"
  },
  {
    "year": 2018,
    "manufacturer_name": "Kia",
    "model_name": "Sedona",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2018,
    "manufacturer_name": "Lexus",
    "model_name": "GS",
    "car_type": "Sedan"
  },
  {
    "year": 2018,
    "manufacturer_name": "Jeep",
    "model_name": "Compass",
    "car_type": "SUV"
  },
  {
    "year": 2018,
    "manufacturer_name": "Land Rover",
    "model_name": "Range Rover Velar",
    "car_type": "SUV"
  },
  {
    "year": 2018,
    "manufacturer_name": "Land Rover",
    "model_name": "Range Rover",
    "car_type": "SUV"
  },
  {
    "year": 2018,
    "manufacturer_name": "Kia",
    "model_name": "Sportage",
    "car_type": "SUV"
  },
  {
    "year": 2018,
    "manufacturer_name": "Kia",
    "model_name": "Niro",
    "car_type": "Wagon"
  },
  {
    "year": 2018,
    "manufacturer_name": "Kia",
    "model_name": "Optima",
    "car_type": "Sedan"
  },
  {
    "year": 2018,
    "manufacturer_name": "Lamborghini",
    "model_name": "Huracan",
    "car_type": "Coupe"
  },
  {
    "year": 2018,
    "manufacturer_name": "Kia",
    "model_name": "Rio",
    "car_type": "Sedan, Hatchback"
  },
  {
    "year": 2018,
    "manufacturer_name": "Land Rover",
    "model_name": "Discovery Sport",
    "car_type": "SUV"
  },
  {
    "year": 2018,
    "manufacturer_name": "Lexus",
    "model_name": "LC",
    "car_type": "Coupe"
  },
  {
    "year": 2018,
    "manufacturer_name": "Lexus",
    "model_name": "IS",
    "car_type": "Sedan"
  },
  {
    "year": 2018,
    "manufacturer_name": "Lincoln",
    "model_name": "MKC",
    "car_type": "SUV"
  },
  {
    "year": 2018,
    "manufacturer_name": "Lexus",
    "model_name": "RC",
    "car_type": "Coupe"
  },
  {
    "year": 2018,
    "manufacturer_name": "Land Rover",
    "model_name": "Range Rover Evoque",
    "car_type": "SUV"
  },
  {
    "year": 2018,
    "manufacturer_name": "Lincoln",
    "model_name": "Continental",
    "car_type": "Sedan"
  },
  {
    "year": 2018,
    "manufacturer_name": "Lexus",
    "model_name": "RX",
    "car_type": "SUV"
  },
  {
    "year": 2018,
    "manufacturer_name": "Lexus",
    "model_name": "LS",
    "car_type": "Sedan"
  },
  {
    "year": 2018,
    "manufacturer_name": "Land Rover",
    "model_name": "Range Rover Sport",
    "car_type": "SUV"
  },
  {
    "year": 2018,
    "manufacturer_name": "Lexus",
    "model_name": "ES",
    "car_type": "Sedan"
  },
  {
    "year": 2018,
    "manufacturer_name": "Lexus",
    "model_name": "NX",
    "car_type": "SUV"
  },
  {
    "year": 2018,
    "manufacturer_name": "Lamborghini",
    "model_name": "Aventador",
    "car_type": "Convertible, Coupe"
  },
  {
    "year": 2018,
    "manufacturer_name": "Lexus",
    "model_name": "GX",
    "car_type": "SUV"
  },
  {
    "year": 2018,
    "manufacturer_name": "Lincoln",
    "model_name": "MKT",
    "car_type": "SUV"
  },
  {
    "year": 2018,
    "manufacturer_name": "Lincoln",
    "model_name": "Navigator L",
    "car_type": "SUV"
  },
  {
    "year": 2018,
    "manufacturer_name": "Maserati",
    "model_name": "Quattroporte",
    "car_type": "Sedan"
  },
  {
    "year": 2018,
    "manufacturer_name": "Maserati",
    "model_name": "Levante",
    "car_type": "SUV"
  },
  {
    "year": 2018,
    "manufacturer_name": "Mercedes-Benz",
    "model_name": "GLS",
    "car_type": "SUV"
  },
  {
    "year": 2018,
    "manufacturer_name": "MAZDA",
    "model_name": "MX-5 Miata RF",
    "car_type": "Convertible"
  },
  {
    "year": 2018,
    "manufacturer_name": "Mercedes-Benz",
    "model_name": "GLC Coupe",
    "car_type": "SUV"
  },
  {
    "year": 2018,
    "manufacturer_name": "Lincoln",
    "model_name": "MKX",
    "car_type": "SUV"
  },
  {
    "year": 2018,
    "manufacturer_name": "Mercedes-Benz",
    "model_name": "Mercedes-AMG G-Class",
    "car_type": "SUV"
  },
  {
    "year": 2018,
    "manufacturer_name": "MAZDA",
    "model_name": "CX-5",
    "car_type": "SUV"
  },
  {
    "year": 2018,
    "manufacturer_name": "Lotus",
    "model_name": "Evora 400",
    "car_type": "Coupe"
  },
  {
    "year": 2018,
    "manufacturer_name": "McLaren",
    "model_name": "570GT",
    "car_type": "Coupe"
  },
  {
    "year": 2018,
    "manufacturer_name": "Lincoln",
    "model_name": "Navigator",
    "car_type": "SUV"
  },
  {
    "year": 2018,
    "manufacturer_name": "Mercedes-Benz",
    "model_name": "GLE",
    "car_type": "SUV"
  },
  {
    "year": 2018,
    "manufacturer_name": "Lincoln",
    "model_name": "MKZ",
    "car_type": "Sedan"
  },
  {
    "year": 2018,
    "manufacturer_name": "Maserati",
    "model_name": "GranTurismo",
    "car_type": "Coupe, Convertible"
  },
  {
    "year": 2018,
    "manufacturer_name": "McLaren",
    "model_name": "720S",
    "car_type": "Coupe"
  },
  {
    "year": 2018,
    "manufacturer_name": "Maserati",
    "model_name": "Ghibli",
    "car_type": "Sedan"
  },
  {
    "year": 2018,
    "manufacturer_name": "MAZDA",
    "model_name": "MAZDA6",
    "car_type": "Sedan"
  },
  {
    "year": 2018,
    "manufacturer_name": "McLaren",
    "model_name": "570S",
    "car_type": "Coupe, Convertible"
  },
  {
    "year": 2018,
    "manufacturer_name": "Mercedes-Benz",
    "model_name": "G-Class",
    "car_type": "SUV"
  },
  {
    "year": 2018,
    "manufacturer_name": "MAZDA",
    "model_name": "CX-9",
    "car_type": "SUV"
  },
  {
    "year": 2018,
    "manufacturer_name": "Mercedes-Benz",
    "model_name": "CLA",
    "car_type": "Sedan"
  },
  {
    "year": 2018,
    "manufacturer_name": "Mercedes-Benz",
    "model_name": "CLS",
    "car_type": "Sedan"
  },
  {
    "year": 2018,
    "manufacturer_name": "Mercedes-Benz",
    "model_name": "E-Class",
    "car_type": "Sedan, Coupe, Convertible, Wagon"
  },
  {
    "year": 2018,
    "manufacturer_name": "MAZDA",
    "model_name": "MAZDA3",
    "car_type": "Sedan, Hatchback"
  },
  {
    "year": 2018,
    "manufacturer_name": "MAZDA",
    "model_name": "MX-5 Miata",
    "car_type": "Convertible"
  },
  {
    "year": 2018,
    "manufacturer_name": "MAZDA",
    "model_name": "CX-3",
    "car_type": "SUV"
  },
  {
    "year": 2018,
    "manufacturer_name": "Mercedes-Benz",
    "model_name": "C-Class",
    "car_type": "Convertible, Coupe, Sedan"
  },
  {
    "year": 2018,
    "manufacturer_name": "Mercedes-Benz",
    "model_name": "Mercedes-AMG GLE",
    "car_type": "SUV"
  },
  {
    "year": 2018,
    "manufacturer_name": "Mercedes-Benz",
    "model_name": "Mercedes-AMG CLA",
    "car_type": "Sedan"
  },
  {
    "year": 2018,
    "manufacturer_name": "Mercedes-Benz",
    "model_name": "Mercedes-AMG GLC Coupe",
    "car_type": "SUV"
  },
  {
    "year": 2018,
    "manufacturer_name": "Mercedes-Benz",
    "model_name": "Mercedes-AMG SLC",
    "car_type": "Convertible"
  },
  {
    "year": 2018,
    "manufacturer_name": "Mercedes-Benz",
    "model_name": "Mercedes-AMG SL",
    "car_type": "Convertible"
  },
  {
    "year": 2018,
    "manufacturer_name": "Mercedes-Benz",
    "model_name": "Mercedes-AMG GLC",
    "car_type": "SUV"
  },
  {
    "year": 2018,
    "manufacturer_name": "Mercedes-Benz",
    "model_name": "Mercedes-AMG E-Class",
    "car_type": "Sedan, Wagon"
  },
  {
    "year": 2018,
    "manufacturer_name": "Mercedes-Benz",
    "model_name": "Mercedes-AMG GLE Coupe",
    "car_type": "SUV"
  },
  {
    "year": 2018,
    "manufacturer_name": "Mercedes-Benz",
    "model_name": "Mercedes-AMG CLS",
    "car_type": "Sedan"
  },
  {
    "year": 2018,
    "manufacturer_name": "Mercedes-Benz",
    "model_name": "Sprinter 2500 Crew",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2018,
    "manufacturer_name": "Mercedes-Benz",
    "model_name": "GLA",
    "car_type": "SUV"
  },
  {
    "year": 2018,
    "manufacturer_name": "Mercedes-Benz",
    "model_name": "GLC",
    "car_type": "SUV"
  },
  {
    "year": 2018,
    "manufacturer_name": "Mercedes-Benz",
    "model_name": "SLC",
    "car_type": "Convertible"
  },
  {
    "year": 2018,
    "manufacturer_name": "Mercedes-Benz",
    "model_name": "Mercedes-AMG GT",
    "car_type": "Coupe, Convertible"
  },
  {
    "year": 2018,
    "manufacturer_name": "Mercedes-Benz",
    "model_name": "Metris Passenger",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2018,
    "manufacturer_name": "Mercedes-Benz",
    "model_name": "Mercedes-AMG GLA",
    "car_type": "SUV"
  },
  {
    "year": 2018,
    "manufacturer_name": "Mercedes-Benz",
    "model_name": "Sprinter 2500 Cargo",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2018,
    "manufacturer_name": "Mercedes-Benz",
    "model_name": "Mercedes-AMG GLS",
    "car_type": "SUV"
  },
  {
    "year": 2018,
    "manufacturer_name": "Mercedes-Benz",
    "model_name": "Mercedes-AMG C-Class",
    "car_type": "Convertible, Sedan, Coupe"
  },
  {
    "year": 2018,
    "manufacturer_name": "Mercedes-Benz",
    "model_name": "Metris WORKER Cargo",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2018,
    "manufacturer_name": "Mercedes-Benz",
    "model_name": "Mercedes-AMG S-Class",
    "car_type": "Coupe, Convertible, Sedan"
  },
  {
    "year": 2018,
    "manufacturer_name": "Mercedes-Benz",
    "model_name": "Metris Cargo",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2018,
    "manufacturer_name": "Mercedes-Benz",
    "model_name": "Metris WORKER Passenger",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2018,
    "manufacturer_name": "Mercedes-Benz",
    "model_name": "Mercedes-Maybach S-Class",
    "car_type": "Sedan"
  },
  {
    "year": 2018,
    "manufacturer_name": "Nissan",
    "model_name": "LEAF",
    "car_type": "Hatchback"
  },
  {
    "year": 2018,
    "manufacturer_name": "MINI",
    "model_name": "Countryman",
    "car_type": "SUV"
  },
  {
    "year": 2018,
    "manufacturer_name": "Nissan",
    "model_name": "Armada",
    "car_type": "SUV"
  },
  {
    "year": 2018,
    "manufacturer_name": "Mercedes-Benz",
    "model_name": "SL",
    "car_type": "Convertible"
  },
  {
    "year": 2018,
    "manufacturer_name": "Mitsubishi",
    "model_name": "Outlander",
    "car_type": "SUV"
  },
  {
    "year": 2018,
    "manufacturer_name": "Nissan",
    "model_name": "Altima",
    "car_type": "Sedan"
  },
  {
    "year": 2018,
    "manufacturer_name": "Mercedes-Benz",
    "model_name": "Sprinter 3500 XD Cargo",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2018,
    "manufacturer_name": "MINI",
    "model_name": "Convertible",
    "car_type": "Convertible"
  },
  {
    "year": 2018,
    "manufacturer_name": "Nissan",
    "model_name": "Frontier King Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2018,
    "manufacturer_name": "MINI",
    "model_name": "Hardtop 2 Door",
    "car_type": "Hatchback"
  },
  {
    "year": 2018,
    "manufacturer_name": "Mitsubishi",
    "model_name": "Outlander PHEV",
    "car_type": "SUV"
  },
  {
    "year": 2018,
    "manufacturer_name": "MINI",
    "model_name": "Hardtop 4 Door",
    "car_type": "Hatchback"
  },
  {
    "year": 2018,
    "manufacturer_name": "MINI",
    "model_name": "Clubman",
    "car_type": "Hatchback"
  },
  {
    "year": 2018,
    "manufacturer_name": "Mercedes-Benz",
    "model_name": "Sprinter 2500 Passenger",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2018,
    "manufacturer_name": "Nissan",
    "model_name": "Frontier Crew Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2018,
    "manufacturer_name": "Mitsubishi",
    "model_name": "Mirage",
    "car_type": "Hatchback"
  },
  {
    "year": 2018,
    "manufacturer_name": "Mercedes-Benz",
    "model_name": "Sprinter WORKER Cargo",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2018,
    "manufacturer_name": "Mitsubishi",
    "model_name": "Mirage G4",
    "car_type": "Sedan"
  },
  {
    "year": 2018,
    "manufacturer_name": "Mitsubishi",
    "model_name": "Eclipse Cross",
    "car_type": "SUV"
  },
  {
    "year": 2018,
    "manufacturer_name": "Nissan",
    "model_name": "Maxima",
    "car_type": "Sedan"
  },
  {
    "year": 2018,
    "manufacturer_name": "Nissan",
    "model_name": "Murano",
    "car_type": "SUV"
  },
  {
    "year": 2018,
    "manufacturer_name": "Mercedes-Benz",
    "model_name": "Sprinter 3500 Cargo",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2018,
    "manufacturer_name": "Mercedes-Benz",
    "model_name": "S-Class",
    "car_type": "Sedan, Coupe, Convertible"
  },
  {
    "year": 2018,
    "manufacturer_name": "Mitsubishi",
    "model_name": "Outlander Sport",
    "car_type": "SUV"
  },
  {
    "year": 2018,
    "manufacturer_name": "Nissan",
    "model_name": "TITAN XD Crew Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2018,
    "manufacturer_name": "Nissan",
    "model_name": "NV3500 HD Passenger",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2018,
    "manufacturer_name": "Nissan",
    "model_name": "NV200",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2018,
    "manufacturer_name": "Nissan",
    "model_name": "370Z",
    "car_type": "Coupe, Convertible"
  },
  {
    "year": 2018,
    "manufacturer_name": "Nissan",
    "model_name": "Titan Crew Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2018,
    "manufacturer_name": "Nissan",
    "model_name": "NV3500 HD Cargo",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2018,
    "manufacturer_name": "Nissan",
    "model_name": "GT-R",
    "car_type": "Coupe"
  },
  {
    "year": 2018,
    "manufacturer_name": "Nissan",
    "model_name": "TITAN XD Single Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2018,
    "manufacturer_name": "Nissan",
    "model_name": "NV2500 HD Cargo",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2018,
    "manufacturer_name": "Nissan",
    "model_name": "Kicks",
    "car_type": "SUV"
  },
  {
    "year": 2018,
    "manufacturer_name": "Nissan",
    "model_name": "TITAN XD King Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2018,
    "manufacturer_name": "Nissan",
    "model_name": "NV1500 Cargo",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2018,
    "manufacturer_name": "Nissan",
    "model_name": "TITAN Single Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2018,
    "manufacturer_name": "Nissan",
    "model_name": "Rogue Sport",
    "car_type": "SUV"
  },
  {
    "year": 2018,
    "manufacturer_name": "Porsche",
    "model_name": "718 Boxster",
    "car_type": "Convertible"
  },
  {
    "year": 2018,
    "manufacturer_name": "Nissan",
    "model_name": "Rogue",
    "car_type": "SUV"
  },
  {
    "year": 2018,
    "manufacturer_name": "Nissan",
    "model_name": "Sentra",
    "car_type": "Sedan"
  },
  {
    "year": 2018,
    "manufacturer_name": "Porsche",
    "model_name": "911",
    "car_type": "Coupe, Convertible"
  },
  {
    "year": 2018,
    "manufacturer_name": "Nissan",
    "model_name": "Versa",
    "car_type": "Sedan"
  },
  {
    "year": 2018,
    "manufacturer_name": "Nissan",
    "model_name": "Versa Note",
    "car_type": "Hatchback"
  },
  {
    "year": 2018,
    "manufacturer_name": "Nissan",
    "model_name": "Pathfinder",
    "car_type": "SUV"
  },
  {
    "year": 2018,
    "manufacturer_name": "Porsche",
    "model_name": "718 Cayman",
    "car_type": "Coupe"
  },
  {
    "year": 2018,
    "manufacturer_name": "Nissan",
    "model_name": "Titan King Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2018,
    "manufacturer_name": "Porsche",
    "model_name": "Cayenne",
    "car_type": "SUV"
  },
  {
    "year": 2018,
    "manufacturer_name": "Ram",
    "model_name": "2500 Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2018,
    "manufacturer_name": "Ram",
    "model_name": "1500 Quad Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2018,
    "manufacturer_name": "Rolls-Royce",
    "model_name": "Ghost",
    "car_type": "Sedan"
  },
  {
    "year": 2018,
    "manufacturer_name": "Subaru",
    "model_name": "Crosstrek",
    "car_type": "SUV"
  },
  {
    "year": 2018,
    "manufacturer_name": "Ram",
    "model_name": "1500 Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2018,
    "manufacturer_name": "Ram",
    "model_name": "3500 Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2018,
    "manufacturer_name": "Tesla",
    "model_name": "Model S",
    "car_type": "Sedan"
  },
  {
    "year": 2018,
    "manufacturer_name": "smart",
    "model_name": "fortwo electric drive",
    "car_type": "Hatchback"
  },
  {
    "year": 2018,
    "manufacturer_name": "Rolls-Royce",
    "model_name": "Wraith",
    "car_type": "Coupe"
  },
  {
    "year": 2018,
    "manufacturer_name": "Ram",
    "model_name": "1500 Crew Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2018,
    "manufacturer_name": "Ram",
    "model_name": "ProMaster Cargo Van",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2018,
    "manufacturer_name": "Ram",
    "model_name": "2500 Crew Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2018,
    "manufacturer_name": "Ram",
    "model_name": "2500 Mega Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2018,
    "manufacturer_name": "Porsche",
    "model_name": "Panamera",
    "car_type": "Sedan"
  },
  {
    "year": 2018,
    "manufacturer_name": "Porsche",
    "model_name": "Macan",
    "car_type": "SUV"
  },
  {
    "year": 2018,
    "manufacturer_name": "Tesla",
    "model_name": "Model 3",
    "car_type": "Sedan"
  },
  {
    "year": 2018,
    "manufacturer_name": "Ram",
    "model_name": "3500 Crew Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2018,
    "manufacturer_name": "Subaru",
    "model_name": "Forester",
    "car_type": "SUV"
  },
  {
    "year": 2018,
    "manufacturer_name": "Rolls-Royce",
    "model_name": "Dawn",
    "car_type": "Convertible"
  },
  {
    "year": 2018,
    "manufacturer_name": "Ram",
    "model_name": "ProMaster City",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2018,
    "manufacturer_name": "smart",
    "model_name": "fortwo electric drive cabrio",
    "car_type": "Convertible"
  },
  {
    "year": 2018,
    "manufacturer_name": "Ram",
    "model_name": "ProMaster Window Van",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2018,
    "manufacturer_name": "Subaru",
    "model_name": "WRX",
    "car_type": "Sedan"
  },
  {
    "year": 2018,
    "manufacturer_name": "Ram",
    "model_name": "3500 Mega Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2018,
    "manufacturer_name": "Subaru",
    "model_name": "Impreza",
    "car_type": "Wagon, Sedan"
  },
  {
    "year": 2018,
    "manufacturer_name": "Rolls-Royce",
    "model_name": "Phantom",
    "car_type": "Sedan"
  },
  {
    "year": 2018,
    "manufacturer_name": "Subaru",
    "model_name": "BRZ",
    "car_type": "Coupe"
  },
  {
    "year": 2018,
    "manufacturer_name": "Toyota",
    "model_name": "Avalon Hybrid",
    "car_type": "Sedan"
  },
  {
    "year": 2018,
    "manufacturer_name": "Subaru",
    "model_name": "Legacy",
    "car_type": "Sedan"
  },
  {
    "year": 2018,
    "manufacturer_name": "Toyota",
    "model_name": "86",
    "car_type": "Coupe"
  },
  {
    "year": 2018,
    "manufacturer_name": "Toyota",
    "model_name": "Avalon",
    "car_type": "Sedan"
  },
  {
    "year": 2018,
    "manufacturer_name": "Toyota",
    "model_name": "C-HR",
    "car_type": "SUV"
  },
  {
    "year": 2018,
    "manufacturer_name": "Toyota",
    "model_name": "4Runner",
    "car_type": "SUV"
  },
  {
    "year": 2018,
    "manufacturer_name": "Subaru",
    "model_name": "Outback",
    "car_type": "SUV"
  },
  {
    "year": 2018,
    "manufacturer_name": "Toyota",
    "model_name": "Corolla iM",
    "car_type": "Hatchback"
  },
  {
    "year": 2018,
    "manufacturer_name": "Toyota",
    "model_name": "Highlander",
    "car_type": "SUV"
  },
  {
    "year": 2018,
    "manufacturer_name": "Toyota",
    "model_name": "Camry",
    "car_type": "Sedan"
  },
  {
    "year": 2018,
    "manufacturer_name": "Toyota",
    "model_name": "Mirai",
    "car_type": "Sedan"
  },
  {
    "year": 2018,
    "manufacturer_name": "Toyota",
    "model_name": "Highlander Hybrid",
    "car_type": "SUV"
  },
  {
    "year": 2018,
    "manufacturer_name": "Toyota",
    "model_name": "Camry Hybrid",
    "car_type": "Sedan"
  },
  {
    "year": 2018,
    "manufacturer_name": "Toyota",
    "model_name": "Prius",
    "car_type": "Hatchback"
  },
  {
    "year": 2018,
    "manufacturer_name": "Toyota",
    "model_name": "Land Cruiser",
    "car_type": "SUV"
  },
  {
    "year": 2018,
    "manufacturer_name": "Toyota",
    "model_name": "Corolla",
    "car_type": "Sedan"
  },
  {
    "year": 2018,
    "manufacturer_name": "Toyota",
    "model_name": "Prius c",
    "car_type": "Hatchback"
  },
  {
    "year": 2018,
    "manufacturer_name": "Tesla",
    "model_name": "Model X",
    "car_type": "SUV"
  },
  {
    "year": 2018,
    "manufacturer_name": "Toyota",
    "model_name": "Prius Prime",
    "car_type": "Hatchback"
  },
  {
    "year": 2018,
    "manufacturer_name": "Toyota",
    "model_name": "Tacoma Access Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2018,
    "manufacturer_name": "Toyota",
    "model_name": "Sequoia",
    "car_type": "SUV"
  },
  {
    "year": 2018,
    "manufacturer_name": "Toyota",
    "model_name": "Tundra CrewMax",
    "car_type": "Pickup"
  },
  {
    "year": 2018,
    "manufacturer_name": "Toyota",
    "model_name": "Sienna",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2018,
    "manufacturer_name": "Toyota",
    "model_name": "RAV4",
    "car_type": "SUV"
  },
  {
    "year": 2018,
    "manufacturer_name": "Toyota",
    "model_name": "Tacoma Double Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2018,
    "manufacturer_name": "Toyota",
    "model_name": "RAV4 Hybrid",
    "car_type": "SUV"
  },
  {
    "year": 2018,
    "manufacturer_name": "Toyota",
    "model_name": "Tundra Double Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2018,
    "manufacturer_name": "Volkswagen",
    "model_name": "Golf",
    "car_type": "Hatchback"
  },
  {
    "year": 2018,
    "manufacturer_name": "Volkswagen",
    "model_name": "Golf GTI",
    "car_type": "Hatchback"
  },
  {
    "year": 2018,
    "manufacturer_name": "Volkswagen",
    "model_name": "Tiguan",
    "car_type": "SUV"
  },
  {
    "year": 2018,
    "manufacturer_name": "Volvo",
    "model_name": "V90",
    "car_type": "Wagon"
  },
  {
    "year": 2018,
    "manufacturer_name": "Volkswagen",
    "model_name": "Golf R",
    "car_type": "Hatchback"
  },
  {
    "year": 2018,
    "manufacturer_name": "Volvo",
    "model_name": "S60",
    "car_type": "Sedan"
  },
  {
    "year": 2018,
    "manufacturer_name": "Volkswagen",
    "model_name": "Atlas",
    "car_type": "SUV"
  },
  {
    "year": 2018,
    "manufacturer_name": "Volkswagen",
    "model_name": "Golf Alltrack",
    "car_type": "Wagon"
  },
  {
    "year": 2018,
    "manufacturer_name": "Volvo",
    "model_name": "V60",
    "car_type": "Wagon"
  },
  {
    "year": 2017,
    "manufacturer_name": "Alfa Romeo",
    "model_name": "Giulia",
    "car_type": "Sedan"
  },
  {
    "year": 2018,
    "manufacturer_name": "Toyota",
    "model_name": "Yaris iA",
    "car_type": "Sedan"
  },
  {
    "year": 2018,
    "manufacturer_name": "Volkswagen",
    "model_name": "e-Golf",
    "car_type": "Hatchback"
  },
  {
    "year": 2017,
    "manufacturer_name": "Acura",
    "model_name": "MDX Sport Hybrid",
    "car_type": "SUV"
  },
  {
    "year": 2018,
    "manufacturer_name": "Volkswagen",
    "model_name": "Jetta",
    "car_type": "Sedan"
  },
  {
    "year": 2017,
    "manufacturer_name": "Acura",
    "model_name": "MDX",
    "car_type": "SUV"
  },
  {
    "year": 2017,
    "manufacturer_name": "Acura",
    "model_name": "RDX",
    "car_type": "SUV"
  },
  {
    "year": 2018,
    "manufacturer_name": "Toyota",
    "model_name": "Yaris",
    "car_type": "Hatchback"
  },
  {
    "year": 2017,
    "manufacturer_name": "Acura",
    "model_name": "NSX",
    "car_type": "Coupe"
  },
  {
    "year": 2018,
    "manufacturer_name": "Volkswagen",
    "model_name": "Golf SportWagen",
    "car_type": "Wagon"
  },
  {
    "year": 2018,
    "manufacturer_name": "Volkswagen",
    "model_name": "Beetle",
    "car_type": "Hatchback, Convertible"
  },
  {
    "year": 2018,
    "manufacturer_name": "Volvo",
    "model_name": "S90",
    "car_type": "Sedan"
  },
  {
    "year": 2018,
    "manufacturer_name": "Volvo",
    "model_name": "XC60",
    "car_type": "SUV"
  },
  {
    "year": 2017,
    "manufacturer_name": "Acura",
    "model_name": "ILX",
    "car_type": "Sedan"
  },
  {
    "year": 2018,
    "manufacturer_name": "Volkswagen",
    "model_name": "Passat",
    "car_type": "Sedan"
  },
  {
    "year": 2018,
    "manufacturer_name": "Volvo",
    "model_name": "XC90",
    "car_type": "SUV"
  },
  {
    "year": 2018,
    "manufacturer_name": "Volkswagen",
    "model_name": "Tiguan Limited",
    "car_type": "SUV"
  },
  {
    "year": 2017,
    "manufacturer_name": "Acura",
    "model_name": "RLX Sport Hybrid",
    "car_type": "Sedan"
  },
  {
    "year": 2017,
    "manufacturer_name": "Alfa Romeo",
    "model_name": "4C",
    "car_type": "Coupe"
  },
  {
    "year": 2017,
    "manufacturer_name": "Acura",
    "model_name": "RLX",
    "car_type": "Sedan"
  },
  {
    "year": 2017,
    "manufacturer_name": "Audi",
    "model_name": "A4 allroad",
    "car_type": "Wagon"
  },
  {
    "year": 2017,
    "manufacturer_name": "Acura",
    "model_name": "TLX",
    "car_type": "Sedan"
  },
  {
    "year": 2017,
    "manufacturer_name": "Aston Martin",
    "model_name": "Rapide S",
    "car_type": "Sedan"
  },
  {
    "year": 2017,
    "manufacturer_name": "Audi",
    "model_name": "A8",
    "car_type": "Sedan"
  },
  {
    "year": 2017,
    "manufacturer_name": "Audi",
    "model_name": "A3 Sportback e-tron",
    "car_type": "Wagon"
  },
  {
    "year": 2017,
    "manufacturer_name": "Audi",
    "model_name": "Q5",
    "car_type": "SUV"
  },
  {
    "year": 2017,
    "manufacturer_name": "Audi",
    "model_name": "A3",
    "car_type": "Sedan, Convertible"
  },
  {
    "year": 2017,
    "manufacturer_name": "Aston Martin",
    "model_name": "Vanquish",
    "car_type": "Coupe, Convertible"
  },
  {
    "year": 2017,
    "manufacturer_name": "Audi",
    "model_name": "Q7",
    "car_type": "SUV"
  },
  {
    "year": 2017,
    "manufacturer_name": "Aston Martin",
    "model_name": "DB11",
    "car_type": "Coupe"
  },
  {
    "year": 2017,
    "manufacturer_name": "Aston Martin",
    "model_name": "Vantage",
    "car_type": "Convertible, Coupe"
  },
  {
    "year": 2017,
    "manufacturer_name": "Audi",
    "model_name": "A7",
    "car_type": "Sedan"
  },
  {
    "year": 2017,
    "manufacturer_name": "Audi",
    "model_name": "Q3",
    "car_type": "SUV"
  },
  {
    "year": 2017,
    "manufacturer_name": "Audi",
    "model_name": "A4",
    "car_type": "Sedan"
  },
  {
    "year": 2017,
    "manufacturer_name": "Audi",
    "model_name": "A5 Sport",
    "car_type": "Convertible, Coupe"
  },
  {
    "year": 2017,
    "manufacturer_name": "Audi",
    "model_name": "A6",
    "car_type": "Sedan"
  },
  {
    "year": 2017,
    "manufacturer_name": "Audi",
    "model_name": "R8",
    "car_type": "Coupe, Convertible"
  },
  {
    "year": 2017,
    "manufacturer_name": "Audi",
    "model_name": "S6",
    "car_type": "Sedan"
  },
  {
    "year": 2017,
    "manufacturer_name": "Audi",
    "model_name": "RS 3",
    "car_type": "Sedan"
  },
  {
    "year": 2017,
    "manufacturer_name": "Audi",
    "model_name": "SQ5",
    "car_type": "SUV"
  },
  {
    "year": 2017,
    "manufacturer_name": "Audi",
    "model_name": "S5",
    "car_type": "Coupe, Convertible"
  },
  {
    "year": 2017,
    "manufacturer_name": "Audi",
    "model_name": "S3",
    "car_type": "Sedan"
  },
  {
    "year": 2017,
    "manufacturer_name": "Audi",
    "model_name": "RS 7",
    "car_type": "Sedan"
  },
  {
    "year": 2017,
    "manufacturer_name": "Audi",
    "model_name": "S8",
    "car_type": "Sedan"
  },
  {
    "year": 2017,
    "manufacturer_name": "Audi",
    "model_name": "S7",
    "car_type": "Sedan"
  },
  {
    "year": 2017,
    "manufacturer_name": "Bentley",
    "model_name": "Mulsanne",
    "car_type": "Sedan"
  },
  {
    "year": 2017,
    "manufacturer_name": "BMW",
    "model_name": "5 Series",
    "car_type": "Sedan"
  },
  {
    "year": 2017,
    "manufacturer_name": "BMW",
    "model_name": "7 Series",
    "car_type": "Sedan"
  },
  {
    "year": 2017,
    "manufacturer_name": "Bentley",
    "model_name": "Continental",
    "car_type": "Convertible, Coupe"
  },
  {
    "year": 2017,
    "manufacturer_name": "BMW",
    "model_name": "X4",
    "car_type": "SUV"
  },
  {
    "year": 2017,
    "manufacturer_name": "BMW",
    "model_name": "6 Series",
    "car_type": "Coupe, Sedan, Convertible"
  },
  {
    "year": 2017,
    "manufacturer_name": "Audi",
    "model_name": "TT",
    "car_type": "Coupe, Convertible"
  },
  {
    "year": 2017,
    "manufacturer_name": "Bentley",
    "model_name": "Bentayga",
    "car_type": "SUV"
  },
  {
    "year": 2017,
    "manufacturer_name": "Bentley",
    "model_name": "Flying Spur",
    "car_type": "Sedan"
  },
  {
    "year": 2017,
    "manufacturer_name": "BMW",
    "model_name": "i8",
    "car_type": "Coupe"
  },
  {
    "year": 2017,
    "manufacturer_name": "BMW",
    "model_name": "4 Series",
    "car_type": "Sedan, Coupe, Convertible"
  },
  {
    "year": 2017,
    "manufacturer_name": "BMW",
    "model_name": "2 Series",
    "car_type": "Convertible, Coupe"
  },
  {
    "year": 2017,
    "manufacturer_name": "BMW",
    "model_name": "3 Series",
    "car_type": "Sedan, Wagon"
  },
  {
    "year": 2017,
    "manufacturer_name": "BMW",
    "model_name": "M2",
    "car_type": "Coupe"
  },
  {
    "year": 2017,
    "manufacturer_name": "BMW",
    "model_name": "i3",
    "car_type": "Hatchback"
  },
  {
    "year": 2017,
    "manufacturer_name": "BMW",
    "model_name": "M3",
    "car_type": "Sedan"
  },
  {
    "year": 2017,
    "manufacturer_name": "BMW",
    "model_name": "X6 M",
    "car_type": "SUV"
  },
  {
    "year": 2017,
    "manufacturer_name": "Cadillac",
    "model_name": "CTS",
    "car_type": "Sedan"
  },
  {
    "year": 2017,
    "manufacturer_name": "Buick",
    "model_name": "Regal",
    "car_type": "Sedan"
  },
  {
    "year": 2017,
    "manufacturer_name": "BMW",
    "model_name": "X3",
    "car_type": "SUV"
  },
  {
    "year": 2017,
    "manufacturer_name": "Buick",
    "model_name": "Envision",
    "car_type": "SUV"
  },
  {
    "year": 2017,
    "manufacturer_name": "Buick",
    "model_name": "Cascada",
    "car_type": "Convertible"
  },
  {
    "year": 2017,
    "manufacturer_name": "BMW",
    "model_name": "X1",
    "car_type": "SUV"
  },
  {
    "year": 2017,
    "manufacturer_name": "BMW",
    "model_name": "X5",
    "car_type": "SUV"
  },
  {
    "year": 2017,
    "manufacturer_name": "BMW",
    "model_name": "M4",
    "car_type": "Convertible, Coupe"
  },
  {
    "year": 2017,
    "manufacturer_name": "BMW",
    "model_name": "X6",
    "car_type": "SUV"
  },
  {
    "year": 2017,
    "manufacturer_name": "Buick",
    "model_name": "Enclave",
    "car_type": "SUV"
  },
  {
    "year": 2017,
    "manufacturer_name": "Buick",
    "model_name": "LaCrosse",
    "car_type": "Sedan"
  },
  {
    "year": 2017,
    "manufacturer_name": "BMW",
    "model_name": "X5 M",
    "car_type": "SUV"
  },
  {
    "year": 2017,
    "manufacturer_name": "Cadillac",
    "model_name": "ATS-V",
    "car_type": "Sedan, Coupe"
  },
  {
    "year": 2017,
    "manufacturer_name": "BMW",
    "model_name": "M6",
    "car_type": "Coupe, Convertible"
  },
  {
    "year": 2017,
    "manufacturer_name": "Cadillac",
    "model_name": "CT6",
    "car_type": "Sedan"
  },
  {
    "year": 2017,
    "manufacturer_name": "Buick",
    "model_name": "Encore",
    "car_type": "SUV"
  },
  {
    "year": 2017,
    "manufacturer_name": "Buick",
    "model_name": "Verano",
    "car_type": "Sedan"
  },
  {
    "year": 2017,
    "manufacturer_name": "Chevrolet",
    "model_name": "Colorado Crew Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2017,
    "manufacturer_name": "Chevrolet",
    "model_name": "Silverado 2500 HD Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2017,
    "manufacturer_name": "Chevrolet",
    "model_name": "Bolt EV",
    "car_type": "Hatchback"
  },
  {
    "year": 2017,
    "manufacturer_name": "Cadillac",
    "model_name": "Escalade",
    "car_type": "SUV"
  },
  {
    "year": 2017,
    "manufacturer_name": "Chevrolet",
    "model_name": "Colorado Extended Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2017,
    "manufacturer_name": "Cadillac",
    "model_name": "CTS-V",
    "car_type": "Sedan"
  },
  {
    "year": 2017,
    "manufacturer_name": "Cadillac",
    "model_name": "Escalade ESV",
    "car_type": "SUV"
  },
  {
    "year": 2017,
    "manufacturer_name": "Chevrolet",
    "model_name": "Corvette",
    "car_type": "Convertible, Coupe"
  },
  {
    "year": 2017,
    "manufacturer_name": "Cadillac",
    "model_name": "XT5",
    "car_type": "SUV"
  },
  {
    "year": 2017,
    "manufacturer_name": "Chevrolet",
    "model_name": "Camaro",
    "car_type": "Coupe, Convertible"
  },
  {
    "year": 2017,
    "manufacturer_name": "Cadillac",
    "model_name": "XTS",
    "car_type": "Sedan"
  },
  {
    "year": 2017,
    "manufacturer_name": "Cadillac",
    "model_name": "ATS",
    "car_type": "Coupe, Sedan"
  },
  {
    "year": 2017,
    "manufacturer_name": "Chevrolet",
    "model_name": "Impala",
    "car_type": "Sedan"
  },
  {
    "year": 2017,
    "manufacturer_name": "Chevrolet",
    "model_name": "Express 2500 Cargo",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2017,
    "manufacturer_name": "Chevrolet",
    "model_name": "City Express",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2017,
    "manufacturer_name": "Chevrolet",
    "model_name": "Silverado 1500 Crew Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2017,
    "manufacturer_name": "Chevrolet",
    "model_name": "Cruze",
    "car_type": "Hatchback, Sedan"
  },
  {
    "year": 2017,
    "manufacturer_name": "Chevrolet",
    "model_name": "Silverado 1500 Double Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2017,
    "manufacturer_name": "Chevrolet",
    "model_name": "Sonic",
    "car_type": "Sedan, Hatchback"
  },
  {
    "year": 2017,
    "manufacturer_name": "Chevrolet",
    "model_name": "Silverado 1500 Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2017,
    "manufacturer_name": "Chevrolet",
    "model_name": "Equinox",
    "car_type": "SUV"
  },
  {
    "year": 2017,
    "manufacturer_name": "Chevrolet",
    "model_name": "Express 2500 Passenger",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2017,
    "manufacturer_name": "Chevrolet",
    "model_name": "Malibu",
    "car_type": "Sedan"
  },
  {
    "year": 2017,
    "manufacturer_name": "Chevrolet",
    "model_name": "Silverado 2500 HD Double Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2017,
    "manufacturer_name": "Chevrolet",
    "model_name": "Spark",
    "car_type": "Hatchback"
  },
  {
    "year": 2017,
    "manufacturer_name": "Chevrolet",
    "model_name": "Silverado 2500 HD Crew Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2017,
    "manufacturer_name": "Chevrolet",
    "model_name": "Express 3500 Cargo",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2017,
    "manufacturer_name": "Chevrolet",
    "model_name": "Express 3500 Passenger",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2017,
    "manufacturer_name": "Dodge",
    "model_name": "Charger",
    "car_type": "Sedan"
  },
  {
    "year": 2017,
    "manufacturer_name": "Ferrari",
    "model_name": "GTC4Lusso",
    "car_type": "Hatchback"
  },
  {
    "year": 2017,
    "manufacturer_name": "Chevrolet",
    "model_name": "Silverado 3500 HD Double Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2017,
    "manufacturer_name": "Chevrolet",
    "model_name": "Traverse",
    "car_type": "SUV"
  },
  {
    "year": 2017,
    "manufacturer_name": "Chevrolet",
    "model_name": "Trax",
    "car_type": "SUV"
  },
  {
    "year": 2017,
    "manufacturer_name": "Chrysler",
    "model_name": "Pacifica",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2017,
    "manufacturer_name": "Chrysler",
    "model_name": "300",
    "car_type": "Sedan"
  },
  {
    "year": 2017,
    "manufacturer_name": "Chrysler",
    "model_name": "200",
    "car_type": "Sedan"
  },
  {
    "year": 2017,
    "manufacturer_name": "FIAT",
    "model_name": "500",
    "car_type": "Hatchback"
  },
  {
    "year": 2017,
    "manufacturer_name": "Dodge",
    "model_name": "Durango",
    "car_type": "SUV"
  },
  {
    "year": 2017,
    "manufacturer_name": "Chevrolet",
    "model_name": "Silverado 3500 HD Crew Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2017,
    "manufacturer_name": "Chevrolet",
    "model_name": "Suburban",
    "car_type": "SUV"
  },
  {
    "year": 2017,
    "manufacturer_name": "Chevrolet",
    "model_name": "Tahoe",
    "car_type": "SUV"
  },
  {
    "year": 2017,
    "manufacturer_name": "Chevrolet",
    "model_name": "Silverado 3500 HD Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2017,
    "manufacturer_name": "Chevrolet",
    "model_name": "SS",
    "car_type": "Sedan"
  },
  {
    "year": 2017,
    "manufacturer_name": "Chevrolet",
    "model_name": "Suburban 3500HD",
    "car_type": "SUV"
  },
  {
    "year": 2017,
    "manufacturer_name": "Ferrari",
    "model_name": "F12berlinetta",
    "car_type": "Coupe"
  },
  {
    "year": 2017,
    "manufacturer_name": "Ferrari",
    "model_name": "California",
    "car_type": "Convertible"
  },
  {
    "year": 2017,
    "manufacturer_name": "Chevrolet",
    "model_name": "Volt",
    "car_type": "Hatchback"
  },
  {
    "year": 2017,
    "manufacturer_name": "FIAT",
    "model_name": "124 Spider",
    "car_type": "Convertible"
  },
  {
    "year": 2017,
    "manufacturer_name": "FIAT",
    "model_name": "500 Abarth",
    "car_type": "Hatchback"
  },
  {
    "year": 2017,
    "manufacturer_name": "Dodge",
    "model_name": "Grand Caravan Passenger",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2017,
    "manufacturer_name": "Dodge",
    "model_name": "Challenger",
    "car_type": "Coupe"
  },
  {
    "year": 2017,
    "manufacturer_name": "Chrysler",
    "model_name": "Pacifica Hybrid",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2017,
    "manufacturer_name": "Ferrari",
    "model_name": "488 Spider",
    "car_type": "Convertible"
  },
  {
    "year": 2017,
    "manufacturer_name": "Ferrari",
    "model_name": "488 GTB",
    "car_type": "Coupe"
  },
  {
    "year": 2017,
    "manufacturer_name": "Dodge",
    "model_name": "Viper",
    "car_type": "Coupe"
  },
  {
    "year": 2017,
    "manufacturer_name": "FIAT",
    "model_name": "500c",
    "car_type": "Convertible"
  },
  {
    "year": 2017,
    "manufacturer_name": "Dodge",
    "model_name": "Journey",
    "car_type": "SUV"
  },
  {
    "year": 2017,
    "manufacturer_name": "FIAT",
    "model_name": "500e",
    "car_type": "Hatchback"
  },
  {
    "year": 2017,
    "manufacturer_name": "Ford",
    "model_name": "C-MAX Energi",
    "car_type": "Wagon"
  },
  {
    "year": 2017,
    "manufacturer_name": "Ford",
    "model_name": "Edge",
    "car_type": "SUV"
  },
  {
    "year": 2017,
    "manufacturer_name": "FIAT",
    "model_name": "500L",
    "car_type": "Hatchback"
  },
  {
    "year": 2017,
    "manufacturer_name": "Ford",
    "model_name": "Expedition",
    "car_type": "SUV"
  },
  {
    "year": 2017,
    "manufacturer_name": "FIAT",
    "model_name": "500c Abarth",
    "car_type": "Convertible"
  },
  {
    "year": 2017,
    "manufacturer_name": "FIAT",
    "model_name": "500X",
    "car_type": "SUV"
  },
  {
    "year": 2017,
    "manufacturer_name": "Ford",
    "model_name": "F150 Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2017,
    "manufacturer_name": "Ford",
    "model_name": "F150 SuperCrew Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2017,
    "manufacturer_name": "Ford",
    "model_name": "C-MAX Hybrid",
    "car_type": "Wagon"
  },
  {
    "year": 2017,
    "manufacturer_name": "Ford",
    "model_name": "Escape",
    "car_type": "SUV"
  },
  {
    "year": 2017,
    "manufacturer_name": "Ford",
    "model_name": "F350 Super Duty Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2017,
    "manufacturer_name": "Ford",
    "model_name": "Fusion Energi",
    "car_type": "Sedan"
  },
  {
    "year": 2017,
    "manufacturer_name": "Ford",
    "model_name": "F250 Super Duty Crew Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2017,
    "manufacturer_name": "Ford",
    "model_name": "Fusion",
    "car_type": "Sedan"
  },
  {
    "year": 2017,
    "manufacturer_name": "Freightliner",
    "model_name": "Sprinter 2500 Passenger",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2017,
    "manufacturer_name": "Ford",
    "model_name": "Transit 350 Wagon",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2017,
    "manufacturer_name": "Ford",
    "model_name": "F250 Super Duty Super Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2017,
    "manufacturer_name": "Ford",
    "model_name": "Transit 150 Wagon",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2017,
    "manufacturer_name": "Ford",
    "model_name": "Explorer",
    "car_type": "SUV"
  },
  {
    "year": 2017,
    "manufacturer_name": "Ford",
    "model_name": "Fiesta",
    "car_type": "Sedan, Hatchback"
  },
  {
    "year": 2017,
    "manufacturer_name": "Ford",
    "model_name": "Transit 350 HD Van",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2017,
    "manufacturer_name": "Ford",
    "model_name": "Expedition EL",
    "car_type": "SUV"
  },
  {
    "year": 2017,
    "manufacturer_name": "Ford",
    "model_name": "F350 Super Duty Super Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2017,
    "manufacturer_name": "Ford",
    "model_name": "Focus",
    "car_type": "Sedan, Hatchback"
  },
  {
    "year": 2017,
    "manufacturer_name": "Ford",
    "model_name": "Transit 150 Van",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2017,
    "manufacturer_name": "Ford",
    "model_name": "F350 Super Duty Crew Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2017,
    "manufacturer_name": "Ford",
    "model_name": "Flex",
    "car_type": "SUV"
  },
  {
    "year": 2017,
    "manufacturer_name": "Freightliner",
    "model_name": "Sprinter 2500 Cargo",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2017,
    "manufacturer_name": "Ford",
    "model_name": "F150 Super Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2017,
    "manufacturer_name": "Ford",
    "model_name": "Mustang",
    "car_type": "Convertible, Coupe"
  },
  {
    "year": 2017,
    "manufacturer_name": "Ford",
    "model_name": "Taurus",
    "car_type": "Sedan"
  },
  {
    "year": 2017,
    "manufacturer_name": "Ford",
    "model_name": "F450 Super Duty Crew Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2017,
    "manufacturer_name": "Ford",
    "model_name": "F250 Super Duty Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2017,
    "manufacturer_name": "GMC",
    "model_name": "Canyon Extended Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2017,
    "manufacturer_name": "Ford",
    "model_name": "Transit Connect Cargo",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2017,
    "manufacturer_name": "Freightliner",
    "model_name": "Sprinter 3500 Cargo",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2017,
    "manufacturer_name": "Genesis",
    "model_name": "G90",
    "car_type": "Sedan"
  },
  {
    "year": 2017,
    "manufacturer_name": "Freightliner",
    "model_name": "Sprinter 3500XD Cargo",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2017,
    "manufacturer_name": "Genesis",
    "model_name": "G80",
    "car_type": "Sedan"
  },
  {
    "year": 2017,
    "manufacturer_name": "GMC",
    "model_name": "Acadia",
    "car_type": "SUV"
  },
  {
    "year": 2017,
    "manufacturer_name": "Ford",
    "model_name": "Transit 250 Van",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2017,
    "manufacturer_name": "Ford",
    "model_name": "Transit Connect Passenger",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2017,
    "manufacturer_name": "Freightliner",
    "model_name": "Sprinter 2500 Crew",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2017,
    "manufacturer_name": "GMC",
    "model_name": "Sierra 1500 Crew Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2017,
    "manufacturer_name": "Freightliner",
    "model_name": "Sprinter WORKER Cargo",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2017,
    "manufacturer_name": "Ford",
    "model_name": "Transit 350 Van",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2017,
    "manufacturer_name": "Freightliner",
    "model_name": "Sprinter WORKER Passenger",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2017,
    "manufacturer_name": "GMC",
    "model_name": "Acadia Limited",
    "car_type": "SUV"
  },
  {
    "year": 2017,
    "manufacturer_name": "GMC",
    "model_name": "Savana 3500 Cargo",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2017,
    "manufacturer_name": "Honda",
    "model_name": "Accord",
    "car_type": "Sedan, Coupe"
  },
  {
    "year": 2017,
    "manufacturer_name": "GMC",
    "model_name": "Sierra 1500 Double Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2017,
    "manufacturer_name": "GMC",
    "model_name": "Savana 2500 Cargo",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2017,
    "manufacturer_name": "GMC",
    "model_name": "Sierra 3500 HD Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2017,
    "manufacturer_name": "GMC",
    "model_name": "Savana 3500 Passenger",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2017,
    "manufacturer_name": "GMC",
    "model_name": "Savana 2500 Passenger",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2017,
    "manufacturer_name": "Hyundai",
    "model_name": "Accent",
    "car_type": "Sedan, Hatchback"
  },
  {
    "year": 2017,
    "manufacturer_name": "GMC",
    "model_name": "Terrain",
    "car_type": "SUV"
  },
  {
    "year": 2017,
    "manufacturer_name": "GMC",
    "model_name": "Canyon Crew Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2017,
    "manufacturer_name": "Hyundai",
    "model_name": "Ioniq Hybrid",
    "car_type": "Hatchback"
  },
  {
    "year": 2017,
    "manufacturer_name": "GMC",
    "model_name": "Sierra 2500 HD Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2017,
    "manufacturer_name": "Honda",
    "model_name": "Fit",
    "car_type": "Hatchback"
  },
  {
    "year": 2017,
    "manufacturer_name": "GMC",
    "model_name": "Sierra 1500 Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2017,
    "manufacturer_name": "GMC",
    "model_name": "Yukon",
    "car_type": "SUV"
  },
  {
    "year": 2017,
    "manufacturer_name": "GMC",
    "model_name": "Sierra 3500 HD Double Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2017,
    "manufacturer_name": "Hyundai",
    "model_name": "Elantra GT",
    "car_type": "Hatchback"
  },
  {
    "year": 2017,
    "manufacturer_name": "GMC",
    "model_name": "Sierra 2500 HD Double Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2017,
    "manufacturer_name": "Honda",
    "model_name": "HR-V",
    "car_type": "SUV"
  },
  {
    "year": 2017,
    "manufacturer_name": "Honda",
    "model_name": "Odyssey",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2017,
    "manufacturer_name": "GMC",
    "model_name": "Sierra 2500 HD Crew Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2017,
    "manufacturer_name": "Hyundai",
    "model_name": "Veloster",
    "car_type": "Coupe"
  },
  {
    "year": 2017,
    "manufacturer_name": "GMC",
    "model_name": "Yukon XL",
    "car_type": "SUV"
  },
  {
    "year": 2017,
    "manufacturer_name": "Hyundai",
    "model_name": "Sonata",
    "car_type": "Sedan"
  },
  {
    "year": 2017,
    "manufacturer_name": "Honda",
    "model_name": "Pilot",
    "car_type": "SUV"
  },
  {
    "year": 2017,
    "manufacturer_name": "GMC",
    "model_name": "Sierra 3500 HD Crew Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2017,
    "manufacturer_name": "Honda",
    "model_name": "Accord Hybrid",
    "car_type": "Sedan"
  },
  {
    "year": 2017,
    "manufacturer_name": "Honda",
    "model_name": "Civic Type R",
    "car_type": "Hatchback"
  },
  {
    "year": 2017,
    "manufacturer_name": "Honda",
    "model_name": "Civic",
    "car_type": "Coupe, Sedan, Hatchback"
  },
  {
    "year": 2017,
    "manufacturer_name": "Honda",
    "model_name": "CR-V",
    "car_type": "SUV"
  },
  {
    "year": 2017,
    "manufacturer_name": "Hyundai",
    "model_name": "Elantra",
    "car_type": "Sedan"
  },
  {
    "year": 2017,
    "manufacturer_name": "Hyundai",
    "model_name": "Santa Fe Sport",
    "car_type": "SUV"
  },
  {
    "year": 2017,
    "manufacturer_name": "Hyundai",
    "model_name": "Sonata Plug-in Hybrid",
    "car_type": "Sedan"
  },
  {
    "year": 2017,
    "manufacturer_name": "Hyundai",
    "model_name": "Azera",
    "car_type": "Sedan"
  },
  {
    "year": 2017,
    "manufacturer_name": "Honda",
    "model_name": "Ridgeline",
    "car_type": "Pickup"
  },
  {
    "year": 2017,
    "manufacturer_name": "INFINITI",
    "model_name": "QX50",
    "car_type": "SUV"
  },
  {
    "year": 2017,
    "manufacturer_name": "INFINITI",
    "model_name": "QX30",
    "car_type": "SUV"
  },
  {
    "year": 2017,
    "manufacturer_name": "INFINITI",
    "model_name": "QX70",
    "car_type": "SUV"
  },
  {
    "year": 2017,
    "manufacturer_name": "Hyundai",
    "model_name": "Tucson",
    "car_type": "SUV"
  },
  {
    "year": 2017,
    "manufacturer_name": "Hyundai",
    "model_name": "Sonata Hybrid",
    "car_type": "Sedan"
  },
  {
    "year": 2017,
    "manufacturer_name": "Jaguar",
    "model_name": "F-TYPE",
    "car_type": "Coupe, Convertible"
  },
  {
    "year": 2017,
    "manufacturer_name": "Hyundai",
    "model_name": "Tucson Fuel Cell",
    "car_type": "SUV"
  },
  {
    "year": 2017,
    "manufacturer_name": "INFINITI",
    "model_name": "QX80",
    "car_type": "SUV"
  },
  {
    "year": 2017,
    "manufacturer_name": "Hyundai",
    "model_name": "Santa Fe",
    "car_type": "SUV"
  },
  {
    "year": 2017,
    "manufacturer_name": "INFINITI",
    "model_name": "Q70",
    "car_type": "Sedan"
  },
  {
    "year": 2017,
    "manufacturer_name": "INFINITI",
    "model_name": "QX60",
    "car_type": "SUV"
  },
  {
    "year": 2017,
    "manufacturer_name": "Jaguar",
    "model_name": "F-PACE",
    "car_type": "SUV"
  },
  {
    "year": 2017,
    "manufacturer_name": "INFINITI",
    "model_name": "Q50",
    "car_type": "Sedan"
  },
  {
    "year": 2017,
    "manufacturer_name": "INFINITI",
    "model_name": "Q60",
    "car_type": "Coupe"
  },
  {
    "year": 2017,
    "manufacturer_name": "Jaguar",
    "model_name": "XE",
    "car_type": "Sedan"
  },
  {
    "year": 2017,
    "manufacturer_name": "Hyundai",
    "model_name": "Ioniq Electric",
    "car_type": "Hatchback"
  },
  {
    "year": 2017,
    "manufacturer_name": "Jeep",
    "model_name": "Grand Cherokee",
    "car_type": "SUV"
  },
  {
    "year": 2017,
    "manufacturer_name": "Jeep",
    "model_name": "Cherokee",
    "car_type": "SUV"
  },
  {
    "year": 2017,
    "manufacturer_name": "Jaguar",
    "model_name": "XF",
    "car_type": "Sedan"
  },
  {
    "year": 2017,
    "manufacturer_name": "Jeep",
    "model_name": "Wrangler",
    "car_type": "SUV"
  },
  {
    "year": 2017,
    "manufacturer_name": "Jaguar",
    "model_name": "XJ",
    "car_type": "Sedan"
  },
  {
    "year": 2017,
    "manufacturer_name": "Jeep",
    "model_name": "Renegade",
    "car_type": "SUV"
  },
  {
    "year": 2017,
    "manufacturer_name": "Jeep",
    "model_name": "Wrangler Unlimited",
    "car_type": "SUV"
  },
  {
    "year": 2017,
    "manufacturer_name": "Kia",
    "model_name": "Rio",
    "car_type": "Sedan, Hatchback"
  },
  {
    "year": 2017,
    "manufacturer_name": "Kia",
    "model_name": "K900",
    "car_type": "Sedan"
  },
  {
    "year": 2017,
    "manufacturer_name": "Kia",
    "model_name": "Optima",
    "car_type": "Sedan"
  },
  {
    "year": 2017,
    "manufacturer_name": "Kia",
    "model_name": "Cadenza",
    "car_type": "Sedan"
  },
  {
    "year": 2017,
    "manufacturer_name": "Jeep",
    "model_name": "Compass",
    "car_type": "SUV"
  },
  {
    "year": 2017,
    "manufacturer_name": "Kia",
    "model_name": "Niro",
    "car_type": "Wagon"
  },
  {
    "year": 2017,
    "manufacturer_name": "Kia",
    "model_name": "Sedona",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2017,
    "manufacturer_name": "Kia",
    "model_name": "Forte",
    "car_type": "Sedan"
  },
  {
    "year": 2017,
    "manufacturer_name": "Kia",
    "model_name": "Forte5",
    "car_type": "Hatchback"
  },
  {
    "year": 2017,
    "manufacturer_name": "Jeep",
    "model_name": "Patriot",
    "car_type": "SUV"
  },
  {
    "year": 2017,
    "manufacturer_name": "Kia",
    "model_name": "Optima Hybrid",
    "car_type": "Sedan"
  },
  {
    "year": 2017,
    "manufacturer_name": "Land Rover",
    "model_name": "Discovery",
    "car_type": "SUV"
  },
  {
    "year": 2017,
    "manufacturer_name": "Land Rover",
    "model_name": "Range Rover",
    "car_type": "SUV"
  },
  {
    "year": 2017,
    "manufacturer_name": "Kia",
    "model_name": "Soul",
    "car_type": "Wagon"
  },
  {
    "year": 2017,
    "manufacturer_name": "Kia",
    "model_name": "Sorento",
    "car_type": "SUV"
  },
  {
    "year": 2017,
    "manufacturer_name": "Land Rover",
    "model_name": "Range Rover Sport",
    "car_type": "SUV"
  },
  {
    "year": 2017,
    "manufacturer_name": "Lexus",
    "model_name": "LS",
    "car_type": "Sedan"
  },
  {
    "year": 2017,
    "manufacturer_name": "Lamborghini",
    "model_name": "Aventador",
    "car_type": "Coupe, Convertible"
  },
  {
    "year": 2017,
    "manufacturer_name": "Lamborghini",
    "model_name": "Huracan",
    "car_type": "Coupe, Convertible"
  },
  {
    "year": 2017,
    "manufacturer_name": "Kia",
    "model_name": "Soul EV",
    "car_type": "Wagon"
  },
  {
    "year": 2017,
    "manufacturer_name": "Kia",
    "model_name": "Optima Plug-in Hybrid",
    "car_type": "Sedan"
  },
  {
    "year": 2017,
    "manufacturer_name": "Land Rover",
    "model_name": "Discovery Sport",
    "car_type": "SUV"
  },
  {
    "year": 2017,
    "manufacturer_name": "Kia",
    "model_name": "Sportage",
    "car_type": "SUV"
  },
  {
    "year": 2017,
    "manufacturer_name": "Lexus",
    "model_name": "GX",
    "car_type": "SUV"
  },
  {
    "year": 2017,
    "manufacturer_name": "Lexus",
    "model_name": "IS",
    "car_type": "Sedan"
  },
  {
    "year": 2017,
    "manufacturer_name": "Lexus",
    "model_name": "CT",
    "car_type": "Hatchback"
  },
  {
    "year": 2017,
    "manufacturer_name": "Lexus",
    "model_name": "GS",
    "car_type": "Sedan"
  },
  {
    "year": 2017,
    "manufacturer_name": "Land Rover",
    "model_name": "Range Rover Evoque",
    "car_type": "SUV"
  },
  {
    "year": 2017,
    "manufacturer_name": "Lexus",
    "model_name": "LX",
    "car_type": "SUV"
  },
  {
    "year": 2017,
    "manufacturer_name": "MAZDA",
    "model_name": "CX-3",
    "car_type": "SUV"
  },
  {
    "year": 2017,
    "manufacturer_name": "Lincoln",
    "model_name": "Navigator",
    "car_type": "SUV"
  },
  {
    "year": 2017,
    "manufacturer_name": "Mercedes-Benz",
    "model_name": "C-Class",
    "car_type": "Coupe, Sedan, Convertible"
  },
  {
    "year": 2017,
    "manufacturer_name": "Mercedes-Benz",
    "model_name": "Mercedes-AMG C-Class",
    "car_type": "Convertible, Sedan, Coupe"
  },
  {
    "year": 2017,
    "manufacturer_name": "MAZDA",
    "model_name": "MX-5 Miata RF",
    "car_type": "Convertible"
  },
  {
    "year": 2017,
    "manufacturer_name": "MAZDA",
    "model_name": "MAZDA6",
    "car_type": "Sedan"
  },
  {
    "year": 2017,
    "manufacturer_name": "Lexus",
    "model_name": "RC",
    "car_type": "Coupe"
  },
  {
    "year": 2017,
    "manufacturer_name": "Lexus",
    "model_name": "RX",
    "car_type": "SUV"
  },
  {
    "year": 2017,
    "manufacturer_name": "Lincoln",
    "model_name": "Continental",
    "car_type": "Sedan"
  },
  {
    "year": 2017,
    "manufacturer_name": "Lincoln",
    "model_name": "MKX",
    "car_type": "SUV"
  },
  {
    "year": 2017,
    "manufacturer_name": "Maserati",
    "model_name": "Ghibli",
    "car_type": "Sedan"
  },
  {
    "year": 2017,
    "manufacturer_name": "Lincoln",
    "model_name": "Navigator L",
    "car_type": "SUV"
  },
  {
    "year": 2017,
    "manufacturer_name": "McLaren",
    "model_name": "570S",
    "car_type": "Coupe"
  },
  {
    "year": 2017,
    "manufacturer_name": "MAZDA",
    "model_name": "MX-5 Miata",
    "car_type": "Convertible"
  },
  {
    "year": 2017,
    "manufacturer_name": "Lincoln",
    "model_name": "MKT",
    "car_type": "SUV"
  },
  {
    "year": 2017,
    "manufacturer_name": "Maserati",
    "model_name": "Levante",
    "car_type": "SUV"
  },
  {
    "year": 2017,
    "manufacturer_name": "Mercedes-Benz",
    "model_name": "E-Class",
    "car_type": "Convertible, Sedan, Coupe, Wagon"
  },
  {
    "year": 2017,
    "manufacturer_name": "Lincoln",
    "model_name": "MKC",
    "car_type": "SUV"
  },
  {
    "year": 2017,
    "manufacturer_name": "Lincoln",
    "model_name": "MKZ",
    "car_type": "Sedan"
  },
  {
    "year": 2017,
    "manufacturer_name": "Lexus",
    "model_name": "ES",
    "car_type": "Sedan"
  },
  {
    "year": 2017,
    "manufacturer_name": "Maserati",
    "model_name": "GranTurismo",
    "car_type": "Coupe, Convertible"
  },
  {
    "year": 2017,
    "manufacturer_name": "Mercedes-Benz",
    "model_name": "GLC Coupe",
    "car_type": "SUV"
  },
  {
    "year": 2017,
    "manufacturer_name": "MAZDA",
    "model_name": "CX-5",
    "car_type": "SUV"
  },
  {
    "year": 2017,
    "manufacturer_name": "Mercedes-Benz",
    "model_name": "GLE",
    "car_type": "SUV"
  },
  {
    "year": 2017,
    "manufacturer_name": "Mercedes-Benz",
    "model_name": "GLC",
    "car_type": "SUV"
  },
  {
    "year": 2017,
    "manufacturer_name": "Lexus",
    "model_name": "NX",
    "car_type": "SUV"
  },
  {
    "year": 2017,
    "manufacturer_name": "Lotus",
    "model_name": "Evora 400",
    "car_type": "Coupe"
  },
  {
    "year": 2017,
    "manufacturer_name": "MAZDA",
    "model_name": "MAZDA3",
    "car_type": "Hatchback, Sedan"
  },
  {
    "year": 2017,
    "manufacturer_name": "McLaren",
    "model_name": "570GT",
    "car_type": "Coupe"
  },
  {
    "year": 2017,
    "manufacturer_name": "MAZDA",
    "model_name": "CX-9",
    "car_type": "SUV"
  },
  {
    "year": 2017,
    "manufacturer_name": "Maserati",
    "model_name": "Quattroporte",
    "car_type": "Sedan"
  },
  {
    "year": 2017,
    "manufacturer_name": "Mercedes-Benz",
    "model_name": "CLS",
    "car_type": "Sedan"
  },
  {
    "year": 2017,
    "manufacturer_name": "Mercedes-Benz",
    "model_name": "CLA",
    "car_type": "Sedan"
  },
  {
    "year": 2017,
    "manufacturer_name": "Mercedes-Benz",
    "model_name": "B-Class",
    "car_type": "Hatchback"
  },
  {
    "year": 2017,
    "manufacturer_name": "Mercedes-Benz",
    "model_name": "Mercedes-AMG E-Class",
    "car_type": "Sedan"
  },
  {
    "year": 2017,
    "manufacturer_name": "Mercedes-Benz",
    "model_name": "G-Class",
    "car_type": "SUV"
  },
  {
    "year": 2017,
    "manufacturer_name": "Mercedes-Benz",
    "model_name": "GLA",
    "car_type": "SUV"
  },
  {
    "year": 2017,
    "manufacturer_name": "Mercedes-Benz",
    "model_name": "Mercedes-AMG CLS",
    "car_type": "Sedan"
  },
  {
    "year": 2017,
    "manufacturer_name": "Mercedes-Benz",
    "model_name": "Mercedes-AMG CLA",
    "car_type": "Sedan"
  },
  {
    "year": 2017,
    "manufacturer_name": "Mercedes-Benz",
    "model_name": "Mercedes-AMG GLS",
    "car_type": "SUV"
  },
  {
    "year": 2017,
    "manufacturer_name": "Mercedes-Benz",
    "model_name": "Mercedes-AMG SL",
    "car_type": "Convertible"
  },
  {
    "year": 2017,
    "manufacturer_name": "Mercedes-Benz",
    "model_name": "Mercedes-AMG GLC",
    "car_type": "SUV"
  },
  {
    "year": 2017,
    "manufacturer_name": "Mercedes-Benz",
    "model_name": "Mercedes-AMG GLE Coupe",
    "car_type": "SUV"
  },
  {
    "year": 2017,
    "manufacturer_name": "Mercedes-Benz",
    "model_name": "Mercedes-AMG GLA",
    "car_type": "SUV"
  },
  {
    "year": 2017,
    "manufacturer_name": "Mercedes-Benz",
    "model_name": "SL",
    "car_type": "Convertible"
  },
  {
    "year": 2017,
    "manufacturer_name": "Mercedes-Benz",
    "model_name": "Sprinter 2500 Cargo",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2017,
    "manufacturer_name": "Mercedes-Benz",
    "model_name": "Metris Cargo",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2017,
    "manufacturer_name": "Mercedes-Benz",
    "model_name": "GLS",
    "car_type": "SUV"
  },
  {
    "year": 2017,
    "manufacturer_name": "Mercedes-Benz",
    "model_name": "Mercedes-Maybach S-Class",
    "car_type": "Sedan"
  },
  {
    "year": 2017,
    "manufacturer_name": "Mercedes-Benz",
    "model_name": "Mercedes-AMG G-Class",
    "car_type": "SUV"
  },
  {
    "year": 2017,
    "manufacturer_name": "Mercedes-Benz",
    "model_name": "Sprinter 3500 XD Cargo",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2017,
    "manufacturer_name": "Mercedes-Benz",
    "model_name": "Sprinter 2500 Passenger",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2017,
    "manufacturer_name": "Mercedes-Benz",
    "model_name": "Metris WORKER Passenger",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2017,
    "manufacturer_name": "Mercedes-Benz",
    "model_name": "Mercedes-AMG GLE",
    "car_type": "SUV"
  },
  {
    "year": 2017,
    "manufacturer_name": "Mercedes-Benz",
    "model_name": "Mercedes-AMG GLC Coupe",
    "car_type": "SUV"
  },
  {
    "year": 2017,
    "manufacturer_name": "Mercedes-Benz",
    "model_name": "Mercedes-AMG S-Class",
    "car_type": "Sedan, Coupe, Convertible"
  },
  {
    "year": 2017,
    "manufacturer_name": "Mercedes-Benz",
    "model_name": "Mercedes-AMG GT",
    "car_type": "Coupe"
  },
  {
    "year": 2017,
    "manufacturer_name": "Mercedes-Benz",
    "model_name": "Sprinter 3500 Cargo",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2017,
    "manufacturer_name": "Mercedes-Benz",
    "model_name": "S-Class",
    "car_type": "Sedan, Convertible, Coupe"
  },
  {
    "year": 2017,
    "manufacturer_name": "Mercedes-Benz",
    "model_name": "Metris WORKER Cargo",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2017,
    "manufacturer_name": "Mercedes-Benz",
    "model_name": "SLC",
    "car_type": "Convertible"
  },
  {
    "year": 2017,
    "manufacturer_name": "Mercedes-Benz",
    "model_name": "Mercedes-AMG SLC",
    "car_type": "Convertible"
  },
  {
    "year": 2017,
    "manufacturer_name": "Mercedes-Benz",
    "model_name": "Metris Passenger",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2017,
    "manufacturer_name": "Mercedes-Benz",
    "model_name": "Sprinter 2500 Crew",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2017,
    "manufacturer_name": "MINI",
    "model_name": "Clubman",
    "car_type": "Hatchback"
  },
  {
    "year": 2017,
    "manufacturer_name": "MINI",
    "model_name": "Convertible",
    "car_type": "Convertible"
  },
  {
    "year": 2017,
    "manufacturer_name": "Mercedes-Benz",
    "model_name": "Sprinter WORKER Cargo",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2017,
    "manufacturer_name": "Mercedes-Benz",
    "model_name": "Sprinter WORKER Passenger",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2017,
    "manufacturer_name": "Mitsubishi",
    "model_name": "Mirage",
    "car_type": "Hatchback"
  },
  {
    "year": 2017,
    "manufacturer_name": "MINI",
    "model_name": "Hardtop 2 Door",
    "car_type": "Hatchback"
  },
  {
    "year": 2017,
    "manufacturer_name": "Nissan",
    "model_name": "370Z",
    "car_type": "Coupe, Convertible"
  },
  {
    "year": 2017,
    "manufacturer_name": "Mitsubishi",
    "model_name": "Lancer",
    "car_type": "Sedan"
  },
  {
    "year": 2017,
    "manufacturer_name": "MINI",
    "model_name": "Hardtop 4 Door",
    "car_type": "Hatchback"
  },
  {
    "year": 2017,
    "manufacturer_name": "Nissan",
    "model_name": "Altima",
    "car_type": "Sedan"
  },
  {
    "year": 2017,
    "manufacturer_name": "Mitsubishi",
    "model_name": "i-MiEV",
    "car_type": "Hatchback"
  },
  {
    "year": 2017,
    "manufacturer_name": "MINI",
    "model_name": "Countryman",
    "car_type": "SUV"
  },
  {
    "year": 2017,
    "manufacturer_name": "Nissan",
    "model_name": "Quest",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2017,
    "manufacturer_name": "Mitsubishi",
    "model_name": "Outlander Sport",
    "car_type": "SUV"
  },
  {
    "year": 2017,
    "manufacturer_name": "Nissan",
    "model_name": "Frontier King Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2017,
    "manufacturer_name": "Nissan",
    "model_name": "Titan King Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2017,
    "manufacturer_name": "Nissan",
    "model_name": "Maxima",
    "car_type": "Sedan"
  },
  {
    "year": 2017,
    "manufacturer_name": "Nissan",
    "model_name": "Armada",
    "car_type": "SUV"
  },
  {
    "year": 2017,
    "manufacturer_name": "Nissan",
    "model_name": "GT-R",
    "car_type": "Coupe"
  },
  {
    "year": 2017,
    "manufacturer_name": "Nissan",
    "model_name": "Murano",
    "car_type": "SUV"
  },
  {
    "year": 2017,
    "manufacturer_name": "Nissan",
    "model_name": "NV200",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2017,
    "manufacturer_name": "Mitsubishi",
    "model_name": "Outlander",
    "car_type": "SUV"
  },
  {
    "year": 2017,
    "manufacturer_name": "Nissan",
    "model_name": "NV2500 HD Cargo",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2017,
    "manufacturer_name": "Mitsubishi",
    "model_name": "Mirage G4",
    "car_type": "Sedan"
  },
  {
    "year": 2017,
    "manufacturer_name": "Nissan",
    "model_name": "NV3500 HD Passenger",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2017,
    "manufacturer_name": "Nissan",
    "model_name": "Rogue Sport",
    "car_type": "SUV"
  },
  {
    "year": 2017,
    "manufacturer_name": "Nissan",
    "model_name": "NV1500 Cargo",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2017,
    "manufacturer_name": "Nissan",
    "model_name": "Pathfinder",
    "car_type": "SUV"
  },
  {
    "year": 2017,
    "manufacturer_name": "Nissan",
    "model_name": "Titan Crew Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2017,
    "manufacturer_name": "Nissan",
    "model_name": "JUKE",
    "car_type": "SUV"
  },
  {
    "year": 2017,
    "manufacturer_name": "Nissan",
    "model_name": "NV3500 HD Cargo",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2017,
    "manufacturer_name": "Nissan",
    "model_name": "Frontier Crew Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2017,
    "manufacturer_name": "Nissan",
    "model_name": "LEAF",
    "car_type": "Hatchback"
  },
  {
    "year": 2017,
    "manufacturer_name": "Nissan",
    "model_name": "TITAN XD Single Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2017,
    "manufacturer_name": "Ram",
    "model_name": "1500 Crew Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2017,
    "manufacturer_name": "Ram",
    "model_name": "3500 Crew Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2017,
    "manufacturer_name": "Ram",
    "model_name": "1500 Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2017,
    "manufacturer_name": "Nissan",
    "model_name": "Sentra",
    "car_type": "Sedan"
  },
  {
    "year": 2017,
    "manufacturer_name": "Nissan",
    "model_name": "TITAN XD King Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2017,
    "manufacturer_name": "Nissan",
    "model_name": "Versa",
    "car_type": "Sedan"
  },
  {
    "year": 2017,
    "manufacturer_name": "Nissan",
    "model_name": "Rogue",
    "car_type": "SUV"
  },
  {
    "year": 2017,
    "manufacturer_name": "Ram",
    "model_name": "2500 Mega Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2017,
    "manufacturer_name": "Porsche",
    "model_name": "911",
    "car_type": "Coupe, Convertible"
  },
  {
    "year": 2017,
    "manufacturer_name": "Porsche",
    "model_name": "Panamera",
    "car_type": "Sedan"
  },
  {
    "year": 2017,
    "manufacturer_name": "Nissan",
    "model_name": "Versa Note",
    "car_type": "Hatchback"
  },
  {
    "year": 2017,
    "manufacturer_name": "Porsche",
    "model_name": "Cayenne",
    "car_type": "SUV"
  },
  {
    "year": 2017,
    "manufacturer_name": "Nissan",
    "model_name": "TITAN XD Crew Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2017,
    "manufacturer_name": "Porsche",
    "model_name": "718 Boxster",
    "car_type": "Convertible"
  },
  {
    "year": 2017,
    "manufacturer_name": "Ram",
    "model_name": "1500 Quad Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2017,
    "manufacturer_name": "Porsche",
    "model_name": "Macan",
    "car_type": "SUV"
  },
  {
    "year": 2017,
    "manufacturer_name": "Nissan",
    "model_name": "TITAN Single Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2017,
    "manufacturer_name": "Porsche",
    "model_name": "718 Cayman",
    "car_type": "Coupe"
  },
  {
    "year": 2017,
    "manufacturer_name": "Ram",
    "model_name": "ProMaster Window Van",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2017,
    "manufacturer_name": "Ram",
    "model_name": "3500 Mega Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2017,
    "manufacturer_name": "Ram",
    "model_name": "ProMaster Cargo Van",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2017,
    "manufacturer_name": "Subaru",
    "model_name": "Forester",
    "car_type": "SUV"
  },
  {
    "year": 2017,
    "manufacturer_name": "Toyota",
    "model_name": "Camry",
    "car_type": "Sedan"
  },
  {
    "year": 2017,
    "manufacturer_name": "smart",
    "model_name": "fortwo cabrio",
    "car_type": "Convertible"
  },
  {
    "year": 2017,
    "manufacturer_name": "smart",
    "model_name": "fortwo",
    "car_type": "Hatchback"
  },
  {
    "year": 2017,
    "manufacturer_name": "Toyota",
    "model_name": "Avalon Hybrid",
    "car_type": "Sedan"
  },
  {
    "year": 2017,
    "manufacturer_name": "smart",
    "model_name": "fortwo electric drive",
    "car_type": "Hatchback"
  },
  {
    "year": 2017,
    "manufacturer_name": "Ram",
    "model_name": "2500 Crew Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2017,
    "manufacturer_name": "Ram",
    "model_name": "2500 Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2017,
    "manufacturer_name": "Rolls-Royce",
    "model_name": "Ghost",
    "car_type": "Sedan"
  },
  {
    "year": 2017,
    "manufacturer_name": "Rolls-Royce",
    "model_name": "Dawn",
    "car_type": "Convertible"
  },
  {
    "year": 2017,
    "manufacturer_name": "Tesla",
    "model_name": "Model X",
    "car_type": "SUV"
  },
  {
    "year": 2017,
    "manufacturer_name": "Subaru",
    "model_name": "Outback",
    "car_type": "SUV"
  },
  {
    "year": 2017,
    "manufacturer_name": "Subaru",
    "model_name": "Impreza",
    "car_type": "Wagon, Sedan"
  },
  {
    "year": 2017,
    "manufacturer_name": "Ram",
    "model_name": "ProMaster City",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2017,
    "manufacturer_name": "smart",
    "model_name": "fortwo electric drive cabrio",
    "car_type": "Convertible"
  },
  {
    "year": 2017,
    "manufacturer_name": "Rolls-Royce",
    "model_name": "Wraith",
    "car_type": "Coupe"
  },
  {
    "year": 2017,
    "manufacturer_name": "Ram",
    "model_name": "3500 Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2017,
    "manufacturer_name": "Subaru",
    "model_name": "BRZ",
    "car_type": "Coupe"
  },
  {
    "year": 2017,
    "manufacturer_name": "Tesla",
    "model_name": "Model S",
    "car_type": "Sedan"
  },
  {
    "year": 2017,
    "manufacturer_name": "Toyota",
    "model_name": "Highlander",
    "car_type": "SUV"
  },
  {
    "year": 2017,
    "manufacturer_name": "Toyota",
    "model_name": "Corolla",
    "car_type": "Sedan"
  },
  {
    "year": 2017,
    "manufacturer_name": "Toyota",
    "model_name": "Prius c",
    "car_type": "Hatchback"
  },
  {
    "year": 2017,
    "manufacturer_name": "Subaru",
    "model_name": "Crosstrek",
    "car_type": "SUV"
  },
  {
    "year": 2017,
    "manufacturer_name": "Subaru",
    "model_name": "Legacy",
    "car_type": "Sedan"
  },
  {
    "year": 2017,
    "manufacturer_name": "Toyota",
    "model_name": "86",
    "car_type": "Coupe"
  },
  {
    "year": 2017,
    "manufacturer_name": "Toyota",
    "model_name": "Avalon",
    "car_type": "Sedan"
  },
  {
    "year": 2017,
    "manufacturer_name": "Toyota",
    "model_name": "Mirai",
    "car_type": "Sedan"
  },
  {
    "year": 2017,
    "manufacturer_name": "Toyota",
    "model_name": "Prius",
    "car_type": "Hatchback"
  },
  {
    "year": 2017,
    "manufacturer_name": "Toyota",
    "model_name": "Prius Prime",
    "car_type": "Hatchback"
  },
  {
    "year": 2017,
    "manufacturer_name": "Toyota",
    "model_name": "Sienna",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2017,
    "manufacturer_name": "Toyota",
    "model_name": "Prius v",
    "car_type": "Wagon"
  },
  {
    "year": 2017,
    "manufacturer_name": "Subaru",
    "model_name": "WRX",
    "car_type": "Sedan"
  },
  {
    "year": 2017,
    "manufacturer_name": "Toyota",
    "model_name": "Tundra Double Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2017,
    "manufacturer_name": "Toyota",
    "model_name": "4Runner",
    "car_type": "SUV"
  },
  {
    "year": 2017,
    "manufacturer_name": "Toyota",
    "model_name": "Highlander Hybrid",
    "car_type": "SUV"
  },
  {
    "year": 2017,
    "manufacturer_name": "Toyota",
    "model_name": "Corolla iM",
    "car_type": "Hatchback"
  },
  {
    "year": 2017,
    "manufacturer_name": "Toyota",
    "model_name": "RAV4",
    "car_type": "SUV"
  },
  {
    "year": 2017,
    "manufacturer_name": "Toyota",
    "model_name": "Camry Hybrid",
    "car_type": "Sedan"
  },
  {
    "year": 2017,
    "manufacturer_name": "Toyota",
    "model_name": "Sequoia",
    "car_type": "SUV"
  },
  {
    "year": 2017,
    "manufacturer_name": "Toyota",
    "model_name": "Tacoma Double Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2017,
    "manufacturer_name": "Toyota",
    "model_name": "Land Cruiser",
    "car_type": "SUV"
  },
  {
    "year": 2017,
    "manufacturer_name": "Toyota",
    "model_name": "Tacoma Access Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2017,
    "manufacturer_name": "Toyota",
    "model_name": "Tundra CrewMax",
    "car_type": "Pickup"
  },
  {
    "year": 2017,
    "manufacturer_name": "Toyota",
    "model_name": "RAV4 Hybrid",
    "car_type": "SUV"
  },
  {
    "year": 2017,
    "manufacturer_name": "Toyota",
    "model_name": "Tundra Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2017,
    "manufacturer_name": "Toyota",
    "model_name": "Yaris iA",
    "car_type": "Sedan"
  },
  {
    "year": 2017,
    "manufacturer_name": "Toyota",
    "model_name": "Yaris",
    "car_type": "Hatchback"
  },
  {
    "year": 2017,
    "manufacturer_name": "Volkswagen",
    "model_name": "CC",
    "car_type": "Sedan"
  },
  {
    "year": 2017,
    "manufacturer_name": "Volkswagen",
    "model_name": "Beetle",
    "car_type": "Hatchback, Convertible"
  },
  {
    "year": 2017,
    "manufacturer_name": "Volkswagen",
    "model_name": "Touareg",
    "car_type": "SUV"
  },
  {
    "year": 2017,
    "manufacturer_name": "Volkswagen",
    "model_name": "e-Golf",
    "car_type": "Hatchback"
  },
  {
    "year": 2017,
    "manufacturer_name": "Volvo",
    "model_name": "S60",
    "car_type": "Sedan"
  },
  {
    "year": 2017,
    "manufacturer_name": "Volkswagen",
    "model_name": "Golf Alltrack",
    "car_type": "Wagon"
  },
  {
    "year": 2017,
    "manufacturer_name": "Volkswagen",
    "model_name": "Jetta",
    "car_type": "Sedan"
  },
  {
    "year": 2017,
    "manufacturer_name": "Volkswagen",
    "model_name": "Golf SportWagen",
    "car_type": "Wagon"
  },
  {
    "year": 2017,
    "manufacturer_name": "Volkswagen",
    "model_name": "Golf",
    "car_type": "Hatchback"
  },
  {
    "year": 2017,
    "manufacturer_name": "Volvo",
    "model_name": "V90",
    "car_type": "Wagon"
  },
  {
    "year": 2017,
    "manufacturer_name": "Volkswagen",
    "model_name": "Golf R",
    "car_type": "Hatchback"
  },
  {
    "year": 2017,
    "manufacturer_name": "Volkswagen",
    "model_name": "Golf GTI",
    "car_type": "Hatchback"
  },
  {
    "year": 2017,
    "manufacturer_name": "Volkswagen",
    "model_name": "Tiguan Limited",
    "car_type": "SUV"
  },
  {
    "year": 2017,
    "manufacturer_name": "Volkswagen",
    "model_name": "Passat",
    "car_type": "Sedan"
  },
  {
    "year": 2017,
    "manufacturer_name": "Volkswagen",
    "model_name": "Tiguan",
    "car_type": "SUV"
  },
  {
    "year": 2017,
    "manufacturer_name": "Volvo",
    "model_name": "XC90",
    "car_type": "SUV"
  },
  {
    "year": 2016,
    "manufacturer_name": "Audi",
    "model_name": "A3",
    "car_type": "Sedan, Convertible"
  },
  {
    "year": 2017,
    "manufacturer_name": "Volvo",
    "model_name": "S90",
    "car_type": "Sedan"
  },
  {
    "year": 2016,
    "manufacturer_name": "Aston Martin",
    "model_name": "DB9 GT",
    "car_type": "Coupe, Convertible"
  },
  {
    "year": 2016,
    "manufacturer_name": "Acura",
    "model_name": "RLX",
    "car_type": "Sedan"
  },
  {
    "year": 2017,
    "manufacturer_name": "Volvo",
    "model_name": "XC60",
    "car_type": "SUV"
  },
  {
    "year": 2016,
    "manufacturer_name": "Aston Martin",
    "model_name": "Rapide S",
    "car_type": "Sedan"
  },
  {
    "year": 2016,
    "manufacturer_name": "Acura",
    "model_name": "TLX",
    "car_type": "Sedan"
  },
  {
    "year": 2016,
    "manufacturer_name": "Aston Martin",
    "model_name": "Vanquish",
    "car_type": "Coupe, Convertible"
  },
  {
    "year": 2016,
    "manufacturer_name": "Acura",
    "model_name": "RLX Sport Hybrid",
    "car_type": "Sedan"
  },
  {
    "year": 2016,
    "manufacturer_name": "Acura",
    "model_name": "ILX",
    "car_type": "Sedan"
  },
  {
    "year": 2016,
    "manufacturer_name": "Audi",
    "model_name": "A7",
    "car_type": "Sedan"
  },
  {
    "year": 2017,
    "manufacturer_name": "Volvo",
    "model_name": "V60",
    "car_type": "Wagon"
  },
  {
    "year": 2016,
    "manufacturer_name": "Acura",
    "model_name": "MDX",
    "car_type": "SUV"
  },
  {
    "year": 2016,
    "manufacturer_name": "Audi",
    "model_name": "A3 Sportback e-tron",
    "car_type": "Wagon"
  },
  {
    "year": 2016,
    "manufacturer_name": "Acura",
    "model_name": "RDX",
    "car_type": "SUV"
  },
  {
    "year": 2016,
    "manufacturer_name": "Aston Martin",
    "model_name": "Vantage",
    "car_type": "Coupe, Convertible"
  },
  {
    "year": 2016,
    "manufacturer_name": "Alfa Romeo",
    "model_name": "4C Spider",
    "car_type": "Convertible"
  },
  {
    "year": 2016,
    "manufacturer_name": "Alfa Romeo",
    "model_name": "4C",
    "car_type": "Coupe"
  },
  {
    "year": 2016,
    "manufacturer_name": "Audi",
    "model_name": "A5",
    "car_type": "Coupe, Convertible"
  },
  {
    "year": 2016,
    "manufacturer_name": "Audi",
    "model_name": "S4",
    "car_type": "Sedan"
  },
  {
    "year": 2016,
    "manufacturer_name": "Audi",
    "model_name": "allroad",
    "car_type": "Wagon"
  },
  {
    "year": 2016,
    "manufacturer_name": "Audi",
    "model_name": "SQ5",
    "car_type": "SUV"
  },
  {
    "year": 2016,
    "manufacturer_name": "Audi",
    "model_name": "S5",
    "car_type": "Coupe, Convertible"
  },
  {
    "year": 2016,
    "manufacturer_name": "Audi",
    "model_name": "S3",
    "car_type": "Sedan"
  },
  {
    "year": 2016,
    "manufacturer_name": "Audi",
    "model_name": "Q5",
    "car_type": "SUV"
  },
  {
    "year": 2016,
    "manufacturer_name": "Audi",
    "model_name": "RS 7",
    "car_type": "Sedan"
  },
  {
    "year": 2016,
    "manufacturer_name": "Audi",
    "model_name": "A4",
    "car_type": "Sedan"
  },
  {
    "year": 2016,
    "manufacturer_name": "Bentley",
    "model_name": "Continental",
    "car_type": "Convertible, Coupe"
  },
  {
    "year": 2016,
    "manufacturer_name": "Bentley",
    "model_name": "Flying Spur",
    "car_type": "Sedan"
  },
  {
    "year": 2016,
    "manufacturer_name": "Audi",
    "model_name": "A6",
    "car_type": "Sedan"
  },
  {
    "year": 2016,
    "manufacturer_name": "Audi",
    "model_name": "TT",
    "car_type": "Coupe, Convertible"
  },
  {
    "year": 2016,
    "manufacturer_name": "Audi",
    "model_name": "A8",
    "car_type": "Sedan"
  },
  {
    "year": 2016,
    "manufacturer_name": "Audi",
    "model_name": "S7",
    "car_type": "Sedan"
  },
  {
    "year": 2016,
    "manufacturer_name": "BMW",
    "model_name": "5 Series",
    "car_type": "Sedan"
  },
  {
    "year": 2016,
    "manufacturer_name": "Audi",
    "model_name": "Q3",
    "car_type": "SUV"
  },
  {
    "year": 2016,
    "manufacturer_name": "Audi",
    "model_name": "S8",
    "car_type": "Sedan"
  },
  {
    "year": 2016,
    "manufacturer_name": "Audi",
    "model_name": "S6",
    "car_type": "Sedan"
  },
  {
    "year": 2016,
    "manufacturer_name": "Bentley",
    "model_name": "Mulsanne",
    "car_type": "Sedan"
  },
  {
    "year": 2016,
    "manufacturer_name": "BMW",
    "model_name": "3 Series",
    "car_type": "Sedan, Wagon"
  },
  {
    "year": 2016,
    "manufacturer_name": "BMW",
    "model_name": "M5",
    "car_type": "Sedan"
  },
  {
    "year": 2016,
    "manufacturer_name": "Buick",
    "model_name": "Encore",
    "car_type": "SUV"
  },
  {
    "year": 2016,
    "manufacturer_name": "BMW",
    "model_name": "i3",
    "car_type": "Hatchback"
  },
  {
    "year": 2016,
    "manufacturer_name": "BMW",
    "model_name": "7 Series",
    "car_type": "Sedan"
  },
  {
    "year": 2016,
    "manufacturer_name": "BMW",
    "model_name": "4 Series",
    "car_type": "Coupe, Convertible"
  },
  {
    "year": 2016,
    "manufacturer_name": "BMW",
    "model_name": "M2",
    "car_type": "Coupe"
  },
  {
    "year": 2016,
    "manufacturer_name": "BMW",
    "model_name": "2 Series",
    "car_type": "Convertible, Coupe"
  },
  {
    "year": 2016,
    "manufacturer_name": "Buick",
    "model_name": "Regal",
    "car_type": "Sedan"
  },
  {
    "year": 2016,
    "manufacturer_name": "BMW",
    "model_name": "X3",
    "car_type": "SUV"
  },
  {
    "year": 2016,
    "manufacturer_name": "BMW",
    "model_name": "6 Series",
    "car_type": "Coupe, Sedan, Convertible"
  },
  {
    "year": 2016,
    "manufacturer_name": "BMW",
    "model_name": "Z4",
    "car_type": "Convertible"
  },
  {
    "year": 2016,
    "manufacturer_name": "BMW",
    "model_name": "X4",
    "car_type": "SUV"
  },
  {
    "year": 2016,
    "manufacturer_name": "BMW",
    "model_name": "X5 M",
    "car_type": "SUV"
  },
  {
    "year": 2016,
    "manufacturer_name": "BMW",
    "model_name": "M4",
    "car_type": "Coupe, Convertible"
  },
  {
    "year": 2016,
    "manufacturer_name": "Buick",
    "model_name": "Cascada",
    "car_type": "Convertible"
  },
  {
    "year": 2016,
    "manufacturer_name": "Buick",
    "model_name": "Verano",
    "car_type": "Sedan"
  },
  {
    "year": 2016,
    "manufacturer_name": "Cadillac",
    "model_name": "ATS",
    "car_type": "Coupe, Sedan"
  },
  {
    "year": 2016,
    "manufacturer_name": "BMW",
    "model_name": "X5",
    "car_type": "SUV"
  },
  {
    "year": 2016,
    "manufacturer_name": "BMW",
    "model_name": "i8",
    "car_type": "Coupe"
  },
  {
    "year": 2016,
    "manufacturer_name": "Cadillac",
    "model_name": "ELR",
    "car_type": "Coupe"
  },
  {
    "year": 2016,
    "manufacturer_name": "BMW",
    "model_name": "X1",
    "car_type": "SUV"
  },
  {
    "year": 2016,
    "manufacturer_name": "Buick",
    "model_name": "Enclave",
    "car_type": "SUV"
  },
  {
    "year": 2016,
    "manufacturer_name": "BMW",
    "model_name": "X6 M",
    "car_type": "SUV"
  },
  {
    "year": 2016,
    "manufacturer_name": "Buick",
    "model_name": "Envision",
    "car_type": "SUV"
  },
  {
    "year": 2016,
    "manufacturer_name": "BMW",
    "model_name": "M6",
    "car_type": "Coupe, Convertible"
  },
  {
    "year": 2016,
    "manufacturer_name": "BMW",
    "model_name": "M3",
    "car_type": "Sedan"
  },
  {
    "year": 2016,
    "manufacturer_name": "Cadillac",
    "model_name": "ATS-V",
    "car_type": "Sedan, Coupe"
  },
  {
    "year": 2016,
    "manufacturer_name": "BMW",
    "model_name": "X6",
    "car_type": "SUV"
  },
  {
    "year": 2016,
    "manufacturer_name": "Cadillac",
    "model_name": "CTS",
    "car_type": "Sedan"
  },
  {
    "year": 2016,
    "manufacturer_name": "Chevrolet",
    "model_name": "Camaro",
    "car_type": "Coupe, Convertible"
  },
  {
    "year": 2016,
    "manufacturer_name": "Buick",
    "model_name": "LaCrosse",
    "car_type": "Sedan"
  },
  {
    "year": 2016,
    "manufacturer_name": "Chevrolet",
    "model_name": "Colorado Extended Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2016,
    "manufacturer_name": "Cadillac",
    "model_name": "XTS",
    "car_type": "Sedan"
  },
  {
    "year": 2016,
    "manufacturer_name": "Chevrolet",
    "model_name": "Cruze",
    "car_type": "Sedan"
  },
  {
    "year": 2016,
    "manufacturer_name": "Chevrolet",
    "model_name": "Corvette",
    "car_type": "Coupe, Convertible"
  },
  {
    "year": 2016,
    "manufacturer_name": "Chevrolet",
    "model_name": "Colorado Crew Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2016,
    "manufacturer_name": "Cadillac",
    "model_name": "Escalade ESV",
    "car_type": "SUV"
  },
  {
    "year": 2016,
    "manufacturer_name": "Cadillac",
    "model_name": "Escalade",
    "car_type": "SUV"
  },
  {
    "year": 2016,
    "manufacturer_name": "Cadillac",
    "model_name": "CTS-V",
    "car_type": "Sedan"
  },
  {
    "year": 2016,
    "manufacturer_name": "Cadillac",
    "model_name": "SRX",
    "car_type": "SUV"
  },
  {
    "year": 2016,
    "manufacturer_name": "Cadillac",
    "model_name": "CT6",
    "car_type": "Sedan"
  },
  {
    "year": 2016,
    "manufacturer_name": "Chevrolet",
    "model_name": "Cruze Limited",
    "car_type": "Sedan"
  },
  {
    "year": 2016,
    "manufacturer_name": "Chevrolet",
    "model_name": "City Express",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2016,
    "manufacturer_name": "Chevrolet",
    "model_name": "Express 2500 Cargo",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2016,
    "manufacturer_name": "Chevrolet",
    "model_name": "Express 2500 Passenger",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2016,
    "manufacturer_name": "Chevrolet",
    "model_name": "Equinox",
    "car_type": "SUV"
  },
  {
    "year": 2016,
    "manufacturer_name": "Chevrolet",
    "model_name": "Express 3500 Passenger",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2016,
    "manufacturer_name": "Chevrolet",
    "model_name": "Silverado 2500 HD Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2016,
    "manufacturer_name": "Chevrolet",
    "model_name": "Express 3500 Cargo",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2016,
    "manufacturer_name": "Chevrolet",
    "model_name": "Silverado 3500 HD Double Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2016,
    "manufacturer_name": "Chevrolet",
    "model_name": "Silverado 1500 Double Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2016,
    "manufacturer_name": "Chevrolet",
    "model_name": "Silverado 2500 HD Crew Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2016,
    "manufacturer_name": "Chevrolet",
    "model_name": "Silverado 1500 Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2016,
    "manufacturer_name": "Chevrolet",
    "model_name": "Impala Limited",
    "car_type": "Sedan"
  },
  {
    "year": 2016,
    "manufacturer_name": "Chevrolet",
    "model_name": "Impala",
    "car_type": "Sedan"
  },
  {
    "year": 2016,
    "manufacturer_name": "Chevrolet",
    "model_name": "Sonic",
    "car_type": "Sedan, Hatchback"
  },
  {
    "year": 2016,
    "manufacturer_name": "Chevrolet",
    "model_name": "Silverado 1500 Crew Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2016,
    "manufacturer_name": "Chevrolet",
    "model_name": "Malibu",
    "car_type": "Sedan"
  },
  {
    "year": 2016,
    "manufacturer_name": "Chevrolet",
    "model_name": "Silverado 2500 HD Double Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2016,
    "manufacturer_name": "Chevrolet",
    "model_name": "Malibu Limited",
    "car_type": "Sedan"
  },
  {
    "year": 2016,
    "manufacturer_name": "Dodge",
    "model_name": "Dart",
    "car_type": "Sedan"
  },
  {
    "year": 2016,
    "manufacturer_name": "Chevrolet",
    "model_name": "Silverado 3500 HD Crew Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2016,
    "manufacturer_name": "Chevrolet",
    "model_name": "Spark",
    "car_type": "Hatchback"
  },
  {
    "year": 2016,
    "manufacturer_name": "Chevrolet",
    "model_name": "Traverse",
    "car_type": "SUV"
  },
  {
    "year": 2016,
    "manufacturer_name": "Chevrolet",
    "model_name": "Suburban 3500HD",
    "car_type": "SUV"
  },
  {
    "year": 2016,
    "manufacturer_name": "Dodge",
    "model_name": "Durango",
    "car_type": "SUV"
  },
  {
    "year": 2016,
    "manufacturer_name": "Dodge",
    "model_name": "Charger",
    "car_type": "Sedan"
  },
  {
    "year": 2016,
    "manufacturer_name": "Chevrolet",
    "model_name": "Silverado 3500 HD Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2016,
    "manufacturer_name": "Dodge",
    "model_name": "Challenger",
    "car_type": "Coupe"
  },
  {
    "year": 2016,
    "manufacturer_name": "Chrysler",
    "model_name": "Town & Country",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2016,
    "manufacturer_name": "Chevrolet",
    "model_name": "Spark EV",
    "car_type": "Hatchback"
  },
  {
    "year": 2016,
    "manufacturer_name": "Chevrolet",
    "model_name": "Volt",
    "car_type": "Sedan"
  },
  {
    "year": 2016,
    "manufacturer_name": "Chevrolet",
    "model_name": "Suburban",
    "car_type": "SUV"
  },
  {
    "year": 2016,
    "manufacturer_name": "Chevrolet",
    "model_name": "SS",
    "car_type": "Sedan"
  },
  {
    "year": 2016,
    "manufacturer_name": "Chevrolet",
    "model_name": "Trax",
    "car_type": "SUV"
  },
  {
    "year": 2016,
    "manufacturer_name": "Ferrari",
    "model_name": "488 GTB",
    "car_type": "Coupe"
  },
  {
    "year": 2016,
    "manufacturer_name": "Chevrolet",
    "model_name": "Tahoe",
    "car_type": "SUV"
  },
  {
    "year": 2016,
    "manufacturer_name": "Chrysler",
    "model_name": "200",
    "car_type": "Sedan"
  },
  {
    "year": 2016,
    "manufacturer_name": "Chrysler",
    "model_name": "300",
    "car_type": "Sedan"
  },
  {
    "year": 2016,
    "manufacturer_name": "Dodge",
    "model_name": "Journey",
    "car_type": "SUV"
  },
  {
    "year": 2016,
    "manufacturer_name": "Dodge",
    "model_name": "Viper",
    "car_type": "Coupe"
  },
  {
    "year": 2016,
    "manufacturer_name": "Ferrari",
    "model_name": "F12berlinetta",
    "car_type": "Coupe"
  },
  {
    "year": 2016,
    "manufacturer_name": "Ferrari",
    "model_name": "California",
    "car_type": "Convertible"
  },
  {
    "year": 2016,
    "manufacturer_name": "Dodge",
    "model_name": "Grand Caravan Passenger",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2016,
    "manufacturer_name": "Ford",
    "model_name": "F250 Super Duty Super Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2016,
    "manufacturer_name": "FIAT",
    "model_name": "500e",
    "car_type": "Hatchback"
  },
  {
    "year": 2016,
    "manufacturer_name": "Ford",
    "model_name": "F150 Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2016,
    "manufacturer_name": "FIAT",
    "model_name": "500",
    "car_type": "Hatchback"
  },
  {
    "year": 2016,
    "manufacturer_name": "FIAT",
    "model_name": "500L",
    "car_type": "Hatchback"
  },
  {
    "year": 2016,
    "manufacturer_name": "FIAT",
    "model_name": "500X",
    "car_type": "SUV"
  },
  {
    "year": 2016,
    "manufacturer_name": "Ferrari",
    "model_name": "FF",
    "car_type": "Coupe"
  },
  {
    "year": 2016,
    "manufacturer_name": "Ferrari",
    "model_name": "488 Spider",
    "car_type": "Convertible"
  },
  {
    "year": 2016,
    "manufacturer_name": "Ford",
    "model_name": "Edge",
    "car_type": "SUV"
  },
  {
    "year": 2016,
    "manufacturer_name": "FIAT",
    "model_name": "500c",
    "car_type": "Convertible"
  },
  {
    "year": 2016,
    "manufacturer_name": "Ford",
    "model_name": "Escape",
    "car_type": "SUV"
  },
  {
    "year": 2016,
    "manufacturer_name": "Ford",
    "model_name": "C-MAX Energi",
    "car_type": "Wagon"
  },
  {
    "year": 2016,
    "manufacturer_name": "FIAT",
    "model_name": "500 Abarth",
    "car_type": "Hatchback, Convertible"
  },
  {
    "year": 2016,
    "manufacturer_name": "Ford",
    "model_name": "Expedition EL",
    "car_type": "SUV"
  },
  {
    "year": 2016,
    "manufacturer_name": "Ford",
    "model_name": "Expedition",
    "car_type": "SUV"
  },
  {
    "year": 2016,
    "manufacturer_name": "Ford",
    "model_name": "F150 SuperCrew Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2016,
    "manufacturer_name": "Ford",
    "model_name": "F350 Super Duty Crew Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2016,
    "manufacturer_name": "Ford",
    "model_name": "Mustang",
    "car_type": "Coupe, Convertible"
  },
  {
    "year": 2016,
    "manufacturer_name": "Ford",
    "model_name": "F350 Super Duty Super Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2016,
    "manufacturer_name": "Ford",
    "model_name": "Fiesta",
    "car_type": "Hatchback, Sedan"
  },
  {
    "year": 2016,
    "manufacturer_name": "Freightliner",
    "model_name": "Sprinter 2500 Cargo",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2016,
    "manufacturer_name": "Ford",
    "model_name": "C-MAX Hybrid",
    "car_type": "Wagon"
  },
  {
    "year": 2016,
    "manufacturer_name": "Ford",
    "model_name": "Transit 150 Van",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2016,
    "manufacturer_name": "Ford",
    "model_name": "F350 Super Duty Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2016,
    "manufacturer_name": "Ford",
    "model_name": "Fusion",
    "car_type": "Sedan"
  },
  {
    "year": 2016,
    "manufacturer_name": "Ford",
    "model_name": "F150 Super Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2016,
    "manufacturer_name": "Ford",
    "model_name": "F250 Super Duty Crew Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2016,
    "manufacturer_name": "Ford",
    "model_name": "Explorer",
    "car_type": "SUV"
  },
  {
    "year": 2016,
    "manufacturer_name": "Ford",
    "model_name": "Transit Connect Cargo",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2016,
    "manufacturer_name": "Ford",
    "model_name": "Transit 150 Wagon",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2016,
    "manufacturer_name": "Ford",
    "model_name": "Transit 350 HD Van",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2016,
    "manufacturer_name": "Ford",
    "model_name": "F250 Super Duty Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2016,
    "manufacturer_name": "Ford",
    "model_name": "Taurus",
    "car_type": "Sedan"
  },
  {
    "year": 2016,
    "manufacturer_name": "Ford",
    "model_name": "Flex",
    "car_type": "SUV"
  },
  {
    "year": 2016,
    "manufacturer_name": "Ford",
    "model_name": "Focus",
    "car_type": "Sedan, Hatchback"
  },
  {
    "year": 2016,
    "manufacturer_name": "Ford",
    "model_name": "F450 Super Duty Crew Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2016,
    "manufacturer_name": "GMC",
    "model_name": "Canyon Crew Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2016,
    "manufacturer_name": "Ford",
    "model_name": "Fusion Energi",
    "car_type": "Sedan"
  },
  {
    "year": 2016,
    "manufacturer_name": "Ford",
    "model_name": "Transit 350 Van",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2016,
    "manufacturer_name": "GMC",
    "model_name": "Canyon Extended Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2016,
    "manufacturer_name": "GMC",
    "model_name": "Savana 3500 Cargo",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2016,
    "manufacturer_name": "GMC",
    "model_name": "Sierra 2500 HD Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2016,
    "manufacturer_name": "Freightliner",
    "model_name": "Sprinter 2500 Passenger",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2016,
    "manufacturer_name": "Freightliner",
    "model_name": "Sprinter 2500 Crew",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2016,
    "manufacturer_name": "GMC",
    "model_name": "Sierra 2500 HD Double Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2016,
    "manufacturer_name": "Freightliner",
    "model_name": "Sprinter 3500 Cargo",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2016,
    "manufacturer_name": "GMC",
    "model_name": "Sierra 3500 HD Crew Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2016,
    "manufacturer_name": "GMC",
    "model_name": "Sierra 2500 HD Crew Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2016,
    "manufacturer_name": "Ford",
    "model_name": "Transit 350 Wagon",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2016,
    "manufacturer_name": "GMC",
    "model_name": "Sierra 1500 Crew Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2016,
    "manufacturer_name": "GMC",
    "model_name": "Sierra 1500 Double Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2016,
    "manufacturer_name": "GMC",
    "model_name": "Savana 2500 Passenger",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2016,
    "manufacturer_name": "Ford",
    "model_name": "Transit 250 Van",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2016,
    "manufacturer_name": "GMC",
    "model_name": "Sierra 1500 Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2016,
    "manufacturer_name": "GMC",
    "model_name": "Savana 2500 Cargo",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2016,
    "manufacturer_name": "GMC",
    "model_name": "Sierra 3500 HD Double Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2016,
    "manufacturer_name": "GMC",
    "model_name": "Savana 3500 Passenger",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2016,
    "manufacturer_name": "Ford",
    "model_name": "Transit Connect Passenger",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2016,
    "manufacturer_name": "GMC",
    "model_name": "Acadia",
    "car_type": "SUV"
  },
  {
    "year": 2016,
    "manufacturer_name": "Honda",
    "model_name": "HR-V",
    "car_type": "SUV"
  },
  {
    "year": 2016,
    "manufacturer_name": "GMC",
    "model_name": "Sierra 3500 HD Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2016,
    "manufacturer_name": "GMC",
    "model_name": "Yukon",
    "car_type": "SUV"
  },
  {
    "year": 2016,
    "manufacturer_name": "Honda",
    "model_name": "Civic",
    "car_type": "Sedan, Coupe"
  },
  {
    "year": 2016,
    "manufacturer_name": "GMC",
    "model_name": "Terrain",
    "car_type": "SUV"
  },
  {
    "year": 2016,
    "manufacturer_name": "Honda",
    "model_name": "Pilot",
    "car_type": "SUV"
  },
  {
    "year": 2016,
    "manufacturer_name": "GMC",
    "model_name": "Yukon XL",
    "car_type": "SUV"
  },
  {
    "year": 2016,
    "manufacturer_name": "Honda",
    "model_name": "Fit",
    "car_type": "Hatchback"
  },
  {
    "year": 2016,
    "manufacturer_name": "Honda",
    "model_name": "Odyssey",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2016,
    "manufacturer_name": "Honda",
    "model_name": "CR-V",
    "car_type": "SUV"
  },
  {
    "year": 2016,
    "manufacturer_name": "Honda",
    "model_name": "Accord",
    "car_type": "Sedan, Coupe"
  },
  {
    "year": 2016,
    "manufacturer_name": "Hyundai",
    "model_name": "Elantra",
    "car_type": "Sedan"
  },
  {
    "year": 2016,
    "manufacturer_name": "Honda",
    "model_name": "CR-Z",
    "car_type": "Coupe"
  },
  {
    "year": 2016,
    "manufacturer_name": "Hyundai",
    "model_name": "Accent",
    "car_type": "Hatchback, Sedan"
  },
  {
    "year": 2016,
    "manufacturer_name": "Hyundai",
    "model_name": "Sonata Plug-in Hybrid",
    "car_type": "Sedan"
  },
  {
    "year": 2016,
    "manufacturer_name": "Hyundai",
    "model_name": "Santa Fe",
    "car_type": "SUV"
  },
  {
    "year": 2016,
    "manufacturer_name": "Hyundai",
    "model_name": "Genesis",
    "car_type": "Sedan"
  },
  {
    "year": 2016,
    "manufacturer_name": "Hyundai",
    "model_name": "Azera",
    "car_type": "Sedan"
  },
  {
    "year": 2016,
    "manufacturer_name": "Hyundai",
    "model_name": "Genesis Coupe",
    "car_type": "Coupe"
  },
  {
    "year": 2016,
    "manufacturer_name": "INFINITI",
    "model_name": "Q50",
    "car_type": "Sedan"
  },
  {
    "year": 2016,
    "manufacturer_name": "Hyundai",
    "model_name": "Equus",
    "car_type": "Sedan"
  },
  {
    "year": 2016,
    "manufacturer_name": "INFINITI",
    "model_name": "QX50",
    "car_type": "SUV"
  },
  {
    "year": 2016,
    "manufacturer_name": "Hyundai",
    "model_name": "Elantra GT",
    "car_type": "Hatchback"
  },
  {
    "year": 2016,
    "manufacturer_name": "Hyundai",
    "model_name": "Santa Fe Sport",
    "car_type": "SUV"
  },
  {
    "year": 2016,
    "manufacturer_name": "Hyundai",
    "model_name": "Tucson Fuel Cell",
    "car_type": "SUV"
  },
  {
    "year": 2016,
    "manufacturer_name": "Hyundai",
    "model_name": "Tucson",
    "car_type": "SUV"
  },
  {
    "year": 2016,
    "manufacturer_name": "Hyundai",
    "model_name": "Veloster",
    "car_type": "Coupe"
  },
  {
    "year": 2016,
    "manufacturer_name": "Hyundai",
    "model_name": "Sonata",
    "car_type": "Sedan"
  },
  {
    "year": 2016,
    "manufacturer_name": "Hyundai",
    "model_name": "Sonata Hybrid",
    "car_type": "Sedan"
  },
  {
    "year": 2016,
    "manufacturer_name": "Jeep",
    "model_name": "Cherokee",
    "car_type": "SUV"
  },
  {
    "year": 2016,
    "manufacturer_name": "Jaguar",
    "model_name": "XF",
    "car_type": "Sedan"
  },
  {
    "year": 2016,
    "manufacturer_name": "Jeep",
    "model_name": "Compass",
    "car_type": "SUV"
  },
  {
    "year": 2016,
    "manufacturer_name": "INFINITI",
    "model_name": "QX70",
    "car_type": "SUV"
  },
  {
    "year": 2016,
    "manufacturer_name": "Jeep",
    "model_name": "Wrangler",
    "car_type": "SUV"
  },
  {
    "year": 2016,
    "manufacturer_name": "INFINITI",
    "model_name": "QX80",
    "car_type": "SUV"
  },
  {
    "year": 2016,
    "manufacturer_name": "INFINITI",
    "model_name": "QX60",
    "car_type": "SUV"
  },
  {
    "year": 2016,
    "manufacturer_name": "Jeep",
    "model_name": "Patriot",
    "car_type": "SUV"
  },
  {
    "year": 2016,
    "manufacturer_name": "Jaguar",
    "model_name": "XJ",
    "car_type": "Sedan"
  },
  {
    "year": 2016,
    "manufacturer_name": "Jaguar",
    "model_name": "F-TYPE",
    "car_type": "Coupe, Convertible"
  },
  {
    "year": 2016,
    "manufacturer_name": "INFINITI",
    "model_name": "Q70",
    "car_type": "Sedan"
  },
  {
    "year": 2016,
    "manufacturer_name": "Kia",
    "model_name": "Cadenza",
    "car_type": "Sedan"
  },
  {
    "year": 2016,
    "manufacturer_name": "Jeep",
    "model_name": "Grand Cherokee",
    "car_type": "SUV"
  },
  {
    "year": 2016,
    "manufacturer_name": "Lexus",
    "model_name": "GS",
    "car_type": "Sedan"
  },
  {
    "year": 2016,
    "manufacturer_name": "Kia",
    "model_name": "Sorento",
    "car_type": "SUV"
  },
  {
    "year": 2016,
    "manufacturer_name": "Kia",
    "model_name": "Optima",
    "car_type": "Sedan"
  },
  {
    "year": 2016,
    "manufacturer_name": "Kia",
    "model_name": "K900",
    "car_type": "Sedan"
  },
  {
    "year": 2016,
    "manufacturer_name": "Jeep",
    "model_name": "Renegade",
    "car_type": "SUV"
  },
  {
    "year": 2016,
    "manufacturer_name": "Kia",
    "model_name": "Forte Koup",
    "car_type": "Coupe"
  },
  {
    "year": 2016,
    "manufacturer_name": "Kia",
    "model_name": "Rio",
    "car_type": "Sedan, Hatchback"
  },
  {
    "year": 2016,
    "manufacturer_name": "Lamborghini",
    "model_name": "Huracan",
    "car_type": "Coupe, Convertible"
  },
  {
    "year": 2016,
    "manufacturer_name": "Kia",
    "model_name": "Forte5",
    "car_type": "Hatchback"
  },
  {
    "year": 2016,
    "manufacturer_name": "Kia",
    "model_name": "Forte",
    "car_type": "Sedan"
  },
  {
    "year": 2016,
    "manufacturer_name": "Land Rover",
    "model_name": "Range Rover Sport",
    "car_type": "SUV"
  },
  {
    "year": 2016,
    "manufacturer_name": "Kia",
    "model_name": "Sedona",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2016,
    "manufacturer_name": "Land Rover",
    "model_name": "Range Rover",
    "car_type": "SUV"
  },
  {
    "year": 2016,
    "manufacturer_name": "Kia",
    "model_name": "Sportage",
    "car_type": "SUV"
  },
  {
    "year": 2016,
    "manufacturer_name": "Kia",
    "model_name": "Optima Hybrid",
    "car_type": "Sedan"
  },
  {
    "year": 2016,
    "manufacturer_name": "Kia",
    "model_name": "Soul",
    "car_type": "Wagon"
  },
  {
    "year": 2016,
    "manufacturer_name": "Lexus",
    "model_name": "RC",
    "car_type": "Coupe"
  },
  {
    "year": 2016,
    "manufacturer_name": "Maserati",
    "model_name": "Ghibli",
    "car_type": "Sedan"
  },
  {
    "year": 2016,
    "manufacturer_name": "Lexus",
    "model_name": "CT",
    "car_type": "Hatchback"
  },
  {
    "year": 2016,
    "manufacturer_name": "Lamborghini",
    "model_name": "Aventador",
    "car_type": "Convertible, Coupe"
  },
  {
    "year": 2016,
    "manufacturer_name": "Lincoln",
    "model_name": "MKZ",
    "car_type": "Sedan"
  },
  {
    "year": 2016,
    "manufacturer_name": "Lexus",
    "model_name": "NX",
    "car_type": "SUV"
  },
  {
    "year": 2016,
    "manufacturer_name": "Land Rover",
    "model_name": "Range Rover Evoque",
    "car_type": "SUV"
  },
  {
    "year": 2016,
    "manufacturer_name": "Kia",
    "model_name": "Soul EV",
    "car_type": "Wagon"
  },
  {
    "year": 2016,
    "manufacturer_name": "Maserati",
    "model_name": "Quattroporte",
    "car_type": "Sedan"
  },
  {
    "year": 2016,
    "manufacturer_name": "Lexus",
    "model_name": "GX",
    "car_type": "SUV"
  },
  {
    "year": 2016,
    "manufacturer_name": "Land Rover",
    "model_name": "LR4",
    "car_type": "SUV"
  },
  {
    "year": 2016,
    "manufacturer_name": "Lincoln",
    "model_name": "MKX",
    "car_type": "SUV"
  },
  {
    "year": 2016,
    "manufacturer_name": "Lexus",
    "model_name": "IS",
    "car_type": "Sedan"
  },
  {
    "year": 2016,
    "manufacturer_name": "Land Rover",
    "model_name": "Discovery Sport",
    "car_type": "SUV"
  },
  {
    "year": 2016,
    "manufacturer_name": "Lincoln",
    "model_name": "MKT",
    "car_type": "SUV"
  },
  {
    "year": 2016,
    "manufacturer_name": "Lexus",
    "model_name": "RX",
    "car_type": "SUV"
  },
  {
    "year": 2016,
    "manufacturer_name": "MAZDA",
    "model_name": "CX-9",
    "car_type": "SUV"
  },
  {
    "year": 2016,
    "manufacturer_name": "Lexus",
    "model_name": "LS",
    "car_type": "Sedan"
  },
  {
    "year": 2016,
    "manufacturer_name": "Lexus",
    "model_name": "ES",
    "car_type": "Sedan"
  },
  {
    "year": 2016,
    "manufacturer_name": "MAZDA",
    "model_name": "MAZDA3",
    "car_type": "Sedan, Hatchback"
  },
  {
    "year": 2016,
    "manufacturer_name": "Lincoln",
    "model_name": "MKC",
    "car_type": "SUV"
  },
  {
    "year": 2016,
    "manufacturer_name": "MAZDA",
    "model_name": "MAZDA6",
    "car_type": "Sedan"
  },
  {
    "year": 2016,
    "manufacturer_name": "McLaren",
    "model_name": "650S",
    "car_type": "Convertible, Coupe"
  },
  {
    "year": 2016,
    "manufacturer_name": "Lexus",
    "model_name": "LX",
    "car_type": "SUV"
  },
  {
    "year": 2016,
    "manufacturer_name": "Lincoln",
    "model_name": "MKS",
    "car_type": "Sedan"
  },
  {
    "year": 2016,
    "manufacturer_name": "Mercedes-Benz",
    "model_name": "B-Class",
    "car_type": "Hatchback"
  },
  {
    "year": 2016,
    "manufacturer_name": "McLaren",
    "model_name": "675LT",
    "car_type": "Coupe"
  },
  {
    "year": 2016,
    "manufacturer_name": "Maserati",
    "model_name": "GranTurismo",
    "car_type": "Coupe, Convertible"
  },
  {
    "year": 2016,
    "manufacturer_name": "Mercedes-Benz",
    "model_name": "G-Class",
    "car_type": "SUV"
  },
  {
    "year": 2016,
    "manufacturer_name": "Lincoln",
    "model_name": "Navigator",
    "car_type": "SUV"
  },
  {
    "year": 2016,
    "manufacturer_name": "MAZDA",
    "model_name": "CX-3",
    "car_type": "SUV"
  },
  {
    "year": 2016,
    "manufacturer_name": "Mercedes-Benz",
    "model_name": "CLS-Class",
    "car_type": "Sedan"
  },
  {
    "year": 2016,
    "manufacturer_name": "Mercedes-Benz",
    "model_name": "GL-Class",
    "car_type": "SUV"
  },
  {
    "year": 2016,
    "manufacturer_name": "Lincoln",
    "model_name": "Navigator L",
    "car_type": "SUV"
  },
  {
    "year": 2016,
    "manufacturer_name": "Mercedes-Benz",
    "model_name": "E-Class",
    "car_type": "Sedan, Coupe, Wagon, Convertible"
  },
  {
    "year": 2016,
    "manufacturer_name": "Mercedes-Benz",
    "model_name": "CLA",
    "car_type": "Sedan"
  },
  {
    "year": 2016,
    "manufacturer_name": "MAZDA",
    "model_name": "MX-5 Miata",
    "car_type": "Convertible"
  },
  {
    "year": 2016,
    "manufacturer_name": "MAZDA",
    "model_name": "CX-5",
    "car_type": "SUV"
  },
  {
    "year": 2016,
    "manufacturer_name": "McLaren",
    "model_name": "570S",
    "car_type": "Coupe"
  },
  {
    "year": 2016,
    "manufacturer_name": "Mercedes-Benz",
    "model_name": "C-Class",
    "car_type": "Sedan"
  },
  {
    "year": 2016,
    "manufacturer_name": "Mercedes-Benz",
    "model_name": "GLA",
    "car_type": "SUV"
  },
  {
    "year": 2016,
    "manufacturer_name": "Mercedes-Benz",
    "model_name": "GLC",
    "car_type": "SUV"
  },
  {
    "year": 2016,
    "manufacturer_name": "Mercedes-Benz",
    "model_name": "Mercedes-AMG CLA",
    "car_type": "Sedan"
  },
  {
    "year": 2016,
    "manufacturer_name": "Mercedes-Benz",
    "model_name": "GLE",
    "car_type": "SUV"
  },
  {
    "year": 2016,
    "manufacturer_name": "Mercedes-Benz",
    "model_name": "SL",
    "car_type": "Convertible"
  },
  {
    "year": 2016,
    "manufacturer_name": "Mercedes-Benz",
    "model_name": "GLE Coupe",
    "car_type": "SUV"
  },
  {
    "year": 2016,
    "manufacturer_name": "Mercedes-Benz",
    "model_name": "Mercedes-AMG SL",
    "car_type": "Convertible"
  },
  {
    "year": 2016,
    "manufacturer_name": "MINI",
    "model_name": "Countryman",
    "car_type": "SUV"
  },
  {
    "year": 2016,
    "manufacturer_name": "Nissan",
    "model_name": "370Z",
    "car_type": "Coupe, Convertible"
  },
  {
    "year": 2016,
    "manufacturer_name": "Mercedes-Benz",
    "model_name": "Metris Passenger",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2016,
    "manufacturer_name": "Mercedes-Benz",
    "model_name": "Mercedes-AMG GLE",
    "car_type": "SUV"
  },
  {
    "year": 2016,
    "manufacturer_name": "Mercedes-Benz",
    "model_name": "Mercedes-AMG GLA",
    "car_type": "SUV"
  },
  {
    "year": 2016,
    "manufacturer_name": "Mercedes-Benz",
    "model_name": "Mercedes-Maybach S 600",
    "car_type": "Sedan"
  },
  {
    "year": 2016,
    "manufacturer_name": "Mercedes-Benz",
    "model_name": "SLK",
    "car_type": "Convertible"
  },
  {
    "year": 2016,
    "manufacturer_name": "Mercedes-Benz",
    "model_name": "Metris Cargo",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2016,
    "manufacturer_name": "Mercedes-Benz",
    "model_name": "S-Class",
    "car_type": "Sedan, Coupe"
  },
  {
    "year": 2016,
    "manufacturer_name": "Mercedes-Benz",
    "model_name": "Mercedes-AMG GT",
    "car_type": "Coupe"
  },
  {
    "year": 2016,
    "manufacturer_name": "MINI",
    "model_name": "Clubman",
    "car_type": "Hatchback"
  },
  {
    "year": 2016,
    "manufacturer_name": "Mercedes-Benz",
    "model_name": "Sprinter 2500 Passenger",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2016,
    "manufacturer_name": "Mercedes-Benz",
    "model_name": "Mercedes-AMG SLK",
    "car_type": "Convertible"
  },
  {
    "year": 2016,
    "manufacturer_name": "Mercedes-Benz",
    "model_name": "Mercedes-AMG GLE Coupe",
    "car_type": "SUV"
  },
  {
    "year": 2016,
    "manufacturer_name": "Mercedes-Benz",
    "model_name": "Sprinter 3500 Cargo",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2016,
    "manufacturer_name": "MINI",
    "model_name": "Hardtop 2 Door",
    "car_type": "Hatchback"
  },
  {
    "year": 2016,
    "manufacturer_name": "Mercedes-Benz",
    "model_name": "Sprinter 2500 Cargo",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2016,
    "manufacturer_name": "Mercedes-Benz",
    "model_name": "Sprinter 2500 Crew",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2016,
    "manufacturer_name": "MINI",
    "model_name": "Paceman",
    "car_type": "Hatchback"
  },
  {
    "year": 2016,
    "manufacturer_name": "MINI",
    "model_name": "Convertible",
    "car_type": "Convertible"
  },
  {
    "year": 2016,
    "manufacturer_name": "Nissan",
    "model_name": "NV3500 HD Passenger",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2016,
    "manufacturer_name": "Mitsubishi",
    "model_name": "Lancer",
    "car_type": "Sedan"
  },
  {
    "year": 2016,
    "manufacturer_name": "Mitsubishi",
    "model_name": "Outlander Sport",
    "car_type": "SUV"
  },
  {
    "year": 2016,
    "manufacturer_name": "Porsche",
    "model_name": "Panamera",
    "car_type": "Sedan"
  },
  {
    "year": 2016,
    "manufacturer_name": "Nissan",
    "model_name": "NV1500 Cargo",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2016,
    "manufacturer_name": "Ram",
    "model_name": "2500 Mega Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2016,
    "manufacturer_name": "Nissan",
    "model_name": "Murano",
    "car_type": "SUV"
  },
  {
    "year": 2016,
    "manufacturer_name": "Nissan",
    "model_name": "NV3500 HD Cargo",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2016,
    "manufacturer_name": "Nissan",
    "model_name": "Frontier Crew Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2016,
    "manufacturer_name": "Nissan",
    "model_name": "NV2500 HD Cargo",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2016,
    "manufacturer_name": "Nissan",
    "model_name": "Versa",
    "car_type": "Sedan"
  },
  {
    "year": 2016,
    "manufacturer_name": "MINI",
    "model_name": "Hardtop 4 Door",
    "car_type": "Hatchback"
  },
  {
    "year": 2016,
    "manufacturer_name": "Nissan",
    "model_name": "Sentra",
    "car_type": "Sedan"
  },
  {
    "year": 2016,
    "manufacturer_name": "Ram",
    "model_name": "2500 Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2016,
    "manufacturer_name": "Nissan",
    "model_name": "Pathfinder",
    "car_type": "SUV"
  },
  {
    "year": 2016,
    "manufacturer_name": "Mitsubishi",
    "model_name": "i-MiEV",
    "car_type": "Hatchback"
  },
  {
    "year": 2016,
    "manufacturer_name": "Nissan",
    "model_name": "NV200",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2016,
    "manufacturer_name": "Nissan",
    "model_name": "TITAN XD Crew Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2016,
    "manufacturer_name": "Nissan",
    "model_name": "Quest",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2016,
    "manufacturer_name": "Porsche",
    "model_name": "Cayman",
    "car_type": "Coupe"
  },
  {
    "year": 2016,
    "manufacturer_name": "Nissan",
    "model_name": "Rogue",
    "car_type": "SUV"
  },
  {
    "year": 2016,
    "manufacturer_name": "Porsche",
    "model_name": "Boxster",
    "car_type": "Convertible"
  },
  {
    "year": 2016,
    "manufacturer_name": "Nissan",
    "model_name": "Maxima",
    "car_type": "Sedan"
  },
  {
    "year": 2016,
    "manufacturer_name": "Ram",
    "model_name": "1500 Quad Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2016,
    "manufacturer_name": "Nissan",
    "model_name": "JUKE",
    "car_type": "SUV"
  },
  {
    "year": 2016,
    "manufacturer_name": "Mitsubishi",
    "model_name": "Outlander",
    "car_type": "SUV"
  },
  {
    "year": 2016,
    "manufacturer_name": "Porsche",
    "model_name": "Macan",
    "car_type": "SUV"
  },
  {
    "year": 2016,
    "manufacturer_name": "Porsche",
    "model_name": "Cayenne",
    "car_type": "SUV"
  },
  {
    "year": 2016,
    "manufacturer_name": "Ram",
    "model_name": "3500 Mega Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2016,
    "manufacturer_name": "Nissan",
    "model_name": "LEAF",
    "car_type": "Hatchback"
  },
  {
    "year": 2016,
    "manufacturer_name": "Rolls-Royce",
    "model_name": "Dawn",
    "car_type": "Convertible"
  },
  {
    "year": 2016,
    "manufacturer_name": "Nissan",
    "model_name": "Altima",
    "car_type": "Sedan"
  },
  {
    "year": 2016,
    "manufacturer_name": "Ram",
    "model_name": "1500 Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2016,
    "manufacturer_name": "Nissan",
    "model_name": "GT-R",
    "car_type": "Coupe"
  },
  {
    "year": 2016,
    "manufacturer_name": "Nissan",
    "model_name": "Frontier King Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2016,
    "manufacturer_name": "Ram",
    "model_name": "ProMaster Cargo Van",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2016,
    "manufacturer_name": "Porsche",
    "model_name": "911",
    "car_type": "Coupe, Convertible"
  },
  {
    "year": 2016,
    "manufacturer_name": "Nissan",
    "model_name": "NV200 Taxi",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2016,
    "manufacturer_name": "Ram",
    "model_name": "1500 Crew Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2016,
    "manufacturer_name": "Nissan",
    "model_name": "Versa Note",
    "car_type": "Hatchback"
  },
  {
    "year": 2016,
    "manufacturer_name": "Scion",
    "model_name": "iA",
    "car_type": "Sedan"
  },
  {
    "year": 2016,
    "manufacturer_name": "Ram",
    "model_name": "ProMaster Window Van",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2016,
    "manufacturer_name": "Rolls-Royce",
    "model_name": "Wraith",
    "car_type": "Coupe"
  },
  {
    "year": 2016,
    "manufacturer_name": "Ram",
    "model_name": "3500 Crew Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2016,
    "manufacturer_name": "Ram",
    "model_name": "2500 Crew Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2016,
    "manufacturer_name": "Ram",
    "model_name": "ProMaster City",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2016,
    "manufacturer_name": "Ram",
    "model_name": "3500 Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2016,
    "manufacturer_name": "Rolls-Royce",
    "model_name": "Phantom",
    "car_type": "Sedan, Convertible, Coupe"
  },
  {
    "year": 2016,
    "manufacturer_name": "Subaru",
    "model_name": "BRZ",
    "car_type": "Coupe"
  },
  {
    "year": 2016,
    "manufacturer_name": "Scion",
    "model_name": "tC",
    "car_type": "Coupe"
  },
  {
    "year": 2016,
    "manufacturer_name": "Subaru",
    "model_name": "WRX",
    "car_type": "Sedan"
  },
  {
    "year": 2016,
    "manufacturer_name": "Tesla",
    "model_name": "Model S",
    "car_type": "Sedan"
  },
  {
    "year": 2016,
    "manufacturer_name": "smart",
    "model_name": "fortwo electric drive",
    "car_type": "Hatchback"
  },
  {
    "year": 2016,
    "manufacturer_name": "Subaru",
    "model_name": "Impreza",
    "car_type": "Wagon, Sedan"
  },
  {
    "year": 2016,
    "manufacturer_name": "Subaru",
    "model_name": "Forester",
    "car_type": "SUV"
  },
  {
    "year": 2016,
    "manufacturer_name": "smart",
    "model_name": "fortwo",
    "car_type": "Hatchback"
  },
  {
    "year": 2016,
    "manufacturer_name": "Rolls-Royce",
    "model_name": "Ghost",
    "car_type": "Sedan"
  },
  {
    "year": 2016,
    "manufacturer_name": "Subaru",
    "model_name": "Legacy",
    "car_type": "Sedan"
  },
  {
    "year": 2016,
    "manufacturer_name": "Scion",
    "model_name": "iM",
    "car_type": "Hatchback"
  },
  {
    "year": 2016,
    "manufacturer_name": "Scion",
    "model_name": "FR-S",
    "car_type": "Coupe"
  },
  {
    "year": 2016,
    "manufacturer_name": "Toyota",
    "model_name": "Corolla",
    "car_type": "Sedan"
  },
  {
    "year": 2016,
    "manufacturer_name": "Tesla",
    "model_name": "Model X",
    "car_type": "SUV"
  },
  {
    "year": 2016,
    "manufacturer_name": "Subaru",
    "model_name": "Crosstrek",
    "car_type": "SUV"
  },
  {
    "year": 2016,
    "manufacturer_name": "Toyota",
    "model_name": "Prius c",
    "car_type": "Hatchback"
  },
  {
    "year": 2016,
    "manufacturer_name": "Subaru",
    "model_name": "Outback",
    "car_type": "SUV"
  },
  {
    "year": 2016,
    "manufacturer_name": "Toyota",
    "model_name": "Avalon",
    "car_type": "Sedan"
  },
  {
    "year": 2016,
    "manufacturer_name": "Toyota",
    "model_name": "Highlander",
    "car_type": "SUV"
  },
  {
    "year": 2016,
    "manufacturer_name": "Toyota",
    "model_name": "Mirai",
    "car_type": "Sedan"
  },
  {
    "year": 2016,
    "manufacturer_name": "Toyota",
    "model_name": "Land Cruiser",
    "car_type": "SUV"
  },
  {
    "year": 2016,
    "manufacturer_name": "Toyota",
    "model_name": "4Runner",
    "car_type": "SUV"
  },
  {
    "year": 2016,
    "manufacturer_name": "Toyota",
    "model_name": "Prius",
    "car_type": "Hatchback"
  },
  {
    "year": 2016,
    "manufacturer_name": "Toyota",
    "model_name": "Prius v",
    "car_type": "Wagon"
  },
  {
    "year": 2016,
    "manufacturer_name": "Toyota",
    "model_name": "RAV4",
    "car_type": "SUV"
  },
  {
    "year": 2016,
    "manufacturer_name": "Toyota",
    "model_name": "Sequoia",
    "car_type": "SUV"
  },
  {
    "year": 2016,
    "manufacturer_name": "Toyota",
    "model_name": "Camry",
    "car_type": "Sedan"
  },
  {
    "year": 2016,
    "manufacturer_name": "Toyota",
    "model_name": "Sienna",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2016,
    "manufacturer_name": "Toyota",
    "model_name": "Tacoma Access Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2016,
    "manufacturer_name": "Toyota",
    "model_name": "Tundra Double Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2016,
    "manufacturer_name": "Toyota",
    "model_name": "Tundra CrewMax",
    "car_type": "Pickup"
  },
  {
    "year": 2016,
    "manufacturer_name": "Toyota",
    "model_name": "Tacoma Double Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2016,
    "manufacturer_name": "Volkswagen",
    "model_name": "Beetle",
    "car_type": "Hatchback, Convertible"
  },
  {
    "year": 2016,
    "manufacturer_name": "Volkswagen",
    "model_name": "e-Golf",
    "car_type": "Hatchback"
  },
  {
    "year": 2016,
    "manufacturer_name": "Toyota",
    "model_name": "Yaris",
    "car_type": "Hatchback"
  },
  {
    "year": 2016,
    "manufacturer_name": "Toyota",
    "model_name": "Tundra Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2016,
    "manufacturer_name": "Volkswagen",
    "model_name": "CC",
    "car_type": "Sedan"
  },
  {
    "year": 2016,
    "manufacturer_name": "Volkswagen",
    "model_name": "Golf",
    "car_type": "Hatchback"
  },
  {
    "year": 2016,
    "manufacturer_name": "Volkswagen",
    "model_name": "Golf GTI",
    "car_type": "Hatchback"
  },
  {
    "year": 2016,
    "manufacturer_name": "Volkswagen",
    "model_name": "Golf SportWagen",
    "car_type": "Wagon"
  },
  {
    "year": 2016,
    "manufacturer_name": "Volkswagen",
    "model_name": "Golf R",
    "car_type": "Hatchback"
  },
  {
    "year": 2016,
    "manufacturer_name": "Volkswagen",
    "model_name": "Passat",
    "car_type": "Sedan"
  },
  {
    "year": 2016,
    "manufacturer_name": "Volkswagen",
    "model_name": "Eos",
    "car_type": "Convertible"
  },
  {
    "year": 2016,
    "manufacturer_name": "Volkswagen",
    "model_name": "Tiguan",
    "car_type": "SUV"
  },
  {
    "year": 2016,
    "manufacturer_name": "Volkswagen",
    "model_name": "Jetta",
    "car_type": "Sedan"
  },
  {
    "year": 2015,
    "manufacturer_name": "Aston Martin",
    "model_name": "DB9",
    "car_type": "Coupe, Convertible"
  },
  {
    "year": 2016,
    "manufacturer_name": "Volvo",
    "model_name": "XC90",
    "car_type": "SUV"
  },
  {
    "year": 2016,
    "manufacturer_name": "Volvo",
    "model_name": "S80",
    "car_type": "Sedan"
  },
  {
    "year": 2016,
    "manufacturer_name": "Volvo",
    "model_name": "S60",
    "car_type": "Sedan"
  },
  {
    "year": 2015,
    "manufacturer_name": "Acura",
    "model_name": "TLX",
    "car_type": "Sedan"
  },
  {
    "year": 2016,
    "manufacturer_name": "Volkswagen",
    "model_name": "Touareg",
    "car_type": "SUV"
  },
  {
    "year": 2016,
    "manufacturer_name": "Volvo",
    "model_name": "XC60",
    "car_type": "SUV"
  },
  {
    "year": 2015,
    "manufacturer_name": "Acura",
    "model_name": "MDX",
    "car_type": "SUV"
  },
  {
    "year": 2016,
    "manufacturer_name": "Volvo",
    "model_name": "V60",
    "car_type": "Wagon"
  },
  {
    "year": 2016,
    "manufacturer_name": "Volvo",
    "model_name": "XC70",
    "car_type": "Wagon"
  },
  {
    "year": 2015,
    "manufacturer_name": "Acura",
    "model_name": "RLX",
    "car_type": "Sedan"
  },
  {
    "year": 2015,
    "manufacturer_name": "Acura",
    "model_name": "RDX",
    "car_type": "SUV"
  },
  {
    "year": 2015,
    "manufacturer_name": "Alfa Romeo",
    "model_name": "4C Spider",
    "car_type": "Convertible"
  },
  {
    "year": 2015,
    "manufacturer_name": "Audi",
    "model_name": "A6",
    "car_type": "Sedan"
  },
  {
    "year": 2015,
    "manufacturer_name": "Audi",
    "model_name": "A4",
    "car_type": "Sedan"
  },
  {
    "year": 2015,
    "manufacturer_name": "Audi",
    "model_name": "allroad",
    "car_type": "Wagon"
  },
  {
    "year": 2015,
    "manufacturer_name": "Aston Martin",
    "model_name": "Rapide S",
    "car_type": "Sedan"
  },
  {
    "year": 2015,
    "manufacturer_name": "Audi",
    "model_name": "A3",
    "car_type": "Sedan, Convertible"
  },
  {
    "year": 2015,
    "manufacturer_name": "Alfa Romeo",
    "model_name": "4C",
    "car_type": "Coupe"
  },
  {
    "year": 2015,
    "manufacturer_name": "Audi",
    "model_name": "A8",
    "car_type": "Sedan"
  },
  {
    "year": 2015,
    "manufacturer_name": "Aston Martin",
    "model_name": "Vanquish",
    "car_type": "Coupe, Convertible"
  },
  {
    "year": 2015,
    "manufacturer_name": "Acura",
    "model_name": "ILX",
    "car_type": "Sedan"
  },
  {
    "year": 2015,
    "manufacturer_name": "Audi",
    "model_name": "Q5",
    "car_type": "SUV"
  },
  {
    "year": 2015,
    "manufacturer_name": "Aston Martin",
    "model_name": "Vantage",
    "car_type": "Coupe, Convertible"
  },
  {
    "year": 2015,
    "manufacturer_name": "Audi",
    "model_name": "RS 5",
    "car_type": "Coupe, Convertible"
  },
  {
    "year": 2015,
    "manufacturer_name": "Audi",
    "model_name": "A5",
    "car_type": "Coupe, Convertible"
  },
  {
    "year": 2015,
    "manufacturer_name": "Audi",
    "model_name": "A7",
    "car_type": "Sedan"
  },
  {
    "year": 2015,
    "manufacturer_name": "Audi",
    "model_name": "R8",
    "car_type": "Coupe, Convertible"
  },
  {
    "year": 2015,
    "manufacturer_name": "Audi",
    "model_name": "S3",
    "car_type": "Sedan"
  },
  {
    "year": 2015,
    "manufacturer_name": "Audi",
    "model_name": "S5",
    "car_type": "Coupe, Convertible"
  },
  {
    "year": 2015,
    "manufacturer_name": "BMW",
    "model_name": "3 Series",
    "car_type": "Sedan, Wagon"
  },
  {
    "year": 2015,
    "manufacturer_name": "Audi",
    "model_name": "TT",
    "car_type": "Coupe, Convertible"
  },
  {
    "year": 2015,
    "manufacturer_name": "Audi",
    "model_name": "S4",
    "car_type": "Sedan"
  },
  {
    "year": 2015,
    "manufacturer_name": "Audi",
    "model_name": "S8",
    "car_type": "Sedan"
  },
  {
    "year": 2015,
    "manufacturer_name": "Audi",
    "model_name": "S6",
    "car_type": "Sedan"
  },
  {
    "year": 2015,
    "manufacturer_name": "BMW",
    "model_name": "6 Series",
    "car_type": "Coupe, Sedan, Convertible"
  },
  {
    "year": 2015,
    "manufacturer_name": "Bentley",
    "model_name": "Mulsanne",
    "car_type": "Sedan"
  },
  {
    "year": 2015,
    "manufacturer_name": "Audi",
    "model_name": "Q3",
    "car_type": "SUV"
  },
  {
    "year": 2015,
    "manufacturer_name": "Audi",
    "model_name": "Q7",
    "car_type": "SUV"
  },
  {
    "year": 2015,
    "manufacturer_name": "Audi",
    "model_name": "RS 7",
    "car_type": "Sedan"
  },
  {
    "year": 2015,
    "manufacturer_name": "Bentley",
    "model_name": "Continental",
    "car_type": "Coupe, Convertible"
  },
  {
    "year": 2015,
    "manufacturer_name": "Audi",
    "model_name": "SQ5",
    "car_type": "SUV"
  },
  {
    "year": 2015,
    "manufacturer_name": "BMW",
    "model_name": "4 Series",
    "car_type": "Coupe, Convertible"
  },
  {
    "year": 2015,
    "manufacturer_name": "Audi",
    "model_name": "S7",
    "car_type": "Sedan"
  },
  {
    "year": 2015,
    "manufacturer_name": "BMW",
    "model_name": "i8",
    "car_type": "Coupe"
  },
  {
    "year": 2015,
    "manufacturer_name": "BMW",
    "model_name": "i3",
    "car_type": "Hatchback"
  },
  {
    "year": 2015,
    "manufacturer_name": "BMW",
    "model_name": "X3",
    "car_type": "SUV"
  },
  {
    "year": 2015,
    "manufacturer_name": "Buick",
    "model_name": "Encore",
    "car_type": "SUV"
  },
  {
    "year": 2015,
    "manufacturer_name": "BMW",
    "model_name": "2 Series",
    "car_type": "Coupe, Convertible"
  },
  {
    "year": 2015,
    "manufacturer_name": "BMW",
    "model_name": "7 Series",
    "car_type": "Sedan"
  },
  {
    "year": 2015,
    "manufacturer_name": "Buick",
    "model_name": "LaCrosse",
    "car_type": "Sedan"
  },
  {
    "year": 2015,
    "manufacturer_name": "BMW",
    "model_name": "X1",
    "car_type": "SUV"
  },
  {
    "year": 2015,
    "manufacturer_name": "BMW",
    "model_name": "5 Series",
    "car_type": "Sedan"
  },
  {
    "year": 2015,
    "manufacturer_name": "BMW",
    "model_name": "M5",
    "car_type": "Sedan"
  },
  {
    "year": 2015,
    "manufacturer_name": "Bentley",
    "model_name": "Flying Spur",
    "car_type": "Sedan"
  },
  {
    "year": 2015,
    "manufacturer_name": "BMW",
    "model_name": "X5",
    "car_type": "SUV"
  },
  {
    "year": 2015,
    "manufacturer_name": "BMW",
    "model_name": "M4",
    "car_type": "Coupe, Convertible"
  },
  {
    "year": 2015,
    "manufacturer_name": "BMW",
    "model_name": "M6",
    "car_type": "Coupe, Convertible"
  },
  {
    "year": 2015,
    "manufacturer_name": "BMW",
    "model_name": "Z4",
    "car_type": "Convertible"
  },
  {
    "year": 2015,
    "manufacturer_name": "Buick",
    "model_name": "Verano",
    "car_type": "Sedan"
  },
  {
    "year": 2015,
    "manufacturer_name": "BMW",
    "model_name": "M3",
    "car_type": "Sedan"
  },
  {
    "year": 2015,
    "manufacturer_name": "Cadillac",
    "model_name": "Escalade",
    "car_type": "SUV"
  },
  {
    "year": 2015,
    "manufacturer_name": "Cadillac",
    "model_name": "CTS",
    "car_type": "Sedan, Coupe"
  },
  {
    "year": 2015,
    "manufacturer_name": "Cadillac",
    "model_name": "SRX",
    "car_type": "SUV"
  },
  {
    "year": 2015,
    "manufacturer_name": "BMW",
    "model_name": "X6 M",
    "car_type": "SUV"
  },
  {
    "year": 2015,
    "manufacturer_name": "BMW",
    "model_name": "X5 M",
    "car_type": "SUV"
  },
  {
    "year": 2015,
    "manufacturer_name": "BMW",
    "model_name": "X4",
    "car_type": "SUV"
  },
  {
    "year": 2015,
    "manufacturer_name": "Chevrolet",
    "model_name": "Colorado Crew Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2015,
    "manufacturer_name": "BMW",
    "model_name": "X6",
    "car_type": "SUV"
  },
  {
    "year": 2015,
    "manufacturer_name": "Chevrolet",
    "model_name": "Captiva Sport",
    "car_type": "SUV"
  },
  {
    "year": 2015,
    "manufacturer_name": "Chevrolet",
    "model_name": "Camaro",
    "car_type": "Convertible, Coupe"
  },
  {
    "year": 2015,
    "manufacturer_name": "Buick",
    "model_name": "Enclave",
    "car_type": "SUV"
  },
  {
    "year": 2015,
    "manufacturer_name": "Buick",
    "model_name": "Regal",
    "car_type": "Sedan"
  },
  {
    "year": 2015,
    "manufacturer_name": "Chevrolet",
    "model_name": "Cruze",
    "car_type": "Sedan"
  },
  {
    "year": 2015,
    "manufacturer_name": "Chevrolet",
    "model_name": "Corvette",
    "car_type": "Convertible, Coupe"
  },
  {
    "year": 2015,
    "manufacturer_name": "Chevrolet",
    "model_name": "City Express",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2015,
    "manufacturer_name": "Cadillac",
    "model_name": "Escalade ESV",
    "car_type": "SUV"
  },
  {
    "year": 2015,
    "manufacturer_name": "Chevrolet",
    "model_name": "Colorado Extended Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2015,
    "manufacturer_name": "Cadillac",
    "model_name": "XTS",
    "car_type": "Sedan"
  },
  {
    "year": 2015,
    "manufacturer_name": "Chevrolet",
    "model_name": "Express 2500 Cargo",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2015,
    "manufacturer_name": "Cadillac",
    "model_name": "ATS",
    "car_type": "Sedan, Coupe"
  },
  {
    "year": 2015,
    "manufacturer_name": "Chevrolet",
    "model_name": "Equinox",
    "car_type": "SUV"
  },
  {
    "year": 2015,
    "manufacturer_name": "Chevrolet",
    "model_name": "Impala Limited",
    "car_type": "Sedan"
  },
  {
    "year": 2015,
    "manufacturer_name": "Chevrolet",
    "model_name": "Express 3500 Cargo",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2015,
    "manufacturer_name": "Chevrolet",
    "model_name": "Express 3500 Passenger",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2015,
    "manufacturer_name": "Chevrolet",
    "model_name": "Malibu",
    "car_type": "Sedan"
  },
  {
    "year": 2015,
    "manufacturer_name": "Chevrolet",
    "model_name": "Express 2500 Passenger",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2015,
    "manufacturer_name": "Chevrolet",
    "model_name": "Silverado 1500 Crew Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2015,
    "manufacturer_name": "Chevrolet",
    "model_name": "Impala",
    "car_type": "Sedan"
  },
  {
    "year": 2015,
    "manufacturer_name": "Chevrolet",
    "model_name": "Silverado 1500 Double Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2015,
    "manufacturer_name": "Chevrolet",
    "model_name": "Volt",
    "car_type": "Sedan"
  },
  {
    "year": 2015,
    "manufacturer_name": "Chevrolet",
    "model_name": "Silverado 3500 HD Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2015,
    "manufacturer_name": "Chevrolet",
    "model_name": "Silverado 2500 HD Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2015,
    "manufacturer_name": "Chevrolet",
    "model_name": "SS",
    "car_type": "Sedan"
  },
  {
    "year": 2015,
    "manufacturer_name": "Chevrolet",
    "model_name": "Spark EV",
    "car_type": "Hatchback"
  },
  {
    "year": 2015,
    "manufacturer_name": "Chevrolet",
    "model_name": "Silverado 1500 Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2015,
    "manufacturer_name": "Chevrolet",
    "model_name": "Sonic",
    "car_type": "Sedan, Hatchback"
  },
  {
    "year": 2015,
    "manufacturer_name": "Chevrolet",
    "model_name": "Silverado 3500 HD Crew Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2015,
    "manufacturer_name": "Chevrolet",
    "model_name": "Spark",
    "car_type": "Hatchback"
  },
  {
    "year": 2015,
    "manufacturer_name": "Chevrolet",
    "model_name": "Silverado 2500 HD Double Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2015,
    "manufacturer_name": "Chevrolet",
    "model_name": "Silverado 2500 HD Crew Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2015,
    "manufacturer_name": "Chrysler",
    "model_name": "200",
    "car_type": "Sedan"
  },
  {
    "year": 2015,
    "manufacturer_name": "Chevrolet",
    "model_name": "Silverado 3500 HD Double Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2015,
    "manufacturer_name": "Chevrolet",
    "model_name": "Suburban",
    "car_type": "SUV"
  },
  {
    "year": 2015,
    "manufacturer_name": "Chevrolet",
    "model_name": "Traverse",
    "car_type": "SUV"
  },
  {
    "year": 2015,
    "manufacturer_name": "Ferrari",
    "model_name": "California",
    "car_type": "Convertible"
  },
  {
    "year": 2015,
    "manufacturer_name": "Dodge",
    "model_name": "Challenger",
    "car_type": "Coupe"
  },
  {
    "year": 2015,
    "manufacturer_name": "Dodge",
    "model_name": "Dart",
    "car_type": "Sedan"
  },
  {
    "year": 2015,
    "manufacturer_name": "Chrysler",
    "model_name": "Town & Country",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2015,
    "manufacturer_name": "Chevrolet",
    "model_name": "Tahoe",
    "car_type": "SUV"
  },
  {
    "year": 2015,
    "manufacturer_name": "Dodge",
    "model_name": "Charger",
    "car_type": "Sedan"
  },
  {
    "year": 2015,
    "manufacturer_name": "Dodge",
    "model_name": "Journey",
    "car_type": "SUV"
  },
  {
    "year": 2015,
    "manufacturer_name": "Dodge",
    "model_name": "Durango",
    "car_type": "SUV"
  },
  {
    "year": 2015,
    "manufacturer_name": "Ferrari",
    "model_name": "458 Italia",
    "car_type": "Coupe"
  },
  {
    "year": 2015,
    "manufacturer_name": "Dodge",
    "model_name": "Viper",
    "car_type": "Coupe"
  },
  {
    "year": 2015,
    "manufacturer_name": "Chevrolet",
    "model_name": "Trax",
    "car_type": "SUV"
  },
  {
    "year": 2015,
    "manufacturer_name": "Chrysler",
    "model_name": "300",
    "car_type": "Sedan"
  },
  {
    "year": 2015,
    "manufacturer_name": "Dodge",
    "model_name": "Grand Caravan Passenger",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2015,
    "manufacturer_name": "Ferrari",
    "model_name": "F12berlinetta",
    "car_type": "Coupe"
  },
  {
    "year": 2015,
    "manufacturer_name": "Ferrari",
    "model_name": "458 Speciale",
    "car_type": "Coupe"
  },
  {
    "year": 2015,
    "manufacturer_name": "Ferrari",
    "model_name": "458 Spider",
    "car_type": "Convertible"
  },
  {
    "year": 2015,
    "manufacturer_name": "Ferrari",
    "model_name": "FF",
    "car_type": "Coupe"
  },
  {
    "year": 2015,
    "manufacturer_name": "Ford",
    "model_name": "Expedition",
    "car_type": "SUV"
  },
  {
    "year": 2015,
    "manufacturer_name": "FIAT",
    "model_name": "500L",
    "car_type": "Hatchback"
  },
  {
    "year": 2015,
    "manufacturer_name": "FIAT",
    "model_name": "500c",
    "car_type": "Convertible"
  },
  {
    "year": 2015,
    "manufacturer_name": "Ford",
    "model_name": "C-MAX Hybrid",
    "car_type": "Wagon"
  },
  {
    "year": 2015,
    "manufacturer_name": "Ford",
    "model_name": "F150 SuperCrew Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2015,
    "manufacturer_name": "Ford",
    "model_name": "F250 Super Duty Super Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2015,
    "manufacturer_name": "Ford",
    "model_name": "Edge",
    "car_type": "SUV"
  },
  {
    "year": 2015,
    "manufacturer_name": "Ford",
    "model_name": "C-MAX Energi",
    "car_type": "Wagon"
  },
  {
    "year": 2015,
    "manufacturer_name": "Ford",
    "model_name": "F350 Super Duty Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2015,
    "manufacturer_name": "Ford",
    "model_name": "F250 Super Duty Crew Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2015,
    "manufacturer_name": "Ford",
    "model_name": "Expedition EL",
    "car_type": "SUV"
  },
  {
    "year": 2015,
    "manufacturer_name": "Ford",
    "model_name": "F350 Super Duty Crew Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2015,
    "manufacturer_name": "FIAT",
    "model_name": "500",
    "car_type": "Hatchback"
  },
  {
    "year": 2015,
    "manufacturer_name": "Ford",
    "model_name": "Explorer",
    "car_type": "SUV"
  },
  {
    "year": 2015,
    "manufacturer_name": "FIAT",
    "model_name": "500 Abarth",
    "car_type": "Hatchback, Convertible"
  },
  {
    "year": 2015,
    "manufacturer_name": "FIAT",
    "model_name": "500e",
    "car_type": "Hatchback"
  },
  {
    "year": 2015,
    "manufacturer_name": "Ford",
    "model_name": "Escape",
    "car_type": "SUV"
  },
  {
    "year": 2015,
    "manufacturer_name": "Ford",
    "model_name": "Focus",
    "car_type": "Sedan, Hatchback"
  },
  {
    "year": 2015,
    "manufacturer_name": "Ford",
    "model_name": "F150 Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2015,
    "manufacturer_name": "Ford",
    "model_name": "F150 Super Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2015,
    "manufacturer_name": "Ford",
    "model_name": "F250 Super Duty Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2015,
    "manufacturer_name": "GMC",
    "model_name": "Canyon Extended Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2015,
    "manufacturer_name": "Freightliner",
    "model_name": "Sprinter 3500 Cargo",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2015,
    "manufacturer_name": "Ford",
    "model_name": "Fiesta",
    "car_type": "Sedan, Hatchback"
  },
  {
    "year": 2015,
    "manufacturer_name": "Ford",
    "model_name": "F450 Super Duty Crew Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2015,
    "manufacturer_name": "Ford",
    "model_name": "Mustang",
    "car_type": "Coupe, Convertible"
  },
  {
    "year": 2015,
    "manufacturer_name": "Ford",
    "model_name": "Transit Connect Passenger",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2015,
    "manufacturer_name": "Ford",
    "model_name": "F350 Super Duty Super Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2015,
    "manufacturer_name": "Ford",
    "model_name": "Fusion",
    "car_type": "Sedan"
  },
  {
    "year": 2015,
    "manufacturer_name": "Ford",
    "model_name": "Transit 150 Van",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2015,
    "manufacturer_name": "Ford",
    "model_name": "Flex",
    "car_type": "SUV"
  },
  {
    "year": 2015,
    "manufacturer_name": "Ford",
    "model_name": "Taurus",
    "car_type": "Sedan"
  },
  {
    "year": 2015,
    "manufacturer_name": "Freightliner",
    "model_name": "Sprinter 2500 Crew",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2015,
    "manufacturer_name": "Ford",
    "model_name": "Focus ST",
    "car_type": "Hatchback"
  },
  {
    "year": 2015,
    "manufacturer_name": "GMC",
    "model_name": "Sierra 1500 Crew Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2015,
    "manufacturer_name": "Ford",
    "model_name": "Transit 350 HD Van",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2015,
    "manufacturer_name": "Ford",
    "model_name": "Transit Connect Cargo",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2015,
    "manufacturer_name": "Ford",
    "model_name": "Transit 150 Wagon",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2015,
    "manufacturer_name": "Ford",
    "model_name": "Transit 350 Wagon",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2015,
    "manufacturer_name": "GMC",
    "model_name": "Canyon Crew Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2015,
    "manufacturer_name": "Ford",
    "model_name": "Fusion Energi",
    "car_type": "Sedan"
  },
  {
    "year": 2015,
    "manufacturer_name": "Freightliner",
    "model_name": "Sprinter 2500 Cargo",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2015,
    "manufacturer_name": "Ford",
    "model_name": "Transit 350 Van",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2015,
    "manufacturer_name": "Ford",
    "model_name": "Transit 250 Van",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2015,
    "manufacturer_name": "GMC",
    "model_name": "Acadia",
    "car_type": "SUV"
  },
  {
    "year": 2015,
    "manufacturer_name": "GMC",
    "model_name": "Sierra 3500 HD Double Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2015,
    "manufacturer_name": "GMC",
    "model_name": "Sierra 2500 HD Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2015,
    "manufacturer_name": "GMC",
    "model_name": "Sierra 2500 HD Crew Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2015,
    "manufacturer_name": "GMC",
    "model_name": "Yukon",
    "car_type": "SUV"
  },
  {
    "year": 2015,
    "manufacturer_name": "GMC",
    "model_name": "Sierra 3500 HD Crew Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2015,
    "manufacturer_name": "GMC",
    "model_name": "Terrain",
    "car_type": "SUV"
  },
  {
    "year": 2015,
    "manufacturer_name": "GMC",
    "model_name": "Savana 3500 Passenger",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2015,
    "manufacturer_name": "GMC",
    "model_name": "Savana 3500 Cargo",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2015,
    "manufacturer_name": "GMC",
    "model_name": "Sierra 1500 Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2015,
    "manufacturer_name": "GMC",
    "model_name": "Savana 2500 Passenger",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2015,
    "manufacturer_name": "Freightliner",
    "model_name": "Sprinter 2500 Passenger",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2015,
    "manufacturer_name": "GMC",
    "model_name": "Sierra 1500 Double Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2015,
    "manufacturer_name": "GMC",
    "model_name": "Savana 2500 Cargo",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2015,
    "manufacturer_name": "GMC",
    "model_name": "Sierra 2500 HD Double Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2015,
    "manufacturer_name": "GMC",
    "model_name": "Sierra 3500 HD Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2015,
    "manufacturer_name": "Honda",
    "model_name": "Crosstour",
    "car_type": "SUV"
  },
  {
    "year": 2015,
    "manufacturer_name": "GMC",
    "model_name": "Yukon XL",
    "car_type": "SUV"
  },
  {
    "year": 2015,
    "manufacturer_name": "Honda",
    "model_name": "CR-Z",
    "car_type": "Coupe"
  },
  {
    "year": 2015,
    "manufacturer_name": "Honda",
    "model_name": "Civic",
    "car_type": "Sedan, Coupe"
  },
  {
    "year": 2015,
    "manufacturer_name": "Honda",
    "model_name": "Accord Hybrid",
    "car_type": "Sedan"
  },
  {
    "year": 2015,
    "manufacturer_name": "Honda",
    "model_name": "Accord",
    "car_type": "Sedan, Coupe"
  },
  {
    "year": 2015,
    "manufacturer_name": "Honda",
    "model_name": "Fit",
    "car_type": "Hatchback"
  },
  {
    "year": 2015,
    "manufacturer_name": "Honda",
    "model_name": "Odyssey",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2015,
    "manufacturer_name": "Honda",
    "model_name": "Pilot",
    "car_type": "SUV"
  },
  {
    "year": 2015,
    "manufacturer_name": "Honda",
    "model_name": "CR-V",
    "car_type": "SUV"
  },
  {
    "year": 2015,
    "manufacturer_name": "Hyundai",
    "model_name": "Azera",
    "car_type": "Sedan"
  },
  {
    "year": 2015,
    "manufacturer_name": "Hyundai",
    "model_name": "Elantra GT",
    "car_type": "Hatchback"
  },
  {
    "year": 2015,
    "manufacturer_name": "Hyundai",
    "model_name": "Equus",
    "car_type": "Sedan"
  },
  {
    "year": 2015,
    "manufacturer_name": "Hyundai",
    "model_name": "Accent",
    "car_type": "Sedan, Hatchback"
  },
  {
    "year": 2015,
    "manufacturer_name": "Hyundai",
    "model_name": "Elantra",
    "car_type": "Sedan"
  },
  {
    "year": 2015,
    "manufacturer_name": "Hyundai",
    "model_name": "Genesis Coupe",
    "car_type": "Coupe"
  },
  {
    "year": 2015,
    "manufacturer_name": "Hyundai",
    "model_name": "Sonata",
    "car_type": "Sedan"
  },
  {
    "year": 2015,
    "manufacturer_name": "INFINITI",
    "model_name": "Q50",
    "car_type": "Sedan"
  },
  {
    "year": 2015,
    "manufacturer_name": "INFINITI",
    "model_name": "Q40",
    "car_type": "Sedan"
  },
  {
    "year": 2015,
    "manufacturer_name": "INFINITI",
    "model_name": "QX70",
    "car_type": "SUV"
  },
  {
    "year": 2015,
    "manufacturer_name": "Lamborghini",
    "model_name": "Aventador",
    "car_type": "Coupe, Convertible"
  },
  {
    "year": 2015,
    "manufacturer_name": "Hyundai",
    "model_name": "Tucson Fuel Cell",
    "car_type": "SUV"
  },
  {
    "year": 2015,
    "manufacturer_name": "Hyundai",
    "model_name": "Santa Fe",
    "car_type": "SUV"
  },
  {
    "year": 2015,
    "manufacturer_name": "Hyundai",
    "model_name": "Tucson",
    "car_type": "SUV"
  },
  {
    "year": 2015,
    "manufacturer_name": "Hyundai",
    "model_name": "Santa Fe Sport",
    "car_type": "SUV"
  },
  {
    "year": 2015,
    "manufacturer_name": "Hyundai",
    "model_name": "Veloster",
    "car_type": "Coupe"
  },
  {
    "year": 2015,
    "manufacturer_name": "Jeep",
    "model_name": "Renegade",
    "car_type": "SUV"
  },
  {
    "year": 2015,
    "manufacturer_name": "Jaguar",
    "model_name": "XK",
    "car_type": "Coupe, Convertible"
  },
  {
    "year": 2015,
    "manufacturer_name": "INFINITI",
    "model_name": "Q70",
    "car_type": "Sedan"
  },
  {
    "year": 2015,
    "manufacturer_name": "Hyundai",
    "model_name": "Genesis",
    "car_type": "Sedan"
  },
  {
    "year": 2015,
    "manufacturer_name": "Kia",
    "model_name": "Forte5",
    "car_type": "Hatchback"
  },
  {
    "year": 2015,
    "manufacturer_name": "INFINITI",
    "model_name": "QX60",
    "car_type": "SUV"
  },
  {
    "year": 2015,
    "manufacturer_name": "Kia",
    "model_name": "Sedona",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2015,
    "manufacturer_name": "Land Rover",
    "model_name": "Range Rover",
    "car_type": "SUV"
  },
  {
    "year": 2015,
    "manufacturer_name": "Lexus",
    "model_name": "GS",
    "car_type": "Sedan"
  },
  {
    "year": 2015,
    "manufacturer_name": "Jaguar",
    "model_name": "F-TYPE",
    "car_type": "Coupe, Convertible"
  },
  {
    "year": 2015,
    "manufacturer_name": "Lexus",
    "model_name": "NX",
    "car_type": "SUV"
  },
  {
    "year": 2015,
    "manufacturer_name": "Kia",
    "model_name": "K900",
    "car_type": "Sedan"
  },
  {
    "year": 2015,
    "manufacturer_name": "INFINITI",
    "model_name": "Q60",
    "car_type": "Coupe, Convertible"
  },
  {
    "year": 2015,
    "manufacturer_name": "Kia",
    "model_name": "Optima",
    "car_type": "Sedan"
  },
  {
    "year": 2015,
    "manufacturer_name": "Kia",
    "model_name": "Soul",
    "car_type": "Wagon"
  },
  {
    "year": 2015,
    "manufacturer_name": "Maserati",
    "model_name": "Ghibli",
    "car_type": "Sedan"
  },
  {
    "year": 2015,
    "manufacturer_name": "Lincoln",
    "model_name": "MKT",
    "car_type": "SUV"
  },
  {
    "year": 2015,
    "manufacturer_name": "Jeep",
    "model_name": "Patriot",
    "car_type": "SUV"
  },
  {
    "year": 2015,
    "manufacturer_name": "Jaguar",
    "model_name": "XF",
    "car_type": "Sedan"
  },
  {
    "year": 2015,
    "manufacturer_name": "Kia",
    "model_name": "Sorento",
    "car_type": "SUV"
  },
  {
    "year": 2015,
    "manufacturer_name": "Jeep",
    "model_name": "Wrangler",
    "car_type": "SUV"
  },
  {
    "year": 2015,
    "manufacturer_name": "INFINITI",
    "model_name": "QX50",
    "car_type": "SUV"
  },
  {
    "year": 2015,
    "manufacturer_name": "Kia",
    "model_name": "Cadenza",
    "car_type": "Sedan"
  },
  {
    "year": 2015,
    "manufacturer_name": "Jaguar",
    "model_name": "XJ",
    "car_type": "Sedan"
  },
  {
    "year": 2015,
    "manufacturer_name": "INFINITI",
    "model_name": "QX80",
    "car_type": "SUV"
  },
  {
    "year": 2015,
    "manufacturer_name": "Kia",
    "model_name": "Optima Hybrid",
    "car_type": "Sedan"
  },
  {
    "year": 2015,
    "manufacturer_name": "Kia",
    "model_name": "Rio",
    "car_type": "Sedan, Hatchback"
  },
  {
    "year": 2015,
    "manufacturer_name": "Jeep",
    "model_name": "Grand Cherokee",
    "car_type": "SUV"
  },
  {
    "year": 2015,
    "manufacturer_name": "Jeep",
    "model_name": "Compass",
    "car_type": "SUV"
  },
  {
    "year": 2015,
    "manufacturer_name": "Mercedes-Benz",
    "model_name": "B-Class",
    "car_type": "Hatchback"
  },
  {
    "year": 2015,
    "manufacturer_name": "Kia",
    "model_name": "Forte Koup",
    "car_type": "Coupe"
  },
  {
    "year": 2015,
    "manufacturer_name": "Jeep",
    "model_name": "Cherokee",
    "car_type": "SUV"
  },
  {
    "year": 2015,
    "manufacturer_name": "MAZDA",
    "model_name": "MAZDA3",
    "car_type": "Sedan, Hatchback"
  },
  {
    "year": 2015,
    "manufacturer_name": "Kia",
    "model_name": "Forte",
    "car_type": "Sedan"
  },
  {
    "year": 2015,
    "manufacturer_name": "Mercedes-Benz",
    "model_name": "G-Class",
    "car_type": "SUV"
  },
  {
    "year": 2015,
    "manufacturer_name": "Land Rover",
    "model_name": "LR4",
    "car_type": "SUV"
  },
  {
    "year": 2015,
    "manufacturer_name": "Land Rover",
    "model_name": "LR2",
    "car_type": "SUV"
  },
  {
    "year": 2015,
    "manufacturer_name": "Kia",
    "model_name": "Sportage",
    "car_type": "SUV"
  },
  {
    "year": 2015,
    "manufacturer_name": "Lamborghini",
    "model_name": "Huracan",
    "car_type": "Coupe"
  },
  {
    "year": 2015,
    "manufacturer_name": "Land Rover",
    "model_name": "Range Rover Sport",
    "car_type": "SUV"
  },
  {
    "year": 2015,
    "manufacturer_name": "Lexus",
    "model_name": "LX",
    "car_type": "SUV"
  },
  {
    "year": 2015,
    "manufacturer_name": "Land Rover",
    "model_name": "Discovery Sport",
    "car_type": "SUV"
  },
  {
    "year": 2015,
    "manufacturer_name": "Kia",
    "model_name": "Soul EV",
    "car_type": "Wagon"
  },
  {
    "year": 2015,
    "manufacturer_name": "Mercedes-Benz",
    "model_name": "S-Class",
    "car_type": "Sedan, Coupe"
  },
  {
    "year": 2015,
    "manufacturer_name": "Lexus",
    "model_name": "GX",
    "car_type": "SUV"
  },
  {
    "year": 2015,
    "manufacturer_name": "Lexus",
    "model_name": "RC",
    "car_type": "Coupe"
  },
  {
    "year": 2015,
    "manufacturer_name": "Land Rover",
    "model_name": "Range Rover Evoque",
    "car_type": "SUV"
  },
  {
    "year": 2015,
    "manufacturer_name": "Lexus",
    "model_name": "ES",
    "car_type": "Sedan"
  },
  {
    "year": 2015,
    "manufacturer_name": "Lexus",
    "model_name": "IS",
    "car_type": "Sedan, Convertible"
  },
  {
    "year": 2015,
    "manufacturer_name": "Lexus",
    "model_name": "RX",
    "car_type": "SUV"
  },
  {
    "year": 2015,
    "manufacturer_name": "Lexus",
    "model_name": "CT",
    "car_type": "Hatchback"
  },
  {
    "year": 2015,
    "manufacturer_name": "MAZDA",
    "model_name": "CX-5",
    "car_type": "SUV"
  },
  {
    "year": 2015,
    "manufacturer_name": "Lincoln",
    "model_name": "MKX",
    "car_type": "SUV"
  },
  {
    "year": 2015,
    "manufacturer_name": "Mercedes-Benz",
    "model_name": "M-Class",
    "car_type": "SUV"
  },
  {
    "year": 2015,
    "manufacturer_name": "Mercedes-Benz",
    "model_name": "CLA-Class",
    "car_type": "Sedan"
  },
  {
    "year": 2015,
    "manufacturer_name": "Lincoln",
    "model_name": "Navigator",
    "car_type": "SUV"
  },
  {
    "year": 2015,
    "manufacturer_name": "MAZDA",
    "model_name": "MAZDA5",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2015,
    "manufacturer_name": "Lincoln",
    "model_name": "Navigator L",
    "car_type": "SUV"
  },
  {
    "year": 2015,
    "manufacturer_name": "Mercedes-Benz",
    "model_name": "C-Class",
    "car_type": "Sedan, Coupe"
  },
  {
    "year": 2015,
    "manufacturer_name": "Lincoln",
    "model_name": "MKZ",
    "car_type": "Sedan"
  },
  {
    "year": 2015,
    "manufacturer_name": "Lincoln",
    "model_name": "MKS",
    "car_type": "Sedan"
  },
  {
    "year": 2015,
    "manufacturer_name": "Maserati",
    "model_name": "Quattroporte",
    "car_type": "Sedan"
  },
  {
    "year": 2015,
    "manufacturer_name": "Mercedes-Benz",
    "model_name": "GL-Class",
    "car_type": "SUV"
  },
  {
    "year": 2015,
    "manufacturer_name": "Mercedes-Benz",
    "model_name": "E-Class",
    "car_type": "Convertible, Wagon, Coupe, Sedan"
  },
  {
    "year": 2015,
    "manufacturer_name": "Lincoln",
    "model_name": "MKC",
    "car_type": "SUV"
  },
  {
    "year": 2015,
    "manufacturer_name": "Lexus",
    "model_name": "LS",
    "car_type": "Sedan"
  },
  {
    "year": 2015,
    "manufacturer_name": "MAZDA",
    "model_name": "MX-5 Miata",
    "car_type": "Convertible"
  },
  {
    "year": 2015,
    "manufacturer_name": "MAZDA",
    "model_name": "CX-9",
    "car_type": "SUV"
  },
  {
    "year": 2015,
    "manufacturer_name": "Mercedes-Benz",
    "model_name": "GLK-Class",
    "car_type": "SUV"
  },
  {
    "year": 2015,
    "manufacturer_name": "MAZDA",
    "model_name": "MAZDA6",
    "car_type": "Sedan"
  },
  {
    "year": 2015,
    "manufacturer_name": "Maserati",
    "model_name": "GranTurismo",
    "car_type": "Coupe, Convertible"
  },
  {
    "year": 2015,
    "manufacturer_name": "McLaren",
    "model_name": "650S",
    "car_type": "Coupe, Convertible"
  },
  {
    "year": 2015,
    "manufacturer_name": "Mercedes-Benz",
    "model_name": "GLA-Class",
    "car_type": "SUV"
  },
  {
    "year": 2015,
    "manufacturer_name": "Mercedes-Benz",
    "model_name": "CLS-Class",
    "car_type": "Sedan"
  },
  {
    "year": 2015,
    "manufacturer_name": "Mercedes-Benz",
    "model_name": "SLS-Class",
    "car_type": "Coupe, Convertible"
  },
  {
    "year": 2015,
    "manufacturer_name": "Mercedes-Benz",
    "model_name": "Sprinter 2500 Passenger",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2015,
    "manufacturer_name": "Mercedes-Benz",
    "model_name": "Sprinter 2500 Crew",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2015,
    "manufacturer_name": "Mercedes-Benz",
    "model_name": "SL-Class",
    "car_type": "Convertible"
  },
  {
    "year": 2015,
    "manufacturer_name": "Mercedes-Benz",
    "model_name": "Sprinter 3500 Cargo",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2015,
    "manufacturer_name": "Mercedes-Benz",
    "model_name": "SLK-Class",
    "car_type": "Convertible"
  },
  {
    "year": 2015,
    "manufacturer_name": "MINI",
    "model_name": "Convertible",
    "car_type": "Convertible"
  },
  {
    "year": 2015,
    "manufacturer_name": "MINI",
    "model_name": "Coupe",
    "car_type": "Coupe"
  },
  {
    "year": 2015,
    "manufacturer_name": "MINI",
    "model_name": "Paceman",
    "car_type": "Hatchback"
  },
  {
    "year": 2015,
    "manufacturer_name": "MINI",
    "model_name": "Hardtop 4 Door",
    "car_type": "Hatchback"
  },
  {
    "year": 2015,
    "manufacturer_name": "Mitsubishi",
    "model_name": "Lancer",
    "car_type": "Sedan"
  },
  {
    "year": 2015,
    "manufacturer_name": "Mercedes-Benz",
    "model_name": "Sprinter 2500 Cargo",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2015,
    "manufacturer_name": "MINI",
    "model_name": "Countryman",
    "car_type": "Hatchback"
  },
  {
    "year": 2015,
    "manufacturer_name": "Nissan",
    "model_name": "NV3500 HD Passenger",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2015,
    "manufacturer_name": "MINI",
    "model_name": "Roadster",
    "car_type": "Convertible"
  },
  {
    "year": 2015,
    "manufacturer_name": "Mitsubishi",
    "model_name": "Outlander",
    "car_type": "SUV"
  },
  {
    "year": 2015,
    "manufacturer_name": "Nissan",
    "model_name": "NV2500 HD Cargo",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2015,
    "manufacturer_name": "Nissan",
    "model_name": "370Z",
    "car_type": "Coupe, Convertible"
  },
  {
    "year": 2015,
    "manufacturer_name": "MINI",
    "model_name": "Hardtop 2 Door",
    "car_type": "Hatchback"
  },
  {
    "year": 2015,
    "manufacturer_name": "Mitsubishi",
    "model_name": "Outlander Sport",
    "car_type": "SUV"
  },
  {
    "year": 2015,
    "manufacturer_name": "Nissan",
    "model_name": "Altima",
    "car_type": "Sedan"
  },
  {
    "year": 2015,
    "manufacturer_name": "Nissan",
    "model_name": "Frontier Crew Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2015,
    "manufacturer_name": "Nissan",
    "model_name": "Titan Crew Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2015,
    "manufacturer_name": "Nissan",
    "model_name": "Murano",
    "car_type": "SUV"
  },
  {
    "year": 2015,
    "manufacturer_name": "Nissan",
    "model_name": "NV1500 Cargo",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2015,
    "manufacturer_name": "Nissan",
    "model_name": "Armada",
    "car_type": "SUV"
  },
  {
    "year": 2015,
    "manufacturer_name": "Nissan",
    "model_name": "LEAF",
    "car_type": "Hatchback"
  },
  {
    "year": 2015,
    "manufacturer_name": "Nissan",
    "model_name": "NV200",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2015,
    "manufacturer_name": "Nissan",
    "model_name": "GT-R",
    "car_type": "Coupe"
  },
  {
    "year": 2015,
    "manufacturer_name": "Mitsubishi",
    "model_name": "Mirage",
    "car_type": "Hatchback"
  },
  {
    "year": 2015,
    "manufacturer_name": "Mitsubishi",
    "model_name": "Lancer Evolution",
    "car_type": "Sedan"
  },
  {
    "year": 2015,
    "manufacturer_name": "Nissan",
    "model_name": "NV200 Taxi",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2015,
    "manufacturer_name": "Ram",
    "model_name": "1500 Crew Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2015,
    "manufacturer_name": "Nissan",
    "model_name": "JUKE",
    "car_type": "SUV"
  },
  {
    "year": 2015,
    "manufacturer_name": "Porsche",
    "model_name": "Boxster",
    "car_type": "Convertible"
  },
  {
    "year": 2015,
    "manufacturer_name": "Nissan",
    "model_name": "Sentra",
    "car_type": "Sedan"
  },
  {
    "year": 2015,
    "manufacturer_name": "Nissan",
    "model_name": "Frontier King Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2015,
    "manufacturer_name": "Nissan",
    "model_name": "Pathfinder",
    "car_type": "SUV"
  },
  {
    "year": 2015,
    "manufacturer_name": "Nissan",
    "model_name": "Rogue Select",
    "car_type": "SUV"
  },
  {
    "year": 2015,
    "manufacturer_name": "Nissan",
    "model_name": "Rogue",
    "car_type": "SUV"
  },
  {
    "year": 2015,
    "manufacturer_name": "Nissan",
    "model_name": "Quest",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2015,
    "manufacturer_name": "Nissan",
    "model_name": "NV3500 HD Cargo",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2015,
    "manufacturer_name": "Nissan",
    "model_name": "Versa",
    "car_type": "Sedan, Hatchback"
  },
  {
    "year": 2015,
    "manufacturer_name": "Porsche",
    "model_name": "Cayenne",
    "car_type": "SUV"
  },
  {
    "year": 2015,
    "manufacturer_name": "Nissan",
    "model_name": "Xterra",
    "car_type": "SUV"
  },
  {
    "year": 2015,
    "manufacturer_name": "Porsche",
    "model_name": "911",
    "car_type": "Coupe, Convertible"
  },
  {
    "year": 2015,
    "manufacturer_name": "Porsche",
    "model_name": "Macan",
    "car_type": "SUV"
  },
  {
    "year": 2015,
    "manufacturer_name": "Ram",
    "model_name": "ProMaster Cargo Van",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2015,
    "manufacturer_name": "Ram",
    "model_name": "2500 Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2015,
    "manufacturer_name": "Rolls-Royce",
    "model_name": "Wraith",
    "car_type": "Coupe"
  },
  {
    "year": 2015,
    "manufacturer_name": "Ram",
    "model_name": "2500 Crew Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2015,
    "manufacturer_name": "Porsche",
    "model_name": "Cayman",
    "car_type": "Coupe"
  },
  {
    "year": 2015,
    "manufacturer_name": "Nissan",
    "model_name": "Titan King Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2015,
    "manufacturer_name": "Ram",
    "model_name": "1500 Quad Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2015,
    "manufacturer_name": "Porsche",
    "model_name": "Panamera",
    "car_type": "Sedan"
  },
  {
    "year": 2015,
    "manufacturer_name": "Ram",
    "model_name": "1500 Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2015,
    "manufacturer_name": "Ram",
    "model_name": "2500 Mega Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2015,
    "manufacturer_name": "Toyota",
    "model_name": "Camry",
    "car_type": "Sedan"
  },
  {
    "year": 2015,
    "manufacturer_name": "Scion",
    "model_name": "tC",
    "car_type": "Coupe"
  },
  {
    "year": 2015,
    "manufacturer_name": "Toyota",
    "model_name": "4Runner",
    "car_type": "SUV"
  },
  {
    "year": 2015,
    "manufacturer_name": "Toyota",
    "model_name": "Corolla",
    "car_type": "Sedan"
  },
  {
    "year": 2015,
    "manufacturer_name": "Toyota",
    "model_name": "Prius c",
    "car_type": "Hatchback"
  },
  {
    "year": 2015,
    "manufacturer_name": "Ram",
    "model_name": "ProMaster City",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2015,
    "manufacturer_name": "Toyota",
    "model_name": "Sequoia",
    "car_type": "SUV"
  },
  {
    "year": 2015,
    "manufacturer_name": "Scion",
    "model_name": "iQ",
    "car_type": "Hatchback"
  },
  {
    "year": 2015,
    "manufacturer_name": "Subaru",
    "model_name": "XV Crosstrek",
    "car_type": "SUV"
  },
  {
    "year": 2015,
    "manufacturer_name": "Toyota",
    "model_name": "Land Cruiser",
    "car_type": "SUV"
  },
  {
    "year": 2015,
    "manufacturer_name": "Tesla",
    "model_name": "Model S",
    "car_type": "Sedan"
  },
  {
    "year": 2015,
    "manufacturer_name": "Ram",
    "model_name": "3500 Crew Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2015,
    "manufacturer_name": "Ram",
    "model_name": "C/V Tradesman",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2015,
    "manufacturer_name": "smart",
    "model_name": "fortwo",
    "car_type": "Hatchback, Convertible"
  },
  {
    "year": 2015,
    "manufacturer_name": "Ram",
    "model_name": "3500 Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2015,
    "manufacturer_name": "smart",
    "model_name": "fortwo electric drive",
    "car_type": "Hatchback, Convertible"
  },
  {
    "year": 2015,
    "manufacturer_name": "Ram",
    "model_name": "3500 Mega Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2015,
    "manufacturer_name": "Subaru",
    "model_name": "Impreza",
    "car_type": "Sedan, Wagon"
  },
  {
    "year": 2015,
    "manufacturer_name": "Subaru",
    "model_name": "BRZ",
    "car_type": "Coupe"
  },
  {
    "year": 2015,
    "manufacturer_name": "Rolls-Royce",
    "model_name": "Ghost",
    "car_type": "Sedan"
  },
  {
    "year": 2015,
    "manufacturer_name": "Ram",
    "model_name": "ProMaster Window Van",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2015,
    "manufacturer_name": "Toyota",
    "model_name": "RAV4",
    "car_type": "SUV"
  },
  {
    "year": 2015,
    "manufacturer_name": "Toyota",
    "model_name": "Avalon",
    "car_type": "Sedan"
  },
  {
    "year": 2015,
    "manufacturer_name": "Toyota",
    "model_name": "Tacoma Access Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2015,
    "manufacturer_name": "Toyota",
    "model_name": "Tundra CrewMax",
    "car_type": "Pickup"
  },
  {
    "year": 2015,
    "manufacturer_name": "Rolls-Royce",
    "model_name": "Phantom",
    "car_type": "Coupe, Convertible, Sedan"
  },
  {
    "year": 2015,
    "manufacturer_name": "Scion",
    "model_name": "xB",
    "car_type": "Hatchback"
  },
  {
    "year": 2015,
    "manufacturer_name": "Toyota",
    "model_name": "Highlander",
    "car_type": "SUV"
  },
  {
    "year": 2015,
    "manufacturer_name": "Subaru",
    "model_name": "Legacy",
    "car_type": "Sedan"
  },
  {
    "year": 2015,
    "manufacturer_name": "Volkswagen",
    "model_name": "Beetle",
    "car_type": "Hatchback, Convertible"
  },
  {
    "year": 2015,
    "manufacturer_name": "Subaru",
    "model_name": "WRX",
    "car_type": "Sedan"
  },
  {
    "year": 2015,
    "manufacturer_name": "Scion",
    "model_name": "FR-S",
    "car_type": "Coupe"
  },
  {
    "year": 2015,
    "manufacturer_name": "Subaru",
    "model_name": "Outback",
    "car_type": "SUV"
  },
  {
    "year": 2015,
    "manufacturer_name": "Toyota",
    "model_name": "Prius",
    "car_type": "Hatchback"
  },
  {
    "year": 2015,
    "manufacturer_name": "Toyota",
    "model_name": "Prius Plug-in Hybrid",
    "car_type": "Hatchback"
  },
  {
    "year": 2015,
    "manufacturer_name": "Toyota",
    "model_name": "Tacoma Double Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2015,
    "manufacturer_name": "Subaru",
    "model_name": "Forester",
    "car_type": "SUV"
  },
  {
    "year": 2015,
    "manufacturer_name": "Toyota",
    "model_name": "Prius v",
    "car_type": "Wagon"
  },
  {
    "year": 2015,
    "manufacturer_name": "Toyota",
    "model_name": "Sienna",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2015,
    "manufacturer_name": "Toyota",
    "model_name": "Tundra Double Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2015,
    "manufacturer_name": "Toyota",
    "model_name": "Tundra Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2015,
    "manufacturer_name": "Toyota",
    "model_name": "Venza",
    "car_type": "Wagon"
  },
  {
    "year": 2015,
    "manufacturer_name": "Toyota",
    "model_name": "Yaris",
    "car_type": "Hatchback"
  },
  {
    "year": 2015,
    "manufacturer_name": "Volkswagen",
    "model_name": "e-Golf",
    "car_type": "Hatchback"
  },
  {
    "year": 2015,
    "manufacturer_name": "Volkswagen",
    "model_name": "CC",
    "car_type": "Sedan"
  },
  {
    "year": 2015,
    "manufacturer_name": "Volkswagen",
    "model_name": "Eos",
    "car_type": "Convertible"
  },
  {
    "year": 2015,
    "manufacturer_name": "Volkswagen",
    "model_name": "Tiguan",
    "car_type": "SUV"
  },
  {
    "year": 2015,
    "manufacturer_name": "Volkswagen",
    "model_name": "Golf R",
    "car_type": "Hatchback"
  },
  {
    "year": 2015,
    "manufacturer_name": "Volkswagen",
    "model_name": "Golf",
    "car_type": "Hatchback"
  },
  {
    "year": 2015,
    "manufacturer_name": "Volkswagen",
    "model_name": "Passat",
    "car_type": "Sedan"
  },
  {
    "year": 2015,
    "manufacturer_name": "Volkswagen",
    "model_name": "Golf SportWagen",
    "car_type": "Wagon"
  },
  {
    "year": 2015,
    "manufacturer_name": "Volkswagen",
    "model_name": "Golf GTI",
    "car_type": "Hatchback"
  },
  {
    "year": 2015,
    "manufacturer_name": "Volkswagen",
    "model_name": "Jetta",
    "car_type": "Sedan"
  },
  {
    "year": 2015,
    "manufacturer_name": "Volvo",
    "model_name": "V60",
    "car_type": "Wagon"
  },
  {
    "year": 2015,
    "manufacturer_name": "Volvo",
    "model_name": "S80",
    "car_type": "Sedan"
  },
  {
    "year": 2014,
    "manufacturer_name": "Acura",
    "model_name": "ILX",
    "car_type": "Sedan"
  },
  {
    "year": 2015,
    "manufacturer_name": "Volvo",
    "model_name": "S60",
    "car_type": "Sedan"
  },
  {
    "year": 2014,
    "manufacturer_name": "Acura",
    "model_name": "RDX",
    "car_type": "SUV"
  },
  {
    "year": 2015,
    "manufacturer_name": "Volvo",
    "model_name": "XC60",
    "car_type": "SUV"
  },
  {
    "year": 2014,
    "manufacturer_name": "Acura",
    "model_name": "MDX",
    "car_type": "SUV"
  },
  {
    "year": 2014,
    "manufacturer_name": "Aston Martin",
    "model_name": "Vanquish",
    "car_type": "Coupe, Convertible"
  },
  {
    "year": 2014,
    "manufacturer_name": "Audi",
    "model_name": "A5",
    "car_type": "Coupe, Convertible"
  },
  {
    "year": 2015,
    "manufacturer_name": "Volvo",
    "model_name": "XC70",
    "car_type": "Wagon"
  },
  {
    "year": 2014,
    "manufacturer_name": "Audi",
    "model_name": "S4",
    "car_type": "Sedan"
  },
  {
    "year": 2014,
    "manufacturer_name": "Acura",
    "model_name": "TSX",
    "car_type": "Sedan, Wagon"
  },
  {
    "year": 2014,
    "manufacturer_name": "Aston Martin",
    "model_name": "Vantage",
    "car_type": "Coupe, Convertible"
  },
  {
    "year": 2014,
    "manufacturer_name": "Acura",
    "model_name": "RLX",
    "car_type": "Sedan"
  },
  {
    "year": 2014,
    "manufacturer_name": "Audi",
    "model_name": "A4",
    "car_type": "Sedan"
  },
  {
    "year": 2014,
    "manufacturer_name": "Aston Martin",
    "model_name": "DB9",
    "car_type": "Coupe, Convertible"
  },
  {
    "year": 2014,
    "manufacturer_name": "Acura",
    "model_name": "TL",
    "car_type": "Sedan"
  },
  {
    "year": 2014,
    "manufacturer_name": "Aston Martin",
    "model_name": "Rapide S",
    "car_type": "Sedan"
  },
  {
    "year": 2014,
    "manufacturer_name": "Audi",
    "model_name": "S6",
    "car_type": "Sedan"
  },
  {
    "year": 2015,
    "manufacturer_name": "Volkswagen",
    "model_name": "Touareg",
    "car_type": "SUV"
  },
  {
    "year": 2014,
    "manufacturer_name": "Audi",
    "model_name": "A8",
    "car_type": "Sedan"
  },
  {
    "year": 2014,
    "manufacturer_name": "Audi",
    "model_name": "SQ5",
    "car_type": "SUV"
  },
  {
    "year": 2014,
    "manufacturer_name": "Audi",
    "model_name": "RS 5",
    "car_type": "Convertible, Coupe"
  },
  {
    "year": 2014,
    "manufacturer_name": "BMW",
    "model_name": "2 Series",
    "car_type": "Coupe"
  },
  {
    "year": 2014,
    "manufacturer_name": "Audi",
    "model_name": "Q7",
    "car_type": "SUV"
  },
  {
    "year": 2014,
    "manufacturer_name": "Acura",
    "model_name": "RLX Sport Hybrid",
    "car_type": "Sedan"
  },
  {
    "year": 2014,
    "manufacturer_name": "Audi",
    "model_name": "RS 7",
    "car_type": "Sedan"
  },
  {
    "year": 2014,
    "manufacturer_name": "Audi",
    "model_name": "S7",
    "car_type": "Sedan"
  },
  {
    "year": 2014,
    "manufacturer_name": "Audi",
    "model_name": "A6",
    "car_type": "Sedan"
  },
  {
    "year": 2014,
    "manufacturer_name": "Audi",
    "model_name": "Q5",
    "car_type": "SUV"
  },
  {
    "year": 2014,
    "manufacturer_name": "Audi",
    "model_name": "S5",
    "car_type": "Convertible, Coupe"
  },
  {
    "year": 2014,
    "manufacturer_name": "Audi",
    "model_name": "TT",
    "car_type": "Coupe, Convertible"
  },
  {
    "year": 2014,
    "manufacturer_name": "Audi",
    "model_name": "R8",
    "car_type": "Coupe, Convertible"
  },
  {
    "year": 2014,
    "manufacturer_name": "Audi",
    "model_name": "S8",
    "car_type": "Sedan"
  },
  {
    "year": 2014,
    "manufacturer_name": "Audi",
    "model_name": "allroad",
    "car_type": "Wagon"
  },
  {
    "year": 2014,
    "manufacturer_name": "Audi",
    "model_name": "A7",
    "car_type": "Sedan"
  },
  {
    "year": 2014,
    "manufacturer_name": "Bentley",
    "model_name": "Flying Spur",
    "car_type": "Sedan"
  },
  {
    "year": 2014,
    "manufacturer_name": "BMW",
    "model_name": "i8",
    "car_type": "Coupe"
  },
  {
    "year": 2014,
    "manufacturer_name": "BMW",
    "model_name": "X6 M",
    "car_type": "SUV"
  },
  {
    "year": 2014,
    "manufacturer_name": "BMW",
    "model_name": "5 Series",
    "car_type": "Sedan"
  },
  {
    "year": 2014,
    "manufacturer_name": "BMW",
    "model_name": "X3",
    "car_type": "SUV"
  },
  {
    "year": 2014,
    "manufacturer_name": "Bentley",
    "model_name": "Mulsanne",
    "car_type": "Sedan"
  },
  {
    "year": 2014,
    "manufacturer_name": "Buick",
    "model_name": "LaCrosse",
    "car_type": "Sedan"
  },
  {
    "year": 2014,
    "manufacturer_name": "BMW",
    "model_name": "M6",
    "car_type": "Coupe, Convertible"
  },
  {
    "year": 2014,
    "manufacturer_name": "BMW",
    "model_name": "7 Series",
    "car_type": "Sedan"
  },
  {
    "year": 2014,
    "manufacturer_name": "BMW",
    "model_name": "3 Series",
    "car_type": "Wagon, Sedan"
  },
  {
    "year": 2014,
    "manufacturer_name": "BMW",
    "model_name": "M5",
    "car_type": "Sedan"
  },
  {
    "year": 2014,
    "manufacturer_name": "BMW",
    "model_name": "i3",
    "car_type": "Hatchback"
  },
  {
    "year": 2014,
    "manufacturer_name": "BMW",
    "model_name": "6 Series",
    "car_type": "Coupe, Convertible"
  },
  {
    "year": 2014,
    "manufacturer_name": "BMW",
    "model_name": "X1",
    "car_type": "SUV"
  },
  {
    "year": 2014,
    "manufacturer_name": "Buick",
    "model_name": "Verano",
    "car_type": "Sedan"
  },
  {
    "year": 2014,
    "manufacturer_name": "Bentley",
    "model_name": "Continental",
    "car_type": "Coupe, Convertible"
  },
  {
    "year": 2014,
    "manufacturer_name": "BMW",
    "model_name": "X6",
    "car_type": "SUV"
  },
  {
    "year": 2014,
    "manufacturer_name": "Buick",
    "model_name": "Enclave",
    "car_type": "SUV"
  },
  {
    "year": 2014,
    "manufacturer_name": "BMW",
    "model_name": "4 Series",
    "car_type": "Coupe, Convertible"
  },
  {
    "year": 2014,
    "manufacturer_name": "BMW",
    "model_name": "Z4",
    "car_type": "Convertible"
  },
  {
    "year": 2014,
    "manufacturer_name": "Cadillac",
    "model_name": "ELR",
    "car_type": "Coupe"
  },
  {
    "year": 2014,
    "manufacturer_name": "Chevrolet",
    "model_name": "Impala Limited",
    "car_type": "Sedan"
  },
  {
    "year": 2014,
    "manufacturer_name": "BMW",
    "model_name": "X5",
    "car_type": "SUV"
  },
  {
    "year": 2014,
    "manufacturer_name": "Cadillac",
    "model_name": "Escalade ESV",
    "car_type": "SUV"
  },
  {
    "year": 2014,
    "manufacturer_name": "Cadillac",
    "model_name": "CTS",
    "car_type": "Sedan, Coupe, Wagon"
  },
  {
    "year": 2014,
    "manufacturer_name": "Chevrolet",
    "model_name": "Express 2500 Passenger",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2014,
    "manufacturer_name": "Buick",
    "model_name": "Regal",
    "car_type": "Sedan"
  },
  {
    "year": 2014,
    "manufacturer_name": "Cadillac",
    "model_name": "SRX",
    "car_type": "SUV"
  },
  {
    "year": 2014,
    "manufacturer_name": "Cadillac",
    "model_name": "ATS",
    "car_type": "Sedan"
  },
  {
    "year": 2014,
    "manufacturer_name": "Chevrolet",
    "model_name": "Express 1500 Cargo",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2014,
    "manufacturer_name": "Chevrolet",
    "model_name": "Camaro",
    "car_type": "Coupe, Convertible"
  },
  {
    "year": 2014,
    "manufacturer_name": "Buick",
    "model_name": "Encore",
    "car_type": "SUV"
  },
  {
    "year": 2014,
    "manufacturer_name": "Chevrolet",
    "model_name": "Express 3500 Passenger",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2014,
    "manufacturer_name": "Chevrolet",
    "model_name": "Express 3500 Cargo",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2014,
    "manufacturer_name": "Chevrolet",
    "model_name": "Silverado 1500 Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2014,
    "manufacturer_name": "Chevrolet",
    "model_name": "Captiva Sport",
    "car_type": "SUV"
  },
  {
    "year": 2014,
    "manufacturer_name": "Chevrolet",
    "model_name": "Express 2500 Cargo",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2014,
    "manufacturer_name": "Chevrolet",
    "model_name": "Cruze",
    "car_type": "Sedan"
  },
  {
    "year": 2014,
    "manufacturer_name": "Cadillac",
    "model_name": "Escalade",
    "car_type": "SUV"
  },
  {
    "year": 2014,
    "manufacturer_name": "Chevrolet",
    "model_name": "Silverado 3500 HD Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2014,
    "manufacturer_name": "Chevrolet",
    "model_name": "Express 1500 Passenger",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2014,
    "manufacturer_name": "Chevrolet",
    "model_name": "Impala",
    "car_type": "Sedan"
  },
  {
    "year": 2014,
    "manufacturer_name": "Cadillac",
    "model_name": "XTS",
    "car_type": "Sedan"
  },
  {
    "year": 2014,
    "manufacturer_name": "Chevrolet",
    "model_name": "Malibu",
    "car_type": "Sedan"
  },
  {
    "year": 2014,
    "manufacturer_name": "Chevrolet",
    "model_name": "Silverado 2500 HD Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2014,
    "manufacturer_name": "Chevrolet",
    "model_name": "Silverado 2500 HD Crew Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2014,
    "manufacturer_name": "Chevrolet",
    "model_name": "Equinox",
    "car_type": "SUV"
  },
  {
    "year": 2014,
    "manufacturer_name": "Chevrolet",
    "model_name": "Corvette",
    "car_type": "Coupe, Convertible"
  },
  {
    "year": 2014,
    "manufacturer_name": "Chevrolet",
    "model_name": "Silverado 1500 Double Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2014,
    "manufacturer_name": "Chevrolet",
    "model_name": "Silverado 3500 HD Crew Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2014,
    "manufacturer_name": "Chevrolet",
    "model_name": "Sonic",
    "car_type": "Sedan, Hatchback"
  },
  {
    "year": 2014,
    "manufacturer_name": "Chevrolet",
    "model_name": "Spark",
    "car_type": "Hatchback"
  },
  {
    "year": 2014,
    "manufacturer_name": "Chevrolet",
    "model_name": "Silverado 1500 Crew Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2014,
    "manufacturer_name": "Chevrolet",
    "model_name": "Spark EV",
    "car_type": "Hatchback"
  },
  {
    "year": 2014,
    "manufacturer_name": "Chevrolet",
    "model_name": "SS",
    "car_type": "Sedan"
  },
  {
    "year": 2014,
    "manufacturer_name": "Chrysler",
    "model_name": "300",
    "car_type": "Sedan"
  },
  {
    "year": 2014,
    "manufacturer_name": "Chrysler",
    "model_name": "200",
    "car_type": "Sedan, Convertible"
  },
  {
    "year": 2014,
    "manufacturer_name": "Chevrolet",
    "model_name": "Suburban 1500",
    "car_type": "SUV"
  },
  {
    "year": 2014,
    "manufacturer_name": "Chevrolet",
    "model_name": "Tahoe",
    "car_type": "SUV"
  },
  {
    "year": 2014,
    "manufacturer_name": "Chevrolet",
    "model_name": "Traverse",
    "car_type": "SUV"
  },
  {
    "year": 2014,
    "manufacturer_name": "Dodge",
    "model_name": "Challenger",
    "car_type": "Coupe"
  },
  {
    "year": 2014,
    "manufacturer_name": "Chevrolet",
    "model_name": "Volt",
    "car_type": "Sedan"
  },
  {
    "year": 2014,
    "manufacturer_name": "Dodge",
    "model_name": "Avenger",
    "car_type": "Sedan"
  },
  {
    "year": 2014,
    "manufacturer_name": "Chrysler",
    "model_name": "Town & Country",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2014,
    "manufacturer_name": "Ferrari",
    "model_name": "California",
    "car_type": "Convertible"
  },
  {
    "year": 2014,
    "manufacturer_name": "Dodge",
    "model_name": "Dart",
    "car_type": "Sedan"
  },
  {
    "year": 2014,
    "manufacturer_name": "FIAT",
    "model_name": "500",
    "car_type": "Hatchback"
  },
  {
    "year": 2014,
    "manufacturer_name": "Dodge",
    "model_name": "Grand Caravan Passenger",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2014,
    "manufacturer_name": "Dodge",
    "model_name": "Journey",
    "car_type": "SUV"
  },
  {
    "year": 2014,
    "manufacturer_name": "Dodge",
    "model_name": "Charger",
    "car_type": "Sedan"
  },
  {
    "year": 2014,
    "manufacturer_name": "Ferrari",
    "model_name": "FF",
    "car_type": "Coupe"
  },
  {
    "year": 2014,
    "manufacturer_name": "Ferrari",
    "model_name": "F12berlinetta",
    "car_type": "Coupe"
  },
  {
    "year": 2014,
    "manufacturer_name": "Dodge",
    "model_name": "Durango",
    "car_type": "SUV"
  },
  {
    "year": 2014,
    "manufacturer_name": "Ferrari",
    "model_name": "458 Speciale",
    "car_type": "Coupe"
  },
  {
    "year": 2014,
    "manufacturer_name": "FIAT",
    "model_name": "500c",
    "car_type": "Convertible"
  },
  {
    "year": 2014,
    "manufacturer_name": "Ferrari",
    "model_name": "458 Italia",
    "car_type": "Coupe"
  },
  {
    "year": 2014,
    "manufacturer_name": "FIAT",
    "model_name": "500e",
    "car_type": "Hatchback"
  },
  {
    "year": 2014,
    "manufacturer_name": "Ferrari",
    "model_name": "458 Spider",
    "car_type": "Convertible"
  },
  {
    "year": 2014,
    "manufacturer_name": "Ford",
    "model_name": "E350 Super Duty Cargo",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2014,
    "manufacturer_name": "FIAT",
    "model_name": "500 Abarth",
    "car_type": "Hatchback, Convertible"
  },
  {
    "year": 2014,
    "manufacturer_name": "FIAT",
    "model_name": "500L",
    "car_type": "Hatchback"
  },
  {
    "year": 2014,
    "manufacturer_name": "Ford",
    "model_name": "C-MAX Hybrid",
    "car_type": "Wagon"
  },
  {
    "year": 2014,
    "manufacturer_name": "Ford",
    "model_name": "Expedition",
    "car_type": "SUV"
  },
  {
    "year": 2014,
    "manufacturer_name": "Ford",
    "model_name": "Explorer",
    "car_type": "SUV"
  },
  {
    "year": 2014,
    "manufacturer_name": "Ford",
    "model_name": "F250 Super Duty Super Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2014,
    "manufacturer_name": "Ford",
    "model_name": "E150 Passenger",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2014,
    "manufacturer_name": "Ford",
    "model_name": "Edge",
    "car_type": "SUV"
  },
  {
    "year": 2014,
    "manufacturer_name": "Ford",
    "model_name": "Fiesta",
    "car_type": "Sedan, Hatchback"
  },
  {
    "year": 2014,
    "manufacturer_name": "Ford",
    "model_name": "E150 Cargo",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2014,
    "manufacturer_name": "Ford",
    "model_name": "C-MAX Energi",
    "car_type": "Wagon"
  },
  {
    "year": 2014,
    "manufacturer_name": "Ford",
    "model_name": "E250 Cargo",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2014,
    "manufacturer_name": "Ford",
    "model_name": "Escape",
    "car_type": "SUV"
  },
  {
    "year": 2014,
    "manufacturer_name": "Ford",
    "model_name": "E350 Super Duty Passenger",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2014,
    "manufacturer_name": "Ford",
    "model_name": "F450 Super Duty Crew Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2014,
    "manufacturer_name": "Ford",
    "model_name": "F150 Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2014,
    "manufacturer_name": "Ford",
    "model_name": "F350 Super Duty Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2014,
    "manufacturer_name": "Ford",
    "model_name": "Expedition EL",
    "car_type": "SUV"
  },
  {
    "year": 2014,
    "manufacturer_name": "Ford",
    "model_name": "F150 Super Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2014,
    "manufacturer_name": "Ford",
    "model_name": "F350 Super Duty Crew Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2014,
    "manufacturer_name": "Ford",
    "model_name": "F150 SuperCrew Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2014,
    "manufacturer_name": "Ford",
    "model_name": "F350 Super Duty Super Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2014,
    "manufacturer_name": "Ford",
    "model_name": "Mustang",
    "car_type": "Coupe, Convertible"
  },
  {
    "year": 2014,
    "manufacturer_name": "Ford",
    "model_name": "F250 Super Duty Crew Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2014,
    "manufacturer_name": "Ford",
    "model_name": "Focus ST",
    "car_type": "Hatchback"
  },
  {
    "year": 2014,
    "manufacturer_name": "Ford",
    "model_name": "Focus",
    "car_type": "Sedan, Hatchback"
  },
  {
    "year": 2014,
    "manufacturer_name": "Ford",
    "model_name": "F250 Super Duty Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2014,
    "manufacturer_name": "Ford",
    "model_name": "Flex",
    "car_type": "SUV"
  },
  {
    "year": 2014,
    "manufacturer_name": "Ford",
    "model_name": "Fusion Energi",
    "car_type": "Sedan"
  },
  {
    "year": 2014,
    "manufacturer_name": "GMC",
    "model_name": "Acadia",
    "car_type": "SUV"
  },
  {
    "year": 2014,
    "manufacturer_name": "Freightliner",
    "model_name": "Sprinter 2500 Cargo",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2014,
    "manufacturer_name": "Freightliner",
    "model_name": "Sprinter 3500 Cargo",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2014,
    "manufacturer_name": "Ford",
    "model_name": "Taurus",
    "car_type": "Sedan"
  },
  {
    "year": 2014,
    "manufacturer_name": "Ford",
    "model_name": "Fusion",
    "car_type": "Sedan"
  },
  {
    "year": 2014,
    "manufacturer_name": "Ford",
    "model_name": "Transit Connect Cargo",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2014,
    "manufacturer_name": "GMC",
    "model_name": "Sierra 1500 Crew Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2014,
    "manufacturer_name": "Freightliner",
    "model_name": "Sprinter 2500 Passenger",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2014,
    "manufacturer_name": "Ford",
    "model_name": "Transit Connect Passenger",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2014,
    "manufacturer_name": "Freightliner",
    "model_name": "Sprinter 2500 Crew",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2014,
    "manufacturer_name": "GMC",
    "model_name": "Savana 1500 Cargo",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2014,
    "manufacturer_name": "GMC",
    "model_name": "Savana 2500 Passenger",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2014,
    "manufacturer_name": "GMC",
    "model_name": "Savana 1500 Passenger",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2014,
    "manufacturer_name": "GMC",
    "model_name": "Sierra 3500 HD Crew Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2014,
    "manufacturer_name": "GMC",
    "model_name": "Savana 3500 Passenger",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2014,
    "manufacturer_name": "GMC",
    "model_name": "Sierra 1500 Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2014,
    "manufacturer_name": "GMC",
    "model_name": "Yukon XL 1500",
    "car_type": "SUV"
  },
  {
    "year": 2014,
    "manufacturer_name": "GMC",
    "model_name": "Savana 2500 Cargo",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2014,
    "manufacturer_name": "Honda",
    "model_name": "Odyssey",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2014,
    "manufacturer_name": "Hyundai",
    "model_name": "Genesis Coupe",
    "car_type": "Coupe"
  },
  {
    "year": 2014,
    "manufacturer_name": "GMC",
    "model_name": "Sierra 1500 Double Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2014,
    "manufacturer_name": "GMC",
    "model_name": "Sierra 2500 HD Crew Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2014,
    "manufacturer_name": "Honda",
    "model_name": "Accord",
    "car_type": "Sedan, Coupe"
  },
  {
    "year": 2014,
    "manufacturer_name": "GMC",
    "model_name": "Sierra 3500 HD Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2014,
    "manufacturer_name": "Honda",
    "model_name": "Accord Hybrid",
    "car_type": "Sedan"
  },
  {
    "year": 2014,
    "manufacturer_name": "GMC",
    "model_name": "Sierra 2500 HD Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2014,
    "manufacturer_name": "Honda",
    "model_name": "Civic",
    "car_type": "Sedan, Coupe"
  },
  {
    "year": 2014,
    "manufacturer_name": "Honda",
    "model_name": "Crosstour",
    "car_type": "SUV"
  },
  {
    "year": 2014,
    "manufacturer_name": "GMC",
    "model_name": "Savana 3500 Cargo",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2014,
    "manufacturer_name": "Honda",
    "model_name": "CR-V",
    "car_type": "SUV"
  },
  {
    "year": 2014,
    "manufacturer_name": "Honda",
    "model_name": "Insight",
    "car_type": "Hatchback"
  },
  {
    "year": 2014,
    "manufacturer_name": "Honda",
    "model_name": "CR-Z",
    "car_type": "Coupe"
  },
  {
    "year": 2014,
    "manufacturer_name": "Hyundai",
    "model_name": "Accent",
    "car_type": "Hatchback, Sedan"
  },
  {
    "year": 2014,
    "manufacturer_name": "GMC",
    "model_name": "Terrain",
    "car_type": "SUV"
  },
  {
    "year": 2014,
    "manufacturer_name": "Hyundai",
    "model_name": "Elantra",
    "car_type": "Sedan, Hatchback, Coupe"
  },
  {
    "year": 2014,
    "manufacturer_name": "GMC",
    "model_name": "Yukon",
    "car_type": "SUV"
  },
  {
    "year": 2014,
    "manufacturer_name": "Honda",
    "model_name": "Pilot",
    "car_type": "SUV"
  },
  {
    "year": 2014,
    "manufacturer_name": "Hyundai",
    "model_name": "Azera",
    "car_type": "Sedan"
  },
  {
    "year": 2014,
    "manufacturer_name": "Hyundai",
    "model_name": "Santa Fe Sport",
    "car_type": "SUV"
  },
  {
    "year": 2014,
    "manufacturer_name": "Honda",
    "model_name": "Ridgeline",
    "car_type": "Pickup"
  },
  {
    "year": 2014,
    "manufacturer_name": "Hyundai",
    "model_name": "Santa Fe",
    "car_type": "SUV"
  },
  {
    "year": 2014,
    "manufacturer_name": "Hyundai",
    "model_name": "Tucson",
    "car_type": "SUV"
  },
  {
    "year": 2014,
    "manufacturer_name": "Hyundai",
    "model_name": "Equus",
    "car_type": "Sedan"
  },
  {
    "year": 2014,
    "manufacturer_name": "Hyundai",
    "model_name": "Sonata",
    "car_type": "Sedan"
  },
  {
    "year": 2014,
    "manufacturer_name": "Hyundai",
    "model_name": "Veloster",
    "car_type": "Coupe"
  },
  {
    "year": 2014,
    "manufacturer_name": "Hyundai",
    "model_name": "Genesis",
    "car_type": "Sedan"
  },
  {
    "year": 2014,
    "manufacturer_name": "INFINITI",
    "model_name": "Q50",
    "car_type": "Sedan"
  },
  {
    "year": 2014,
    "manufacturer_name": "INFINITI",
    "model_name": "Q60",
    "car_type": "Coupe, Convertible"
  },
  {
    "year": 2014,
    "manufacturer_name": "INFINITI",
    "model_name": "QX50",
    "car_type": "SUV"
  },
  {
    "year": 2014,
    "manufacturer_name": "INFINITI",
    "model_name": "Q70",
    "car_type": "Sedan"
  },
  {
    "year": 2014,
    "manufacturer_name": "INFINITI",
    "model_name": "QX60",
    "car_type": "SUV"
  },
  {
    "year": 2014,
    "manufacturer_name": "Jaguar",
    "model_name": "XF",
    "car_type": "Sedan"
  },
  {
    "year": 2014,
    "manufacturer_name": "INFINITI",
    "model_name": "QX70",
    "car_type": "SUV"
  },
  {
    "year": 2014,
    "manufacturer_name": "Jaguar",
    "model_name": "XJ",
    "car_type": "Sedan"
  },
  {
    "year": 2014,
    "manufacturer_name": "INFINITI",
    "model_name": "QX80",
    "car_type": "SUV"
  },
  {
    "year": 2014,
    "manufacturer_name": "Jeep",
    "model_name": "Patriot",
    "car_type": "SUV"
  },
  {
    "year": 2014,
    "manufacturer_name": "Jaguar",
    "model_name": "XK",
    "car_type": "Coupe, Convertible"
  },
  {
    "year": 2014,
    "manufacturer_name": "Jeep",
    "model_name": "Cherokee",
    "car_type": "SUV"
  },
  {
    "year": 2014,
    "manufacturer_name": "Jaguar",
    "model_name": "F-TYPE",
    "car_type": "Convertible"
  },
  {
    "year": 2014,
    "manufacturer_name": "Kia",
    "model_name": "Forte",
    "car_type": "Sedan, Coupe, Hatchback"
  },
  {
    "year": 2014,
    "manufacturer_name": "Kia",
    "model_name": "Optima",
    "car_type": "Sedan"
  },
  {
    "year": 2014,
    "manufacturer_name": "Kia",
    "model_name": "Cadenza",
    "car_type": "Sedan"
  },
  {
    "year": 2014,
    "manufacturer_name": "Jeep",
    "model_name": "Wrangler",
    "car_type": "SUV"
  },
  {
    "year": 2014,
    "manufacturer_name": "Jeep",
    "model_name": "Grand Cherokee",
    "car_type": "SUV"
  },
  {
    "year": 2014,
    "manufacturer_name": "Kia",
    "model_name": "Rio",
    "car_type": "Sedan, Hatchback"
  },
  {
    "year": 2014,
    "manufacturer_name": "Jeep",
    "model_name": "Compass",
    "car_type": "SUV"
  },
  {
    "year": 2014,
    "manufacturer_name": "Lexus",
    "model_name": "GX",
    "car_type": "SUV"
  },
  {
    "year": 2014,
    "manufacturer_name": "Land Rover",
    "model_name": "LR4",
    "car_type": "SUV"
  },
  {
    "year": 2014,
    "manufacturer_name": "Lexus",
    "model_name": "LS",
    "car_type": "Sedan"
  },
  {
    "year": 2014,
    "manufacturer_name": "Kia",
    "model_name": "Sorento",
    "car_type": "SUV"
  },
  {
    "year": 2014,
    "manufacturer_name": "Lexus",
    "model_name": "LX",
    "car_type": "SUV"
  },
  {
    "year": 2014,
    "manufacturer_name": "Lexus",
    "model_name": "IS",
    "car_type": "Sedan, Convertible"
  },
  {
    "year": 2014,
    "manufacturer_name": "Kia",
    "model_name": "Sportage",
    "car_type": "SUV"
  },
  {
    "year": 2014,
    "manufacturer_name": "Lincoln",
    "model_name": "Navigator L",
    "car_type": "SUV"
  },
  {
    "year": 2014,
    "manufacturer_name": "Kia",
    "model_name": "Sedona",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2014,
    "manufacturer_name": "Kia",
    "model_name": "Soul",
    "car_type": "Wagon"
  },
  {
    "year": 2014,
    "manufacturer_name": "MAZDA",
    "model_name": "CX-5",
    "car_type": "SUV"
  },
  {
    "year": 2014,
    "manufacturer_name": "Land Rover",
    "model_name": "Range Rover Sport",
    "car_type": "SUV"
  },
  {
    "year": 2014,
    "manufacturer_name": "Lamborghini",
    "model_name": "Aventador",
    "car_type": "Coupe, Convertible"
  },
  {
    "year": 2014,
    "manufacturer_name": "Lamborghini",
    "model_name": "Gallardo",
    "car_type": "Coupe, Convertible"
  },
  {
    "year": 2014,
    "manufacturer_name": "Land Rover",
    "model_name": "Range Rover Evoque",
    "car_type": "SUV"
  },
  {
    "year": 2014,
    "manufacturer_name": "Lexus",
    "model_name": "GS",
    "car_type": "Sedan"
  },
  {
    "year": 2014,
    "manufacturer_name": "Lexus",
    "model_name": "RX",
    "car_type": "SUV"
  },
  {
    "year": 2014,
    "manufacturer_name": "Land Rover",
    "model_name": "LR2",
    "car_type": "SUV"
  },
  {
    "year": 2014,
    "manufacturer_name": "Lincoln",
    "model_name": "MKS",
    "car_type": "Sedan"
  },
  {
    "year": 2014,
    "manufacturer_name": "MAZDA",
    "model_name": "MAZDA2",
    "car_type": "Hatchback"
  },
  {
    "year": 2014,
    "manufacturer_name": "Lotus",
    "model_name": "Evora",
    "car_type": "Coupe"
  },
  {
    "year": 2014,
    "manufacturer_name": "Land Rover",
    "model_name": "Range Rover",
    "car_type": "SUV"
  },
  {
    "year": 2014,
    "manufacturer_name": "Lexus",
    "model_name": "CT",
    "car_type": "Hatchback"
  },
  {
    "year": 2014,
    "manufacturer_name": "Lincoln",
    "model_name": "Navigator",
    "car_type": "SUV"
  },
  {
    "year": 2014,
    "manufacturer_name": "Lincoln",
    "model_name": "MKX",
    "car_type": "SUV"
  },
  {
    "year": 2014,
    "manufacturer_name": "Lincoln",
    "model_name": "MKT",
    "car_type": "SUV"
  },
  {
    "year": 2014,
    "manufacturer_name": "Lexus",
    "model_name": "ES",
    "car_type": "Sedan"
  },
  {
    "year": 2014,
    "manufacturer_name": "Lincoln",
    "model_name": "MKZ",
    "car_type": "Sedan"
  },
  {
    "year": 2014,
    "manufacturer_name": "Maserati",
    "model_name": "GranTurismo",
    "car_type": "Convertible, Coupe"
  },
  {
    "year": 2014,
    "manufacturer_name": "MAZDA",
    "model_name": "MAZDA5",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2014,
    "manufacturer_name": "Maserati",
    "model_name": "Quattroporte",
    "car_type": "Sedan"
  },
  {
    "year": 2014,
    "manufacturer_name": "Maserati",
    "model_name": "Ghibli",
    "car_type": "Sedan"
  },
  {
    "year": 2014,
    "manufacturer_name": "MAZDA",
    "model_name": "CX-9",
    "car_type": "SUV"
  },
  {
    "year": 2014,
    "manufacturer_name": "Mercedes-Benz",
    "model_name": "B-Class",
    "car_type": "Hatchback"
  },
  {
    "year": 2014,
    "manufacturer_name": "MAZDA",
    "model_name": "MAZDA6",
    "car_type": "Sedan"
  },
  {
    "year": 2014,
    "manufacturer_name": "MAZDA",
    "model_name": "MAZDA3",
    "car_type": "Sedan, Hatchback"
  },
  {
    "year": 2014,
    "manufacturer_name": "Mercedes-Benz",
    "model_name": "C-Class",
    "car_type": "Sedan, Coupe"
  },
  {
    "year": 2014,
    "manufacturer_name": "MAZDA",
    "model_name": "MX-5 Miata",
    "car_type": "Convertible"
  },
  {
    "year": 2014,
    "manufacturer_name": "McLaren",
    "model_name": "MP4-12C",
    "car_type": "Coupe, Convertible"
  },
  {
    "year": 2014,
    "manufacturer_name": "Mercedes-Benz",
    "model_name": "G-Class",
    "car_type": "SUV"
  },
  {
    "year": 2014,
    "manufacturer_name": "Mercedes-Benz",
    "model_name": "CLA-Class",
    "car_type": "Sedan"
  },
  {
    "year": 2014,
    "manufacturer_name": "Mercedes-Benz",
    "model_name": "CLS-Class",
    "car_type": "Coupe"
  },
  {
    "year": 2014,
    "manufacturer_name": "Mercedes-Benz",
    "model_name": "Sprinter 2500 Passenger",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2014,
    "manufacturer_name": "MINI",
    "model_name": "Convertible",
    "car_type": "Convertible"
  },
  {
    "year": 2014,
    "manufacturer_name": "Mercedes-Benz",
    "model_name": "Sprinter 2500 Cargo",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2014,
    "manufacturer_name": "Mercedes-Benz",
    "model_name": "CL-Class",
    "car_type": "Coupe"
  },
  {
    "year": 2014,
    "manufacturer_name": "Mercedes-Benz",
    "model_name": "GL-Class",
    "car_type": "SUV"
  },
  {
    "year": 2014,
    "manufacturer_name": "Mercedes-Benz",
    "model_name": "GLK-Class",
    "car_type": "SUV"
  },
  {
    "year": 2014,
    "manufacturer_name": "Mercedes-Benz",
    "model_name": "SL-Class",
    "car_type": "Convertible"
  },
  {
    "year": 2014,
    "manufacturer_name": "Mercedes-Benz",
    "model_name": "E-Class",
    "car_type": "Sedan, Wagon, Coupe, Convertible"
  },
  {
    "year": 2014,
    "manufacturer_name": "Nissan",
    "model_name": "cube",
    "car_type": "Wagon"
  },
  {
    "year": 2014,
    "manufacturer_name": "Mercedes-Benz",
    "model_name": "S-Class",
    "car_type": "Sedan"
  },
  {
    "year": 2014,
    "manufacturer_name": "Nissan",
    "model_name": "GT-R",
    "car_type": "Coupe"
  },
  {
    "year": 2014,
    "manufacturer_name": "Mitsubishi",
    "model_name": "i-MiEV",
    "car_type": "Hatchback"
  },
  {
    "year": 2014,
    "manufacturer_name": "Mercedes-Benz",
    "model_name": "SLS-Class",
    "car_type": "Coupe, Convertible"
  },
  {
    "year": 2014,
    "manufacturer_name": "MINI",
    "model_name": "Coupe",
    "car_type": "Coupe"
  },
  {
    "year": 2014,
    "manufacturer_name": "Mercedes-Benz",
    "model_name": "Sprinter 3500 Cargo",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2014,
    "manufacturer_name": "MINI",
    "model_name": "Roadster",
    "car_type": "Convertible"
  },
  {
    "year": 2014,
    "manufacturer_name": "Mercedes-Benz",
    "model_name": "M-Class",
    "car_type": "SUV"
  },
  {
    "year": 2014,
    "manufacturer_name": "Mercedes-Benz",
    "model_name": "SLK-Class",
    "car_type": "Convertible"
  },
  {
    "year": 2014,
    "manufacturer_name": "Nissan",
    "model_name": "JUKE",
    "car_type": "SUV"
  },
  {
    "year": 2014,
    "manufacturer_name": "MINI",
    "model_name": "Paceman",
    "car_type": "Hatchback"
  },
  {
    "year": 2014,
    "manufacturer_name": "Nissan",
    "model_name": "370Z",
    "car_type": "Coupe, Convertible"
  },
  {
    "year": 2014,
    "manufacturer_name": "MINI",
    "model_name": "Clubman",
    "car_type": "Hatchback"
  },
  {
    "year": 2014,
    "manufacturer_name": "Mitsubishi",
    "model_name": "Outlander Sport",
    "car_type": "SUV"
  },
  {
    "year": 2014,
    "manufacturer_name": "Mitsubishi",
    "model_name": "Mirage",
    "car_type": "Hatchback"
  },
  {
    "year": 2014,
    "manufacturer_name": "Mitsubishi",
    "model_name": "Lancer",
    "car_type": "Sedan, Hatchback"
  },
  {
    "year": 2014,
    "manufacturer_name": "MINI",
    "model_name": "Hardtop",
    "car_type": "Hatchback"
  },
  {
    "year": 2014,
    "manufacturer_name": "Mercedes-Benz",
    "model_name": "Sprinter 2500 Crew",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2014,
    "manufacturer_name": "Mitsubishi",
    "model_name": "Outlander",
    "car_type": "SUV"
  },
  {
    "year": 2014,
    "manufacturer_name": "Nissan",
    "model_name": "Frontier King Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2014,
    "manufacturer_name": "Nissan",
    "model_name": "Altima",
    "car_type": "Sedan"
  },
  {
    "year": 2014,
    "manufacturer_name": "Nissan",
    "model_name": "Armada",
    "car_type": "SUV"
  },
  {
    "year": 2014,
    "manufacturer_name": "MINI",
    "model_name": "Countryman",
    "car_type": "Hatchback"
  },
  {
    "year": 2014,
    "manufacturer_name": "Nissan",
    "model_name": "NV1500 Cargo",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2014,
    "manufacturer_name": "Nissan",
    "model_name": "Murano",
    "car_type": "SUV"
  },
  {
    "year": 2014,
    "manufacturer_name": "Nissan",
    "model_name": "LEAF",
    "car_type": "Hatchback"
  },
  {
    "year": 2014,
    "manufacturer_name": "Nissan",
    "model_name": "Maxima",
    "car_type": "Sedan"
  },
  {
    "year": 2014,
    "manufacturer_name": "Nissan",
    "model_name": "Frontier Crew Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2014,
    "manufacturer_name": "Nissan",
    "model_name": "NV200",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2014,
    "manufacturer_name": "Nissan",
    "model_name": "NV2500 HD Cargo",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2014,
    "manufacturer_name": "Nissan",
    "model_name": "NV3500 HD Passenger",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2014,
    "manufacturer_name": "Nissan",
    "model_name": "Titan Crew Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2014,
    "manufacturer_name": "Nissan",
    "model_name": "Sentra",
    "car_type": "Sedan"
  },
  {
    "year": 2014,
    "manufacturer_name": "Nissan",
    "model_name": "Rogue Select",
    "car_type": "SUV"
  },
  {
    "year": 2014,
    "manufacturer_name": "Nissan",
    "model_name": "Titan King Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2014,
    "manufacturer_name": "Nissan",
    "model_name": "Quest",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2014,
    "manufacturer_name": "Nissan",
    "model_name": "Pathfinder",
    "car_type": "SUV"
  },
  {
    "year": 2014,
    "manufacturer_name": "Nissan",
    "model_name": "NV3500 HD Cargo",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2014,
    "manufacturer_name": "Nissan",
    "model_name": "Rogue",
    "car_type": "SUV"
  },
  {
    "year": 2014,
    "manufacturer_name": "Porsche",
    "model_name": "Cayenne",
    "car_type": "SUV"
  },
  {
    "year": 2014,
    "manufacturer_name": "Ram",
    "model_name": "1500 Crew Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2014,
    "manufacturer_name": "Porsche",
    "model_name": "Panamera",
    "car_type": "Sedan"
  },
  {
    "year": 2014,
    "manufacturer_name": "Porsche",
    "model_name": "Boxster",
    "car_type": "Convertible"
  },
  {
    "year": 2014,
    "manufacturer_name": "Nissan",
    "model_name": "Xterra",
    "car_type": "SUV"
  },
  {
    "year": 2014,
    "manufacturer_name": "Porsche",
    "model_name": "Cayman",
    "car_type": "Coupe"
  },
  {
    "year": 2014,
    "manufacturer_name": "Porsche",
    "model_name": "911",
    "car_type": "Coupe, Convertible"
  },
  {
    "year": 2014,
    "manufacturer_name": "Ram",
    "model_name": "1500 Quad Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2014,
    "manufacturer_name": "Nissan",
    "model_name": "Versa",
    "car_type": "Sedan, Hatchback"
  },
  {
    "year": 2014,
    "manufacturer_name": "Ram",
    "model_name": "3500 Crew Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2014,
    "manufacturer_name": "Ram",
    "model_name": "1500 Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2014,
    "manufacturer_name": "Subaru",
    "model_name": "Tribeca",
    "car_type": "SUV"
  },
  {
    "year": 2014,
    "manufacturer_name": "Rolls-Royce",
    "model_name": "Phantom",
    "car_type": "Sedan, Coupe, Convertible"
  },
  {
    "year": 2014,
    "manufacturer_name": "Ram",
    "model_name": "3500 Mega Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2014,
    "manufacturer_name": "Ram",
    "model_name": "2500 Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2014,
    "manufacturer_name": "Ram",
    "model_name": "C/V Tradesman",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2014,
    "manufacturer_name": "smart",
    "model_name": "fortwo electric drive",
    "car_type": "Hatchback, Convertible"
  },
  {
    "year": 2014,
    "manufacturer_name": "Ram",
    "model_name": "2500 Crew Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2014,
    "manufacturer_name": "Ram",
    "model_name": "ProMaster 3500 Cargo",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2014,
    "manufacturer_name": "Ram",
    "model_name": "ProMaster 2500 Cargo",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2014,
    "manufacturer_name": "Ram",
    "model_name": "2500 Mega Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2014,
    "manufacturer_name": "Scion",
    "model_name": "iQ",
    "car_type": "Hatchback"
  },
  {
    "year": 2014,
    "manufacturer_name": "Scion",
    "model_name": "FR-S",
    "car_type": "Coupe"
  },
  {
    "year": 2014,
    "manufacturer_name": "Subaru",
    "model_name": "BRZ",
    "car_type": "Coupe"
  },
  {
    "year": 2014,
    "manufacturer_name": "Scion",
    "model_name": "xD",
    "car_type": "Hatchback"
  },
  {
    "year": 2014,
    "manufacturer_name": "Tesla",
    "model_name": "Model S",
    "car_type": "Sedan"
  },
  {
    "year": 2014,
    "manufacturer_name": "Ram",
    "model_name": "ProMaster 1500 Cargo",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2014,
    "manufacturer_name": "Subaru",
    "model_name": "Legacy",
    "car_type": "Sedan"
  },
  {
    "year": 2014,
    "manufacturer_name": "Rolls-Royce",
    "model_name": "Ghost",
    "car_type": "Sedan"
  },
  {
    "year": 2014,
    "manufacturer_name": "Scion",
    "model_name": "xB",
    "car_type": "Hatchback"
  },
  {
    "year": 2014,
    "manufacturer_name": "SRT",
    "model_name": "Viper",
    "car_type": "Coupe"
  },
  {
    "year": 2014,
    "manufacturer_name": "Rolls-Royce",
    "model_name": "Wraith",
    "car_type": "Coupe"
  },
  {
    "year": 2014,
    "manufacturer_name": "Ram",
    "model_name": "3500 Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2014,
    "manufacturer_name": "smart",
    "model_name": "fortwo",
    "car_type": "Hatchback, Convertible"
  },
  {
    "year": 2014,
    "manufacturer_name": "Scion",
    "model_name": "tC",
    "car_type": "Coupe"
  },
  {
    "year": 2014,
    "manufacturer_name": "Subaru",
    "model_name": "Impreza",
    "car_type": "Sedan, Wagon"
  },
  {
    "year": 2014,
    "manufacturer_name": "Toyota",
    "model_name": "FJ Cruiser",
    "car_type": "SUV"
  },
  {
    "year": 2014,
    "manufacturer_name": "Subaru",
    "model_name": "Forester",
    "car_type": "SUV"
  },
  {
    "year": 2014,
    "manufacturer_name": "Toyota",
    "model_name": "Prius",
    "car_type": "Hatchback"
  },
  {
    "year": 2014,
    "manufacturer_name": "Toyota",
    "model_name": "Prius c",
    "car_type": "Hatchback"
  },
  {
    "year": 2014,
    "manufacturer_name": "Toyota",
    "model_name": "Camry",
    "car_type": "Sedan"
  },
  {
    "year": 2014,
    "manufacturer_name": "Toyota",
    "model_name": "Highlander",
    "car_type": "SUV"
  },
  {
    "year": 2014,
    "manufacturer_name": "Toyota",
    "model_name": "Avalon",
    "car_type": "Sedan"
  },
  {
    "year": 2014,
    "manufacturer_name": "Toyota",
    "model_name": "Corolla",
    "car_type": "Sedan"
  },
  {
    "year": 2014,
    "manufacturer_name": "Toyota",
    "model_name": "Tacoma Access Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2014,
    "manufacturer_name": "Toyota",
    "model_name": "RAV4",
    "car_type": "SUV"
  },
  {
    "year": 2014,
    "manufacturer_name": "Toyota",
    "model_name": "Tundra Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2014,
    "manufacturer_name": "Toyota",
    "model_name": "Land Cruiser",
    "car_type": "SUV"
  },
  {
    "year": 2014,
    "manufacturer_name": "Subaru",
    "model_name": "XV Crosstrek",
    "car_type": "SUV"
  },
  {
    "year": 2014,
    "manufacturer_name": "Toyota",
    "model_name": "Tacoma Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2014,
    "manufacturer_name": "Subaru",
    "model_name": "Outback",
    "car_type": "Wagon"
  },
  {
    "year": 2014,
    "manufacturer_name": "Toyota",
    "model_name": "4Runner",
    "car_type": "SUV"
  },
  {
    "year": 2014,
    "manufacturer_name": "Toyota",
    "model_name": "Prius v",
    "car_type": "Wagon"
  },
  {
    "year": 2014,
    "manufacturer_name": "Toyota",
    "model_name": "Sequoia",
    "car_type": "SUV"
  },
  {
    "year": 2014,
    "manufacturer_name": "Toyota",
    "model_name": "Venza",
    "car_type": "Wagon"
  },
  {
    "year": 2014,
    "manufacturer_name": "Toyota",
    "model_name": "Prius Plug-in Hybrid",
    "car_type": "Hatchback"
  },
  {
    "year": 2014,
    "manufacturer_name": "Volkswagen",
    "model_name": "Passat",
    "car_type": "Sedan"
  },
  {
    "year": 2014,
    "manufacturer_name": "Volkswagen",
    "model_name": "Golf",
    "car_type": "Hatchback"
  },
  {
    "year": 2014,
    "manufacturer_name": "Toyota",
    "model_name": "Sienna",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2014,
    "manufacturer_name": "Toyota",
    "model_name": "Tacoma Double Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2014,
    "manufacturer_name": "Volkswagen",
    "model_name": "CC",
    "car_type": "Sedan"
  },
  {
    "year": 2014,
    "manufacturer_name": "Toyota",
    "model_name": "Tundra Double Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2014,
    "manufacturer_name": "Volkswagen",
    "model_name": "Beetle",
    "car_type": "Hatchback, Convertible"
  },
  {
    "year": 2014,
    "manufacturer_name": "Toyota",
    "model_name": "Yaris",
    "car_type": "Hatchback"
  },
  {
    "year": 2014,
    "manufacturer_name": "Volkswagen",
    "model_name": "Eos",
    "car_type": "Convertible"
  },
  {
    "year": 2014,
    "manufacturer_name": "Toyota",
    "model_name": "Tundra CrewMax",
    "car_type": "Pickup"
  },
  {
    "year": 2014,
    "manufacturer_name": "Volvo",
    "model_name": "S80",
    "car_type": "Sedan"
  },
  {
    "year": 2014,
    "manufacturer_name": "Volkswagen",
    "model_name": "Jetta",
    "car_type": "Sedan"
  },
  {
    "year": 2014,
    "manufacturer_name": "Volkswagen",
    "model_name": "GTI",
    "car_type": "Hatchback"
  },
  {
    "year": 2014,
    "manufacturer_name": "Volkswagen",
    "model_name": "Routan",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2013,
    "manufacturer_name": "Acura",
    "model_name": "MDX",
    "car_type": "SUV"
  },
  {
    "year": 2013,
    "manufacturer_name": "Audi",
    "model_name": "A6",
    "car_type": "Sedan"
  },
  {
    "year": 2014,
    "manufacturer_name": "Volvo",
    "model_name": "S60",
    "car_type": "Sedan"
  },
  {
    "year": 2013,
    "manufacturer_name": "Acura",
    "model_name": "ILX",
    "car_type": "Sedan"
  },
  {
    "year": 2013,
    "manufacturer_name": "Acura",
    "model_name": "TSX",
    "car_type": "Sedan, Wagon"
  },
  {
    "year": 2014,
    "manufacturer_name": "Volvo",
    "model_name": "XC90",
    "car_type": "SUV"
  },
  {
    "year": 2014,
    "manufacturer_name": "Volkswagen",
    "model_name": "Jetta SportWagen",
    "car_type": "Wagon"
  },
  {
    "year": 2014,
    "manufacturer_name": "Volkswagen",
    "model_name": "Touareg",
    "car_type": "SUV"
  },
  {
    "year": 2014,
    "manufacturer_name": "Volvo",
    "model_name": "XC60",
    "car_type": "SUV"
  },
  {
    "year": 2013,
    "manufacturer_name": "Acura",
    "model_name": "TL",
    "car_type": "Sedan"
  },
  {
    "year": 2013,
    "manufacturer_name": "Audi",
    "model_name": "A7",
    "car_type": "Sedan"
  },
  {
    "year": 2014,
    "manufacturer_name": "Volkswagen",
    "model_name": "Tiguan",
    "car_type": "SUV"
  },
  {
    "year": 2013,
    "manufacturer_name": "Audi",
    "model_name": "A4",
    "car_type": "Sedan"
  },
  {
    "year": 2013,
    "manufacturer_name": "Acura",
    "model_name": "RDX",
    "car_type": "SUV"
  },
  {
    "year": 2013,
    "manufacturer_name": "Audi",
    "model_name": "A5",
    "car_type": "Convertible, Coupe"
  },
  {
    "year": 2014,
    "manufacturer_name": "Volvo",
    "model_name": "XC70",
    "car_type": "Wagon"
  },
  {
    "year": 2013,
    "manufacturer_name": "Aston Martin",
    "model_name": "Vantage",
    "car_type": "Coupe, Convertible"
  },
  {
    "year": 2013,
    "manufacturer_name": "Aston Martin",
    "model_name": "DB9",
    "car_type": "Coupe, Convertible"
  },
  {
    "year": 2013,
    "manufacturer_name": "Audi",
    "model_name": "A3",
    "car_type": "Wagon"
  },
  {
    "year": 2013,
    "manufacturer_name": "Acura",
    "model_name": "ZDX",
    "car_type": "SUV"
  },
  {
    "year": 2013,
    "manufacturer_name": "Audi",
    "model_name": "allroad",
    "car_type": "Wagon"
  },
  {
    "year": 2013,
    "manufacturer_name": "Audi",
    "model_name": "S5",
    "car_type": "Coupe, Convertible"
  },
  {
    "year": 2013,
    "manufacturer_name": "Audi",
    "model_name": "TT",
    "car_type": "Convertible, Coupe"
  },
  {
    "year": 2013,
    "manufacturer_name": "BMW",
    "model_name": "3 Series",
    "car_type": "Convertible, Sedan, Coupe"
  },
  {
    "year": 2013,
    "manufacturer_name": "Audi",
    "model_name": "A8",
    "car_type": "Sedan"
  },
  {
    "year": 2013,
    "manufacturer_name": "BMW",
    "model_name": "1 Series",
    "car_type": "Coupe, Convertible"
  },
  {
    "year": 2013,
    "manufacturer_name": "Audi",
    "model_name": "S7",
    "car_type": "Sedan"
  },
  {
    "year": 2013,
    "manufacturer_name": "Audi",
    "model_name": "Q5",
    "car_type": "SUV"
  },
  {
    "year": 2013,
    "manufacturer_name": "Bentley",
    "model_name": "Continental",
    "car_type": "Sedan, Convertible, Coupe"
  },
  {
    "year": 2013,
    "manufacturer_name": "Audi",
    "model_name": "Q7",
    "car_type": "SUV"
  },
  {
    "year": 2013,
    "manufacturer_name": "Audi",
    "model_name": "S6",
    "car_type": "Sedan"
  },
  {
    "year": 2013,
    "manufacturer_name": "Audi",
    "model_name": "RS 5",
    "car_type": "Coupe, Convertible"
  },
  {
    "year": 2013,
    "manufacturer_name": "Audi",
    "model_name": "S4",
    "car_type": "Sedan"
  },
  {
    "year": 2013,
    "manufacturer_name": "BMW",
    "model_name": "6 Series",
    "car_type": "Convertible, Coupe"
  },
  {
    "year": 2013,
    "manufacturer_name": "Bentley",
    "model_name": "Mulsanne",
    "car_type": "Sedan"
  },
  {
    "year": 2013,
    "manufacturer_name": "Audi",
    "model_name": "S8",
    "car_type": "Sedan"
  },
  {
    "year": 2013,
    "manufacturer_name": "BMW",
    "model_name": "M5",
    "car_type": "Sedan"
  },
  {
    "year": 2013,
    "manufacturer_name": "BMW",
    "model_name": "5 Series",
    "car_type": "Sedan"
  },
  {
    "year": 2013,
    "manufacturer_name": "BMW",
    "model_name": "M3",
    "car_type": "Coupe, Convertible"
  },
  {
    "year": 2013,
    "manufacturer_name": "BMW",
    "model_name": "M6",
    "car_type": "Coupe, Convertible"
  },
  {
    "year": 2013,
    "manufacturer_name": "BMW",
    "model_name": "X6 M",
    "car_type": "SUV"
  },
  {
    "year": 2013,
    "manufacturer_name": "Buick",
    "model_name": "Regal",
    "car_type": "Sedan"
  },
  {
    "year": 2013,
    "manufacturer_name": "BMW",
    "model_name": "7 Series",
    "car_type": "Sedan"
  },
  {
    "year": 2013,
    "manufacturer_name": "BMW",
    "model_name": "X5 M",
    "car_type": "SUV"
  },
  {
    "year": 2013,
    "manufacturer_name": "Buick",
    "model_name": "Encore",
    "car_type": "SUV"
  },
  {
    "year": 2013,
    "manufacturer_name": "Cadillac",
    "model_name": "Escalade",
    "car_type": "SUV"
  },
  {
    "year": 2013,
    "manufacturer_name": "BMW",
    "model_name": "X3",
    "car_type": "SUV"
  },
  {
    "year": 2013,
    "manufacturer_name": "BMW",
    "model_name": "X1",
    "car_type": "SUV"
  },
  {
    "year": 2013,
    "manufacturer_name": "Buick",
    "model_name": "Enclave",
    "car_type": "SUV"
  },
  {
    "year": 2013,
    "manufacturer_name": "Buick",
    "model_name": "Verano",
    "car_type": "Sedan"
  },
  {
    "year": 2013,
    "manufacturer_name": "Cadillac",
    "model_name": "XTS",
    "car_type": "Sedan"
  },
  {
    "year": 2013,
    "manufacturer_name": "BMW",
    "model_name": "X5",
    "car_type": "SUV"
  },
  {
    "year": 2013,
    "manufacturer_name": "Cadillac",
    "model_name": "Escalade ESV",
    "car_type": "SUV"
  },
  {
    "year": 2013,
    "manufacturer_name": "Buick",
    "model_name": "LaCrosse",
    "car_type": "Sedan"
  },
  {
    "year": 2013,
    "manufacturer_name": "BMW",
    "model_name": "X6",
    "car_type": "SUV"
  },
  {
    "year": 2013,
    "manufacturer_name": "Cadillac",
    "model_name": "Escalade EXT",
    "car_type": "Pickup"
  },
  {
    "year": 2013,
    "manufacturer_name": "Cadillac",
    "model_name": "CTS",
    "car_type": "Sedan, Coupe, Wagon"
  },
  {
    "year": 2013,
    "manufacturer_name": "BMW",
    "model_name": "Z4",
    "car_type": "Convertible"
  },
  {
    "year": 2013,
    "manufacturer_name": "Cadillac",
    "model_name": "SRX",
    "car_type": "SUV"
  },
  {
    "year": 2013,
    "manufacturer_name": "Cadillac",
    "model_name": "ATS",
    "car_type": "Sedan"
  },
  {
    "year": 2013,
    "manufacturer_name": "Chevrolet",
    "model_name": "Express 1500 Cargo",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2013,
    "manufacturer_name": "Chevrolet",
    "model_name": "Silverado 1500 Crew Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2013,
    "manufacturer_name": "Chevrolet",
    "model_name": "Camaro",
    "car_type": "Coupe, Convertible"
  },
  {
    "year": 2013,
    "manufacturer_name": "Chevrolet",
    "model_name": "Equinox",
    "car_type": "SUV"
  },
  {
    "year": 2013,
    "manufacturer_name": "Chevrolet",
    "model_name": "Corvette",
    "car_type": "Coupe, Convertible"
  },
  {
    "year": 2013,
    "manufacturer_name": "Chevrolet",
    "model_name": "Express 2500 Cargo",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2013,
    "manufacturer_name": "Chevrolet",
    "model_name": "Cruze",
    "car_type": "Sedan"
  },
  {
    "year": 2013,
    "manufacturer_name": "Chevrolet",
    "model_name": "Malibu",
    "car_type": "Sedan"
  },
  {
    "year": 2013,
    "manufacturer_name": "Chevrolet",
    "model_name": "Captiva Sport",
    "car_type": "SUV"
  },
  {
    "year": 2013,
    "manufacturer_name": "Chevrolet",
    "model_name": "Spark",
    "car_type": "Hatchback"
  },
  {
    "year": 2013,
    "manufacturer_name": "Chevrolet",
    "model_name": "Express 3500 Cargo",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2013,
    "manufacturer_name": "Chevrolet",
    "model_name": "Impala",
    "car_type": "Sedan"
  },
  {
    "year": 2013,
    "manufacturer_name": "Chevrolet",
    "model_name": "Silverado 2500 HD Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2013,
    "manufacturer_name": "Chevrolet",
    "model_name": "Express 1500 Passenger",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2013,
    "manufacturer_name": "Chevrolet",
    "model_name": "Silverado 1500 Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2013,
    "manufacturer_name": "Chevrolet",
    "model_name": "Avalanche",
    "car_type": "SUV"
  },
  {
    "year": 2013,
    "manufacturer_name": "Chevrolet",
    "model_name": "Express 2500 Passenger",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2013,
    "manufacturer_name": "Chevrolet",
    "model_name": "Express 3500 Passenger",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2013,
    "manufacturer_name": "Chevrolet",
    "model_name": "Sonic",
    "car_type": "Sedan, Hatchback"
  },
  {
    "year": 2013,
    "manufacturer_name": "Chevrolet",
    "model_name": "Silverado 2500 HD Extended Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2013,
    "manufacturer_name": "Chevrolet",
    "model_name": "Silverado 3500 HD Extended Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2013,
    "manufacturer_name": "Dodge",
    "model_name": "Challenger",
    "car_type": "Coupe"
  },
  {
    "year": 2013,
    "manufacturer_name": "Chevrolet",
    "model_name": "Volt",
    "car_type": "Sedan"
  },
  {
    "year": 2013,
    "manufacturer_name": "Chevrolet",
    "model_name": "Silverado 1500 Extended Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2013,
    "manufacturer_name": "Chevrolet",
    "model_name": "Silverado 2500 HD Crew Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2013,
    "manufacturer_name": "Chevrolet",
    "model_name": "Silverado 3500 HD Crew Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2013,
    "manufacturer_name": "Dodge",
    "model_name": "Grand Caravan Passenger",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2013,
    "manufacturer_name": "Ferrari",
    "model_name": "California",
    "car_type": "Convertible"
  },
  {
    "year": 2013,
    "manufacturer_name": "Ferrari",
    "model_name": "FF",
    "car_type": "Coupe"
  },
  {
    "year": 2013,
    "manufacturer_name": "Ford",
    "model_name": "C-MAX Energi",
    "car_type": "Wagon"
  },
  {
    "year": 2013,
    "manufacturer_name": "Chevrolet",
    "model_name": "Tahoe",
    "car_type": "SUV"
  },
  {
    "year": 2013,
    "manufacturer_name": "Chevrolet",
    "model_name": "Suburban 2500",
    "car_type": "SUV"
  },
  {
    "year": 2013,
    "manufacturer_name": "Chevrolet",
    "model_name": "Silverado 3500 HD Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2013,
    "manufacturer_name": "Chevrolet",
    "model_name": "Traverse",
    "car_type": "SUV"
  },
  {
    "year": 2013,
    "manufacturer_name": "Chevrolet",
    "model_name": "Suburban 1500",
    "car_type": "SUV"
  },
  {
    "year": 2013,
    "manufacturer_name": "Chrysler",
    "model_name": "Town & Country",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2013,
    "manufacturer_name": "Dodge",
    "model_name": "Journey",
    "car_type": "SUV"
  },
  {
    "year": 2013,
    "manufacturer_name": "Dodge",
    "model_name": "Avenger",
    "car_type": "Sedan"
  },
  {
    "year": 2013,
    "manufacturer_name": "Ferrari",
    "model_name": "458 Spider",
    "car_type": "Convertible"
  },
  {
    "year": 2013,
    "manufacturer_name": "Dodge",
    "model_name": "Durango",
    "car_type": "SUV"
  },
  {
    "year": 2013,
    "manufacturer_name": "Dodge",
    "model_name": "Charger",
    "car_type": "Sedan"
  },
  {
    "year": 2013,
    "manufacturer_name": "Chrysler",
    "model_name": "300",
    "car_type": "Sedan"
  },
  {
    "year": 2013,
    "manufacturer_name": "Ford",
    "model_name": "Edge",
    "car_type": "SUV"
  },
  {
    "year": 2013,
    "manufacturer_name": "Ford",
    "model_name": "E150 Cargo",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2013,
    "manufacturer_name": "Chrysler",
    "model_name": "200",
    "car_type": "Sedan, Convertible"
  },
  {
    "year": 2013,
    "manufacturer_name": "Ford",
    "model_name": "E350 Super Duty Cargo",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2013,
    "manufacturer_name": "FIAT",
    "model_name": "500e",
    "car_type": "Hatchback"
  },
  {
    "year": 2013,
    "manufacturer_name": "Ferrari",
    "model_name": "F12berlinetta",
    "car_type": "Coupe"
  },
  {
    "year": 2013,
    "manufacturer_name": "Ford",
    "model_name": "C-MAX Hybrid",
    "car_type": "Wagon"
  },
  {
    "year": 2013,
    "manufacturer_name": "Dodge",
    "model_name": "Dart",
    "car_type": "Sedan"
  },
  {
    "year": 2013,
    "manufacturer_name": "Ford",
    "model_name": "F150 Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2013,
    "manufacturer_name": "Ford",
    "model_name": "E250 Cargo",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2013,
    "manufacturer_name": "Ferrari",
    "model_name": "458 Italia",
    "car_type": "Coupe"
  },
  {
    "year": 2013,
    "manufacturer_name": "FIAT",
    "model_name": "500",
    "car_type": "Hatchback, Convertible"
  },
  {
    "year": 2013,
    "manufacturer_name": "Ford",
    "model_name": "E350 Super Duty Passenger",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2013,
    "manufacturer_name": "Ford",
    "model_name": "E150 Passenger",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2013,
    "manufacturer_name": "Ford",
    "model_name": "Explorer",
    "car_type": "SUV"
  },
  {
    "year": 2013,
    "manufacturer_name": "Ford",
    "model_name": "Escape",
    "car_type": "SUV"
  },
  {
    "year": 2013,
    "manufacturer_name": "Ford",
    "model_name": "Expedition",
    "car_type": "SUV"
  },
  {
    "year": 2013,
    "manufacturer_name": "Ford",
    "model_name": "Expedition EL",
    "car_type": "SUV"
  },
  {
    "year": 2013,
    "manufacturer_name": "Ford",
    "model_name": "F150 SuperCrew Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2013,
    "manufacturer_name": "Ford",
    "model_name": "F350 Super Duty Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2013,
    "manufacturer_name": "Ford",
    "model_name": "F250 Super Duty Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2013,
    "manufacturer_name": "Ford",
    "model_name": "F450 Super Duty Crew Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2013,
    "manufacturer_name": "Ford",
    "model_name": "F350 Super Duty Crew Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2013,
    "manufacturer_name": "Ford",
    "model_name": "F250 Super Duty Super Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2013,
    "manufacturer_name": "Ford",
    "model_name": "F150 Super Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2013,
    "manufacturer_name": "Ford",
    "model_name": "F250 Super Duty Crew Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2013,
    "manufacturer_name": "Ford",
    "model_name": "F350 Super Duty Super Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2013,
    "manufacturer_name": "Ford",
    "model_name": "Flex",
    "car_type": "SUV"
  },
  {
    "year": 2013,
    "manufacturer_name": "Ford",
    "model_name": "Focus",
    "car_type": "Sedan, Hatchback"
  },
  {
    "year": 2013,
    "manufacturer_name": "Ford",
    "model_name": "Fiesta",
    "car_type": "Sedan, Hatchback"
  },
  {
    "year": 2013,
    "manufacturer_name": "Ford",
    "model_name": "Mustang",
    "car_type": "Coupe, Convertible"
  },
  {
    "year": 2013,
    "manufacturer_name": "Freightliner",
    "model_name": "Sprinter 2500 Cargo",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2013,
    "manufacturer_name": "Freightliner",
    "model_name": "Sprinter 3500 Cargo",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2013,
    "manufacturer_name": "GMC",
    "model_name": "Savana 2500 Cargo",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2013,
    "manufacturer_name": "Ford",
    "model_name": "Focus ST",
    "car_type": "Hatchback"
  },
  {
    "year": 2013,
    "manufacturer_name": "Ford",
    "model_name": "Taurus",
    "car_type": "Sedan"
  },
  {
    "year": 2013,
    "manufacturer_name": "Ford",
    "model_name": "Fusion",
    "car_type": "Sedan"
  },
  {
    "year": 2013,
    "manufacturer_name": "Freightliner",
    "model_name": "Sprinter 2500 Passenger",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2013,
    "manufacturer_name": "Ford",
    "model_name": "Fusion Energi",
    "car_type": "Sedan"
  },
  {
    "year": 2013,
    "manufacturer_name": "Ford",
    "model_name": "Transit Connect Cargo",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2013,
    "manufacturer_name": "GMC",
    "model_name": "Savana 3500 Passenger",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2013,
    "manufacturer_name": "Ford",
    "model_name": "Transit Connect Passenger",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2013,
    "manufacturer_name": "GMC",
    "model_name": "Savana 3500 Cargo",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2013,
    "manufacturer_name": "GMC",
    "model_name": "Savana 1500 Passenger",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2013,
    "manufacturer_name": "GMC",
    "model_name": "Acadia",
    "car_type": "SUV"
  },
  {
    "year": 2013,
    "manufacturer_name": "Freightliner",
    "model_name": "Sprinter 2500 Crew",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2013,
    "manufacturer_name": "GMC",
    "model_name": "Sierra 1500 Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2013,
    "manufacturer_name": "GMC",
    "model_name": "Savana 1500 Cargo",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2013,
    "manufacturer_name": "GMC",
    "model_name": "Savana 2500 Passenger",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2013,
    "manufacturer_name": "GMC",
    "model_name": "Yukon XL 1500",
    "car_type": "SUV"
  },
  {
    "year": 2013,
    "manufacturer_name": "GMC",
    "model_name": "Yukon",
    "car_type": "SUV"
  },
  {
    "year": 2013,
    "manufacturer_name": "GMC",
    "model_name": "Terrain",
    "car_type": "SUV"
  },
  {
    "year": 2013,
    "manufacturer_name": "GMC",
    "model_name": "Sierra 3500 HD Crew Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2013,
    "manufacturer_name": "GMC",
    "model_name": "Sierra 1500 Crew Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2013,
    "manufacturer_name": "GMC",
    "model_name": "Sierra 3500 HD Extended Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2013,
    "manufacturer_name": "Honda",
    "model_name": "Pilot",
    "car_type": "SUV"
  },
  {
    "year": 2013,
    "manufacturer_name": "GMC",
    "model_name": "Sierra 2500 HD Crew Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2013,
    "manufacturer_name": "Honda",
    "model_name": "Civic",
    "car_type": "Sedan, Coupe"
  },
  {
    "year": 2013,
    "manufacturer_name": "Honda",
    "model_name": "CR-V",
    "car_type": "SUV"
  },
  {
    "year": 2013,
    "manufacturer_name": "GMC",
    "model_name": "Sierra 1500 Extended Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2013,
    "manufacturer_name": "GMC",
    "model_name": "Sierra 3500 HD Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2013,
    "manufacturer_name": "Honda",
    "model_name": "Insight",
    "car_type": "Hatchback"
  },
  {
    "year": 2013,
    "manufacturer_name": "GMC",
    "model_name": "Yukon XL 2500",
    "car_type": "SUV"
  },
  {
    "year": 2013,
    "manufacturer_name": "GMC",
    "model_name": "Sierra 2500 HD Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2013,
    "manufacturer_name": "GMC",
    "model_name": "Sierra 2500 HD Extended Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2013,
    "manufacturer_name": "Honda",
    "model_name": "Crosstour",
    "car_type": "SUV"
  },
  {
    "year": 2013,
    "manufacturer_name": "Honda",
    "model_name": "Odyssey",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2013,
    "manufacturer_name": "Hyundai",
    "model_name": "Santa Fe",
    "car_type": "SUV"
  },
  {
    "year": 2013,
    "manufacturer_name": "Honda",
    "model_name": "CR-Z",
    "car_type": "Coupe"
  },
  {
    "year": 2013,
    "manufacturer_name": "Honda",
    "model_name": "Accord",
    "car_type": "Sedan, Coupe"
  },
  {
    "year": 2013,
    "manufacturer_name": "Hyundai",
    "model_name": "Azera",
    "car_type": "Sedan"
  },
  {
    "year": 2013,
    "manufacturer_name": "Honda",
    "model_name": "Ridgeline",
    "car_type": "Pickup"
  },
  {
    "year": 2013,
    "manufacturer_name": "INFINITI",
    "model_name": "EX",
    "car_type": "SUV"
  },
  {
    "year": 2013,
    "manufacturer_name": "Honda",
    "model_name": "Fit",
    "car_type": "Hatchback"
  },
  {
    "year": 2013,
    "manufacturer_name": "INFINITI",
    "model_name": "QX",
    "car_type": "SUV"
  },
  {
    "year": 2013,
    "manufacturer_name": "Hyundai",
    "model_name": "Genesis",
    "car_type": "Sedan"
  },
  {
    "year": 2013,
    "manufacturer_name": "INFINITI",
    "model_name": "G",
    "car_type": "Sedan, Coupe, Convertible"
  },
  {
    "year": 2013,
    "manufacturer_name": "Hyundai",
    "model_name": "Equus",
    "car_type": "Sedan"
  },
  {
    "year": 2013,
    "manufacturer_name": "Hyundai",
    "model_name": "Sonata",
    "car_type": "Sedan"
  },
  {
    "year": 2013,
    "manufacturer_name": "Hyundai",
    "model_name": "Elantra",
    "car_type": "Sedan, Coupe, Hatchback"
  },
  {
    "year": 2013,
    "manufacturer_name": "Hyundai",
    "model_name": "Accent",
    "car_type": "Sedan, Hatchback"
  },
  {
    "year": 2013,
    "manufacturer_name": "Hyundai",
    "model_name": "Genesis Coupe",
    "car_type": "Coupe"
  },
  {
    "year": 2013,
    "manufacturer_name": "Hyundai",
    "model_name": "Veloster",
    "car_type": "Coupe"
  },
  {
    "year": 2013,
    "manufacturer_name": "Lamborghini",
    "model_name": "Gallardo",
    "car_type": "Coupe, Convertible"
  },
  {
    "year": 2013,
    "manufacturer_name": "Hyundai",
    "model_name": "Santa Fe Sport",
    "car_type": "SUV"
  },
  {
    "year": 2013,
    "manufacturer_name": "Jeep",
    "model_name": "Grand Cherokee",
    "car_type": "SUV"
  },
  {
    "year": 2013,
    "manufacturer_name": "Hyundai",
    "model_name": "Tucson",
    "car_type": "SUV"
  },
  {
    "year": 2013,
    "manufacturer_name": "INFINITI",
    "model_name": "JX",
    "car_type": "SUV"
  },
  {
    "year": 2013,
    "manufacturer_name": "Kia",
    "model_name": "Rio",
    "car_type": "Sedan, Hatchback"
  },
  {
    "year": 2013,
    "manufacturer_name": "INFINITI",
    "model_name": "FX",
    "car_type": "SUV"
  },
  {
    "year": 2013,
    "manufacturer_name": "Jeep",
    "model_name": "Compass",
    "car_type": "SUV"
  },
  {
    "year": 2013,
    "manufacturer_name": "Kia",
    "model_name": "Optima",
    "car_type": "Sedan"
  },
  {
    "year": 2013,
    "manufacturer_name": "Jaguar",
    "model_name": "XF",
    "car_type": "Sedan"
  },
  {
    "year": 2013,
    "manufacturer_name": "INFINITI",
    "model_name": "M",
    "car_type": "Sedan"
  },
  {
    "year": 2013,
    "manufacturer_name": "Jaguar",
    "model_name": "XJ",
    "car_type": "Sedan"
  },
  {
    "year": 2013,
    "manufacturer_name": "Lincoln",
    "model_name": "MKT",
    "car_type": "SUV"
  },
  {
    "year": 2013,
    "manufacturer_name": "Jaguar",
    "model_name": "XK",
    "car_type": "Coupe, Convertible"
  },
  {
    "year": 2013,
    "manufacturer_name": "Kia",
    "model_name": "Forte",
    "car_type": "Sedan, Hatchback, Coupe"
  },
  {
    "year": 2013,
    "manufacturer_name": "Jeep",
    "model_name": "Patriot",
    "car_type": "SUV"
  },
  {
    "year": 2013,
    "manufacturer_name": "Kia",
    "model_name": "Sportage",
    "car_type": "SUV"
  },
  {
    "year": 2013,
    "manufacturer_name": "Land Rover",
    "model_name": "Range Rover Sport",
    "car_type": "SUV"
  },
  {
    "year": 2013,
    "manufacturer_name": "Lexus",
    "model_name": "IS",
    "car_type": "Sedan, Convertible"
  },
  {
    "year": 2013,
    "manufacturer_name": "Jeep",
    "model_name": "Wrangler",
    "car_type": "SUV"
  },
  {
    "year": 2013,
    "manufacturer_name": "Lamborghini",
    "model_name": "Aventador",
    "car_type": "Coupe, Convertible"
  },
  {
    "year": 2013,
    "manufacturer_name": "Lexus",
    "model_name": "CT",
    "car_type": "Hatchback"
  },
  {
    "year": 2013,
    "manufacturer_name": "Kia",
    "model_name": "Sorento",
    "car_type": "SUV"
  },
  {
    "year": 2013,
    "manufacturer_name": "Land Rover",
    "model_name": "Range Rover",
    "car_type": "SUV"
  },
  {
    "year": 2013,
    "manufacturer_name": "Land Rover",
    "model_name": "LR4",
    "car_type": "SUV"
  },
  {
    "year": 2013,
    "manufacturer_name": "Lexus",
    "model_name": "GS",
    "car_type": "Sedan"
  },
  {
    "year": 2013,
    "manufacturer_name": "Land Rover",
    "model_name": "LR2",
    "car_type": "SUV"
  },
  {
    "year": 2013,
    "manufacturer_name": "Land Rover",
    "model_name": "Range Rover Evoque",
    "car_type": "SUV"
  },
  {
    "year": 2013,
    "manufacturer_name": "Kia",
    "model_name": "Soul",
    "car_type": "Wagon"
  },
  {
    "year": 2013,
    "manufacturer_name": "Lexus",
    "model_name": "GX",
    "car_type": "SUV"
  },
  {
    "year": 2013,
    "manufacturer_name": "Lexus",
    "model_name": "LX",
    "car_type": "SUV"
  },
  {
    "year": 2013,
    "manufacturer_name": "Lincoln",
    "model_name": "MKS",
    "car_type": "Sedan"
  },
  {
    "year": 2013,
    "manufacturer_name": "Lexus",
    "model_name": "ES",
    "car_type": "Sedan"
  },
  {
    "year": 2013,
    "manufacturer_name": "Lexus",
    "model_name": "RX",
    "car_type": "SUV"
  },
  {
    "year": 2013,
    "manufacturer_name": "Lexus",
    "model_name": "LS",
    "car_type": "Sedan"
  },
  {
    "year": 2013,
    "manufacturer_name": "Lincoln",
    "model_name": "MKX",
    "car_type": "SUV"
  },
  {
    "year": 2013,
    "manufacturer_name": "Lincoln",
    "model_name": "Navigator L",
    "car_type": "SUV"
  },
  {
    "year": 2013,
    "manufacturer_name": "MAZDA",
    "model_name": "CX-5",
    "car_type": "SUV"
  },
  {
    "year": 2013,
    "manufacturer_name": "MAZDA",
    "model_name": "MAZDA2",
    "car_type": "Hatchback"
  },
  {
    "year": 2013,
    "manufacturer_name": "MAZDA",
    "model_name": "CX-9",
    "car_type": "SUV"
  },
  {
    "year": 2013,
    "manufacturer_name": "Maserati",
    "model_name": "Quattroporte",
    "car_type": "Sedan"
  },
  {
    "year": 2013,
    "manufacturer_name": "MAZDA",
    "model_name": "MAZDA3",
    "car_type": "Sedan, Hatchback"
  },
  {
    "year": 2013,
    "manufacturer_name": "Lincoln",
    "model_name": "MKZ",
    "car_type": "Sedan"
  },
  {
    "year": 2013,
    "manufacturer_name": "Lincoln",
    "model_name": "Navigator",
    "car_type": "SUV"
  },
  {
    "year": 2013,
    "manufacturer_name": "MAZDA",
    "model_name": "MAZDA5",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2013,
    "manufacturer_name": "McLaren",
    "model_name": "MP4-12C",
    "car_type": "Coupe"
  },
  {
    "year": 2013,
    "manufacturer_name": "MAZDA",
    "model_name": "MX-5 Miata",
    "car_type": "Convertible"
  },
  {
    "year": 2013,
    "manufacturer_name": "Maserati",
    "model_name": "GranTurismo",
    "car_type": "Coupe, Convertible"
  },
  {
    "year": 2013,
    "manufacturer_name": "Lotus",
    "model_name": "Evora",
    "car_type": "Coupe"
  },
  {
    "year": 2013,
    "manufacturer_name": "Mercedes-Benz",
    "model_name": "E-Class",
    "car_type": "Sedan, Coupe, Wagon, Convertible"
  },
  {
    "year": 2013,
    "manufacturer_name": "Mercedes-Benz",
    "model_name": "G-Class",
    "car_type": "SUV"
  },
  {
    "year": 2013,
    "manufacturer_name": "MINI",
    "model_name": "Countryman",
    "car_type": "Hatchback"
  },
  {
    "year": 2013,
    "manufacturer_name": "Mercedes-Benz",
    "model_name": "Sprinter 2500 Passenger",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2013,
    "manufacturer_name": "Mercedes-Benz",
    "model_name": "C-Class",
    "car_type": "Sedan, Coupe"
  },
  {
    "year": 2013,
    "manufacturer_name": "Mercedes-Benz",
    "model_name": "GLK-Class",
    "car_type": "SUV"
  },
  {
    "year": 2013,
    "manufacturer_name": "Mercedes-Benz",
    "model_name": "SL-Class",
    "car_type": "Convertible"
  },
  {
    "year": 2013,
    "manufacturer_name": "MINI",
    "model_name": "Hardtop",
    "car_type": "Hatchback"
  },
  {
    "year": 2013,
    "manufacturer_name": "Mercedes-Benz",
    "model_name": "GL-Class",
    "car_type": "SUV"
  },
  {
    "year": 2013,
    "manufacturer_name": "Mercedes-Benz",
    "model_name": "M-Class",
    "car_type": "SUV"
  },
  {
    "year": 2013,
    "manufacturer_name": "MAZDA",
    "model_name": "MAZDA6",
    "car_type": "Sedan"
  },
  {
    "year": 2013,
    "manufacturer_name": "Mercedes-Benz",
    "model_name": "Sprinter 2500 Cargo",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2013,
    "manufacturer_name": "MINI",
    "model_name": "Clubman",
    "car_type": "Hatchback"
  },
  {
    "year": 2013,
    "manufacturer_name": "Mercedes-Benz",
    "model_name": "CL-Class",
    "car_type": "Coupe"
  },
  {
    "year": 2013,
    "manufacturer_name": "Mercedes-Benz",
    "model_name": "SLS-Class",
    "car_type": "Coupe, Convertible"
  },
  {
    "year": 2013,
    "manufacturer_name": "Mercedes-Benz",
    "model_name": "S-Class",
    "car_type": "Sedan"
  },
  {
    "year": 2013,
    "manufacturer_name": "Mercedes-Benz",
    "model_name": "Sprinter 2500 Crew",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2013,
    "manufacturer_name": "MINI",
    "model_name": "Coupe",
    "car_type": "Coupe"
  },
  {
    "year": 2013,
    "manufacturer_name": "Mercedes-Benz",
    "model_name": "SLK-Class",
    "car_type": "Convertible"
  },
  {
    "year": 2013,
    "manufacturer_name": "Mitsubishi",
    "model_name": "Outlander",
    "car_type": "SUV"
  },
  {
    "year": 2013,
    "manufacturer_name": "Mercedes-Benz",
    "model_name": "CLS-Class",
    "car_type": "Coupe"
  },
  {
    "year": 2013,
    "manufacturer_name": "Mercedes-Benz",
    "model_name": "Sprinter 3500 Cargo",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2013,
    "manufacturer_name": "Mitsubishi",
    "model_name": "Lancer",
    "car_type": "Sedan, Hatchback"
  },
  {
    "year": 2013,
    "manufacturer_name": "Nissan",
    "model_name": "Altima",
    "car_type": "Sedan, Coupe"
  },
  {
    "year": 2013,
    "manufacturer_name": "Nissan",
    "model_name": "Armada",
    "car_type": "SUV"
  },
  {
    "year": 2013,
    "manufacturer_name": "Nissan",
    "model_name": "370Z",
    "car_type": "Coupe, Convertible"
  },
  {
    "year": 2013,
    "manufacturer_name": "MINI",
    "model_name": "Roadster",
    "car_type": "Convertible"
  },
  {
    "year": 2013,
    "manufacturer_name": "Nissan",
    "model_name": "Frontier Crew Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2013,
    "manufacturer_name": "Nissan",
    "model_name": "Murano",
    "car_type": "SUV"
  },
  {
    "year": 2013,
    "manufacturer_name": "Nissan",
    "model_name": "NV200",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2013,
    "manufacturer_name": "Porsche",
    "model_name": "Boxster",
    "car_type": "Convertible"
  },
  {
    "year": 2013,
    "manufacturer_name": "Nissan",
    "model_name": "Frontier King Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2013,
    "manufacturer_name": "Nissan",
    "model_name": "Pathfinder",
    "car_type": "SUV"
  },
  {
    "year": 2013,
    "manufacturer_name": "Nissan",
    "model_name": "Rogue",
    "car_type": "SUV"
  },
  {
    "year": 2013,
    "manufacturer_name": "MINI",
    "model_name": "Paceman",
    "car_type": "Hatchback"
  },
  {
    "year": 2013,
    "manufacturer_name": "Mitsubishi",
    "model_name": "Outlander Sport",
    "car_type": "SUV"
  },
  {
    "year": 2013,
    "manufacturer_name": "Nissan",
    "model_name": "NV1500 Cargo",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2013,
    "manufacturer_name": "Nissan",
    "model_name": "NV3500 HD Passenger",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2013,
    "manufacturer_name": "Nissan",
    "model_name": "GT-R",
    "car_type": "Coupe"
  },
  {
    "year": 2013,
    "manufacturer_name": "Nissan",
    "model_name": "NV2500 HD Cargo",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2013,
    "manufacturer_name": "Porsche",
    "model_name": "911",
    "car_type": "Coupe, Convertible"
  },
  {
    "year": 2013,
    "manufacturer_name": "Nissan",
    "model_name": "Maxima",
    "car_type": "Sedan"
  },
  {
    "year": 2013,
    "manufacturer_name": "Porsche",
    "model_name": "Panamera",
    "car_type": "Sedan"
  },
  {
    "year": 2013,
    "manufacturer_name": "Ram",
    "model_name": "1500 Crew Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2013,
    "manufacturer_name": "Nissan",
    "model_name": "Titan Crew Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2013,
    "manufacturer_name": "MINI",
    "model_name": "Convertible",
    "car_type": "Convertible"
  },
  {
    "year": 2013,
    "manufacturer_name": "Nissan",
    "model_name": "Xterra",
    "car_type": "SUV"
  },
  {
    "year": 2013,
    "manufacturer_name": "Nissan",
    "model_name": "NV3500 HD Cargo",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2013,
    "manufacturer_name": "Ram",
    "model_name": "2500 Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2013,
    "manufacturer_name": "Nissan",
    "model_name": "Titan King Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2013,
    "manufacturer_name": "Nissan",
    "model_name": "Versa",
    "car_type": "Sedan"
  },
  {
    "year": 2013,
    "manufacturer_name": "Nissan",
    "model_name": "cube",
    "car_type": "Wagon"
  },
  {
    "year": 2013,
    "manufacturer_name": "Nissan",
    "model_name": "LEAF",
    "car_type": "Hatchback"
  },
  {
    "year": 2013,
    "manufacturer_name": "Nissan",
    "model_name": "JUKE",
    "car_type": "SUV"
  },
  {
    "year": 2013,
    "manufacturer_name": "Nissan",
    "model_name": "Quest",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2013,
    "manufacturer_name": "Nissan",
    "model_name": "Sentra",
    "car_type": "Sedan"
  },
  {
    "year": 2013,
    "manufacturer_name": "Porsche",
    "model_name": "Cayenne",
    "car_type": "SUV"
  },
  {
    "year": 2013,
    "manufacturer_name": "Ram",
    "model_name": "1500 Quad Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2013,
    "manufacturer_name": "Ram",
    "model_name": "3500 Mega Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2013,
    "manufacturer_name": "Ram",
    "model_name": "3500 Crew Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2013,
    "manufacturer_name": "Rolls-Royce",
    "model_name": "Phantom",
    "car_type": "Sedan, Coupe, Convertible"
  },
  {
    "year": 2013,
    "manufacturer_name": "Scion",
    "model_name": "FR-S",
    "car_type": "Coupe"
  },
  {
    "year": 2013,
    "manufacturer_name": "Rolls-Royce",
    "model_name": "Ghost",
    "car_type": "Sedan"
  },
  {
    "year": 2013,
    "manufacturer_name": "Scion",
    "model_name": "xB",
    "car_type": "Hatchback"
  },
  {
    "year": 2013,
    "manufacturer_name": "Ram",
    "model_name": "2500 Mega Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2013,
    "manufacturer_name": "Ram",
    "model_name": "C/V Tradesman",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2013,
    "manufacturer_name": "Ram",
    "model_name": "1500 Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2013,
    "manufacturer_name": "Subaru",
    "model_name": "BRZ",
    "car_type": "Coupe"
  },
  {
    "year": 2013,
    "manufacturer_name": "Scion",
    "model_name": "xD",
    "car_type": "Hatchback"
  },
  {
    "year": 2013,
    "manufacturer_name": "Ram",
    "model_name": "2500 Crew Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2013,
    "manufacturer_name": "Ram",
    "model_name": "3500 Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2013,
    "manufacturer_name": "Scion",
    "model_name": "tC",
    "car_type": "Coupe"
  },
  {
    "year": 2013,
    "manufacturer_name": "smart",
    "model_name": "fortwo",
    "car_type": "Hatchback, Convertible"
  },
  {
    "year": 2013,
    "manufacturer_name": "Subaru",
    "model_name": "XV Crosstrek",
    "car_type": "SUV"
  },
  {
    "year": 2013,
    "manufacturer_name": "Subaru",
    "model_name": "Impreza",
    "car_type": "Sedan, Wagon"
  },
  {
    "year": 2013,
    "manufacturer_name": "Subaru",
    "model_name": "Forester",
    "car_type": "SUV"
  },
  {
    "year": 2013,
    "manufacturer_name": "Subaru",
    "model_name": "Legacy",
    "car_type": "Sedan"
  },
  {
    "year": 2013,
    "manufacturer_name": "Suzuki",
    "model_name": "SX4",
    "car_type": "Sedan, Hatchback"
  },
  {
    "year": 2013,
    "manufacturer_name": "SRT",
    "model_name": "Viper",
    "car_type": "Coupe"
  },
  {
    "year": 2013,
    "manufacturer_name": "Suzuki",
    "model_name": "Kizashi",
    "car_type": "Sedan"
  },
  {
    "year": 2013,
    "manufacturer_name": "Subaru",
    "model_name": "Outback",
    "car_type": "Wagon"
  },
  {
    "year": 2013,
    "manufacturer_name": "Tesla",
    "model_name": "Model S",
    "car_type": "Sedan"
  },
  {
    "year": 2013,
    "manufacturer_name": "Suzuki",
    "model_name": "Grand Vitara",
    "car_type": "SUV"
  },
  {
    "year": 2013,
    "manufacturer_name": "Scion",
    "model_name": "iQ",
    "car_type": "Hatchback"
  },
  {
    "year": 2013,
    "manufacturer_name": "Subaru",
    "model_name": "Tribeca",
    "car_type": "SUV"
  },
  {
    "year": 2013,
    "manufacturer_name": "smart",
    "model_name": "fortwo electric drive",
    "car_type": "Hatchback, Convertible"
  },
  {
    "year": 2013,
    "manufacturer_name": "Toyota",
    "model_name": "Corolla",
    "car_type": "Sedan"
  },
  {
    "year": 2013,
    "manufacturer_name": "Toyota",
    "model_name": "Sequoia",
    "car_type": "SUV"
  },
  {
    "year": 2013,
    "manufacturer_name": "Toyota",
    "model_name": "Avalon",
    "car_type": "Sedan"
  },
  {
    "year": 2013,
    "manufacturer_name": "Toyota",
    "model_name": "4Runner",
    "car_type": "SUV"
  },
  {
    "year": 2013,
    "manufacturer_name": "Toyota",
    "model_name": "Prius v",
    "car_type": "Wagon"
  },
  {
    "year": 2013,
    "manufacturer_name": "Toyota",
    "model_name": "Matrix",
    "car_type": "Wagon"
  },
  {
    "year": 2013,
    "manufacturer_name": "Toyota",
    "model_name": "FJ Cruiser",
    "car_type": "SUV"
  },
  {
    "year": 2013,
    "manufacturer_name": "Toyota",
    "model_name": "Tacoma Double Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2013,
    "manufacturer_name": "Toyota",
    "model_name": "Land Cruiser",
    "car_type": "SUV"
  },
  {
    "year": 2013,
    "manufacturer_name": "Toyota",
    "model_name": "RAV4",
    "car_type": "SUV"
  },
  {
    "year": 2013,
    "manufacturer_name": "Toyota",
    "model_name": "Highlander",
    "car_type": "SUV"
  },
  {
    "year": 2013,
    "manufacturer_name": "Toyota",
    "model_name": "Prius c",
    "car_type": "Hatchback"
  },
  {
    "year": 2013,
    "manufacturer_name": "Toyota",
    "model_name": "Prius Plug-in Hybrid",
    "car_type": "Hatchback"
  },
  {
    "year": 2013,
    "manufacturer_name": "Toyota",
    "model_name": "Tundra Double Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2013,
    "manufacturer_name": "Toyota",
    "model_name": "Prius",
    "car_type": "Hatchback"
  },
  {
    "year": 2013,
    "manufacturer_name": "Toyota",
    "model_name": "Camry",
    "car_type": "Sedan"
  },
  {
    "year": 2013,
    "manufacturer_name": "Toyota",
    "model_name": "Sienna",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2013,
    "manufacturer_name": "Toyota",
    "model_name": "Tacoma Access Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2013,
    "manufacturer_name": "Toyota",
    "model_name": "Tundra CrewMax",
    "car_type": "Pickup"
  },
  {
    "year": 2013,
    "manufacturer_name": "Toyota",
    "model_name": "Venza",
    "car_type": "SUV"
  },
  {
    "year": 2013,
    "manufacturer_name": "Volkswagen",
    "model_name": "Golf",
    "car_type": "Hatchback"
  },
  {
    "year": 2013,
    "manufacturer_name": "Toyota",
    "model_name": "Yaris",
    "car_type": "Hatchback"
  },
  {
    "year": 2013,
    "manufacturer_name": "Volvo",
    "model_name": "C30",
    "car_type": "Hatchback"
  },
  {
    "year": 2013,
    "manufacturer_name": "Volvo",
    "model_name": "S80",
    "car_type": "Sedan"
  },
  {
    "year": 2013,
    "manufacturer_name": "Volkswagen",
    "model_name": "Jetta",
    "car_type": "Sedan"
  },
  {
    "year": 2013,
    "manufacturer_name": "Volvo",
    "model_name": "XC70",
    "car_type": "Wagon"
  },
  {
    "year": 2013,
    "manufacturer_name": "Volkswagen",
    "model_name": "Beetle",
    "car_type": "Hatchback, Convertible"
  },
  {
    "year": 2013,
    "manufacturer_name": "Toyota",
    "model_name": "Tacoma Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2013,
    "manufacturer_name": "Volkswagen",
    "model_name": "Tiguan",
    "car_type": "SUV"
  },
  {
    "year": 2013,
    "manufacturer_name": "Toyota",
    "model_name": "Tundra Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2013,
    "manufacturer_name": "Volkswagen",
    "model_name": "CC",
    "car_type": "Sedan"
  },
  {
    "year": 2013,
    "manufacturer_name": "Volvo",
    "model_name": "S60",
    "car_type": "Sedan"
  },
  {
    "year": 2013,
    "manufacturer_name": "Volkswagen",
    "model_name": "Touareg",
    "car_type": "SUV"
  },
  {
    "year": 2013,
    "manufacturer_name": "Volkswagen",
    "model_name": "Routan",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2013,
    "manufacturer_name": "Volvo",
    "model_name": "XC90",
    "car_type": "SUV"
  },
  {
    "year": 2013,
    "manufacturer_name": "Volkswagen",
    "model_name": "Eos",
    "car_type": "Convertible"
  },
  {
    "year": 2013,
    "manufacturer_name": "Volkswagen",
    "model_name": "Passat",
    "car_type": "Sedan"
  },
  {
    "year": 2013,
    "manufacturer_name": "Volkswagen",
    "model_name": "Jetta SportWagen",
    "car_type": "Wagon"
  },
  {
    "year": 2013,
    "manufacturer_name": "Volkswagen",
    "model_name": "GTI",
    "car_type": "Hatchback"
  },
  {
    "year": 2013,
    "manufacturer_name": "Volvo",
    "model_name": "C70",
    "car_type": "Convertible"
  },
  {
    "year": 2013,
    "manufacturer_name": "Volvo",
    "model_name": "XC60",
    "car_type": "SUV"
  },
  {
    "year": 2012,
    "manufacturer_name": "Acura",
    "model_name": "RDX",
    "car_type": "SUV"
  },
  {
    "year": 2012,
    "manufacturer_name": "Acura",
    "model_name": "TSX",
    "car_type": "Wagon, Sedan"
  },
  {
    "year": 2012,
    "manufacturer_name": "Audi",
    "model_name": "Q5",
    "car_type": "SUV"
  },
  {
    "year": 2012,
    "manufacturer_name": "Audi",
    "model_name": "R8",
    "car_type": "Coupe, Convertible"
  },
  {
    "year": 2012,
    "manufacturer_name": "Audi",
    "model_name": "A4",
    "car_type": "Sedan, Wagon"
  },
  {
    "year": 2012,
    "manufacturer_name": "Aston Martin",
    "model_name": "Vantage",
    "car_type": "Coupe, Convertible"
  },
  {
    "year": 2012,
    "manufacturer_name": "Acura",
    "model_name": "MDX",
    "car_type": "SUV"
  },
  {
    "year": 2012,
    "manufacturer_name": "Audi",
    "model_name": "A8",
    "car_type": "Sedan"
  },
  {
    "year": 2012,
    "manufacturer_name": "Acura",
    "model_name": "RL",
    "car_type": "Sedan"
  },
  {
    "year": 2012,
    "manufacturer_name": "Acura",
    "model_name": "TL",
    "car_type": "Sedan"
  },
  {
    "year": 2012,
    "manufacturer_name": "Acura",
    "model_name": "ZDX",
    "car_type": "SUV"
  },
  {
    "year": 2012,
    "manufacturer_name": "Aston Martin",
    "model_name": "Rapide",
    "car_type": "Sedan"
  },
  {
    "year": 2012,
    "manufacturer_name": "Audi",
    "model_name": "A5",
    "car_type": "Convertible, Coupe"
  },
  {
    "year": 2012,
    "manufacturer_name": "Audi",
    "model_name": "A7",
    "car_type": "Sedan"
  },
  {
    "year": 2012,
    "manufacturer_name": "Aston Martin",
    "model_name": "DB9",
    "car_type": "Coupe, Convertible"
  },
  {
    "year": 2012,
    "manufacturer_name": "Audi",
    "model_name": "A3",
    "car_type": "Wagon"
  },
  {
    "year": 2012,
    "manufacturer_name": "Bentley",
    "model_name": "Continental",
    "car_type": "Coupe, Sedan, Convertible"
  },
  {
    "year": 2012,
    "manufacturer_name": "Aston Martin",
    "model_name": "DBS",
    "car_type": "Coupe, Convertible"
  },
  {
    "year": 2012,
    "manufacturer_name": "Audi",
    "model_name": "Q7",
    "car_type": "SUV"
  },
  {
    "year": 2012,
    "manufacturer_name": "Bentley",
    "model_name": "Mulsanne",
    "car_type": "Sedan"
  },
  {
    "year": 2012,
    "manufacturer_name": "Audi",
    "model_name": "A6",
    "car_type": "Sedan"
  },
  {
    "year": 2012,
    "manufacturer_name": "Aston Martin",
    "model_name": "Virage",
    "car_type": "Coupe, Convertible"
  },
  {
    "year": 2012,
    "manufacturer_name": "BMW",
    "model_name": "6 Series",
    "car_type": "Convertible, Coupe"
  },
  {
    "year": 2012,
    "manufacturer_name": "Buick",
    "model_name": "Regal",
    "car_type": "Sedan"
  },
  {
    "year": 2012,
    "manufacturer_name": "BMW",
    "model_name": "X3",
    "car_type": "SUV"
  },
  {
    "year": 2012,
    "manufacturer_name": "BMW",
    "model_name": "1 Series",
    "car_type": "Convertible, Coupe"
  },
  {
    "year": 2012,
    "manufacturer_name": "BMW",
    "model_name": "Z4",
    "car_type": "Convertible"
  },
  {
    "year": 2012,
    "manufacturer_name": "BMW",
    "model_name": "X6 M",
    "car_type": "SUV"
  },
  {
    "year": 2012,
    "manufacturer_name": "BMW",
    "model_name": "X5",
    "car_type": "SUV"
  },
  {
    "year": 2012,
    "manufacturer_name": "Audi",
    "model_name": "S5",
    "car_type": "Coupe, Convertible"
  },
  {
    "year": 2012,
    "manufacturer_name": "Buick",
    "model_name": "LaCrosse",
    "car_type": "Sedan"
  },
  {
    "year": 2012,
    "manufacturer_name": "BMW",
    "model_name": "M6",
    "car_type": "Convertible"
  },
  {
    "year": 2012,
    "manufacturer_name": "Cadillac",
    "model_name": "Escalade",
    "car_type": "SUV"
  },
  {
    "year": 2012,
    "manufacturer_name": "BMW",
    "model_name": "X5 M",
    "car_type": "SUV"
  },
  {
    "year": 2012,
    "manufacturer_name": "BMW",
    "model_name": "3 Series",
    "car_type": "Coupe, Convertible, Wagon, Sedan"
  },
  {
    "year": 2012,
    "manufacturer_name": "Audi",
    "model_name": "TT",
    "car_type": "Coupe, Convertible"
  },
  {
    "year": 2012,
    "manufacturer_name": "Audi",
    "model_name": "S4",
    "car_type": "Sedan"
  },
  {
    "year": 2012,
    "manufacturer_name": "Buick",
    "model_name": "Verano",
    "car_type": "Sedan"
  },
  {
    "year": 2012,
    "manufacturer_name": "BMW",
    "model_name": "M3",
    "car_type": "Convertible, Coupe"
  },
  {
    "year": 2012,
    "manufacturer_name": "Chevrolet",
    "model_name": "Camaro",
    "car_type": "Coupe, Convertible"
  },
  {
    "year": 2012,
    "manufacturer_name": "BMW",
    "model_name": "5 Series",
    "car_type": "Sedan"
  },
  {
    "year": 2012,
    "manufacturer_name": "BMW",
    "model_name": "X6",
    "car_type": "SUV"
  },
  {
    "year": 2012,
    "manufacturer_name": "Cadillac",
    "model_name": "CTS",
    "car_type": "Sedan, Coupe, Wagon"
  },
  {
    "year": 2012,
    "manufacturer_name": "Cadillac",
    "model_name": "Escalade ESV",
    "car_type": "SUV"
  },
  {
    "year": 2012,
    "manufacturer_name": "BMW",
    "model_name": "7 Series",
    "car_type": "Sedan"
  },
  {
    "year": 2012,
    "manufacturer_name": "Chevrolet",
    "model_name": "Cruze",
    "car_type": "Sedan"
  },
  {
    "year": 2012,
    "manufacturer_name": "Cadillac",
    "model_name": "SRX",
    "car_type": "SUV"
  },
  {
    "year": 2012,
    "manufacturer_name": "Buick",
    "model_name": "Enclave",
    "car_type": "SUV"
  },
  {
    "year": 2012,
    "manufacturer_name": "Chevrolet",
    "model_name": "Captiva Sport",
    "car_type": "SUV"
  },
  {
    "year": 2012,
    "manufacturer_name": "Cadillac",
    "model_name": "Escalade EXT",
    "car_type": "Pickup"
  },
  {
    "year": 2012,
    "manufacturer_name": "Chevrolet",
    "model_name": "Corvette",
    "car_type": "Convertible, Coupe"
  },
  {
    "year": 2012,
    "manufacturer_name": "Chevrolet",
    "model_name": "Colorado Extended Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2012,
    "manufacturer_name": "Chevrolet",
    "model_name": "Colorado Crew Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2012,
    "manufacturer_name": "Chevrolet",
    "model_name": "Equinox",
    "car_type": "SUV"
  },
  {
    "year": 2012,
    "manufacturer_name": "Chevrolet",
    "model_name": "Avalanche",
    "car_type": "SUV"
  },
  {
    "year": 2012,
    "manufacturer_name": "Chevrolet",
    "model_name": "Colorado Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2012,
    "manufacturer_name": "Chevrolet",
    "model_name": "Express 1500 Cargo",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2012,
    "manufacturer_name": "Chevrolet",
    "model_name": "Express 2500 Cargo",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2012,
    "manufacturer_name": "Chevrolet",
    "model_name": "Express 1500 Passenger",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2012,
    "manufacturer_name": "Chevrolet",
    "model_name": "Malibu",
    "car_type": "Sedan"
  },
  {
    "year": 2012,
    "manufacturer_name": "Chevrolet",
    "model_name": "Express 3500 Passenger",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2012,
    "manufacturer_name": "Chevrolet",
    "model_name": "Express 2500 Passenger",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2012,
    "manufacturer_name": "Chevrolet",
    "model_name": "Silverado 1500 Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2012,
    "manufacturer_name": "Chevrolet",
    "model_name": "Silverado 1500 Extended Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2012,
    "manufacturer_name": "Chevrolet",
    "model_name": "Silverado 1500 Crew Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2012,
    "manufacturer_name": "Chevrolet",
    "model_name": "Express 3500 Cargo",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2012,
    "manufacturer_name": "Chevrolet",
    "model_name": "Impala",
    "car_type": "Sedan"
  },
  {
    "year": 2012,
    "manufacturer_name": "Chevrolet",
    "model_name": "Suburban 1500",
    "car_type": "SUV"
  },
  {
    "year": 2012,
    "manufacturer_name": "Chevrolet",
    "model_name": "Sonic",
    "car_type": "Sedan, Hatchback"
  },
  {
    "year": 2012,
    "manufacturer_name": "Chevrolet",
    "model_name": "Silverado 2500 HD Extended Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2012,
    "manufacturer_name": "Chevrolet",
    "model_name": "Suburban 2500",
    "car_type": "SUV"
  },
  {
    "year": 2012,
    "manufacturer_name": "Chevrolet",
    "model_name": "Volt",
    "car_type": "Sedan"
  },
  {
    "year": 2012,
    "manufacturer_name": "Chevrolet",
    "model_name": "Silverado 3500 HD Extended Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2012,
    "manufacturer_name": "Chevrolet",
    "model_name": "Silverado 2500 HD Crew Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2012,
    "manufacturer_name": "Chevrolet",
    "model_name": "Silverado 3500 HD Crew Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2012,
    "manufacturer_name": "Chevrolet",
    "model_name": "Silverado 2500 HD Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2012,
    "manufacturer_name": "Dodge",
    "model_name": "Caliber",
    "car_type": "Wagon"
  },
  {
    "year": 2012,
    "manufacturer_name": "Chevrolet",
    "model_name": "Silverado 3500 HD Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2012,
    "manufacturer_name": "Chevrolet",
    "model_name": "Traverse",
    "car_type": "SUV"
  },
  {
    "year": 2012,
    "manufacturer_name": "Chevrolet",
    "model_name": "Tahoe",
    "car_type": "SUV"
  },
  {
    "year": 2012,
    "manufacturer_name": "Chrysler",
    "model_name": "Town & Country",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2012,
    "manufacturer_name": "Ferrari",
    "model_name": "California",
    "car_type": "Convertible"
  },
  {
    "year": 2012,
    "manufacturer_name": "Ferrari",
    "model_name": "458 Italia",
    "car_type": "Coupe"
  },
  {
    "year": 2012,
    "manufacturer_name": "Dodge",
    "model_name": "Challenger",
    "car_type": "Coupe"
  },
  {
    "year": 2012,
    "manufacturer_name": "Dodge",
    "model_name": "Journey",
    "car_type": "SUV"
  },
  {
    "year": 2012,
    "manufacturer_name": "Chrysler",
    "model_name": "200",
    "car_type": "Sedan, Convertible"
  },
  {
    "year": 2012,
    "manufacturer_name": "Ford",
    "model_name": "E250 Cargo",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2012,
    "manufacturer_name": "Dodge",
    "model_name": "Charger",
    "car_type": "Sedan"
  },
  {
    "year": 2012,
    "manufacturer_name": "Dodge",
    "model_name": "Grand Caravan Passenger",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2012,
    "manufacturer_name": "Ford",
    "model_name": "Explorer",
    "car_type": "SUV"
  },
  {
    "year": 2012,
    "manufacturer_name": "Dodge",
    "model_name": "Avenger",
    "car_type": "Sedan"
  },
  {
    "year": 2012,
    "manufacturer_name": "Ford",
    "model_name": "Edge",
    "car_type": "SUV"
  },
  {
    "year": 2012,
    "manufacturer_name": "FIAT",
    "model_name": "500",
    "car_type": "Hatchback, Convertible"
  },
  {
    "year": 2012,
    "manufacturer_name": "Dodge",
    "model_name": "Durango",
    "car_type": "SUV"
  },
  {
    "year": 2012,
    "manufacturer_name": "Chrysler",
    "model_name": "300",
    "car_type": "Sedan"
  },
  {
    "year": 2012,
    "manufacturer_name": "Ford",
    "model_name": "E150 Passenger",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2012,
    "manufacturer_name": "Fisker",
    "model_name": "Karma",
    "car_type": "Sedan"
  },
  {
    "year": 2012,
    "manufacturer_name": "Ferrari",
    "model_name": "FF",
    "car_type": "Coupe"
  },
  {
    "year": 2012,
    "manufacturer_name": "Ford",
    "model_name": "E150 Cargo",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2012,
    "manufacturer_name": "Ford",
    "model_name": "E350 Super Duty Passenger",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2012,
    "manufacturer_name": "Ford",
    "model_name": "E350 Super Duty Cargo",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2012,
    "manufacturer_name": "Ford",
    "model_name": "F250 Super Duty Super Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2012,
    "manufacturer_name": "Ford",
    "model_name": "F450 Super Duty Crew Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2012,
    "manufacturer_name": "Ford",
    "model_name": "F150 Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2012,
    "manufacturer_name": "Ford",
    "model_name": "F250 Super Duty Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2012,
    "manufacturer_name": "Ford",
    "model_name": "Expedition",
    "car_type": "SUV"
  },
  {
    "year": 2012,
    "manufacturer_name": "Ford",
    "model_name": "Fiesta",
    "car_type": "Sedan, Hatchback"
  },
  {
    "year": 2012,
    "manufacturer_name": "Ford",
    "model_name": "Escape",
    "car_type": "SUV"
  },
  {
    "year": 2012,
    "manufacturer_name": "Ford",
    "model_name": "F250 Super Duty Crew Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2012,
    "manufacturer_name": "Ford",
    "model_name": "Expedition EL",
    "car_type": "SUV"
  },
  {
    "year": 2012,
    "manufacturer_name": "Ford",
    "model_name": "Focus",
    "car_type": "Sedan, Hatchback"
  },
  {
    "year": 2012,
    "manufacturer_name": "GMC",
    "model_name": "Canyon Crew Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2012,
    "manufacturer_name": "Ford",
    "model_name": "Taurus",
    "car_type": "Sedan"
  },
  {
    "year": 2012,
    "manufacturer_name": "Ford",
    "model_name": "F150 Super Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2012,
    "manufacturer_name": "Ford",
    "model_name": "F350 Super Duty Super Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2012,
    "manufacturer_name": "Ford",
    "model_name": "Mustang",
    "car_type": "Coupe, Convertible"
  },
  {
    "year": 2012,
    "manufacturer_name": "Ford",
    "model_name": "Transit Connect Passenger",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2012,
    "manufacturer_name": "Ford",
    "model_name": "F150 SuperCrew Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2012,
    "manufacturer_name": "Ford",
    "model_name": "Fusion",
    "car_type": "Sedan"
  },
  {
    "year": 2012,
    "manufacturer_name": "Ford",
    "model_name": "F350 Super Duty Crew Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2012,
    "manufacturer_name": "Ford",
    "model_name": "Flex",
    "car_type": "SUV"
  },
  {
    "year": 2012,
    "manufacturer_name": "Ford",
    "model_name": "F350 Super Duty Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2012,
    "manufacturer_name": "Ford",
    "model_name": "Transit Connect Cargo",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2012,
    "manufacturer_name": "GMC",
    "model_name": "Acadia",
    "car_type": "SUV"
  },
  {
    "year": 2012,
    "manufacturer_name": "GMC",
    "model_name": "Canyon Extended Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2012,
    "manufacturer_name": "GMC",
    "model_name": "Sierra 1500 Extended Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2012,
    "manufacturer_name": "GMC",
    "model_name": "Savana 2500 Passenger",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2012,
    "manufacturer_name": "GMC",
    "model_name": "Savana 2500 Cargo",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2012,
    "manufacturer_name": "GMC",
    "model_name": "Savana 1500 Cargo",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2012,
    "manufacturer_name": "GMC",
    "model_name": "Canyon Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2012,
    "manufacturer_name": "GMC",
    "model_name": "Sierra 1500 Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2012,
    "manufacturer_name": "GMC",
    "model_name": "Savana 1500 Passenger",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2012,
    "manufacturer_name": "GMC",
    "model_name": "Savana 3500 Cargo",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2012,
    "manufacturer_name": "GMC",
    "model_name": "Sierra 2500 HD Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2012,
    "manufacturer_name": "GMC",
    "model_name": "Sierra 3500 HD Crew Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2012,
    "manufacturer_name": "GMC",
    "model_name": "Sierra 1500 Crew Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2012,
    "manufacturer_name": "GMC",
    "model_name": "Sierra 2500 HD Crew Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2012,
    "manufacturer_name": "GMC",
    "model_name": "Sierra 3500 HD Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2012,
    "manufacturer_name": "GMC",
    "model_name": "Savana 3500 Passenger",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2012,
    "manufacturer_name": "GMC",
    "model_name": "Yukon XL 1500",
    "car_type": "SUV"
  },
  {
    "year": 2012,
    "manufacturer_name": "GMC",
    "model_name": "Sierra 2500 HD Extended Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2012,
    "manufacturer_name": "GMC",
    "model_name": "Terrain",
    "car_type": "SUV"
  },
  {
    "year": 2012,
    "manufacturer_name": "Honda",
    "model_name": "Accord",
    "car_type": "Sedan, Coupe"
  },
  {
    "year": 2012,
    "manufacturer_name": "Hyundai",
    "model_name": "Azera",
    "car_type": "Sedan"
  },
  {
    "year": 2012,
    "manufacturer_name": "Honda",
    "model_name": "Insight",
    "car_type": "Hatchback"
  },
  {
    "year": 2012,
    "manufacturer_name": "Honda",
    "model_name": "Civic",
    "car_type": "Coupe, Sedan"
  },
  {
    "year": 2012,
    "manufacturer_name": "GMC",
    "model_name": "Sierra 3500 HD Extended Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2012,
    "manufacturer_name": "Honda",
    "model_name": "Crosstour",
    "car_type": "SUV"
  },
  {
    "year": 2012,
    "manufacturer_name": "Honda",
    "model_name": "Fit",
    "car_type": "Hatchback"
  },
  {
    "year": 2012,
    "manufacturer_name": "Honda",
    "model_name": "CR-V",
    "car_type": "SUV"
  },
  {
    "year": 2012,
    "manufacturer_name": "GMC",
    "model_name": "Yukon",
    "car_type": "SUV"
  },
  {
    "year": 2012,
    "manufacturer_name": "Hyundai",
    "model_name": "Accent",
    "car_type": "Sedan, Hatchback"
  },
  {
    "year": 2012,
    "manufacturer_name": "Honda",
    "model_name": "Odyssey",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2012,
    "manufacturer_name": "Hyundai",
    "model_name": "Elantra",
    "car_type": "Sedan, Wagon"
  },
  {
    "year": 2012,
    "manufacturer_name": "Honda",
    "model_name": "Pilot",
    "car_type": "SUV"
  },
  {
    "year": 2012,
    "manufacturer_name": "GMC",
    "model_name": "Yukon XL 2500",
    "car_type": "SUV"
  },
  {
    "year": 2012,
    "manufacturer_name": "Hyundai",
    "model_name": "Equus",
    "car_type": "Sedan"
  },
  {
    "year": 2012,
    "manufacturer_name": "Honda",
    "model_name": "Ridgeline",
    "car_type": "Pickup"
  },
  {
    "year": 2012,
    "manufacturer_name": "Honda",
    "model_name": "CR-Z",
    "car_type": "Coupe"
  },
  {
    "year": 2012,
    "manufacturer_name": "Hyundai",
    "model_name": "Genesis",
    "car_type": "Sedan"
  },
  {
    "year": 2012,
    "manufacturer_name": "INFINITI",
    "model_name": "G",
    "car_type": "Coupe, Convertible, Sedan"
  },
  {
    "year": 2012,
    "manufacturer_name": "Hyundai",
    "model_name": "Santa Fe",
    "car_type": "SUV"
  },
  {
    "year": 2012,
    "manufacturer_name": "INFINITI",
    "model_name": "EX",
    "car_type": "SUV"
  },
  {
    "year": 2012,
    "manufacturer_name": "Hyundai",
    "model_name": "Veracruz",
    "car_type": "SUV"
  },
  {
    "year": 2012,
    "manufacturer_name": "Hyundai",
    "model_name": "Genesis Coupe",
    "car_type": "Coupe"
  },
  {
    "year": 2012,
    "manufacturer_name": "Hyundai",
    "model_name": "Sonata",
    "car_type": "Sedan"
  },
  {
    "year": 2012,
    "manufacturer_name": "Hyundai",
    "model_name": "Veloster",
    "car_type": "Coupe"
  },
  {
    "year": 2012,
    "manufacturer_name": "INFINITI",
    "model_name": "QX",
    "car_type": "SUV"
  },
  {
    "year": 2012,
    "manufacturer_name": "Jeep",
    "model_name": "Liberty",
    "car_type": "SUV"
  },
  {
    "year": 2012,
    "manufacturer_name": "INFINITI",
    "model_name": "FX",
    "car_type": "SUV"
  },
  {
    "year": 2012,
    "manufacturer_name": "Jaguar",
    "model_name": "XJ",
    "car_type": "Sedan"
  },
  {
    "year": 2012,
    "manufacturer_name": "Jaguar",
    "model_name": "XF",
    "car_type": "Sedan"
  },
  {
    "year": 2012,
    "manufacturer_name": "Hyundai",
    "model_name": "Tucson",
    "car_type": "SUV"
  },
  {
    "year": 2012,
    "manufacturer_name": "Jaguar",
    "model_name": "XK",
    "car_type": "Coupe, Convertible"
  },
  {
    "year": 2012,
    "manufacturer_name": "Jeep",
    "model_name": "Grand Cherokee",
    "car_type": "SUV"
  },
  {
    "year": 2012,
    "manufacturer_name": "INFINITI",
    "model_name": "M",
    "car_type": "Sedan"
  },
  {
    "year": 2012,
    "manufacturer_name": "Jeep",
    "model_name": "Compass",
    "car_type": "SUV"
  },
  {
    "year": 2012,
    "manufacturer_name": "Jeep",
    "model_name": "Patriot",
    "car_type": "SUV"
  },
  {
    "year": 2012,
    "manufacturer_name": "Kia",
    "model_name": "Forte",
    "car_type": "Sedan, Hatchback, Coupe"
  },
  {
    "year": 2012,
    "manufacturer_name": "Lamborghini",
    "model_name": "Aventador",
    "car_type": "Coupe"
  },
  {
    "year": 2012,
    "manufacturer_name": "Lincoln",
    "model_name": "MKS",
    "car_type": "Sedan"
  },
  {
    "year": 2012,
    "manufacturer_name": "Land Rover",
    "model_name": "LR2",
    "car_type": "SUV"
  },
  {
    "year": 2012,
    "manufacturer_name": "Kia",
    "model_name": "Soul",
    "car_type": "Wagon"
  },
  {
    "year": 2012,
    "manufacturer_name": "Land Rover",
    "model_name": "Range Rover",
    "car_type": "SUV"
  },
  {
    "year": 2012,
    "manufacturer_name": "Lexus",
    "model_name": "ES",
    "car_type": "Sedan"
  },
  {
    "year": 2012,
    "manufacturer_name": "Jeep",
    "model_name": "Wrangler",
    "car_type": "SUV"
  },
  {
    "year": 2012,
    "manufacturer_name": "Kia",
    "model_name": "Rio",
    "car_type": "Hatchback, Sedan"
  },
  {
    "year": 2012,
    "manufacturer_name": "Lexus",
    "model_name": "IS",
    "car_type": "Sedan, Convertible"
  },
  {
    "year": 2012,
    "manufacturer_name": "Land Rover",
    "model_name": "Range Rover Evoque",
    "car_type": "SUV"
  },
  {
    "year": 2012,
    "manufacturer_name": "Lexus",
    "model_name": "HS",
    "car_type": "Sedan"
  },
  {
    "year": 2012,
    "manufacturer_name": "Lexus",
    "model_name": "LFA",
    "car_type": "Coupe"
  },
  {
    "year": 2012,
    "manufacturer_name": "Lexus",
    "model_name": "RX",
    "car_type": "SUV"
  },
  {
    "year": 2012,
    "manufacturer_name": "Kia",
    "model_name": "Sportage",
    "car_type": "SUV"
  },
  {
    "year": 2012,
    "manufacturer_name": "Lotus",
    "model_name": "Evora",
    "car_type": "Coupe"
  },
  {
    "year": 2012,
    "manufacturer_name": "Kia",
    "model_name": "Optima",
    "car_type": "Sedan"
  },
  {
    "year": 2012,
    "manufacturer_name": "Kia",
    "model_name": "Sedona",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2012,
    "manufacturer_name": "Kia",
    "model_name": "Sorento",
    "car_type": "SUV"
  },
  {
    "year": 2012,
    "manufacturer_name": "Land Rover",
    "model_name": "LR4",
    "car_type": "SUV"
  },
  {
    "year": 2012,
    "manufacturer_name": "Maserati",
    "model_name": "Quattroporte",
    "car_type": "Sedan"
  },
  {
    "year": 2012,
    "manufacturer_name": "Lexus",
    "model_name": "GX",
    "car_type": "SUV"
  },
  {
    "year": 2012,
    "manufacturer_name": "Lexus",
    "model_name": "CT",
    "car_type": "Hatchback"
  },
  {
    "year": 2012,
    "manufacturer_name": "Lincoln",
    "model_name": "Navigator L",
    "car_type": "SUV"
  },
  {
    "year": 2012,
    "manufacturer_name": "Lamborghini",
    "model_name": "Gallardo",
    "car_type": "Coupe, Convertible"
  },
  {
    "year": 2012,
    "manufacturer_name": "Maybach",
    "model_name": "62",
    "car_type": "Sedan"
  },
  {
    "year": 2012,
    "manufacturer_name": "Land Rover",
    "model_name": "Range Rover Sport",
    "car_type": "SUV"
  },
  {
    "year": 2012,
    "manufacturer_name": "Lexus",
    "model_name": "LS",
    "car_type": "Sedan"
  },
  {
    "year": 2012,
    "manufacturer_name": "Lincoln",
    "model_name": "Navigator",
    "car_type": "SUV"
  },
  {
    "year": 2012,
    "manufacturer_name": "Lincoln",
    "model_name": "MKX",
    "car_type": "SUV"
  },
  {
    "year": 2012,
    "manufacturer_name": "Lincoln",
    "model_name": "MKZ",
    "car_type": "Sedan"
  },
  {
    "year": 2012,
    "manufacturer_name": "Lincoln",
    "model_name": "MKT",
    "car_type": "SUV"
  },
  {
    "year": 2012,
    "manufacturer_name": "Maserati",
    "model_name": "GranTurismo",
    "car_type": "Coupe, Convertible"
  },
  {
    "year": 2012,
    "manufacturer_name": "MAZDA",
    "model_name": "MAZDA6",
    "car_type": "Sedan"
  },
  {
    "year": 2012,
    "manufacturer_name": "MAZDA",
    "model_name": "MX-5 Miata",
    "car_type": "Convertible"
  },
  {
    "year": 2012,
    "manufacturer_name": "Mercedes-Benz",
    "model_name": "Sprinter 2500 Cargo",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2012,
    "manufacturer_name": "MAZDA",
    "model_name": "MAZDA3",
    "car_type": "Hatchback, Sedan"
  },
  {
    "year": 2012,
    "manufacturer_name": "McLaren",
    "model_name": "MP4-12C",
    "car_type": "Coupe"
  },
  {
    "year": 2012,
    "manufacturer_name": "MAZDA",
    "model_name": "CX-7",
    "car_type": "SUV"
  },
  {
    "year": 2012,
    "manufacturer_name": "Mercedes-Benz",
    "model_name": "SLK-Class",
    "car_type": "Convertible"
  },
  {
    "year": 2012,
    "manufacturer_name": "Maybach",
    "model_name": "57",
    "car_type": "Sedan"
  },
  {
    "year": 2012,
    "manufacturer_name": "Mercedes-Benz",
    "model_name": "C-Class",
    "car_type": "Sedan, Coupe"
  },
  {
    "year": 2012,
    "manufacturer_name": "MAZDA",
    "model_name": "MAZDA2",
    "car_type": "Hatchback"
  },
  {
    "year": 2012,
    "manufacturer_name": "Mercedes-Benz",
    "model_name": "SL-Class",
    "car_type": "Convertible"
  },
  {
    "year": 2012,
    "manufacturer_name": "Mercedes-Benz",
    "model_name": "CL-Class",
    "car_type": "Coupe"
  },
  {
    "year": 2012,
    "manufacturer_name": "MAZDA",
    "model_name": "CX-9",
    "car_type": "SUV"
  },
  {
    "year": 2012,
    "manufacturer_name": "MINI",
    "model_name": "Hardtop",
    "car_type": "Hatchback"
  },
  {
    "year": 2012,
    "manufacturer_name": "MAZDA",
    "model_name": "MAZDA5",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2012,
    "manufacturer_name": "Mercedes-Benz",
    "model_name": "GLK-Class",
    "car_type": "SUV"
  },
  {
    "year": 2012,
    "manufacturer_name": "Mercedes-Benz",
    "model_name": "CLS-Class",
    "car_type": "Coupe"
  },
  {
    "year": 2012,
    "manufacturer_name": "Mercedes-Benz",
    "model_name": "M-Class",
    "car_type": "SUV"
  },
  {
    "year": 2012,
    "manufacturer_name": "Mercedes-Benz",
    "model_name": "SLS-Class",
    "car_type": "Convertible, Coupe"
  },
  {
    "year": 2012,
    "manufacturer_name": "Mercedes-Benz",
    "model_name": "E-Class",
    "car_type": "Sedan, Coupe, Convertible, Wagon"
  },
  {
    "year": 2012,
    "manufacturer_name": "Mercedes-Benz",
    "model_name": "Sprinter 3500 Cargo",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2012,
    "manufacturer_name": "Mercedes-Benz",
    "model_name": "R-Class",
    "car_type": "Wagon"
  },
  {
    "year": 2012,
    "manufacturer_name": "Mercedes-Benz",
    "model_name": "G-Class",
    "car_type": "SUV"
  },
  {
    "year": 2012,
    "manufacturer_name": "Mercedes-Benz",
    "model_name": "GL-Class",
    "car_type": "SUV"
  },
  {
    "year": 2012,
    "manufacturer_name": "MINI",
    "model_name": "Convertible",
    "car_type": "Convertible"
  },
  {
    "year": 2012,
    "manufacturer_name": "Mitsubishi",
    "model_name": "Lancer",
    "car_type": "Sedan, Hatchback"
  },
  {
    "year": 2012,
    "manufacturer_name": "Mercedes-Benz",
    "model_name": "S-Class",
    "car_type": "Sedan"
  },
  {
    "year": 2012,
    "manufacturer_name": "Mercedes-Benz",
    "model_name": "Sprinter 2500 Crew",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2012,
    "manufacturer_name": "Mitsubishi",
    "model_name": "i-MiEV",
    "car_type": "Hatchback"
  },
  {
    "year": 2012,
    "manufacturer_name": "MINI",
    "model_name": "Clubman",
    "car_type": "Hatchback"
  },
  {
    "year": 2012,
    "manufacturer_name": "MINI",
    "model_name": "Countryman",
    "car_type": "Hatchback"
  },
  {
    "year": 2012,
    "manufacturer_name": "Nissan",
    "model_name": "Armada",
    "car_type": "SUV"
  },
  {
    "year": 2012,
    "manufacturer_name": "MINI",
    "model_name": "Roadster",
    "car_type": "Convertible"
  },
  {
    "year": 2012,
    "manufacturer_name": "Nissan",
    "model_name": "JUKE",
    "car_type": "SUV"
  },
  {
    "year": 2012,
    "manufacturer_name": "Nissan",
    "model_name": "370Z",
    "car_type": "Convertible, Coupe"
  },
  {
    "year": 2012,
    "manufacturer_name": "Mitsubishi",
    "model_name": "Eclipse",
    "car_type": "Coupe, Convertible"
  },
  {
    "year": 2012,
    "manufacturer_name": "Mercedes-Benz",
    "model_name": "Sprinter 2500 Passenger",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2012,
    "manufacturer_name": "Mitsubishi",
    "model_name": "Galant",
    "car_type": "Sedan"
  },
  {
    "year": 2012,
    "manufacturer_name": "Mitsubishi",
    "model_name": "Outlander Sport",
    "car_type": "SUV"
  },
  {
    "year": 2012,
    "manufacturer_name": "MINI",
    "model_name": "Coupe",
    "car_type": "Coupe"
  },
  {
    "year": 2012,
    "manufacturer_name": "Nissan",
    "model_name": "Frontier Crew Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2012,
    "manufacturer_name": "Mitsubishi",
    "model_name": "Outlander",
    "car_type": "SUV"
  },
  {
    "year": 2012,
    "manufacturer_name": "Nissan",
    "model_name": "LEAF",
    "car_type": "Hatchback"
  },
  {
    "year": 2012,
    "manufacturer_name": "Nissan",
    "model_name": "Altima",
    "car_type": "Coupe, Sedan"
  },
  {
    "year": 2012,
    "manufacturer_name": "Nissan",
    "model_name": "cube",
    "car_type": "Wagon"
  },
  {
    "year": 2012,
    "manufacturer_name": "Nissan",
    "model_name": "Frontier King Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2012,
    "manufacturer_name": "Nissan",
    "model_name": "Maxima",
    "car_type": "Sedan"
  },
  {
    "year": 2012,
    "manufacturer_name": "Nissan",
    "model_name": "GT-R",
    "car_type": "Coupe"
  },
  {
    "year": 2012,
    "manufacturer_name": "Nissan",
    "model_name": "NV3500 HD Passenger",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2012,
    "manufacturer_name": "Nissan",
    "model_name": "NV1500 Cargo",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2012,
    "manufacturer_name": "Nissan",
    "model_name": "NV2500 HD Cargo",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2012,
    "manufacturer_name": "Nissan",
    "model_name": "Sentra",
    "car_type": "Sedan"
  },
  {
    "year": 2012,
    "manufacturer_name": "Nissan",
    "model_name": "NV3500 HD Cargo",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2012,
    "manufacturer_name": "Nissan",
    "model_name": "Titan Crew Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2012,
    "manufacturer_name": "Nissan",
    "model_name": "Rogue",
    "car_type": "SUV"
  },
  {
    "year": 2012,
    "manufacturer_name": "Nissan",
    "model_name": "Versa",
    "car_type": "Sedan, Hatchback"
  },
  {
    "year": 2012,
    "manufacturer_name": "Nissan",
    "model_name": "Pathfinder",
    "car_type": "SUV"
  },
  {
    "year": 2012,
    "manufacturer_name": "Porsche",
    "model_name": "Boxster",
    "car_type": "Convertible"
  },
  {
    "year": 2012,
    "manufacturer_name": "Nissan",
    "model_name": "Murano",
    "car_type": "SUV"
  },
  {
    "year": 2012,
    "manufacturer_name": "Ram",
    "model_name": "1500 Crew Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2012,
    "manufacturer_name": "Nissan",
    "model_name": "Xterra",
    "car_type": "SUV"
  },
  {
    "year": 2012,
    "manufacturer_name": "Porsche",
    "model_name": "911",
    "car_type": "Coupe, Convertible"
  },
  {
    "year": 2012,
    "manufacturer_name": "Nissan",
    "model_name": "Quest",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2012,
    "manufacturer_name": "Ram",
    "model_name": "2500 Crew Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2012,
    "manufacturer_name": "Ram",
    "model_name": "C/V",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2012,
    "manufacturer_name": "Porsche",
    "model_name": "Cayenne",
    "car_type": "SUV"
  },
  {
    "year": 2012,
    "manufacturer_name": "Porsche",
    "model_name": "Cayman",
    "car_type": "Coupe"
  },
  {
    "year": 2012,
    "manufacturer_name": "Ram",
    "model_name": "3500 Crew Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2012,
    "manufacturer_name": "Porsche",
    "model_name": "Panamera",
    "car_type": "Sedan"
  },
  {
    "year": 2012,
    "manufacturer_name": "Ram",
    "model_name": "2500 Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2012,
    "manufacturer_name": "Ram",
    "model_name": "1500 Quad Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2012,
    "manufacturer_name": "Ram",
    "model_name": "2500 Mega Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2012,
    "manufacturer_name": "Nissan",
    "model_name": "Titan King Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2012,
    "manufacturer_name": "Rolls-Royce",
    "model_name": "Ghost",
    "car_type": "Sedan"
  },
  {
    "year": 2012,
    "manufacturer_name": "Rolls-Royce",
    "model_name": "Phantom",
    "car_type": "Convertible, Coupe, Sedan"
  },
  {
    "year": 2012,
    "manufacturer_name": "Ram",
    "model_name": "3500 Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2012,
    "manufacturer_name": "Scion",
    "model_name": "xB",
    "car_type": "Hatchback"
  },
  {
    "year": 2012,
    "manufacturer_name": "Scion",
    "model_name": "xD",
    "car_type": "Hatchback"
  },
  {
    "year": 2012,
    "manufacturer_name": "Ram",
    "model_name": "1500 Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2012,
    "manufacturer_name": "Toyota",
    "model_name": "Sequoia",
    "car_type": "SUV"
  },
  {
    "year": 2012,
    "manufacturer_name": "Subaru",
    "model_name": "Impreza",
    "car_type": "Sedan, Wagon"
  },
  {
    "year": 2011,
    "manufacturer_name": "Acura",
    "model_name": "ZDX",
    "car_type": "SUV"
  },
  {
    "year": 2012,
    "manufacturer_name": "Toyota",
    "model_name": "RAV4",
    "car_type": "SUV"
  },
  {
    "year": 2012,
    "manufacturer_name": "Toyota",
    "model_name": "Highlander",
    "car_type": "SUV"
  },
  {
    "year": 2012,
    "manufacturer_name": "Subaru",
    "model_name": "Tribeca",
    "car_type": "SUV"
  },
  {
    "year": 2012,
    "manufacturer_name": "Suzuki",
    "model_name": "SX4",
    "car_type": "Sedan, Hatchback"
  },
  {
    "year": 2012,
    "manufacturer_name": "Toyota",
    "model_name": "Prius v",
    "car_type": "Wagon"
  },
  {
    "year": 2012,
    "manufacturer_name": "Scion",
    "model_name": "iQ",
    "car_type": "Hatchback"
  },
  {
    "year": 2012,
    "manufacturer_name": "Volvo",
    "model_name": "S80",
    "car_type": "Sedan"
  },
  {
    "year": 2012,
    "manufacturer_name": "Ram",
    "model_name": "3500 Mega Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2012,
    "manufacturer_name": "Subaru",
    "model_name": "Outback",
    "car_type": "Wagon"
  },
  {
    "year": 2012,
    "manufacturer_name": "Suzuki",
    "model_name": "Grand Vitara",
    "car_type": "SUV"
  },
  {
    "year": 2012,
    "manufacturer_name": "Toyota",
    "model_name": "Tundra CrewMax",
    "car_type": "Pickup"
  },
  {
    "year": 2012,
    "manufacturer_name": "Suzuki",
    "model_name": "Equator Extended Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2012,
    "manufacturer_name": "Subaru",
    "model_name": "Forester",
    "car_type": "SUV"
  },
  {
    "year": 2012,
    "manufacturer_name": "Toyota",
    "model_name": "Venza",
    "car_type": "Wagon"
  },
  {
    "year": 2012,
    "manufacturer_name": "smart",
    "model_name": "fortwo",
    "car_type": "Hatchback, Convertible"
  },
  {
    "year": 2012,
    "manufacturer_name": "Volkswagen",
    "model_name": "Tiguan",
    "car_type": "SUV"
  },
  {
    "year": 2012,
    "manufacturer_name": "Volkswagen",
    "model_name": "Passat",
    "car_type": "Sedan"
  },
  {
    "year": 2012,
    "manufacturer_name": "Toyota",
    "model_name": "Sienna",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2012,
    "manufacturer_name": "Subaru",
    "model_name": "Legacy",
    "car_type": "Sedan"
  },
  {
    "year": 2012,
    "manufacturer_name": "Toyota",
    "model_name": "Camry",
    "car_type": "Sedan"
  },
  {
    "year": 2012,
    "manufacturer_name": "Volvo",
    "model_name": "XC90",
    "car_type": "SUV"
  },
  {
    "year": 2012,
    "manufacturer_name": "Toyota",
    "model_name": "Prius",
    "car_type": "Hatchback"
  },
  {
    "year": 2012,
    "manufacturer_name": "Scion",
    "model_name": "tC",
    "car_type": "Coupe"
  },
  {
    "year": 2012,
    "manufacturer_name": "Toyota",
    "model_name": "Prius c",
    "car_type": "Hatchback"
  },
  {
    "year": 2012,
    "manufacturer_name": "Volkswagen",
    "model_name": "Jetta",
    "car_type": "Sedan"
  },
  {
    "year": 2012,
    "manufacturer_name": "Suzuki",
    "model_name": "Equator Crew Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2012,
    "manufacturer_name": "Toyota",
    "model_name": "Tacoma Double Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2012,
    "manufacturer_name": "Volkswagen",
    "model_name": "GTI",
    "car_type": "Hatchback"
  },
  {
    "year": 2011,
    "manufacturer_name": "Acura",
    "model_name": "MDX",
    "car_type": "SUV"
  },
  {
    "year": 2012,
    "manufacturer_name": "Toyota",
    "model_name": "Avalon",
    "car_type": "Sedan"
  },
  {
    "year": 2012,
    "manufacturer_name": "Volkswagen",
    "model_name": "Touareg",
    "car_type": "SUV"
  },
  {
    "year": 2011,
    "manufacturer_name": "Acura",
    "model_name": "RDX",
    "car_type": "SUV"
  },
  {
    "year": 2011,
    "manufacturer_name": "Audi",
    "model_name": "A5",
    "car_type": "Coupe, Convertible"
  },
  {
    "year": 2012,
    "manufacturer_name": "Suzuki",
    "model_name": "Kizashi",
    "car_type": "Sedan"
  },
  {
    "year": 2012,
    "manufacturer_name": "Volvo",
    "model_name": "S60",
    "car_type": "Sedan"
  },
  {
    "year": 2012,
    "manufacturer_name": "Toyota",
    "model_name": "Tacoma Access Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2011,
    "manufacturer_name": "Aston Martin",
    "model_name": "Vantage",
    "car_type": "Coupe, Convertible"
  },
  {
    "year": 2012,
    "manufacturer_name": "Volkswagen",
    "model_name": "Eos",
    "car_type": "Convertible"
  },
  {
    "year": 2012,
    "manufacturer_name": "Toyota",
    "model_name": "Yaris",
    "car_type": "Hatchback, Sedan"
  },
  {
    "year": 2011,
    "manufacturer_name": "Audi",
    "model_name": "A4",
    "car_type": "Sedan, Wagon"
  },
  {
    "year": 2012,
    "manufacturer_name": "Volvo",
    "model_name": "C70",
    "car_type": "Convertible"
  },
  {
    "year": 2012,
    "manufacturer_name": "Toyota",
    "model_name": "Corolla",
    "car_type": "Sedan"
  },
  {
    "year": 2012,
    "manufacturer_name": "Volkswagen",
    "model_name": "Beetle",
    "car_type": "Hatchback"
  },
  {
    "year": 2012,
    "manufacturer_name": "Toyota",
    "model_name": "Prius Plug-in Hybrid",
    "car_type": "Hatchback"
  },
  {
    "year": 2012,
    "manufacturer_name": "Volkswagen",
    "model_name": "Routan",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2012,
    "manufacturer_name": "Volkswagen",
    "model_name": "Jetta SportWagen",
    "car_type": "Wagon"
  },
  {
    "year": 2012,
    "manufacturer_name": "Toyota",
    "model_name": "4Runner",
    "car_type": "SUV"
  },
  {
    "year": 2011,
    "manufacturer_name": "Audi",
    "model_name": "A6",
    "car_type": "Sedan, Wagon"
  },
  {
    "year": 2012,
    "manufacturer_name": "Toyota",
    "model_name": "FJ Cruiser",
    "car_type": "SUV"
  },
  {
    "year": 2012,
    "manufacturer_name": "Toyota",
    "model_name": "Matrix",
    "car_type": "Wagon"
  },
  {
    "year": 2011,
    "manufacturer_name": "Audi",
    "model_name": "A3",
    "car_type": "Wagon"
  },
  {
    "year": 2012,
    "manufacturer_name": "Volvo",
    "model_name": "C30",
    "car_type": "Hatchback"
  },
  {
    "year": 2012,
    "manufacturer_name": "Volkswagen",
    "model_name": "Golf",
    "car_type": "Hatchback"
  },
  {
    "year": 2012,
    "manufacturer_name": "Volvo",
    "model_name": "XC60",
    "car_type": "SUV"
  },
  {
    "year": 2012,
    "manufacturer_name": "Tesla",
    "model_name": "Model S",
    "car_type": "Sedan"
  },
  {
    "year": 2012,
    "manufacturer_name": "Volkswagen",
    "model_name": "CC",
    "car_type": "Sedan"
  },
  {
    "year": 2011,
    "manufacturer_name": "Acura",
    "model_name": "TL",
    "car_type": "Sedan"
  },
  {
    "year": 2012,
    "manufacturer_name": "Volvo",
    "model_name": "XC70",
    "car_type": "Wagon"
  },
  {
    "year": 2012,
    "manufacturer_name": "Toyota",
    "model_name": "Tacoma Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2011,
    "manufacturer_name": "Aston Martin",
    "model_name": "Rapide",
    "car_type": "Sedan"
  },
  {
    "year": 2012,
    "manufacturer_name": "Toyota",
    "model_name": "Tundra Double Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2011,
    "manufacturer_name": "Acura",
    "model_name": "RL",
    "car_type": "Sedan"
  },
  {
    "year": 2012,
    "manufacturer_name": "Toyota",
    "model_name": "Tundra Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2011,
    "manufacturer_name": "Aston Martin",
    "model_name": "DB9",
    "car_type": "Convertible, Coupe"
  },
  {
    "year": 2011,
    "manufacturer_name": "Acura",
    "model_name": "TSX",
    "car_type": "Sedan, Wagon"
  },
  {
    "year": 2011,
    "manufacturer_name": "Aston Martin",
    "model_name": "DBS",
    "car_type": "Coupe, Convertible"
  },
  {
    "year": 2011,
    "manufacturer_name": "Audi",
    "model_name": "Q5",
    "car_type": "SUV"
  },
  {
    "year": 2011,
    "manufacturer_name": "Audi",
    "model_name": "R8",
    "car_type": "Coupe, Convertible"
  },
  {
    "year": 2011,
    "manufacturer_name": "Audi",
    "model_name": "A8",
    "car_type": "Sedan"
  },
  {
    "year": 2011,
    "manufacturer_name": "Audi",
    "model_name": "Q7",
    "car_type": "SUV"
  },
  {
    "year": 2011,
    "manufacturer_name": "Bentley",
    "model_name": "Continental",
    "car_type": "Convertible, Sedan, Coupe"
  },
  {
    "year": 2011,
    "manufacturer_name": "BMW",
    "model_name": "X5 M",
    "car_type": "SUV"
  },
  {
    "year": 2011,
    "manufacturer_name": "BMW",
    "model_name": "M3",
    "car_type": "Convertible, Coupe, Sedan"
  },
  {
    "year": 2011,
    "manufacturer_name": "BMW",
    "model_name": "3 Series",
    "car_type": "Sedan, Coupe, Convertible, Wagon"
  },
  {
    "year": 2011,
    "manufacturer_name": "BMW",
    "model_name": "X6",
    "car_type": "SUV"
  },
  {
    "year": 2011,
    "manufacturer_name": "Audi",
    "model_name": "S6",
    "car_type": "Sedan"
  },
  {
    "year": 2011,
    "manufacturer_name": "BMW",
    "model_name": "X5",
    "car_type": "SUV"
  },
  {
    "year": 2011,
    "manufacturer_name": "Audi",
    "model_name": "TT",
    "car_type": "Coupe, Convertible"
  },
  {
    "year": 2011,
    "manufacturer_name": "BMW",
    "model_name": "5 Series",
    "car_type": "Sedan"
  },
  {
    "year": 2011,
    "manufacturer_name": "Audi",
    "model_name": "S4",
    "car_type": "Sedan"
  },
  {
    "year": 2011,
    "manufacturer_name": "Audi",
    "model_name": "S5",
    "car_type": "Coupe, Convertible"
  },
  {
    "year": 2011,
    "manufacturer_name": "BMW",
    "model_name": "7 Series",
    "car_type": "Sedan"
  },
  {
    "year": 2011,
    "manufacturer_name": "Bentley",
    "model_name": "Mulsanne",
    "car_type": "Sedan"
  },
  {
    "year": 2011,
    "manufacturer_name": "BMW",
    "model_name": "1 Series",
    "car_type": "Coupe, Convertible"
  },
  {
    "year": 2011,
    "manufacturer_name": "BMW",
    "model_name": "X6 M",
    "car_type": "SUV"
  },
  {
    "year": 2011,
    "manufacturer_name": "Cadillac",
    "model_name": "DTS",
    "car_type": "Sedan"
  },
  {
    "year": 2011,
    "manufacturer_name": "Cadillac",
    "model_name": "Escalade",
    "car_type": "SUV"
  },
  {
    "year": 2011,
    "manufacturer_name": "Buick",
    "model_name": "Enclave",
    "car_type": "SUV"
  },
  {
    "year": 2011,
    "manufacturer_name": "Buick",
    "model_name": "Lucerne",
    "car_type": "Sedan"
  },
  {
    "year": 2011,
    "manufacturer_name": "BMW",
    "model_name": "Z4",
    "car_type": "Convertible"
  },
  {
    "year": 2011,
    "manufacturer_name": "Buick",
    "model_name": "Regal",
    "car_type": "Sedan"
  },
  {
    "year": 2011,
    "manufacturer_name": "BMW",
    "model_name": "X3",
    "car_type": "SUV"
  },
  {
    "year": 2011,
    "manufacturer_name": "Buick",
    "model_name": "LaCrosse",
    "car_type": "Sedan"
  },
  {
    "year": 2011,
    "manufacturer_name": "Cadillac",
    "model_name": "Escalade EXT",
    "car_type": "Pickup"
  },
  {
    "year": 2011,
    "manufacturer_name": "Cadillac",
    "model_name": "CTS",
    "car_type": "Sedan, Wagon, Coupe"
  },
  {
    "year": 2011,
    "manufacturer_name": "Cadillac",
    "model_name": "Escalade ESV",
    "car_type": "SUV"
  },
  {
    "year": 2011,
    "manufacturer_name": "Chevrolet",
    "model_name": "Aveo",
    "car_type": "Hatchback, Sedan"
  },
  {
    "year": 2011,
    "manufacturer_name": "Chevrolet",
    "model_name": "Cruze",
    "car_type": "Sedan"
  },
  {
    "year": 2011,
    "manufacturer_name": "Chevrolet",
    "model_name": "HHR",
    "car_type": "Wagon"
  },
  {
    "year": 2011,
    "manufacturer_name": "Chevrolet",
    "model_name": "Silverado 1500 Extended Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2011,
    "manufacturer_name": "Chevrolet",
    "model_name": "Colorado Crew Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2011,
    "manufacturer_name": "Cadillac",
    "model_name": "STS",
    "car_type": "Sedan"
  },
  {
    "year": 2011,
    "manufacturer_name": "Chevrolet",
    "model_name": "Avalanche",
    "car_type": "SUV"
  },
  {
    "year": 2011,
    "manufacturer_name": "Chevrolet",
    "model_name": "Express 3500 Passenger",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2011,
    "manufacturer_name": "Chevrolet",
    "model_name": "Camaro",
    "car_type": "Coupe, Convertible"
  },
  {
    "year": 2011,
    "manufacturer_name": "Chevrolet",
    "model_name": "Colorado Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2011,
    "manufacturer_name": "Chevrolet",
    "model_name": "Express 3500 Cargo",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2011,
    "manufacturer_name": "Chevrolet",
    "model_name": "Express 2500 Cargo",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2011,
    "manufacturer_name": "Chevrolet",
    "model_name": "Colorado Extended Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2011,
    "manufacturer_name": "Chevrolet",
    "model_name": "Silverado 3500 HD Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2011,
    "manufacturer_name": "Dodge",
    "model_name": "Durango",
    "car_type": "SUV"
  },
  {
    "year": 2011,
    "manufacturer_name": "Cadillac",
    "model_name": "SRX",
    "car_type": "SUV"
  },
  {
    "year": 2011,
    "manufacturer_name": "Chrysler",
    "model_name": "200",
    "car_type": "Convertible, Sedan"
  },
  {
    "year": 2011,
    "manufacturer_name": "Chevrolet",
    "model_name": "Express 2500 Passenger",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2011,
    "manufacturer_name": "Chevrolet",
    "model_name": "Silverado 2500 HD Crew Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2011,
    "manufacturer_name": "Chevrolet",
    "model_name": "Silverado 2500 HD Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2011,
    "manufacturer_name": "Chevrolet",
    "model_name": "Silverado 3500 HD Extended Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2011,
    "manufacturer_name": "Chevrolet",
    "model_name": "Suburban 1500",
    "car_type": "SUV"
  },
  {
    "year": 2011,
    "manufacturer_name": "Chrysler",
    "model_name": "300",
    "car_type": "Sedan"
  },
  {
    "year": 2011,
    "manufacturer_name": "Chevrolet",
    "model_name": "Equinox",
    "car_type": "SUV"
  },
  {
    "year": 2011,
    "manufacturer_name": "Chevrolet",
    "model_name": "Silverado 3500 HD Crew Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2011,
    "manufacturer_name": "Ferrari",
    "model_name": "599 GTB Fiorano",
    "car_type": "Coupe"
  },
  {
    "year": 2011,
    "manufacturer_name": "Chevrolet",
    "model_name": "Suburban 2500",
    "car_type": "SUV"
  },
  {
    "year": 2011,
    "manufacturer_name": "Chrysler",
    "model_name": "Town & Country",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2011,
    "manufacturer_name": "Chevrolet",
    "model_name": "Volt",
    "car_type": "Sedan"
  },
  {
    "year": 2011,
    "manufacturer_name": "Chevrolet",
    "model_name": "Silverado 2500 HD Extended Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2011,
    "manufacturer_name": "Chevrolet",
    "model_name": "Express 1500 Cargo",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2011,
    "manufacturer_name": "Chevrolet",
    "model_name": "Corvette",
    "car_type": "Convertible, Coupe"
  },
  {
    "year": 2011,
    "manufacturer_name": "Chevrolet",
    "model_name": "Silverado 1500 Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2011,
    "manufacturer_name": "Dodge",
    "model_name": "Grand Caravan Cargo",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2011,
    "manufacturer_name": "Chevrolet",
    "model_name": "Traverse",
    "car_type": "SUV"
  },
  {
    "year": 2011,
    "manufacturer_name": "Dodge",
    "model_name": "Charger",
    "car_type": "Sedan"
  },
  {
    "year": 2011,
    "manufacturer_name": "Chevrolet",
    "model_name": "Express 1500 Passenger",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2011,
    "manufacturer_name": "Chevrolet",
    "model_name": "Malibu",
    "car_type": "Sedan"
  },
  {
    "year": 2011,
    "manufacturer_name": "Chevrolet",
    "model_name": "Tahoe",
    "car_type": "SUV"
  },
  {
    "year": 2011,
    "manufacturer_name": "Ferrari",
    "model_name": "599 GTO",
    "car_type": "Coupe"
  },
  {
    "year": 2011,
    "manufacturer_name": "Dodge",
    "model_name": "Challenger",
    "car_type": "Coupe"
  },
  {
    "year": 2011,
    "manufacturer_name": "Dodge",
    "model_name": "Journey",
    "car_type": "SUV"
  },
  {
    "year": 2011,
    "manufacturer_name": "Dodge",
    "model_name": "Avenger",
    "car_type": "Sedan"
  },
  {
    "year": 2011,
    "manufacturer_name": "Chevrolet",
    "model_name": "Impala",
    "car_type": "Sedan"
  },
  {
    "year": 2011,
    "manufacturer_name": "Ferrari",
    "model_name": "612 Scaglietti",
    "car_type": "Coupe"
  },
  {
    "year": 2011,
    "manufacturer_name": "Chevrolet",
    "model_name": "Silverado 1500 Crew Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2011,
    "manufacturer_name": "Ford",
    "model_name": "E150 Passenger",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2011,
    "manufacturer_name": "Dodge",
    "model_name": "Caliber",
    "car_type": "Wagon"
  },
  {
    "year": 2011,
    "manufacturer_name": "Ford",
    "model_name": "E250 Cargo",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2011,
    "manufacturer_name": "Ford",
    "model_name": "E350 Super Duty Passenger",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2011,
    "manufacturer_name": "Ferrari",
    "model_name": "458 Italia",
    "car_type": "Coupe"
  },
  {
    "year": 2011,
    "manufacturer_name": "Dodge",
    "model_name": "Nitro",
    "car_type": "SUV"
  },
  {
    "year": 2011,
    "manufacturer_name": "Dodge",
    "model_name": "Grand Caravan Passenger",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2011,
    "manufacturer_name": "Ford",
    "model_name": "E150 Cargo",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2011,
    "manufacturer_name": "Ford",
    "model_name": "Crown Victoria",
    "car_type": "Sedan"
  },
  {
    "year": 2011,
    "manufacturer_name": "Ford",
    "model_name": "Edge",
    "car_type": "SUV"
  },
  {
    "year": 2011,
    "manufacturer_name": "Ford",
    "model_name": "Explorer",
    "car_type": "SUV"
  },
  {
    "year": 2011,
    "manufacturer_name": "Ferrari",
    "model_name": "California",
    "car_type": "Convertible"
  },
  {
    "year": 2011,
    "manufacturer_name": "Ford",
    "model_name": "Escape",
    "car_type": "SUV"
  },
  {
    "year": 2011,
    "manufacturer_name": "Ford",
    "model_name": "Expedition",
    "car_type": "SUV"
  },
  {
    "year": 2011,
    "manufacturer_name": "Ford",
    "model_name": "F150 Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2011,
    "manufacturer_name": "Ford",
    "model_name": "F350 Super Duty Crew Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2011,
    "manufacturer_name": "Ford",
    "model_name": "F250 Super Duty Crew Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2011,
    "manufacturer_name": "Ford",
    "model_name": "F350 Super Duty Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2011,
    "manufacturer_name": "Ford",
    "model_name": "F250 Super Duty Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2011,
    "manufacturer_name": "Ford",
    "model_name": "F150 Super Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2011,
    "manufacturer_name": "Ford",
    "model_name": "F150 SuperCrew Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2011,
    "manufacturer_name": "Ford",
    "model_name": "E350 Super Duty Cargo",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2011,
    "manufacturer_name": "Ford",
    "model_name": "F250 Super Duty Super Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2011,
    "manufacturer_name": "Ford",
    "model_name": "Expedition EL",
    "car_type": "SUV"
  },
  {
    "year": 2011,
    "manufacturer_name": "Ford",
    "model_name": "Fusion",
    "car_type": "Sedan"
  },
  {
    "year": 2011,
    "manufacturer_name": "Ford",
    "model_name": "F450 Super Duty Crew Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2011,
    "manufacturer_name": "Ford",
    "model_name": "Fiesta",
    "car_type": "Sedan, Hatchback"
  },
  {
    "year": 2011,
    "manufacturer_name": "GMC",
    "model_name": "Savana 1500 Cargo",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2011,
    "manufacturer_name": "GMC",
    "model_name": "Sierra 1500 Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2011,
    "manufacturer_name": "Ford",
    "model_name": "Transit Connect Cargo",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2011,
    "manufacturer_name": "GMC",
    "model_name": "Canyon Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2011,
    "manufacturer_name": "GMC",
    "model_name": "Canyon Extended Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2011,
    "manufacturer_name": "Ford",
    "model_name": "F350 Super Duty Super Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2011,
    "manufacturer_name": "Ford",
    "model_name": "Focus",
    "car_type": "Sedan"
  },
  {
    "year": 2011,
    "manufacturer_name": "Ford",
    "model_name": "Flex",
    "car_type": "SUV"
  },
  {
    "year": 2011,
    "manufacturer_name": "Ford",
    "model_name": "Taurus",
    "car_type": "Sedan"
  },
  {
    "year": 2011,
    "manufacturer_name": "GMC",
    "model_name": "Savana 3500 Passenger",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2011,
    "manufacturer_name": "GMC",
    "model_name": "Savana 2500 Cargo",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2011,
    "manufacturer_name": "GMC",
    "model_name": "Acadia",
    "car_type": "SUV"
  },
  {
    "year": 2011,
    "manufacturer_name": "GMC",
    "model_name": "Savana 2500 Passenger",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2011,
    "manufacturer_name": "Ford",
    "model_name": "Ranger Super Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2011,
    "manufacturer_name": "Ford",
    "model_name": "Transit Connect Passenger",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2011,
    "manufacturer_name": "GMC",
    "model_name": "Canyon Crew Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2011,
    "manufacturer_name": "Ford",
    "model_name": "Mustang",
    "car_type": "Convertible, Coupe"
  },
  {
    "year": 2011,
    "manufacturer_name": "GMC",
    "model_name": "Savana 1500 Passenger",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2011,
    "manufacturer_name": "GMC",
    "model_name": "Savana 3500 Cargo",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2011,
    "manufacturer_name": "Ford",
    "model_name": "Ranger Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2011,
    "manufacturer_name": "GMC",
    "model_name": "Sierra 2500 HD Crew Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2011,
    "manufacturer_name": "GMC",
    "model_name": "Sierra 1500 Crew Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2011,
    "manufacturer_name": "GMC",
    "model_name": "Sierra 3500 HD Extended Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2011,
    "manufacturer_name": "GMC",
    "model_name": "Yukon XL 2500",
    "car_type": "SUV"
  },
  {
    "year": 2011,
    "manufacturer_name": "GMC",
    "model_name": "Sierra 1500 Extended Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2011,
    "manufacturer_name": "GMC",
    "model_name": "Sierra 3500 HD Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2011,
    "manufacturer_name": "GMC",
    "model_name": "Sierra 3500 HD Crew Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2011,
    "manufacturer_name": "GMC",
    "model_name": "Sierra 2500 HD Extended Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2011,
    "manufacturer_name": "GMC",
    "model_name": "Sierra 2500 HD Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2011,
    "manufacturer_name": "GMC",
    "model_name": "Yukon XL 1500",
    "car_type": "SUV"
  },
  {
    "year": 2011,
    "manufacturer_name": "Honda",
    "model_name": "Pilot",
    "car_type": "SUV"
  },
  {
    "year": 2011,
    "manufacturer_name": "Honda",
    "model_name": "CR-Z",
    "car_type": "Coupe"
  },
  {
    "year": 2011,
    "manufacturer_name": "GMC",
    "model_name": "Yukon",
    "car_type": "SUV"
  },
  {
    "year": 2011,
    "manufacturer_name": "Honda",
    "model_name": "Accord Crosstour",
    "car_type": "SUV"
  },
  {
    "year": 2011,
    "manufacturer_name": "Honda",
    "model_name": "Accord",
    "car_type": "Sedan, Coupe"
  },
  {
    "year": 2011,
    "manufacturer_name": "Honda",
    "model_name": "Civic",
    "car_type": "Sedan, Coupe"
  },
  {
    "year": 2011,
    "manufacturer_name": "GMC",
    "model_name": "Terrain",
    "car_type": "SUV"
  },
  {
    "year": 2011,
    "manufacturer_name": "Hyundai",
    "model_name": "Tucson",
    "car_type": "SUV"
  },
  {
    "year": 2011,
    "manufacturer_name": "Honda",
    "model_name": "CR-V",
    "car_type": "SUV"
  },
  {
    "year": 2011,
    "manufacturer_name": "Hyundai",
    "model_name": "Equus",
    "car_type": "Sedan"
  },
  {
    "year": 2011,
    "manufacturer_name": "Honda",
    "model_name": "Fit",
    "car_type": "Hatchback"
  },
  {
    "year": 2011,
    "manufacturer_name": "Honda",
    "model_name": "Element",
    "car_type": "SUV"
  },
  {
    "year": 2011,
    "manufacturer_name": "Honda",
    "model_name": "Odyssey",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2011,
    "manufacturer_name": "Hyundai",
    "model_name": "Accent",
    "car_type": "Sedan, Hatchback"
  },
  {
    "year": 2011,
    "manufacturer_name": "INFINITI",
    "model_name": "M",
    "car_type": "Sedan"
  },
  {
    "year": 2011,
    "manufacturer_name": "Hyundai",
    "model_name": "Genesis Coupe",
    "car_type": "Coupe"
  },
  {
    "year": 2011,
    "manufacturer_name": "Kia",
    "model_name": "Rio",
    "car_type": "Sedan, Hatchback"
  },
  {
    "year": 2011,
    "manufacturer_name": "Hyundai",
    "model_name": "Elantra",
    "car_type": "Wagon, Sedan"
  },
  {
    "year": 2011,
    "manufacturer_name": "Jaguar",
    "model_name": "XF",
    "car_type": "Sedan"
  },
  {
    "year": 2011,
    "manufacturer_name": "Kia",
    "model_name": "Soul",
    "car_type": "Wagon"
  },
  {
    "year": 2011,
    "manufacturer_name": "INFINITI",
    "model_name": "G",
    "car_type": "Sedan, Coupe, Convertible"
  },
  {
    "year": 2011,
    "manufacturer_name": "Jaguar",
    "model_name": "XK",
    "car_type": "Convertible, Coupe"
  },
  {
    "year": 2011,
    "manufacturer_name": "Jeep",
    "model_name": "Liberty",
    "car_type": "SUV"
  },
  {
    "year": 2011,
    "manufacturer_name": "Hyundai",
    "model_name": "Sonata",
    "car_type": "Sedan"
  },
  {
    "year": 2011,
    "manufacturer_name": "INFINITI",
    "model_name": "EX",
    "car_type": "SUV"
  },
  {
    "year": 2011,
    "manufacturer_name": "Jeep",
    "model_name": "Compass",
    "car_type": "SUV"
  },
  {
    "year": 2011,
    "manufacturer_name": "Kia",
    "model_name": "Forte",
    "car_type": "Sedan, Coupe, Hatchback"
  },
  {
    "year": 2011,
    "manufacturer_name": "Honda",
    "model_name": "Insight",
    "car_type": "Hatchback"
  },
  {
    "year": 2011,
    "manufacturer_name": "Land Rover",
    "model_name": "LR4",
    "car_type": "SUV"
  },
  {
    "year": 2011,
    "manufacturer_name": "Land Rover",
    "model_name": "Range Rover",
    "car_type": "SUV"
  },
  {
    "year": 2011,
    "manufacturer_name": "Hyundai",
    "model_name": "Genesis",
    "car_type": "Sedan"
  },
  {
    "year": 2011,
    "manufacturer_name": "Lamborghini",
    "model_name": "Gallardo",
    "car_type": "Coupe, Convertible"
  },
  {
    "year": 2011,
    "manufacturer_name": "Hyundai",
    "model_name": "Azera",
    "car_type": "Sedan"
  },
  {
    "year": 2011,
    "manufacturer_name": "Honda",
    "model_name": "Ridgeline",
    "car_type": "Pickup"
  },
  {
    "year": 2011,
    "manufacturer_name": "Jeep",
    "model_name": "Wrangler",
    "car_type": "SUV"
  },
  {
    "year": 2011,
    "manufacturer_name": "Lexus",
    "model_name": "CT",
    "car_type": "Hatchback"
  },
  {
    "year": 2011,
    "manufacturer_name": "Hyundai",
    "model_name": "Santa Fe",
    "car_type": "SUV"
  },
  {
    "year": 2011,
    "manufacturer_name": "Kia",
    "model_name": "Sorento",
    "car_type": "SUV"
  },
  {
    "year": 2011,
    "manufacturer_name": "Lexus",
    "model_name": "LX",
    "car_type": "SUV"
  },
  {
    "year": 2011,
    "manufacturer_name": "Lexus",
    "model_name": "GX",
    "car_type": "SUV"
  },
  {
    "year": 2011,
    "manufacturer_name": "Kia",
    "model_name": "Optima",
    "car_type": "Sedan"
  },
  {
    "year": 2011,
    "manufacturer_name": "Land Rover",
    "model_name": "Range Rover Sport",
    "car_type": "SUV"
  },
  {
    "year": 2011,
    "manufacturer_name": "Lexus",
    "model_name": "GS",
    "car_type": "Sedan"
  },
  {
    "year": 2011,
    "manufacturer_name": "Lincoln",
    "model_name": "MKS",
    "car_type": "Sedan"
  },
  {
    "year": 2011,
    "manufacturer_name": "INFINITI",
    "model_name": "FX",
    "car_type": "SUV"
  },
  {
    "year": 2011,
    "manufacturer_name": "Lexus",
    "model_name": "IS",
    "car_type": "Sedan, Convertible"
  },
  {
    "year": 2011,
    "manufacturer_name": "Kia",
    "model_name": "Sportage",
    "car_type": "SUV"
  },
  {
    "year": 2011,
    "manufacturer_name": "Kia",
    "model_name": "Sedona",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2011,
    "manufacturer_name": "Jeep",
    "model_name": "Grand Cherokee",
    "car_type": "SUV"
  },
  {
    "year": 2011,
    "manufacturer_name": "Hyundai",
    "model_name": "Veracruz",
    "car_type": "SUV"
  },
  {
    "year": 2011,
    "manufacturer_name": "INFINITI",
    "model_name": "QX",
    "car_type": "SUV"
  },
  {
    "year": 2011,
    "manufacturer_name": "Lexus",
    "model_name": "HS",
    "car_type": "Sedan"
  },
  {
    "year": 2011,
    "manufacturer_name": "Lincoln",
    "model_name": "MKZ",
    "car_type": "Sedan"
  },
  {
    "year": 2011,
    "manufacturer_name": "Lexus",
    "model_name": "LS",
    "car_type": "Sedan"
  },
  {
    "year": 2011,
    "manufacturer_name": "Jaguar",
    "model_name": "XJ",
    "car_type": "Sedan"
  },
  {
    "year": 2011,
    "manufacturer_name": "Jeep",
    "model_name": "Patriot",
    "car_type": "SUV"
  },
  {
    "year": 2011,
    "manufacturer_name": "Lincoln",
    "model_name": "Navigator L",
    "car_type": "SUV"
  },
  {
    "year": 2011,
    "manufacturer_name": "Lexus",
    "model_name": "ES",
    "car_type": "Sedan"
  },
  {
    "year": 2011,
    "manufacturer_name": "Lotus",
    "model_name": "Evora",
    "car_type": "Coupe"
  },
  {
    "year": 2011,
    "manufacturer_name": "Lotus",
    "model_name": "Elise",
    "car_type": "Coupe"
  },
  {
    "year": 2011,
    "manufacturer_name": "Lexus",
    "model_name": "IS F",
    "car_type": "Sedan"
  },
  {
    "year": 2011,
    "manufacturer_name": "Lincoln",
    "model_name": "MKX",
    "car_type": "SUV"
  },
  {
    "year": 2011,
    "manufacturer_name": "Land Rover",
    "model_name": "LR2",
    "car_type": "SUV"
  },
  {
    "year": 2011,
    "manufacturer_name": "Lincoln",
    "model_name": "Town Car",
    "car_type": "Sedan"
  },
  {
    "year": 2011,
    "manufacturer_name": "Lincoln",
    "model_name": "MKT",
    "car_type": "SUV"
  },
  {
    "year": 2011,
    "manufacturer_name": "Lexus",
    "model_name": "RX",
    "car_type": "SUV"
  },
  {
    "year": 2011,
    "manufacturer_name": "Lincoln",
    "model_name": "Navigator",
    "car_type": "SUV"
  },
  {
    "year": 2011,
    "manufacturer_name": "Lotus",
    "model_name": "Exige",
    "car_type": "Coupe"
  },
  {
    "year": 2011,
    "manufacturer_name": "Maserati",
    "model_name": "GranTurismo",
    "car_type": "Coupe, Convertible"
  },
  {
    "year": 2011,
    "manufacturer_name": "Maybach",
    "model_name": "62",
    "car_type": "Sedan"
  },
  {
    "year": 2011,
    "manufacturer_name": "Maserati",
    "model_name": "Quattroporte",
    "car_type": "Sedan"
  },
  {
    "year": 2011,
    "manufacturer_name": "MAZDA",
    "model_name": "CX-9",
    "car_type": "SUV"
  },
  {
    "year": 2011,
    "manufacturer_name": "Maybach",
    "model_name": "57",
    "car_type": "Sedan"
  },
  {
    "year": 2011,
    "manufacturer_name": "MAZDA",
    "model_name": "MAZDA6",
    "car_type": "Sedan"
  },
  {
    "year": 2011,
    "manufacturer_name": "MAZDA",
    "model_name": "MAZDA2",
    "car_type": "Hatchback"
  },
  {
    "year": 2011,
    "manufacturer_name": "MAZDA",
    "model_name": "CX-7",
    "car_type": "SUV"
  },
  {
    "year": 2011,
    "manufacturer_name": "MAZDA",
    "model_name": "MAZDA3",
    "car_type": "Sedan, Hatchback"
  },
  {
    "year": 2011,
    "manufacturer_name": "MAZDA",
    "model_name": "RX-8",
    "car_type": "Coupe"
  },
  {
    "year": 2011,
    "manufacturer_name": "Mercedes-Benz",
    "model_name": "CL-Class",
    "car_type": "Coupe"
  },
  {
    "year": 2011,
    "manufacturer_name": "Mercedes-Benz",
    "model_name": "SLK-Class",
    "car_type": "Convertible"
  },
  {
    "year": 2011,
    "manufacturer_name": "Mercedes-Benz",
    "model_name": "GL-Class",
    "car_type": "SUV"
  },
  {
    "year": 2011,
    "manufacturer_name": "Nissan",
    "model_name": "370Z",
    "car_type": "Coupe, Convertible"
  },
  {
    "year": 2011,
    "manufacturer_name": "Mercedes-Benz",
    "model_name": "C-Class",
    "car_type": "Sedan"
  },
  {
    "year": 2011,
    "manufacturer_name": "Mercedes-Benz",
    "model_name": "G-Class",
    "car_type": "SUV"
  },
  {
    "year": 2011,
    "manufacturer_name": "Mercedes-Benz",
    "model_name": "Sprinter 3500 Cargo",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2011,
    "manufacturer_name": "Mercedes-Benz",
    "model_name": "E-Class",
    "car_type": "Coupe, Convertible, Sedan, Wagon"
  },
  {
    "year": 2011,
    "manufacturer_name": "Mitsubishi",
    "model_name": "Lancer",
    "car_type": "Sedan, Hatchback"
  },
  {
    "year": 2011,
    "manufacturer_name": "Mitsubishi",
    "model_name": "Outlander Sport",
    "car_type": "SUV"
  },
  {
    "year": 2011,
    "manufacturer_name": "MAZDA",
    "model_name": "MX-5 Miata",
    "car_type": "Convertible"
  },
  {
    "year": 2011,
    "manufacturer_name": "MAZDA",
    "model_name": "Tribute",
    "car_type": "SUV"
  },
  {
    "year": 2011,
    "manufacturer_name": "Mercedes-Benz",
    "model_name": "Sprinter 2500 Passenger",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2011,
    "manufacturer_name": "Mercedes-Benz",
    "model_name": "SL-Class",
    "car_type": "Convertible"
  },
  {
    "year": 2011,
    "manufacturer_name": "Mercedes-Benz",
    "model_name": "R-Class",
    "car_type": "Wagon"
  },
  {
    "year": 2011,
    "manufacturer_name": "Mercury",
    "model_name": "Milan",
    "car_type": "Sedan"
  },
  {
    "year": 2011,
    "manufacturer_name": "Mercedes-Benz",
    "model_name": "CLS-Class",
    "car_type": "Coupe"
  },
  {
    "year": 2011,
    "manufacturer_name": "Mitsubishi",
    "model_name": "Galant",
    "car_type": "Sedan"
  },
  {
    "year": 2011,
    "manufacturer_name": "Mercury",
    "model_name": "Mariner",
    "car_type": "SUV"
  },
  {
    "year": 2011,
    "manufacturer_name": "Mercedes-Benz",
    "model_name": "S-Class",
    "car_type": "Sedan"
  },
  {
    "year": 2011,
    "manufacturer_name": "Mercedes-Benz",
    "model_name": "GLK-Class",
    "car_type": "SUV"
  },
  {
    "year": 2011,
    "manufacturer_name": "Nissan",
    "model_name": "Frontier King Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2011,
    "manufacturer_name": "Mercedes-Benz",
    "model_name": "Sprinter 2500 Cargo",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2011,
    "manufacturer_name": "Nissan",
    "model_name": "Frontier Crew Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2011,
    "manufacturer_name": "Mitsubishi",
    "model_name": "Outlander",
    "car_type": "SUV"
  },
  {
    "year": 2011,
    "manufacturer_name": "Mercury",
    "model_name": "Grand Marquis",
    "car_type": "Sedan"
  },
  {
    "year": 2011,
    "manufacturer_name": "Mercedes-Benz",
    "model_name": "M-Class",
    "car_type": "SUV"
  },
  {
    "year": 2011,
    "manufacturer_name": "MINI",
    "model_name": "Clubman",
    "car_type": "Hatchback"
  },
  {
    "year": 2011,
    "manufacturer_name": "MINI",
    "model_name": "Convertible",
    "car_type": "Convertible"
  },
  {
    "year": 2011,
    "manufacturer_name": "Mitsubishi",
    "model_name": "Endeavor",
    "car_type": "SUV"
  },
  {
    "year": 2011,
    "manufacturer_name": "Nissan",
    "model_name": "GT-R",
    "car_type": "Coupe"
  },
  {
    "year": 2011,
    "manufacturer_name": "Mercedes-Benz",
    "model_name": "Sprinter 2500 Crew",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2011,
    "manufacturer_name": "Nissan",
    "model_name": "LEAF",
    "car_type": "Hatchback"
  },
  {
    "year": 2011,
    "manufacturer_name": "Nissan",
    "model_name": "Altima",
    "car_type": "Coupe, Sedan"
  },
  {
    "year": 2011,
    "manufacturer_name": "Nissan",
    "model_name": "Pathfinder",
    "car_type": "SUV"
  },
  {
    "year": 2011,
    "manufacturer_name": "MINI",
    "model_name": "Hardtop",
    "car_type": "Hatchback"
  },
  {
    "year": 2011,
    "manufacturer_name": "Mitsubishi",
    "model_name": "Eclipse",
    "car_type": "Coupe, Convertible"
  },
  {
    "year": 2011,
    "manufacturer_name": "Mercedes-Benz",
    "model_name": "SLS-Class",
    "car_type": "Coupe"
  },
  {
    "year": 2011,
    "manufacturer_name": "Nissan",
    "model_name": "cube",
    "car_type": "Wagon"
  },
  {
    "year": 2011,
    "manufacturer_name": "MINI",
    "model_name": "Countryman",
    "car_type": "Hatchback"
  },
  {
    "year": 2011,
    "manufacturer_name": "Nissan",
    "model_name": "Murano",
    "car_type": "SUV"
  },
  {
    "year": 2011,
    "manufacturer_name": "Nissan",
    "model_name": "Rogue",
    "car_type": "SUV"
  },
  {
    "year": 2011,
    "manufacturer_name": "Nissan",
    "model_name": "Maxima",
    "car_type": "Sedan"
  },
  {
    "year": 2011,
    "manufacturer_name": "Porsche",
    "model_name": "Cayenne",
    "car_type": "SUV"
  },
  {
    "year": 2011,
    "manufacturer_name": "Nissan",
    "model_name": "Sentra",
    "car_type": "Sedan"
  },
  {
    "year": 2011,
    "manufacturer_name": "Nissan",
    "model_name": "Titan Crew Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2011,
    "manufacturer_name": "Nissan",
    "model_name": "Titan King Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2011,
    "manufacturer_name": "Nissan",
    "model_name": "Armada",
    "car_type": "SUV"
  },
  {
    "year": 2011,
    "manufacturer_name": "Nissan",
    "model_name": "Xterra",
    "car_type": "SUV"
  },
  {
    "year": 2011,
    "manufacturer_name": "Porsche",
    "model_name": "911",
    "car_type": "Convertible, Coupe"
  },
  {
    "year": 2011,
    "manufacturer_name": "Nissan",
    "model_name": "JUKE",
    "car_type": "SUV"
  },
  {
    "year": 2011,
    "manufacturer_name": "Ram",
    "model_name": "1500 Crew Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2011,
    "manufacturer_name": "Ram",
    "model_name": "1500 Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2011,
    "manufacturer_name": "Nissan",
    "model_name": "Quest",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2011,
    "manufacturer_name": "Rolls-Royce",
    "model_name": "Phantom",
    "car_type": "Convertible, Sedan, Coupe"
  },
  {
    "year": 2011,
    "manufacturer_name": "Porsche",
    "model_name": "Panamera",
    "car_type": "Sedan"
  },
  {
    "year": 2011,
    "manufacturer_name": "Nissan",
    "model_name": "Versa",
    "car_type": "Sedan, Hatchback"
  },
  {
    "year": 2011,
    "manufacturer_name": "Ram",
    "model_name": "3500 Crew Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2011,
    "manufacturer_name": "Ram",
    "model_name": "2500 Mega Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2011,
    "manufacturer_name": "Scion",
    "model_name": "xD",
    "car_type": "Hatchback"
  },
  {
    "year": 2011,
    "manufacturer_name": "Ram",
    "model_name": "1500 Quad Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2011,
    "manufacturer_name": "Ram",
    "model_name": "2500 Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2011,
    "manufacturer_name": "Saab",
    "model_name": "9-4X",
    "car_type": "SUV"
  },
  {
    "year": 2011,
    "manufacturer_name": "Subaru",
    "model_name": "Legacy",
    "car_type": "Sedan"
  },
  {
    "year": 2011,
    "manufacturer_name": "Porsche",
    "model_name": "Boxster",
    "car_type": "Convertible"
  },
  {
    "year": 2011,
    "manufacturer_name": "Ram",
    "model_name": "3500 Mega Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2011,
    "manufacturer_name": "Rolls-Royce",
    "model_name": "Ghost",
    "car_type": "Sedan"
  },
  {
    "year": 2011,
    "manufacturer_name": "Scion",
    "model_name": "xB",
    "car_type": "Hatchback"
  },
  {
    "year": 2011,
    "manufacturer_name": "Suzuki",
    "model_name": "Grand Vitara",
    "car_type": "SUV"
  },
  {
    "year": 2011,
    "manufacturer_name": "Suzuki",
    "model_name": "Equator Crew Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2011,
    "manufacturer_name": "Subaru",
    "model_name": "Forester",
    "car_type": "SUV"
  },
  {
    "year": 2011,
    "manufacturer_name": "Saab",
    "model_name": "3-Sep",
    "car_type": "Sedan, Convertible, Wagon"
  },
  {
    "year": 2011,
    "manufacturer_name": "Subaru",
    "model_name": "Impreza",
    "car_type": "Wagon, Sedan"
  },
  {
    "year": 2011,
    "manufacturer_name": "Ram",
    "model_name": "Dakota Crew Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2011,
    "manufacturer_name": "Ram",
    "model_name": "Dakota Extended Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2011,
    "manufacturer_name": "Toyota",
    "model_name": "Avalon",
    "car_type": "Sedan"
  },
  {
    "year": 2011,
    "manufacturer_name": "Porsche",
    "model_name": "Cayman",
    "car_type": "Coupe"
  },
  {
    "year": 2011,
    "manufacturer_name": "Scion",
    "model_name": "tC",
    "car_type": "Coupe"
  },
  {
    "year": 2011,
    "manufacturer_name": "Subaru",
    "model_name": "Tribeca",
    "car_type": "SUV"
  },
  {
    "year": 2011,
    "manufacturer_name": "Ram",
    "model_name": "2500 Crew Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2011,
    "manufacturer_name": "Suzuki",
    "model_name": "Equator Extended Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2011,
    "manufacturer_name": "smart",
    "model_name": "fortwo",
    "car_type": "Hatchback, Convertible"
  },
  {
    "year": 2011,
    "manufacturer_name": "Toyota",
    "model_name": "Camry",
    "car_type": "Sedan"
  },
  {
    "year": 2011,
    "manufacturer_name": "Saab",
    "model_name": "5-Sep",
    "car_type": "Sedan"
  },
  {
    "year": 2011,
    "manufacturer_name": "Ram",
    "model_name": "3500 Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2011,
    "manufacturer_name": "Suzuki",
    "model_name": "SX4",
    "car_type": "Sedan, Hatchback"
  },
  {
    "year": 2011,
    "manufacturer_name": "Subaru",
    "model_name": "Outback",
    "car_type": "Wagon"
  },
  {
    "year": 2011,
    "manufacturer_name": "Suzuki",
    "model_name": "Kizashi",
    "car_type": "Sedan"
  },
  {
    "year": 2011,
    "manufacturer_name": "Toyota",
    "model_name": "4Runner",
    "car_type": "SUV"
  },
  {
    "year": 2011,
    "manufacturer_name": "Toyota",
    "model_name": "Corolla",
    "car_type": "Sedan"
  },
  {
    "year": 2011,
    "manufacturer_name": "Toyota",
    "model_name": "Land Cruiser",
    "car_type": "SUV"
  },
  {
    "year": 2011,
    "manufacturer_name": "Toyota",
    "model_name": "Sienna",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2011,
    "manufacturer_name": "Toyota",
    "model_name": "Tacoma Double Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2011,
    "manufacturer_name": "Toyota",
    "model_name": "Highlander",
    "car_type": "SUV"
  },
  {
    "year": 2011,
    "manufacturer_name": "Toyota",
    "model_name": "Matrix",
    "car_type": "Wagon"
  },
  {
    "year": 2011,
    "manufacturer_name": "Toyota",
    "model_name": "Tacoma Access Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2011,
    "manufacturer_name": "Toyota",
    "model_name": "RAV4",
    "car_type": "SUV"
  },
  {
    "year": 2011,
    "manufacturer_name": "Toyota",
    "model_name": "FJ Cruiser",
    "car_type": "SUV"
  },
  {
    "year": 2011,
    "manufacturer_name": "Toyota",
    "model_name": "Prius",
    "car_type": "Hatchback"
  },
  {
    "year": 2011,
    "manufacturer_name": "Toyota",
    "model_name": "Sequoia",
    "car_type": "SUV"
  },
  {
    "year": 2011,
    "manufacturer_name": "Toyota",
    "model_name": "Tundra Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2011,
    "manufacturer_name": "Toyota",
    "model_name": "Yaris",
    "car_type": "Hatchback, Sedan"
  },
  {
    "year": 2011,
    "manufacturer_name": "Volkswagen",
    "model_name": "Golf",
    "car_type": "Hatchback"
  },
  {
    "year": 2011,
    "manufacturer_name": "Volkswagen",
    "model_name": "Eos",
    "car_type": "Convertible"
  },
  {
    "year": 2011,
    "manufacturer_name": "Toyota",
    "model_name": "Tundra CrewMax",
    "car_type": "Pickup"
  },
  {
    "year": 2011,
    "manufacturer_name": "Toyota",
    "model_name": "Tacoma Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2011,
    "manufacturer_name": "Toyota",
    "model_name": "Tundra Double Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2011,
    "manufacturer_name": "Toyota",
    "model_name": "Venza",
    "car_type": "Wagon"
  },
  {
    "year": 2011,
    "manufacturer_name": "Volvo",
    "model_name": "S80",
    "car_type": "Sedan"
  },
  {
    "year": 2011,
    "manufacturer_name": "Volkswagen",
    "model_name": "Touareg",
    "car_type": "SUV"
  },
  {
    "year": 2011,
    "manufacturer_name": "Volvo",
    "model_name": "S60",
    "car_type": "Sedan"
  },
  {
    "year": 2011,
    "manufacturer_name": "Volkswagen",
    "model_name": "GTI",
    "car_type": "Hatchback"
  },
  {
    "year": 2011,
    "manufacturer_name": "Volkswagen",
    "model_name": "Tiguan",
    "car_type": "SUV"
  },
  {
    "year": 2011,
    "manufacturer_name": "Volkswagen",
    "model_name": "Jetta",
    "car_type": "Sedan, Wagon"
  },
  {
    "year": 2011,
    "manufacturer_name": "Volkswagen",
    "model_name": "CC",
    "car_type": "Sedan"
  },
  {
    "year": 2010,
    "manufacturer_name": "Acura",
    "model_name": "MDX",
    "car_type": "SUV"
  },
  {
    "year": 2010,
    "manufacturer_name": "Audi",
    "model_name": "S4",
    "car_type": "Sedan"
  },
  {
    "year": 2010,
    "manufacturer_name": "Acura",
    "model_name": "TSX",
    "car_type": "Sedan"
  },
  {
    "year": 2010,
    "manufacturer_name": "Acura",
    "model_name": "RDX",
    "car_type": "SUV"
  },
  {
    "year": 2011,
    "manufacturer_name": "Volvo",
    "model_name": "C70",
    "car_type": "Convertible"
  },
  {
    "year": 2011,
    "manufacturer_name": "Volvo",
    "model_name": "C30",
    "car_type": "Hatchback"
  },
  {
    "year": 2011,
    "manufacturer_name": "Volvo",
    "model_name": "V50",
    "car_type": "Wagon"
  },
  {
    "year": 2010,
    "manufacturer_name": "Audi",
    "model_name": "A3",
    "car_type": "Wagon"
  },
  {
    "year": 2011,
    "manufacturer_name": "Volvo",
    "model_name": "S40",
    "car_type": "Sedan"
  },
  {
    "year": 2010,
    "manufacturer_name": "Acura",
    "model_name": "RL",
    "car_type": "Sedan"
  },
  {
    "year": 2011,
    "manufacturer_name": "Volvo",
    "model_name": "XC60",
    "car_type": "SUV"
  },
  {
    "year": 2011,
    "manufacturer_name": "Volvo",
    "model_name": "XC90",
    "car_type": "SUV"
  },
  {
    "year": 2010,
    "manufacturer_name": "Bentley",
    "model_name": "Continental",
    "car_type": "Convertible, Sedan, Coupe"
  },
  {
    "year": 2011,
    "manufacturer_name": "Volvo",
    "model_name": "XC70",
    "car_type": "Wagon"
  },
  {
    "year": 2010,
    "manufacturer_name": "Aston Martin",
    "model_name": "DB9",
    "car_type": "Coupe, Convertible"
  },
  {
    "year": 2010,
    "manufacturer_name": "Aston Martin",
    "model_name": "DBS",
    "car_type": "Coupe, Convertible"
  },
  {
    "year": 2010,
    "manufacturer_name": "Acura",
    "model_name": "ZDX",
    "car_type": "SUV"
  },
  {
    "year": 2010,
    "manufacturer_name": "Acura",
    "model_name": "TL",
    "car_type": "Sedan"
  },
  {
    "year": 2010,
    "manufacturer_name": "Audi",
    "model_name": "S6",
    "car_type": "Sedan"
  },
  {
    "year": 2010,
    "manufacturer_name": "Audi",
    "model_name": "S5",
    "car_type": "Coupe, Convertible"
  },
  {
    "year": 2010,
    "manufacturer_name": "Audi",
    "model_name": "Q7",
    "car_type": "SUV"
  },
  {
    "year": 2010,
    "manufacturer_name": "BMW",
    "model_name": "M3",
    "car_type": "Coupe, Sedan, Convertible"
  },
  {
    "year": 2010,
    "manufacturer_name": "Aston Martin",
    "model_name": "Vantage",
    "car_type": "Coupe, Convertible"
  },
  {
    "year": 2010,
    "manufacturer_name": "Audi",
    "model_name": "A4",
    "car_type": "Sedan, Wagon"
  },
  {
    "year": 2010,
    "manufacturer_name": "Audi",
    "model_name": "TT",
    "car_type": "Coupe, Convertible"
  },
  {
    "year": 2010,
    "manufacturer_name": "Audi",
    "model_name": "A8",
    "car_type": "Sedan"
  },
  {
    "year": 2011,
    "manufacturer_name": "Volkswagen",
    "model_name": "Routan",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2010,
    "manufacturer_name": "Audi",
    "model_name": "A5",
    "car_type": "Coupe, Convertible"
  },
  {
    "year": 2010,
    "manufacturer_name": "BMW",
    "model_name": "1 Series",
    "car_type": "Coupe, Convertible"
  },
  {
    "year": 2010,
    "manufacturer_name": "Aston Martin",
    "model_name": "Rapide",
    "car_type": "Sedan"
  },
  {
    "year": 2010,
    "manufacturer_name": "Audi",
    "model_name": "Q5",
    "car_type": "SUV"
  },
  {
    "year": 2010,
    "manufacturer_name": "Audi",
    "model_name": "A6",
    "car_type": "Sedan, Wagon"
  },
  {
    "year": 2010,
    "manufacturer_name": "BMW",
    "model_name": "7 Series",
    "car_type": "Sedan"
  },
  {
    "year": 2010,
    "manufacturer_name": "BMW",
    "model_name": "X5 M",
    "car_type": "SUV"
  },
  {
    "year": 2010,
    "manufacturer_name": "BMW",
    "model_name": "3 Series",
    "car_type": "Sedan, Coupe, Convertible, Wagon"
  },
  {
    "year": 2010,
    "manufacturer_name": "BMW",
    "model_name": "X5",
    "car_type": "SUV"
  },
  {
    "year": 2010,
    "manufacturer_name": "Buick",
    "model_name": "LaCrosse",
    "car_type": "Sedan"
  },
  {
    "year": 2010,
    "manufacturer_name": "Bentley",
    "model_name": "Azure T",
    "car_type": "Convertible"
  },
  {
    "year": 2010,
    "manufacturer_name": "Bentley",
    "model_name": "Brooklands",
    "car_type": "Coupe"
  },
  {
    "year": 2010,
    "manufacturer_name": "BMW",
    "model_name": "6 Series",
    "car_type": "Coupe, Convertible"
  },
  {
    "year": 2010,
    "manufacturer_name": "Audi",
    "model_name": "R8",
    "car_type": "Coupe"
  },
  {
    "year": 2010,
    "manufacturer_name": "BMW",
    "model_name": "5 Series",
    "car_type": "Sedan, Wagon"
  },
  {
    "year": 2010,
    "manufacturer_name": "Cadillac",
    "model_name": "Escalade ESV",
    "car_type": "SUV"
  },
  {
    "year": 2010,
    "manufacturer_name": "Buick",
    "model_name": "Enclave",
    "car_type": "SUV"
  },
  {
    "year": 2010,
    "manufacturer_name": "Buick",
    "model_name": "Lucerne",
    "car_type": "Sedan"
  },
  {
    "year": 2010,
    "manufacturer_name": "Chevrolet",
    "model_name": "Colorado Extended Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2010,
    "manufacturer_name": "BMW",
    "model_name": "M5",
    "car_type": "Sedan"
  },
  {
    "year": 2010,
    "manufacturer_name": "Chevrolet",
    "model_name": "HHR",
    "car_type": "Wagon"
  },
  {
    "year": 2010,
    "manufacturer_name": "BMW",
    "model_name": "X6 M",
    "car_type": "SUV"
  },
  {
    "year": 2010,
    "manufacturer_name": "Chevrolet",
    "model_name": "Equinox",
    "car_type": "SUV"
  },
  {
    "year": 2010,
    "manufacturer_name": "BMW",
    "model_name": "M6",
    "car_type": "Coupe, Convertible"
  },
  {
    "year": 2010,
    "manufacturer_name": "Cadillac",
    "model_name": "Escalade",
    "car_type": "SUV"
  },
  {
    "year": 2010,
    "manufacturer_name": "Chevrolet",
    "model_name": "Express 3500 Cargo",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2010,
    "manufacturer_name": "BMW",
    "model_name": "Z4",
    "car_type": "Convertible"
  },
  {
    "year": 2010,
    "manufacturer_name": "Chevrolet",
    "model_name": "Express 1500 Passenger",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2010,
    "manufacturer_name": "Cadillac",
    "model_name": "STS",
    "car_type": "Sedan"
  },
  {
    "year": 2010,
    "manufacturer_name": "BMW",
    "model_name": "X6",
    "car_type": "SUV"
  },
  {
    "year": 2010,
    "manufacturer_name": "Chevrolet",
    "model_name": "Express 2500 Passenger",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2010,
    "manufacturer_name": "BMW",
    "model_name": "X3",
    "car_type": "SUV"
  },
  {
    "year": 2010,
    "manufacturer_name": "Cadillac",
    "model_name": "SRX",
    "car_type": "SUV"
  },
  {
    "year": 2010,
    "manufacturer_name": "Chevrolet",
    "model_name": "Camaro",
    "car_type": "Coupe"
  },
  {
    "year": 2010,
    "manufacturer_name": "Chevrolet",
    "model_name": "Express 2500 Cargo",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2010,
    "manufacturer_name": "Chevrolet",
    "model_name": "Impala",
    "car_type": "Sedan"
  },
  {
    "year": 2010,
    "manufacturer_name": "Cadillac",
    "model_name": "CTS",
    "car_type": "Sedan, Wagon"
  },
  {
    "year": 2010,
    "manufacturer_name": "Chevrolet",
    "model_name": "Avalanche",
    "car_type": "SUV"
  },
  {
    "year": 2010,
    "manufacturer_name": "Chevrolet",
    "model_name": "Express 1500 Cargo",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2010,
    "manufacturer_name": "Chevrolet",
    "model_name": "Colorado Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2010,
    "manufacturer_name": "Chevrolet",
    "model_name": "Cobalt",
    "car_type": "Sedan, Coupe"
  },
  {
    "year": 2010,
    "manufacturer_name": "Chevrolet",
    "model_name": "Aveo",
    "car_type": "Sedan, Hatchback"
  },
  {
    "year": 2010,
    "manufacturer_name": "Chevrolet",
    "model_name": "Corvette",
    "car_type": "Coupe, Convertible"
  },
  {
    "year": 2010,
    "manufacturer_name": "Cadillac",
    "model_name": "Escalade EXT",
    "car_type": "Pickup"
  },
  {
    "year": 2010,
    "manufacturer_name": "Chevrolet",
    "model_name": "Express 3500 Passenger",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2010,
    "manufacturer_name": "Cadillac",
    "model_name": "DTS",
    "car_type": "Sedan"
  },
  {
    "year": 2010,
    "manufacturer_name": "Chevrolet",
    "model_name": "Colorado Crew Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2010,
    "manufacturer_name": "Chevrolet",
    "model_name": "Silverado 1500 Extended Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2010,
    "manufacturer_name": "Chevrolet",
    "model_name": "Malibu",
    "car_type": "Sedan"
  },
  {
    "year": 2010,
    "manufacturer_name": "Dodge",
    "model_name": "Ram 2500 Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2010,
    "manufacturer_name": "Chevrolet",
    "model_name": "Silverado 3500 HD Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2010,
    "manufacturer_name": "Dodge",
    "model_name": "Caliber",
    "car_type": "Wagon"
  },
  {
    "year": 2010,
    "manufacturer_name": "Chevrolet",
    "model_name": "Traverse",
    "car_type": "SUV"
  },
  {
    "year": 2010,
    "manufacturer_name": "Chevrolet",
    "model_name": "Silverado 2500 HD Crew Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2010,
    "manufacturer_name": "Chrysler",
    "model_name": "PT Cruiser",
    "car_type": "Wagon"
  },
  {
    "year": 2010,
    "manufacturer_name": "Dodge",
    "model_name": "Avenger",
    "car_type": "Sedan"
  },
  {
    "year": 2010,
    "manufacturer_name": "Chrysler",
    "model_name": "Sebring",
    "car_type": "Sedan, Convertible"
  },
  {
    "year": 2010,
    "manufacturer_name": "Chrysler",
    "model_name": "Town & Country",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2010,
    "manufacturer_name": "Chevrolet",
    "model_name": "Silverado 1500 Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2010,
    "manufacturer_name": "Dodge",
    "model_name": "Ram 1500 Quad Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2010,
    "manufacturer_name": "Chevrolet",
    "model_name": "Silverado 1500 Crew Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2010,
    "manufacturer_name": "Dodge",
    "model_name": "Dakota Extended Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2010,
    "manufacturer_name": "Chevrolet",
    "model_name": "Tahoe",
    "car_type": "SUV"
  },
  {
    "year": 2010,
    "manufacturer_name": "Chevrolet",
    "model_name": "Silverado 2500 HD Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2010,
    "manufacturer_name": "Dodge",
    "model_name": "Charger",
    "car_type": "Sedan"
  },
  {
    "year": 2010,
    "manufacturer_name": "Dodge",
    "model_name": "Grand Caravan Cargo",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2010,
    "manufacturer_name": "Chevrolet",
    "model_name": "Silverado 2500 HD Extended Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2010,
    "manufacturer_name": "Dodge",
    "model_name": "Ram 1500 Crew Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2010,
    "manufacturer_name": "Dodge",
    "model_name": "Challenger",
    "car_type": "Coupe"
  },
  {
    "year": 2010,
    "manufacturer_name": "Dodge",
    "model_name": "Dakota Crew Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2010,
    "manufacturer_name": "Chrysler",
    "model_name": "300",
    "car_type": "Sedan"
  },
  {
    "year": 2010,
    "manufacturer_name": "Dodge",
    "model_name": "Journey",
    "car_type": "SUV"
  },
  {
    "year": 2010,
    "manufacturer_name": "Dodge",
    "model_name": "Ram 2500 Mega Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2010,
    "manufacturer_name": "Dodge",
    "model_name": "Grand Caravan Passenger",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2010,
    "manufacturer_name": "Dodge",
    "model_name": "Nitro",
    "car_type": "SUV"
  },
  {
    "year": 2010,
    "manufacturer_name": "Dodge",
    "model_name": "Ram 1500 Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2010,
    "manufacturer_name": "Chevrolet",
    "model_name": "Silverado 3500 HD Extended Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2010,
    "manufacturer_name": "Chevrolet",
    "model_name": "Silverado 3500 HD Crew Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2010,
    "manufacturer_name": "Chevrolet",
    "model_name": "Suburban 1500",
    "car_type": "SUV"
  },
  {
    "year": 2010,
    "manufacturer_name": "Chevrolet",
    "model_name": "Suburban 2500",
    "car_type": "SUV"
  },
  {
    "year": 2010,
    "manufacturer_name": "Dodge",
    "model_name": "Ram 3500 Crew Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2010,
    "manufacturer_name": "Dodge",
    "model_name": "Ram 2500 Crew Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2010,
    "manufacturer_name": "Dodge",
    "model_name": "Viper",
    "car_type": "Convertible, Coupe"
  },
  {
    "year": 2010,
    "manufacturer_name": "Ferrari",
    "model_name": "458 Italia",
    "car_type": "Coupe"
  },
  {
    "year": 2010,
    "manufacturer_name": "Dodge",
    "model_name": "Ram 3500 Mega Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2010,
    "manufacturer_name": "Ford",
    "model_name": "E250 Cargo",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2010,
    "manufacturer_name": "Ferrari",
    "model_name": "612 Scaglietti",
    "car_type": "Coupe"
  },
  {
    "year": 2010,
    "manufacturer_name": "Ford",
    "model_name": "Crown Victoria",
    "car_type": "Sedan"
  },
  {
    "year": 2010,
    "manufacturer_name": "Ford",
    "model_name": "E350 Super Duty Passenger",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2010,
    "manufacturer_name": "Ford",
    "model_name": "F150 Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2010,
    "manufacturer_name": "Ford",
    "model_name": "E150 Cargo",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2010,
    "manufacturer_name": "Dodge",
    "model_name": "Ram 3500 Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2010,
    "manufacturer_name": "Ford",
    "model_name": "Expedition",
    "car_type": "SUV"
  },
  {
    "year": 2010,
    "manufacturer_name": "Ford",
    "model_name": "Edge",
    "car_type": "SUV"
  },
  {
    "year": 2010,
    "manufacturer_name": "Ford",
    "model_name": "E150 Super Duty Passenger",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2010,
    "manufacturer_name": "Ford",
    "model_name": "E350 Super Duty Cargo",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2010,
    "manufacturer_name": "Ford",
    "model_name": "F150 Super Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2010,
    "manufacturer_name": "Ferrari",
    "model_name": "California",
    "car_type": "Convertible"
  },
  {
    "year": 2010,
    "manufacturer_name": "Ford",
    "model_name": "Explorer Sport Trac",
    "car_type": "Pickup"
  },
  {
    "year": 2010,
    "manufacturer_name": "Ferrari",
    "model_name": "599 GTB Fiorano",
    "car_type": "Coupe"
  },
  {
    "year": 2010,
    "manufacturer_name": "Ford",
    "model_name": "F250 Super Duty Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2010,
    "manufacturer_name": "Ford",
    "model_name": "Escape",
    "car_type": "SUV"
  },
  {
    "year": 2010,
    "manufacturer_name": "Ford",
    "model_name": "Expedition EL",
    "car_type": "SUV"
  },
  {
    "year": 2010,
    "manufacturer_name": "Ford",
    "model_name": "Ranger Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2010,
    "manufacturer_name": "Ford",
    "model_name": "Explorer",
    "car_type": "SUV"
  },
  {
    "year": 2010,
    "manufacturer_name": "Ford",
    "model_name": "F350 Super Duty Super Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2010,
    "manufacturer_name": "Ford",
    "model_name": "F250 Super Duty Super Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2010,
    "manufacturer_name": "Ford",
    "model_name": "F250 Super Duty Crew Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2010,
    "manufacturer_name": "Ford",
    "model_name": "F350 Super Duty Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2010,
    "manufacturer_name": "Ford",
    "model_name": "F150 SuperCrew Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2010,
    "manufacturer_name": "Ford",
    "model_name": "F450 Super Duty Crew Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2010,
    "manufacturer_name": "GMC",
    "model_name": "Savana 1500 Passenger",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2010,
    "manufacturer_name": "GMC",
    "model_name": "Yukon",
    "car_type": "SUV"
  },
  {
    "year": 2010,
    "manufacturer_name": "Ford",
    "model_name": "Fusion",
    "car_type": "Sedan"
  },
  {
    "year": 2010,
    "manufacturer_name": "Ford",
    "model_name": "Focus",
    "car_type": "Sedan, Coupe"
  },
  {
    "year": 2010,
    "manufacturer_name": "Ford",
    "model_name": "Flex",
    "car_type": "SUV"
  },
  {
    "year": 2010,
    "manufacturer_name": "GMC",
    "model_name": "Canyon Crew Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2010,
    "manufacturer_name": "GMC",
    "model_name": "Terrain",
    "car_type": "SUV"
  },
  {
    "year": 2010,
    "manufacturer_name": "GMC",
    "model_name": "Sierra 2500 HD Crew Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2010,
    "manufacturer_name": "Ford",
    "model_name": "Transit Connect Passenger",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2010,
    "manufacturer_name": "Ford",
    "model_name": "F350 Super Duty Crew Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2010,
    "manufacturer_name": "GMC",
    "model_name": "Savana 1500 Cargo",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2010,
    "manufacturer_name": "GMC",
    "model_name": "Sierra 1500 Crew Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2010,
    "manufacturer_name": "Ford",
    "model_name": "Mustang",
    "car_type": "Coupe, Convertible"
  },
  {
    "year": 2010,
    "manufacturer_name": "Ford",
    "model_name": "Ranger Super Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2010,
    "manufacturer_name": "GMC",
    "model_name": "Canyon Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2010,
    "manufacturer_name": "Ford",
    "model_name": "Transit Connect Cargo",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2010,
    "manufacturer_name": "Ford",
    "model_name": "Taurus",
    "car_type": "Sedan"
  },
  {
    "year": 2010,
    "manufacturer_name": "GMC",
    "model_name": "Sierra 2500 HD Extended Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2010,
    "manufacturer_name": "GMC",
    "model_name": "Canyon Extended Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2010,
    "manufacturer_name": "GMC",
    "model_name": "Savana 3500 Passenger",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2010,
    "manufacturer_name": "GMC",
    "model_name": "Acadia",
    "car_type": "SUV"
  },
  {
    "year": 2010,
    "manufacturer_name": "GMC",
    "model_name": "Savana 2500 Passenger",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2010,
    "manufacturer_name": "GMC",
    "model_name": "Savana 2500 Cargo",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2010,
    "manufacturer_name": "GMC",
    "model_name": "Sierra 1500 Extended Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2010,
    "manufacturer_name": "GMC",
    "model_name": "Savana 3500 Cargo",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2010,
    "manufacturer_name": "GMC",
    "model_name": "Sierra 3500 HD Crew Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2010,
    "manufacturer_name": "Honda",
    "model_name": "Civic",
    "car_type": "Sedan, Coupe"
  },
  {
    "year": 2010,
    "manufacturer_name": "Honda",
    "model_name": "Accord Crosstour",
    "car_type": "SUV"
  },
  {
    "year": 2010,
    "manufacturer_name": "GMC",
    "model_name": "Sierra 2500 HD Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2010,
    "manufacturer_name": "GMC",
    "model_name": "Sierra 1500 Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2010,
    "manufacturer_name": "GMC",
    "model_name": "Sierra 3500 HD Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2010,
    "manufacturer_name": "Honda",
    "model_name": "Accord",
    "car_type": "Sedan, Coupe"
  },
  {
    "year": 2010,
    "manufacturer_name": "GMC",
    "model_name": "Sierra 3500 HD Extended Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2010,
    "manufacturer_name": "Honda",
    "model_name": "CR-V",
    "car_type": "SUV"
  },
  {
    "year": 2010,
    "manufacturer_name": "GMC",
    "model_name": "Yukon XL 2500",
    "car_type": "SUV"
  },
  {
    "year": 2010,
    "manufacturer_name": "GMC",
    "model_name": "Yukon XL 1500",
    "car_type": "SUV"
  },
  {
    "year": 2010,
    "manufacturer_name": "Honda",
    "model_name": "Odyssey",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2010,
    "manufacturer_name": "Hyundai",
    "model_name": "Accent",
    "car_type": "Hatchback, Sedan"
  },
  {
    "year": 2010,
    "manufacturer_name": "Hyundai",
    "model_name": "Sonata",
    "car_type": "Sedan"
  },
  {
    "year": 2010,
    "manufacturer_name": "Honda",
    "model_name": "Fit",
    "car_type": "Hatchback"
  },
  {
    "year": 2010,
    "manufacturer_name": "Hyundai",
    "model_name": "Azera",
    "car_type": "Sedan"
  },
  {
    "year": 2010,
    "manufacturer_name": "Honda",
    "model_name": "Pilot",
    "car_type": "SUV"
  },
  {
    "year": 2010,
    "manufacturer_name": "HUMMER",
    "model_name": "H3T",
    "car_type": "Pickup"
  },
  {
    "year": 2010,
    "manufacturer_name": "INFINITI",
    "model_name": "FX",
    "car_type": "SUV"
  },
  {
    "year": 2010,
    "manufacturer_name": "Honda",
    "model_name": "Element",
    "car_type": "SUV"
  },
  {
    "year": 2010,
    "manufacturer_name": "Hyundai",
    "model_name": "Genesis Coupe",
    "car_type": "Coupe"
  },
  {
    "year": 2010,
    "manufacturer_name": "HUMMER",
    "model_name": "H3",
    "car_type": "SUV"
  },
  {
    "year": 2010,
    "manufacturer_name": "INFINITI",
    "model_name": "G",
    "car_type": "Coupe, Sedan, Convertible"
  },
  {
    "year": 2010,
    "manufacturer_name": "Honda",
    "model_name": "Insight",
    "car_type": "Hatchback"
  },
  {
    "year": 2010,
    "manufacturer_name": "Honda",
    "model_name": "Ridgeline",
    "car_type": "Pickup"
  },
  {
    "year": 2010,
    "manufacturer_name": "Hyundai",
    "model_name": "Genesis",
    "car_type": "Sedan"
  },
  {
    "year": 2010,
    "manufacturer_name": "Hyundai",
    "model_name": "Santa Fe",
    "car_type": "SUV"
  },
  {
    "year": 2010,
    "manufacturer_name": "Hyundai",
    "model_name": "Elantra",
    "car_type": "Wagon, Sedan"
  },
  {
    "year": 2010,
    "manufacturer_name": "INFINITI",
    "model_name": "EX",
    "car_type": "SUV"
  },
  {
    "year": 2010,
    "manufacturer_name": "Hyundai",
    "model_name": "Veracruz",
    "car_type": "SUV"
  },
  {
    "year": 2010,
    "manufacturer_name": "INFINITI",
    "model_name": "QX",
    "car_type": "SUV"
  },
  {
    "year": 2010,
    "manufacturer_name": "Hyundai",
    "model_name": "Tucson",
    "car_type": "SUV"
  },
  {
    "year": 2010,
    "manufacturer_name": "Jaguar",
    "model_name": "XK",
    "car_type": "Coupe, Convertible"
  },
  {
    "year": 2010,
    "manufacturer_name": "Jeep",
    "model_name": "Patriot",
    "car_type": "SUV"
  },
  {
    "year": 2010,
    "manufacturer_name": "Jeep",
    "model_name": "Compass",
    "car_type": "SUV"
  },
  {
    "year": 2010,
    "manufacturer_name": "Jeep",
    "model_name": "Liberty",
    "car_type": "SUV"
  },
  {
    "year": 2010,
    "manufacturer_name": "Kia",
    "model_name": "Rondo",
    "car_type": "Wagon"
  },
  {
    "year": 2010,
    "manufacturer_name": "INFINITI",
    "model_name": "M",
    "car_type": "Sedan"
  },
  {
    "year": 2010,
    "manufacturer_name": "Jaguar",
    "model_name": "XF",
    "car_type": "Sedan"
  },
  {
    "year": 2010,
    "manufacturer_name": "Jeep",
    "model_name": "Commander",
    "car_type": "SUV"
  },
  {
    "year": 2010,
    "manufacturer_name": "Kia",
    "model_name": "Rio",
    "car_type": "Sedan, Hatchback"
  },
  {
    "year": 2010,
    "manufacturer_name": "Lamborghini",
    "model_name": "Murcielago",
    "car_type": "Coupe, Convertible"
  },
  {
    "year": 2010,
    "manufacturer_name": "Jeep",
    "model_name": "Wrangler",
    "car_type": "SUV"
  },
  {
    "year": 2010,
    "manufacturer_name": "Kia",
    "model_name": "Optima",
    "car_type": "Sedan"
  },
  {
    "year": 2010,
    "manufacturer_name": "Kia",
    "model_name": "Forte",
    "car_type": "Sedan, Coupe"
  },
  {
    "year": 2010,
    "manufacturer_name": "Jeep",
    "model_name": "Grand Cherokee",
    "car_type": "SUV"
  },
  {
    "year": 2010,
    "manufacturer_name": "Lamborghini",
    "model_name": "Gallardo",
    "car_type": "Coupe, Convertible"
  },
  {
    "year": 2010,
    "manufacturer_name": "Kia",
    "model_name": "Sedona",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2010,
    "manufacturer_name": "Land Rover",
    "model_name": "Range Rover Sport",
    "car_type": "SUV"
  },
  {
    "year": 2010,
    "manufacturer_name": "Lexus",
    "model_name": "GS",
    "car_type": "Sedan"
  },
  {
    "year": 2010,
    "manufacturer_name": "Land Rover",
    "model_name": "LR4",
    "car_type": "SUV"
  },
  {
    "year": 2010,
    "manufacturer_name": "Lincoln",
    "model_name": "MKS",
    "car_type": "Sedan"
  },
  {
    "year": 2010,
    "manufacturer_name": "Lexus",
    "model_name": "RX",
    "car_type": "SUV"
  },
  {
    "year": 2010,
    "manufacturer_name": "Kia",
    "model_name": "Soul",
    "car_type": "Wagon"
  },
  {
    "year": 2010,
    "manufacturer_name": "Lincoln",
    "model_name": "MKX",
    "car_type": "SUV"
  },
  {
    "year": 2010,
    "manufacturer_name": "Lincoln",
    "model_name": "Navigator L",
    "car_type": "SUV"
  },
  {
    "year": 2010,
    "manufacturer_name": "Lexus",
    "model_name": "IS",
    "car_type": "Convertible, Sedan"
  },
  {
    "year": 2010,
    "manufacturer_name": "Lexus",
    "model_name": "SC",
    "car_type": "Convertible"
  },
  {
    "year": 2010,
    "manufacturer_name": "Lincoln",
    "model_name": "Navigator",
    "car_type": "SUV"
  },
  {
    "year": 2010,
    "manufacturer_name": "Lincoln",
    "model_name": "Town Car",
    "car_type": "Sedan"
  },
  {
    "year": 2010,
    "manufacturer_name": "Kia",
    "model_name": "Sportage",
    "car_type": "SUV"
  },
  {
    "year": 2010,
    "manufacturer_name": "Land Rover",
    "model_name": "Range Rover",
    "car_type": "SUV"
  },
  {
    "year": 2010,
    "manufacturer_name": "Lexus",
    "model_name": "ES",
    "car_type": "Sedan"
  },
  {
    "year": 2010,
    "manufacturer_name": "Land Rover",
    "model_name": "LR2",
    "car_type": "SUV"
  },
  {
    "year": 2010,
    "manufacturer_name": "Lexus",
    "model_name": "GX",
    "car_type": "SUV"
  },
  {
    "year": 2010,
    "manufacturer_name": "Lotus",
    "model_name": "Exige",
    "car_type": "Coupe"
  },
  {
    "year": 2010,
    "manufacturer_name": "Lexus",
    "model_name": "HS",
    "car_type": "Sedan"
  },
  {
    "year": 2010,
    "manufacturer_name": "Lexus",
    "model_name": "LX",
    "car_type": "SUV"
  },
  {
    "year": 2010,
    "manufacturer_name": "Lincoln",
    "model_name": "MKZ",
    "car_type": "Sedan"
  },
  {
    "year": 2010,
    "manufacturer_name": "Lexus",
    "model_name": "IS F",
    "car_type": "Sedan"
  },
  {
    "year": 2010,
    "manufacturer_name": "Lincoln",
    "model_name": "MKT",
    "car_type": "SUV"
  },
  {
    "year": 2010,
    "manufacturer_name": "Lexus",
    "model_name": "LS",
    "car_type": "Sedan"
  },
  {
    "year": 2010,
    "manufacturer_name": "Mercedes-Benz",
    "model_name": "CLS-Class",
    "car_type": "Coupe"
  },
  {
    "year": 2010,
    "manufacturer_name": "Lotus",
    "model_name": "Evora",
    "car_type": "Coupe"
  },
  {
    "year": 2010,
    "manufacturer_name": "Maserati",
    "model_name": "Quattroporte",
    "car_type": "Sedan"
  },
  {
    "year": 2010,
    "manufacturer_name": "MAZDA",
    "model_name": "RX-8",
    "car_type": "Coupe"
  },
  {
    "year": 2010,
    "manufacturer_name": "Lotus",
    "model_name": "Elise",
    "car_type": "Coupe"
  },
  {
    "year": 2010,
    "manufacturer_name": "Maserati",
    "model_name": "GranTurismo",
    "car_type": "Convertible, Coupe"
  },
  {
    "year": 2010,
    "manufacturer_name": "MAZDA",
    "model_name": "CX-7",
    "car_type": "SUV"
  },
  {
    "year": 2010,
    "manufacturer_name": "MAZDA",
    "model_name": "MAZDA3",
    "car_type": "Sedan, Hatchback"
  },
  {
    "year": 2010,
    "manufacturer_name": "Maybach",
    "model_name": "62",
    "car_type": "Sedan"
  },
  {
    "year": 2010,
    "manufacturer_name": "MAZDA",
    "model_name": "CX-9",
    "car_type": "SUV"
  },
  {
    "year": 2010,
    "manufacturer_name": "MAZDA",
    "model_name": "Tribute",
    "car_type": "SUV"
  },
  {
    "year": 2010,
    "manufacturer_name": "Maybach",
    "model_name": "57",
    "car_type": "Sedan"
  },
  {
    "year": 2010,
    "manufacturer_name": "MAZDA",
    "model_name": "MAZDA5",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2010,
    "manufacturer_name": "MAZDA",
    "model_name": "MX-5 Miata",
    "car_type": "Convertible"
  },
  {
    "year": 2010,
    "manufacturer_name": "MAZDA",
    "model_name": "MAZDA6",
    "car_type": "Sedan"
  },
  {
    "year": 2010,
    "manufacturer_name": "Mercedes-Benz",
    "model_name": "G-Class",
    "car_type": "SUV"
  },
  {
    "year": 2010,
    "manufacturer_name": "MINI",
    "model_name": "Hardtop",
    "car_type": "Hatchback"
  },
  {
    "year": 2010,
    "manufacturer_name": "Nissan",
    "model_name": "Altima",
    "car_type": "Sedan, Coupe"
  },
  {
    "year": 2010,
    "manufacturer_name": "Mercedes-Benz",
    "model_name": "C-Class",
    "car_type": "Sedan"
  },
  {
    "year": 2010,
    "manufacturer_name": "Mitsubishi",
    "model_name": "Endeavor",
    "car_type": "SUV"
  },
  {
    "year": 2010,
    "manufacturer_name": "Mercedes-Benz",
    "model_name": "S-Class",
    "car_type": "Sedan"
  },
  {
    "year": 2010,
    "manufacturer_name": "Mitsubishi",
    "model_name": "Outlander",
    "car_type": "SUV"
  },
  {
    "year": 2010,
    "manufacturer_name": "Mercedes-Benz",
    "model_name": "SLK-Class",
    "car_type": "Convertible"
  },
  {
    "year": 2010,
    "manufacturer_name": "Mercedes-Benz",
    "model_name": "R-Class",
    "car_type": "Wagon"
  },
  {
    "year": 2010,
    "manufacturer_name": "Mercedes-Benz",
    "model_name": "M-Class",
    "car_type": "SUV"
  },
  {
    "year": 2010,
    "manufacturer_name": "Mitsubishi",
    "model_name": "Lancer",
    "car_type": "Sedan, Hatchback"
  },
  {
    "year": 2010,
    "manufacturer_name": "Mercury",
    "model_name": "Grand Marquis",
    "car_type": "Sedan"
  },
  {
    "year": 2010,
    "manufacturer_name": "Mercury",
    "model_name": "Milan",
    "car_type": "Sedan"
  },
  {
    "year": 2010,
    "manufacturer_name": "Mercedes-Benz",
    "model_name": "E-Class",
    "car_type": "Sedan, Coupe"
  },
  {
    "year": 2010,
    "manufacturer_name": "MINI",
    "model_name": "Convertible",
    "car_type": "Convertible"
  },
  {
    "year": 2010,
    "manufacturer_name": "Mercedes-Benz",
    "model_name": "GL-Class",
    "car_type": "SUV"
  },
  {
    "year": 2010,
    "manufacturer_name": "Nissan",
    "model_name": "370Z",
    "car_type": "Convertible, Coupe"
  },
  {
    "year": 2010,
    "manufacturer_name": "Mercedes-Benz",
    "model_name": "CL-Class",
    "car_type": "Coupe"
  },
  {
    "year": 2010,
    "manufacturer_name": "Mercury",
    "model_name": "Mountaineer",
    "car_type": "SUV"
  },
  {
    "year": 2010,
    "manufacturer_name": "MINI",
    "model_name": "Clubman",
    "car_type": "Hatchback"
  },
  {
    "year": 2010,
    "manufacturer_name": "Mercury",
    "model_name": "Mariner",
    "car_type": "SUV"
  },
  {
    "year": 2010,
    "manufacturer_name": "Mercedes-Benz",
    "model_name": "GLK-Class",
    "car_type": "SUV"
  },
  {
    "year": 2010,
    "manufacturer_name": "Mitsubishi",
    "model_name": "Galant",
    "car_type": "Sedan"
  },
  {
    "year": 2010,
    "manufacturer_name": "Mitsubishi",
    "model_name": "Eclipse",
    "car_type": "Coupe, Convertible"
  },
  {
    "year": 2010,
    "manufacturer_name": "Nissan",
    "model_name": "Armada",
    "car_type": "SUV"
  },
  {
    "year": 2010,
    "manufacturer_name": "Nissan",
    "model_name": "Sentra",
    "car_type": "Sedan"
  },
  {
    "year": 2010,
    "manufacturer_name": "Nissan",
    "model_name": "Pathfinder",
    "car_type": "SUV"
  },
  {
    "year": 2010,
    "manufacturer_name": "Porsche",
    "model_name": "911",
    "car_type": "Coupe, Convertible"
  },
  {
    "year": 2010,
    "manufacturer_name": "Nissan",
    "model_name": "Xterra",
    "car_type": "SUV"
  },
  {
    "year": 2010,
    "manufacturer_name": "Nissan",
    "model_name": "Rogue",
    "car_type": "SUV"
  },
  {
    "year": 2010,
    "manufacturer_name": "Saab",
    "model_name": "3-Sep",
    "car_type": "Wagon, Convertible, Sedan"
  },
  {
    "year": 2010,
    "manufacturer_name": "Nissan",
    "model_name": "Murano",
    "car_type": "SUV"
  },
  {
    "year": 2010,
    "manufacturer_name": "Nissan",
    "model_name": "GT-R",
    "car_type": "Coupe"
  },
  {
    "year": 2010,
    "manufacturer_name": "Nissan",
    "model_name": "Frontier Crew Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2010,
    "manufacturer_name": "Nissan",
    "model_name": "Titan King Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2010,
    "manufacturer_name": "Nissan",
    "model_name": "Versa",
    "car_type": "Sedan, Hatchback"
  },
  {
    "year": 2010,
    "manufacturer_name": "Pontiac",
    "model_name": "Vibe",
    "car_type": "Wagon"
  },
  {
    "year": 2010,
    "manufacturer_name": "Nissan",
    "model_name": "cube",
    "car_type": "Wagon"
  },
  {
    "year": 2010,
    "manufacturer_name": "Rolls-Royce",
    "model_name": "Phantom",
    "car_type": "Convertible, Sedan, Coupe"
  },
  {
    "year": 2010,
    "manufacturer_name": "Nissan",
    "model_name": "Frontier King Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2010,
    "manufacturer_name": "Nissan",
    "model_name": "Maxima",
    "car_type": "Sedan"
  },
  {
    "year": 2010,
    "manufacturer_name": "Pontiac",
    "model_name": "G6",
    "car_type": "Sedan"
  },
  {
    "year": 2010,
    "manufacturer_name": "Porsche",
    "model_name": "Boxster",
    "car_type": "Convertible"
  },
  {
    "year": 2010,
    "manufacturer_name": "Pontiac",
    "model_name": "G3",
    "car_type": "Hatchback"
  },
  {
    "year": 2010,
    "manufacturer_name": "Rolls-Royce",
    "model_name": "Ghost",
    "car_type": "Sedan"
  },
  {
    "year": 2010,
    "manufacturer_name": "Nissan",
    "model_name": "Titan Crew Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2010,
    "manufacturer_name": "Porsche",
    "model_name": "Cayenne",
    "car_type": "SUV"
  },
  {
    "year": 2010,
    "manufacturer_name": "Saturn",
    "model_name": "VUE",
    "car_type": "SUV"
  },
  {
    "year": 2010,
    "manufacturer_name": "Saab",
    "model_name": "5-Sep",
    "car_type": "Sedan"
  },
  {
    "year": 2010,
    "manufacturer_name": "Suzuki",
    "model_name": "Equator Extended Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2010,
    "manufacturer_name": "Subaru",
    "model_name": "Legacy",
    "car_type": "Sedan"
  },
  {
    "year": 2010,
    "manufacturer_name": "Suzuki",
    "model_name": "Equator Crew Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2010,
    "manufacturer_name": "Saturn",
    "model_name": "Outlook",
    "car_type": "SUV"
  },
  {
    "year": 2010,
    "manufacturer_name": "Porsche",
    "model_name": "Cayman",
    "car_type": "Coupe"
  },
  {
    "year": 2010,
    "manufacturer_name": "Porsche",
    "model_name": "Panamera",
    "car_type": "Sedan"
  },
  {
    "year": 2010,
    "manufacturer_name": "Subaru",
    "model_name": "Forester",
    "car_type": "SUV"
  },
  {
    "year": 2010,
    "manufacturer_name": "Scion",
    "model_name": "xB",
    "car_type": "Hatchback"
  },
  {
    "year": 2010,
    "manufacturer_name": "Scion",
    "model_name": "tC",
    "car_type": "Coupe"
  },
  {
    "year": 2010,
    "manufacturer_name": "smart",
    "model_name": "fortwo",
    "car_type": "Hatchback, Convertible"
  },
  {
    "year": 2010,
    "manufacturer_name": "Suzuki",
    "model_name": "Grand Vitara",
    "car_type": "SUV"
  },
  {
    "year": 2010,
    "manufacturer_name": "Subaru",
    "model_name": "Impreza",
    "car_type": "Sedan, Wagon"
  },
  {
    "year": 2010,
    "manufacturer_name": "Scion",
    "model_name": "xD",
    "car_type": "Hatchback"
  },
  {
    "year": 2010,
    "manufacturer_name": "Toyota",
    "model_name": "Avalon",
    "car_type": "Sedan"
  },
  {
    "year": 2010,
    "manufacturer_name": "Toyota",
    "model_name": "Sienna",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2010,
    "manufacturer_name": "Toyota",
    "model_name": "Land Cruiser",
    "car_type": "SUV"
  },
  {
    "year": 2010,
    "manufacturer_name": "Toyota",
    "model_name": "Highlander",
    "car_type": "SUV"
  },
  {
    "year": 2010,
    "manufacturer_name": "Volkswagen",
    "model_name": "Golf",
    "car_type": "Hatchback"
  },
  {
    "year": 2010,
    "manufacturer_name": "Toyota",
    "model_name": "RAV4",
    "car_type": "SUV"
  },
  {
    "year": 2010,
    "manufacturer_name": "Toyota",
    "model_name": "Corolla",
    "car_type": "Sedan"
  },
  {
    "year": 2010,
    "manufacturer_name": "Toyota",
    "model_name": "FJ Cruiser",
    "car_type": "SUV"
  },
  {
    "year": 2010,
    "manufacturer_name": "Suzuki",
    "model_name": "SX4",
    "car_type": "Sedan, Hatchback"
  },
  {
    "year": 2010,
    "manufacturer_name": "Subaru",
    "model_name": "Tribeca",
    "car_type": "SUV"
  },
  {
    "year": 2010,
    "manufacturer_name": "Toyota",
    "model_name": "Tundra CrewMax",
    "car_type": "Pickup"
  },
  {
    "year": 2010,
    "manufacturer_name": "Toyota",
    "model_name": "Matrix",
    "car_type": "Wagon"
  },
  {
    "year": 2010,
    "manufacturer_name": "Subaru",
    "model_name": "Outback",
    "car_type": "Wagon"
  },
  {
    "year": 2010,
    "manufacturer_name": "Toyota",
    "model_name": "Tacoma Double Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2010,
    "manufacturer_name": "Toyota",
    "model_name": "Camry",
    "car_type": "Sedan"
  },
  {
    "year": 2010,
    "manufacturer_name": "Toyota",
    "model_name": "4Runner",
    "car_type": "SUV"
  },
  {
    "year": 2010,
    "manufacturer_name": "Volkswagen",
    "model_name": "New Beetle",
    "car_type": "Hatchback, Convertible"
  },
  {
    "year": 2010,
    "manufacturer_name": "Toyota",
    "model_name": "Prius",
    "car_type": "Hatchback"
  },
  {
    "year": 2010,
    "manufacturer_name": "Volkswagen",
    "model_name": "Eos",
    "car_type": "Convertible"
  },
  {
    "year": 2010,
    "manufacturer_name": "Volkswagen",
    "model_name": "Passat",
    "car_type": "Sedan, Wagon"
  },
  {
    "year": 2010,
    "manufacturer_name": "Toyota",
    "model_name": "Tundra Double Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2010,
    "manufacturer_name": "Toyota",
    "model_name": "Tacoma Access Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2010,
    "manufacturer_name": "Toyota",
    "model_name": "Venza",
    "car_type": "Wagon"
  },
  {
    "year": 2010,
    "manufacturer_name": "Toyota",
    "model_name": "Sequoia",
    "car_type": "SUV"
  },
  {
    "year": 2010,
    "manufacturer_name": "Toyota",
    "model_name": "Yaris",
    "car_type": "Sedan, Hatchback"
  },
  {
    "year": 2010,
    "manufacturer_name": "Suzuki",
    "model_name": "Kizashi",
    "car_type": "Sedan"
  },
  {
    "year": 2010,
    "manufacturer_name": "Toyota",
    "model_name": "Tundra Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2010,
    "manufacturer_name": "Toyota",
    "model_name": "Tacoma Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2010,
    "manufacturer_name": "Volkswagen",
    "model_name": "CC",
    "car_type": "Sedan"
  },
  {
    "year": 2010,
    "manufacturer_name": "Volkswagen",
    "model_name": "Routan",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2010,
    "manufacturer_name": "Volvo",
    "model_name": "C30",
    "car_type": "Hatchback"
  },
  {
    "year": 2010,
    "manufacturer_name": "Volvo",
    "model_name": "C70",
    "car_type": "Convertible"
  },
  {
    "year": 2010,
    "manufacturer_name": "Volvo",
    "model_name": "S40",
    "car_type": "Sedan"
  },
  {
    "year": 2010,
    "manufacturer_name": "Volkswagen",
    "model_name": "GTI",
    "car_type": "Hatchback"
  },
  {
    "year": 2010,
    "manufacturer_name": "Volvo",
    "model_name": "XC60",
    "car_type": "SUV"
  },
  {
    "year": 2010,
    "manufacturer_name": "Volvo",
    "model_name": "S80",
    "car_type": "Sedan"
  },
  {
    "year": 2010,
    "manufacturer_name": "Volvo",
    "model_name": "XC70",
    "car_type": "Wagon"
  },
  {
    "year": 2010,
    "manufacturer_name": "Volkswagen",
    "model_name": "Jetta",
    "car_type": "Sedan, Wagon"
  },
  {
    "year": 2010,
    "manufacturer_name": "Volkswagen",
    "model_name": "Tiguan",
    "car_type": "SUV"
  },
  {
    "year": 2010,
    "manufacturer_name": "Volvo",
    "model_name": "V70",
    "car_type": "Wagon"
  },
  {
    "year": 2010,
    "manufacturer_name": "Volvo",
    "model_name": "V50",
    "car_type": "Wagon"
  },
  {
    "year": 2010,
    "manufacturer_name": "Volkswagen",
    "model_name": "Touareg",
    "car_type": "SUV"
  },
  {
    "year": 2009,
    "manufacturer_name": "Acura",
    "model_name": "RL",
    "car_type": "Sedan"
  },
  {
    "year": 2010,
    "manufacturer_name": "Volvo",
    "model_name": "XC90",
    "car_type": "SUV"
  },
  {
    "year": 2009,
    "manufacturer_name": "Audi",
    "model_name": "Q5",
    "car_type": "SUV"
  },
  {
    "year": 2009,
    "manufacturer_name": "Aston Martin",
    "model_name": "DB9",
    "car_type": "Coupe, Convertible"
  },
  {
    "year": 2009,
    "manufacturer_name": "Acura",
    "model_name": "TSX",
    "car_type": "Sedan"
  },
  {
    "year": 2009,
    "manufacturer_name": "Audi",
    "model_name": "A4",
    "car_type": "Convertible, Wagon, Sedan"
  },
  {
    "year": 2009,
    "manufacturer_name": "Acura",
    "model_name": "RDX",
    "car_type": "SUV"
  },
  {
    "year": 2009,
    "manufacturer_name": "Audi",
    "model_name": "A3",
    "car_type": "Wagon"
  },
  {
    "year": 2009,
    "manufacturer_name": "Acura",
    "model_name": "MDX",
    "car_type": "SUV"
  },
  {
    "year": 2009,
    "manufacturer_name": "Audi",
    "model_name": "R8",
    "car_type": "Coupe"
  },
  {
    "year": 2009,
    "manufacturer_name": "Aston Martin",
    "model_name": "Vantage",
    "car_type": "Convertible, Coupe"
  },
  {
    "year": 2009,
    "manufacturer_name": "Audi",
    "model_name": "S4",
    "car_type": "Convertible"
  },
  {
    "year": 2009,
    "manufacturer_name": "Acura",
    "model_name": "TL",
    "car_type": "Sedan"
  },
  {
    "year": 2009,
    "manufacturer_name": "Audi",
    "model_name": "S5",
    "car_type": "Coupe"
  },
  {
    "year": 2009,
    "manufacturer_name": "Audi",
    "model_name": "Q7",
    "car_type": "SUV"
  },
  {
    "year": 2009,
    "manufacturer_name": "Aston Martin",
    "model_name": "DBS",
    "car_type": "Coupe, Convertible"
  },
  {
    "year": 2009,
    "manufacturer_name": "Audi",
    "model_name": "A5",
    "car_type": "Coupe"
  },
  {
    "year": 2009,
    "manufacturer_name": "Audi",
    "model_name": "S6",
    "car_type": "Sedan"
  },
  {
    "year": 2009,
    "manufacturer_name": "Audi",
    "model_name": "A8",
    "car_type": "Sedan"
  },
  {
    "year": 2009,
    "manufacturer_name": "Audi",
    "model_name": "A6",
    "car_type": "Sedan, Wagon"
  },
  {
    "year": 2009,
    "manufacturer_name": "Audi",
    "model_name": "S8",
    "car_type": "Sedan"
  },
  {
    "year": 2009,
    "manufacturer_name": "Bentley",
    "model_name": "Arnage",
    "car_type": "Sedan"
  },
  {
    "year": 2009,
    "manufacturer_name": "Bentley",
    "model_name": "Brooklands",
    "car_type": "Coupe"
  },
  {
    "year": 2009,
    "manufacturer_name": "Audi",
    "model_name": "TT",
    "car_type": "Coupe, Convertible"
  },
  {
    "year": 2009,
    "manufacturer_name": "BMW",
    "model_name": "5 Series",
    "car_type": "Sedan, Wagon"
  },
  {
    "year": 2009,
    "manufacturer_name": "BMW",
    "model_name": "3 Series",
    "car_type": "Sedan, Convertible, Coupe, Wagon"
  },
  {
    "year": 2009,
    "manufacturer_name": "BMW",
    "model_name": "7 Series",
    "car_type": "Sedan"
  },
  {
    "year": 2009,
    "manufacturer_name": "BMW",
    "model_name": "M3",
    "car_type": "Coupe, Sedan, Convertible"
  },
  {
    "year": 2009,
    "manufacturer_name": "BMW",
    "model_name": "1 Series",
    "car_type": "Coupe, Convertible"
  },
  {
    "year": 2009,
    "manufacturer_name": "Bentley",
    "model_name": "Azure",
    "car_type": "Convertible"
  },
  {
    "year": 2009,
    "manufacturer_name": "BMW",
    "model_name": "M5",
    "car_type": "Sedan"
  },
  {
    "year": 2009,
    "manufacturer_name": "Bentley",
    "model_name": "Continental",
    "car_type": "Coupe, Sedan, Convertible"
  },
  {
    "year": 2009,
    "manufacturer_name": "BMW",
    "model_name": "6 Series",
    "car_type": "Convertible, Coupe"
  },
  {
    "year": 2009,
    "manufacturer_name": "BMW",
    "model_name": "M6",
    "car_type": "Coupe, Convertible"
  },
  {
    "year": 2009,
    "manufacturer_name": "Buick",
    "model_name": "LaCrosse",
    "car_type": "Sedan"
  },
  {
    "year": 2009,
    "manufacturer_name": "BMW",
    "model_name": "X6",
    "car_type": "SUV"
  },
  {
    "year": 2009,
    "manufacturer_name": "Cadillac",
    "model_name": "Escalade EXT",
    "car_type": "Pickup"
  },
  {
    "year": 2009,
    "manufacturer_name": "Chevrolet",
    "model_name": "Cobalt",
    "car_type": "Sedan, Coupe"
  },
  {
    "year": 2009,
    "manufacturer_name": "Cadillac",
    "model_name": "CTS",
    "car_type": "Sedan"
  },
  {
    "year": 2009,
    "manufacturer_name": "BMW",
    "model_name": "X3",
    "car_type": "SUV"
  },
  {
    "year": 2009,
    "manufacturer_name": "Cadillac",
    "model_name": "Escalade",
    "car_type": "SUV"
  },
  {
    "year": 2009,
    "manufacturer_name": "Cadillac",
    "model_name": "DTS",
    "car_type": "Sedan"
  },
  {
    "year": 2009,
    "manufacturer_name": "BMW",
    "model_name": "Z4",
    "car_type": "Convertible"
  },
  {
    "year": 2009,
    "manufacturer_name": "Buick",
    "model_name": "Enclave",
    "car_type": "SUV"
  },
  {
    "year": 2009,
    "manufacturer_name": "Chevrolet",
    "model_name": "Aveo",
    "car_type": "Sedan, Hatchback"
  },
  {
    "year": 2009,
    "manufacturer_name": "Chevrolet",
    "model_name": "Express 1500 Cargo",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2009,
    "manufacturer_name": "BMW",
    "model_name": "X5",
    "car_type": "SUV"
  },
  {
    "year": 2009,
    "manufacturer_name": "Cadillac",
    "model_name": "Escalade ESV",
    "car_type": "SUV"
  },
  {
    "year": 2009,
    "manufacturer_name": "Cadillac",
    "model_name": "XLR",
    "car_type": "Convertible"
  },
  {
    "year": 2009,
    "manufacturer_name": "Cadillac",
    "model_name": "SRX",
    "car_type": "SUV"
  },
  {
    "year": 2009,
    "manufacturer_name": "Buick",
    "model_name": "Lucerne",
    "car_type": "Sedan"
  },
  {
    "year": 2009,
    "manufacturer_name": "Chevrolet",
    "model_name": "Avalanche",
    "car_type": "SUV"
  },
  {
    "year": 2009,
    "manufacturer_name": "Chevrolet",
    "model_name": "Corvette",
    "car_type": "Coupe, Convertible"
  },
  {
    "year": 2009,
    "manufacturer_name": "Chevrolet",
    "model_name": "HHR",
    "car_type": "Wagon"
  },
  {
    "year": 2009,
    "manufacturer_name": "Chevrolet",
    "model_name": "Express 1500 Passenger",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2009,
    "manufacturer_name": "Chevrolet",
    "model_name": "Colorado Extended Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2009,
    "manufacturer_name": "Chevrolet",
    "model_name": "Colorado Crew Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2009,
    "manufacturer_name": "Chevrolet",
    "model_name": "Colorado Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2009,
    "manufacturer_name": "Cadillac",
    "model_name": "STS",
    "car_type": "Sedan"
  },
  {
    "year": 2009,
    "manufacturer_name": "Chevrolet",
    "model_name": "Express 2500 Passenger",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2009,
    "manufacturer_name": "Chevrolet",
    "model_name": "Equinox",
    "car_type": "SUV"
  },
  {
    "year": 2009,
    "manufacturer_name": "Chevrolet",
    "model_name": "Express 3500 Passenger",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2009,
    "manufacturer_name": "Chevrolet",
    "model_name": "Silverado 1500 Extended Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2009,
    "manufacturer_name": "Chevrolet",
    "model_name": "Silverado 1500 Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2009,
    "manufacturer_name": "Chevrolet",
    "model_name": "Silverado 3500 HD Extended Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2009,
    "manufacturer_name": "Chevrolet",
    "model_name": "Express 2500 Cargo",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2009,
    "manufacturer_name": "Chevrolet",
    "model_name": "Malibu",
    "car_type": "Sedan"
  },
  {
    "year": 2009,
    "manufacturer_name": "Chevrolet",
    "model_name": "TrailBlazer",
    "car_type": "SUV"
  },
  {
    "year": 2009,
    "manufacturer_name": "Chrysler",
    "model_name": "300",
    "car_type": "Sedan"
  },
  {
    "year": 2009,
    "manufacturer_name": "Chevrolet",
    "model_name": "Silverado 3500 HD Crew Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2009,
    "manufacturer_name": "Chevrolet",
    "model_name": "Suburban 1500",
    "car_type": "SUV"
  },
  {
    "year": 2009,
    "manufacturer_name": "Chevrolet",
    "model_name": "Impala",
    "car_type": "Sedan"
  },
  {
    "year": 2009,
    "manufacturer_name": "Chevrolet",
    "model_name": "Silverado 2500 HD Crew Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2009,
    "manufacturer_name": "Chevrolet",
    "model_name": "Silverado 1500 Crew Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2009,
    "manufacturer_name": "Chrysler",
    "model_name": "Sebring",
    "car_type": "Sedan, Convertible"
  },
  {
    "year": 2009,
    "manufacturer_name": "Chevrolet",
    "model_name": "Tahoe",
    "car_type": "SUV"
  },
  {
    "year": 2009,
    "manufacturer_name": "Chevrolet",
    "model_name": "Silverado 2500 HD Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2009,
    "manufacturer_name": "Chevrolet",
    "model_name": "Silverado 2500 HD Extended Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2009,
    "manufacturer_name": "Chevrolet",
    "model_name": "Silverado 3500 HD Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2009,
    "manufacturer_name": "Chrysler",
    "model_name": "PT Cruiser",
    "car_type": "Wagon"
  },
  {
    "year": 2009,
    "manufacturer_name": "Chevrolet",
    "model_name": "Express 3500 Cargo",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2009,
    "manufacturer_name": "Dodge",
    "model_name": "Dakota Crew Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2009,
    "manufacturer_name": "Chevrolet",
    "model_name": "Traverse",
    "car_type": "SUV"
  },
  {
    "year": 2009,
    "manufacturer_name": "Dodge",
    "model_name": "Journey",
    "car_type": "SUV"
  },
  {
    "year": 2009,
    "manufacturer_name": "Dodge",
    "model_name": "Grand Caravan Passenger",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2009,
    "manufacturer_name": "Dodge",
    "model_name": "Avenger",
    "car_type": "Sedan"
  },
  {
    "year": 2009,
    "manufacturer_name": "Dodge",
    "model_name": "Ram 2500 Mega Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2009,
    "manufacturer_name": "Dodge",
    "model_name": "Ram 3500 Quad Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2009,
    "manufacturer_name": "Dodge",
    "model_name": "Durango",
    "car_type": "SUV"
  },
  {
    "year": 2009,
    "manufacturer_name": "Dodge",
    "model_name": "Dakota Extended Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2009,
    "manufacturer_name": "Chrysler",
    "model_name": "Aspen",
    "car_type": "SUV"
  },
  {
    "year": 2009,
    "manufacturer_name": "Dodge",
    "model_name": "Charger",
    "car_type": "Sedan"
  },
  {
    "year": 2009,
    "manufacturer_name": "Chevrolet",
    "model_name": "Suburban 2500",
    "car_type": "SUV"
  },
  {
    "year": 2009,
    "manufacturer_name": "Dodge",
    "model_name": "Challenger",
    "car_type": "Coupe"
  },
  {
    "year": 2009,
    "manufacturer_name": "Dodge",
    "model_name": "Ram 1500 Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2009,
    "manufacturer_name": "Dodge",
    "model_name": "Ram 2500 Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2009,
    "manufacturer_name": "Ford",
    "model_name": "E150 Cargo",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2009,
    "manufacturer_name": "Ferrari",
    "model_name": "430 Scuderia",
    "car_type": "Coupe, Convertible"
  },
  {
    "year": 2009,
    "manufacturer_name": "Dodge",
    "model_name": "Grand Caravan Cargo",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2009,
    "manufacturer_name": "Ferrari",
    "model_name": "599 GTB Fiorano",
    "car_type": "Coupe"
  },
  {
    "year": 2009,
    "manufacturer_name": "Dodge",
    "model_name": "Ram 1500 Quad Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2009,
    "manufacturer_name": "Dodge",
    "model_name": "Ram 3500 Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2009,
    "manufacturer_name": "Chrysler",
    "model_name": "Town & Country",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2009,
    "manufacturer_name": "Dodge",
    "model_name": "Caliber",
    "car_type": "Wagon"
  },
  {
    "year": 2009,
    "manufacturer_name": "Ferrari",
    "model_name": "California",
    "car_type": "Convertible"
  },
  {
    "year": 2009,
    "manufacturer_name": "Dodge",
    "model_name": "Nitro",
    "car_type": "SUV"
  },
  {
    "year": 2009,
    "manufacturer_name": "Dodge",
    "model_name": "Ram 2500 Quad Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2009,
    "manufacturer_name": "Dodge",
    "model_name": "Ram 3500 Mega Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2009,
    "manufacturer_name": "Ford",
    "model_name": "Edge",
    "car_type": "SUV"
  },
  {
    "year": 2009,
    "manufacturer_name": "Dodge",
    "model_name": "Sprinter 2500 Cargo",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2009,
    "manufacturer_name": "Dodge",
    "model_name": "Ram 1500 Crew Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2009,
    "manufacturer_name": "Ford",
    "model_name": "Crown Victoria",
    "car_type": "Sedan"
  },
  {
    "year": 2009,
    "manufacturer_name": "Ford",
    "model_name": "E350 Super Duty Cargo",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2009,
    "manufacturer_name": "Ford",
    "model_name": "E150 Super Duty Passenger",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2009,
    "manufacturer_name": "Ford",
    "model_name": "Escape",
    "car_type": "SUV"
  },
  {
    "year": 2009,
    "manufacturer_name": "Dodge",
    "model_name": "Viper",
    "car_type": "Coupe, Convertible"
  },
  {
    "year": 2009,
    "manufacturer_name": "Ferrari",
    "model_name": "612 Scaglietti",
    "car_type": "Coupe"
  },
  {
    "year": 2009,
    "manufacturer_name": "Ford",
    "model_name": "E350 Super Duty Passenger",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2009,
    "manufacturer_name": "Ford",
    "model_name": "E250 Cargo",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2009,
    "manufacturer_name": "Ferrari",
    "model_name": "F430",
    "car_type": "Coupe, Convertible"
  },
  {
    "year": 2009,
    "manufacturer_name": "Ford",
    "model_name": "F150 Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2009,
    "manufacturer_name": "Ford",
    "model_name": "Expedition EL",
    "car_type": "SUV"
  },
  {
    "year": 2009,
    "manufacturer_name": "Ford",
    "model_name": "Expedition",
    "car_type": "SUV"
  },
  {
    "year": 2009,
    "manufacturer_name": "Ford",
    "model_name": "F250 Super Duty Crew Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2009,
    "manufacturer_name": "Ford",
    "model_name": "Explorer",
    "car_type": "SUV"
  },
  {
    "year": 2009,
    "manufacturer_name": "Ford",
    "model_name": "F250 Super Duty Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2009,
    "manufacturer_name": "Ford",
    "model_name": "Explorer Sport Trac",
    "car_type": "Pickup"
  },
  {
    "year": 2009,
    "manufacturer_name": "Ford",
    "model_name": "F250 Super Duty Super Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2009,
    "manufacturer_name": "Ford",
    "model_name": "Ranger Super Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2009,
    "manufacturer_name": "Ford",
    "model_name": "F150 SuperCrew Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2009,
    "manufacturer_name": "Ford",
    "model_name": "F350 Super Duty Crew Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2009,
    "manufacturer_name": "Ford",
    "model_name": "F150 Super Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2009,
    "manufacturer_name": "Ford",
    "model_name": "Ranger Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2009,
    "manufacturer_name": "Ford",
    "model_name": "F350 Super Duty Super Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2009,
    "manufacturer_name": "Ford",
    "model_name": "F450 Super Duty Crew Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2009,
    "manufacturer_name": "Ford",
    "model_name": "Flex",
    "car_type": "SUV"
  },
  {
    "year": 2009,
    "manufacturer_name": "Ford",
    "model_name": "Mustang",
    "car_type": "Convertible, Coupe"
  },
  {
    "year": 2009,
    "manufacturer_name": "Ford",
    "model_name": "F350 Super Duty Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2009,
    "manufacturer_name": "GMC",
    "model_name": "Acadia",
    "car_type": "SUV"
  },
  {
    "year": 2009,
    "manufacturer_name": "GMC",
    "model_name": "Canyon Crew Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2009,
    "manufacturer_name": "Ford",
    "model_name": "Fusion",
    "car_type": "Sedan"
  },
  {
    "year": 2009,
    "manufacturer_name": "Ford",
    "model_name": "Taurus",
    "car_type": "Sedan"
  },
  {
    "year": 2009,
    "manufacturer_name": "Ford",
    "model_name": "Focus",
    "car_type": "Coupe, Sedan"
  },
  {
    "year": 2009,
    "manufacturer_name": "GMC",
    "model_name": "Yukon",
    "car_type": "SUV"
  },
  {
    "year": 2009,
    "manufacturer_name": "GMC",
    "model_name": "Savana 2500 Passenger",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2009,
    "manufacturer_name": "Ford",
    "model_name": "Taurus X",
    "car_type": "SUV"
  },
  {
    "year": 2009,
    "manufacturer_name": "GMC",
    "model_name": "Savana 1500 Cargo",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2009,
    "manufacturer_name": "GMC",
    "model_name": "Envoy",
    "car_type": "SUV"
  },
  {
    "year": 2009,
    "manufacturer_name": "GMC",
    "model_name": "Canyon Extended Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2009,
    "manufacturer_name": "GMC",
    "model_name": "Canyon Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2009,
    "manufacturer_name": "GMC",
    "model_name": "Sierra 1500 Crew Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2009,
    "manufacturer_name": "GMC",
    "model_name": "Savana 3500 Cargo",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2009,
    "manufacturer_name": "GMC",
    "model_name": "Savana 1500 Passenger",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2009,
    "manufacturer_name": "GMC",
    "model_name": "Sierra 2500 HD Extended Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2009,
    "manufacturer_name": "GMC",
    "model_name": "Savana 3500 Passenger",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2009,
    "manufacturer_name": "GMC",
    "model_name": "Savana 2500 Cargo",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2009,
    "manufacturer_name": "GMC",
    "model_name": "Sierra 2500 HD Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2009,
    "manufacturer_name": "GMC",
    "model_name": "Sierra 1500 Extended Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2009,
    "manufacturer_name": "Honda",
    "model_name": "Fit",
    "car_type": "Hatchback"
  },
  {
    "year": 2009,
    "manufacturer_name": "Honda",
    "model_name": "CR-V",
    "car_type": "SUV"
  },
  {
    "year": 2009,
    "manufacturer_name": "INFINITI",
    "model_name": "G",
    "car_type": "Coupe, Sedan, Convertible"
  },
  {
    "year": 2009,
    "manufacturer_name": "Honda",
    "model_name": "Element",
    "car_type": "SUV"
  },
  {
    "year": 2009,
    "manufacturer_name": "GMC",
    "model_name": "Sierra 3500 HD Extended Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2009,
    "manufacturer_name": "Honda",
    "model_name": "S2000",
    "car_type": "Convertible"
  },
  {
    "year": 2009,
    "manufacturer_name": "GMC",
    "model_name": "Yukon XL 1500",
    "car_type": "SUV"
  },
  {
    "year": 2009,
    "manufacturer_name": "GMC",
    "model_name": "Sierra 3500 HD Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2009,
    "manufacturer_name": "GMC",
    "model_name": "Sierra 1500 Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2009,
    "manufacturer_name": "GMC",
    "model_name": "Sierra 2500 HD Crew Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2009,
    "manufacturer_name": "Honda",
    "model_name": "Accord",
    "car_type": "Sedan, Coupe"
  },
  {
    "year": 2009,
    "manufacturer_name": "GMC",
    "model_name": "Sierra 3500 HD Crew Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2009,
    "manufacturer_name": "Hyundai",
    "model_name": "Sonata",
    "car_type": "Sedan"
  },
  {
    "year": 2009,
    "manufacturer_name": "GMC",
    "model_name": "Yukon XL 2500",
    "car_type": "SUV"
  },
  {
    "year": 2009,
    "manufacturer_name": "Honda",
    "model_name": "Civic",
    "car_type": "Coupe, Sedan"
  },
  {
    "year": 2009,
    "manufacturer_name": "Hyundai",
    "model_name": "Accent",
    "car_type": "Hatchback, Sedan"
  },
  {
    "year": 2009,
    "manufacturer_name": "Honda",
    "model_name": "Odyssey",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2009,
    "manufacturer_name": "Honda",
    "model_name": "Ridgeline",
    "car_type": "Pickup"
  },
  {
    "year": 2009,
    "manufacturer_name": "HUMMER",
    "model_name": "H3T",
    "car_type": "Pickup"
  },
  {
    "year": 2009,
    "manufacturer_name": "Hyundai",
    "model_name": "Tucson",
    "car_type": "SUV"
  },
  {
    "year": 2009,
    "manufacturer_name": "Hyundai",
    "model_name": "Azera",
    "car_type": "Sedan"
  },
  {
    "year": 2009,
    "manufacturer_name": "Hyundai",
    "model_name": "Elantra",
    "car_type": "Sedan, Wagon"
  },
  {
    "year": 2009,
    "manufacturer_name": "HUMMER",
    "model_name": "H2",
    "car_type": "SUV"
  },
  {
    "year": 2009,
    "manufacturer_name": "Honda",
    "model_name": "Pilot",
    "car_type": "SUV"
  },
  {
    "year": 2009,
    "manufacturer_name": "INFINITI",
    "model_name": "QX",
    "car_type": "SUV"
  },
  {
    "year": 2009,
    "manufacturer_name": "INFINITI",
    "model_name": "M",
    "car_type": "Sedan"
  },
  {
    "year": 2009,
    "manufacturer_name": "Hyundai",
    "model_name": "Veracruz",
    "car_type": "SUV"
  },
  {
    "year": 2009,
    "manufacturer_name": "Hyundai",
    "model_name": "Santa Fe",
    "car_type": "SUV"
  },
  {
    "year": 2009,
    "manufacturer_name": "Jaguar",
    "model_name": "XK",
    "car_type": "Convertible, Coupe"
  },
  {
    "year": 2009,
    "manufacturer_name": "HUMMER",
    "model_name": "H3",
    "car_type": "SUV"
  },
  {
    "year": 2009,
    "manufacturer_name": "Kia",
    "model_name": "Amanti",
    "car_type": "Sedan"
  },
  {
    "year": 2009,
    "manufacturer_name": "Kia",
    "model_name": "Sedona",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2009,
    "manufacturer_name": "Jeep",
    "model_name": "Wrangler",
    "car_type": "SUV"
  },
  {
    "year": 2009,
    "manufacturer_name": "Lexus",
    "model_name": "LS",
    "car_type": "Sedan"
  },
  {
    "year": 2009,
    "manufacturer_name": "Jeep",
    "model_name": "Patriot",
    "car_type": "SUV"
  },
  {
    "year": 2009,
    "manufacturer_name": "Jeep",
    "model_name": "Liberty",
    "car_type": "SUV"
  },
  {
    "year": 2009,
    "manufacturer_name": "Kia",
    "model_name": "Rondo",
    "car_type": "Wagon"
  },
  {
    "year": 2009,
    "manufacturer_name": "INFINITI",
    "model_name": "FX",
    "car_type": "SUV"
  },
  {
    "year": 2009,
    "manufacturer_name": "Kia",
    "model_name": "Rio",
    "car_type": "Sedan, Hatchback"
  },
  {
    "year": 2009,
    "manufacturer_name": "Jeep",
    "model_name": "Commander",
    "car_type": "SUV"
  },
  {
    "year": 2009,
    "manufacturer_name": "Lexus",
    "model_name": "IS",
    "car_type": "Sedan"
  },
  {
    "year": 2009,
    "manufacturer_name": "Land Rover",
    "model_name": "Range Rover",
    "car_type": "SUV"
  },
  {
    "year": 2009,
    "manufacturer_name": "Hyundai",
    "model_name": "Genesis",
    "car_type": "Sedan"
  },
  {
    "year": 2009,
    "manufacturer_name": "Jaguar",
    "model_name": "XJ",
    "car_type": "Sedan"
  },
  {
    "year": 2009,
    "manufacturer_name": "Jeep",
    "model_name": "Compass",
    "car_type": "SUV"
  },
  {
    "year": 2009,
    "manufacturer_name": "Kia",
    "model_name": "Sportage",
    "car_type": "SUV"
  },
  {
    "year": 2009,
    "manufacturer_name": "INFINITI",
    "model_name": "EX",
    "car_type": "SUV"
  },
  {
    "year": 2009,
    "manufacturer_name": "Kia",
    "model_name": "Borrego",
    "car_type": "SUV"
  },
  {
    "year": 2009,
    "manufacturer_name": "Kia",
    "model_name": "Optima",
    "car_type": "Sedan"
  },
  {
    "year": 2009,
    "manufacturer_name": "Jaguar",
    "model_name": "XF",
    "car_type": "Sedan"
  },
  {
    "year": 2009,
    "manufacturer_name": "Land Rover",
    "model_name": "Range Rover Sport",
    "car_type": "SUV"
  },
  {
    "year": 2009,
    "manufacturer_name": "Land Rover",
    "model_name": "LR2",
    "car_type": "SUV"
  },
  {
    "year": 2009,
    "manufacturer_name": "Jeep",
    "model_name": "Grand Cherokee",
    "car_type": "SUV"
  },
  {
    "year": 2009,
    "manufacturer_name": "Lamborghini",
    "model_name": "Gallardo",
    "car_type": "Convertible, Coupe"
  },
  {
    "year": 2009,
    "manufacturer_name": "Lamborghini",
    "model_name": "Murcielago",
    "car_type": "Convertible, Coupe"
  },
  {
    "year": 2009,
    "manufacturer_name": "Lexus",
    "model_name": "ES",
    "car_type": "Sedan"
  },
  {
    "year": 2009,
    "manufacturer_name": "Lexus",
    "model_name": "IS F",
    "car_type": "Sedan"
  },
  {
    "year": 2009,
    "manufacturer_name": "Kia",
    "model_name": "Spectra",
    "car_type": "Sedan, Hatchback"
  },
  {
    "year": 2009,
    "manufacturer_name": "Lexus",
    "model_name": "GX",
    "car_type": "SUV"
  },
  {
    "year": 2009,
    "manufacturer_name": "Land Rover",
    "model_name": "LR3",
    "car_type": "SUV"
  },
  {
    "year": 2009,
    "manufacturer_name": "Kia",
    "model_name": "Sorento",
    "car_type": "SUV"
  },
  {
    "year": 2009,
    "manufacturer_name": "Lexus",
    "model_name": "GS",
    "car_type": "Sedan"
  },
  {
    "year": 2009,
    "manufacturer_name": "Lincoln",
    "model_name": "MKX",
    "car_type": "SUV"
  },
  {
    "year": 2009,
    "manufacturer_name": "Lexus",
    "model_name": "SC",
    "car_type": "Convertible"
  },
  {
    "year": 2009,
    "manufacturer_name": "Lincoln",
    "model_name": "MKS",
    "car_type": "Sedan"
  },
  {
    "year": 2009,
    "manufacturer_name": "Lincoln",
    "model_name": "MKZ",
    "car_type": "Sedan"
  },
  {
    "year": 2009,
    "manufacturer_name": "Lincoln",
    "model_name": "Navigator L",
    "car_type": "SUV"
  },
  {
    "year": 2009,
    "manufacturer_name": "MAZDA",
    "model_name": "MX-5 Miata",
    "car_type": "Convertible"
  },
  {
    "year": 2009,
    "manufacturer_name": "MAZDA",
    "model_name": "CX-9",
    "car_type": "SUV"
  },
  {
    "year": 2009,
    "manufacturer_name": "MAZDA",
    "model_name": "CX-7",
    "car_type": "SUV"
  },
  {
    "year": 2009,
    "manufacturer_name": "Lotus",
    "model_name": "Elise",
    "car_type": "Coupe"
  },
  {
    "year": 2009,
    "manufacturer_name": "Maybach",
    "model_name": "57",
    "car_type": "Sedan"
  },
  {
    "year": 2009,
    "manufacturer_name": "Lincoln",
    "model_name": "Town Car",
    "car_type": "Sedan"
  },
  {
    "year": 2009,
    "manufacturer_name": "Lexus",
    "model_name": "LX",
    "car_type": "SUV"
  },
  {
    "year": 2009,
    "manufacturer_name": "Lexus",
    "model_name": "RX",
    "car_type": "SUV"
  },
  {
    "year": 2009,
    "manufacturer_name": "Lotus",
    "model_name": "Exige",
    "car_type": "Coupe"
  },
  {
    "year": 2009,
    "manufacturer_name": "MAZDA",
    "model_name": "MAZDA3",
    "car_type": "Sedan, Hatchback"
  },
  {
    "year": 2009,
    "manufacturer_name": "Maserati",
    "model_name": "GranTurismo",
    "car_type": "Coupe"
  },
  {
    "year": 2009,
    "manufacturer_name": "Maybach",
    "model_name": "62",
    "car_type": "Sedan"
  },
  {
    "year": 2009,
    "manufacturer_name": "Maserati",
    "model_name": "Quattroporte",
    "car_type": "Sedan"
  },
  {
    "year": 2009,
    "manufacturer_name": "Lincoln",
    "model_name": "Navigator",
    "car_type": "SUV"
  },
  {
    "year": 2009,
    "manufacturer_name": "MAZDA",
    "model_name": "B-Series Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2009,
    "manufacturer_name": "MAZDA",
    "model_name": "RX-8",
    "car_type": "Coupe"
  },
  {
    "year": 2009,
    "manufacturer_name": "Mercedes-Benz",
    "model_name": "CLK-Class",
    "car_type": "Coupe, Convertible"
  },
  {
    "year": 2009,
    "manufacturer_name": "MAZDA",
    "model_name": "Tribute",
    "car_type": "SUV"
  },
  {
    "year": 2009,
    "manufacturer_name": "MAZDA",
    "model_name": "B-Series Extended Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2009,
    "manufacturer_name": "MAZDA",
    "model_name": "MAZDA6",
    "car_type": "Sedan"
  },
  {
    "year": 2009,
    "manufacturer_name": "Mercedes-Benz",
    "model_name": "CLS-Class",
    "car_type": "Coupe"
  },
  {
    "year": 2009,
    "manufacturer_name": "MAZDA",
    "model_name": "MAZDA5",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2009,
    "manufacturer_name": "Mercedes-Benz",
    "model_name": "CL-Class",
    "car_type": "Coupe"
  },
  {
    "year": 2009,
    "manufacturer_name": "Mercedes-Benz",
    "model_name": "E-Class",
    "car_type": "Sedan, Wagon"
  },
  {
    "year": 2009,
    "manufacturer_name": "Mercedes-Benz",
    "model_name": "GL-Class",
    "car_type": "SUV"
  },
  {
    "year": 2009,
    "manufacturer_name": "Mercedes-Benz",
    "model_name": "S-Class",
    "car_type": "Sedan"
  },
  {
    "year": 2009,
    "manufacturer_name": "Mercedes-Benz",
    "model_name": "R-Class",
    "car_type": "Wagon"
  },
  {
    "year": 2009,
    "manufacturer_name": "Mercedes-Benz",
    "model_name": "SLK-Class",
    "car_type": "Convertible"
  },
  {
    "year": 2009,
    "manufacturer_name": "Mercury",
    "model_name": "Grand Marquis",
    "car_type": "Sedan"
  },
  {
    "year": 2009,
    "manufacturer_name": "Nissan",
    "model_name": "350Z",
    "car_type": "Convertible"
  },
  {
    "year": 2009,
    "manufacturer_name": "Mitsubishi",
    "model_name": "Galant",
    "car_type": "Sedan"
  },
  {
    "year": 2009,
    "manufacturer_name": "Mercedes-Benz",
    "model_name": "C-Class",
    "car_type": "Sedan"
  },
  {
    "year": 2009,
    "manufacturer_name": "Mercury",
    "model_name": "Sable",
    "car_type": "Sedan"
  },
  {
    "year": 2009,
    "manufacturer_name": "Mercedes-Benz",
    "model_name": "M-Class",
    "car_type": "SUV"
  },
  {
    "year": 2009,
    "manufacturer_name": "Mercedes-Benz",
    "model_name": "SLR McLaren",
    "car_type": "Convertible"
  },
  {
    "year": 2009,
    "manufacturer_name": "Mitsubishi",
    "model_name": "Outlander",
    "car_type": "SUV"
  },
  {
    "year": 2009,
    "manufacturer_name": "Mercury",
    "model_name": "Mariner",
    "car_type": "SUV"
  },
  {
    "year": 2009,
    "manufacturer_name": "MINI",
    "model_name": "Clubman",
    "car_type": "Hatchback"
  },
  {
    "year": 2009,
    "manufacturer_name": "MINI",
    "model_name": "Convertible",
    "car_type": "Convertible"
  },
  {
    "year": 2009,
    "manufacturer_name": "Mercedes-Benz",
    "model_name": "G-Class",
    "car_type": "SUV"
  },
  {
    "year": 2009,
    "manufacturer_name": "Mercedes-Benz",
    "model_name": "SL-Class",
    "car_type": "Convertible"
  },
  {
    "year": 2009,
    "manufacturer_name": "Nissan",
    "model_name": "370Z",
    "car_type": "Coupe"
  },
  {
    "year": 2009,
    "manufacturer_name": "Mitsubishi",
    "model_name": "Lancer",
    "car_type": "Sedan"
  },
  {
    "year": 2009,
    "manufacturer_name": "Mercury",
    "model_name": "Mountaineer",
    "car_type": "SUV"
  },
  {
    "year": 2009,
    "manufacturer_name": "Mercury",
    "model_name": "Milan",
    "car_type": "Sedan"
  },
  {
    "year": 2009,
    "manufacturer_name": "Nissan",
    "model_name": "GT-R",
    "car_type": "Coupe"
  },
  {
    "year": 2009,
    "manufacturer_name": "Mitsubishi",
    "model_name": "Raider Double Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2009,
    "manufacturer_name": "Nissan",
    "model_name": "Altima",
    "car_type": "Sedan, Coupe"
  },
  {
    "year": 2009,
    "manufacturer_name": "MINI",
    "model_name": "Hardtop",
    "car_type": "Hatchback"
  },
  {
    "year": 2009,
    "manufacturer_name": "Nissan",
    "model_name": "cube",
    "car_type": "Wagon"
  },
  {
    "year": 2009,
    "manufacturer_name": "Mitsubishi",
    "model_name": "Eclipse",
    "car_type": "Coupe, Convertible"
  },
  {
    "year": 2009,
    "manufacturer_name": "Nissan",
    "model_name": "Rogue",
    "car_type": "SUV"
  },
  {
    "year": 2009,
    "manufacturer_name": "Nissan",
    "model_name": "Quest",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2009,
    "manufacturer_name": "Nissan",
    "model_name": "Frontier Crew Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2009,
    "manufacturer_name": "Nissan",
    "model_name": "Frontier King Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2009,
    "manufacturer_name": "Nissan",
    "model_name": "Versa",
    "car_type": "Sedan, Hatchback"
  },
  {
    "year": 2009,
    "manufacturer_name": "Nissan",
    "model_name": "Xterra",
    "car_type": "SUV"
  },
  {
    "year": 2009,
    "manufacturer_name": "Mitsubishi",
    "model_name": "Raider Extended Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2009,
    "manufacturer_name": "Nissan",
    "model_name": "Titan King Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2009,
    "manufacturer_name": "Nissan",
    "model_name": "Pathfinder",
    "car_type": "SUV"
  },
  {
    "year": 2009,
    "manufacturer_name": "Pontiac",
    "model_name": "G6 (2009.5)",
    "car_type": "Coupe, Sedan, Convertible"
  },
  {
    "year": 2009,
    "manufacturer_name": "Nissan",
    "model_name": "Armada",
    "car_type": "SUV"
  },
  {
    "year": 2009,
    "manufacturer_name": "Saturn",
    "model_name": "VUE",
    "car_type": "SUV"
  },
  {
    "year": 2009,
    "manufacturer_name": "Pontiac",
    "model_name": "Solstice",
    "car_type": "Convertible, Coupe"
  },
  {
    "year": 2009,
    "manufacturer_name": "Saturn",
    "model_name": "Outlook",
    "car_type": "SUV"
  },
  {
    "year": 2009,
    "manufacturer_name": "Nissan",
    "model_name": "Maxima",
    "car_type": "Sedan"
  },
  {
    "year": 2009,
    "manufacturer_name": "Nissan",
    "model_name": "Murano",
    "car_type": "SUV"
  },
  {
    "year": 2009,
    "manufacturer_name": "Nissan",
    "model_name": "Titan Crew Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2009,
    "manufacturer_name": "Pontiac",
    "model_name": "G8",
    "car_type": "Sedan"
  },
  {
    "year": 2009,
    "manufacturer_name": "Pontiac",
    "model_name": "Vibe",
    "car_type": "Wagon"
  },
  {
    "year": 2009,
    "manufacturer_name": "Scion",
    "model_name": "xD",
    "car_type": "Hatchback"
  },
  {
    "year": 2009,
    "manufacturer_name": "Pontiac",
    "model_name": "G6",
    "car_type": "Sedan, Coupe, Convertible"
  },
  {
    "year": 2009,
    "manufacturer_name": "Saab",
    "model_name": "3-Sep",
    "car_type": "Sedan, Convertible, Wagon"
  },
  {
    "year": 2009,
    "manufacturer_name": "Saturn",
    "model_name": "Aura",
    "car_type": "Sedan"
  },
  {
    "year": 2009,
    "manufacturer_name": "Porsche",
    "model_name": "Boxster",
    "car_type": "Convertible"
  },
  {
    "year": 2009,
    "manufacturer_name": "Saab",
    "model_name": "9-7X",
    "car_type": "SUV"
  },
  {
    "year": 2009,
    "manufacturer_name": "Subaru",
    "model_name": "Tribeca",
    "car_type": "SUV"
  },
  {
    "year": 2009,
    "manufacturer_name": "Pontiac",
    "model_name": "Torrent",
    "car_type": "SUV"
  },
  {
    "year": 2009,
    "manufacturer_name": "Subaru",
    "model_name": "Forester",
    "car_type": "SUV"
  },
  {
    "year": 2009,
    "manufacturer_name": "Rolls-Royce",
    "model_name": "Phantom",
    "car_type": "Convertible, Coupe, Sedan"
  },
  {
    "year": 2009,
    "manufacturer_name": "Pontiac",
    "model_name": "G5",
    "car_type": "Coupe"
  },
  {
    "year": 2009,
    "manufacturer_name": "Porsche",
    "model_name": "Cayenne",
    "car_type": "SUV"
  },
  {
    "year": 2009,
    "manufacturer_name": "Porsche",
    "model_name": "911",
    "car_type": "Coupe, Convertible"
  },
  {
    "year": 2009,
    "manufacturer_name": "Nissan",
    "model_name": "Sentra",
    "car_type": "Sedan"
  },
  {
    "year": 2009,
    "manufacturer_name": "Saab",
    "model_name": "5-Sep",
    "car_type": "Sedan, Wagon"
  },
  {
    "year": 2009,
    "manufacturer_name": "smart",
    "model_name": "fortwo",
    "car_type": "Hatchback, Convertible"
  },
  {
    "year": 2009,
    "manufacturer_name": "Scion",
    "model_name": "xB",
    "car_type": "Hatchback"
  },
  {
    "year": 2009,
    "manufacturer_name": "Pontiac",
    "model_name": "G3",
    "car_type": "Hatchback"
  },
  {
    "year": 2009,
    "manufacturer_name": "Porsche",
    "model_name": "Cayman",
    "car_type": "Coupe"
  },
  {
    "year": 2009,
    "manufacturer_name": "Scion",
    "model_name": "tC",
    "car_type": "Coupe"
  },
  {
    "year": 2009,
    "manufacturer_name": "Saturn",
    "model_name": "SKY",
    "car_type": "Convertible"
  },
  {
    "year": 2009,
    "manufacturer_name": "Subaru",
    "model_name": "Legacy",
    "car_type": "Sedan"
  },
  {
    "year": 2009,
    "manufacturer_name": "Suzuki",
    "model_name": "Equator Crew Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2009,
    "manufacturer_name": "Subaru",
    "model_name": "Impreza",
    "car_type": "Sedan, Wagon"
  },
  {
    "year": 2009,
    "manufacturer_name": "Subaru",
    "model_name": "Outback",
    "car_type": "Wagon"
  },
  {
    "year": 2009,
    "manufacturer_name": "Suzuki",
    "model_name": "XL7",
    "car_type": "SUV"
  },
  {
    "year": 2009,
    "manufacturer_name": "Suzuki",
    "model_name": "Grand Vitara",
    "car_type": "SUV"
  },
  {
    "year": 2009,
    "manufacturer_name": "Toyota",
    "model_name": "4Runner",
    "car_type": "SUV"
  },
  {
    "year": 2009,
    "manufacturer_name": "Toyota",
    "model_name": "Sequoia",
    "car_type": "SUV"
  },
  {
    "year": 2009,
    "manufacturer_name": "Toyota",
    "model_name": "FJ Cruiser",
    "car_type": "SUV"
  },
  {
    "year": 2009,
    "manufacturer_name": "Toyota",
    "model_name": "Land Cruiser",
    "car_type": "SUV"
  },
  {
    "year": 2009,
    "manufacturer_name": "Suzuki",
    "model_name": "SX4",
    "car_type": "Sedan, Hatchback"
  },
  {
    "year": 2009,
    "manufacturer_name": "Toyota",
    "model_name": "RAV4",
    "car_type": "SUV"
  },
  {
    "year": 2009,
    "manufacturer_name": "Suzuki",
    "model_name": "Equator Extended Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2009,
    "manufacturer_name": "Toyota",
    "model_name": "Prius",
    "car_type": "Hatchback"
  },
  {
    "year": 2009,
    "manufacturer_name": "Toyota",
    "model_name": "Camry",
    "car_type": "Sedan"
  },
  {
    "year": 2009,
    "manufacturer_name": "Toyota",
    "model_name": "Corolla",
    "car_type": "Sedan"
  },
  {
    "year": 2009,
    "manufacturer_name": "Toyota",
    "model_name": "Highlander",
    "car_type": "SUV"
  },
  {
    "year": 2009,
    "manufacturer_name": "Toyota",
    "model_name": "Avalon",
    "car_type": "Sedan"
  },
  {
    "year": 2009,
    "manufacturer_name": "Toyota",
    "model_name": "Tacoma Access Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2009,
    "manufacturer_name": "Toyota",
    "model_name": "Tacoma Double Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2009,
    "manufacturer_name": "Volkswagen",
    "model_name": "New Beetle",
    "car_type": "Hatchback, Convertible"
  },
  {
    "year": 2009,
    "manufacturer_name": "Toyota",
    "model_name": "Sienna",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2009,
    "manufacturer_name": "Toyota",
    "model_name": "Matrix",
    "car_type": "Wagon"
  },
  {
    "year": 2009,
    "manufacturer_name": "Toyota",
    "model_name": "Tundra CrewMax",
    "car_type": "Pickup"
  },
  {
    "year": 2009,
    "manufacturer_name": "Toyota",
    "model_name": "Venza",
    "car_type": "Wagon"
  },
  {
    "year": 2009,
    "manufacturer_name": "Volkswagen",
    "model_name": "CC",
    "car_type": "Sedan"
  },
  {
    "year": 2009,
    "manufacturer_name": "Toyota",
    "model_name": "Tacoma Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2009,
    "manufacturer_name": "Volkswagen",
    "model_name": "Jetta",
    "car_type": "Sedan, Wagon"
  },
  {
    "year": 2009,
    "manufacturer_name": "Toyota",
    "model_name": "Tundra Double Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2009,
    "manufacturer_name": "Toyota",
    "model_name": "Yaris",
    "car_type": "Hatchback, Sedan"
  },
  {
    "year": 2009,
    "manufacturer_name": "Volkswagen",
    "model_name": "GTI",
    "car_type": "Hatchback"
  },
  {
    "year": 2009,
    "manufacturer_name": "Volvo",
    "model_name": "XC90",
    "car_type": "SUV"
  },
  {
    "year": 2009,
    "manufacturer_name": "Volkswagen",
    "model_name": "Rabbit",
    "car_type": "Hatchback"
  },
  {
    "year": 2009,
    "manufacturer_name": "Volkswagen",
    "model_name": "Passat",
    "car_type": "Wagon, Sedan"
  },
  {
    "year": 2009,
    "manufacturer_name": "Volkswagen",
    "model_name": "Touareg 2",
    "car_type": "SUV"
  },
  {
    "year": 2009,
    "manufacturer_name": "Toyota",
    "model_name": "Tundra Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2009,
    "manufacturer_name": "Volkswagen",
    "model_name": "GLI",
    "car_type": "Sedan"
  },
  {
    "year": 2009,
    "manufacturer_name": "Volvo",
    "model_name": "S40",
    "car_type": "Sedan"
  },
  {
    "year": 2009,
    "manufacturer_name": "Volkswagen",
    "model_name": "Routan",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2009,
    "manufacturer_name": "Volkswagen",
    "model_name": "Eos",
    "car_type": "Convertible"
  },
  {
    "year": 2008,
    "manufacturer_name": "Acura",
    "model_name": "MDX",
    "car_type": "SUV"
  },
  {
    "year": 2009,
    "manufacturer_name": "Volvo",
    "model_name": "XC70",
    "car_type": "Wagon"
  },
  {
    "year": 2009,
    "manufacturer_name": "Volkswagen",
    "model_name": "Tiguan",
    "car_type": "SUV"
  },
  {
    "year": 2009,
    "manufacturer_name": "Volvo",
    "model_name": "S80",
    "car_type": "Sedan"
  },
  {
    "year": 2009,
    "manufacturer_name": "Volvo",
    "model_name": "C30",
    "car_type": "Hatchback"
  },
  {
    "year": 2009,
    "manufacturer_name": "Volvo",
    "model_name": "V50",
    "car_type": "Wagon"
  },
  {
    "year": 2009,
    "manufacturer_name": "Volvo",
    "model_name": "C70",
    "car_type": "Convertible"
  },
  {
    "year": 2009,
    "manufacturer_name": "Volvo",
    "model_name": "S60",
    "car_type": "Sedan"
  },
  {
    "year": 2008,
    "manufacturer_name": "Acura",
    "model_name": "TSX",
    "car_type": "Sedan"
  },
  {
    "year": 2008,
    "manufacturer_name": "Acura",
    "model_name": "RDX",
    "car_type": "SUV"
  },
  {
    "year": 2008,
    "manufacturer_name": "Audi",
    "model_name": "R8",
    "car_type": "Coupe"
  },
  {
    "year": 2008,
    "manufacturer_name": "Aston Martin",
    "model_name": "DB9",
    "car_type": "Convertible, Coupe"
  },
  {
    "year": 2008,
    "manufacturer_name": "Audi",
    "model_name": "Q7",
    "car_type": "SUV"
  },
  {
    "year": 2008,
    "manufacturer_name": "Audi",
    "model_name": "A5",
    "car_type": "Coupe"
  },
  {
    "year": 2008,
    "manufacturer_name": "Audi",
    "model_name": "A4",
    "car_type": "Convertible, Sedan, Wagon"
  },
  {
    "year": 2008,
    "manufacturer_name": "Acura",
    "model_name": "TL",
    "car_type": "Sedan"
  },
  {
    "year": 2008,
    "manufacturer_name": "Aston Martin",
    "model_name": "Vantage",
    "car_type": "Coupe, Convertible"
  },
  {
    "year": 2009,
    "manufacturer_name": "Volvo",
    "model_name": "V70",
    "car_type": "Wagon"
  },
  {
    "year": 2008,
    "manufacturer_name": "Acura",
    "model_name": "RL",
    "car_type": "Sedan"
  },
  {
    "year": 2008,
    "manufacturer_name": "Audi",
    "model_name": "RS 4",
    "car_type": "Sedan, Convertible"
  },
  {
    "year": 2008,
    "manufacturer_name": "Audi",
    "model_name": "A6",
    "car_type": "Sedan, Wagon"
  },
  {
    "year": 2008,
    "manufacturer_name": "Audi",
    "model_name": "TT",
    "car_type": "Convertible, Coupe"
  },
  {
    "year": 2008,
    "manufacturer_name": "Audi",
    "model_name": "S8",
    "car_type": "Sedan"
  },
  {
    "year": 2008,
    "manufacturer_name": "Aston Martin",
    "model_name": "DBS",
    "car_type": "Coupe"
  },
  {
    "year": 2008,
    "manufacturer_name": "Audi",
    "model_name": "S4",
    "car_type": "Sedan, Wagon, Convertible"
  },
  {
    "year": 2008,
    "manufacturer_name": "Audi",
    "model_name": "A3",
    "car_type": "Wagon"
  },
  {
    "year": 2008,
    "manufacturer_name": "Audi",
    "model_name": "S6",
    "car_type": "Sedan"
  },
  {
    "year": 2008,
    "manufacturer_name": "Audi",
    "model_name": "A8",
    "car_type": "Sedan"
  },
  {
    "year": 2008,
    "manufacturer_name": "BMW",
    "model_name": "1 Series",
    "car_type": "Coupe, Convertible"
  },
  {
    "year": 2008,
    "manufacturer_name": "BMW",
    "model_name": "X6",
    "car_type": "SUV"
  },
  {
    "year": 2008,
    "manufacturer_name": "BMW",
    "model_name": "3 Series",
    "car_type": "Sedan, Coupe, Wagon, Convertible"
  },
  {
    "year": 2008,
    "manufacturer_name": "Bentley",
    "model_name": "Continental",
    "car_type": "Sedan, Coupe, Convertible"
  },
  {
    "year": 2008,
    "manufacturer_name": "Cadillac",
    "model_name": "Escalade EXT",
    "car_type": "Pickup"
  },
  {
    "year": 2008,
    "manufacturer_name": "BMW",
    "model_name": "5 Series",
    "car_type": "Sedan, Wagon"
  },
  {
    "year": 2008,
    "manufacturer_name": "Audi",
    "model_name": "S5",
    "car_type": "Coupe"
  },
  {
    "year": 2008,
    "manufacturer_name": "Bentley",
    "model_name": "Arnage",
    "car_type": "Sedan"
  },
  {
    "year": 2008,
    "manufacturer_name": "BMW",
    "model_name": "Z4",
    "car_type": "Convertible, Coupe"
  },
  {
    "year": 2008,
    "manufacturer_name": "BMW",
    "model_name": "M6",
    "car_type": "Coupe, Convertible"
  },
  {
    "year": 2008,
    "manufacturer_name": "Cadillac",
    "model_name": "SRX",
    "car_type": "SUV"
  },
  {
    "year": 2008,
    "manufacturer_name": "BMW",
    "model_name": "7 Series",
    "car_type": "Sedan"
  },
  {
    "year": 2008,
    "manufacturer_name": "BMW",
    "model_name": "Z4 M",
    "car_type": "Coupe, Convertible"
  },
  {
    "year": 2008,
    "manufacturer_name": "BMW",
    "model_name": "6 Series",
    "car_type": "Convertible, Coupe"
  },
  {
    "year": 2008,
    "manufacturer_name": "Buick",
    "model_name": "LaCrosse",
    "car_type": "Sedan"
  },
  {
    "year": 2008,
    "manufacturer_name": "Chevrolet",
    "model_name": "Corvette",
    "car_type": "Convertible, Coupe"
  },
  {
    "year": 2008,
    "manufacturer_name": "BMW",
    "model_name": "X3",
    "car_type": "SUV"
  },
  {
    "year": 2008,
    "manufacturer_name": "BMW",
    "model_name": "M3",
    "car_type": "Coupe, Sedan, Convertible"
  },
  {
    "year": 2008,
    "manufacturer_name": "Cadillac",
    "model_name": "Escalade",
    "car_type": "SUV"
  },
  {
    "year": 2008,
    "manufacturer_name": "Buick",
    "model_name": "Lucerne",
    "car_type": "Sedan"
  },
  {
    "year": 2008,
    "manufacturer_name": "Buick",
    "model_name": "Enclave",
    "car_type": "SUV"
  },
  {
    "year": 2008,
    "manufacturer_name": "Chevrolet",
    "model_name": "Avalanche",
    "car_type": "SUV"
  },
  {
    "year": 2008,
    "manufacturer_name": "BMW",
    "model_name": "M5",
    "car_type": "Sedan"
  },
  {
    "year": 2008,
    "manufacturer_name": "Bentley",
    "model_name": "Azure",
    "car_type": "Convertible"
  },
  {
    "year": 2008,
    "manufacturer_name": "Chevrolet",
    "model_name": "Aveo",
    "car_type": "Hatchback, Sedan"
  },
  {
    "year": 2008,
    "manufacturer_name": "BMW",
    "model_name": "X5",
    "car_type": "SUV"
  },
  {
    "year": 2008,
    "manufacturer_name": "Cadillac",
    "model_name": "XLR",
    "car_type": "Convertible"
  },
  {
    "year": 2008,
    "manufacturer_name": "Cadillac",
    "model_name": "DTS",
    "car_type": "Sedan"
  },
  {
    "year": 2008,
    "manufacturer_name": "BMW",
    "model_name": "Alpina B7",
    "car_type": "Sedan"
  },
  {
    "year": 2008,
    "manufacturer_name": "Cadillac",
    "model_name": "CTS",
    "car_type": "Sedan"
  },
  {
    "year": 2008,
    "manufacturer_name": "Cadillac",
    "model_name": "Escalade ESV",
    "car_type": "SUV"
  },
  {
    "year": 2008,
    "manufacturer_name": "Chevrolet",
    "model_name": "Cobalt",
    "car_type": "Sedan, Coupe"
  },
  {
    "year": 2008,
    "manufacturer_name": "Chevrolet",
    "model_name": "Colorado Extended Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2008,
    "manufacturer_name": "Cadillac",
    "model_name": "STS",
    "car_type": "Sedan"
  },
  {
    "year": 2008,
    "manufacturer_name": "Chevrolet",
    "model_name": "Colorado Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2008,
    "manufacturer_name": "Chevrolet",
    "model_name": "Colorado Crew Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2008,
    "manufacturer_name": "Chevrolet",
    "model_name": "Equinox",
    "car_type": "SUV"
  },
  {
    "year": 2008,
    "manufacturer_name": "Chevrolet",
    "model_name": "Express 1500 Passenger",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2008,
    "manufacturer_name": "Chevrolet",
    "model_name": "Express 2500 Cargo",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2008,
    "manufacturer_name": "Chevrolet",
    "model_name": "HHR",
    "car_type": "Wagon"
  },
  {
    "year": 2008,
    "manufacturer_name": "Chevrolet",
    "model_name": "Silverado 1500 Crew Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2008,
    "manufacturer_name": "Chevrolet",
    "model_name": "Malibu",
    "car_type": "Sedan"
  },
  {
    "year": 2008,
    "manufacturer_name": "Chevrolet",
    "model_name": "Express 3500 Passenger",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2008,
    "manufacturer_name": "Chevrolet",
    "model_name": "Express 2500 Passenger",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2008,
    "manufacturer_name": "Chevrolet",
    "model_name": "Express 1500 Cargo",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2008,
    "manufacturer_name": "Chevrolet",
    "model_name": "Silverado 1500 Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2008,
    "manufacturer_name": "Chevrolet",
    "model_name": "Impala",
    "car_type": "Sedan"
  },
  {
    "year": 2008,
    "manufacturer_name": "Chevrolet",
    "model_name": "Malibu (Classic)",
    "car_type": "Sedan"
  },
  {
    "year": 2008,
    "manufacturer_name": "Chevrolet",
    "model_name": "Express 3500 Cargo",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2008,
    "manufacturer_name": "Chevrolet",
    "model_name": "Silverado 2500 HD Crew Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2008,
    "manufacturer_name": "Chevrolet",
    "model_name": "Silverado 3500 HD Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2008,
    "manufacturer_name": "Chevrolet",
    "model_name": "Silverado 1500 Extended Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2008,
    "manufacturer_name": "Chevrolet",
    "model_name": "Silverado 2500 HD Extended Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2008,
    "manufacturer_name": "Chevrolet",
    "model_name": "Silverado 2500 HD Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2008,
    "manufacturer_name": "Chevrolet",
    "model_name": "Tahoe",
    "car_type": "SUV"
  },
  {
    "year": 2008,
    "manufacturer_name": "Chrysler",
    "model_name": "300",
    "car_type": "Sedan"
  },
  {
    "year": 2008,
    "manufacturer_name": "Chevrolet",
    "model_name": "Silverado 3500 HD Crew Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2008,
    "manufacturer_name": "Chevrolet",
    "model_name": "TrailBlazer",
    "car_type": "SUV"
  },
  {
    "year": 2008,
    "manufacturer_name": "Chevrolet",
    "model_name": "Suburban 2500",
    "car_type": "SUV"
  },
  {
    "year": 2008,
    "manufacturer_name": "Chrysler",
    "model_name": "Aspen",
    "car_type": "SUV"
  },
  {
    "year": 2008,
    "manufacturer_name": "Chevrolet",
    "model_name": "Silverado 3500 HD Extended Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2008,
    "manufacturer_name": "Chrysler",
    "model_name": "Pacifica",
    "car_type": "Wagon"
  },
  {
    "year": 2008,
    "manufacturer_name": "Chevrolet",
    "model_name": "Suburban 1500",
    "car_type": "SUV"
  },
  {
    "year": 2008,
    "manufacturer_name": "Chevrolet",
    "model_name": "Uplander Cargo",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2008,
    "manufacturer_name": "Chrysler",
    "model_name": "Crossfire",
    "car_type": "Coupe, Convertible"
  },
  {
    "year": 2008,
    "manufacturer_name": "Chevrolet",
    "model_name": "Uplander Passenger",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2008,
    "manufacturer_name": "Dodge",
    "model_name": "Caliber",
    "car_type": "Wagon"
  },
  {
    "year": 2008,
    "manufacturer_name": "Dodge",
    "model_name": "Avenger",
    "car_type": "Sedan"
  },
  {
    "year": 2008,
    "manufacturer_name": "Chrysler",
    "model_name": "Sebring",
    "car_type": "Sedan, Convertible"
  },
  {
    "year": 2008,
    "manufacturer_name": "Dodge",
    "model_name": "Challenger",
    "car_type": "Coupe"
  },
  {
    "year": 2008,
    "manufacturer_name": "Dodge",
    "model_name": "Ram 2500 Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2008,
    "manufacturer_name": "Dodge",
    "model_name": "Ram 1500 Quad Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2008,
    "manufacturer_name": "Dodge",
    "model_name": "Grand Caravan Cargo",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2008,
    "manufacturer_name": "Dodge",
    "model_name": "Nitro",
    "car_type": "SUV"
  },
  {
    "year": 2008,
    "manufacturer_name": "Dodge",
    "model_name": "Ram 2500 Mega Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2008,
    "manufacturer_name": "Dodge",
    "model_name": "Dakota Crew Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2008,
    "manufacturer_name": "Dodge",
    "model_name": "Ram 1500 Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2008,
    "manufacturer_name": "Dodge",
    "model_name": "Sprinter 2500 Passenger",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2008,
    "manufacturer_name": "Dodge",
    "model_name": "Charger",
    "car_type": "Sedan"
  },
  {
    "year": 2008,
    "manufacturer_name": "Chrysler",
    "model_name": "PT Cruiser",
    "car_type": "Wagon, Convertible"
  },
  {
    "year": 2008,
    "manufacturer_name": "Chrysler",
    "model_name": "Town & Country",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2008,
    "manufacturer_name": "Dodge",
    "model_name": "Sprinter 2500 Cargo",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2008,
    "manufacturer_name": "Dodge",
    "model_name": "Durango",
    "car_type": "SUV"
  },
  {
    "year": 2008,
    "manufacturer_name": "Dodge",
    "model_name": "Grand Caravan Passenger",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2008,
    "manufacturer_name": "Dodge",
    "model_name": "Magnum",
    "car_type": "Wagon"
  },
  {
    "year": 2008,
    "manufacturer_name": "Dodge",
    "model_name": "Ram 2500 Quad Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2008,
    "manufacturer_name": "Dodge",
    "model_name": "Ram 1500 Mega Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2008,
    "manufacturer_name": "Dodge",
    "model_name": "Dakota Extended Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2008,
    "manufacturer_name": "Dodge",
    "model_name": "Ram 3500 Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2008,
    "manufacturer_name": "Ferrari",
    "model_name": "612 Scaglietti",
    "car_type": "Coupe"
  },
  {
    "year": 2008,
    "manufacturer_name": "Dodge",
    "model_name": "Ram 3500 Quad Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2008,
    "manufacturer_name": "Ferrari",
    "model_name": "F430",
    "car_type": "Convertible, Coupe"
  },
  {
    "year": 2008,
    "manufacturer_name": "Dodge",
    "model_name": "Sprinter 3500 Cargo",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2008,
    "manufacturer_name": "Dodge",
    "model_name": "Ram 3500 Mega Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2008,
    "manufacturer_name": "Ford",
    "model_name": "E250 Cargo",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2008,
    "manufacturer_name": "Dodge",
    "model_name": "Viper",
    "car_type": "Coupe, Convertible"
  },
  {
    "year": 2008,
    "manufacturer_name": "Ferrari",
    "model_name": "599 GTB Fiorano",
    "car_type": "Coupe"
  },
  {
    "year": 2008,
    "manufacturer_name": "Ferrari",
    "model_name": "430 Scuderia",
    "car_type": "Coupe"
  },
  {
    "year": 2008,
    "manufacturer_name": "Ford",
    "model_name": "Crown Victoria",
    "car_type": "Sedan"
  },
  {
    "year": 2008,
    "manufacturer_name": "Ford",
    "model_name": "E150 Super Duty Passenger",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2008,
    "manufacturer_name": "Ford",
    "model_name": "Expedition",
    "car_type": "SUV"
  },
  {
    "year": 2008,
    "manufacturer_name": "Ford",
    "model_name": "Explorer Sport Trac",
    "car_type": "SUV"
  },
  {
    "year": 2008,
    "manufacturer_name": "Ford",
    "model_name": "Escape",
    "car_type": "SUV"
  },
  {
    "year": 2008,
    "manufacturer_name": "Ford",
    "model_name": "F150 Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2008,
    "manufacturer_name": "Ford",
    "model_name": "F150 SuperCrew Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2008,
    "manufacturer_name": "Ford",
    "model_name": "Mustang",
    "car_type": "Coupe, Convertible"
  },
  {
    "year": 2008,
    "manufacturer_name": "Ford",
    "model_name": "Explorer",
    "car_type": "SUV"
  },
  {
    "year": 2008,
    "manufacturer_name": "Ford",
    "model_name": "Ranger Super Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2008,
    "manufacturer_name": "Ford",
    "model_name": "E150 Cargo",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2008,
    "manufacturer_name": "Ford",
    "model_name": "E350 Super Duty Passenger",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2008,
    "manufacturer_name": "Ford",
    "model_name": "E350 Super Duty Cargo",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2008,
    "manufacturer_name": "Ford",
    "model_name": "F350 Super Duty Crew Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2008,
    "manufacturer_name": "Ford",
    "model_name": "F250 Super Duty Crew Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2008,
    "manufacturer_name": "Ford",
    "model_name": "F350 Super Duty Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2008,
    "manufacturer_name": "Ford",
    "model_name": "Taurus X",
    "car_type": "SUV"
  },
  {
    "year": 2008,
    "manufacturer_name": "Ford",
    "model_name": "F150 Super Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2008,
    "manufacturer_name": "Ford",
    "model_name": "Expedition EL",
    "car_type": "SUV"
  },
  {
    "year": 2008,
    "manufacturer_name": "Ford",
    "model_name": "Edge",
    "car_type": "SUV"
  },
  {
    "year": 2008,
    "manufacturer_name": "Ford",
    "model_name": "Fusion",
    "car_type": "Sedan"
  },
  {
    "year": 2008,
    "manufacturer_name": "Ford",
    "model_name": "Ranger Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2008,
    "manufacturer_name": "Ford",
    "model_name": "F250 Super Duty Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2008,
    "manufacturer_name": "Ford",
    "model_name": "Focus",
    "car_type": "Coupe, Sedan"
  },
  {
    "year": 2008,
    "manufacturer_name": "GMC",
    "model_name": "Acadia",
    "car_type": "SUV"
  },
  {
    "year": 2008,
    "manufacturer_name": "Ford",
    "model_name": "F350 Super Duty Super Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2008,
    "manufacturer_name": "Ford",
    "model_name": "F250 Super Duty Super Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2008,
    "manufacturer_name": "Ford",
    "model_name": "F450 Super Duty Crew Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2008,
    "manufacturer_name": "GMC",
    "model_name": "Savana 2500 Passenger",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2008,
    "manufacturer_name": "GMC",
    "model_name": "Canyon Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2008,
    "manufacturer_name": "Ford",
    "model_name": "Taurus",
    "car_type": "Sedan"
  },
  {
    "year": 2008,
    "manufacturer_name": "GMC",
    "model_name": "Envoy",
    "car_type": "SUV"
  },
  {
    "year": 2008,
    "manufacturer_name": "GMC",
    "model_name": "Savana 1500 Passenger",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2008,
    "manufacturer_name": "GMC",
    "model_name": "Savana 3500 Cargo",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2008,
    "manufacturer_name": "GMC",
    "model_name": "Canyon Crew Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2008,
    "manufacturer_name": "GMC",
    "model_name": "Savana 2500 Cargo",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2008,
    "manufacturer_name": "GMC",
    "model_name": "Savana 1500 Cargo",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2008,
    "manufacturer_name": "GMC",
    "model_name": "Canyon Extended Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2008,
    "manufacturer_name": "GMC",
    "model_name": "Sierra 1500 Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2008,
    "manufacturer_name": "GMC",
    "model_name": "Sierra 2500 HD Crew Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2008,
    "manufacturer_name": "GMC",
    "model_name": "Savana 3500 Passenger",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2008,
    "manufacturer_name": "GMC",
    "model_name": "Sierra 3500 HD Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2008,
    "manufacturer_name": "GMC",
    "model_name": "Sierra 1500 Extended Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2008,
    "manufacturer_name": "GMC",
    "model_name": "Sierra 1500 Crew Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2008,
    "manufacturer_name": "GMC",
    "model_name": "Sierra 3500 HD Crew Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2008,
    "manufacturer_name": "GMC",
    "model_name": "Sierra 2500 HD Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2008,
    "manufacturer_name": "GMC",
    "model_name": "Sierra 2500 HD Extended Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2008,
    "manufacturer_name": "Honda",
    "model_name": "Civic",
    "car_type": "Coupe, Sedan"
  },
  {
    "year": 2008,
    "manufacturer_name": "Honda",
    "model_name": "Element",
    "car_type": "SUV"
  },
  {
    "year": 2008,
    "manufacturer_name": "Honda",
    "model_name": "Fit",
    "car_type": "Hatchback"
  },
  {
    "year": 2008,
    "manufacturer_name": "GMC",
    "model_name": "Yukon XL 2500",
    "car_type": "SUV"
  },
  {
    "year": 2008,
    "manufacturer_name": "Honda",
    "model_name": "Accord",
    "car_type": "Sedan, Coupe"
  },
  {
    "year": 2008,
    "manufacturer_name": "GMC",
    "model_name": "Yukon XL 1500",
    "car_type": "SUV"
  },
  {
    "year": 2008,
    "manufacturer_name": "GMC",
    "model_name": "Sierra 3500 HD Extended Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2008,
    "manufacturer_name": "Honda",
    "model_name": "Pilot",
    "car_type": "SUV"
  },
  {
    "year": 2008,
    "manufacturer_name": "GMC",
    "model_name": "Yukon",
    "car_type": "SUV"
  },
  {
    "year": 2008,
    "manufacturer_name": "Hyundai",
    "model_name": "Accent",
    "car_type": "Hatchback, Sedan"
  },
  {
    "year": 2008,
    "manufacturer_name": "INFINITI",
    "model_name": "FX",
    "car_type": "SUV"
  },
  {
    "year": 2008,
    "manufacturer_name": "Honda",
    "model_name": "Ridgeline",
    "car_type": "Pickup"
  },
  {
    "year": 2008,
    "manufacturer_name": "HUMMER",
    "model_name": "H2",
    "car_type": "SUV"
  },
  {
    "year": 2008,
    "manufacturer_name": "Hyundai",
    "model_name": "Tucson",
    "car_type": "SUV"
  },
  {
    "year": 2008,
    "manufacturer_name": "Hyundai",
    "model_name": "Sonata",
    "car_type": "Sedan"
  },
  {
    "year": 2008,
    "manufacturer_name": "Hyundai",
    "model_name": "Azera",
    "car_type": "Sedan"
  },
  {
    "year": 2008,
    "manufacturer_name": "Honda",
    "model_name": "CR-V",
    "car_type": "SUV"
  },
  {
    "year": 2008,
    "manufacturer_name": "INFINITI",
    "model_name": "QX",
    "car_type": "SUV"
  },
  {
    "year": 2008,
    "manufacturer_name": "Honda",
    "model_name": "S2000",
    "car_type": "Convertible"
  },
  {
    "year": 2008,
    "manufacturer_name": "Hyundai",
    "model_name": "Entourage",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2008,
    "manufacturer_name": "Isuzu",
    "model_name": "i-370 Extended Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2008,
    "manufacturer_name": "HUMMER",
    "model_name": "H3",
    "car_type": "SUV"
  },
  {
    "year": 2008,
    "manufacturer_name": "INFINITI",
    "model_name": "M",
    "car_type": "Sedan"
  },
  {
    "year": 2008,
    "manufacturer_name": "Hyundai",
    "model_name": "Tiburon",
    "car_type": "Hatchback"
  },
  {
    "year": 2008,
    "manufacturer_name": "Hyundai",
    "model_name": "Elantra",
    "car_type": "Sedan"
  },
  {
    "year": 2008,
    "manufacturer_name": "Hyundai",
    "model_name": "Veracruz",
    "car_type": "SUV"
  },
  {
    "year": 2008,
    "manufacturer_name": "Honda",
    "model_name": "Odyssey",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2008,
    "manufacturer_name": "Hyundai",
    "model_name": "Santa Fe",
    "car_type": "SUV"
  },
  {
    "year": 2008,
    "manufacturer_name": "Isuzu",
    "model_name": "i-290 Extended Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2008,
    "manufacturer_name": "Jaguar",
    "model_name": "XK",
    "car_type": "Coupe, Convertible"
  },
  {
    "year": 2008,
    "manufacturer_name": "INFINITI",
    "model_name": "EX",
    "car_type": "SUV"
  },
  {
    "year": 2008,
    "manufacturer_name": "INFINITI",
    "model_name": "G",
    "car_type": "Sedan, Coupe"
  },
  {
    "year": 2008,
    "manufacturer_name": "Jaguar",
    "model_name": "S-Type",
    "car_type": "Sedan"
  },
  {
    "year": 2008,
    "manufacturer_name": "Jeep",
    "model_name": "Commander",
    "car_type": "SUV"
  },
  {
    "year": 2008,
    "manufacturer_name": "Land Rover",
    "model_name": "LR2",
    "car_type": "SUV"
  },
  {
    "year": 2008,
    "manufacturer_name": "Jaguar",
    "model_name": "XJ",
    "car_type": "Sedan"
  },
  {
    "year": 2008,
    "manufacturer_name": "Jeep",
    "model_name": "Compass",
    "car_type": "SUV"
  },
  {
    "year": 2008,
    "manufacturer_name": "Lamborghini",
    "model_name": "Murcielago LP640",
    "car_type": "Coupe, Convertible"
  },
  {
    "year": 2008,
    "manufacturer_name": "Jeep",
    "model_name": "Grand Cherokee",
    "car_type": "SUV"
  },
  {
    "year": 2008,
    "manufacturer_name": "Kia",
    "model_name": "Sportage",
    "car_type": "SUV"
  },
  {
    "year": 2008,
    "manufacturer_name": "Kia",
    "model_name": "Amanti",
    "car_type": "Sedan"
  },
  {
    "year": 2008,
    "manufacturer_name": "Jeep",
    "model_name": "Patriot",
    "car_type": "SUV"
  },
  {
    "year": 2008,
    "manufacturer_name": "Kia",
    "model_name": "Rondo",
    "car_type": "Wagon"
  },
  {
    "year": 2008,
    "manufacturer_name": "Jeep",
    "model_name": "Wrangler",
    "car_type": "SUV"
  },
  {
    "year": 2008,
    "manufacturer_name": "Isuzu",
    "model_name": "Ascender",
    "car_type": "SUV"
  },
  {
    "year": 2008,
    "manufacturer_name": "Jeep",
    "model_name": "Liberty",
    "car_type": "SUV"
  },
  {
    "year": 2008,
    "manufacturer_name": "Kia",
    "model_name": "Sorento",
    "car_type": "SUV"
  },
  {
    "year": 2008,
    "manufacturer_name": "Lexus",
    "model_name": "ES",
    "car_type": "Sedan"
  },
  {
    "year": 2008,
    "manufacturer_name": "Land Rover",
    "model_name": "Range Rover",
    "car_type": "SUV"
  },
  {
    "year": 2008,
    "manufacturer_name": "Jaguar",
    "model_name": "X-Type",
    "car_type": "Sedan, Wagon"
  },
  {
    "year": 2008,
    "manufacturer_name": "Isuzu",
    "model_name": "i-370 Crew Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2008,
    "manufacturer_name": "Kia",
    "model_name": "Optima",
    "car_type": "Sedan"
  },
  {
    "year": 2008,
    "manufacturer_name": "Kia",
    "model_name": "Rio",
    "car_type": "Sedan, Hatchback"
  },
  {
    "year": 2008,
    "manufacturer_name": "Kia",
    "model_name": "Sedona",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2008,
    "manufacturer_name": "Lamborghini",
    "model_name": "Gallardo",
    "car_type": "Convertible, Coupe"
  },
  {
    "year": 2008,
    "manufacturer_name": "Kia",
    "model_name": "Spectra",
    "car_type": "Sedan, Hatchback"
  },
  {
    "year": 2008,
    "manufacturer_name": "Lexus",
    "model_name": "SC",
    "car_type": "Convertible"
  },
  {
    "year": 2008,
    "manufacturer_name": "Lexus",
    "model_name": "IS",
    "car_type": "Sedan"
  },
  {
    "year": 2008,
    "manufacturer_name": "Lexus",
    "model_name": "GS",
    "car_type": "Sedan"
  },
  {
    "year": 2008,
    "manufacturer_name": "Lexus",
    "model_name": "LS",
    "car_type": "Sedan"
  },
  {
    "year": 2008,
    "manufacturer_name": "Lincoln",
    "model_name": "MKZ",
    "car_type": "Sedan"
  },
  {
    "year": 2008,
    "manufacturer_name": "Lincoln",
    "model_name": "MKX",
    "car_type": "SUV"
  },
  {
    "year": 2008,
    "manufacturer_name": "Lincoln",
    "model_name": "Navigator L",
    "car_type": "SUV"
  },
  {
    "year": 2008,
    "manufacturer_name": "Lexus",
    "model_name": "GX",
    "car_type": "SUV"
  },
  {
    "year": 2008,
    "manufacturer_name": "Land Rover",
    "model_name": "LR3",
    "car_type": "SUV"
  },
  {
    "year": 2008,
    "manufacturer_name": "Maserati",
    "model_name": "Quattroporte",
    "car_type": "Sedan"
  },
  {
    "year": 2008,
    "manufacturer_name": "Lotus",
    "model_name": "Elise",
    "car_type": "Coupe"
  },
  {
    "year": 2008,
    "manufacturer_name": "Land Rover",
    "model_name": "Range Rover Sport",
    "car_type": "SUV"
  },
  {
    "year": 2008,
    "manufacturer_name": "Lexus",
    "model_name": "LX",
    "car_type": "SUV"
  },
  {
    "year": 2008,
    "manufacturer_name": "Lexus",
    "model_name": "IS F",
    "car_type": "Sedan"
  },
  {
    "year": 2008,
    "manufacturer_name": "MAZDA",
    "model_name": "MX-5 Miata",
    "car_type": "Convertible"
  },
  {
    "year": 2008,
    "manufacturer_name": "Lincoln",
    "model_name": "Town Car",
    "car_type": "Sedan"
  },
  {
    "year": 2008,
    "manufacturer_name": "MAZDA",
    "model_name": "Tribute",
    "car_type": "SUV"
  },
  {
    "year": 2008,
    "manufacturer_name": "MAZDA",
    "model_name": "MAZDA3",
    "car_type": "Sedan, Hatchback"
  },
  {
    "year": 2008,
    "manufacturer_name": "MAZDA",
    "model_name": "CX-9",
    "car_type": "SUV"
  },
  {
    "year": 2008,
    "manufacturer_name": "MAZDA",
    "model_name": "B-Series Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2008,
    "manufacturer_name": "Maserati",
    "model_name": "GranTurismo",
    "car_type": "Coupe"
  },
  {
    "year": 2008,
    "manufacturer_name": "Lotus",
    "model_name": "Exige S",
    "car_type": "Coupe"
  },
  {
    "year": 2008,
    "manufacturer_name": "MAZDA",
    "model_name": "MAZDA5",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2008,
    "manufacturer_name": "Maybach",
    "model_name": "57",
    "car_type": "Sedan"
  },
  {
    "year": 2008,
    "manufacturer_name": "Maybach",
    "model_name": "62",
    "car_type": "Sedan"
  },
  {
    "year": 2008,
    "manufacturer_name": "Mercedes-Benz",
    "model_name": "CLK-Class",
    "car_type": "Convertible, Coupe"
  },
  {
    "year": 2008,
    "manufacturer_name": "MAZDA",
    "model_name": "B-Series Extended Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2008,
    "manufacturer_name": "Mercedes-Benz",
    "model_name": "C-Class",
    "car_type": "Sedan"
  },
  {
    "year": 2008,
    "manufacturer_name": "Lincoln",
    "model_name": "Mark LT",
    "car_type": "Pickup"
  },
  {
    "year": 2008,
    "manufacturer_name": "Lexus",
    "model_name": "RX",
    "car_type": "SUV"
  },
  {
    "year": 2008,
    "manufacturer_name": "MAZDA",
    "model_name": "MAZDA6",
    "car_type": "Sedan, Hatchback"
  },
  {
    "year": 2008,
    "manufacturer_name": "MAZDA",
    "model_name": "RX-8",
    "car_type": "Coupe"
  },
  {
    "year": 2008,
    "manufacturer_name": "Mercedes-Benz",
    "model_name": "CL-Class",
    "car_type": "Coupe"
  },
  {
    "year": 2008,
    "manufacturer_name": "MAZDA",
    "model_name": "CX-7",
    "car_type": "SUV"
  },
  {
    "year": 2008,
    "manufacturer_name": "Lincoln",
    "model_name": "Navigator",
    "car_type": "SUV"
  },
  {
    "year": 2008,
    "manufacturer_name": "Mercedes-Benz",
    "model_name": "CLS-Class",
    "car_type": "Coupe"
  },
  {
    "year": 2008,
    "manufacturer_name": "Mercedes-Benz",
    "model_name": "R-Class",
    "car_type": "Wagon"
  },
  {
    "year": 2008,
    "manufacturer_name": "Mercury",
    "model_name": "Mariner",
    "car_type": "SUV"
  },
  {
    "year": 2008,
    "manufacturer_name": "Mercury",
    "model_name": "Grand Marquis",
    "car_type": "Sedan"
  },
  {
    "year": 2008,
    "manufacturer_name": "Mercedes-Benz",
    "model_name": "M-Class",
    "car_type": "SUV"
  },
  {
    "year": 2008,
    "manufacturer_name": "Mitsubishi",
    "model_name": "Outlander",
    "car_type": "SUV"
  },
  {
    "year": 2008,
    "manufacturer_name": "Mercedes-Benz",
    "model_name": "E-Class",
    "car_type": "Sedan, Wagon"
  },
  {
    "year": 2008,
    "manufacturer_name": "MINI",
    "model_name": "Clubman",
    "car_type": "Hatchback"
  },
  {
    "year": 2008,
    "manufacturer_name": "Mercury",
    "model_name": "Milan",
    "car_type": "Sedan"
  },
  {
    "year": 2008,
    "manufacturer_name": "Mercedes-Benz",
    "model_name": "SLR McLaren",
    "car_type": "Convertible"
  },
  {
    "year": 2008,
    "manufacturer_name": "MINI",
    "model_name": "Convertible",
    "car_type": "Convertible"
  },
  {
    "year": 2008,
    "manufacturer_name": "Mercedes-Benz",
    "model_name": "G-Class",
    "car_type": "SUV"
  },
  {
    "year": 2008,
    "manufacturer_name": "Mitsubishi",
    "model_name": "Raider Extended Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2008,
    "manufacturer_name": "Mercury",
    "model_name": "Sable",
    "car_type": "Sedan"
  },
  {
    "year": 2008,
    "manufacturer_name": "Mercedes-Benz",
    "model_name": "S-Class",
    "car_type": "Sedan"
  },
  {
    "year": 2008,
    "manufacturer_name": "Mitsubishi",
    "model_name": "Endeavor",
    "car_type": "SUV"
  },
  {
    "year": 2008,
    "manufacturer_name": "Mitsubishi",
    "model_name": "Galant",
    "car_type": "Sedan"
  },
  {
    "year": 2008,
    "manufacturer_name": "Mercedes-Benz",
    "model_name": "GL-Class",
    "car_type": "SUV"
  },
  {
    "year": 2008,
    "manufacturer_name": "Mercedes-Benz",
    "model_name": "SL-Class",
    "car_type": "Convertible"
  },
  {
    "year": 2008,
    "manufacturer_name": "Nissan",
    "model_name": "Altima",
    "car_type": "Sedan, Coupe"
  },
  {
    "year": 2008,
    "manufacturer_name": "Nissan",
    "model_name": "350Z",
    "car_type": "Coupe, Convertible"
  },
  {
    "year": 2008,
    "manufacturer_name": "Mitsubishi",
    "model_name": "Lancer",
    "car_type": "Sedan"
  },
  {
    "year": 2008,
    "manufacturer_name": "MINI",
    "model_name": "Cooper",
    "car_type": "Hatchback"
  },
  {
    "year": 2008,
    "manufacturer_name": "Pontiac",
    "model_name": "G8",
    "car_type": "Sedan"
  },
  {
    "year": 2008,
    "manufacturer_name": "Nissan",
    "model_name": "Armada",
    "car_type": "SUV"
  },
  {
    "year": 2008,
    "manufacturer_name": "Nissan",
    "model_name": "Pathfinder",
    "car_type": "SUV"
  },
  {
    "year": 2008,
    "manufacturer_name": "Nissan",
    "model_name": "Titan Crew Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2008,
    "manufacturer_name": "Mercury",
    "model_name": "Mountaineer",
    "car_type": "SUV"
  },
  {
    "year": 2008,
    "manufacturer_name": "Nissan",
    "model_name": "Maxima",
    "car_type": "Sedan"
  },
  {
    "year": 2008,
    "manufacturer_name": "Mercedes-Benz",
    "model_name": "SLK-Class",
    "car_type": "Convertible"
  },
  {
    "year": 2008,
    "manufacturer_name": "Nissan",
    "model_name": "Titan King Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2008,
    "manufacturer_name": "Nissan",
    "model_name": "Sentra",
    "car_type": "Sedan"
  },
  {
    "year": 2008,
    "manufacturer_name": "Nissan",
    "model_name": "Frontier King Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2008,
    "manufacturer_name": "Nissan",
    "model_name": "Quest",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2008,
    "manufacturer_name": "Pontiac",
    "model_name": "G6",
    "car_type": "Sedan, Coupe, Convertible"
  },
  {
    "year": 2008,
    "manufacturer_name": "Nissan",
    "model_name": "Versa",
    "car_type": "Sedan, Hatchback"
  },
  {
    "year": 2008,
    "manufacturer_name": "Pontiac",
    "model_name": "G5",
    "car_type": "Coupe"
  },
  {
    "year": 2008,
    "manufacturer_name": "Pontiac",
    "model_name": "Torrent",
    "car_type": "SUV"
  },
  {
    "year": 2008,
    "manufacturer_name": "Saab",
    "model_name": "3-Sep",
    "car_type": "Sedan, Convertible, Wagon"
  },
  {
    "year": 2008,
    "manufacturer_name": "Porsche",
    "model_name": "911",
    "car_type": "Coupe, Convertible"
  },
  {
    "year": 2008,
    "manufacturer_name": "Porsche",
    "model_name": "Cayman",
    "car_type": "Coupe"
  },
  {
    "year": 2008,
    "manufacturer_name": "Mitsubishi",
    "model_name": "Raider Double Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2008,
    "manufacturer_name": "Pontiac",
    "model_name": "Grand Prix",
    "car_type": "Sedan"
  },
  {
    "year": 2008,
    "manufacturer_name": "Porsche",
    "model_name": "Boxster",
    "car_type": "Convertible"
  },
  {
    "year": 2008,
    "manufacturer_name": "Rolls-Royce",
    "model_name": "Phantom",
    "car_type": "Convertible, Sedan, Coupe"
  },
  {
    "year": 2008,
    "manufacturer_name": "Pontiac",
    "model_name": "Vibe",
    "car_type": "Wagon"
  },
  {
    "year": 2008,
    "manufacturer_name": "Mitsubishi",
    "model_name": "Eclipse",
    "car_type": "Convertible, Coupe"
  },
  {
    "year": 2008,
    "manufacturer_name": "Toyota",
    "model_name": "FJ Cruiser",
    "car_type": "SUV"
  },
  {
    "year": 2008,
    "manufacturer_name": "Scion",
    "model_name": "tC",
    "car_type": "Coupe"
  },
  {
    "year": 2008,
    "manufacturer_name": "smart",
    "model_name": "fortwo",
    "car_type": "Hatchback, Convertible"
  },
  {
    "year": 2008,
    "manufacturer_name": "Suzuki",
    "model_name": "SX4",
    "car_type": "Sedan, Hatchback"
  },
  {
    "year": 2008,
    "manufacturer_name": "Subaru",
    "model_name": "Tribeca",
    "car_type": "SUV"
  },
  {
    "year": 2008,
    "manufacturer_name": "Scion",
    "model_name": "xD",
    "car_type": "Hatchback"
  },
  {
    "year": 2008,
    "manufacturer_name": "Saab",
    "model_name": "5-Sep",
    "car_type": "Sedan, Wagon"
  },
  {
    "year": 2008,
    "manufacturer_name": "Suzuki",
    "model_name": "XL7",
    "car_type": "SUV"
  },
  {
    "year": 2008,
    "manufacturer_name": "Subaru",
    "model_name": "Legacy",
    "car_type": "Sedan"
  },
  {
    "year": 2008,
    "manufacturer_name": "Nissan",
    "model_name": "Frontier Crew Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2008,
    "manufacturer_name": "Saturn",
    "model_name": "Astra",
    "car_type": "Hatchback"
  },
  {
    "year": 2008,
    "manufacturer_name": "Subaru",
    "model_name": "Outback",
    "car_type": "Wagon"
  },
  {
    "year": 2008,
    "manufacturer_name": "Nissan",
    "model_name": "Rogue",
    "car_type": "SUV"
  },
  {
    "year": 2008,
    "manufacturer_name": "Scion",
    "model_name": "xB",
    "car_type": "Hatchback"
  },
  {
    "year": 2008,
    "manufacturer_name": "Saturn",
    "model_name": "Outlook",
    "car_type": "SUV"
  },
  {
    "year": 2008,
    "manufacturer_name": "Subaru",
    "model_name": "Impreza",
    "car_type": "Sedan, Wagon"
  },
  {
    "year": 2008,
    "manufacturer_name": "Toyota",
    "model_name": "Camry",
    "car_type": "Sedan"
  },
  {
    "year": 2008,
    "manufacturer_name": "Toyota",
    "model_name": "Sienna",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2008,
    "manufacturer_name": "Saturn",
    "model_name": "Aura",
    "car_type": "Sedan"
  },
  {
    "year": 2008,
    "manufacturer_name": "Toyota",
    "model_name": "Avalon",
    "car_type": "Sedan"
  },
  {
    "year": 2008,
    "manufacturer_name": "Toyota",
    "model_name": "Prius",
    "car_type": "Hatchback"
  },
  {
    "year": 2008,
    "manufacturer_name": "Porsche",
    "model_name": "Cayenne",
    "car_type": "SUV"
  },
  {
    "year": 2008,
    "manufacturer_name": "Suzuki",
    "model_name": "Reno",
    "car_type": "Hatchback"
  },
  {
    "year": 2008,
    "manufacturer_name": "Saturn",
    "model_name": "SKY",
    "car_type": "Convertible"
  },
  {
    "year": 2008,
    "manufacturer_name": "Saab",
    "model_name": "9-7X",
    "car_type": "SUV"
  },
  {
    "year": 2008,
    "manufacturer_name": "Toyota",
    "model_name": "RAV4",
    "car_type": "SUV"
  },
  {
    "year": 2008,
    "manufacturer_name": "Toyota",
    "model_name": "Tacoma Access Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2008,
    "manufacturer_name": "Toyota",
    "model_name": "Corolla",
    "car_type": "Sedan"
  },
  {
    "year": 2008,
    "manufacturer_name": "Suzuki",
    "model_name": "Grand Vitara",
    "car_type": "SUV"
  },
  {
    "year": 2008,
    "manufacturer_name": "Nissan",
    "model_name": "Xterra",
    "car_type": "SUV"
  },
  {
    "year": 2008,
    "manufacturer_name": "Toyota",
    "model_name": "Land Cruiser",
    "car_type": "SUV"
  },
  {
    "year": 2008,
    "manufacturer_name": "Toyota",
    "model_name": "Matrix",
    "car_type": "Wagon"
  },
  {
    "year": 2008,
    "manufacturer_name": "Pontiac",
    "model_name": "Solstice",
    "car_type": "Convertible"
  },
  {
    "year": 2008,
    "manufacturer_name": "Toyota",
    "model_name": "Solara",
    "car_type": "Coupe, Convertible"
  },
  {
    "year": 2008,
    "manufacturer_name": "Volkswagen",
    "model_name": "New Beetle",
    "car_type": "Hatchback, Convertible"
  },
  {
    "year": 2008,
    "manufacturer_name": "Subaru",
    "model_name": "Forester",
    "car_type": "SUV"
  },
  {
    "year": 2008,
    "manufacturer_name": "Volkswagen",
    "model_name": "R32",
    "car_type": "Hatchback"
  },
  {
    "year": 2008,
    "manufacturer_name": "Toyota",
    "model_name": "Tundra Double Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2008,
    "manufacturer_name": "Volkswagen",
    "model_name": "GTI",
    "car_type": "Hatchback"
  },
  {
    "year": 2008,
    "manufacturer_name": "Toyota",
    "model_name": "Tacoma Double Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2008,
    "manufacturer_name": "Toyota",
    "model_name": "4Runner",
    "car_type": "SUV"
  },
  {
    "year": 2008,
    "manufacturer_name": "Saturn",
    "model_name": "VUE",
    "car_type": "SUV"
  },
  {
    "year": 2008,
    "manufacturer_name": "Toyota",
    "model_name": "Yaris",
    "car_type": "Hatchback, Sedan"
  },
  {
    "year": 2008,
    "manufacturer_name": "Toyota",
    "model_name": "Highlander",
    "car_type": "SUV"
  },
  {
    "year": 2008,
    "manufacturer_name": "Toyota",
    "model_name": "Tundra Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2008,
    "manufacturer_name": "Volkswagen",
    "model_name": "GLI",
    "car_type": "Sedan"
  },
  {
    "year": 2008,
    "manufacturer_name": "Suzuki",
    "model_name": "Forenza",
    "car_type": "Sedan, Wagon"
  },
  {
    "year": 2008,
    "manufacturer_name": "Toyota",
    "model_name": "Tacoma Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2008,
    "manufacturer_name": "Volkswagen",
    "model_name": "Jetta",
    "car_type": "Sedan"
  },
  {
    "year": 2008,
    "manufacturer_name": "Toyota",
    "model_name": "Tundra CrewMax",
    "car_type": "Pickup"
  },
  {
    "year": 2008,
    "manufacturer_name": "Toyota",
    "model_name": "Sequoia",
    "car_type": "SUV"
  },
  {
    "year": 2008,
    "manufacturer_name": "Volkswagen",
    "model_name": "Passat",
    "car_type": "Sedan, Wagon"
  },
  {
    "year": 2008,
    "manufacturer_name": "Volkswagen",
    "model_name": "Eos",
    "car_type": "Convertible"
  },
  {
    "year": 2008,
    "manufacturer_name": "Volkswagen",
    "model_name": "Rabbit",
    "car_type": "Hatchback"
  },
  {
    "year": 2008,
    "manufacturer_name": "Volvo",
    "model_name": "S60",
    "car_type": "Sedan"
  },
  {
    "year": 2008,
    "manufacturer_name": "Volvo",
    "model_name": "XC90",
    "car_type": "SUV"
  },
  {
    "year": 2008,
    "manufacturer_name": "Volkswagen",
    "model_name": "Touareg 2",
    "car_type": "SUV"
  },
  {
    "year": 2008,
    "manufacturer_name": "Volvo",
    "model_name": "C30",
    "car_type": "Hatchback"
  },
  {
    "year": 2008,
    "manufacturer_name": "Volvo",
    "model_name": "V50",
    "car_type": "Wagon"
  },
  {
    "year": 2008,
    "manufacturer_name": "Volvo",
    "model_name": "V70",
    "car_type": "Wagon"
  },
  {
    "year": 2008,
    "manufacturer_name": "Volvo",
    "model_name": "S40",
    "car_type": "Sedan"
  },
  {
    "year": 2007,
    "manufacturer_name": "Acura",
    "model_name": "MDX",
    "car_type": "SUV"
  },
  {
    "year": 2007,
    "manufacturer_name": "Acura",
    "model_name": "TL",
    "car_type": "Sedan"
  },
  {
    "year": 2008,
    "manufacturer_name": "Volvo",
    "model_name": "S80",
    "car_type": "Sedan"
  },
  {
    "year": 2008,
    "manufacturer_name": "Volvo",
    "model_name": "XC70",
    "car_type": "Wagon"
  },
  {
    "year": 2008,
    "manufacturer_name": "Volvo",
    "model_name": "C70",
    "car_type": "Convertible"
  },
  {
    "year": 2007,
    "manufacturer_name": "Audi",
    "model_name": "A8",
    "car_type": "Sedan"
  },
  {
    "year": 2007,
    "manufacturer_name": "Acura",
    "model_name": "TSX",
    "car_type": "Sedan"
  },
  {
    "year": 2007,
    "manufacturer_name": "Acura",
    "model_name": "RDX",
    "car_type": "SUV"
  },
  {
    "year": 2007,
    "manufacturer_name": "Audi",
    "model_name": "A4",
    "car_type": "Sedan, Wagon, Convertible"
  },
  {
    "year": 2007,
    "manufacturer_name": "Aston Martin",
    "model_name": "DB9",
    "car_type": "Convertible, Coupe"
  },
  {
    "year": 2007,
    "manufacturer_name": "Acura",
    "model_name": "RL",
    "car_type": "Sedan"
  },
  {
    "year": 2007,
    "manufacturer_name": "Audi",
    "model_name": "S4",
    "car_type": "Sedan, Wagon, Convertible"
  },
  {
    "year": 2007,
    "manufacturer_name": "Aston Martin",
    "model_name": "Vantage",
    "car_type": "Convertible, Coupe"
  },
  {
    "year": 2007,
    "manufacturer_name": "Bentley",
    "model_name": "Arnage",
    "car_type": "Sedan"
  },
  {
    "year": 2007,
    "manufacturer_name": "Buick",
    "model_name": "Rendezvous",
    "car_type": "SUV"
  },
  {
    "year": 2007,
    "manufacturer_name": "Bentley",
    "model_name": "Continental",
    "car_type": "Sedan, Coupe, Convertible"
  },
  {
    "year": 2007,
    "manufacturer_name": "Audi",
    "model_name": "Q7",
    "car_type": "SUV"
  },
  {
    "year": 2007,
    "manufacturer_name": "BMW",
    "model_name": "Alpina B7",
    "car_type": "Sedan"
  },
  {
    "year": 2007,
    "manufacturer_name": "BMW",
    "model_name": "7 Series",
    "car_type": "Sedan"
  },
  {
    "year": 2007,
    "manufacturer_name": "BMW",
    "model_name": "M5",
    "car_type": "Sedan"
  },
  {
    "year": 2007,
    "manufacturer_name": "BMW",
    "model_name": "3 Series",
    "car_type": "Coupe, Sedan, Convertible, Wagon"
  },
  {
    "year": 2007,
    "manufacturer_name": "BMW",
    "model_name": "Z4 M",
    "car_type": "Coupe, Convertible"
  },
  {
    "year": 2007,
    "manufacturer_name": "Audi",
    "model_name": "S8",
    "car_type": "Sedan"
  },
  {
    "year": 2007,
    "manufacturer_name": "Audi",
    "model_name": "A6",
    "car_type": "Sedan, Wagon"
  },
  {
    "year": 2007,
    "manufacturer_name": "Audi",
    "model_name": "S6",
    "car_type": "Sedan"
  },
  {
    "year": 2007,
    "manufacturer_name": "BMW",
    "model_name": "Z4",
    "car_type": "Convertible, Coupe"
  },
  {
    "year": 2007,
    "manufacturer_name": "Audi",
    "model_name": "RS 4",
    "car_type": "Sedan"
  },
  {
    "year": 2007,
    "manufacturer_name": "Buick",
    "model_name": "LaCrosse",
    "car_type": "Sedan"
  },
  {
    "year": 2007,
    "manufacturer_name": "Bentley",
    "model_name": "Azure",
    "car_type": "Convertible"
  },
  {
    "year": 2007,
    "manufacturer_name": "BMW",
    "model_name": "5 Series",
    "car_type": "Sedan, Wagon"
  },
  {
    "year": 2007,
    "manufacturer_name": "Audi",
    "model_name": "A3",
    "car_type": "Wagon"
  },
  {
    "year": 2007,
    "manufacturer_name": "BMW",
    "model_name": "M6",
    "car_type": "Coupe, Convertible"
  },
  {
    "year": 2007,
    "manufacturer_name": "BMW",
    "model_name": "X5",
    "car_type": "SUV"
  },
  {
    "year": 2007,
    "manufacturer_name": "Cadillac",
    "model_name": "Escalade",
    "car_type": "SUV"
  },
  {
    "year": 2007,
    "manufacturer_name": "Cadillac",
    "model_name": "Escalade ESV",
    "car_type": "SUV"
  },
  {
    "year": 2007,
    "manufacturer_name": "Chevrolet",
    "model_name": "Colorado Extended Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2007,
    "manufacturer_name": "Chevrolet",
    "model_name": "Avalanche",
    "car_type": "Pickup"
  },
  {
    "year": 2007,
    "manufacturer_name": "Cadillac",
    "model_name": "XLR",
    "car_type": "Convertible"
  },
  {
    "year": 2007,
    "manufacturer_name": "BMW",
    "model_name": "6 Series",
    "car_type": "Coupe, Convertible"
  },
  {
    "year": 2007,
    "manufacturer_name": "Chevrolet",
    "model_name": "Equinox",
    "car_type": "SUV"
  },
  {
    "year": 2007,
    "manufacturer_name": "Cadillac",
    "model_name": "SRX",
    "car_type": "SUV"
  },
  {
    "year": 2007,
    "manufacturer_name": "Cadillac",
    "model_name": "CTS",
    "car_type": "Sedan"
  },
  {
    "year": 2007,
    "manufacturer_name": "Buick",
    "model_name": "Lucerne",
    "car_type": "Sedan"
  },
  {
    "year": 2007,
    "manufacturer_name": "Cadillac",
    "model_name": "STS",
    "car_type": "Sedan"
  },
  {
    "year": 2007,
    "manufacturer_name": "Buick",
    "model_name": "Terraza",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2007,
    "manufacturer_name": "Chevrolet",
    "model_name": "Colorado Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2007,
    "manufacturer_name": "Buick",
    "model_name": "Rainier",
    "car_type": "SUV"
  },
  {
    "year": 2007,
    "manufacturer_name": "BMW",
    "model_name": "X3",
    "car_type": "SUV"
  },
  {
    "year": 2007,
    "manufacturer_name": "Chevrolet",
    "model_name": "Express 2500 Passenger",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2007,
    "manufacturer_name": "Chevrolet",
    "model_name": "Cobalt",
    "car_type": "Sedan, Coupe"
  },
  {
    "year": 2007,
    "manufacturer_name": "Cadillac",
    "model_name": "DTS",
    "car_type": "Sedan"
  },
  {
    "year": 2007,
    "manufacturer_name": "Chevrolet",
    "model_name": "Aveo",
    "car_type": "Sedan, Hatchback"
  },
  {
    "year": 2007,
    "manufacturer_name": "Cadillac",
    "model_name": "Escalade EXT",
    "car_type": "Pickup"
  },
  {
    "year": 2007,
    "manufacturer_name": "Chevrolet",
    "model_name": "Corvette",
    "car_type": "Coupe, Convertible"
  },
  {
    "year": 2007,
    "manufacturer_name": "Chevrolet",
    "model_name": "Impala",
    "car_type": "Sedan"
  },
  {
    "year": 2007,
    "manufacturer_name": "Chevrolet",
    "model_name": "Express 2500 Cargo",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2007,
    "manufacturer_name": "Chevrolet",
    "model_name": "HHR",
    "car_type": "Wagon"
  },
  {
    "year": 2007,
    "manufacturer_name": "Chevrolet",
    "model_name": "Silverado (Classic) 3500 Extended Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2007,
    "manufacturer_name": "Chevrolet",
    "model_name": "Express 3500 Passenger",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2007,
    "manufacturer_name": "Chevrolet",
    "model_name": "Express 1500 Passenger",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2007,
    "manufacturer_name": "Chevrolet",
    "model_name": "Colorado Crew Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2007,
    "manufacturer_name": "Chevrolet",
    "model_name": "Silverado (Classic) 2500 HD Crew Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2007,
    "manufacturer_name": "Chevrolet",
    "model_name": "Express 3500 Cargo",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2007,
    "manufacturer_name": "Chevrolet",
    "model_name": "Silverado (Classic) 1500 Crew Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2007,
    "manufacturer_name": "Chevrolet",
    "model_name": "Silverado (Classic) 1500 Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2007,
    "manufacturer_name": "Chevrolet",
    "model_name": "Malibu",
    "car_type": "Sedan, Hatchback"
  },
  {
    "year": 2007,
    "manufacturer_name": "Chevrolet",
    "model_name": "Silverado (Classic) 1500 Extended Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2007,
    "manufacturer_name": "Chevrolet",
    "model_name": "Silverado (Classic) 1500 HD Crew Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2007,
    "manufacturer_name": "Chevrolet",
    "model_name": "Silverado (Classic) 3500 Crew Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2007,
    "manufacturer_name": "Chevrolet",
    "model_name": "Monte Carlo",
    "car_type": "Coupe"
  },
  {
    "year": 2007,
    "manufacturer_name": "Chevrolet",
    "model_name": "Silverado 1500 Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2007,
    "manufacturer_name": "Chevrolet",
    "model_name": "Express 1500 Cargo",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2007,
    "manufacturer_name": "Chevrolet",
    "model_name": "Silverado 3500 HD Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2007,
    "manufacturer_name": "Chevrolet",
    "model_name": "Silverado 2500 HD Crew Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2007,
    "manufacturer_name": "Chevrolet",
    "model_name": "Silverado 2500 HD Extended Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2007,
    "manufacturer_name": "Chevrolet",
    "model_name": "Silverado 1500 Extended Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2007,
    "manufacturer_name": "Chevrolet",
    "model_name": "Silverado (Classic) 3500 Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2007,
    "manufacturer_name": "Chevrolet",
    "model_name": "Suburban 1500",
    "car_type": "SUV"
  },
  {
    "year": 2007,
    "manufacturer_name": "Chrysler",
    "model_name": "Crossfire",
    "car_type": "Coupe, Convertible"
  },
  {
    "year": 2007,
    "manufacturer_name": "Chevrolet",
    "model_name": "Silverado (Classic) 2500 HD Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2007,
    "manufacturer_name": "Chevrolet",
    "model_name": "Silverado 3500 HD Crew Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2007,
    "manufacturer_name": "Chevrolet",
    "model_name": "Silverado 3500 HD Extended Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2007,
    "manufacturer_name": "Chevrolet",
    "model_name": "Silverado 1500 Crew Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2007,
    "manufacturer_name": "Chevrolet",
    "model_name": "TrailBlazer",
    "car_type": "SUV"
  },
  {
    "year": 2007,
    "manufacturer_name": "Chevrolet",
    "model_name": "Uplander Cargo",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2007,
    "manufacturer_name": "Chevrolet",
    "model_name": "Silverado (Classic) 2500 HD Extended Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2007,
    "manufacturer_name": "Chevrolet",
    "model_name": "Silverado 2500 HD Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2007,
    "manufacturer_name": "Chevrolet",
    "model_name": "Tahoe",
    "car_type": "SUV"
  },
  {
    "year": 2007,
    "manufacturer_name": "Chrysler",
    "model_name": "300",
    "car_type": "Sedan"
  },
  {
    "year": 2007,
    "manufacturer_name": "Chevrolet",
    "model_name": "Uplander Passenger",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2007,
    "manufacturer_name": "Chrysler",
    "model_name": "Aspen",
    "car_type": "SUV"
  },
  {
    "year": 2007,
    "manufacturer_name": "Chevrolet",
    "model_name": "Suburban 2500",
    "car_type": "SUV"
  },
  {
    "year": 2007,
    "manufacturer_name": "Chrysler",
    "model_name": "Town & Country",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2007,
    "manufacturer_name": "Dodge",
    "model_name": "Caravan Passenger",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2007,
    "manufacturer_name": "Chrysler",
    "model_name": "Pacifica",
    "car_type": "Wagon"
  },
  {
    "year": 2007,
    "manufacturer_name": "Chrysler",
    "model_name": "PT Cruiser",
    "car_type": "Wagon, Convertible"
  },
  {
    "year": 2007,
    "manufacturer_name": "Chrysler",
    "model_name": "Sebring",
    "car_type": "Sedan"
  },
  {
    "year": 2007,
    "manufacturer_name": "Dodge",
    "model_name": "Caliber",
    "car_type": "Wagon"
  },
  {
    "year": 2007,
    "manufacturer_name": "Dodge",
    "model_name": "Nitro",
    "car_type": "SUV"
  },
  {
    "year": 2007,
    "manufacturer_name": "Dodge",
    "model_name": "Durango",
    "car_type": "SUV"
  },
  {
    "year": 2007,
    "manufacturer_name": "Dodge",
    "model_name": "Grand Caravan Passenger",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2007,
    "manufacturer_name": "Dodge",
    "model_name": "Caravan Cargo",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2007,
    "manufacturer_name": "Dodge",
    "model_name": "Ram 3500 Mega Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2007,
    "manufacturer_name": "Dodge",
    "model_name": "Ram 1500 Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2007,
    "manufacturer_name": "Dodge",
    "model_name": "Charger",
    "car_type": "Sedan"
  },
  {
    "year": 2007,
    "manufacturer_name": "Dodge",
    "model_name": "Magnum",
    "car_type": "Wagon"
  },
  {
    "year": 2007,
    "manufacturer_name": "Dodge",
    "model_name": "Grand Caravan Cargo",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2007,
    "manufacturer_name": "Dodge",
    "model_name": "Dakota Quad Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2007,
    "manufacturer_name": "Dodge",
    "model_name": "Dakota Club Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2007,
    "manufacturer_name": "Dodge",
    "model_name": "Ram 1500 Quad Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2007,
    "manufacturer_name": "Dodge",
    "model_name": "Ram 1500 Mega Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2007,
    "manufacturer_name": "Dodge",
    "model_name": "Ram 2500 Quad Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2007,
    "manufacturer_name": "Dodge",
    "model_name": "Ram 2500 Mega Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2007,
    "manufacturer_name": "Ford",
    "model_name": "E250 Super Duty Cargo",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2007,
    "manufacturer_name": "Dodge",
    "model_name": "Ram 3500 Quad Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2007,
    "manufacturer_name": "Ford",
    "model_name": "Expedition",
    "car_type": "SUV"
  },
  {
    "year": 2007,
    "manufacturer_name": "Ford",
    "model_name": "Explorer Sport Trac",
    "car_type": "Pickup"
  },
  {
    "year": 2007,
    "manufacturer_name": "Ford",
    "model_name": "Crown Victoria",
    "car_type": "Sedan"
  },
  {
    "year": 2007,
    "manufacturer_name": "Ford",
    "model_name": "F250 Super Duty Super Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2007,
    "manufacturer_name": "Dodge",
    "model_name": "Ram 3500 Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2007,
    "manufacturer_name": "Ford",
    "model_name": "Expedition EL",
    "car_type": "SUV"
  },
  {
    "year": 2007,
    "manufacturer_name": "Dodge",
    "model_name": "Ram 2500 Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2007,
    "manufacturer_name": "Ford",
    "model_name": "Escape",
    "car_type": "SUV"
  },
  {
    "year": 2007,
    "manufacturer_name": "Dodge",
    "model_name": "Sprinter 2500 Cargo",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2007,
    "manufacturer_name": "Ford",
    "model_name": "E150 Super Duty Passenger",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2007,
    "manufacturer_name": "Ferrari",
    "model_name": "599 GTB Fiorano",
    "car_type": "Coupe"
  },
  {
    "year": 2007,
    "manufacturer_name": "Ferrari",
    "model_name": "F430",
    "car_type": "Convertible, Coupe"
  },
  {
    "year": 2007,
    "manufacturer_name": "Dodge",
    "model_name": "Sprinter 2500 Passenger",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2007,
    "manufacturer_name": "Ford",
    "model_name": "E350 Super Duty Cargo",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2007,
    "manufacturer_name": "Ford",
    "model_name": "F250 Super Duty Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2007,
    "manufacturer_name": "Ford",
    "model_name": "F150 SuperCrew Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2007,
    "manufacturer_name": "Dodge",
    "model_name": "Sprinter 3500 Cargo",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2007,
    "manufacturer_name": "Ford",
    "model_name": "F150 Super Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2007,
    "manufacturer_name": "Ferrari",
    "model_name": "612 Scaglietti",
    "car_type": "Coupe"
  },
  {
    "year": 2007,
    "manufacturer_name": "Ford",
    "model_name": "F250 Super Duty Crew Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2007,
    "manufacturer_name": "Ford",
    "model_name": "Edge",
    "car_type": "SUV"
  },
  {
    "year": 2007,
    "manufacturer_name": "Ford",
    "model_name": "E150 Super Duty Cargo",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2007,
    "manufacturer_name": "Ford",
    "model_name": "F150 Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2007,
    "manufacturer_name": "Ford",
    "model_name": "E350 Super Duty Passenger",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2007,
    "manufacturer_name": "Ford",
    "model_name": "Explorer",
    "car_type": "SUV"
  },
  {
    "year": 2007,
    "manufacturer_name": "Ford",
    "model_name": "F350 Super Duty Crew Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2007,
    "manufacturer_name": "Ford",
    "model_name": "F350 Super Duty Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2007,
    "manufacturer_name": "GMC",
    "model_name": "Canyon Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2007,
    "manufacturer_name": "Ford",
    "model_name": "Freestar Cargo",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2007,
    "manufacturer_name": "Ford",
    "model_name": "Ranger Super Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2007,
    "manufacturer_name": "Ford",
    "model_name": "Five Hundred",
    "car_type": "Sedan"
  },
  {
    "year": 2007,
    "manufacturer_name": "Ford",
    "model_name": "F350 Super Duty Super Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2007,
    "manufacturer_name": "GMC",
    "model_name": "Savana 2500 Passenger",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2007,
    "manufacturer_name": "GMC",
    "model_name": "Sierra (Classic) 1500 HD Crew Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2007,
    "manufacturer_name": "Ford",
    "model_name": "Freestar Passenger",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2007,
    "manufacturer_name": "Ford",
    "model_name": "Focus",
    "car_type": "Hatchback, Sedan, Wagon"
  },
  {
    "year": 2007,
    "manufacturer_name": "Ford",
    "model_name": "Fusion",
    "car_type": "Sedan"
  },
  {
    "year": 2007,
    "manufacturer_name": "Honda",
    "model_name": "Odyssey",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2007,
    "manufacturer_name": "GMC",
    "model_name": "Sierra (Classic) 3500 Crew Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2007,
    "manufacturer_name": "GMC",
    "model_name": "Sierra 1500 Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2007,
    "manufacturer_name": "GMC",
    "model_name": "Sierra 3500 HD Extended Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2007,
    "manufacturer_name": "Honda",
    "model_name": "Accord",
    "car_type": "Sedan, Coupe"
  },
  {
    "year": 2007,
    "manufacturer_name": "Ford",
    "model_name": "Freestyle",
    "car_type": "SUV"
  },
  {
    "year": 2007,
    "manufacturer_name": "GMC",
    "model_name": "Canyon Crew Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2007,
    "manufacturer_name": "Ford",
    "model_name": "Ranger Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2007,
    "manufacturer_name": "Ford",
    "model_name": "Mustang",
    "car_type": "Coupe, Convertible"
  },
  {
    "year": 2007,
    "manufacturer_name": "GMC",
    "model_name": "Sierra (Classic) 1500 Crew Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2007,
    "manufacturer_name": "GMC",
    "model_name": "Savana 2500 Cargo",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2007,
    "manufacturer_name": "GMC",
    "model_name": "Canyon Extended Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2007,
    "manufacturer_name": "Ford",
    "model_name": "Taurus",
    "car_type": "Sedan"
  },
  {
    "year": 2007,
    "manufacturer_name": "GMC",
    "model_name": "Sierra (Classic) 1500 Extended Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2007,
    "manufacturer_name": "GMC",
    "model_name": "Savana 3500 Passenger",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2007,
    "manufacturer_name": "GMC",
    "model_name": "Savana 1500 Passenger",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2007,
    "manufacturer_name": "GMC",
    "model_name": "Sierra (Classic) 2500 HD Crew Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2007,
    "manufacturer_name": "GMC",
    "model_name": "Acadia",
    "car_type": "SUV"
  },
  {
    "year": 2007,
    "manufacturer_name": "GMC",
    "model_name": "Savana 1500 Cargo",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2007,
    "manufacturer_name": "GMC",
    "model_name": "Envoy",
    "car_type": "SUV"
  },
  {
    "year": 2007,
    "manufacturer_name": "GMC",
    "model_name": "Savana 3500 Cargo",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2007,
    "manufacturer_name": "GMC",
    "model_name": "Sierra 2500 HD Extended Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2007,
    "manufacturer_name": "GMC",
    "model_name": "Sierra (Classic) 1500 Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2007,
    "manufacturer_name": "GMC",
    "model_name": "Yukon",
    "car_type": "SUV"
  },
  {
    "year": 2007,
    "manufacturer_name": "Honda",
    "model_name": "Element",
    "car_type": "SUV"
  },
  {
    "year": 2007,
    "manufacturer_name": "GMC",
    "model_name": "Sierra (Classic) 3500 Extended Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2007,
    "manufacturer_name": "GMC",
    "model_name": "Sierra (Classic) 3500 Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2007,
    "manufacturer_name": "GMC",
    "model_name": "Sierra 1500 Crew Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2007,
    "manufacturer_name": "GMC",
    "model_name": "Sierra (Classic) 2500 HD Extended Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2007,
    "manufacturer_name": "GMC",
    "model_name": "Sierra 2500 HD Crew Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2007,
    "manufacturer_name": "Honda",
    "model_name": "Fit",
    "car_type": "Hatchback"
  },
  {
    "year": 2007,
    "manufacturer_name": "GMC",
    "model_name": "Sierra 3500 HD Crew Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2007,
    "manufacturer_name": "Honda",
    "model_name": "CR-V",
    "car_type": "SUV"
  },
  {
    "year": 2007,
    "manufacturer_name": "GMC",
    "model_name": "Yukon XL 1500",
    "car_type": "SUV"
  },
  {
    "year": 2007,
    "manufacturer_name": "GMC",
    "model_name": "Sierra 1500 Extended Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2007,
    "manufacturer_name": "GMC",
    "model_name": "Sierra (Classic) 2500 HD Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2007,
    "manufacturer_name": "GMC",
    "model_name": "Sierra 2500 HD Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2007,
    "manufacturer_name": "GMC",
    "model_name": "Yukon XL 2500",
    "car_type": "SUV"
  },
  {
    "year": 2007,
    "manufacturer_name": "GMC",
    "model_name": "Sierra 3500 HD Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2007,
    "manufacturer_name": "Honda",
    "model_name": "Civic",
    "car_type": "Sedan, Coupe"
  },
  {
    "year": 2007,
    "manufacturer_name": "Honda",
    "model_name": "Pilot",
    "car_type": "SUV"
  },
  {
    "year": 2007,
    "manufacturer_name": "HUMMER",
    "model_name": "H3",
    "car_type": "SUV"
  },
  {
    "year": 2007,
    "manufacturer_name": "Hyundai",
    "model_name": "Sonata",
    "car_type": "Sedan"
  },
  {
    "year": 2007,
    "manufacturer_name": "Honda",
    "model_name": "S2000",
    "car_type": "Convertible"
  },
  {
    "year": 2007,
    "manufacturer_name": "Hyundai",
    "model_name": "Azera",
    "car_type": "Sedan"
  },
  {
    "year": 2007,
    "manufacturer_name": "Hyundai",
    "model_name": "Tiburon",
    "car_type": "Coupe"
  },
  {
    "year": 2007,
    "manufacturer_name": "Hyundai",
    "model_name": "Veracruz",
    "car_type": "SUV"
  },
  {
    "year": 2007,
    "manufacturer_name": "INFINITI",
    "model_name": "G",
    "car_type": "Sedan, Coupe"
  },
  {
    "year": 2007,
    "manufacturer_name": "Honda",
    "model_name": "Ridgeline",
    "car_type": "Pickup"
  },
  {
    "year": 2007,
    "manufacturer_name": "Hyundai",
    "model_name": "Accent",
    "car_type": "Hatchback, Sedan"
  },
  {
    "year": 2007,
    "manufacturer_name": "Hyundai",
    "model_name": "Entourage",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2007,
    "manufacturer_name": "Hyundai",
    "model_name": "Tucson",
    "car_type": "SUV"
  },
  {
    "year": 2007,
    "manufacturer_name": "Isuzu",
    "model_name": "Ascender",
    "car_type": "SUV"
  },
  {
    "year": 2007,
    "manufacturer_name": "INFINITI",
    "model_name": "M",
    "car_type": "Sedan"
  },
  {
    "year": 2007,
    "manufacturer_name": "HUMMER",
    "model_name": "H2",
    "car_type": "SUV, Pickup"
  },
  {
    "year": 2007,
    "manufacturer_name": "Hyundai",
    "model_name": "Santa Fe",
    "car_type": "SUV"
  },
  {
    "year": 2007,
    "manufacturer_name": "Hyundai",
    "model_name": "Elantra",
    "car_type": "Sedan"
  },
  {
    "year": 2007,
    "manufacturer_name": "INFINITI",
    "model_name": "FX",
    "car_type": "SUV"
  },
  {
    "year": 2007,
    "manufacturer_name": "Jeep",
    "model_name": "Commander",
    "car_type": "SUV"
  },
  {
    "year": 2007,
    "manufacturer_name": "Isuzu",
    "model_name": "i-290 Extended Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2007,
    "manufacturer_name": "INFINITI",
    "model_name": "QX",
    "car_type": "SUV"
  },
  {
    "year": 2007,
    "manufacturer_name": "Isuzu",
    "model_name": "i-370 Crew Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2007,
    "manufacturer_name": "Jeep",
    "model_name": "Patriot",
    "car_type": "SUV"
  },
  {
    "year": 2007,
    "manufacturer_name": "Jaguar",
    "model_name": "S-Type",
    "car_type": "Sedan"
  },
  {
    "year": 2007,
    "manufacturer_name": "Jeep",
    "model_name": "Compass",
    "car_type": "SUV"
  },
  {
    "year": 2007,
    "manufacturer_name": "Jeep",
    "model_name": "Grand Cherokee",
    "car_type": "SUV"
  },
  {
    "year": 2007,
    "manufacturer_name": "Jeep",
    "model_name": "Wrangler",
    "car_type": "SUV"
  },
  {
    "year": 2007,
    "manufacturer_name": "Jaguar",
    "model_name": "XK",
    "car_type": "Coupe, Convertible"
  },
  {
    "year": 2007,
    "manufacturer_name": "Jaguar",
    "model_name": "X-Type",
    "car_type": "Sedan, Wagon"
  },
  {
    "year": 2007,
    "manufacturer_name": "Jeep",
    "model_name": "Liberty",
    "car_type": "SUV"
  },
  {
    "year": 2007,
    "manufacturer_name": "Jaguar",
    "model_name": "XJ",
    "car_type": "Sedan"
  },
  {
    "year": 2007,
    "manufacturer_name": "Isuzu",
    "model_name": "i-370 Extended Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2007,
    "manufacturer_name": "Kia",
    "model_name": "Amanti",
    "car_type": "Sedan"
  },
  {
    "year": 2007,
    "manufacturer_name": "Kia",
    "model_name": "Rondo",
    "car_type": "Wagon"
  },
  {
    "year": 2007,
    "manufacturer_name": "Kia",
    "model_name": "Rio",
    "car_type": "Sedan, Hatchback"
  },
  {
    "year": 2007,
    "manufacturer_name": "Land Rover",
    "model_name": "Range Rover",
    "car_type": "SUV"
  },
  {
    "year": 2007,
    "manufacturer_name": "Land Rover",
    "model_name": "LR3",
    "car_type": "SUV"
  },
  {
    "year": 2007,
    "manufacturer_name": "Lexus",
    "model_name": "ES",
    "car_type": "Sedan"
  },
  {
    "year": 2007,
    "manufacturer_name": "Lexus",
    "model_name": "GS",
    "car_type": "Sedan"
  },
  {
    "year": 2007,
    "manufacturer_name": "Lincoln",
    "model_name": "MKX",
    "car_type": "SUV"
  },
  {
    "year": 2007,
    "manufacturer_name": "Kia",
    "model_name": "Optima",
    "car_type": "Sedan"
  },
  {
    "year": 2007,
    "manufacturer_name": "Lexus",
    "model_name": "GX",
    "car_type": "SUV"
  },
  {
    "year": 2007,
    "manufacturer_name": "Kia",
    "model_name": "Sorento",
    "car_type": "SUV"
  },
  {
    "year": 2007,
    "manufacturer_name": "Lincoln",
    "model_name": "Navigator",
    "car_type": "SUV"
  },
  {
    "year": 2007,
    "manufacturer_name": "Lamborghini",
    "model_name": "Gallardo",
    "car_type": "Convertible, Coupe"
  },
  {
    "year": 2007,
    "manufacturer_name": "Land Rover",
    "model_name": "Range Rover Sport",
    "car_type": "SUV"
  },
  {
    "year": 2007,
    "manufacturer_name": "Kia",
    "model_name": "Spectra",
    "car_type": "Sedan, Hatchback"
  },
  {
    "year": 2007,
    "manufacturer_name": "Kia",
    "model_name": "Sedona",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2007,
    "manufacturer_name": "Lotus",
    "model_name": "Elise",
    "car_type": "Coupe"
  },
  {
    "year": 2007,
    "manufacturer_name": "Lamborghini",
    "model_name": "Murcielago",
    "car_type": "Convertible, Coupe"
  },
  {
    "year": 2007,
    "manufacturer_name": "Lotus",
    "model_name": "Exige S",
    "car_type": "Coupe"
  },
  {
    "year": 2007,
    "manufacturer_name": "Lincoln",
    "model_name": "Navigator L",
    "car_type": "SUV"
  },
  {
    "year": 2007,
    "manufacturer_name": "Kia",
    "model_name": "Sportage",
    "car_type": "SUV"
  },
  {
    "year": 2007,
    "manufacturer_name": "Lincoln",
    "model_name": "Mark LT",
    "car_type": "Pickup"
  },
  {
    "year": 2007,
    "manufacturer_name": "Lexus",
    "model_name": "LS",
    "car_type": "Sedan"
  },
  {
    "year": 2007,
    "manufacturer_name": "Lexus",
    "model_name": "LX",
    "car_type": "SUV"
  },
  {
    "year": 2007,
    "manufacturer_name": "Lincoln",
    "model_name": "Town Car",
    "car_type": "Sedan"
  },
  {
    "year": 2007,
    "manufacturer_name": "Lexus",
    "model_name": "SC",
    "car_type": "Convertible"
  },
  {
    "year": 2007,
    "manufacturer_name": "Lexus",
    "model_name": "IS",
    "car_type": "Sedan"
  },
  {
    "year": 2007,
    "manufacturer_name": "Maybach",
    "model_name": "57",
    "car_type": "Sedan"
  },
  {
    "year": 2007,
    "manufacturer_name": "Lincoln",
    "model_name": "MKZ",
    "car_type": "Sedan"
  },
  {
    "year": 2007,
    "manufacturer_name": "Lexus",
    "model_name": "RX",
    "car_type": "SUV"
  },
  {
    "year": 2007,
    "manufacturer_name": "MAZDA",
    "model_name": "RX-8",
    "car_type": "Coupe"
  },
  {
    "year": 2007,
    "manufacturer_name": "MAZDA",
    "model_name": "MAZDA3",
    "car_type": "Sedan, Hatchback"
  },
  {
    "year": 2007,
    "manufacturer_name": "MAZDA",
    "model_name": "CX-9",
    "car_type": "SUV"
  },
  {
    "year": 2007,
    "manufacturer_name": "Maybach",
    "model_name": "62",
    "car_type": "Sedan"
  },
  {
    "year": 2007,
    "manufacturer_name": "Mercedes-Benz",
    "model_name": "C-Class",
    "car_type": "Sedan"
  },
  {
    "year": 2007,
    "manufacturer_name": "Mercedes-Benz",
    "model_name": "E-Class",
    "car_type": "Sedan, Wagon"
  },
  {
    "year": 2007,
    "manufacturer_name": "Mercury",
    "model_name": "Mariner",
    "car_type": "SUV"
  },
  {
    "year": 2007,
    "manufacturer_name": "Mercury",
    "model_name": "Milan",
    "car_type": "Sedan"
  },
  {
    "year": 2007,
    "manufacturer_name": "MAZDA",
    "model_name": "MAZDA6",
    "car_type": "Sedan, Hatchback, Wagon"
  },
  {
    "year": 2007,
    "manufacturer_name": "MAZDA",
    "model_name": "MX-5 Miata",
    "car_type": "Convertible"
  },
  {
    "year": 2007,
    "manufacturer_name": "Mercedes-Benz",
    "model_name": "CLK-Class",
    "car_type": "Convertible, Coupe"
  },
  {
    "year": 2007,
    "manufacturer_name": "Mercedes-Benz",
    "model_name": "CLS-Class",
    "car_type": "Coupe"
  },
  {
    "year": 2007,
    "manufacturer_name": "Mercedes-Benz",
    "model_name": "S-Class",
    "car_type": "Sedan"
  },
  {
    "year": 2007,
    "manufacturer_name": "MAZDA",
    "model_name": "MAZDA5",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2007,
    "manufacturer_name": "Mercedes-Benz",
    "model_name": "G-Class",
    "car_type": "SUV"
  },
  {
    "year": 2007,
    "manufacturer_name": "Mercedes-Benz",
    "model_name": "SL-Class",
    "car_type": "Convertible"
  },
  {
    "year": 2007,
    "manufacturer_name": "MAZDA",
    "model_name": "B-Series Extended Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2007,
    "manufacturer_name": "MAZDA",
    "model_name": "CX-7",
    "car_type": "SUV"
  },
  {
    "year": 2007,
    "manufacturer_name": "MAZDA",
    "model_name": "B-Series Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2007,
    "manufacturer_name": "Mercedes-Benz",
    "model_name": "M-Class",
    "car_type": "SUV"
  },
  {
    "year": 2007,
    "manufacturer_name": "MINI",
    "model_name": "Convertible",
    "car_type": "Convertible"
  },
  {
    "year": 2007,
    "manufacturer_name": "MINI",
    "model_name": "Cooper",
    "car_type": "Hatchback"
  },
  {
    "year": 2007,
    "manufacturer_name": "Maserati",
    "model_name": "Quattroporte",
    "car_type": "Sedan"
  },
  {
    "year": 2007,
    "manufacturer_name": "Mercedes-Benz",
    "model_name": "CL-Class",
    "car_type": "Coupe"
  },
  {
    "year": 2007,
    "manufacturer_name": "Mitsubishi",
    "model_name": "Lancer",
    "car_type": "Sedan"
  },
  {
    "year": 2007,
    "manufacturer_name": "Mitsubishi",
    "model_name": "Raider Double Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2007,
    "manufacturer_name": "Mitsubishi",
    "model_name": "Eclipse",
    "car_type": "Convertible, Coupe"
  },
  {
    "year": 2007,
    "manufacturer_name": "Mercury",
    "model_name": "Montego",
    "car_type": "Sedan"
  },
  {
    "year": 2007,
    "manufacturer_name": "Mercedes-Benz",
    "model_name": "SLR McLaren",
    "car_type": "Coupe"
  },
  {
    "year": 2007,
    "manufacturer_name": "Mercury",
    "model_name": "Monterey",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2007,
    "manufacturer_name": "Mercury",
    "model_name": "Grand Marquis",
    "car_type": "Sedan"
  },
  {
    "year": 2007,
    "manufacturer_name": "Mitsubishi",
    "model_name": "Endeavor",
    "car_type": "SUV"
  },
  {
    "year": 2007,
    "manufacturer_name": "Mercedes-Benz",
    "model_name": "GL-Class",
    "car_type": "SUV"
  },
  {
    "year": 2007,
    "manufacturer_name": "Mercedes-Benz",
    "model_name": "R-Class",
    "car_type": "Wagon"
  },
  {
    "year": 2007,
    "manufacturer_name": "Mercedes-Benz",
    "model_name": "SLK-Class",
    "car_type": "Convertible"
  },
  {
    "year": 2007,
    "manufacturer_name": "Mitsubishi",
    "model_name": "Outlander",
    "car_type": "SUV"
  },
  {
    "year": 2007,
    "manufacturer_name": "Mercury",
    "model_name": "Mountaineer",
    "car_type": "SUV"
  },
  {
    "year": 2007,
    "manufacturer_name": "Mitsubishi",
    "model_name": "Galant",
    "car_type": "Sedan"
  },
  {
    "year": 2007,
    "manufacturer_name": "Mitsubishi",
    "model_name": "Raider Extended Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2007,
    "manufacturer_name": "Nissan",
    "model_name": "350Z",
    "car_type": "Coupe, Convertible"
  },
  {
    "year": 2007,
    "manufacturer_name": "Nissan",
    "model_name": "Altima",
    "car_type": "Sedan"
  },
  {
    "year": 2007,
    "manufacturer_name": "Nissan",
    "model_name": "Armada",
    "car_type": "SUV"
  },
  {
    "year": 2007,
    "manufacturer_name": "Nissan",
    "model_name": "Frontier Crew Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2007,
    "manufacturer_name": "Nissan",
    "model_name": "Murano",
    "car_type": "SUV"
  },
  {
    "year": 2007,
    "manufacturer_name": "Nissan",
    "model_name": "Frontier King Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2007,
    "manufacturer_name": "Nissan",
    "model_name": "Maxima",
    "car_type": "Sedan"
  },
  {
    "year": 2007,
    "manufacturer_name": "Saturn",
    "model_name": "Aura",
    "car_type": "Sedan"
  },
  {
    "year": 2007,
    "manufacturer_name": "Nissan",
    "model_name": "Quest",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2007,
    "manufacturer_name": "Nissan",
    "model_name": "Titan Crew Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2007,
    "manufacturer_name": "Nissan",
    "model_name": "Xterra",
    "car_type": "SUV"
  },
  {
    "year": 2007,
    "manufacturer_name": "Pontiac",
    "model_name": "Grand Prix",
    "car_type": "Sedan"
  },
  {
    "year": 2007,
    "manufacturer_name": "Saab",
    "model_name": "9-7X",
    "car_type": "SUV"
  },
  {
    "year": 2007,
    "manufacturer_name": "Nissan",
    "model_name": "Versa",
    "car_type": "Hatchback, Sedan"
  },
  {
    "year": 2007,
    "manufacturer_name": "Nissan",
    "model_name": "Titan King Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2007,
    "manufacturer_name": "Pontiac",
    "model_name": "G6",
    "car_type": "Sedan, Coupe, Convertible"
  },
  {
    "year": 2007,
    "manufacturer_name": "Nissan",
    "model_name": "Pathfinder",
    "car_type": "SUV"
  },
  {
    "year": 2007,
    "manufacturer_name": "Pontiac",
    "model_name": "Solstice",
    "car_type": "Convertible"
  },
  {
    "year": 2007,
    "manufacturer_name": "Nissan",
    "model_name": "Sentra",
    "car_type": "Sedan"
  },
  {
    "year": 2007,
    "manufacturer_name": "Pontiac",
    "model_name": "Torrent",
    "car_type": "SUV"
  },
  {
    "year": 2007,
    "manufacturer_name": "Porsche",
    "model_name": "911",
    "car_type": "Coupe, Convertible"
  },
  {
    "year": 2007,
    "manufacturer_name": "Pontiac",
    "model_name": "G5",
    "car_type": "Coupe"
  },
  {
    "year": 2007,
    "manufacturer_name": "Pontiac",
    "model_name": "Vibe",
    "car_type": "Hatchback"
  },
  {
    "year": 2007,
    "manufacturer_name": "Rolls-Royce",
    "model_name": "Phantom",
    "car_type": "Sedan"
  },
  {
    "year": 2007,
    "manufacturer_name": "Porsche",
    "model_name": "Cayman",
    "car_type": "Coupe"
  },
  {
    "year": 2007,
    "manufacturer_name": "Porsche",
    "model_name": "Boxster",
    "car_type": "Convertible"
  },
  {
    "year": 2007,
    "manufacturer_name": "Saab",
    "model_name": "3-Sep",
    "car_type": "Wagon, Sedan, Convertible"
  },
  {
    "year": 2007,
    "manufacturer_name": "Saturn",
    "model_name": "Relay",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2007,
    "manufacturer_name": "Scion",
    "model_name": "tC",
    "car_type": "Coupe"
  },
  {
    "year": 2007,
    "manufacturer_name": "Saturn",
    "model_name": "Ion",
    "car_type": "Sedan, Coupe"
  },
  {
    "year": 2007,
    "manufacturer_name": "Saab",
    "model_name": "5-Sep",
    "car_type": "Sedan, Wagon"
  },
  {
    "year": 2007,
    "manufacturer_name": "Saturn",
    "model_name": "Outlook",
    "car_type": "SUV"
  },
  {
    "year": 2007,
    "manufacturer_name": "Subaru",
    "model_name": "Legacy",
    "car_type": "Sedan, Wagon"
  },
  {
    "year": 2007,
    "manufacturer_name": "Saturn",
    "model_name": "VUE",
    "car_type": "SUV"
  },
  {
    "year": 2007,
    "manufacturer_name": "Saturn",
    "model_name": "SKY",
    "car_type": "Convertible"
  },
  {
    "year": 2007,
    "manufacturer_name": "Suzuki",
    "model_name": "SX4",
    "car_type": "Hatchback"
  },
  {
    "year": 2007,
    "manufacturer_name": "Subaru",
    "model_name": "Impreza",
    "car_type": "Sedan, Wagon"
  },
  {
    "year": 2007,
    "manufacturer_name": "Subaru",
    "model_name": "Forester",
    "car_type": "SUV"
  },
  {
    "year": 2007,
    "manufacturer_name": "Subaru",
    "model_name": "B9 Tribeca",
    "car_type": "SUV"
  },
  {
    "year": 2007,
    "manufacturer_name": "Toyota",
    "model_name": "Sequoia",
    "car_type": "SUV"
  },
  {
    "year": 2007,
    "manufacturer_name": "Suzuki",
    "model_name": "Aerio",
    "car_type": "Sedan"
  },
  {
    "year": 2007,
    "manufacturer_name": "Toyota",
    "model_name": "Prius",
    "car_type": "Hatchback"
  },
  {
    "year": 2007,
    "manufacturer_name": "Suzuki",
    "model_name": "XL7",
    "car_type": "SUV"
  },
  {
    "year": 2007,
    "manufacturer_name": "Toyota",
    "model_name": "Corolla",
    "car_type": "Sedan"
  },
  {
    "year": 2007,
    "manufacturer_name": "Suzuki",
    "model_name": "Forenza",
    "car_type": "Sedan, Wagon"
  },
  {
    "year": 2007,
    "manufacturer_name": "Toyota",
    "model_name": "Highlander",
    "car_type": "SUV"
  },
  {
    "year": 2007,
    "manufacturer_name": "Suzuki",
    "model_name": "Grand Vitara",
    "car_type": "SUV"
  },
  {
    "year": 2007,
    "manufacturer_name": "Suzuki",
    "model_name": "Reno",
    "car_type": "Hatchback"
  },
  {
    "year": 2007,
    "manufacturer_name": "Toyota",
    "model_name": "Solara",
    "car_type": "Convertible, Coupe"
  },
  {
    "year": 2007,
    "manufacturer_name": "Subaru",
    "model_name": "Outback",
    "car_type": "Wagon, Sedan"
  },
  {
    "year": 2007,
    "manufacturer_name": "Toyota",
    "model_name": "Tacoma Double Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2007,
    "manufacturer_name": "Toyota",
    "model_name": "FJ Cruiser",
    "car_type": "SUV"
  },
  {
    "year": 2007,
    "manufacturer_name": "Toyota",
    "model_name": "Tacoma Access Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2007,
    "manufacturer_name": "Toyota",
    "model_name": "Tacoma Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2007,
    "manufacturer_name": "Toyota",
    "model_name": "Camry",
    "car_type": "Sedan"
  },
  {
    "year": 2007,
    "manufacturer_name": "Toyota",
    "model_name": "RAV4",
    "car_type": "SUV"
  },
  {
    "year": 2007,
    "manufacturer_name": "Toyota",
    "model_name": "4Runner",
    "car_type": "SUV"
  },
  {
    "year": 2007,
    "manufacturer_name": "Toyota",
    "model_name": "Tundra Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2007,
    "manufacturer_name": "Toyota",
    "model_name": "Matrix",
    "car_type": "Wagon"
  },
  {
    "year": 2007,
    "manufacturer_name": "Toyota",
    "model_name": "Avalon",
    "car_type": "Sedan"
  },
  {
    "year": 2007,
    "manufacturer_name": "Toyota",
    "model_name": "Land Cruiser",
    "car_type": "SUV"
  },
  {
    "year": 2007,
    "manufacturer_name": "Toyota",
    "model_name": "Tundra Double Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2007,
    "manufacturer_name": "Volvo",
    "model_name": "XC70",
    "car_type": "Wagon"
  },
  {
    "year": 2007,
    "manufacturer_name": "Toyota",
    "model_name": "Yaris",
    "car_type": "Hatchback, Sedan"
  },
  {
    "year": 2007,
    "manufacturer_name": "Volkswagen",
    "model_name": "Eos",
    "car_type": "Convertible"
  },
  {
    "year": 2007,
    "manufacturer_name": "Volvo",
    "model_name": "S60",
    "car_type": "Sedan"
  },
  {
    "year": 2007,
    "manufacturer_name": "Volkswagen",
    "model_name": "Jetta",
    "car_type": "Sedan"
  },
  {
    "year": 2007,
    "manufacturer_name": "Volvo",
    "model_name": "C70",
    "car_type": "Convertible"
  },
  {
    "year": 2006,
    "manufacturer_name": "Acura",
    "model_name": "MDX",
    "car_type": "SUV"
  },
  {
    "year": 2007,
    "manufacturer_name": "Volkswagen",
    "model_name": "New Beetle",
    "car_type": "Hatchback, Convertible"
  },
  {
    "year": 2007,
    "manufacturer_name": "Volvo",
    "model_name": "V70",
    "car_type": "Wagon"
  },
  {
    "year": 2007,
    "manufacturer_name": "Toyota",
    "model_name": "Tundra CrewMax",
    "car_type": "Pickup"
  },
  {
    "year": 2007,
    "manufacturer_name": "Toyota",
    "model_name": "Sienna",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2007,
    "manufacturer_name": "Volvo",
    "model_name": "S40",
    "car_type": "Sedan"
  },
  {
    "year": 2007,
    "manufacturer_name": "Volkswagen",
    "model_name": "Passat",
    "car_type": "Sedan, Wagon"
  },
  {
    "year": 2007,
    "manufacturer_name": "Volkswagen",
    "model_name": "Rabbit",
    "car_type": "Hatchback"
  },
  {
    "year": 2007,
    "manufacturer_name": "Volvo",
    "model_name": "S80",
    "car_type": "Sedan"
  },
  {
    "year": 2006,
    "manufacturer_name": "Acura",
    "model_name": "TSX",
    "car_type": "Sedan"
  },
  {
    "year": 2006,
    "manufacturer_name": "Bentley",
    "model_name": "Continental",
    "car_type": "Sedan, Coupe"
  },
  {
    "year": 2007,
    "manufacturer_name": "Volvo",
    "model_name": "XC90",
    "car_type": "SUV"
  },
  {
    "year": 2006,
    "manufacturer_name": "Acura",
    "model_name": "TL",
    "car_type": "Sedan"
  },
  {
    "year": 2006,
    "manufacturer_name": "BMW",
    "model_name": "6 Series",
    "car_type": "Coupe, Convertible"
  },
  {
    "year": 2007,
    "manufacturer_name": "Volkswagen",
    "model_name": "GTI",
    "car_type": "Hatchback"
  },
  {
    "year": 2006,
    "manufacturer_name": "Aston Martin",
    "model_name": "Vanquish S",
    "car_type": "Coupe"
  },
  {
    "year": 2006,
    "manufacturer_name": "Aston Martin",
    "model_name": "Vantage",
    "car_type": "Coupe"
  },
  {
    "year": 2006,
    "manufacturer_name": "Acura",
    "model_name": "RL",
    "car_type": "Sedan"
  },
  {
    "year": 2006,
    "manufacturer_name": "Audi",
    "model_name": "A8",
    "car_type": "Sedan"
  },
  {
    "year": 2006,
    "manufacturer_name": "Aston Martin",
    "model_name": "DB9",
    "car_type": "Convertible, Coupe"
  },
  {
    "year": 2006,
    "manufacturer_name": "Audi",
    "model_name": "A6",
    "car_type": "Sedan, Wagon"
  },
  {
    "year": 2006,
    "manufacturer_name": "Audi",
    "model_name": "A3",
    "car_type": "Wagon"
  },
  {
    "year": 2006,
    "manufacturer_name": "Audi",
    "model_name": "A4",
    "car_type": "Convertible, Sedan, Wagon"
  },
  {
    "year": 2007,
    "manufacturer_name": "Volkswagen",
    "model_name": "Touareg",
    "car_type": "SUV"
  },
  {
    "year": 2006,
    "manufacturer_name": "Audi",
    "model_name": "S4",
    "car_type": "Sedan, Wagon, Convertible"
  },
  {
    "year": 2006,
    "manufacturer_name": "BMW",
    "model_name": "5 Series",
    "car_type": "Sedan, Wagon"
  },
  {
    "year": 2006,
    "manufacturer_name": "Audi",
    "model_name": "TT",
    "car_type": "Coupe, Convertible"
  },
  {
    "year": 2006,
    "manufacturer_name": "Acura",
    "model_name": "RSX",
    "car_type": "Coupe"
  },
  {
    "year": 2006,
    "manufacturer_name": "Bentley",
    "model_name": "Arnage",
    "car_type": "Sedan"
  },
  {
    "year": 2007,
    "manufacturer_name": "Volvo",
    "model_name": "V50",
    "car_type": "Wagon"
  },
  {
    "year": 2006,
    "manufacturer_name": "BMW",
    "model_name": "3 Series",
    "car_type": "Coupe, Sedan, Convertible, Wagon"
  },
  {
    "year": 2006,
    "manufacturer_name": "BMW",
    "model_name": "7 Series",
    "car_type": "Sedan"
  },
  {
    "year": 2006,
    "manufacturer_name": "BMW",
    "model_name": "M3",
    "car_type": "Convertible, Coupe"
  },
  {
    "year": 2006,
    "manufacturer_name": "Buick",
    "model_name": "Lucerne",
    "car_type": "Sedan"
  },
  {
    "year": 2006,
    "manufacturer_name": "Buick",
    "model_name": "LaCrosse",
    "car_type": "Sedan"
  },
  {
    "year": 2006,
    "manufacturer_name": "Chevrolet",
    "model_name": "Aveo",
    "car_type": "Hatchback, Sedan"
  },
  {
    "year": 2006,
    "manufacturer_name": "BMW",
    "model_name": "Z4 M",
    "car_type": "Convertible, Coupe"
  },
  {
    "year": 2006,
    "manufacturer_name": "Cadillac",
    "model_name": "SRX",
    "car_type": "SUV"
  },
  {
    "year": 2006,
    "manufacturer_name": "Chevrolet",
    "model_name": "Colorado Crew Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2006,
    "manufacturer_name": "Chevrolet",
    "model_name": "Cobalt",
    "car_type": "Coupe, Sedan"
  },
  {
    "year": 2006,
    "manufacturer_name": "Cadillac",
    "model_name": "CTS",
    "car_type": "Sedan"
  },
  {
    "year": 2006,
    "manufacturer_name": "BMW",
    "model_name": "M6",
    "car_type": "Coupe"
  },
  {
    "year": 2006,
    "manufacturer_name": "Cadillac",
    "model_name": "Escalade ESV",
    "car_type": "SUV"
  },
  {
    "year": 2006,
    "manufacturer_name": "Buick",
    "model_name": "Rainier",
    "car_type": "SUV"
  },
  {
    "year": 2006,
    "manufacturer_name": "BMW",
    "model_name": "X3",
    "car_type": "SUV"
  },
  {
    "year": 2006,
    "manufacturer_name": "BMW",
    "model_name": "M5",
    "car_type": "Sedan"
  },
  {
    "year": 2006,
    "manufacturer_name": "BMW",
    "model_name": "X5",
    "car_type": "SUV"
  },
  {
    "year": 2006,
    "manufacturer_name": "Cadillac",
    "model_name": "Escalade",
    "car_type": "SUV"
  },
  {
    "year": 2006,
    "manufacturer_name": "Buick",
    "model_name": "Terraza",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2006,
    "manufacturer_name": "Chevrolet",
    "model_name": "Avalanche 2500",
    "car_type": "Pickup"
  },
  {
    "year": 2006,
    "manufacturer_name": "Chevrolet",
    "model_name": "Express 3500 Passenger",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2006,
    "manufacturer_name": "Chevrolet",
    "model_name": "Express 2500 Passenger",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2006,
    "manufacturer_name": "Cadillac",
    "model_name": "STS",
    "car_type": "Sedan"
  },
  {
    "year": 2006,
    "manufacturer_name": "Chevrolet",
    "model_name": "Express 1500 Passenger",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2006,
    "manufacturer_name": "Chevrolet",
    "model_name": "Malibu",
    "car_type": "Sedan, Hatchback"
  },
  {
    "year": 2006,
    "manufacturer_name": "Chevrolet",
    "model_name": "Express 1500 Cargo",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2006,
    "manufacturer_name": "Chevrolet",
    "model_name": "Colorado Extended Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2006,
    "manufacturer_name": "Chevrolet",
    "model_name": "Express 2500 Cargo",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2006,
    "manufacturer_name": "Chevrolet",
    "model_name": "Express 3500 Cargo",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2006,
    "manufacturer_name": "Chevrolet",
    "model_name": "Corvette",
    "car_type": "Coupe, Convertible"
  },
  {
    "year": 2006,
    "manufacturer_name": "Cadillac",
    "model_name": "XLR",
    "car_type": "Convertible"
  },
  {
    "year": 2006,
    "manufacturer_name": "Chevrolet",
    "model_name": "Silverado 2500 HD Crew Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2006,
    "manufacturer_name": "Chevrolet",
    "model_name": "Monte Carlo",
    "car_type": "Coupe"
  },
  {
    "year": 2006,
    "manufacturer_name": "Cadillac",
    "model_name": "Escalade EXT",
    "car_type": "Pickup"
  },
  {
    "year": 2006,
    "manufacturer_name": "BMW",
    "model_name": "Z4",
    "car_type": "Convertible, Coupe"
  },
  {
    "year": 2006,
    "manufacturer_name": "Chevrolet",
    "model_name": "HHR",
    "car_type": "Wagon"
  },
  {
    "year": 2006,
    "manufacturer_name": "Chevrolet",
    "model_name": "Colorado Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2006,
    "manufacturer_name": "Chevrolet",
    "model_name": "Silverado 1500 Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2006,
    "manufacturer_name": "Chevrolet",
    "model_name": "Impala",
    "car_type": "Sedan"
  },
  {
    "year": 2006,
    "manufacturer_name": "Buick",
    "model_name": "Rendezvous",
    "car_type": "SUV"
  },
  {
    "year": 2006,
    "manufacturer_name": "Chevrolet",
    "model_name": "Silverado 1500 Extended Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2006,
    "manufacturer_name": "Cadillac",
    "model_name": "DTS",
    "car_type": "Sedan"
  },
  {
    "year": 2006,
    "manufacturer_name": "Chevrolet",
    "model_name": "Equinox",
    "car_type": "SUV"
  },
  {
    "year": 2006,
    "manufacturer_name": "Chevrolet",
    "model_name": "Avalanche 1500",
    "car_type": "Pickup"
  },
  {
    "year": 2006,
    "manufacturer_name": "Chevrolet",
    "model_name": "Silverado 2500 HD Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2006,
    "manufacturer_name": "Chevrolet",
    "model_name": "Uplander Passenger",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2006,
    "manufacturer_name": "Chevrolet",
    "model_name": "SSR",
    "car_type": "Pickup"
  },
  {
    "year": 2006,
    "manufacturer_name": "Chrysler",
    "model_name": "Crossfire",
    "car_type": "Coupe, Convertible"
  },
  {
    "year": 2006,
    "manufacturer_name": "Chevrolet",
    "model_name": "Silverado 2500 HD Extended Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2006,
    "manufacturer_name": "Chevrolet",
    "model_name": "Silverado 1500 Crew Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2006,
    "manufacturer_name": "Chevrolet",
    "model_name": "Silverado 3500 Crew Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2006,
    "manufacturer_name": "Chevrolet",
    "model_name": "Silverado 3500 Extended Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2006,
    "manufacturer_name": "Chrysler",
    "model_name": "Pacifica",
    "car_type": "Wagon"
  },
  {
    "year": 2006,
    "manufacturer_name": "Chevrolet",
    "model_name": "Silverado 3500 Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2006,
    "manufacturer_name": "Chevrolet",
    "model_name": "Suburban 1500",
    "car_type": "SUV"
  },
  {
    "year": 2006,
    "manufacturer_name": "Chevrolet",
    "model_name": "Silverado 1500 HD Crew Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2006,
    "manufacturer_name": "Chevrolet",
    "model_name": "Tahoe",
    "car_type": "SUV"
  },
  {
    "year": 2006,
    "manufacturer_name": "Chevrolet",
    "model_name": "TrailBlazer",
    "car_type": "SUV"
  },
  {
    "year": 2006,
    "manufacturer_name": "Chevrolet",
    "model_name": "Suburban 2500",
    "car_type": "SUV"
  },
  {
    "year": 2006,
    "manufacturer_name": "Dodge",
    "model_name": "Caravan Cargo",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2006,
    "manufacturer_name": "Chrysler",
    "model_name": "Sebring",
    "car_type": "Sedan, Convertible"
  },
  {
    "year": 2006,
    "manufacturer_name": "Dodge",
    "model_name": "Sprinter 3500 Cargo",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2006,
    "manufacturer_name": "Dodge",
    "model_name": "Charger",
    "car_type": "Sedan"
  },
  {
    "year": 2006,
    "manufacturer_name": "Chrysler",
    "model_name": "Town & Country",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2006,
    "manufacturer_name": "Dodge",
    "model_name": "Caravan Passenger",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2006,
    "manufacturer_name": "Dodge",
    "model_name": "Ram 3500 Mega Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2006,
    "manufacturer_name": "Chrysler",
    "model_name": "300",
    "car_type": "Sedan"
  },
  {
    "year": 2006,
    "manufacturer_name": "Dodge",
    "model_name": "Grand Caravan Passenger",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2006,
    "manufacturer_name": "Chrysler",
    "model_name": "PT Cruiser",
    "car_type": "Wagon, Convertible"
  },
  {
    "year": 2006,
    "manufacturer_name": "Dodge",
    "model_name": "Dakota Club Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2006,
    "manufacturer_name": "Dodge",
    "model_name": "Grand Caravan Cargo",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2006,
    "manufacturer_name": "Dodge",
    "model_name": "Ram 2500 Mega Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2006,
    "manufacturer_name": "Chevrolet",
    "model_name": "Uplander Cargo",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2006,
    "manufacturer_name": "Dodge",
    "model_name": "Durango",
    "car_type": "SUV"
  },
  {
    "year": 2006,
    "manufacturer_name": "Dodge",
    "model_name": "Sprinter 2500 Cargo",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2006,
    "manufacturer_name": "Dodge",
    "model_name": "Magnum",
    "car_type": "Wagon"
  },
  {
    "year": 2006,
    "manufacturer_name": "Dodge",
    "model_name": "Ram 3500 Quad Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2006,
    "manufacturer_name": "Dodge",
    "model_name": "Ram 1500 Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2006,
    "manufacturer_name": "Dodge",
    "model_name": "Ram 2500 Quad Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2006,
    "manufacturer_name": "Dodge",
    "model_name": "Ram 1500 Quad Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2006,
    "manufacturer_name": "Dodge",
    "model_name": "Dakota Quad Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2006,
    "manufacturer_name": "Dodge",
    "model_name": "Ram 2500 Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2006,
    "manufacturer_name": "Dodge",
    "model_name": "Stratus",
    "car_type": "Sedan"
  },
  {
    "year": 2006,
    "manufacturer_name": "Ford",
    "model_name": "Crown Victoria",
    "car_type": "Sedan"
  },
  {
    "year": 2006,
    "manufacturer_name": "Dodge",
    "model_name": "Ram 1500 Mega Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2006,
    "manufacturer_name": "Ferrari",
    "model_name": "F430",
    "car_type": "Convertible, Coupe"
  },
  {
    "year": 2006,
    "manufacturer_name": "Ford",
    "model_name": "Explorer",
    "car_type": "SUV"
  },
  {
    "year": 2006,
    "manufacturer_name": "Ford",
    "model_name": "F150 SuperCrew Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2006,
    "manufacturer_name": "Ford",
    "model_name": "Escape",
    "car_type": "SUV"
  },
  {
    "year": 2006,
    "manufacturer_name": "Dodge",
    "model_name": "Ram 3500 Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2006,
    "manufacturer_name": "Dodge",
    "model_name": "Sprinter 2500 Passenger",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2006,
    "manufacturer_name": "Ford",
    "model_name": "E150 Super Duty Passenger",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2006,
    "manufacturer_name": "Ford",
    "model_name": "E150 Super Duty Cargo",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2006,
    "manufacturer_name": "Dodge",
    "model_name": "Viper",
    "car_type": "Coupe, Convertible"
  },
  {
    "year": 2006,
    "manufacturer_name": "Ferrari",
    "model_name": "612 Scaglietti",
    "car_type": "Coupe"
  },
  {
    "year": 2006,
    "manufacturer_name": "Ford",
    "model_name": "E350 Super Duty Passenger",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2006,
    "manufacturer_name": "Ford",
    "model_name": "F150 Super Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2006,
    "manufacturer_name": "Ford",
    "model_name": "E350 Super Duty Cargo",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2006,
    "manufacturer_name": "Ford",
    "model_name": "Expedition",
    "car_type": "SUV"
  },
  {
    "year": 2006,
    "manufacturer_name": "Ford",
    "model_name": "E250 Super Duty Cargo",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2006,
    "manufacturer_name": "Ford",
    "model_name": "F150 Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2006,
    "manufacturer_name": "Ford",
    "model_name": "F250 Super Duty Crew Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2006,
    "manufacturer_name": "GMC",
    "model_name": "Savana 1500 Passenger",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2006,
    "manufacturer_name": "Ford",
    "model_name": "Fusion",
    "car_type": "Sedan"
  },
  {
    "year": 2006,
    "manufacturer_name": "Ford",
    "model_name": "F350 Super Duty Super Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2006,
    "manufacturer_name": "Ford",
    "model_name": "Five Hundred",
    "car_type": "Sedan"
  },
  {
    "year": 2006,
    "manufacturer_name": "Ford",
    "model_name": "Mustang",
    "car_type": "Coupe, Convertible"
  },
  {
    "year": 2006,
    "manufacturer_name": "Ford",
    "model_name": "F350 Super Duty Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2006,
    "manufacturer_name": "GMC",
    "model_name": "Canyon Crew Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2006,
    "manufacturer_name": "Ford",
    "model_name": "F250 Super Duty Super Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2006,
    "manufacturer_name": "Ford",
    "model_name": "Freestar Cargo",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2006,
    "manufacturer_name": "Ford",
    "model_name": "F350 Super Duty Crew Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2006,
    "manufacturer_name": "Ford",
    "model_name": "F250 Super Duty Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2006,
    "manufacturer_name": "Ford",
    "model_name": "Ranger Super Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2006,
    "manufacturer_name": "Ford",
    "model_name": "Taurus",
    "car_type": "Sedan"
  },
  {
    "year": 2006,
    "manufacturer_name": "GMC",
    "model_name": "Canyon Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2006,
    "manufacturer_name": "GMC",
    "model_name": "Canyon Extended Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2006,
    "manufacturer_name": "Ford",
    "model_name": "Ranger Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2006,
    "manufacturer_name": "Ford",
    "model_name": "GT",
    "car_type": "Coupe"
  },
  {
    "year": 2006,
    "manufacturer_name": "Ford",
    "model_name": "Freestyle",
    "car_type": "SUV"
  },
  {
    "year": 2006,
    "manufacturer_name": "Ford",
    "model_name": "Focus",
    "car_type": "Hatchback, Sedan, Wagon"
  },
  {
    "year": 2006,
    "manufacturer_name": "Ford",
    "model_name": "Freestar Passenger",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2006,
    "manufacturer_name": "GMC",
    "model_name": "Savana 1500 Cargo",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2006,
    "manufacturer_name": "GMC",
    "model_name": "Sierra 2500 HD Crew Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2006,
    "manufacturer_name": "GMC",
    "model_name": "Envoy XL",
    "car_type": "SUV"
  },
  {
    "year": 2006,
    "manufacturer_name": "GMC",
    "model_name": "Savana 2500 Cargo",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2006,
    "manufacturer_name": "GMC",
    "model_name": "Envoy",
    "car_type": "SUV"
  },
  {
    "year": 2006,
    "manufacturer_name": "GMC",
    "model_name": "Savana 3500 Passenger",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2006,
    "manufacturer_name": "GMC",
    "model_name": "Sierra 1500 Extended Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2006,
    "manufacturer_name": "GMC",
    "model_name": "Yukon XL 2500",
    "car_type": "SUV"
  },
  {
    "year": 2006,
    "manufacturer_name": "GMC",
    "model_name": "Sierra 2500 HD Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2006,
    "manufacturer_name": "Honda",
    "model_name": "Pilot",
    "car_type": "SUV"
  },
  {
    "year": 2006,
    "manufacturer_name": "GMC",
    "model_name": "Yukon",
    "car_type": "SUV"
  },
  {
    "year": 2006,
    "manufacturer_name": "GMC",
    "model_name": "Savana 3500 Cargo",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2006,
    "manufacturer_name": "GMC",
    "model_name": "Sierra 3500 Crew Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2006,
    "manufacturer_name": "GMC",
    "model_name": "Sierra 1500 Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2006,
    "manufacturer_name": "GMC",
    "model_name": "Sierra 2500 HD Extended Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2006,
    "manufacturer_name": "GMC",
    "model_name": "Savana 2500 Passenger",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2006,
    "manufacturer_name": "GMC",
    "model_name": "Sierra 1500 HD Crew Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2006,
    "manufacturer_name": "Honda",
    "model_name": "Accord",
    "car_type": "Sedan, Coupe"
  },
  {
    "year": 2006,
    "manufacturer_name": "GMC",
    "model_name": "Sierra 1500 Crew Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2006,
    "manufacturer_name": "GMC",
    "model_name": "Yukon XL 1500",
    "car_type": "SUV"
  },
  {
    "year": 2006,
    "manufacturer_name": "GMC",
    "model_name": "Sierra 3500 Extended Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2006,
    "manufacturer_name": "Honda",
    "model_name": "Element",
    "car_type": "SUV"
  },
  {
    "year": 2006,
    "manufacturer_name": "Honda",
    "model_name": "Civic",
    "car_type": "Sedan, Coupe"
  },
  {
    "year": 2006,
    "manufacturer_name": "Honda",
    "model_name": "Ridgeline",
    "car_type": "Pickup"
  },
  {
    "year": 2006,
    "manufacturer_name": "Honda",
    "model_name": "CR-V",
    "car_type": "SUV"
  },
  {
    "year": 2006,
    "manufacturer_name": "GMC",
    "model_name": "Sierra 3500 Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2006,
    "manufacturer_name": "HUMMER",
    "model_name": "H3",
    "car_type": "SUV"
  },
  {
    "year": 2006,
    "manufacturer_name": "Honda",
    "model_name": "S2000",
    "car_type": "Convertible"
  },
  {
    "year": 2006,
    "manufacturer_name": "Honda",
    "model_name": "Insight",
    "car_type": "Hatchback"
  },
  {
    "year": 2006,
    "manufacturer_name": "HUMMER",
    "model_name": "H1",
    "car_type": "Wagon, SUV"
  },
  {
    "year": 2006,
    "manufacturer_name": "Hyundai",
    "model_name": "Accent",
    "car_type": "Sedan"
  },
  {
    "year": 2006,
    "manufacturer_name": "Honda",
    "model_name": "Odyssey",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2006,
    "manufacturer_name": "Hyundai",
    "model_name": "Sonata",
    "car_type": "Sedan"
  },
  {
    "year": 2006,
    "manufacturer_name": "Jeep",
    "model_name": "Commander",
    "car_type": "SUV"
  },
  {
    "year": 2006,
    "manufacturer_name": "INFINITI",
    "model_name": "Q",
    "car_type": "Sedan"
  },
  {
    "year": 2006,
    "manufacturer_name": "Isuzu",
    "model_name": "i-350 Crew Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2006,
    "manufacturer_name": "Hyundai",
    "model_name": "Elantra",
    "car_type": "Hatchback, Sedan"
  },
  {
    "year": 2006,
    "manufacturer_name": "Isuzu",
    "model_name": "i-280 Extended Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2006,
    "manufacturer_name": "INFINITI",
    "model_name": "G",
    "car_type": "Coupe, Sedan"
  },
  {
    "year": 2006,
    "manufacturer_name": "Hyundai",
    "model_name": "Tucson",
    "car_type": "SUV"
  },
  {
    "year": 2006,
    "manufacturer_name": "INFINITI",
    "model_name": "QX",
    "car_type": "SUV"
  },
  {
    "year": 2006,
    "manufacturer_name": "Jaguar",
    "model_name": "X-Type",
    "car_type": "Sedan, Wagon"
  },
  {
    "year": 2006,
    "manufacturer_name": "HUMMER",
    "model_name": "H2",
    "car_type": "SUV, Pickup"
  },
  {
    "year": 2006,
    "manufacturer_name": "Jaguar",
    "model_name": "S-Type",
    "car_type": "Sedan"
  },
  {
    "year": 2006,
    "manufacturer_name": "Hyundai",
    "model_name": "Tiburon",
    "car_type": "Coupe"
  },
  {
    "year": 2006,
    "manufacturer_name": "INFINITI",
    "model_name": "M",
    "car_type": "Sedan"
  },
  {
    "year": 2006,
    "manufacturer_name": "Kia",
    "model_name": "Optima",
    "car_type": "Sedan"
  },
  {
    "year": 2006,
    "manufacturer_name": "INFINITI",
    "model_name": "FX",
    "car_type": "SUV"
  },
  {
    "year": 2006,
    "manufacturer_name": "Jeep",
    "model_name": "Wrangler",
    "car_type": "SUV"
  },
  {
    "year": 2006,
    "manufacturer_name": "Jaguar",
    "model_name": "XK",
    "car_type": "Coupe, Convertible"
  },
  {
    "year": 2006,
    "manufacturer_name": "Hyundai",
    "model_name": "Santa Fe",
    "car_type": "SUV"
  },
  {
    "year": 2006,
    "manufacturer_name": "Hyundai",
    "model_name": "Azera",
    "car_type": "Sedan"
  },
  {
    "year": 2006,
    "manufacturer_name": "Kia",
    "model_name": "Optima (2006.5)",
    "car_type": "Sedan"
  },
  {
    "year": 2006,
    "manufacturer_name": "Jaguar",
    "model_name": "XJ",
    "car_type": "Sedan"
  },
  {
    "year": 2006,
    "manufacturer_name": "Jeep",
    "model_name": "Grand Cherokee",
    "car_type": "SUV"
  },
  {
    "year": 2006,
    "manufacturer_name": "Isuzu",
    "model_name": "Ascender",
    "car_type": "SUV"
  },
  {
    "year": 2006,
    "manufacturer_name": "Kia",
    "model_name": "Amanti",
    "car_type": "Sedan"
  },
  {
    "year": 2006,
    "manufacturer_name": "Kia",
    "model_name": "Sedona",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2006,
    "manufacturer_name": "Lamborghini",
    "model_name": "Murcielago",
    "car_type": "Convertible, Coupe"
  },
  {
    "year": 2006,
    "manufacturer_name": "Lexus",
    "model_name": "GX",
    "car_type": "SUV"
  },
  {
    "year": 2006,
    "manufacturer_name": "Land Rover",
    "model_name": "LR3",
    "car_type": "SUV"
  },
  {
    "year": 2006,
    "manufacturer_name": "Kia",
    "model_name": "Sorento",
    "car_type": "SUV"
  },
  {
    "year": 2006,
    "manufacturer_name": "Kia",
    "model_name": "Sportage",
    "car_type": "SUV"
  },
  {
    "year": 2006,
    "manufacturer_name": "Lamborghini",
    "model_name": "Gallardo",
    "car_type": "Coupe, Convertible"
  },
  {
    "year": 2006,
    "manufacturer_name": "Kia",
    "model_name": "Spectra",
    "car_type": "Sedan, Hatchback"
  },
  {
    "year": 2006,
    "manufacturer_name": "Jeep",
    "model_name": "Liberty",
    "car_type": "SUV"
  },
  {
    "year": 2006,
    "manufacturer_name": "Lexus",
    "model_name": "LS",
    "car_type": "Sedan"
  },
  {
    "year": 2006,
    "manufacturer_name": "Kia",
    "model_name": "Rio",
    "car_type": "Sedan, Hatchback"
  },
  {
    "year": 2006,
    "manufacturer_name": "Land Rover",
    "model_name": "Range Rover Sport",
    "car_type": "SUV"
  },
  {
    "year": 2006,
    "manufacturer_name": "Land Rover",
    "model_name": "Range Rover",
    "car_type": "SUV"
  },
  {
    "year": 2006,
    "manufacturer_name": "Lexus",
    "model_name": "GS",
    "car_type": "Sedan"
  },
  {
    "year": 2006,
    "manufacturer_name": "Lexus",
    "model_name": "LX",
    "car_type": "SUV"
  },
  {
    "year": 2006,
    "manufacturer_name": "Lexus",
    "model_name": "IS",
    "car_type": "Sedan"
  },
  {
    "year": 2006,
    "manufacturer_name": "Lincoln",
    "model_name": "Navigator",
    "car_type": "SUV"
  },
  {
    "year": 2006,
    "manufacturer_name": "Lexus",
    "model_name": "SC",
    "car_type": "Convertible"
  },
  {
    "year": 2006,
    "manufacturer_name": "Lexus",
    "model_name": "RX",
    "car_type": "SUV"
  },
  {
    "year": 2006,
    "manufacturer_name": "Lincoln",
    "model_name": "Mark LT",
    "car_type": "Pickup"
  },
  {
    "year": 2006,
    "manufacturer_name": "Lincoln",
    "model_name": "LS",
    "car_type": "Sedan"
  },
  {
    "year": 2006,
    "manufacturer_name": "Lexus",
    "model_name": "ES",
    "car_type": "Sedan"
  },
  {
    "year": 2006,
    "manufacturer_name": "Lincoln",
    "model_name": "Town Car",
    "car_type": "Sedan"
  },
  {
    "year": 2006,
    "manufacturer_name": "Lotus",
    "model_name": "Exige",
    "car_type": "Coupe"
  },
  {
    "year": 2006,
    "manufacturer_name": "MAZDA",
    "model_name": "RX-8",
    "car_type": "Coupe"
  },
  {
    "year": 2006,
    "manufacturer_name": "MAZDA",
    "model_name": "MX-5 Miata",
    "car_type": "Convertible"
  },
  {
    "year": 2006,
    "manufacturer_name": "Maserati",
    "model_name": "GranSport",
    "car_type": "Coupe, Convertible"
  },
  {
    "year": 2006,
    "manufacturer_name": "Lincoln",
    "model_name": "Zephyr",
    "car_type": "Sedan"
  },
  {
    "year": 2006,
    "manufacturer_name": "MAZDA",
    "model_name": "MAZDA6",
    "car_type": "Sedan, Hatchback, Wagon"
  },
  {
    "year": 2006,
    "manufacturer_name": "MAZDA",
    "model_name": "B-Series Extended Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2006,
    "manufacturer_name": "MAZDA",
    "model_name": "MAZDA5",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2006,
    "manufacturer_name": "Maserati",
    "model_name": "Coupe",
    "car_type": "Coupe"
  },
  {
    "year": 2006,
    "manufacturer_name": "Lotus",
    "model_name": "Elise",
    "car_type": "Coupe"
  },
  {
    "year": 2006,
    "manufacturer_name": "MAZDA",
    "model_name": "MPV",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2006,
    "manufacturer_name": "Maserati",
    "model_name": "Quattroporte",
    "car_type": "Sedan"
  },
  {
    "year": 2006,
    "manufacturer_name": "Maybach",
    "model_name": "57",
    "car_type": "Sedan"
  },
  {
    "year": 2006,
    "manufacturer_name": "Maybach",
    "model_name": "62",
    "car_type": "Sedan"
  },
  {
    "year": 2006,
    "manufacturer_name": "MAZDA",
    "model_name": "MAZDA3",
    "car_type": "Sedan, Hatchback"
  },
  {
    "year": 2006,
    "manufacturer_name": "MAZDA",
    "model_name": "Tribute",
    "car_type": "SUV"
  },
  {
    "year": 2006,
    "manufacturer_name": "MAZDA",
    "model_name": "B-Series Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2006,
    "manufacturer_name": "Mercedes-Benz",
    "model_name": "CL-Class",
    "car_type": "Coupe"
  },
  {
    "year": 2006,
    "manufacturer_name": "Mercedes-Benz",
    "model_name": "G-Class",
    "car_type": "SUV"
  },
  {
    "year": 2006,
    "manufacturer_name": "Mercedes-Benz",
    "model_name": "C-Class",
    "car_type": "Sedan"
  },
  {
    "year": 2006,
    "manufacturer_name": "Mercury",
    "model_name": "Monterey",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2006,
    "manufacturer_name": "Mitsubishi",
    "model_name": "Lancer",
    "car_type": "Sedan"
  },
  {
    "year": 2006,
    "manufacturer_name": "Mercedes-Benz",
    "model_name": "E-Class",
    "car_type": "Sedan, Wagon"
  },
  {
    "year": 2006,
    "manufacturer_name": "Mercedes-Benz",
    "model_name": "M-Class",
    "car_type": "SUV"
  },
  {
    "year": 2006,
    "manufacturer_name": "Mercury",
    "model_name": "Grand Marquis",
    "car_type": "Sedan"
  },
  {
    "year": 2006,
    "manufacturer_name": "Mercedes-Benz",
    "model_name": "SLK-Class",
    "car_type": "Convertible"
  },
  {
    "year": 2006,
    "manufacturer_name": "Mercury",
    "model_name": "Mountaineer",
    "car_type": "SUV"
  },
  {
    "year": 2006,
    "manufacturer_name": "MINI",
    "model_name": "Cooper",
    "car_type": "Hatchback"
  },
  {
    "year": 2006,
    "manufacturer_name": "Mercedes-Benz",
    "model_name": "CLS-Class",
    "car_type": "Coupe"
  },
  {
    "year": 2006,
    "manufacturer_name": "Mitsubishi",
    "model_name": "Montero",
    "car_type": "SUV"
  },
  {
    "year": 2006,
    "manufacturer_name": "Mercury",
    "model_name": "Mariner",
    "car_type": "SUV"
  },
  {
    "year": 2006,
    "manufacturer_name": "Mercedes-Benz",
    "model_name": "CLK-Class",
    "car_type": "Coupe, Convertible"
  },
  {
    "year": 2006,
    "manufacturer_name": "Nissan",
    "model_name": "Armada",
    "car_type": "SUV"
  },
  {
    "year": 2006,
    "manufacturer_name": "MINI",
    "model_name": "Convertible",
    "car_type": "Convertible"
  },
  {
    "year": 2006,
    "manufacturer_name": "Mercedes-Benz",
    "model_name": "SL-Class",
    "car_type": "Convertible"
  },
  {
    "year": 2006,
    "manufacturer_name": "Mercedes-Benz",
    "model_name": "SLR McLaren",
    "car_type": "Coupe"
  },
  {
    "year": 2006,
    "manufacturer_name": "Mitsubishi",
    "model_name": "Galant",
    "car_type": "Sedan"
  },
  {
    "year": 2006,
    "manufacturer_name": "Mitsubishi",
    "model_name": "Raider Double Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2006,
    "manufacturer_name": "Mitsubishi",
    "model_name": "Raider Extended Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2006,
    "manufacturer_name": "Mitsubishi",
    "model_name": "Eclipse",
    "car_type": "Coupe"
  },
  {
    "year": 2006,
    "manufacturer_name": "Nissan",
    "model_name": "350Z",
    "car_type": "Convertible, Coupe"
  },
  {
    "year": 2006,
    "manufacturer_name": "Mercedes-Benz",
    "model_name": "R-Class",
    "car_type": "Wagon"
  },
  {
    "year": 2006,
    "manufacturer_name": "Nissan",
    "model_name": "Pathfinder",
    "car_type": "SUV"
  },
  {
    "year": 2006,
    "manufacturer_name": "Mitsubishi",
    "model_name": "Outlander",
    "car_type": "SUV"
  },
  {
    "year": 2006,
    "manufacturer_name": "Nissan",
    "model_name": "Altima",
    "car_type": "Sedan"
  },
  {
    "year": 2006,
    "manufacturer_name": "Mercedes-Benz",
    "model_name": "S-Class",
    "car_type": "Sedan"
  },
  {
    "year": 2006,
    "manufacturer_name": "Nissan",
    "model_name": "Frontier Crew Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2006,
    "manufacturer_name": "Mercury",
    "model_name": "Montego",
    "car_type": "Sedan"
  },
  {
    "year": 2006,
    "manufacturer_name": "Mercury",
    "model_name": "Milan",
    "car_type": "Sedan"
  },
  {
    "year": 2006,
    "manufacturer_name": "Mitsubishi",
    "model_name": "Endeavor",
    "car_type": "SUV"
  },
  {
    "year": 2006,
    "manufacturer_name": "Nissan",
    "model_name": "Xterra",
    "car_type": "SUV"
  },
  {
    "year": 2006,
    "manufacturer_name": "Pontiac",
    "model_name": "G6",
    "car_type": "Coupe, Convertible, Sedan"
  },
  {
    "year": 2006,
    "manufacturer_name": "Nissan",
    "model_name": "Murano",
    "car_type": "SUV"
  },
  {
    "year": 2006,
    "manufacturer_name": "Nissan",
    "model_name": "Sentra",
    "car_type": "Sedan"
  },
  {
    "year": 2006,
    "manufacturer_name": "Nissan",
    "model_name": "Frontier King Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2006,
    "manufacturer_name": "Nissan",
    "model_name": "Quest",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2006,
    "manufacturer_name": "Panoz",
    "model_name": "Esperante",
    "car_type": "Coupe, Convertible"
  },
  {
    "year": 2006,
    "manufacturer_name": "Pontiac",
    "model_name": "GTO",
    "car_type": "Coupe"
  },
  {
    "year": 2006,
    "manufacturer_name": "Nissan",
    "model_name": "Maxima",
    "car_type": "Sedan"
  },
  {
    "year": 2006,
    "manufacturer_name": "Nissan",
    "model_name": "Titan King Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2006,
    "manufacturer_name": "Pontiac",
    "model_name": "Montana SV6",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2006,
    "manufacturer_name": "Nissan",
    "model_name": "Titan Crew Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2006,
    "manufacturer_name": "Pontiac",
    "model_name": "Solstice",
    "car_type": "Convertible"
  },
  {
    "year": 2006,
    "manufacturer_name": "Porsche",
    "model_name": "Cayman",
    "car_type": "Coupe"
  },
  {
    "year": 2006,
    "manufacturer_name": "Saturn",
    "model_name": "VUE",
    "car_type": "SUV"
  },
  {
    "year": 2006,
    "manufacturer_name": "Subaru",
    "model_name": "Baja",
    "car_type": "Pickup"
  },
  {
    "year": 2006,
    "manufacturer_name": "Saab",
    "model_name": "3-Sep",
    "car_type": "Sedan, Convertible, Wagon"
  },
  {
    "year": 2006,
    "manufacturer_name": "Pontiac",
    "model_name": "Vibe",
    "car_type": "Wagon"
  },
  {
    "year": 2006,
    "manufacturer_name": "Saturn",
    "model_name": "Ion",
    "car_type": "Sedan, Coupe"
  },
  {
    "year": 2006,
    "manufacturer_name": "Scion",
    "model_name": "xA",
    "car_type": "Hatchback"
  },
  {
    "year": 2006,
    "manufacturer_name": "Porsche",
    "model_name": "911",
    "car_type": "Coupe, Convertible"
  },
  {
    "year": 2006,
    "manufacturer_name": "Pontiac",
    "model_name": "Torrent",
    "car_type": "SUV"
  },
  {
    "year": 2006,
    "manufacturer_name": "Scion",
    "model_name": "xB",
    "car_type": "Hatchback"
  },
  {
    "year": 2006,
    "manufacturer_name": "Saab",
    "model_name": "5-Sep",
    "car_type": "Sedan, Wagon"
  },
  {
    "year": 2006,
    "manufacturer_name": "Porsche",
    "model_name": "Boxster",
    "car_type": "Convertible"
  },
  {
    "year": 2006,
    "manufacturer_name": "Saturn",
    "model_name": "Relay",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2006,
    "manufacturer_name": "Pontiac",
    "model_name": "Grand Prix",
    "car_type": "Sedan"
  },
  {
    "year": 2006,
    "manufacturer_name": "Subaru",
    "model_name": "B9 Tribeca",
    "car_type": "SUV"
  },
  {
    "year": 2006,
    "manufacturer_name": "Rolls-Royce",
    "model_name": "Phantom",
    "car_type": "Sedan"
  },
  {
    "year": 2006,
    "manufacturer_name": "Saab",
    "model_name": "9-2X",
    "car_type": "Wagon"
  },
  {
    "year": 2006,
    "manufacturer_name": "Subaru",
    "model_name": "Forester",
    "car_type": "SUV"
  },
  {
    "year": 2006,
    "manufacturer_name": "Porsche",
    "model_name": "Cayenne",
    "car_type": "SUV"
  },
  {
    "year": 2006,
    "manufacturer_name": "Scion",
    "model_name": "tC",
    "car_type": "Coupe"
  },
  {
    "year": 2006,
    "manufacturer_name": "Saab",
    "model_name": "9-7X",
    "car_type": "SUV"
  },
  {
    "year": 2006,
    "manufacturer_name": "Suzuki",
    "model_name": "Grand Vitara",
    "car_type": "SUV"
  },
  {
    "year": 2006,
    "manufacturer_name": "Subaru",
    "model_name": "Outback",
    "car_type": "Sedan, Wagon"
  },
  {
    "year": 2006,
    "manufacturer_name": "Toyota",
    "model_name": "Avalon",
    "car_type": "Sedan"
  },
  {
    "year": 2006,
    "manufacturer_name": "Suzuki",
    "model_name": "XL-7",
    "car_type": "SUV"
  },
  {
    "year": 2006,
    "manufacturer_name": "Toyota",
    "model_name": "Corolla",
    "car_type": "Sedan"
  },
  {
    "year": 2006,
    "manufacturer_name": "Subaru",
    "model_name": "Impreza",
    "car_type": "Wagon, Sedan"
  },
  {
    "year": 2006,
    "manufacturer_name": "Suzuki",
    "model_name": "Forenza",
    "car_type": "Sedan, Wagon"
  },
  {
    "year": 2006,
    "manufacturer_name": "Subaru",
    "model_name": "Legacy",
    "car_type": "Wagon, Sedan"
  },
  {
    "year": 2006,
    "manufacturer_name": "Suzuki",
    "model_name": "Aerio",
    "car_type": "Sedan, Wagon"
  },
  {
    "year": 2006,
    "manufacturer_name": "Suzuki",
    "model_name": "Reno",
    "car_type": "Hatchback"
  },
  {
    "year": 2006,
    "manufacturer_name": "Toyota",
    "model_name": "Camry",
    "car_type": "Sedan"
  },
  {
    "year": 2006,
    "manufacturer_name": "Suzuki",
    "model_name": "Verona",
    "car_type": "Sedan"
  },
  {
    "year": 2006,
    "manufacturer_name": "Toyota",
    "model_name": "4Runner",
    "car_type": "SUV"
  },
  {
    "year": 2006,
    "manufacturer_name": "Toyota",
    "model_name": "Highlander",
    "car_type": "SUV"
  },
  {
    "year": 2006,
    "manufacturer_name": "Toyota",
    "model_name": "Land Cruiser",
    "car_type": "SUV"
  },
  {
    "year": 2006,
    "manufacturer_name": "Toyota",
    "model_name": "Matrix",
    "car_type": "Wagon"
  },
  {
    "year": 2006,
    "manufacturer_name": "Toyota",
    "model_name": "RAV4",
    "car_type": "SUV"
  },
  {
    "year": 2006,
    "manufacturer_name": "Toyota",
    "model_name": "Tundra Double Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2006,
    "manufacturer_name": "Toyota",
    "model_name": "Sienna",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2006,
    "manufacturer_name": "Volkswagen",
    "model_name": "New Beetle",
    "car_type": "Hatchback, Convertible"
  },
  {
    "year": 2006,
    "manufacturer_name": "Toyota",
    "model_name": "Sequoia",
    "car_type": "SUV"
  },
  {
    "year": 2006,
    "manufacturer_name": "Toyota",
    "model_name": "Tacoma Access Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2006,
    "manufacturer_name": "Volkswagen",
    "model_name": "Rabbit",
    "car_type": "Hatchback"
  },
  {
    "year": 2006,
    "manufacturer_name": "Toyota",
    "model_name": "Prius",
    "car_type": "Hatchback"
  },
  {
    "year": 2006,
    "manufacturer_name": "Toyota",
    "model_name": "Tundra Access Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2006,
    "manufacturer_name": "Toyota",
    "model_name": "Tacoma Double Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2006,
    "manufacturer_name": "Toyota",
    "model_name": "Tundra Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2006,
    "manufacturer_name": "Volkswagen",
    "model_name": "Golf",
    "car_type": "Hatchback"
  },
  {
    "year": 2006,
    "manufacturer_name": "Toyota",
    "model_name": "Solara",
    "car_type": "Coupe, Convertible"
  },
  {
    "year": 2006,
    "manufacturer_name": "Toyota",
    "model_name": "Tacoma Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2006,
    "manufacturer_name": "Volkswagen",
    "model_name": "GTI",
    "car_type": "Hatchback"
  },
  {
    "year": 2006,
    "manufacturer_name": "Volkswagen",
    "model_name": "Jetta",
    "car_type": "Sedan"
  },
  {
    "year": 2006,
    "manufacturer_name": "Volvo",
    "model_name": "XC70",
    "car_type": "Wagon"
  },
  {
    "year": 2006,
    "manufacturer_name": "Volvo",
    "model_name": "S60",
    "car_type": "Sedan"
  },
  {
    "year": 2006,
    "manufacturer_name": "Volkswagen",
    "model_name": "Passat",
    "car_type": "Sedan"
  },
  {
    "year": 2006,
    "manufacturer_name": "Volvo",
    "model_name": "XC90",
    "car_type": "SUV"
  },
  {
    "year": 2006,
    "manufacturer_name": "Volvo",
    "model_name": "V50",
    "car_type": "Wagon"
  },
  {
    "year": 2006,
    "manufacturer_name": "Volvo",
    "model_name": "V70",
    "car_type": "Wagon"
  },
  {
    "year": 2005,
    "manufacturer_name": "Audi",
    "model_name": "A4",
    "car_type": "Convertible, Wagon, Sedan"
  },
  {
    "year": 2005,
    "manufacturer_name": "Acura",
    "model_name": "TL",
    "car_type": "Sedan"
  },
  {
    "year": 2005,
    "manufacturer_name": "Acura",
    "model_name": "RSX",
    "car_type": "Coupe"
  },
  {
    "year": 2006,
    "manufacturer_name": "Volvo",
    "model_name": "S40",
    "car_type": "Sedan"
  },
  {
    "year": 2005,
    "manufacturer_name": "Aston Martin",
    "model_name": "Vanquish S",
    "car_type": "Coupe"
  },
  {
    "year": 2005,
    "manufacturer_name": "Audi",
    "model_name": "A4 (2005.5)",
    "car_type": "Sedan, Wagon"
  },
  {
    "year": 2006,
    "manufacturer_name": "Volkswagen",
    "model_name": "Phaeton",
    "car_type": "Sedan"
  },
  {
    "year": 2006,
    "manufacturer_name": "Volvo",
    "model_name": "S80",
    "car_type": "Sedan"
  },
  {
    "year": 2005,
    "manufacturer_name": "Acura",
    "model_name": "MDX",
    "car_type": "SUV"
  },
  {
    "year": 2006,
    "manufacturer_name": "Volkswagen",
    "model_name": "Touareg",
    "car_type": "SUV"
  },
  {
    "year": 2006,
    "manufacturer_name": "Volvo",
    "model_name": "C70",
    "car_type": "Convertible"
  },
  {
    "year": 2005,
    "manufacturer_name": "Audi",
    "model_name": "A6",
    "car_type": "Sedan"
  },
  {
    "year": 2005,
    "manufacturer_name": "Aston Martin",
    "model_name": "DB9",
    "car_type": "Convertible, Coupe"
  },
  {
    "year": 2005,
    "manufacturer_name": "Acura",
    "model_name": "NSX",
    "car_type": "Coupe"
  },
  {
    "year": 2005,
    "manufacturer_name": "Acura",
    "model_name": "RL",
    "car_type": "Sedan"
  },
  {
    "year": 2005,
    "manufacturer_name": "Audi",
    "model_name": "A8",
    "car_type": "Sedan"
  },
  {
    "year": 2005,
    "manufacturer_name": "Acura",
    "model_name": "TSX",
    "car_type": "Sedan"
  },
  {
    "year": 2005,
    "manufacturer_name": "Buick",
    "model_name": "Century",
    "car_type": "Sedan"
  },
  {
    "year": 2005,
    "manufacturer_name": "Bentley",
    "model_name": "Arnage",
    "car_type": "Sedan"
  },
  {
    "year": 2005,
    "manufacturer_name": "Audi",
    "model_name": "TT",
    "car_type": "Coupe, Convertible"
  },
  {
    "year": 2005,
    "manufacturer_name": "Audi",
    "model_name": "allroad",
    "car_type": "Wagon"
  },
  {
    "year": 2005,
    "manufacturer_name": "Buick",
    "model_name": "Rainier",
    "car_type": "SUV"
  },
  {
    "year": 2005,
    "manufacturer_name": "BMW",
    "model_name": "3 Series",
    "car_type": "Sedan, Coupe, Convertible, Wagon"
  },
  {
    "year": 2005,
    "manufacturer_name": "BMW",
    "model_name": "7 Series",
    "car_type": "Sedan"
  },
  {
    "year": 2005,
    "manufacturer_name": "BMW",
    "model_name": "M3",
    "car_type": "Coupe, Convertible"
  },
  {
    "year": 2005,
    "manufacturer_name": "BMW",
    "model_name": "Z4",
    "car_type": "Convertible"
  },
  {
    "year": 2005,
    "manufacturer_name": "Audi",
    "model_name": "S4 (2005.5)",
    "car_type": "Sedan, Wagon"
  },
  {
    "year": 2005,
    "manufacturer_name": "BMW",
    "model_name": "X5",
    "car_type": "SUV"
  },
  {
    "year": 2005,
    "manufacturer_name": "Audi",
    "model_name": "S4",
    "car_type": "Convertible, Wagon, Sedan"
  },
  {
    "year": 2005,
    "manufacturer_name": "BMW",
    "model_name": "6 Series",
    "car_type": "Coupe, Convertible"
  },
  {
    "year": 2005,
    "manufacturer_name": "Bentley",
    "model_name": "Continental",
    "car_type": "Coupe, Sedan"
  },
  {
    "year": 2005,
    "manufacturer_name": "BMW",
    "model_name": "X3",
    "car_type": "SUV"
  },
  {
    "year": 2005,
    "manufacturer_name": "BMW",
    "model_name": "5 Series",
    "car_type": "Sedan"
  },
  {
    "year": 2005,
    "manufacturer_name": "Chevrolet",
    "model_name": "Blazer",
    "car_type": "SUV"
  },
  {
    "year": 2005,
    "manufacturer_name": "Cadillac",
    "model_name": "Escalade ESV",
    "car_type": "SUV"
  },
  {
    "year": 2005,
    "manufacturer_name": "Chevrolet",
    "model_name": "Aveo",
    "car_type": "Sedan, Hatchback"
  },
  {
    "year": 2005,
    "manufacturer_name": "Buick",
    "model_name": "Park Avenue",
    "car_type": "Sedan"
  },
  {
    "year": 2005,
    "manufacturer_name": "Chevrolet",
    "model_name": "Astro Cargo",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2005,
    "manufacturer_name": "Cadillac",
    "model_name": "Escalade",
    "car_type": "SUV"
  },
  {
    "year": 2005,
    "manufacturer_name": "Cadillac",
    "model_name": "DeVille",
    "car_type": "Sedan"
  },
  {
    "year": 2005,
    "manufacturer_name": "Buick",
    "model_name": "LaCrosse",
    "car_type": "Sedan"
  },
  {
    "year": 2005,
    "manufacturer_name": "Buick",
    "model_name": "Rendezvous",
    "car_type": "SUV"
  },
  {
    "year": 2005,
    "manufacturer_name": "Buick",
    "model_name": "LeSabre",
    "car_type": "Sedan"
  },
  {
    "year": 2005,
    "manufacturer_name": "Chevrolet",
    "model_name": "Avalanche 2500",
    "car_type": "Pickup"
  },
  {
    "year": 2005,
    "manufacturer_name": "Chevrolet",
    "model_name": "Cobalt",
    "car_type": "Sedan, Coupe"
  },
  {
    "year": 2005,
    "manufacturer_name": "Chevrolet",
    "model_name": "Colorado Crew Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2005,
    "manufacturer_name": "Cadillac",
    "model_name": "Escalade EXT",
    "car_type": "Pickup"
  },
  {
    "year": 2005,
    "manufacturer_name": "Chevrolet",
    "model_name": "Avalanche 1500",
    "car_type": "Pickup"
  },
  {
    "year": 2005,
    "manufacturer_name": "Buick",
    "model_name": "Terraza",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2005,
    "manufacturer_name": "Cadillac",
    "model_name": "STS",
    "car_type": "Sedan"
  },
  {
    "year": 2005,
    "manufacturer_name": "Chevrolet",
    "model_name": "Classic",
    "car_type": "Sedan"
  },
  {
    "year": 2005,
    "manufacturer_name": "Cadillac",
    "model_name": "XLR",
    "car_type": "Convertible"
  },
  {
    "year": 2005,
    "manufacturer_name": "Cadillac",
    "model_name": "CTS",
    "car_type": "Sedan"
  },
  {
    "year": 2005,
    "manufacturer_name": "Cadillac",
    "model_name": "SRX",
    "car_type": "SUV"
  },
  {
    "year": 2005,
    "manufacturer_name": "Chevrolet",
    "model_name": "Astro Passenger",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2005,
    "manufacturer_name": "Chevrolet",
    "model_name": "Colorado Extended Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2005,
    "manufacturer_name": "Chevrolet",
    "model_name": "Cavalier",
    "car_type": "Sedan, Coupe"
  },
  {
    "year": 2005,
    "manufacturer_name": "Chevrolet",
    "model_name": "Monte Carlo",
    "car_type": "Coupe"
  },
  {
    "year": 2005,
    "manufacturer_name": "Chevrolet",
    "model_name": "Express 2500 Cargo",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2005,
    "manufacturer_name": "Chevrolet",
    "model_name": "Express 3500 Cargo",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2005,
    "manufacturer_name": "Chevrolet",
    "model_name": "Colorado Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2005,
    "manufacturer_name": "Chevrolet",
    "model_name": "Silverado 2500 HD Crew Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2005,
    "manufacturer_name": "Chevrolet",
    "model_name": "Silverado 2500 HD Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2005,
    "manufacturer_name": "Chevrolet",
    "model_name": "Express 1500 Passenger",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2005,
    "manufacturer_name": "Chevrolet",
    "model_name": "Express 2500 Passenger",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2005,
    "manufacturer_name": "Chevrolet",
    "model_name": "Malibu",
    "car_type": "Sedan, Hatchback"
  },
  {
    "year": 2005,
    "manufacturer_name": "Chevrolet",
    "model_name": "Corvette",
    "car_type": "Coupe, Convertible"
  },
  {
    "year": 2005,
    "manufacturer_name": "Chevrolet",
    "model_name": "Impala",
    "car_type": "Sedan"
  },
  {
    "year": 2005,
    "manufacturer_name": "Chevrolet",
    "model_name": "Express 3500 Passenger",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2005,
    "manufacturer_name": "Chevrolet",
    "model_name": "Express 1500 Cargo",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2005,
    "manufacturer_name": "Chevrolet",
    "model_name": "Silverado 1500 Extended Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2005,
    "manufacturer_name": "Chevrolet",
    "model_name": "Silverado 3500 Crew Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2005,
    "manufacturer_name": "Chevrolet",
    "model_name": "Silverado 1500 Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2005,
    "manufacturer_name": "Chevrolet",
    "model_name": "Silverado 1500 HD Crew Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2005,
    "manufacturer_name": "Chevrolet",
    "model_name": "Silverado 2500 HD Extended Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2005,
    "manufacturer_name": "Chevrolet",
    "model_name": "Silverado 1500 Crew Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2005,
    "manufacturer_name": "Chevrolet",
    "model_name": "Equinox",
    "car_type": "SUV"
  },
  {
    "year": 2005,
    "manufacturer_name": "Chevrolet",
    "model_name": "SSR",
    "car_type": "Pickup"
  },
  {
    "year": 2005,
    "manufacturer_name": "Chevrolet",
    "model_name": "Silverado 3500 Extended Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2005,
    "manufacturer_name": "Chevrolet",
    "model_name": "Suburban 2500",
    "car_type": "SUV"
  },
  {
    "year": 2005,
    "manufacturer_name": "Dodge",
    "model_name": "Ram 1500 Quad Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2005,
    "manufacturer_name": "Chevrolet",
    "model_name": "Tahoe",
    "car_type": "SUV"
  },
  {
    "year": 2005,
    "manufacturer_name": "Dodge",
    "model_name": "Magnum",
    "car_type": "Wagon"
  },
  {
    "year": 2005,
    "manufacturer_name": "Chevrolet",
    "model_name": "Suburban 1500",
    "car_type": "SUV"
  },
  {
    "year": 2005,
    "manufacturer_name": "Chevrolet",
    "model_name": "Uplander Cargo",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2005,
    "manufacturer_name": "Chevrolet",
    "model_name": "Uplander Passenger",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2005,
    "manufacturer_name": "Dodge",
    "model_name": "Durango",
    "car_type": "SUV"
  },
  {
    "year": 2005,
    "manufacturer_name": "Chevrolet",
    "model_name": "Venture Passenger",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2005,
    "manufacturer_name": "Chrysler",
    "model_name": "PT Cruiser",
    "car_type": "Wagon, Convertible"
  },
  {
    "year": 2005,
    "manufacturer_name": "Chevrolet",
    "model_name": "Silverado 3500 Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2005,
    "manufacturer_name": "Chevrolet",
    "model_name": "Venture Cargo",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2005,
    "manufacturer_name": "Dodge",
    "model_name": "Ram 1500 Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2005,
    "manufacturer_name": "Chevrolet",
    "model_name": "TrailBlazer",
    "car_type": "SUV"
  },
  {
    "year": 2005,
    "manufacturer_name": "Dodge",
    "model_name": "Caravan Passenger",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2005,
    "manufacturer_name": "Chrysler",
    "model_name": "Pacifica",
    "car_type": "Wagon"
  },
  {
    "year": 2005,
    "manufacturer_name": "Dodge",
    "model_name": "Ram 2500 Quad Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2005,
    "manufacturer_name": "Dodge",
    "model_name": "Dakota Quad Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2005,
    "manufacturer_name": "Chrysler",
    "model_name": "Sebring",
    "car_type": "Coupe, Sedan, Convertible"
  },
  {
    "year": 2005,
    "manufacturer_name": "Dodge",
    "model_name": "Dakota Club Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2005,
    "manufacturer_name": "Chrysler",
    "model_name": "300",
    "car_type": "Sedan"
  },
  {
    "year": 2005,
    "manufacturer_name": "Dodge",
    "model_name": "Ram 2500 Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2005,
    "manufacturer_name": "Chrysler",
    "model_name": "Town & Country",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2005,
    "manufacturer_name": "Dodge",
    "model_name": "Grand Caravan Passenger",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2005,
    "manufacturer_name": "Chrysler",
    "model_name": "Crossfire",
    "car_type": "Coupe, Convertible"
  },
  {
    "year": 2005,
    "manufacturer_name": "Dodge",
    "model_name": "Caravan Cargo",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2005,
    "manufacturer_name": "Dodge",
    "model_name": "Grand Caravan Cargo",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2005,
    "manufacturer_name": "Dodge",
    "model_name": "Neon",
    "car_type": "Sedan"
  },
  {
    "year": 2005,
    "manufacturer_name": "Ford",
    "model_name": "Escape",
    "car_type": "SUV"
  },
  {
    "year": 2005,
    "manufacturer_name": "Ford",
    "model_name": "Crown Victoria",
    "car_type": "Sedan"
  },
  {
    "year": 2005,
    "manufacturer_name": "Dodge",
    "model_name": "Sprinter 3500 Cargo",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2005,
    "manufacturer_name": "Dodge",
    "model_name": "Sprinter 2500 Passenger",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2005,
    "manufacturer_name": "Ford",
    "model_name": "E150 Super Duty Cargo",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2005,
    "manufacturer_name": "Dodge",
    "model_name": "Stratus",
    "car_type": "Sedan, Coupe"
  },
  {
    "year": 2005,
    "manufacturer_name": "Ford",
    "model_name": "E350 Super Duty Passenger",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2005,
    "manufacturer_name": "Dodge",
    "model_name": "Ram 3500 Quad Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2005,
    "manufacturer_name": "Dodge",
    "model_name": "Ram 3500 Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2005,
    "manufacturer_name": "Ford",
    "model_name": "Excursion",
    "car_type": "SUV"
  },
  {
    "year": 2005,
    "manufacturer_name": "Dodge",
    "model_name": "Sprinter 2500 Cargo",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2005,
    "manufacturer_name": "Ford",
    "model_name": "E150 Super Duty Passenger",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2005,
    "manufacturer_name": "Dodge",
    "model_name": "Viper",
    "car_type": "Convertible"
  },
  {
    "year": 2005,
    "manufacturer_name": "Ford",
    "model_name": "Freestyle",
    "car_type": "SUV"
  },
  {
    "year": 2005,
    "manufacturer_name": "Ford",
    "model_name": "Ranger Super Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2005,
    "manufacturer_name": "Ford",
    "model_name": "Five Hundred",
    "car_type": "Sedan"
  },
  {
    "year": 2005,
    "manufacturer_name": "GMC",
    "model_name": "Canyon Extended Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2005,
    "manufacturer_name": "Ford",
    "model_name": "Ranger Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2005,
    "manufacturer_name": "Ford",
    "model_name": "F250 Super Duty Crew Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2005,
    "manufacturer_name": "Ford",
    "model_name": "F150 Super Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2005,
    "manufacturer_name": "Ford",
    "model_name": "F250 Super Duty Super Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2005,
    "manufacturer_name": "Ford",
    "model_name": "Expedition",
    "car_type": "SUV"
  },
  {
    "year": 2005,
    "manufacturer_name": "Ford",
    "model_name": "Explorer Sport Trac",
    "car_type": "SUV"
  },
  {
    "year": 2005,
    "manufacturer_name": "Ford",
    "model_name": "F150 Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2005,
    "manufacturer_name": "Ford",
    "model_name": "E250 Super Duty Cargo",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2005,
    "manufacturer_name": "Ford",
    "model_name": "Mustang",
    "car_type": "Coupe, Convertible"
  },
  {
    "year": 2005,
    "manufacturer_name": "Ford",
    "model_name": "F350 Super Duty Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2005,
    "manufacturer_name": "Ford",
    "model_name": "E350 Super Duty Cargo",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2005,
    "manufacturer_name": "GMC",
    "model_name": "Envoy XUV",
    "car_type": "SUV"
  },
  {
    "year": 2005,
    "manufacturer_name": "Ford",
    "model_name": "Freestar Cargo",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2005,
    "manufacturer_name": "Ford",
    "model_name": "F350 Super Duty Crew Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2005,
    "manufacturer_name": "Ford",
    "model_name": "Focus",
    "car_type": "Hatchback, Sedan, Wagon"
  },
  {
    "year": 2005,
    "manufacturer_name": "Ford",
    "model_name": "Taurus",
    "car_type": "Sedan, Wagon"
  },
  {
    "year": 2005,
    "manufacturer_name": "Ford",
    "model_name": "Explorer",
    "car_type": "SUV"
  },
  {
    "year": 2005,
    "manufacturer_name": "Ford",
    "model_name": "Freestar Passenger",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2005,
    "manufacturer_name": "Ford",
    "model_name": "F150 SuperCrew Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2005,
    "manufacturer_name": "Ford",
    "model_name": "F250 Super Duty Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2005,
    "manufacturer_name": "Ford",
    "model_name": "GT",
    "car_type": "Coupe"
  },
  {
    "year": 2005,
    "manufacturer_name": "Ford",
    "model_name": "F350 Super Duty Super Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2005,
    "manufacturer_name": "GMC",
    "model_name": "Envoy XL",
    "car_type": "SUV"
  },
  {
    "year": 2005,
    "manufacturer_name": "GMC",
    "model_name": "Safari Cargo",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2005,
    "manufacturer_name": "GMC",
    "model_name": "Canyon Crew Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2005,
    "manufacturer_name": "Ford",
    "model_name": "Thunderbird",
    "car_type": "Convertible"
  },
  {
    "year": 2005,
    "manufacturer_name": "GMC",
    "model_name": "Savana 2500 Cargo",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2005,
    "manufacturer_name": "GMC",
    "model_name": "Sierra 1500 Extended Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2005,
    "manufacturer_name": "GMC",
    "model_name": "Safari Passenger",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2005,
    "manufacturer_name": "GMC",
    "model_name": "Envoy",
    "car_type": "SUV"
  },
  {
    "year": 2005,
    "manufacturer_name": "GMC",
    "model_name": "Canyon Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2005,
    "manufacturer_name": "GMC",
    "model_name": "Sierra 1500 HD Crew Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2005,
    "manufacturer_name": "GMC",
    "model_name": "Savana 2500 Passenger",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2005,
    "manufacturer_name": "GMC",
    "model_name": "Savana 1500 Passenger",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2005,
    "manufacturer_name": "GMC",
    "model_name": "Sierra 2500 HD Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2005,
    "manufacturer_name": "GMC",
    "model_name": "Sierra 1500 Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2005,
    "manufacturer_name": "GMC",
    "model_name": "Savana 3500 Passenger",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2005,
    "manufacturer_name": "Honda",
    "model_name": "Element",
    "car_type": "SUV"
  },
  {
    "year": 2005,
    "manufacturer_name": "GMC",
    "model_name": "Yukon XL 2500",
    "car_type": "SUV"
  },
  {
    "year": 2005,
    "manufacturer_name": "GMC",
    "model_name": "Sierra 3500 Crew Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2005,
    "manufacturer_name": "GMC",
    "model_name": "Sierra 1500 Crew Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2005,
    "manufacturer_name": "Honda",
    "model_name": "Insight",
    "car_type": "Hatchback"
  },
  {
    "year": 2005,
    "manufacturer_name": "GMC",
    "model_name": "Savana 1500 Cargo",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2005,
    "manufacturer_name": "GMC",
    "model_name": "Yukon XL 1500",
    "car_type": "SUV"
  },
  {
    "year": 2005,
    "manufacturer_name": "GMC",
    "model_name": "Sierra 2500 HD Crew Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2005,
    "manufacturer_name": "Honda",
    "model_name": "Accord",
    "car_type": "Sedan, Coupe"
  },
  {
    "year": 2005,
    "manufacturer_name": "GMC",
    "model_name": "Yukon",
    "car_type": "SUV"
  },
  {
    "year": 2005,
    "manufacturer_name": "GMC",
    "model_name": "Savana 3500 Cargo",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2005,
    "manufacturer_name": "Honda",
    "model_name": "Civic",
    "car_type": "Coupe, Sedan, Hatchback"
  },
  {
    "year": 2005,
    "manufacturer_name": "GMC",
    "model_name": "Sierra 3500 Extended Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2005,
    "manufacturer_name": "GMC",
    "model_name": "Sierra 2500 HD Extended Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2005,
    "manufacturer_name": "GMC",
    "model_name": "Sierra 3500 Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2005,
    "manufacturer_name": "Honda",
    "model_name": "CR-V",
    "car_type": "SUV"
  },
  {
    "year": 2005,
    "manufacturer_name": "Honda",
    "model_name": "Pilot",
    "car_type": "SUV"
  },
  {
    "year": 2005,
    "manufacturer_name": "Hyundai",
    "model_name": "XG350",
    "car_type": "Sedan"
  },
  {
    "year": 2005,
    "manufacturer_name": "INFINITI",
    "model_name": "FX",
    "car_type": "SUV"
  },
  {
    "year": 2005,
    "manufacturer_name": "Jeep",
    "model_name": "Liberty",
    "car_type": "SUV"
  },
  {
    "year": 2005,
    "manufacturer_name": "Kia",
    "model_name": "Optima",
    "car_type": "Sedan"
  },
  {
    "year": 2005,
    "manufacturer_name": "HUMMER",
    "model_name": "H2",
    "car_type": "SUV, Pickup"
  },
  {
    "year": 2005,
    "manufacturer_name": "Honda",
    "model_name": "S2000",
    "car_type": "Convertible"
  },
  {
    "year": 2005,
    "manufacturer_name": "Honda",
    "model_name": "Odyssey",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2005,
    "manufacturer_name": "Hyundai",
    "model_name": "Elantra",
    "car_type": "Hatchback, Sedan"
  },
  {
    "year": 2005,
    "manufacturer_name": "Jaguar",
    "model_name": "XK",
    "car_type": "Coupe, Convertible"
  },
  {
    "year": 2005,
    "manufacturer_name": "Isuzu",
    "model_name": "Ascender",
    "car_type": "SUV"
  },
  {
    "year": 2005,
    "manufacturer_name": "Jaguar",
    "model_name": "S-Type",
    "car_type": "Sedan"
  },
  {
    "year": 2005,
    "manufacturer_name": "Kia",
    "model_name": "Sedona",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2005,
    "manufacturer_name": "INFINITI",
    "model_name": "QX",
    "car_type": "SUV"
  },
  {
    "year": 2005,
    "manufacturer_name": "Hyundai",
    "model_name": "Santa Fe",
    "car_type": "SUV"
  },
  {
    "year": 2005,
    "manufacturer_name": "INFINITI",
    "model_name": "Q",
    "car_type": "Sedan"
  },
  {
    "year": 2005,
    "manufacturer_name": "Kia",
    "model_name": "Amanti",
    "car_type": "Sedan"
  },
  {
    "year": 2005,
    "manufacturer_name": "Hyundai",
    "model_name": "Tiburon",
    "car_type": "Coupe"
  },
  {
    "year": 2005,
    "manufacturer_name": "Kia",
    "model_name": "Rio",
    "car_type": "Sedan, Wagon"
  },
  {
    "year": 2005,
    "manufacturer_name": "Hyundai",
    "model_name": "Accent",
    "car_type": "Hatchback, Sedan"
  },
  {
    "year": 2005,
    "manufacturer_name": "Hyundai",
    "model_name": "Tucson",
    "car_type": "SUV"
  },
  {
    "year": 2005,
    "manufacturer_name": "Hyundai",
    "model_name": "Sonata",
    "car_type": "Sedan"
  },
  {
    "year": 2005,
    "manufacturer_name": "Jeep",
    "model_name": "Grand Cherokee",
    "car_type": "SUV"
  },
  {
    "year": 2005,
    "manufacturer_name": "Jaguar",
    "model_name": "XJ",
    "car_type": "Sedan"
  },
  {
    "year": 2005,
    "manufacturer_name": "Kia",
    "model_name": "Spectra",
    "car_type": "Sedan, Hatchback"
  },
  {
    "year": 2005,
    "manufacturer_name": "INFINITI",
    "model_name": "G",
    "car_type": "Coupe, Sedan"
  },
  {
    "year": 2005,
    "manufacturer_name": "Kia",
    "model_name": "Sportage",
    "car_type": "SUV"
  },
  {
    "year": 2005,
    "manufacturer_name": "Jaguar",
    "model_name": "X-Type",
    "car_type": "Sedan, Wagon"
  },
  {
    "year": 2005,
    "manufacturer_name": "Jeep",
    "model_name": "Wrangler",
    "car_type": "SUV"
  },
  {
    "year": 2005,
    "manufacturer_name": "Maserati",
    "model_name": "Coupe",
    "car_type": "Coupe"
  },
  {
    "year": 2005,
    "manufacturer_name": "Lexus",
    "model_name": "RX",
    "car_type": "SUV"
  },
  {
    "year": 2005,
    "manufacturer_name": "Land Rover",
    "model_name": "LR3",
    "car_type": "SUV"
  },
  {
    "year": 2005,
    "manufacturer_name": "Kia",
    "model_name": "Sorento",
    "car_type": "SUV"
  },
  {
    "year": 2005,
    "manufacturer_name": "Maserati",
    "model_name": "GranSport",
    "car_type": "Coupe"
  },
  {
    "year": 2005,
    "manufacturer_name": "Lexus",
    "model_name": "GX",
    "car_type": "SUV"
  },
  {
    "year": 2005,
    "manufacturer_name": "MAZDA",
    "model_name": "MX-5 Miata",
    "car_type": "Convertible"
  },
  {
    "year": 2005,
    "manufacturer_name": "Land Rover",
    "model_name": "Freelander",
    "car_type": "SUV"
  },
  {
    "year": 2005,
    "manufacturer_name": "Maserati",
    "model_name": "Quattroporte",
    "car_type": "Sedan"
  },
  {
    "year": 2005,
    "manufacturer_name": "Lexus",
    "model_name": "GS",
    "car_type": "Sedan"
  },
  {
    "year": 2005,
    "manufacturer_name": "Lincoln",
    "model_name": "Town Car",
    "car_type": "Sedan"
  },
  {
    "year": 2005,
    "manufacturer_name": "Land Rover",
    "model_name": "Range Rover",
    "car_type": "SUV"
  },
  {
    "year": 2005,
    "manufacturer_name": "Lexus",
    "model_name": "ES",
    "car_type": "Sedan"
  },
  {
    "year": 2005,
    "manufacturer_name": "Lincoln",
    "model_name": "Aviator",
    "car_type": "SUV"
  },
  {
    "year": 2005,
    "manufacturer_name": "MAZDA",
    "model_name": "B-Series Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2005,
    "manufacturer_name": "MAZDA",
    "model_name": "MAZDA3",
    "car_type": "Sedan, Hatchback"
  },
  {
    "year": 2005,
    "manufacturer_name": "Lexus",
    "model_name": "LX",
    "car_type": "SUV"
  },
  {
    "year": 2005,
    "manufacturer_name": "Lexus",
    "model_name": "IS",
    "car_type": "Sedan, Hatchback"
  },
  {
    "year": 2005,
    "manufacturer_name": "Lincoln",
    "model_name": "LS",
    "car_type": "Sedan"
  },
  {
    "year": 2005,
    "manufacturer_name": "Lexus",
    "model_name": "SC",
    "car_type": "Convertible"
  },
  {
    "year": 2005,
    "manufacturer_name": "Lotus",
    "model_name": "Elise",
    "car_type": "Coupe"
  },
  {
    "year": 2005,
    "manufacturer_name": "Maybach",
    "model_name": "57",
    "car_type": "Sedan"
  },
  {
    "year": 2005,
    "manufacturer_name": "Maybach",
    "model_name": "62",
    "car_type": "Sedan"
  },
  {
    "year": 2005,
    "manufacturer_name": "MAZDA",
    "model_name": "Tribute",
    "car_type": "SUV"
  },
  {
    "year": 2005,
    "manufacturer_name": "MAZDA",
    "model_name": "MAZDA6",
    "car_type": "Sedan, Hatchback, Wagon"
  },
  {
    "year": 2005,
    "manufacturer_name": "MAZDA",
    "model_name": "B-Series Extended Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2005,
    "manufacturer_name": "Lexus",
    "model_name": "LS",
    "car_type": "Sedan"
  },
  {
    "year": 2005,
    "manufacturer_name": "Lincoln",
    "model_name": "Navigator",
    "car_type": "SUV"
  },
  {
    "year": 2005,
    "manufacturer_name": "Mercedes-Benz",
    "model_name": "C-Class",
    "car_type": "Sedan, Coupe, Wagon"
  },
  {
    "year": 2005,
    "manufacturer_name": "MAZDA",
    "model_name": "MPV",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2005,
    "manufacturer_name": "Mitsubishi",
    "model_name": "Eclipse",
    "car_type": "Coupe, Convertible"
  },
  {
    "year": 2005,
    "manufacturer_name": "MINI",
    "model_name": "Convertible",
    "car_type": "Convertible"
  },
  {
    "year": 2005,
    "manufacturer_name": "Mercedes-Benz",
    "model_name": "CLK-Class",
    "car_type": "Coupe, Convertible"
  },
  {
    "year": 2005,
    "manufacturer_name": "Mercedes-Benz",
    "model_name": "G-Class",
    "car_type": "SUV"
  },
  {
    "year": 2005,
    "manufacturer_name": "Mercedes-Benz",
    "model_name": "E-Class",
    "car_type": "Sedan, Wagon"
  },
  {
    "year": 2005,
    "manufacturer_name": "Mercedes-Benz",
    "model_name": "SLR McLaren",
    "car_type": "Coupe"
  },
  {
    "year": 2005,
    "manufacturer_name": "MAZDA",
    "model_name": "RX-8",
    "car_type": "Coupe"
  },
  {
    "year": 2005,
    "manufacturer_name": "Nissan",
    "model_name": "350Z",
    "car_type": "Coupe, Convertible"
  },
  {
    "year": 2005,
    "manufacturer_name": "Mercedes-Benz",
    "model_name": "S-Class",
    "car_type": "Sedan"
  },
  {
    "year": 2005,
    "manufacturer_name": "Mercedes-Benz",
    "model_name": "M-Class",
    "car_type": "SUV"
  },
  {
    "year": 2005,
    "manufacturer_name": "Mercury",
    "model_name": "Montego",
    "car_type": "Sedan"
  },
  {
    "year": 2005,
    "manufacturer_name": "Mercury",
    "model_name": "Grand Marquis",
    "car_type": "Sedan"
  },
  {
    "year": 2005,
    "manufacturer_name": "Mercedes-Benz",
    "model_name": "SL-Class",
    "car_type": "Convertible"
  },
  {
    "year": 2005,
    "manufacturer_name": "Mitsubishi",
    "model_name": "Endeavor",
    "car_type": "SUV"
  },
  {
    "year": 2005,
    "manufacturer_name": "Mercury",
    "model_name": "Mountaineer",
    "car_type": "SUV"
  },
  {
    "year": 2005,
    "manufacturer_name": "MINI",
    "model_name": "Cooper",
    "car_type": "Hatchback"
  },
  {
    "year": 2005,
    "manufacturer_name": "Mercedes-Benz",
    "model_name": "CL-Class",
    "car_type": "Coupe"
  },
  {
    "year": 2005,
    "manufacturer_name": "Mercedes-Benz",
    "model_name": "SLK-Class",
    "car_type": "Convertible"
  },
  {
    "year": 2005,
    "manufacturer_name": "Mercury",
    "model_name": "Mariner",
    "car_type": "SUV"
  },
  {
    "year": 2005,
    "manufacturer_name": "Mercury",
    "model_name": "Sable",
    "car_type": "Sedan, Wagon"
  },
  {
    "year": 2005,
    "manufacturer_name": "Mitsubishi",
    "model_name": "Montero",
    "car_type": "SUV"
  },
  {
    "year": 2005,
    "manufacturer_name": "Mercury",
    "model_name": "Monterey",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2005,
    "manufacturer_name": "Panoz",
    "model_name": "Esperante",
    "car_type": "Coupe, Convertible"
  },
  {
    "year": 2005,
    "manufacturer_name": "Mitsubishi",
    "model_name": "Galant",
    "car_type": "Sedan"
  },
  {
    "year": 2005,
    "manufacturer_name": "Nissan",
    "model_name": "Titan Crew Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2005,
    "manufacturer_name": "Nissan",
    "model_name": "Maxima",
    "car_type": "Sedan"
  },
  {
    "year": 2005,
    "manufacturer_name": "Nissan",
    "model_name": "Frontier King Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2005,
    "manufacturer_name": "Nissan",
    "model_name": "Frontier Crew Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2005,
    "manufacturer_name": "Nissan",
    "model_name": "Quest",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2005,
    "manufacturer_name": "Mitsubishi",
    "model_name": "Outlander",
    "car_type": "SUV"
  },
  {
    "year": 2005,
    "manufacturer_name": "Nissan",
    "model_name": "Armada",
    "car_type": "SUV"
  },
  {
    "year": 2005,
    "manufacturer_name": "Mitsubishi",
    "model_name": "Lancer",
    "car_type": "Sedan"
  },
  {
    "year": 2005,
    "manufacturer_name": "Nissan",
    "model_name": "Murano",
    "car_type": "SUV"
  },
  {
    "year": 2005,
    "manufacturer_name": "Pontiac",
    "model_name": "Bonneville",
    "car_type": "Sedan"
  },
  {
    "year": 2005,
    "manufacturer_name": "Nissan",
    "model_name": "Altima",
    "car_type": "Sedan"
  },
  {
    "year": 2005,
    "manufacturer_name": "Nissan",
    "model_name": "Sentra",
    "car_type": "Sedan"
  },
  {
    "year": 2005,
    "manufacturer_name": "Pontiac",
    "model_name": "Aztek",
    "car_type": "SUV"
  },
  {
    "year": 2005,
    "manufacturer_name": "Nissan",
    "model_name": "Pathfinder",
    "car_type": "SUV"
  },
  {
    "year": 2005,
    "manufacturer_name": "Nissan",
    "model_name": "Titan King Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2005,
    "manufacturer_name": "Pontiac",
    "model_name": "G6",
    "car_type": "Sedan"
  },
  {
    "year": 2005,
    "manufacturer_name": "Nissan",
    "model_name": "Xterra",
    "car_type": "SUV"
  },
  {
    "year": 2005,
    "manufacturer_name": "Pontiac",
    "model_name": "Grand Am",
    "car_type": "Sedan, Coupe"
  },
  {
    "year": 2005,
    "manufacturer_name": "Porsche",
    "model_name": "Boxster",
    "car_type": "Convertible"
  },
  {
    "year": 2005,
    "manufacturer_name": "Subaru",
    "model_name": "Forester",
    "car_type": "SUV"
  },
  {
    "year": 2005,
    "manufacturer_name": "Pontiac",
    "model_name": "GTO",
    "car_type": "Coupe"
  },
  {
    "year": 2005,
    "manufacturer_name": "Pontiac",
    "model_name": "Montana SV6",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2005,
    "manufacturer_name": "Scion",
    "model_name": "tC",
    "car_type": "Coupe"
  },
  {
    "year": 2005,
    "manufacturer_name": "Saab",
    "model_name": "9-2X",
    "car_type": "Wagon"
  },
  {
    "year": 2005,
    "manufacturer_name": "Rolls-Royce",
    "model_name": "Phantom",
    "car_type": "Sedan"
  },
  {
    "year": 2005,
    "manufacturer_name": "Pontiac",
    "model_name": "Vibe",
    "car_type": "Wagon"
  },
  {
    "year": 2005,
    "manufacturer_name": "Pontiac",
    "model_name": "Montana",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2005,
    "manufacturer_name": "Pontiac",
    "model_name": "Sunfire",
    "car_type": "Coupe"
  },
  {
    "year": 2005,
    "manufacturer_name": "Porsche",
    "model_name": "911",
    "car_type": "Coupe, Convertible"
  },
  {
    "year": 2005,
    "manufacturer_name": "Saab",
    "model_name": "9-7X",
    "car_type": "SUV"
  },
  {
    "year": 2005,
    "manufacturer_name": "Pontiac",
    "model_name": "Grand Prix",
    "car_type": "Sedan"
  },
  {
    "year": 2005,
    "manufacturer_name": "Saturn",
    "model_name": "Ion",
    "car_type": "Sedan, Coupe"
  },
  {
    "year": 2005,
    "manufacturer_name": "Saturn",
    "model_name": "VUE",
    "car_type": "SUV"
  },
  {
    "year": 2005,
    "manufacturer_name": "Subaru",
    "model_name": "Baja",
    "car_type": "Pickup"
  },
  {
    "year": 2005,
    "manufacturer_name": "Porsche",
    "model_name": "Cayenne",
    "car_type": "SUV"
  },
  {
    "year": 2005,
    "manufacturer_name": "Saab",
    "model_name": "3-Sep",
    "car_type": "Convertible, Sedan"
  },
  {
    "year": 2005,
    "manufacturer_name": "Saab",
    "model_name": "5-Sep",
    "car_type": "Sedan, Wagon"
  },
  {
    "year": 2005,
    "manufacturer_name": "Toyota",
    "model_name": "RAV4",
    "car_type": "SUV"
  },
  {
    "year": 2005,
    "manufacturer_name": "Porsche",
    "model_name": "Carrera GT",
    "car_type": "Convertible"
  },
  {
    "year": 2005,
    "manufacturer_name": "Scion",
    "model_name": "xA",
    "car_type": "Hatchback"
  },
  {
    "year": 2005,
    "manufacturer_name": "Suzuki",
    "model_name": "Grand Vitara",
    "car_type": "SUV"
  },
  {
    "year": 2005,
    "manufacturer_name": "Saturn",
    "model_name": "Relay",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2005,
    "manufacturer_name": "Scion",
    "model_name": "xB",
    "car_type": "Hatchback"
  },
  {
    "year": 2005,
    "manufacturer_name": "Saturn",
    "model_name": "L-Series",
    "car_type": "Sedan"
  },
  {
    "year": 2005,
    "manufacturer_name": "Toyota",
    "model_name": "Avalon",
    "car_type": "Sedan"
  },
  {
    "year": 2005,
    "manufacturer_name": "Toyota",
    "model_name": "Highlander",
    "car_type": "SUV"
  },
  {
    "year": 2005,
    "manufacturer_name": "Subaru",
    "model_name": "Impreza",
    "car_type": "Sedan, Wagon"
  },
  {
    "year": 2005,
    "manufacturer_name": "Volkswagen",
    "model_name": "Passat",
    "car_type": "Sedan, Wagon"
  },
  {
    "year": 2005,
    "manufacturer_name": "Toyota",
    "model_name": "Tacoma Double Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2005,
    "manufacturer_name": "Volkswagen",
    "model_name": "Golf",
    "car_type": "Hatchback"
  },
  {
    "year": 2005,
    "manufacturer_name": "Volvo",
    "model_name": "S80",
    "car_type": "Sedan"
  },
  {
    "year": 2004,
    "manufacturer_name": "Acura",
    "model_name": "MDX",
    "car_type": "SUV"
  },
  {
    "year": 2005,
    "manufacturer_name": "Toyota",
    "model_name": "Camry",
    "car_type": "Sedan"
  },
  {
    "year": 2004,
    "manufacturer_name": "Buick",
    "model_name": "Century",
    "car_type": "Sedan"
  },
  {
    "year": 2004,
    "manufacturer_name": "Audi",
    "model_name": "S4",
    "car_type": "Wagon, Convertible, Sedan"
  },
  {
    "year": 2005,
    "manufacturer_name": "Suzuki",
    "model_name": "Reno",
    "car_type": "Hatchback"
  },
  {
    "year": 2005,
    "manufacturer_name": "Subaru",
    "model_name": "Legacy",
    "car_type": "Sedan, Wagon"
  },
  {
    "year": 2004,
    "manufacturer_name": "Acura",
    "model_name": "TSX",
    "car_type": "Sedan"
  },
  {
    "year": 2005,
    "manufacturer_name": "Toyota",
    "model_name": "Corolla",
    "car_type": "Sedan"
  },
  {
    "year": 2005,
    "manufacturer_name": "Suzuki",
    "model_name": "Aerio",
    "car_type": "Sedan, Wagon"
  },
  {
    "year": 2005,
    "manufacturer_name": "Toyota",
    "model_name": "Celica",
    "car_type": "Hatchback"
  },
  {
    "year": 2005,
    "manufacturer_name": "Suzuki",
    "model_name": "Forenza",
    "car_type": "Sedan, Wagon"
  },
  {
    "year": 2005,
    "manufacturer_name": "Suzuki",
    "model_name": "XL-7",
    "car_type": "SUV"
  },
  {
    "year": 2005,
    "manufacturer_name": "Subaru",
    "model_name": "Outback",
    "car_type": "Wagon, Sedan"
  },
  {
    "year": 2004,
    "manufacturer_name": "BMW",
    "model_name": "7 Series",
    "car_type": "Sedan"
  },
  {
    "year": 2005,
    "manufacturer_name": "Toyota",
    "model_name": "4Runner",
    "car_type": "SUV"
  },
  {
    "year": 2005,
    "manufacturer_name": "Suzuki",
    "model_name": "Verona",
    "car_type": "Sedan"
  },
  {
    "year": 2005,
    "manufacturer_name": "Toyota",
    "model_name": "Echo",
    "car_type": "Sedan"
  },
  {
    "year": 2004,
    "manufacturer_name": "Buick",
    "model_name": "Rendezvous",
    "car_type": "SUV"
  },
  {
    "year": 2005,
    "manufacturer_name": "Toyota",
    "model_name": "Tundra Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2005,
    "manufacturer_name": "Toyota",
    "model_name": "Prius",
    "car_type": "Hatchback"
  },
  {
    "year": 2005,
    "manufacturer_name": "Toyota",
    "model_name": "Matrix",
    "car_type": "Wagon"
  },
  {
    "year": 2005,
    "manufacturer_name": "Toyota",
    "model_name": "Tundra Double Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2005,
    "manufacturer_name": "Toyota",
    "model_name": "Land Cruiser",
    "car_type": "SUV"
  },
  {
    "year": 2005,
    "manufacturer_name": "Toyota",
    "model_name": "MR2",
    "car_type": "Convertible"
  },
  {
    "year": 2005,
    "manufacturer_name": "Toyota",
    "model_name": "Tacoma Access Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2005,
    "manufacturer_name": "Volkswagen",
    "model_name": "Jetta (New)",
    "car_type": "Sedan"
  },
  {
    "year": 2005,
    "manufacturer_name": "Volvo",
    "model_name": "S60",
    "car_type": "Sedan"
  },
  {
    "year": 2005,
    "manufacturer_name": "Toyota",
    "model_name": "Solara",
    "car_type": "Coupe, Convertible"
  },
  {
    "year": 2005,
    "manufacturer_name": "Volvo",
    "model_name": "XC90",
    "car_type": "SUV"
  },
  {
    "year": 2005,
    "manufacturer_name": "Volkswagen",
    "model_name": "New Beetle",
    "car_type": "Hatchback, Convertible"
  },
  {
    "year": 2005,
    "manufacturer_name": "Volvo",
    "model_name": "XC70",
    "car_type": "Wagon"
  },
  {
    "year": 2005,
    "manufacturer_name": "Volvo",
    "model_name": "S40",
    "car_type": "Sedan"
  },
  {
    "year": 2004,
    "manufacturer_name": "BMW",
    "model_name": "6 Series",
    "car_type": "Convertible, Coupe"
  },
  {
    "year": 2004,
    "manufacturer_name": "Audi",
    "model_name": "A8",
    "car_type": "Sedan"
  },
  {
    "year": 2004,
    "manufacturer_name": "Acura",
    "model_name": "RSX",
    "car_type": "Coupe"
  },
  {
    "year": 2004,
    "manufacturer_name": "Acura",
    "model_name": "TL",
    "car_type": "Sedan"
  },
  {
    "year": 2004,
    "manufacturer_name": "BMW",
    "model_name": "5 Series",
    "car_type": "Sedan"
  },
  {
    "year": 2004,
    "manufacturer_name": "Audi",
    "model_name": "allroad",
    "car_type": "Wagon"
  },
  {
    "year": 2005,
    "manufacturer_name": "Volkswagen",
    "model_name": "Phaeton",
    "car_type": "Sedan"
  },
  {
    "year": 2004,
    "manufacturer_name": "Buick",
    "model_name": "Rainier",
    "car_type": "SUV"
  },
  {
    "year": 2005,
    "manufacturer_name": "Volkswagen",
    "model_name": "GTI",
    "car_type": "Hatchback"
  },
  {
    "year": 2005,
    "manufacturer_name": "Volkswagen",
    "model_name": "Touareg",
    "car_type": "SUV"
  },
  {
    "year": 2005,
    "manufacturer_name": "Toyota",
    "model_name": "Tundra Access Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2004,
    "manufacturer_name": "Buick",
    "model_name": "Regal",
    "car_type": "Sedan"
  },
  {
    "year": 2004,
    "manufacturer_name": "BMW",
    "model_name": "X5",
    "car_type": "SUV"
  },
  {
    "year": 2004,
    "manufacturer_name": "BMW",
    "model_name": "Z4",
    "car_type": "Convertible"
  },
  {
    "year": 2004,
    "manufacturer_name": "Cadillac",
    "model_name": "Escalade ESV",
    "car_type": "SUV"
  },
  {
    "year": 2005,
    "manufacturer_name": "Toyota",
    "model_name": "Sienna",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2004,
    "manufacturer_name": "Cadillac",
    "model_name": "Escalade",
    "car_type": "SUV"
  },
  {
    "year": 2005,
    "manufacturer_name": "Toyota",
    "model_name": "Tacoma Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2005,
    "manufacturer_name": "Toyota",
    "model_name": "Sequoia",
    "car_type": "SUV"
  },
  {
    "year": 2005,
    "manufacturer_name": "Volkswagen",
    "model_name": "Jetta",
    "car_type": "Sedan, Wagon"
  },
  {
    "year": 2004,
    "manufacturer_name": "Audi",
    "model_name": "TT",
    "car_type": "Convertible, Coupe"
  },
  {
    "year": 2004,
    "manufacturer_name": "Acura",
    "model_name": "NSX",
    "car_type": "Coupe"
  },
  {
    "year": 2004,
    "manufacturer_name": "BMW",
    "model_name": "M3",
    "car_type": "Convertible, Coupe"
  },
  {
    "year": 2004,
    "manufacturer_name": "Audi",
    "model_name": "A6",
    "car_type": "Wagon, Sedan"
  },
  {
    "year": 2004,
    "manufacturer_name": "BMW",
    "model_name": "X3",
    "car_type": "SUV"
  },
  {
    "year": 2005,
    "manufacturer_name": "Volvo",
    "model_name": "V50",
    "car_type": "Wagon"
  },
  {
    "year": 2005,
    "manufacturer_name": "Volvo",
    "model_name": "V70",
    "car_type": "Wagon"
  },
  {
    "year": 2004,
    "manufacturer_name": "Audi",
    "model_name": "A4",
    "car_type": "Convertible, Wagon, Sedan"
  },
  {
    "year": 2004,
    "manufacturer_name": "Buick",
    "model_name": "Park Avenue",
    "car_type": "Sedan"
  },
  {
    "year": 2004,
    "manufacturer_name": "Acura",
    "model_name": "RL",
    "car_type": "Sedan"
  },
  {
    "year": 2004,
    "manufacturer_name": "BMW",
    "model_name": "3 Series",
    "car_type": "Sedan, Coupe, Convertible, Wagon"
  },
  {
    "year": 2004,
    "manufacturer_name": "Buick",
    "model_name": "LeSabre",
    "car_type": "Sedan"
  },
  {
    "year": 2004,
    "manufacturer_name": "Cadillac",
    "model_name": "DeVille",
    "car_type": "Sedan"
  },
  {
    "year": 2004,
    "manufacturer_name": "Cadillac",
    "model_name": "CTS",
    "car_type": "Sedan"
  },
  {
    "year": 2004,
    "manufacturer_name": "Cadillac",
    "model_name": "SRX",
    "car_type": "SUV"
  },
  {
    "year": 2004,
    "manufacturer_name": "Cadillac",
    "model_name": "Seville",
    "car_type": "Sedan"
  },
  {
    "year": 2004,
    "manufacturer_name": "Chevrolet",
    "model_name": "Cavalier",
    "car_type": "Sedan, Coupe"
  },
  {
    "year": 2004,
    "manufacturer_name": "Chevrolet",
    "model_name": "Avalanche 1500",
    "car_type": "Pickup"
  },
  {
    "year": 2004,
    "manufacturer_name": "Cadillac",
    "model_name": "XLR",
    "car_type": "Convertible"
  },
  {
    "year": 2004,
    "manufacturer_name": "Chevrolet",
    "model_name": "Express 2500 Passenger",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2004,
    "manufacturer_name": "Chevrolet",
    "model_name": "Astro Passenger",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2004,
    "manufacturer_name": "Chevrolet",
    "model_name": "Express 3500 Cargo",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2004,
    "manufacturer_name": "Chevrolet",
    "model_name": "Avalanche 2500",
    "car_type": "Pickup"
  },
  {
    "year": 2004,
    "manufacturer_name": "Cadillac",
    "model_name": "Escalade EXT",
    "car_type": "Pickup"
  },
  {
    "year": 2004,
    "manufacturer_name": "Chevrolet",
    "model_name": "Aveo",
    "car_type": "Sedan, Hatchback"
  },
  {
    "year": 2004,
    "manufacturer_name": "Chevrolet",
    "model_name": "Colorado Extended Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2004,
    "manufacturer_name": "Chevrolet",
    "model_name": "Malibu",
    "car_type": "Hatchback, Sedan"
  },
  {
    "year": 2004,
    "manufacturer_name": "Chevrolet",
    "model_name": "Corvette",
    "car_type": "Convertible, Coupe"
  },
  {
    "year": 2004,
    "manufacturer_name": "Chevrolet",
    "model_name": "Monte Carlo",
    "car_type": "Coupe"
  },
  {
    "year": 2004,
    "manufacturer_name": "Chevrolet",
    "model_name": "Astro Cargo",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2004,
    "manufacturer_name": "Chevrolet",
    "model_name": "Express 2500 Cargo",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2004,
    "manufacturer_name": "Chevrolet",
    "model_name": "Colorado Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2004,
    "manufacturer_name": "Chevrolet",
    "model_name": "Blazer",
    "car_type": "SUV"
  },
  {
    "year": 2004,
    "manufacturer_name": "Chevrolet",
    "model_name": "Classic",
    "car_type": "Sedan"
  },
  {
    "year": 2004,
    "manufacturer_name": "Chevrolet",
    "model_name": "Colorado Crew Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2004,
    "manufacturer_name": "Chevrolet",
    "model_name": "Express 1500 Passenger",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2004,
    "manufacturer_name": "Chevrolet",
    "model_name": "Suburban 1500",
    "car_type": "SUV"
  },
  {
    "year": 2004,
    "manufacturer_name": "Dodge",
    "model_name": "Grand Caravan Cargo",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2004,
    "manufacturer_name": "Chevrolet",
    "model_name": "Express 1500 Cargo",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2004,
    "manufacturer_name": "Chevrolet",
    "model_name": "Suburban 2500",
    "car_type": "SUV"
  },
  {
    "year": 2004,
    "manufacturer_name": "Chevrolet",
    "model_name": "Silverado 2500 Extended Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2004,
    "manufacturer_name": "Chevrolet",
    "model_name": "S10 Crew Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2004,
    "manufacturer_name": "Chevrolet",
    "model_name": "Venture Cargo",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2004,
    "manufacturer_name": "Chevrolet",
    "model_name": "Silverado 2500 Crew Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2004,
    "manufacturer_name": "Dodge",
    "model_name": "Durango",
    "car_type": "SUV"
  },
  {
    "year": 2004,
    "manufacturer_name": "Chevrolet",
    "model_name": "Silverado 2500 HD Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2004,
    "manufacturer_name": "Dodge",
    "model_name": "Caravan Cargo",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2004,
    "manufacturer_name": "Chevrolet",
    "model_name": "Silverado 1500 Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2004,
    "manufacturer_name": "Chevrolet",
    "model_name": "Express 3500 Passenger",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2004,
    "manufacturer_name": "Chevrolet",
    "model_name": "Silverado 3500 Extended Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2004,
    "manufacturer_name": "Chevrolet",
    "model_name": "Silverado 2500 Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2004,
    "manufacturer_name": "Chevrolet",
    "model_name": "Silverado 1500 Crew Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2004,
    "manufacturer_name": "Chrysler",
    "model_name": "Crossfire",
    "car_type": "Coupe"
  },
  {
    "year": 2004,
    "manufacturer_name": "Chevrolet",
    "model_name": "Impala",
    "car_type": "Sedan"
  },
  {
    "year": 2004,
    "manufacturer_name": "Chevrolet",
    "model_name": "Venture Passenger",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2004,
    "manufacturer_name": "Chevrolet",
    "model_name": "Silverado 2500 HD Crew Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2004,
    "manufacturer_name": "Chrysler",
    "model_name": "Pacifica",
    "car_type": "Wagon"
  },
  {
    "year": 2004,
    "manufacturer_name": "Chevrolet",
    "model_name": "Silverado 2500 HD Extended Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2004,
    "manufacturer_name": "Dodge",
    "model_name": "Dakota Club Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2004,
    "manufacturer_name": "Chrysler",
    "model_name": "300M",
    "car_type": "Sedan"
  },
  {
    "year": 2004,
    "manufacturer_name": "Chevrolet",
    "model_name": "Silverado 1500 Extended Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2004,
    "manufacturer_name": "Chrysler",
    "model_name": "Town & Country",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2004,
    "manufacturer_name": "Chevrolet",
    "model_name": "Silverado 3500 Crew Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2004,
    "manufacturer_name": "Chevrolet",
    "model_name": "Silverado 3500 Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2004,
    "manufacturer_name": "Chrysler",
    "model_name": "Concorde",
    "car_type": "Sedan"
  },
  {
    "year": 2004,
    "manufacturer_name": "Dodge",
    "model_name": "Caravan Passenger",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2004,
    "manufacturer_name": "Chevrolet",
    "model_name": "Tracker",
    "car_type": "SUV"
  },
  {
    "year": 2004,
    "manufacturer_name": "Chevrolet",
    "model_name": "SSR",
    "car_type": "Pickup"
  },
  {
    "year": 2004,
    "manufacturer_name": "Chevrolet",
    "model_name": "TrailBlazer",
    "car_type": "SUV"
  },
  {
    "year": 2004,
    "manufacturer_name": "Chevrolet",
    "model_name": "Tahoe",
    "car_type": "SUV"
  },
  {
    "year": 2004,
    "manufacturer_name": "Chrysler",
    "model_name": "PT Cruiser",
    "car_type": "Wagon"
  },
  {
    "year": 2004,
    "manufacturer_name": "Dodge",
    "model_name": "Dakota Quad Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2004,
    "manufacturer_name": "Dodge",
    "model_name": "Ram 2500 Quad Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2004,
    "manufacturer_name": "Dodge",
    "model_name": "Ram 1500 Quad Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2004,
    "manufacturer_name": "Dodge",
    "model_name": "Ram 1500 Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2004,
    "manufacturer_name": "Dodge",
    "model_name": "Grand Caravan Passenger",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2004,
    "manufacturer_name": "Dodge",
    "model_name": "Dakota Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2004,
    "manufacturer_name": "Chrysler",
    "model_name": "Sebring",
    "car_type": "Coupe, Convertible, Sedan"
  },
  {
    "year": 2004,
    "manufacturer_name": "Dodge",
    "model_name": "Ram 3500 Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2004,
    "manufacturer_name": "Dodge",
    "model_name": "Sprinter 2500 Cargo",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2004,
    "manufacturer_name": "Dodge",
    "model_name": "Intrepid",
    "car_type": "Sedan"
  },
  {
    "year": 2004,
    "manufacturer_name": "Dodge",
    "model_name": "Neon",
    "car_type": "Sedan"
  },
  {
    "year": 2004,
    "manufacturer_name": "Dodge",
    "model_name": "Sprinter 2500 Passenger",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2004,
    "manufacturer_name": "Ford",
    "model_name": "Escape",
    "car_type": "SUV"
  },
  {
    "year": 2004,
    "manufacturer_name": "Dodge",
    "model_name": "Ram 2500 Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2004,
    "manufacturer_name": "Dodge",
    "model_name": "Viper",
    "car_type": "Convertible"
  },
  {
    "year": 2004,
    "manufacturer_name": "Ford",
    "model_name": "E350 Super Duty Passenger",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2004,
    "manufacturer_name": "Ford",
    "model_name": "Crown Victoria",
    "car_type": "Sedan"
  },
  {
    "year": 2004,
    "manufacturer_name": "Ford",
    "model_name": "E150 Passenger",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2004,
    "manufacturer_name": "Ford",
    "model_name": "E350 Super Duty Cargo",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2004,
    "manufacturer_name": "Dodge",
    "model_name": "Ram 3500 Quad Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2004,
    "manufacturer_name": "Ford",
    "model_name": "Excursion",
    "car_type": "SUV"
  },
  {
    "year": 2004,
    "manufacturer_name": "Ford",
    "model_name": "Explorer",
    "car_type": "SUV"
  },
  {
    "year": 2004,
    "manufacturer_name": "Ford",
    "model_name": "E150 Super Duty Cargo",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2004,
    "manufacturer_name": "Ford",
    "model_name": "F250 Super Duty Crew Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2004,
    "manufacturer_name": "Ford",
    "model_name": "F350 Super Duty Crew Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2004,
    "manufacturer_name": "Dodge",
    "model_name": "Stratus",
    "car_type": "Sedan, Coupe"
  },
  {
    "year": 2004,
    "manufacturer_name": "Ford",
    "model_name": "F150 SuperCrew Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2004,
    "manufacturer_name": "Ford",
    "model_name": "F350 Super Duty Super Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2004,
    "manufacturer_name": "Dodge",
    "model_name": "Sprinter 3500 Cargo",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2004,
    "manufacturer_name": "Ford",
    "model_name": "Mustang",
    "car_type": "Convertible, Coupe"
  },
  {
    "year": 2004,
    "manufacturer_name": "Ford",
    "model_name": "Explorer Sport Trac",
    "car_type": "Pickup"
  },
  {
    "year": 2004,
    "manufacturer_name": "Ford",
    "model_name": "F150 (Heritage) Super Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2004,
    "manufacturer_name": "Ford",
    "model_name": "F150 Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2004,
    "manufacturer_name": "Ford",
    "model_name": "E250 Super Duty Cargo",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2004,
    "manufacturer_name": "Ford",
    "model_name": "F150 (Heritage) Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2004,
    "manufacturer_name": "Ford",
    "model_name": "F350 Super Duty Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2004,
    "manufacturer_name": "Ford",
    "model_name": "F150 Super Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2004,
    "manufacturer_name": "Ford",
    "model_name": "F250 Super Duty Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2004,
    "manufacturer_name": "Ford",
    "model_name": "Focus",
    "car_type": "Sedan, Hatchback, Wagon"
  },
  {
    "year": 2004,
    "manufacturer_name": "Ford",
    "model_name": "F250 Super Duty Super Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2004,
    "manufacturer_name": "Ford",
    "model_name": "Expedition",
    "car_type": "SUV"
  },
  {
    "year": 2004,
    "manufacturer_name": "Ford",
    "model_name": "Freestar Cargo",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2004,
    "manufacturer_name": "Ford",
    "model_name": "Freestar Passenger",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2004,
    "manufacturer_name": "GMC",
    "model_name": "Canyon Extended Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2004,
    "manufacturer_name": "Ford",
    "model_name": "Ranger Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2004,
    "manufacturer_name": "Ford",
    "model_name": "Thunderbird",
    "car_type": "Convertible"
  },
  {
    "year": 2004,
    "manufacturer_name": "Ford",
    "model_name": "Taurus",
    "car_type": "Sedan, Wagon"
  },
  {
    "year": 2004,
    "manufacturer_name": "Ford",
    "model_name": "Ranger Super Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2004,
    "manufacturer_name": "GMC",
    "model_name": "Envoy XL",
    "car_type": "SUV"
  },
  {
    "year": 2004,
    "manufacturer_name": "GMC",
    "model_name": "Canyon Crew Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2004,
    "manufacturer_name": "GMC",
    "model_name": "Envoy",
    "car_type": "SUV"
  },
  {
    "year": 2004,
    "manufacturer_name": "GMC",
    "model_name": "Savana 3500 Passenger",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2004,
    "manufacturer_name": "GMC",
    "model_name": "Savana 3500 Cargo",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2004,
    "manufacturer_name": "GMC",
    "model_name": "Canyon Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2004,
    "manufacturer_name": "GMC",
    "model_name": "Safari Cargo",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2004,
    "manufacturer_name": "GMC",
    "model_name": "Sierra 2500 HD Crew Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2004,
    "manufacturer_name": "GMC",
    "model_name": "Sierra 1500 Extended Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2004,
    "manufacturer_name": "GMC",
    "model_name": "Savana 1500 Cargo",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2004,
    "manufacturer_name": "GMC",
    "model_name": "Safari Passenger",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2004,
    "manufacturer_name": "GMC",
    "model_name": "Envoy XUV",
    "car_type": "SUV"
  },
  {
    "year": 2004,
    "manufacturer_name": "GMC",
    "model_name": "Sierra 1500 Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2004,
    "manufacturer_name": "GMC",
    "model_name": "Sierra 3500 Extended Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2004,
    "manufacturer_name": "GMC",
    "model_name": "Yukon XL 2500",
    "car_type": "SUV"
  },
  {
    "year": 2004,
    "manufacturer_name": "GMC",
    "model_name": "Savana 2500 Cargo",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2004,
    "manufacturer_name": "GMC",
    "model_name": "Savana 2500 Passenger",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2004,
    "manufacturer_name": "Honda",
    "model_name": "Civic",
    "car_type": "Coupe, Sedan, Hatchback"
  },
  {
    "year": 2004,
    "manufacturer_name": "GMC",
    "model_name": "Sierra 1500 Crew Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2004,
    "manufacturer_name": "GMC",
    "model_name": "Sierra 2500 Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2004,
    "manufacturer_name": "GMC",
    "model_name": "Sonoma Crew Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2004,
    "manufacturer_name": "Honda",
    "model_name": "Accord",
    "car_type": "Sedan, Coupe"
  },
  {
    "year": 2004,
    "manufacturer_name": "GMC",
    "model_name": "Savana 1500 Passenger",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2004,
    "manufacturer_name": "GMC",
    "model_name": "Sierra 2500 HD Extended Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2004,
    "manufacturer_name": "GMC",
    "model_name": "Sierra 2500 HD Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2004,
    "manufacturer_name": "GMC",
    "model_name": "Sierra 2500 Crew Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2004,
    "manufacturer_name": "GMC",
    "model_name": "Sierra 2500 Extended Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2004,
    "manufacturer_name": "GMC",
    "model_name": "Yukon",
    "car_type": "SUV"
  },
  {
    "year": 2004,
    "manufacturer_name": "GMC",
    "model_name": "Sierra 3500 Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2004,
    "manufacturer_name": "GMC",
    "model_name": "Sierra 3500 Crew Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2004,
    "manufacturer_name": "Hyundai",
    "model_name": "Sonata",
    "car_type": "Sedan"
  },
  {
    "year": 2004,
    "manufacturer_name": "GMC",
    "model_name": "Yukon XL 1500",
    "car_type": "SUV"
  },
  {
    "year": 2004,
    "manufacturer_name": "Honda",
    "model_name": "Insight",
    "car_type": "Hatchback"
  },
  {
    "year": 2004,
    "manufacturer_name": "INFINITI",
    "model_name": "FX",
    "car_type": "SUV"
  },
  {
    "year": 2004,
    "manufacturer_name": "Honda",
    "model_name": "Element",
    "car_type": "SUV"
  },
  {
    "year": 2004,
    "manufacturer_name": "INFINITI",
    "model_name": "Q",
    "car_type": "Sedan"
  },
  {
    "year": 2004,
    "manufacturer_name": "Honda",
    "model_name": "CR-V",
    "car_type": "SUV"
  },
  {
    "year": 2004,
    "manufacturer_name": "Hyundai",
    "model_name": "Accent",
    "car_type": "Hatchback, Sedan"
  },
  {
    "year": 2004,
    "manufacturer_name": "Jaguar",
    "model_name": "XJ",
    "car_type": "Sedan"
  },
  {
    "year": 2004,
    "manufacturer_name": "Honda",
    "model_name": "Odyssey",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2004,
    "manufacturer_name": "HUMMER",
    "model_name": "H2",
    "car_type": "SUV"
  },
  {
    "year": 2004,
    "manufacturer_name": "INFINITI",
    "model_name": "M",
    "car_type": "Sedan"
  },
  {
    "year": 2004,
    "manufacturer_name": "Honda",
    "model_name": "Pilot",
    "car_type": "SUV"
  },
  {
    "year": 2004,
    "manufacturer_name": "Honda",
    "model_name": "S2000",
    "car_type": "Convertible"
  },
  {
    "year": 2004,
    "manufacturer_name": "INFINITI",
    "model_name": "QX",
    "car_type": "SUV"
  },
  {
    "year": 2004,
    "manufacturer_name": "Hyundai",
    "model_name": "Elantra",
    "car_type": "Sedan, Hatchback"
  },
  {
    "year": 2004,
    "manufacturer_name": "Hyundai",
    "model_name": "Tiburon",
    "car_type": "Coupe"
  },
  {
    "year": 2004,
    "manufacturer_name": "INFINITI",
    "model_name": "G",
    "car_type": "Coupe, Sedan"
  },
  {
    "year": 2004,
    "manufacturer_name": "Hyundai",
    "model_name": "XG350",
    "car_type": "Sedan"
  },
  {
    "year": 2004,
    "manufacturer_name": "Hyundai",
    "model_name": "Santa Fe",
    "car_type": "SUV"
  },
  {
    "year": 2004,
    "manufacturer_name": "HUMMER",
    "model_name": "H1",
    "car_type": "Wagon, SUV"
  },
  {
    "year": 2004,
    "manufacturer_name": "Jaguar",
    "model_name": "S-Type",
    "car_type": "Sedan"
  },
  {
    "year": 2004,
    "manufacturer_name": "Kia",
    "model_name": "Rio",
    "car_type": "Wagon, Sedan"
  },
  {
    "year": 2004,
    "manufacturer_name": "Land Rover",
    "model_name": "Discovery",
    "car_type": "SUV"
  },
  {
    "year": 2004,
    "manufacturer_name": "Kia",
    "model_name": "Spectra",
    "car_type": "Sedan, Hatchback"
  },
  {
    "year": 2004,
    "manufacturer_name": "Kia",
    "model_name": "Optima",
    "car_type": "Sedan"
  },
  {
    "year": 2004,
    "manufacturer_name": "Jaguar",
    "model_name": "XK",
    "car_type": "Coupe, Convertible"
  },
  {
    "year": 2004,
    "manufacturer_name": "Jaguar",
    "model_name": "X-Type",
    "car_type": "Sedan"
  },
  {
    "year": 2004,
    "manufacturer_name": "Jeep",
    "model_name": "Wrangler",
    "car_type": "SUV"
  },
  {
    "year": 2004,
    "manufacturer_name": "Lincoln",
    "model_name": "Aviator",
    "car_type": "SUV"
  },
  {
    "year": 2004,
    "manufacturer_name": "Land Rover",
    "model_name": "Range Rover",
    "car_type": "SUV"
  },
  {
    "year": 2004,
    "manufacturer_name": "Kia",
    "model_name": "Amanti",
    "car_type": "Sedan"
  },
  {
    "year": 2004,
    "manufacturer_name": "Mercedes-Benz",
    "model_name": "E-Class",
    "car_type": "Sedan, Wagon"
  },
  {
    "year": 2004,
    "manufacturer_name": "Isuzu",
    "model_name": "Axiom",
    "car_type": "SUV"
  },
  {
    "year": 2004,
    "manufacturer_name": "Isuzu",
    "model_name": "Rodeo",
    "car_type": "SUV"
  },
  {
    "year": 2004,
    "manufacturer_name": "Kia",
    "model_name": "Sorento",
    "car_type": "SUV"
  },
  {
    "year": 2004,
    "manufacturer_name": "Isuzu",
    "model_name": "Ascender",
    "car_type": "SUV"
  },
  {
    "year": 2004,
    "manufacturer_name": "Kia",
    "model_name": "Sedona",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2004,
    "manufacturer_name": "MAZDA",
    "model_name": "MAZDA6",
    "car_type": "Sedan, Wagon, Hatchback"
  },
  {
    "year": 2004,
    "manufacturer_name": "Lincoln",
    "model_name": "LS",
    "car_type": "Sedan"
  },
  {
    "year": 2004,
    "manufacturer_name": "Lexus",
    "model_name": "LX",
    "car_type": "SUV"
  },
  {
    "year": 2004,
    "manufacturer_name": "Jeep",
    "model_name": "Grand Cherokee",
    "car_type": "SUV"
  },
  {
    "year": 2004,
    "manufacturer_name": "MAZDA",
    "model_name": "B-Series Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2004,
    "manufacturer_name": "INFINITI",
    "model_name": "I",
    "car_type": "Sedan"
  },
  {
    "year": 2004,
    "manufacturer_name": "Mercedes-Benz",
    "model_name": "C-Class",
    "car_type": "Sedan, Coupe, Wagon"
  },
  {
    "year": 2004,
    "manufacturer_name": "Mercedes-Benz",
    "model_name": "CLK-Class",
    "car_type": "Coupe, Convertible"
  },
  {
    "year": 2004,
    "manufacturer_name": "Mercedes-Benz",
    "model_name": "CL-Class",
    "car_type": "Coupe"
  },
  {
    "year": 2004,
    "manufacturer_name": "Lexus",
    "model_name": "IS",
    "car_type": "Sedan, Hatchback"
  },
  {
    "year": 2004,
    "manufacturer_name": "Land Rover",
    "model_name": "Freelander",
    "car_type": "SUV"
  },
  {
    "year": 2004,
    "manufacturer_name": "Lexus",
    "model_name": "GX",
    "car_type": "SUV"
  },
  {
    "year": 2004,
    "manufacturer_name": "Jeep",
    "model_name": "Liberty",
    "car_type": "SUV"
  },
  {
    "year": 2004,
    "manufacturer_name": "MAZDA",
    "model_name": "RX-8",
    "car_type": "Coupe"
  },
  {
    "year": 2004,
    "manufacturer_name": "Lexus",
    "model_name": "ES",
    "car_type": "Sedan"
  },
  {
    "year": 2004,
    "manufacturer_name": "Lexus",
    "model_name": "SC",
    "car_type": "Convertible"
  },
  {
    "year": 2004,
    "manufacturer_name": "Lexus",
    "model_name": "GS",
    "car_type": "Sedan"
  },
  {
    "year": 2004,
    "manufacturer_name": "Lincoln",
    "model_name": "Town Car",
    "car_type": "Sedan"
  },
  {
    "year": 2004,
    "manufacturer_name": "Lexus",
    "model_name": "LS",
    "car_type": "Sedan"
  },
  {
    "year": 2004,
    "manufacturer_name": "MAZDA",
    "model_name": "MAZDA3",
    "car_type": "Sedan, Hatchback"
  },
  {
    "year": 2004,
    "manufacturer_name": "MAZDA",
    "model_name": "Tribute",
    "car_type": "SUV"
  },
  {
    "year": 2004,
    "manufacturer_name": "Lexus",
    "model_name": "RX",
    "car_type": "SUV"
  },
  {
    "year": 2004,
    "manufacturer_name": "MAZDA",
    "model_name": "B-Series Cab Plus",
    "car_type": "Pickup"
  },
  {
    "year": 2004,
    "manufacturer_name": "Lincoln",
    "model_name": "Navigator",
    "car_type": "SUV"
  },
  {
    "year": 2004,
    "manufacturer_name": "Mercedes-Benz",
    "model_name": "G-Class",
    "car_type": "SUV"
  },
  {
    "year": 2004,
    "manufacturer_name": "MAZDA",
    "model_name": "MPV",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2004,
    "manufacturer_name": "MAZDA",
    "model_name": "MX-5 Miata",
    "car_type": "Convertible"
  },
  {
    "year": 2004,
    "manufacturer_name": "Mercedes-Benz",
    "model_name": "M-Class",
    "car_type": "SUV"
  },
  {
    "year": 2004,
    "manufacturer_name": "Mercury",
    "model_name": "Grand Marquis",
    "car_type": "Sedan"
  },
  {
    "year": 2004,
    "manufacturer_name": "Mitsubishi",
    "model_name": "Galant",
    "car_type": "Sedan"
  },
  {
    "year": 2004,
    "manufacturer_name": "Mercedes-Benz",
    "model_name": "S-Class",
    "car_type": "Sedan"
  },
  {
    "year": 2004,
    "manufacturer_name": "Mitsubishi",
    "model_name": "Outlander",
    "car_type": "SUV"
  },
  {
    "year": 2004,
    "manufacturer_name": "Nissan",
    "model_name": "350Z",
    "car_type": "Coupe, Convertible"
  },
  {
    "year": 2004,
    "manufacturer_name": "Mercury",
    "model_name": "Mountaineer",
    "car_type": "SUV"
  },
  {
    "year": 2004,
    "manufacturer_name": "Mercury",
    "model_name": "Marauder",
    "car_type": "Sedan"
  },
  {
    "year": 2004,
    "manufacturer_name": "Mitsubishi",
    "model_name": "Endeavor",
    "car_type": "SUV"
  },
  {
    "year": 2004,
    "manufacturer_name": "Mitsubishi",
    "model_name": "Diamante",
    "car_type": "Sedan"
  },
  {
    "year": 2004,
    "manufacturer_name": "Mitsubishi",
    "model_name": "Montero",
    "car_type": "SUV"
  },
  {
    "year": 2004,
    "manufacturer_name": "Mercedes-Benz",
    "model_name": "SL-Class",
    "car_type": "Convertible"
  },
  {
    "year": 2004,
    "manufacturer_name": "Mitsubishi",
    "model_name": "Lancer",
    "car_type": "Sedan, Wagon"
  },
  {
    "year": 2004,
    "manufacturer_name": "Mercedes-Benz",
    "model_name": "SLK-Class",
    "car_type": "Convertible"
  },
  {
    "year": 2004,
    "manufacturer_name": "Mitsubishi",
    "model_name": "Montero Sport",
    "car_type": "SUV"
  },
  {
    "year": 2004,
    "manufacturer_name": "Nissan",
    "model_name": "Frontier Crew Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2004,
    "manufacturer_name": "Mercury",
    "model_name": "Sable",
    "car_type": "Sedan, Wagon"
  },
  {
    "year": 2004,
    "manufacturer_name": "MINI",
    "model_name": "Cooper",
    "car_type": "Hatchback"
  },
  {
    "year": 2004,
    "manufacturer_name": "Nissan",
    "model_name": "Altima",
    "car_type": "Sedan"
  },
  {
    "year": 2004,
    "manufacturer_name": "Mercury",
    "model_name": "Monterey",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2004,
    "manufacturer_name": "Mitsubishi",
    "model_name": "Eclipse",
    "car_type": "Coupe, Convertible"
  },
  {
    "year": 2004,
    "manufacturer_name": "Nissan",
    "model_name": "Pathfinder",
    "car_type": "SUV"
  },
  {
    "year": 2004,
    "manufacturer_name": "Nissan",
    "model_name": "Xterra",
    "car_type": "SUV"
  },
  {
    "year": 2004,
    "manufacturer_name": "Nissan",
    "model_name": "Quest",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2004,
    "manufacturer_name": "Nissan",
    "model_name": "Frontier King Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2004,
    "manufacturer_name": "Nissan",
    "model_name": "Maxima",
    "car_type": "Sedan"
  },
  {
    "year": 2004,
    "manufacturer_name": "Nissan",
    "model_name": "Titan King Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2004,
    "manufacturer_name": "Oldsmobile",
    "model_name": "Bravada",
    "car_type": "SUV"
  },
  {
    "year": 2004,
    "manufacturer_name": "Oldsmobile",
    "model_name": "Alero",
    "car_type": "Coupe, Sedan"
  },
  {
    "year": 2004,
    "manufacturer_name": "Nissan",
    "model_name": "Sentra",
    "car_type": "Sedan"
  },
  {
    "year": 2004,
    "manufacturer_name": "Pontiac",
    "model_name": "Aztek",
    "car_type": "SUV"
  },
  {
    "year": 2004,
    "manufacturer_name": "Nissan",
    "model_name": "Titan Crew Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2004,
    "manufacturer_name": "Nissan",
    "model_name": "Murano",
    "car_type": "SUV"
  },
  {
    "year": 2004,
    "manufacturer_name": "Nissan",
    "model_name": "Pathfinder Armada",
    "car_type": "SUV"
  },
  {
    "year": 2004,
    "manufacturer_name": "Pontiac",
    "model_name": "Bonneville",
    "car_type": "Sedan"
  },
  {
    "year": 2004,
    "manufacturer_name": "Oldsmobile",
    "model_name": "Silhouette",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2004,
    "manufacturer_name": "Porsche",
    "model_name": "Cayenne",
    "car_type": "SUV"
  },
  {
    "year": 2004,
    "manufacturer_name": "Pontiac",
    "model_name": "Vibe",
    "car_type": "Wagon"
  },
  {
    "year": 2004,
    "manufacturer_name": "Pontiac",
    "model_name": "Grand Am",
    "car_type": "Coupe, Sedan"
  },
  {
    "year": 2004,
    "manufacturer_name": "Pontiac",
    "model_name": "Sunfire",
    "car_type": "Coupe"
  },
  {
    "year": 2004,
    "manufacturer_name": "Porsche",
    "model_name": "Carrera GT",
    "car_type": "Convertible"
  },
  {
    "year": 2004,
    "manufacturer_name": "Pontiac",
    "model_name": "Montana",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2004,
    "manufacturer_name": "Pontiac",
    "model_name": "Grand Prix",
    "car_type": "Sedan"
  },
  {
    "year": 2004,
    "manufacturer_name": "Pontiac",
    "model_name": "GTO",
    "car_type": "Coupe"
  },
  {
    "year": 2004,
    "manufacturer_name": "Porsche",
    "model_name": "911",
    "car_type": "Convertible, Coupe"
  },
  {
    "year": 2004,
    "manufacturer_name": "Subaru",
    "model_name": "Legacy",
    "car_type": "Sedan, Wagon"
  },
  {
    "year": 2004,
    "manufacturer_name": "Suzuki",
    "model_name": "Forenza",
    "car_type": "Sedan"
  },
  {
    "year": 2004,
    "manufacturer_name": "Saturn",
    "model_name": "VUE",
    "car_type": "SUV"
  },
  {
    "year": 2004,
    "manufacturer_name": "Saturn",
    "model_name": "Ion",
    "car_type": "Sedan, Coupe"
  },
  {
    "year": 2004,
    "manufacturer_name": "Subaru",
    "model_name": "Outback",
    "car_type": "Sedan, Wagon"
  },
  {
    "year": 2004,
    "manufacturer_name": "Subaru",
    "model_name": "Impreza",
    "car_type": "Wagon, Sedan"
  },
  {
    "year": 2004,
    "manufacturer_name": "Subaru",
    "model_name": "Baja",
    "car_type": "Pickup"
  },
  {
    "year": 2004,
    "manufacturer_name": "Toyota",
    "model_name": "Corolla",
    "car_type": "Sedan"
  },
  {
    "year": 2004,
    "manufacturer_name": "Suzuki",
    "model_name": "Aerio",
    "car_type": "Sedan, Wagon"
  },
  {
    "year": 2004,
    "manufacturer_name": "Saturn",
    "model_name": "L-Series",
    "car_type": "Sedan, Wagon"
  },
  {
    "year": 2004,
    "manufacturer_name": "Subaru",
    "model_name": "Forester",
    "car_type": "SUV"
  },
  {
    "year": 2004,
    "manufacturer_name": "Porsche",
    "model_name": "Boxster",
    "car_type": "Convertible"
  },
  {
    "year": 2004,
    "manufacturer_name": "Toyota",
    "model_name": "Land Cruiser",
    "car_type": "SUV"
  },
  {
    "year": 2004,
    "manufacturer_name": "Suzuki",
    "model_name": "Vitara",
    "car_type": "SUV"
  },
  {
    "year": 2004,
    "manufacturer_name": "Toyota",
    "model_name": "Prius",
    "car_type": "Sedan"
  },
  {
    "year": 2004,
    "manufacturer_name": "Saab",
    "model_name": "3-Sep",
    "car_type": "Sedan, Convertible"
  },
  {
    "year": 2004,
    "manufacturer_name": "Toyota",
    "model_name": "Highlander",
    "car_type": "SUV"
  },
  {
    "year": 2004,
    "manufacturer_name": "Toyota",
    "model_name": "4Runner",
    "car_type": "SUV"
  },
  {
    "year": 2004,
    "manufacturer_name": "Suzuki",
    "model_name": "Verona",
    "car_type": "Sedan"
  },
  {
    "year": 2004,
    "manufacturer_name": "Suzuki",
    "model_name": "Grand Vitara",
    "car_type": "SUV"
  },
  {
    "year": 2004,
    "manufacturer_name": "Saab",
    "model_name": "5-Sep",
    "car_type": "Wagon, Sedan"
  },
  {
    "year": 2004,
    "manufacturer_name": "Toyota",
    "model_name": "Avalon",
    "car_type": "Sedan"
  },
  {
    "year": 2004,
    "manufacturer_name": "Scion",
    "model_name": "xB",
    "car_type": "Hatchback"
  },
  {
    "year": 2004,
    "manufacturer_name": "Toyota",
    "model_name": "Camry",
    "car_type": "Sedan"
  },
  {
    "year": 2004,
    "manufacturer_name": "Toyota",
    "model_name": "MR2",
    "car_type": "Convertible"
  },
  {
    "year": 2004,
    "manufacturer_name": "Toyota",
    "model_name": "Tundra Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2004,
    "manufacturer_name": "Toyota",
    "model_name": "Echo",
    "car_type": "Sedan"
  },
  {
    "year": 2004,
    "manufacturer_name": "Toyota",
    "model_name": "RAV4",
    "car_type": "SUV"
  },
  {
    "year": 2004,
    "manufacturer_name": "Toyota",
    "model_name": "Tacoma Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2004,
    "manufacturer_name": "Toyota",
    "model_name": "Tacoma Double Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2004,
    "manufacturer_name": "Toyota",
    "model_name": "Matrix",
    "car_type": "Hatchback, Wagon"
  },
  {
    "year": 2004,
    "manufacturer_name": "Scion",
    "model_name": "xA",
    "car_type": "Hatchback"
  },
  {
    "year": 2004,
    "manufacturer_name": "Suzuki",
    "model_name": "XL-7",
    "car_type": "SUV"
  },
  {
    "year": 2004,
    "manufacturer_name": "Toyota",
    "model_name": "Solara",
    "car_type": "Coupe, Convertible"
  },
  {
    "year": 2004,
    "manufacturer_name": "Toyota",
    "model_name": "Celica",
    "car_type": "Hatchback"
  },
  {
    "year": 2004,
    "manufacturer_name": "Volvo",
    "model_name": "C70",
    "car_type": "Convertible"
  },
  {
    "year": 2004,
    "manufacturer_name": "Volkswagen",
    "model_name": "New Beetle",
    "car_type": "Hatchback, Convertible"
  },
  {
    "year": 2004,
    "manufacturer_name": "Toyota",
    "model_name": "Tundra Access Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2004,
    "manufacturer_name": "Toyota",
    "model_name": "Sienna",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2004,
    "manufacturer_name": "Volkswagen",
    "model_name": "Phaeton",
    "car_type": "Sedan"
  },
  {
    "year": 2004,
    "manufacturer_name": "Volkswagen",
    "model_name": "Passat",
    "car_type": "Sedan, Wagon"
  },
  {
    "year": 2004,
    "manufacturer_name": "Volkswagen",
    "model_name": "Golf",
    "car_type": "Hatchback"
  },
  {
    "year": 2004,
    "manufacturer_name": "Volkswagen",
    "model_name": "Jetta",
    "car_type": "Wagon, Sedan"
  },
  {
    "year": 2004,
    "manufacturer_name": "Volvo",
    "model_name": "S40 (New)",
    "car_type": "Sedan"
  },
  {
    "year": 2004,
    "manufacturer_name": "Toyota",
    "model_name": "Sequoia",
    "car_type": "SUV"
  },
  {
    "year": 2004,
    "manufacturer_name": "Toyota",
    "model_name": "Tundra Double Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2004,
    "manufacturer_name": "Toyota",
    "model_name": "Tacoma Xtracab",
    "car_type": "Pickup"
  },
  {
    "year": 2004,
    "manufacturer_name": "Volvo",
    "model_name": "S40",
    "car_type": "Sedan"
  },
  {
    "year": 2004,
    "manufacturer_name": "Volvo",
    "model_name": "S60",
    "car_type": "Sedan"
  },
  {
    "year": 2004,
    "manufacturer_name": "Volkswagen",
    "model_name": "R32",
    "car_type": "Hatchback"
  },
  {
    "year": 2004,
    "manufacturer_name": "Volvo",
    "model_name": "V70",
    "car_type": "Wagon"
  },
  {
    "year": 2004,
    "manufacturer_name": "Volkswagen",
    "model_name": "Touareg",
    "car_type": "SUV"
  },
  {
    "year": 2004,
    "manufacturer_name": "Volvo",
    "model_name": "V40",
    "car_type": "Wagon"
  },
  {
    "year": 2004,
    "manufacturer_name": "Volkswagen",
    "model_name": "GTI",
    "car_type": "Hatchback"
  },
  {
    "year": 2004,
    "manufacturer_name": "Volvo",
    "model_name": "S80",
    "car_type": "Sedan"
  },
  {
    "year": 2004,
    "manufacturer_name": "Volvo",
    "model_name": "XC70",
    "car_type": "Wagon"
  },
  {
    "year": 2004,
    "manufacturer_name": "Volvo",
    "model_name": "XC90",
    "car_type": "SUV"
  },
  {
    "year": 2003,
    "manufacturer_name": "Audi",
    "model_name": "A4",
    "car_type": "Wagon, Sedan, Convertible"
  },
  {
    "year": 2003,
    "manufacturer_name": "Acura",
    "model_name": "MDX",
    "car_type": "SUV"
  },
  {
    "year": 2003,
    "manufacturer_name": "Acura",
    "model_name": "RSX",
    "car_type": "Coupe"
  },
  {
    "year": 2003,
    "manufacturer_name": "Acura",
    "model_name": "CL",
    "car_type": "Coupe"
  },
  {
    "year": 2003,
    "manufacturer_name": "Acura",
    "model_name": "TL",
    "car_type": "Sedan"
  },
  {
    "year": 2003,
    "manufacturer_name": "Acura",
    "model_name": "RL",
    "car_type": "Sedan"
  },
  {
    "year": 2003,
    "manufacturer_name": "Audi",
    "model_name": "A6",
    "car_type": "Sedan, Wagon"
  },
  {
    "year": 2003,
    "manufacturer_name": "Acura",
    "model_name": "NSX",
    "car_type": "Coupe"
  },
  {
    "year": 2003,
    "manufacturer_name": "Audi",
    "model_name": "S6",
    "car_type": "Wagon"
  },
  {
    "year": 2003,
    "manufacturer_name": "BMW",
    "model_name": "3 Series",
    "car_type": "Sedan, Convertible, Coupe, Wagon"
  },
  {
    "year": 2003,
    "manufacturer_name": "Cadillac",
    "model_name": "Seville",
    "car_type": "Sedan"
  },
  {
    "year": 2003,
    "manufacturer_name": "Buick",
    "model_name": "Century",
    "car_type": "Sedan"
  },
  {
    "year": 2003,
    "manufacturer_name": "BMW",
    "model_name": "M5",
    "car_type": "Sedan"
  },
  {
    "year": 2003,
    "manufacturer_name": "BMW",
    "model_name": "M3",
    "car_type": "Coupe, Convertible"
  },
  {
    "year": 2003,
    "manufacturer_name": "Audi",
    "model_name": "TT",
    "car_type": "Coupe, Convertible"
  },
  {
    "year": 2003,
    "manufacturer_name": "BMW",
    "model_name": "Z8",
    "car_type": "Convertible"
  },
  {
    "year": 2003,
    "manufacturer_name": "Audi",
    "model_name": "RS 6",
    "car_type": "Sedan"
  },
  {
    "year": 2003,
    "manufacturer_name": "Audi",
    "model_name": "S8",
    "car_type": "Sedan"
  },
  {
    "year": 2003,
    "manufacturer_name": "BMW",
    "model_name": "Z4",
    "car_type": "Convertible"
  },
  {
    "year": 2003,
    "manufacturer_name": "Audi",
    "model_name": "A8",
    "car_type": "Sedan"
  },
  {
    "year": 2003,
    "manufacturer_name": "Audi",
    "model_name": "allroad",
    "car_type": "Wagon"
  },
  {
    "year": 2003,
    "manufacturer_name": "Cadillac",
    "model_name": "Escalade EXT",
    "car_type": "Pickup"
  },
  {
    "year": 2003,
    "manufacturer_name": "Cadillac",
    "model_name": "CTS",
    "car_type": "Sedan"
  },
  {
    "year": 2003,
    "manufacturer_name": "BMW",
    "model_name": "7 Series",
    "car_type": "Sedan"
  },
  {
    "year": 2003,
    "manufacturer_name": "BMW",
    "model_name": "5 Series",
    "car_type": "Sedan, Wagon"
  },
  {
    "year": 2003,
    "manufacturer_name": "Buick",
    "model_name": "Rendezvous",
    "car_type": "SUV"
  },
  {
    "year": 2003,
    "manufacturer_name": "Buick",
    "model_name": "Park Avenue",
    "car_type": "Sedan"
  },
  {
    "year": 2003,
    "manufacturer_name": "Buick",
    "model_name": "Regal",
    "car_type": "Sedan"
  },
  {
    "year": 2003,
    "manufacturer_name": "BMW",
    "model_name": "X5",
    "car_type": "SUV"
  },
  {
    "year": 2003,
    "manufacturer_name": "Chevrolet",
    "model_name": "Astro Passenger",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2003,
    "manufacturer_name": "Chevrolet",
    "model_name": "Corvette",
    "car_type": "Coupe, Convertible"
  },
  {
    "year": 2003,
    "manufacturer_name": "Chevrolet",
    "model_name": "Avalanche 2500",
    "car_type": "Pickup"
  },
  {
    "year": 2003,
    "manufacturer_name": "Chevrolet",
    "model_name": "Blazer",
    "car_type": "SUV"
  },
  {
    "year": 2003,
    "manufacturer_name": "Cadillac",
    "model_name": "Escalade",
    "car_type": "SUV"
  },
  {
    "year": 2003,
    "manufacturer_name": "Chevrolet",
    "model_name": "Express 2500 Cargo",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2003,
    "manufacturer_name": "Cadillac",
    "model_name": "Escalade ESV",
    "car_type": "SUV"
  },
  {
    "year": 2003,
    "manufacturer_name": "Chevrolet",
    "model_name": "Impala",
    "car_type": "Sedan"
  },
  {
    "year": 2003,
    "manufacturer_name": "Chevrolet",
    "model_name": "Silverado 3500 Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2003,
    "manufacturer_name": "Buick",
    "model_name": "LeSabre",
    "car_type": "Sedan"
  },
  {
    "year": 2003,
    "manufacturer_name": "Chevrolet",
    "model_name": "Silverado 2500 HD Extended Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2003,
    "manufacturer_name": "Chevrolet",
    "model_name": "Silverado 2500 HD Crew Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2003,
    "manufacturer_name": "Chevrolet",
    "model_name": "Express 1500 Cargo",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2003,
    "manufacturer_name": "Chevrolet",
    "model_name": "Cavalier",
    "car_type": "Sedan, Coupe"
  },
  {
    "year": 2003,
    "manufacturer_name": "Chevrolet",
    "model_name": "Silverado 1500 Extended Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2003,
    "manufacturer_name": "Chevrolet",
    "model_name": "Avalanche 1500",
    "car_type": "Pickup"
  },
  {
    "year": 2003,
    "manufacturer_name": "Chevrolet",
    "model_name": "Express 3500 Passenger",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2003,
    "manufacturer_name": "Chevrolet",
    "model_name": "Express 1500 Passenger",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2003,
    "manufacturer_name": "Chevrolet",
    "model_name": "Express 2500 Passenger",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2003,
    "manufacturer_name": "Cadillac",
    "model_name": "DeVille",
    "car_type": "Sedan"
  },
  {
    "year": 2003,
    "manufacturer_name": "Chevrolet",
    "model_name": "S10 Extended Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2003,
    "manufacturer_name": "Chevrolet",
    "model_name": "Express 3500 Cargo",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2003,
    "manufacturer_name": "Chevrolet",
    "model_name": "Malibu",
    "car_type": "Sedan"
  },
  {
    "year": 2003,
    "manufacturer_name": "Chevrolet",
    "model_name": "S10 Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2003,
    "manufacturer_name": "Chevrolet",
    "model_name": "Astro Cargo",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2003,
    "manufacturer_name": "Chevrolet",
    "model_name": "S10 Crew Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2003,
    "manufacturer_name": "Chevrolet",
    "model_name": "Silverado 2500 Extended Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2003,
    "manufacturer_name": "Chevrolet",
    "model_name": "Suburban 1500",
    "car_type": "SUV"
  },
  {
    "year": 2003,
    "manufacturer_name": "Chrysler",
    "model_name": "300M",
    "car_type": "Sedan"
  },
  {
    "year": 2003,
    "manufacturer_name": "Dodge",
    "model_name": "Dakota Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2003,
    "manufacturer_name": "Chevrolet",
    "model_name": "Silverado 1500 Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2003,
    "manufacturer_name": "Chevrolet",
    "model_name": "Silverado 3500 Extended Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2003,
    "manufacturer_name": "Chevrolet",
    "model_name": "Silverado 1500 HD Crew Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2003,
    "manufacturer_name": "Chevrolet",
    "model_name": "Venture Cargo",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2003,
    "manufacturer_name": "Chevrolet",
    "model_name": "Silverado 3500 Crew Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2003,
    "manufacturer_name": "Chevrolet",
    "model_name": "Tracker",
    "car_type": "SUV"
  },
  {
    "year": 2003,
    "manufacturer_name": "Chrysler",
    "model_name": "Concorde",
    "car_type": "Sedan"
  },
  {
    "year": 2003,
    "manufacturer_name": "Chevrolet",
    "model_name": "Silverado 2500 Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2003,
    "manufacturer_name": "Chevrolet",
    "model_name": "Monte Carlo",
    "car_type": "Coupe"
  },
  {
    "year": 2003,
    "manufacturer_name": "Dodge",
    "model_name": "Dakota Club Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2003,
    "manufacturer_name": "Chrysler",
    "model_name": "PT Cruiser",
    "car_type": "Wagon"
  },
  {
    "year": 2003,
    "manufacturer_name": "Chevrolet",
    "model_name": "Suburban 2500",
    "car_type": "SUV"
  },
  {
    "year": 2003,
    "manufacturer_name": "Chevrolet",
    "model_name": "Tahoe",
    "car_type": "SUV"
  },
  {
    "year": 2003,
    "manufacturer_name": "Dodge",
    "model_name": "Ram 1500 Quad Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2003,
    "manufacturer_name": "Chrysler",
    "model_name": "Town & Country",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2003,
    "manufacturer_name": "Chevrolet",
    "model_name": "SSR",
    "car_type": "Pickup"
  },
  {
    "year": 2003,
    "manufacturer_name": "Dodge",
    "model_name": "Neon",
    "car_type": "Sedan"
  },
  {
    "year": 2003,
    "manufacturer_name": "Chevrolet",
    "model_name": "Venture Passenger",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2003,
    "manufacturer_name": "Chevrolet",
    "model_name": "Silverado 2500 HD Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2003,
    "manufacturer_name": "Chevrolet",
    "model_name": "TrailBlazer",
    "car_type": "SUV"
  },
  {
    "year": 2003,
    "manufacturer_name": "Chrysler",
    "model_name": "Voyager",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2003,
    "manufacturer_name": "Dodge",
    "model_name": "Caravan Cargo",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2003,
    "manufacturer_name": "Dodge",
    "model_name": "Intrepid",
    "car_type": "Sedan"
  },
  {
    "year": 2003,
    "manufacturer_name": "Dodge",
    "model_name": "Dakota Quad Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2003,
    "manufacturer_name": "Dodge",
    "model_name": "Durango",
    "car_type": "SUV"
  },
  {
    "year": 2003,
    "manufacturer_name": "Chrysler",
    "model_name": "Sebring",
    "car_type": "Sedan, Coupe, Convertible"
  },
  {
    "year": 2003,
    "manufacturer_name": "Dodge",
    "model_name": "Ram Van 1500",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2003,
    "manufacturer_name": "Dodge",
    "model_name": "Ram 3500 Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2003,
    "manufacturer_name": "Dodge",
    "model_name": "Ram Van 2500",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2003,
    "manufacturer_name": "Dodge",
    "model_name": "Caravan Passenger",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2003,
    "manufacturer_name": "Dodge",
    "model_name": "Sprinter 2500 Cargo",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2003,
    "manufacturer_name": "Dodge",
    "model_name": "Ram 3500 Quad Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2003,
    "manufacturer_name": "Dodge",
    "model_name": "Ram Van 3500",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2003,
    "manufacturer_name": "Dodge",
    "model_name": "Grand Caravan Passenger",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2003,
    "manufacturer_name": "Dodge",
    "model_name": "Ram 1500 Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2003,
    "manufacturer_name": "Dodge",
    "model_name": "Ram 2500 Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2003,
    "manufacturer_name": "Dodge",
    "model_name": "Grand Caravan Cargo",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2003,
    "manufacturer_name": "Dodge",
    "model_name": "Ram 2500 Quad Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2003,
    "manufacturer_name": "Dodge",
    "model_name": "Sprinter 2500 Passenger",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2003,
    "manufacturer_name": "Dodge",
    "model_name": "Sprinter 3500 Cargo",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2003,
    "manufacturer_name": "Ford",
    "model_name": "E250 Super Duty Cargo",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2003,
    "manufacturer_name": "Ford",
    "model_name": "Explorer Sport",
    "car_type": "SUV"
  },
  {
    "year": 2003,
    "manufacturer_name": "Ford",
    "model_name": "E150 Passenger",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2003,
    "manufacturer_name": "Dodge",
    "model_name": "Stratus",
    "car_type": "Sedan, Coupe"
  },
  {
    "year": 2003,
    "manufacturer_name": "Ford",
    "model_name": "Explorer",
    "car_type": "SUV"
  },
  {
    "year": 2003,
    "manufacturer_name": "Ford",
    "model_name": "E350 Super Duty Passenger",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2003,
    "manufacturer_name": "Ford",
    "model_name": "E150 Super Duty Cargo",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2003,
    "manufacturer_name": "Dodge",
    "model_name": "Viper",
    "car_type": "Convertible"
  },
  {
    "year": 2003,
    "manufacturer_name": "Ford",
    "model_name": "Crown Victoria",
    "car_type": "Sedan"
  },
  {
    "year": 2003,
    "manufacturer_name": "Ford",
    "model_name": "E350 Super Duty Cargo",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2003,
    "manufacturer_name": "Ford",
    "model_name": "Excursion",
    "car_type": "SUV"
  },
  {
    "year": 2003,
    "manufacturer_name": "Ford",
    "model_name": "Escape",
    "car_type": "SUV"
  },
  {
    "year": 2003,
    "manufacturer_name": "Ford",
    "model_name": "Expedition",
    "car_type": "SUV"
  },
  {
    "year": 2003,
    "manufacturer_name": "Ford",
    "model_name": "F250 Super Duty Crew Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2003,
    "manufacturer_name": "Ford",
    "model_name": "Explorer Sport Trac",
    "car_type": "Pickup"
  },
  {
    "year": 2003,
    "manufacturer_name": "Ford",
    "model_name": "F150 Super Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2003,
    "manufacturer_name": "Ford",
    "model_name": "F350 Super Duty Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2003,
    "manufacturer_name": "GMC",
    "model_name": "Savana 1500 Passenger",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2003,
    "manufacturer_name": "Ford",
    "model_name": "Focus",
    "car_type": "Sedan, Wagon, Hatchback"
  },
  {
    "year": 2003,
    "manufacturer_name": "Ford",
    "model_name": "F350 Super Duty Crew Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2003,
    "manufacturer_name": "Ford",
    "model_name": "F150 SuperCrew Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2003,
    "manufacturer_name": "GMC",
    "model_name": "Safari Cargo",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2003,
    "manufacturer_name": "Ford",
    "model_name": "F150 Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2003,
    "manufacturer_name": "Ford",
    "model_name": "F250 Super Duty Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2003,
    "manufacturer_name": "Ford",
    "model_name": "Windstar Cargo",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2003,
    "manufacturer_name": "Ford",
    "model_name": "ZX2",
    "car_type": "Coupe"
  },
  {
    "year": 2003,
    "manufacturer_name": "Ford",
    "model_name": "Windstar Passenger",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2003,
    "manufacturer_name": "Ford",
    "model_name": "Taurus",
    "car_type": "Sedan, Wagon"
  },
  {
    "year": 2003,
    "manufacturer_name": "Ford",
    "model_name": "Ranger Super Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2003,
    "manufacturer_name": "GMC",
    "model_name": "Envoy",
    "car_type": "SUV"
  },
  {
    "year": 2003,
    "manufacturer_name": "Ford",
    "model_name": "F250 Super Duty Super Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2003,
    "manufacturer_name": "GMC",
    "model_name": "Envoy XL",
    "car_type": "SUV"
  },
  {
    "year": 2003,
    "manufacturer_name": "Ford",
    "model_name": "F350 Super Duty Super Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2003,
    "manufacturer_name": "Ford",
    "model_name": "Mustang",
    "car_type": "Convertible, Coupe"
  },
  {
    "year": 2003,
    "manufacturer_name": "Ford",
    "model_name": "Ranger Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2003,
    "manufacturer_name": "GMC",
    "model_name": "Savana 1500 Cargo",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2003,
    "manufacturer_name": "Ford",
    "model_name": "Thunderbird",
    "car_type": "Convertible"
  },
  {
    "year": 2003,
    "manufacturer_name": "GMC",
    "model_name": "Sierra 1500 HD Crew Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2003,
    "manufacturer_name": "GMC",
    "model_name": "Yukon",
    "car_type": "SUV"
  },
  {
    "year": 2003,
    "manufacturer_name": "GMC",
    "model_name": "Savana 3500 Passenger",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2003,
    "manufacturer_name": "GMC",
    "model_name": "Safari Passenger",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2003,
    "manufacturer_name": "GMC",
    "model_name": "Sierra 3500 Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2003,
    "manufacturer_name": "GMC",
    "model_name": "Sierra 2500 Extended Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2003,
    "manufacturer_name": "GMC",
    "model_name": "Sierra 3500 Crew Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2003,
    "manufacturer_name": "GMC",
    "model_name": "Sierra 2500 HD Crew Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2003,
    "manufacturer_name": "GMC",
    "model_name": "Sierra 1500 Extended Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2003,
    "manufacturer_name": "GMC",
    "model_name": "Savana 2500 Cargo",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2003,
    "manufacturer_name": "GMC",
    "model_name": "Savana 2500 Passenger",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2003,
    "manufacturer_name": "GMC",
    "model_name": "Savana 3500 Cargo",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2003,
    "manufacturer_name": "GMC",
    "model_name": "Sierra 1500 Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2003,
    "manufacturer_name": "GMC",
    "model_name": "Sierra 3500 Extended Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2003,
    "manufacturer_name": "GMC",
    "model_name": "Sierra 2500 Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2003,
    "manufacturer_name": "GMC",
    "model_name": "Sierra 2500 HD Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2003,
    "manufacturer_name": "GMC",
    "model_name": "Sierra 2500 HD Extended Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2003,
    "manufacturer_name": "GMC",
    "model_name": "Sonoma Crew Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2003,
    "manufacturer_name": "Hyundai",
    "model_name": "Tiburon",
    "car_type": "Coupe"
  },
  {
    "year": 2003,
    "manufacturer_name": "GMC",
    "model_name": "Yukon XL 1500",
    "car_type": "SUV"
  },
  {
    "year": 2003,
    "manufacturer_name": "Honda",
    "model_name": "Insight",
    "car_type": "Hatchback"
  },
  {
    "year": 2003,
    "manufacturer_name": "INFINITI",
    "model_name": "I",
    "car_type": "Sedan"
  },
  {
    "year": 2003,
    "manufacturer_name": "Honda",
    "model_name": "CR-V",
    "car_type": "SUV"
  },
  {
    "year": 2003,
    "manufacturer_name": "INFINITI",
    "model_name": "QX",
    "car_type": "SUV"
  },
  {
    "year": 2003,
    "manufacturer_name": "GMC",
    "model_name": "Sonoma Extended Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2003,
    "manufacturer_name": "Honda",
    "model_name": "Civic",
    "car_type": "Coupe, Sedan, Hatchback"
  },
  {
    "year": 2003,
    "manufacturer_name": "Honda",
    "model_name": "Accord",
    "car_type": "Sedan, Coupe"
  },
  {
    "year": 2003,
    "manufacturer_name": "GMC",
    "model_name": "Sonoma Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2003,
    "manufacturer_name": "Hyundai",
    "model_name": "XG350",
    "car_type": "Sedan"
  },
  {
    "year": 2003,
    "manufacturer_name": "HUMMER",
    "model_name": "H2",
    "car_type": "SUV"
  },
  {
    "year": 2003,
    "manufacturer_name": "HUMMER",
    "model_name": "H1",
    "car_type": "Wagon, SUV"
  },
  {
    "year": 2003,
    "manufacturer_name": "GMC",
    "model_name": "Yukon XL 2500",
    "car_type": "SUV"
  },
  {
    "year": 2003,
    "manufacturer_name": "Hyundai",
    "model_name": "Elantra",
    "car_type": "Sedan, Hatchback"
  },
  {
    "year": 2003,
    "manufacturer_name": "Honda",
    "model_name": "Pilot",
    "car_type": "SUV"
  },
  {
    "year": 2003,
    "manufacturer_name": "Honda",
    "model_name": "Element",
    "car_type": "SUV"
  },
  {
    "year": 2003,
    "manufacturer_name": "Jaguar",
    "model_name": "XJ",
    "car_type": "Sedan"
  },
  {
    "year": 2003,
    "manufacturer_name": "INFINITI",
    "model_name": "M",
    "car_type": "Sedan"
  },
  {
    "year": 2003,
    "manufacturer_name": "INFINITI",
    "model_name": "G",
    "car_type": "Sedan, Coupe"
  },
  {
    "year": 2003,
    "manufacturer_name": "Hyundai",
    "model_name": "Sonata",
    "car_type": "Sedan"
  },
  {
    "year": 2003,
    "manufacturer_name": "Honda",
    "model_name": "Odyssey",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2003,
    "manufacturer_name": "INFINITI",
    "model_name": "Q",
    "car_type": "Sedan"
  },
  {
    "year": 2003,
    "manufacturer_name": "Honda",
    "model_name": "S2000",
    "car_type": "Convertible"
  },
  {
    "year": 2003,
    "manufacturer_name": "Hyundai",
    "model_name": "Accent",
    "car_type": "Hatchback, Sedan"
  },
  {
    "year": 2003,
    "manufacturer_name": "Isuzu",
    "model_name": "Axiom",
    "car_type": "SUV"
  },
  {
    "year": 2003,
    "manufacturer_name": "INFINITI",
    "model_name": "FX",
    "car_type": "SUV"
  },
  {
    "year": 2003,
    "manufacturer_name": "Hyundai",
    "model_name": "Santa Fe",
    "car_type": "SUV"
  },
  {
    "year": 2003,
    "manufacturer_name": "Isuzu",
    "model_name": "Ascender",
    "car_type": "SUV"
  },
  {
    "year": 2003,
    "manufacturer_name": "Isuzu",
    "model_name": "Rodeo",
    "car_type": "SUV"
  },
  {
    "year": 2003,
    "manufacturer_name": "Jaguar",
    "model_name": "S-Type",
    "car_type": "Sedan"
  },
  {
    "year": 2003,
    "manufacturer_name": "Jeep",
    "model_name": "Wrangler",
    "car_type": "SUV"
  },
  {
    "year": 2003,
    "manufacturer_name": "Kia",
    "model_name": "Spectra",
    "car_type": "Sedan, Hatchback"
  },
  {
    "year": 2003,
    "manufacturer_name": "Kia",
    "model_name": "Sorento",
    "car_type": "SUV"
  },
  {
    "year": 2003,
    "manufacturer_name": "Land Rover",
    "model_name": "Freelander",
    "car_type": "SUV"
  },
  {
    "year": 2003,
    "manufacturer_name": "Jeep",
    "model_name": "Grand Cherokee",
    "car_type": "SUV"
  },
  {
    "year": 2003,
    "manufacturer_name": "Kia",
    "model_name": "Sedona",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2003,
    "manufacturer_name": "Jeep",
    "model_name": "Liberty",
    "car_type": "SUV"
  },
  {
    "year": 2003,
    "manufacturer_name": "Land Rover",
    "model_name": "Discovery",
    "car_type": "SUV"
  },
  {
    "year": 2003,
    "manufacturer_name": "Isuzu",
    "model_name": "Rodeo Sport",
    "car_type": "SUV"
  },
  {
    "year": 2003,
    "manufacturer_name": "Kia",
    "model_name": "Rio",
    "car_type": "Sedan, Wagon"
  },
  {
    "year": 2003,
    "manufacturer_name": "Jaguar",
    "model_name": "X-Type",
    "car_type": "Sedan"
  },
  {
    "year": 2003,
    "manufacturer_name": "Jaguar",
    "model_name": "XK",
    "car_type": "Coupe, Convertible"
  },
  {
    "year": 2003,
    "manufacturer_name": "Kia",
    "model_name": "Optima",
    "car_type": "Sedan"
  },
  {
    "year": 2003,
    "manufacturer_name": "Land Rover",
    "model_name": "Range Rover",
    "car_type": "SUV"
  },
  {
    "year": 2003,
    "manufacturer_name": "Lexus",
    "model_name": "GX",
    "car_type": "SUV"
  },
  {
    "year": 2003,
    "manufacturer_name": "Lincoln",
    "model_name": "Aviator",
    "car_type": "SUV"
  },
  {
    "year": 2003,
    "manufacturer_name": "Lexus",
    "model_name": "GS",
    "car_type": "Sedan"
  },
  {
    "year": 2003,
    "manufacturer_name": "MAZDA",
    "model_name": "Tribute",
    "car_type": "SUV"
  },
  {
    "year": 2003,
    "manufacturer_name": "Lexus",
    "model_name": "IS",
    "car_type": "Hatchback, Sedan"
  },
  {
    "year": 2003,
    "manufacturer_name": "Lexus",
    "model_name": "LS",
    "car_type": "Sedan"
  },
  {
    "year": 2003,
    "manufacturer_name": "Lexus",
    "model_name": "ES",
    "car_type": "Sedan"
  },
  {
    "year": 2003,
    "manufacturer_name": "MAZDA",
    "model_name": "MPV",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2003,
    "manufacturer_name": "Lexus",
    "model_name": "RX",
    "car_type": "SUV"
  },
  {
    "year": 2003,
    "manufacturer_name": "Lexus",
    "model_name": "SC",
    "car_type": "Convertible"
  },
  {
    "year": 2003,
    "manufacturer_name": "Mercedes-Benz",
    "model_name": "CL-Class",
    "car_type": "Coupe"
  },
  {
    "year": 2003,
    "manufacturer_name": "MAZDA",
    "model_name": "B-Series Cab Plus",
    "car_type": "Pickup"
  },
  {
    "year": 2003,
    "manufacturer_name": "Mercedes-Benz",
    "model_name": "E-Class",
    "car_type": "Sedan, Wagon"
  },
  {
    "year": 2003,
    "manufacturer_name": "Lincoln",
    "model_name": "Navigator",
    "car_type": "SUV"
  },
  {
    "year": 2003,
    "manufacturer_name": "MAZDA",
    "model_name": "MX-5 Miata",
    "car_type": "Convertible"
  },
  {
    "year": 2003,
    "manufacturer_name": "MAZDA",
    "model_name": "Protege5",
    "car_type": "Hatchback"
  },
  {
    "year": 2003,
    "manufacturer_name": "Mercedes-Benz",
    "model_name": "CLK-Class",
    "car_type": "Convertible, Coupe"
  },
  {
    "year": 2003,
    "manufacturer_name": "MAZDA",
    "model_name": "B-Series Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2003,
    "manufacturer_name": "MAZDA",
    "model_name": "Protege",
    "car_type": "Sedan"
  },
  {
    "year": 2003,
    "manufacturer_name": "Mercedes-Benz",
    "model_name": "G-Class",
    "car_type": "SUV"
  },
  {
    "year": 2003,
    "manufacturer_name": "Mercedes-Benz",
    "model_name": "C-Class",
    "car_type": "Coupe, Sedan, Wagon"
  },
  {
    "year": 2003,
    "manufacturer_name": "Lexus",
    "model_name": "LX",
    "car_type": "SUV"
  },
  {
    "year": 2003,
    "manufacturer_name": "Mercedes-Benz",
    "model_name": "SLK-Class",
    "car_type": "Convertible"
  },
  {
    "year": 2003,
    "manufacturer_name": "Lincoln",
    "model_name": "LS",
    "car_type": "Sedan"
  },
  {
    "year": 2003,
    "manufacturer_name": "Mercedes-Benz",
    "model_name": "S-Class",
    "car_type": "Sedan"
  },
  {
    "year": 2003,
    "manufacturer_name": "MAZDA",
    "model_name": "MAZDA6",
    "car_type": "Sedan"
  },
  {
    "year": 2003,
    "manufacturer_name": "Mercedes-Benz",
    "model_name": "M-Class",
    "car_type": "SUV"
  },
  {
    "year": 2003,
    "manufacturer_name": "Lincoln",
    "model_name": "Town Car",
    "car_type": "Sedan"
  },
  {
    "year": 2003,
    "manufacturer_name": "Mercedes-Benz",
    "model_name": "SL-Class",
    "car_type": "Convertible"
  },
  {
    "year": 2003,
    "manufacturer_name": "Mercury",
    "model_name": "Mountaineer",
    "car_type": "SUV"
  },
  {
    "year": 2003,
    "manufacturer_name": "Mercury",
    "model_name": "Sable",
    "car_type": "Sedan, Wagon"
  },
  {
    "year": 2003,
    "manufacturer_name": "MINI",
    "model_name": "Cooper",
    "car_type": "Hatchback"
  },
  {
    "year": 2003,
    "manufacturer_name": "Mercury",
    "model_name": "Grand Marquis",
    "car_type": "Sedan"
  },
  {
    "year": 2003,
    "manufacturer_name": "Mercury",
    "model_name": "Marauder",
    "car_type": "Sedan"
  },
  {
    "year": 2003,
    "manufacturer_name": "Mitsubishi",
    "model_name": "Eclipse",
    "car_type": "Coupe, Convertible"
  },
  {
    "year": 2003,
    "manufacturer_name": "Nissan",
    "model_name": "Murano",
    "car_type": "SUV"
  },
  {
    "year": 2003,
    "manufacturer_name": "Nissan",
    "model_name": "Xterra",
    "car_type": "SUV"
  },
  {
    "year": 2003,
    "manufacturer_name": "Oldsmobile",
    "model_name": "Bravada",
    "car_type": "SUV"
  },
  {
    "year": 2003,
    "manufacturer_name": "Nissan",
    "model_name": "350Z",
    "car_type": "Coupe"
  },
  {
    "year": 2003,
    "manufacturer_name": "Mitsubishi",
    "model_name": "Montero",
    "car_type": "SUV"
  },
  {
    "year": 2003,
    "manufacturer_name": "Mitsubishi",
    "model_name": "Galant",
    "car_type": "Sedan"
  },
  {
    "year": 2003,
    "manufacturer_name": "Mitsubishi",
    "model_name": "Lancer",
    "car_type": "Sedan"
  },
  {
    "year": 2003,
    "manufacturer_name": "Mitsubishi",
    "model_name": "Diamante",
    "car_type": "Sedan"
  },
  {
    "year": 2003,
    "manufacturer_name": "Nissan",
    "model_name": "Frontier Crew Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2003,
    "manufacturer_name": "Nissan",
    "model_name": "Pathfinder",
    "car_type": "SUV"
  },
  {
    "year": 2003,
    "manufacturer_name": "Oldsmobile",
    "model_name": "Silhouette",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2003,
    "manufacturer_name": "Mitsubishi",
    "model_name": "Outlander",
    "car_type": "SUV"
  },
  {
    "year": 2003,
    "manufacturer_name": "Nissan",
    "model_name": "Frontier King Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2003,
    "manufacturer_name": "Nissan",
    "model_name": "Altima",
    "car_type": "Sedan"
  },
  {
    "year": 2003,
    "manufacturer_name": "Nissan",
    "model_name": "Maxima",
    "car_type": "Sedan"
  },
  {
    "year": 2003,
    "manufacturer_name": "Mitsubishi",
    "model_name": "Montero Sport",
    "car_type": "SUV"
  },
  {
    "year": 2003,
    "manufacturer_name": "Oldsmobile",
    "model_name": "Aurora",
    "car_type": "Sedan"
  },
  {
    "year": 2003,
    "manufacturer_name": "Nissan",
    "model_name": "Sentra",
    "car_type": "Sedan"
  },
  {
    "year": 2003,
    "manufacturer_name": "Oldsmobile",
    "model_name": "Alero",
    "car_type": "Sedan, Coupe"
  },
  {
    "year": 2003,
    "manufacturer_name": "Toyota",
    "model_name": "Echo",
    "car_type": "Sedan"
  },
  {
    "year": 2003,
    "manufacturer_name": "Pontiac",
    "model_name": "Montana",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2003,
    "manufacturer_name": "Pontiac",
    "model_name": "Bonneville",
    "car_type": "Sedan"
  },
  {
    "year": 2003,
    "manufacturer_name": "Porsche",
    "model_name": "911",
    "car_type": "Convertible, Coupe"
  },
  {
    "year": 2003,
    "manufacturer_name": "Pontiac",
    "model_name": "Grand Prix",
    "car_type": "Sedan"
  },
  {
    "year": 2003,
    "manufacturer_name": "Porsche",
    "model_name": "Cayenne",
    "car_type": "SUV"
  },
  {
    "year": 2003,
    "manufacturer_name": "Saab",
    "model_name": "5-Sep",
    "car_type": "Sedan, Wagon"
  },
  {
    "year": 2003,
    "manufacturer_name": "Pontiac",
    "model_name": "Vibe",
    "car_type": "Wagon"
  },
  {
    "year": 2003,
    "manufacturer_name": "Subaru",
    "model_name": "Outback",
    "car_type": "Wagon, Sedan"
  },
  {
    "year": 2003,
    "manufacturer_name": "Suzuki",
    "model_name": "Grand Vitara",
    "car_type": "SUV"
  },
  {
    "year": 2003,
    "manufacturer_name": "Subaru",
    "model_name": "Forester",
    "car_type": "SUV"
  },
  {
    "year": 2003,
    "manufacturer_name": "Pontiac",
    "model_name": "Aztek",
    "car_type": "SUV"
  },
  {
    "year": 2003,
    "manufacturer_name": "Pontiac",
    "model_name": "Sunfire",
    "car_type": "Coupe"
  },
  {
    "year": 2003,
    "manufacturer_name": "Porsche",
    "model_name": "Boxster",
    "car_type": "Convertible"
  },
  {
    "year": 2003,
    "manufacturer_name": "Suzuki",
    "model_name": "Aerio",
    "car_type": "Sedan, Wagon"
  },
  {
    "year": 2003,
    "manufacturer_name": "Pontiac",
    "model_name": "Grand Am",
    "car_type": "Sedan, Coupe"
  },
  {
    "year": 2003,
    "manufacturer_name": "Toyota",
    "model_name": "4Runner",
    "car_type": "SUV"
  },
  {
    "year": 2003,
    "manufacturer_name": "Subaru",
    "model_name": "Impreza",
    "car_type": "Wagon, Sedan"
  },
  {
    "year": 2003,
    "manufacturer_name": "Subaru",
    "model_name": "Legacy",
    "car_type": "Sedan, Wagon"
  },
  {
    "year": 2003,
    "manufacturer_name": "Saturn",
    "model_name": "L-Series",
    "car_type": "Sedan, Wagon"
  },
  {
    "year": 2003,
    "manufacturer_name": "Saturn",
    "model_name": "VUE",
    "car_type": "SUV"
  },
  {
    "year": 2003,
    "manufacturer_name": "Subaru",
    "model_name": "Baja",
    "car_type": "Pickup"
  },
  {
    "year": 2003,
    "manufacturer_name": "Toyota",
    "model_name": "Sienna",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2003,
    "manufacturer_name": "Toyota",
    "model_name": "Celica",
    "car_type": "Hatchback"
  },
  {
    "year": 2003,
    "manufacturer_name": "Saturn",
    "model_name": "Ion",
    "car_type": "Sedan, Coupe"
  },
  {
    "year": 2003,
    "manufacturer_name": "Toyota",
    "model_name": "Camry",
    "car_type": "Sedan"
  },
  {
    "year": 2003,
    "manufacturer_name": "Toyota",
    "model_name": "Matrix",
    "car_type": "Wagon"
  },
  {
    "year": 2003,
    "manufacturer_name": "Saab",
    "model_name": "3-Sep",
    "car_type": "Convertible, Sedan"
  },
  {
    "year": 2003,
    "manufacturer_name": "Toyota",
    "model_name": "Prius",
    "car_type": "Sedan"
  },
  {
    "year": 2003,
    "manufacturer_name": "Suzuki",
    "model_name": "XL-7",
    "car_type": "SUV"
  },
  {
    "year": 2003,
    "manufacturer_name": "Suzuki",
    "model_name": "Vitara",
    "car_type": "SUV"
  },
  {
    "year": 2003,
    "manufacturer_name": "Toyota",
    "model_name": "Corolla",
    "car_type": "Sedan"
  },
  {
    "year": 2003,
    "manufacturer_name": "Toyota",
    "model_name": "MR2",
    "car_type": "Convertible"
  },
  {
    "year": 2003,
    "manufacturer_name": "Toyota",
    "model_name": "Avalon",
    "car_type": "Sedan"
  },
  {
    "year": 2003,
    "manufacturer_name": "Toyota",
    "model_name": "Land Cruiser",
    "car_type": "SUV"
  },
  {
    "year": 2003,
    "manufacturer_name": "Toyota",
    "model_name": "Tacoma Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2003,
    "manufacturer_name": "Toyota",
    "model_name": "RAV4",
    "car_type": "SUV"
  },
  {
    "year": 2003,
    "manufacturer_name": "Volkswagen",
    "model_name": "Eurovan",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2003,
    "manufacturer_name": "Toyota",
    "model_name": "Tacoma Double Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2003,
    "manufacturer_name": "Toyota",
    "model_name": "Tundra Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2003,
    "manufacturer_name": "Toyota",
    "model_name": "Tundra Access Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2003,
    "manufacturer_name": "Toyota",
    "model_name": "Highlander",
    "car_type": "SUV"
  },
  {
    "year": 2003,
    "manufacturer_name": "Toyota",
    "model_name": "Tacoma Xtracab",
    "car_type": "Pickup"
  },
  {
    "year": 2003,
    "manufacturer_name": "Toyota",
    "model_name": "Sequoia",
    "car_type": "SUV"
  },
  {
    "year": 2003,
    "manufacturer_name": "Toyota",
    "model_name": "Solara",
    "car_type": "Coupe, Convertible"
  },
  {
    "year": 2003,
    "manufacturer_name": "Volkswagen",
    "model_name": "GTI",
    "car_type": "Hatchback"
  },
  {
    "year": 2002,
    "manufacturer_name": "Acura",
    "model_name": "MDX",
    "car_type": "SUV"
  },
  {
    "year": 2003,
    "manufacturer_name": "Volkswagen",
    "model_name": "New Beetle",
    "car_type": "Convertible, Hatchback"
  },
  {
    "year": 2003,
    "manufacturer_name": "Volkswagen",
    "model_name": "Golf",
    "car_type": "Hatchback"
  },
  {
    "year": 2003,
    "manufacturer_name": "Volvo",
    "model_name": "XC90",
    "car_type": "SUV"
  },
  {
    "year": 2003,
    "manufacturer_name": "Volkswagen",
    "model_name": "Passat",
    "car_type": "Wagon, Sedan"
  },
  {
    "year": 2002,
    "manufacturer_name": "Acura",
    "model_name": "CL",
    "car_type": "Coupe"
  },
  {
    "year": 2003,
    "manufacturer_name": "Volvo",
    "model_name": "S60",
    "car_type": "Sedan"
  },
  {
    "year": 2003,
    "manufacturer_name": "Volvo",
    "model_name": "S80",
    "car_type": "Sedan"
  },
  {
    "year": 2003,
    "manufacturer_name": "Volkswagen",
    "model_name": "Jetta",
    "car_type": "Wagon, Sedan"
  },
  {
    "year": 2003,
    "manufacturer_name": "Volvo",
    "model_name": "V40",
    "car_type": "Wagon"
  },
  {
    "year": 2003,
    "manufacturer_name": "Volvo",
    "model_name": "C70",
    "car_type": "Convertible"
  },
  {
    "year": 2002,
    "manufacturer_name": "Audi",
    "model_name": "allroad",
    "car_type": "Wagon"
  },
  {
    "year": 2002,
    "manufacturer_name": "Audi",
    "model_name": "S6",
    "car_type": "Wagon"
  },
  {
    "year": 2002,
    "manufacturer_name": "BMW",
    "model_name": "7 Series",
    "car_type": "Sedan"
  },
  {
    "year": 2002,
    "manufacturer_name": "Acura",
    "model_name": "TL",
    "car_type": "Sedan"
  },
  {
    "year": 2002,
    "manufacturer_name": "Audi",
    "model_name": "A4",
    "car_type": "Sedan, Wagon"
  },
  {
    "year": 2002,
    "manufacturer_name": "Acura",
    "model_name": "RSX",
    "car_type": "Coupe"
  },
  {
    "year": 2003,
    "manufacturer_name": "Volvo",
    "model_name": "V70",
    "car_type": "Wagon"
  },
  {
    "year": 2002,
    "manufacturer_name": "BMW",
    "model_name": "5 Series",
    "car_type": "Sedan, Wagon"
  },
  {
    "year": 2003,
    "manufacturer_name": "Volvo",
    "model_name": "XC70",
    "car_type": "Wagon"
  },
  {
    "year": 2002,
    "manufacturer_name": "Audi",
    "model_name": "S4",
    "car_type": "Wagon, Sedan"
  },
  {
    "year": 2003,
    "manufacturer_name": "Volvo",
    "model_name": "S40",
    "car_type": "Sedan"
  },
  {
    "year": 2002,
    "manufacturer_name": "Buick",
    "model_name": "Park Avenue",
    "car_type": "Sedan"
  },
  {
    "year": 2002,
    "manufacturer_name": "Audi",
    "model_name": "S8",
    "car_type": "Sedan"
  },
  {
    "year": 2002,
    "manufacturer_name": "BMW",
    "model_name": "Z3",
    "car_type": "Convertible, Coupe"
  },
  {
    "year": 2002,
    "manufacturer_name": "Chevrolet",
    "model_name": "Avalanche 1500",
    "car_type": "Pickup"
  },
  {
    "year": 2002,
    "manufacturer_name": "Acura",
    "model_name": "NSX",
    "car_type": "Coupe"
  },
  {
    "year": 2002,
    "manufacturer_name": "Audi",
    "model_name": "TT",
    "car_type": "Hatchback, Convertible"
  },
  {
    "year": 2002,
    "manufacturer_name": "BMW",
    "model_name": "M5",
    "car_type": "Sedan"
  },
  {
    "year": 2002,
    "manufacturer_name": "BMW",
    "model_name": "M3",
    "car_type": "Convertible, Coupe"
  },
  {
    "year": 2002,
    "manufacturer_name": "BMW",
    "model_name": "3 Series",
    "car_type": "Sedan, Coupe, Convertible, Wagon"
  },
  {
    "year": 2002,
    "manufacturer_name": "Chevrolet",
    "model_name": "Avalanche 2500",
    "car_type": "Pickup"
  },
  {
    "year": 2002,
    "manufacturer_name": "Chevrolet",
    "model_name": "Astro Passenger",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2002,
    "manufacturer_name": "Audi",
    "model_name": "A6",
    "car_type": "Wagon, Sedan"
  },
  {
    "year": 2002,
    "manufacturer_name": "BMW",
    "model_name": "X5",
    "car_type": "SUV"
  },
  {
    "year": 2002,
    "manufacturer_name": "Acura",
    "model_name": "RL",
    "car_type": "Sedan"
  },
  {
    "year": 2002,
    "manufacturer_name": "BMW",
    "model_name": "Z8",
    "car_type": "Convertible"
  },
  {
    "year": 2002,
    "manufacturer_name": "Buick",
    "model_name": "Century",
    "car_type": "Sedan"
  },
  {
    "year": 2002,
    "manufacturer_name": "Buick",
    "model_name": "LeSabre",
    "car_type": "Sedan"
  },
  {
    "year": 2002,
    "manufacturer_name": "Chevrolet",
    "model_name": "Corvette",
    "car_type": "Coupe, Convertible"
  },
  {
    "year": 2002,
    "manufacturer_name": "Cadillac",
    "model_name": "Escalade",
    "car_type": "SUV"
  },
  {
    "year": 2002,
    "manufacturer_name": "Cadillac",
    "model_name": "DeVille",
    "car_type": "Sedan"
  },
  {
    "year": 2002,
    "manufacturer_name": "Buick",
    "model_name": "Regal",
    "car_type": "Sedan"
  },
  {
    "year": 2002,
    "manufacturer_name": "Chevrolet",
    "model_name": "Cavalier",
    "car_type": "Sedan, Coupe"
  },
  {
    "year": 2002,
    "manufacturer_name": "Cadillac",
    "model_name": "Escalade EXT",
    "car_type": "Pickup"
  },
  {
    "year": 2002,
    "manufacturer_name": "Audi",
    "model_name": "A8",
    "car_type": "Sedan"
  },
  {
    "year": 2002,
    "manufacturer_name": "Buick",
    "model_name": "Rendezvous",
    "car_type": "SUV"
  },
  {
    "year": 2002,
    "manufacturer_name": "Chevrolet",
    "model_name": "Express 1500 Cargo",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2002,
    "manufacturer_name": "Cadillac",
    "model_name": "Eldorado",
    "car_type": "Coupe"
  },
  {
    "year": 2002,
    "manufacturer_name": "BMW",
    "model_name": "M",
    "car_type": "Coupe, Convertible"
  },
  {
    "year": 2002,
    "manufacturer_name": "Chevrolet",
    "model_name": "Silverado 1500 HD Crew Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2002,
    "manufacturer_name": "Chevrolet",
    "model_name": "Express 3500 Passenger",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2002,
    "manufacturer_name": "Chevrolet",
    "model_name": "Camaro",
    "car_type": "Coupe, Convertible"
  },
  {
    "year": 2002,
    "manufacturer_name": "Chevrolet",
    "model_name": "Astro Cargo",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2002,
    "manufacturer_name": "Chevrolet",
    "model_name": "Express 2500 Cargo",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2002,
    "manufacturer_name": "Chevrolet",
    "model_name": "Silverado 2500 HD Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2002,
    "manufacturer_name": "Chevrolet",
    "model_name": "Blazer",
    "car_type": "SUV"
  },
  {
    "year": 2002,
    "manufacturer_name": "Chevrolet",
    "model_name": "Express 3500 Cargo",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2002,
    "manufacturer_name": "Chevrolet",
    "model_name": "Express 2500 Passenger",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2002,
    "manufacturer_name": "Chevrolet",
    "model_name": "Silverado 1500 Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2002,
    "manufacturer_name": "Chevrolet",
    "model_name": "Prizm",
    "car_type": "Sedan"
  },
  {
    "year": 2002,
    "manufacturer_name": "Chevrolet",
    "model_name": "S10 Crew Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2002,
    "manufacturer_name": "Chevrolet",
    "model_name": "Monte Carlo",
    "car_type": "Coupe"
  },
  {
    "year": 2002,
    "manufacturer_name": "Cadillac",
    "model_name": "Seville",
    "car_type": "Sedan"
  },
  {
    "year": 2002,
    "manufacturer_name": "Chevrolet",
    "model_name": "Malibu",
    "car_type": "Sedan"
  },
  {
    "year": 2002,
    "manufacturer_name": "Chevrolet",
    "model_name": "Silverado 2500 Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2002,
    "manufacturer_name": "Chevrolet",
    "model_name": "Express 1500 Passenger",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2002,
    "manufacturer_name": "Chevrolet",
    "model_name": "Silverado 1500 Extended Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2002,
    "manufacturer_name": "Chevrolet",
    "model_name": "Silverado 2500 HD Extended Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2002,
    "manufacturer_name": "Chevrolet",
    "model_name": "Impala",
    "car_type": "Sedan"
  },
  {
    "year": 2002,
    "manufacturer_name": "Chevrolet",
    "model_name": "Suburban 1500",
    "car_type": "SUV"
  },
  {
    "year": 2002,
    "manufacturer_name": "Chevrolet",
    "model_name": "S10 Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2002,
    "manufacturer_name": "Chrysler",
    "model_name": "Prowler",
    "car_type": "Convertible"
  },
  {
    "year": 2002,
    "manufacturer_name": "Dodge",
    "model_name": "Dakota Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2002,
    "manufacturer_name": "Chevrolet",
    "model_name": "TrailBlazer",
    "car_type": "SUV"
  },
  {
    "year": 2002,
    "manufacturer_name": "Chevrolet",
    "model_name": "Silverado 2500 Extended Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2002,
    "manufacturer_name": "Chevrolet",
    "model_name": "Venture Passenger",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2002,
    "manufacturer_name": "Chevrolet",
    "model_name": "Suburban 2500",
    "car_type": "SUV"
  },
  {
    "year": 2002,
    "manufacturer_name": "Dodge",
    "model_name": "Durango",
    "car_type": "SUV"
  },
  {
    "year": 2002,
    "manufacturer_name": "Chevrolet",
    "model_name": "Silverado 3500 Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2002,
    "manufacturer_name": "Chevrolet",
    "model_name": "Venture Cargo",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2002,
    "manufacturer_name": "Chevrolet",
    "model_name": "Silverado 2500 HD Crew Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2002,
    "manufacturer_name": "Chevrolet",
    "model_name": "Tracker",
    "car_type": "SUV"
  },
  {
    "year": 2002,
    "manufacturer_name": "Chrysler",
    "model_name": "PT Cruiser",
    "car_type": "Wagon"
  },
  {
    "year": 2002,
    "manufacturer_name": "Chrysler",
    "model_name": "Sebring",
    "car_type": "Sedan, Convertible, Coupe"
  },
  {
    "year": 2002,
    "manufacturer_name": "Chevrolet",
    "model_name": "Silverado 3500 Extended Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2002,
    "manufacturer_name": "Chevrolet",
    "model_name": "S10 Extended Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2002,
    "manufacturer_name": "Chevrolet",
    "model_name": "Tahoe",
    "car_type": "SUV"
  },
  {
    "year": 2002,
    "manufacturer_name": "Daewoo",
    "model_name": "Nubira",
    "car_type": "Sedan, Wagon"
  },
  {
    "year": 2002,
    "manufacturer_name": "Daewoo",
    "model_name": "Leganza",
    "car_type": "Sedan"
  },
  {
    "year": 2002,
    "manufacturer_name": "Chevrolet",
    "model_name": "Silverado 3500 Crew Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2002,
    "manufacturer_name": "Dodge",
    "model_name": "Dakota Quad Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2002,
    "manufacturer_name": "Chrysler",
    "model_name": "Town & Country",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2002,
    "manufacturer_name": "Chrysler",
    "model_name": "Concorde",
    "car_type": "Sedan"
  },
  {
    "year": 2002,
    "manufacturer_name": "Chrysler",
    "model_name": "Voyager",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2002,
    "manufacturer_name": "Chrysler",
    "model_name": "300M",
    "car_type": "Sedan"
  },
  {
    "year": 2002,
    "manufacturer_name": "Daewoo",
    "model_name": "Lanos",
    "car_type": "Sedan, Hatchback"
  },
  {
    "year": 2002,
    "manufacturer_name": "Dodge",
    "model_name": "Dakota Club Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2002,
    "manufacturer_name": "Dodge",
    "model_name": "Caravan Passenger",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2002,
    "manufacturer_name": "Dodge",
    "model_name": "Grand Caravan Passenger",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2002,
    "manufacturer_name": "Dodge",
    "model_name": "Ram Van 2500",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2002,
    "manufacturer_name": "Ford",
    "model_name": "Explorer Sport",
    "car_type": "SUV"
  },
  {
    "year": 2002,
    "manufacturer_name": "Dodge",
    "model_name": "Ram 1500 Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2002,
    "manufacturer_name": "Dodge",
    "model_name": "Ram 2500 Quad Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2002,
    "manufacturer_name": "Dodge",
    "model_name": "Viper",
    "car_type": "Convertible, Coupe"
  },
  {
    "year": 2002,
    "manufacturer_name": "Ford",
    "model_name": "Econoline E250 Cargo",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2002,
    "manufacturer_name": "Ford",
    "model_name": "Econoline E350 Super Duty Passenger",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2002,
    "manufacturer_name": "Dodge",
    "model_name": "Neon",
    "car_type": "Sedan"
  },
  {
    "year": 2002,
    "manufacturer_name": "Dodge",
    "model_name": "Ram Wagon 2500",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2002,
    "manufacturer_name": "Dodge",
    "model_name": "Intrepid",
    "car_type": "Sedan"
  },
  {
    "year": 2002,
    "manufacturer_name": "Ford",
    "model_name": "Econoline E150 Cargo",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2002,
    "manufacturer_name": "Ford",
    "model_name": "Crown Victoria",
    "car_type": "Sedan"
  },
  {
    "year": 2002,
    "manufacturer_name": "Dodge",
    "model_name": "Ram 3500 Quad Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2002,
    "manufacturer_name": "Ford",
    "model_name": "Econoline E150 Passenger",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2002,
    "manufacturer_name": "Dodge",
    "model_name": "Ram 3500 Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2002,
    "manufacturer_name": "Dodge",
    "model_name": "Ram Wagon 1500",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2002,
    "manufacturer_name": "Ford",
    "model_name": "Explorer",
    "car_type": "SUV"
  },
  {
    "year": 2002,
    "manufacturer_name": "Dodge",
    "model_name": "Ram Van 1500",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2002,
    "manufacturer_name": "Ford",
    "model_name": "Econoline E350 Super Duty Cargo",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2002,
    "manufacturer_name": "Dodge",
    "model_name": "Ram 1500 Quad Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2002,
    "manufacturer_name": "Ford",
    "model_name": "Escort",
    "car_type": "Sedan"
  },
  {
    "year": 2002,
    "manufacturer_name": "Ford",
    "model_name": "Explorer Sport Trac",
    "car_type": "Pickup"
  },
  {
    "year": 2002,
    "manufacturer_name": "Dodge",
    "model_name": "Ram Wagon 3500",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2002,
    "manufacturer_name": "Ford",
    "model_name": "Escape",
    "car_type": "SUV"
  },
  {
    "year": 2002,
    "manufacturer_name": "Dodge",
    "model_name": "Ram 2500 Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2002,
    "manufacturer_name": "Dodge",
    "model_name": "Ram Van 3500",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2002,
    "manufacturer_name": "Dodge",
    "model_name": "Stratus",
    "car_type": "Coupe, Sedan"
  },
  {
    "year": 2002,
    "manufacturer_name": "Ford",
    "model_name": "Excursion",
    "car_type": "SUV"
  },
  {
    "year": 2002,
    "manufacturer_name": "Ford",
    "model_name": "Expedition",
    "car_type": "SUV"
  },
  {
    "year": 2002,
    "manufacturer_name": "Ford",
    "model_name": "F150 Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2002,
    "manufacturer_name": "Ford",
    "model_name": "Mustang",
    "car_type": "Coupe, Convertible"
  },
  {
    "year": 2002,
    "manufacturer_name": "Ford",
    "model_name": "F250 Super Duty Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2002,
    "manufacturer_name": "Ford",
    "model_name": "Thunderbird",
    "car_type": "Convertible"
  },
  {
    "year": 2002,
    "manufacturer_name": "Ford",
    "model_name": "F150 Super Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2002,
    "manufacturer_name": "Ford",
    "model_name": "F350 Super Duty Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2002,
    "manufacturer_name": "Ford",
    "model_name": "F250 Super Duty Super Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2002,
    "manufacturer_name": "Ford",
    "model_name": "F250 Super Duty Crew Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2002,
    "manufacturer_name": "Ford",
    "model_name": "Windstar Cargo",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2002,
    "manufacturer_name": "GMC",
    "model_name": "Savana 2500 Cargo",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2002,
    "manufacturer_name": "Ford",
    "model_name": "F350 Super Duty Super Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2002,
    "manufacturer_name": "Ford",
    "model_name": "F150 SuperCrew Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2002,
    "manufacturer_name": "Ford",
    "model_name": "Focus",
    "car_type": "Sedan, Wagon, Hatchback"
  },
  {
    "year": 2002,
    "manufacturer_name": "Ford",
    "model_name": "F350 Super Duty Crew Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2002,
    "manufacturer_name": "GMC",
    "model_name": "Envoy XL",
    "car_type": "SUV"
  },
  {
    "year": 2002,
    "manufacturer_name": "Ford",
    "model_name": "Ranger Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2002,
    "manufacturer_name": "GMC",
    "model_name": "Sierra 2500 HD Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2002,
    "manufacturer_name": "GMC",
    "model_name": "Sierra 1500 HD Crew Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2002,
    "manufacturer_name": "GMC",
    "model_name": "Sonoma Crew Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2002,
    "manufacturer_name": "GMC",
    "model_name": "Yukon XL 2500",
    "car_type": "SUV"
  },
  {
    "year": 2002,
    "manufacturer_name": "Ford",
    "model_name": "Taurus",
    "car_type": "Sedan, Wagon"
  },
  {
    "year": 2002,
    "manufacturer_name": "Ford",
    "model_name": "Ranger Super Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2002,
    "manufacturer_name": "Ford",
    "model_name": "Windstar Passenger",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2002,
    "manufacturer_name": "GMC",
    "model_name": "Safari Cargo",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2002,
    "manufacturer_name": "GMC",
    "model_name": "Safari Passenger",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2002,
    "manufacturer_name": "Honda",
    "model_name": "Odyssey",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2002,
    "manufacturer_name": "GMC",
    "model_name": "Savana 2500 Passenger",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2002,
    "manufacturer_name": "GMC",
    "model_name": "Sonoma Extended Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2002,
    "manufacturer_name": "Isuzu",
    "model_name": "Rodeo Sport",
    "car_type": "SUV"
  },
  {
    "year": 2002,
    "manufacturer_name": "INFINITI",
    "model_name": "I",
    "car_type": "Sedan"
  },
  {
    "year": 2002,
    "manufacturer_name": "GMC",
    "model_name": "Sierra 1500 Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2002,
    "manufacturer_name": "GMC",
    "model_name": "Savana 3500 Cargo",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2002,
    "manufacturer_name": "GMC",
    "model_name": "Sierra 2500 Extended Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2002,
    "manufacturer_name": "Ford",
    "model_name": "ZX2",
    "car_type": "Coupe"
  },
  {
    "year": 2002,
    "manufacturer_name": "GMC",
    "model_name": "Envoy",
    "car_type": "SUV"
  },
  {
    "year": 2002,
    "manufacturer_name": "Hyundai",
    "model_name": "Elantra",
    "car_type": "Sedan, Hatchback"
  },
  {
    "year": 2002,
    "manufacturer_name": "GMC",
    "model_name": "Savana 1500 Cargo",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2002,
    "manufacturer_name": "GMC",
    "model_name": "Sierra 2500 Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2002,
    "manufacturer_name": "GMC",
    "model_name": "Sierra 2500 HD Crew Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2002,
    "manufacturer_name": "GMC",
    "model_name": "Sierra 3500 Extended Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2002,
    "manufacturer_name": "GMC",
    "model_name": "Savana 3500 Passenger",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2002,
    "manufacturer_name": "Honda",
    "model_name": "Accord",
    "car_type": "Sedan, Coupe"
  },
  {
    "year": 2002,
    "manufacturer_name": "GMC",
    "model_name": "Savana 1500 Passenger",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2002,
    "manufacturer_name": "Jaguar",
    "model_name": "X-Type",
    "car_type": "Sedan"
  },
  {
    "year": 2002,
    "manufacturer_name": "GMC",
    "model_name": "Sierra 2500 HD Extended Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2002,
    "manufacturer_name": "Honda",
    "model_name": "Civic",
    "car_type": "Sedan, Coupe, Hatchback"
  },
  {
    "year": 2002,
    "manufacturer_name": "GMC",
    "model_name": "Sierra 3500 Crew Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2002,
    "manufacturer_name": "GMC",
    "model_name": "Sierra 1500 Extended Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2002,
    "manufacturer_name": "Honda",
    "model_name": "Passport",
    "car_type": "SUV"
  },
  {
    "year": 2002,
    "manufacturer_name": "GMC",
    "model_name": "Sonoma Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2002,
    "manufacturer_name": "GMC",
    "model_name": "Yukon XL 1500",
    "car_type": "SUV"
  },
  {
    "year": 2002,
    "manufacturer_name": "GMC",
    "model_name": "Sierra 3500 Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2002,
    "manufacturer_name": "INFINITI",
    "model_name": "QX",
    "car_type": "SUV"
  },
  {
    "year": 2002,
    "manufacturer_name": "HUMMER",
    "model_name": "H1",
    "car_type": "SUV, Wagon"
  },
  {
    "year": 2002,
    "manufacturer_name": "Jaguar",
    "model_name": "XJ",
    "car_type": "Sedan"
  },
  {
    "year": 2002,
    "manufacturer_name": "Honda",
    "model_name": "Insight",
    "car_type": "Hatchback"
  },
  {
    "year": 2002,
    "manufacturer_name": "Jaguar",
    "model_name": "S-Type",
    "car_type": "Sedan"
  },
  {
    "year": 2002,
    "manufacturer_name": "Isuzu",
    "model_name": "Rodeo",
    "car_type": "SUV"
  },
  {
    "year": 2002,
    "manufacturer_name": "Honda",
    "model_name": "CR-V",
    "car_type": "SUV"
  },
  {
    "year": 2002,
    "manufacturer_name": "GMC",
    "model_name": "Yukon",
    "car_type": "SUV"
  },
  {
    "year": 2002,
    "manufacturer_name": "Hyundai",
    "model_name": "Accent",
    "car_type": "Hatchback, Sedan"
  },
  {
    "year": 2002,
    "manufacturer_name": "Honda",
    "model_name": "S2000",
    "car_type": "Convertible"
  },
  {
    "year": 2002,
    "manufacturer_name": "Hyundai",
    "model_name": "Santa Fe",
    "car_type": "SUV"
  },
  {
    "year": 2002,
    "manufacturer_name": "Hyundai",
    "model_name": "XG350",
    "car_type": "Sedan"
  },
  {
    "year": 2002,
    "manufacturer_name": "Hyundai",
    "model_name": "Sonata",
    "car_type": "Sedan"
  },
  {
    "year": 2002,
    "manufacturer_name": "Jaguar",
    "model_name": "XK",
    "car_type": "Coupe, Convertible"
  },
  {
    "year": 2002,
    "manufacturer_name": "Isuzu",
    "model_name": "Trooper",
    "car_type": "SUV"
  },
  {
    "year": 2002,
    "manufacturer_name": "INFINITI",
    "model_name": "Q",
    "car_type": "Sedan"
  },
  {
    "year": 2002,
    "manufacturer_name": "Isuzu",
    "model_name": "Axiom",
    "car_type": "SUV"
  },
  {
    "year": 2002,
    "manufacturer_name": "INFINITI",
    "model_name": "G",
    "car_type": "Sedan"
  },
  {
    "year": 2002,
    "manufacturer_name": "Kia",
    "model_name": "Sportage",
    "car_type": "SUV"
  },
  {
    "year": 2002,
    "manufacturer_name": "Jeep",
    "model_name": "Liberty",
    "car_type": "SUV"
  },
  {
    "year": 2002,
    "manufacturer_name": "Land Rover",
    "model_name": "Discovery Series II",
    "car_type": "SUV"
  },
  {
    "year": 2002,
    "manufacturer_name": "Kia",
    "model_name": "Rio",
    "car_type": "Sedan, Wagon"
  },
  {
    "year": 2002,
    "manufacturer_name": "Kia",
    "model_name": "Spectra",
    "car_type": "Sedan, Hatchback"
  },
  {
    "year": 2002,
    "manufacturer_name": "Jeep",
    "model_name": "Wrangler",
    "car_type": "SUV"
  },
  {
    "year": 2002,
    "manufacturer_name": "Kia",
    "model_name": "Sedona",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2002,
    "manufacturer_name": "Jeep",
    "model_name": "Grand Cherokee",
    "car_type": "SUV"
  },
  {
    "year": 2002,
    "manufacturer_name": "Kia",
    "model_name": "Optima",
    "car_type": "Sedan"
  },
  {
    "year": 2002,
    "manufacturer_name": "Lexus",
    "model_name": "GS",
    "car_type": "Sedan"
  },
  {
    "year": 2002,
    "manufacturer_name": "Lexus",
    "model_name": "LS",
    "car_type": "Sedan"
  },
  {
    "year": 2002,
    "manufacturer_name": "Land Rover",
    "model_name": "Freelander",
    "car_type": "SUV"
  },
  {
    "year": 2002,
    "manufacturer_name": "Lincoln",
    "model_name": "Blackwood",
    "car_type": "Pickup"
  },
  {
    "year": 2002,
    "manufacturer_name": "Lexus",
    "model_name": "IS",
    "car_type": "Sedan, Hatchback"
  },
  {
    "year": 2002,
    "manufacturer_name": "Lexus",
    "model_name": "SC",
    "car_type": "Convertible"
  },
  {
    "year": 2002,
    "manufacturer_name": "Lexus",
    "model_name": "ES",
    "car_type": "Sedan"
  },
  {
    "year": 2002,
    "manufacturer_name": "Lexus",
    "model_name": "RX",
    "car_type": "SUV"
  },
  {
    "year": 2002,
    "manufacturer_name": "Lexus",
    "model_name": "LX",
    "car_type": "SUV"
  },
  {
    "year": 2002,
    "manufacturer_name": "Land Rover",
    "model_name": "Range Rover",
    "car_type": "SUV"
  },
  {
    "year": 2002,
    "manufacturer_name": "Lincoln",
    "model_name": "Continental",
    "car_type": "Sedan"
  },
  {
    "year": 2002,
    "manufacturer_name": "MAZDA",
    "model_name": "626",
    "car_type": "Sedan"
  },
  {
    "year": 2002,
    "manufacturer_name": "Lincoln",
    "model_name": "Navigator",
    "car_type": "SUV"
  },
  {
    "year": 2002,
    "manufacturer_name": "Mercedes-Benz",
    "model_name": "CLK-Class",
    "car_type": "Coupe, Convertible"
  },
  {
    "year": 2002,
    "manufacturer_name": "MAZDA",
    "model_name": "Protege5",
    "car_type": "Hatchback"
  },
  {
    "year": 2002,
    "manufacturer_name": "Lincoln",
    "model_name": "LS",
    "car_type": "Sedan"
  },
  {
    "year": 2002,
    "manufacturer_name": "MAZDA",
    "model_name": "Millenia",
    "car_type": "Sedan"
  },
  {
    "year": 2002,
    "manufacturer_name": "MAZDA",
    "model_name": "Tribute",
    "car_type": "SUV"
  },
  {
    "year": 2002,
    "manufacturer_name": "MAZDA",
    "model_name": "MX-5 Miata",
    "car_type": "Convertible"
  },
  {
    "year": 2002,
    "manufacturer_name": "Mercedes-Benz",
    "model_name": "C-Class",
    "car_type": "Coupe, Sedan, Wagon"
  },
  {
    "year": 2002,
    "manufacturer_name": "Lincoln",
    "model_name": "Town Car",
    "car_type": "Sedan"
  },
  {
    "year": 2002,
    "manufacturer_name": "MAZDA",
    "model_name": "B-Series Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2002,
    "manufacturer_name": "Mercedes-Benz",
    "model_name": "CL-Class",
    "car_type": "Coupe"
  },
  {
    "year": 2002,
    "manufacturer_name": "MAZDA",
    "model_name": "B-Series Cab Plus",
    "car_type": "Pickup"
  },
  {
    "year": 2002,
    "manufacturer_name": "MAZDA",
    "model_name": "MPV",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2002,
    "manufacturer_name": "MAZDA",
    "model_name": "Protege",
    "car_type": "Sedan"
  },
  {
    "year": 2002,
    "manufacturer_name": "Mercedes-Benz",
    "model_name": "E-Class",
    "car_type": "Sedan, Wagon"
  },
  {
    "year": 2002,
    "manufacturer_name": "Mitsubishi",
    "model_name": "Mirage",
    "car_type": "Coupe"
  },
  {
    "year": 2002,
    "manufacturer_name": "Mercury",
    "model_name": "Villager",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2002,
    "manufacturer_name": "MINI",
    "model_name": "Cooper",
    "car_type": "Hatchback"
  },
  {
    "year": 2002,
    "manufacturer_name": "Mercedes-Benz",
    "model_name": "SLK-Class",
    "car_type": "Convertible"
  },
  {
    "year": 2002,
    "manufacturer_name": "Mercury",
    "model_name": "Mountaineer",
    "car_type": "SUV"
  },
  {
    "year": 2002,
    "manufacturer_name": "Mercedes-Benz",
    "model_name": "M-Class",
    "car_type": "SUV"
  },
  {
    "year": 2002,
    "manufacturer_name": "Mercury",
    "model_name": "Cougar",
    "car_type": "Coupe"
  },
  {
    "year": 2002,
    "manufacturer_name": "Mercury",
    "model_name": "Sable",
    "car_type": "Sedan, Wagon"
  },
  {
    "year": 2002,
    "manufacturer_name": "Nissan",
    "model_name": "Frontier Crew Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2002,
    "manufacturer_name": "Mercedes-Benz",
    "model_name": "S-Class",
    "car_type": "Sedan"
  },
  {
    "year": 2002,
    "manufacturer_name": "Mercedes-Benz",
    "model_name": "SL-Class",
    "car_type": "Convertible"
  },
  {
    "year": 2002,
    "manufacturer_name": "Mitsubishi",
    "model_name": "Diamante",
    "car_type": "Sedan"
  },
  {
    "year": 2002,
    "manufacturer_name": "Mitsubishi",
    "model_name": "Eclipse",
    "car_type": "Coupe, Convertible"
  },
  {
    "year": 2002,
    "manufacturer_name": "Mitsubishi",
    "model_name": "Montero",
    "car_type": "SUV"
  },
  {
    "year": 2002,
    "manufacturer_name": "Mercury",
    "model_name": "Grand Marquis",
    "car_type": "Sedan"
  },
  {
    "year": 2002,
    "manufacturer_name": "Mitsubishi",
    "model_name": "Montero Sport",
    "car_type": "SUV"
  },
  {
    "year": 2002,
    "manufacturer_name": "Nissan",
    "model_name": "Altima",
    "car_type": "Sedan"
  },
  {
    "year": 2002,
    "manufacturer_name": "Mercedes-Benz",
    "model_name": "G-Class",
    "car_type": "SUV"
  },
  {
    "year": 2002,
    "manufacturer_name": "Mitsubishi",
    "model_name": "Galant",
    "car_type": "Sedan"
  },
  {
    "year": 2002,
    "manufacturer_name": "Mitsubishi",
    "model_name": "Lancer",
    "car_type": "Sedan"
  },
  {
    "year": 2002,
    "manufacturer_name": "Oldsmobile",
    "model_name": "Bravada",
    "car_type": "SUV"
  },
  {
    "year": 2002,
    "manufacturer_name": "Nissan",
    "model_name": "Sentra",
    "car_type": "Sedan"
  },
  {
    "year": 2002,
    "manufacturer_name": "Pontiac",
    "model_name": "Bonneville",
    "car_type": "Sedan"
  },
  {
    "year": 2002,
    "manufacturer_name": "Nissan",
    "model_name": "Quest",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2002,
    "manufacturer_name": "Nissan",
    "model_name": "Frontier King Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2002,
    "manufacturer_name": "Pontiac",
    "model_name": "Aztek",
    "car_type": "SUV"
  },
  {
    "year": 2002,
    "manufacturer_name": "Nissan",
    "model_name": "Maxima",
    "car_type": "Sedan"
  },
  {
    "year": 2002,
    "manufacturer_name": "Nissan",
    "model_name": "Xterra",
    "car_type": "SUV"
  },
  {
    "year": 2002,
    "manufacturer_name": "Pontiac",
    "model_name": "Grand Am",
    "car_type": "Coupe, Sedan"
  },
  {
    "year": 2002,
    "manufacturer_name": "Porsche",
    "model_name": "911",
    "car_type": "Coupe, Convertible"
  },
  {
    "year": 2002,
    "manufacturer_name": "Porsche",
    "model_name": "Boxster",
    "car_type": "Convertible"
  },
  {
    "year": 2002,
    "manufacturer_name": "Oldsmobile",
    "model_name": "Aurora",
    "car_type": "Sedan"
  },
  {
    "year": 2002,
    "manufacturer_name": "Oldsmobile",
    "model_name": "Silhouette",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2002,
    "manufacturer_name": "Pontiac",
    "model_name": "Montana",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2002,
    "manufacturer_name": "Nissan",
    "model_name": "Pathfinder",
    "car_type": "SUV"
  },
  {
    "year": 2002,
    "manufacturer_name": "Oldsmobile",
    "model_name": "Intrigue",
    "car_type": "Sedan"
  },
  {
    "year": 2002,
    "manufacturer_name": "Pontiac",
    "model_name": "Grand Prix",
    "car_type": "Sedan, Coupe"
  },
  {
    "year": 2002,
    "manufacturer_name": "Oldsmobile",
    "model_name": "Alero",
    "car_type": "Sedan, Coupe"
  },
  {
    "year": 2002,
    "manufacturer_name": "Pontiac",
    "model_name": "Sunfire",
    "car_type": "Sedan, Coupe"
  },
  {
    "year": 2002,
    "manufacturer_name": "Saab",
    "model_name": "5-Sep",
    "car_type": "Sedan, Wagon"
  },
  {
    "year": 2002,
    "manufacturer_name": "Saturn",
    "model_name": "L-Series",
    "car_type": "Sedan, Wagon"
  },
  {
    "year": 2002,
    "manufacturer_name": "Saturn",
    "model_name": "S-Series",
    "car_type": "Coupe, Sedan"
  },
  {
    "year": 2002,
    "manufacturer_name": "Pontiac",
    "model_name": "Firebird",
    "car_type": "Coupe, Convertible"
  },
  {
    "year": 2002,
    "manufacturer_name": "Saab",
    "model_name": "3-Sep",
    "car_type": "Convertible, Hatchback"
  },
  {
    "year": 2002,
    "manufacturer_name": "Subaru",
    "model_name": "Legacy",
    "car_type": "Wagon, Sedan"
  },
  {
    "year": 2002,
    "manufacturer_name": "Suzuki",
    "model_name": "Grand Vitara",
    "car_type": "SUV"
  },
  {
    "year": 2002,
    "manufacturer_name": "Toyota",
    "model_name": "Celica",
    "car_type": "Hatchback"
  },
  {
    "year": 2002,
    "manufacturer_name": "Toyota",
    "model_name": "Echo",
    "car_type": "Sedan, Coupe"
  },
  {
    "year": 2002,
    "manufacturer_name": "Toyota",
    "model_name": "Prius",
    "car_type": "Sedan"
  },
  {
    "year": 2002,
    "manufacturer_name": "Toyota",
    "model_name": "MR2",
    "car_type": "Convertible"
  },
  {
    "year": 2002,
    "manufacturer_name": "Subaru",
    "model_name": "Impreza",
    "car_type": "Wagon, Sedan"
  },
  {
    "year": 2002,
    "manufacturer_name": "Toyota",
    "model_name": "Camry",
    "car_type": "Sedan"
  },
  {
    "year": 2002,
    "manufacturer_name": "Toyota",
    "model_name": "4Runner",
    "car_type": "SUV"
  },
  {
    "year": 2002,
    "manufacturer_name": "Saturn",
    "model_name": "VUE",
    "car_type": "SUV"
  },
  {
    "year": 2002,
    "manufacturer_name": "Suzuki",
    "model_name": "Aerio",
    "car_type": "Wagon, Sedan"
  },
  {
    "year": 2002,
    "manufacturer_name": "Subaru",
    "model_name": "Outback",
    "car_type": "Wagon, Sedan"
  },
  {
    "year": 2002,
    "manufacturer_name": "Toyota",
    "model_name": "Avalon",
    "car_type": "Sedan"
  },
  {
    "year": 2002,
    "manufacturer_name": "Subaru",
    "model_name": "Forester",
    "car_type": "SUV"
  },
  {
    "year": 2002,
    "manufacturer_name": "Toyota",
    "model_name": "Land Cruiser",
    "car_type": "SUV"
  },
  {
    "year": 2002,
    "manufacturer_name": "Suzuki",
    "model_name": "XL-7",
    "car_type": "SUV"
  },
  {
    "year": 2002,
    "manufacturer_name": "Toyota",
    "model_name": "Highlander",
    "car_type": "SUV"
  },
  {
    "year": 2002,
    "manufacturer_name": "Suzuki",
    "model_name": "Vitara",
    "car_type": "SUV"
  },
  {
    "year": 2002,
    "manufacturer_name": "Suzuki",
    "model_name": "Esteem",
    "car_type": "Sedan, Wagon"
  },
  {
    "year": 2002,
    "manufacturer_name": "Toyota",
    "model_name": "Corolla",
    "car_type": "Sedan"
  },
  {
    "year": 2002,
    "manufacturer_name": "Toyota",
    "model_name": "RAV4",
    "car_type": "SUV"
  },
  {
    "year": 2002,
    "manufacturer_name": "Toyota",
    "model_name": "Tundra Access Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2002,
    "manufacturer_name": "Toyota",
    "model_name": "Sequoia",
    "car_type": "SUV"
  },
  {
    "year": 2002,
    "manufacturer_name": "Toyota",
    "model_name": "Tacoma Xtracab",
    "car_type": "Pickup"
  },
  {
    "year": 2002,
    "manufacturer_name": "Toyota",
    "model_name": "Tacoma Double Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2002,
    "manufacturer_name": "Volkswagen",
    "model_name": "GTI",
    "car_type": "Hatchback"
  },
  {
    "year": 2002,
    "manufacturer_name": "Volkswagen",
    "model_name": "Cabrio",
    "car_type": "Convertible"
  },
  {
    "year": 2002,
    "manufacturer_name": "Toyota",
    "model_name": "Solara",
    "car_type": "Coupe, Convertible"
  },
  {
    "year": 2002,
    "manufacturer_name": "Volkswagen",
    "model_name": "New Beetle",
    "car_type": "Hatchback"
  },
  {
    "year": 2002,
    "manufacturer_name": "Toyota",
    "model_name": "Sienna",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2002,
    "manufacturer_name": "Toyota",
    "model_name": "Tacoma Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2002,
    "manufacturer_name": "Toyota",
    "model_name": "Tundra Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2002,
    "manufacturer_name": "Volkswagen",
    "model_name": "Jetta",
    "car_type": "Sedan, Wagon"
  },
  {
    "year": 2002,
    "manufacturer_name": "Volkswagen",
    "model_name": "Golf",
    "car_type": "Hatchback"
  },
  {
    "year": 2002,
    "manufacturer_name": "Volkswagen",
    "model_name": "Eurovan",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2002,
    "manufacturer_name": "Volvo",
    "model_name": "S80",
    "car_type": "Sedan"
  },
  {
    "year": 2001,
    "manufacturer_name": "BMW",
    "model_name": "Z8",
    "car_type": "Convertible"
  },
  {
    "year": 2001,
    "manufacturer_name": "BMW",
    "model_name": "M3",
    "car_type": "Coupe, Convertible"
  },
  {
    "year": 2002,
    "manufacturer_name": "Volvo",
    "model_name": "C70",
    "car_type": "Convertible, Coupe"
  },
  {
    "year": 2001,
    "manufacturer_name": "Acura",
    "model_name": "Integra",
    "car_type": "Hatchback, Sedan"
  },
  {
    "year": 2001,
    "manufacturer_name": "Acura",
    "model_name": "CL",
    "car_type": "Coupe"
  },
  {
    "year": 2001,
    "manufacturer_name": "Audi",
    "model_name": "S8",
    "car_type": "Sedan"
  },
  {
    "year": 2001,
    "manufacturer_name": "Acura",
    "model_name": "MDX",
    "car_type": "SUV"
  },
  {
    "year": 2002,
    "manufacturer_name": "Volvo",
    "model_name": "S40",
    "car_type": "Sedan"
  },
  {
    "year": 2001,
    "manufacturer_name": "Acura",
    "model_name": "TL",
    "car_type": "Sedan"
  },
  {
    "year": 2002,
    "manufacturer_name": "Volvo",
    "model_name": "V70",
    "car_type": "Wagon"
  },
  {
    "year": 2001,
    "manufacturer_name": "Acura",
    "model_name": "NSX",
    "car_type": "Coupe, Convertible"
  },
  {
    "year": 2002,
    "manufacturer_name": "Volkswagen",
    "model_name": "Passat",
    "car_type": "Sedan, Wagon"
  },
  {
    "year": 2001,
    "manufacturer_name": "Acura",
    "model_name": "RL",
    "car_type": "Sedan"
  },
  {
    "year": 2002,
    "manufacturer_name": "Volvo",
    "model_name": "S60",
    "car_type": "Sedan"
  },
  {
    "year": 2002,
    "manufacturer_name": "Volvo",
    "model_name": "V40",
    "car_type": "Wagon"
  },
  {
    "year": 2001,
    "manufacturer_name": "Audi",
    "model_name": "A4",
    "car_type": "Sedan, Wagon"
  },
  {
    "year": 2001,
    "manufacturer_name": "Audi",
    "model_name": "A8",
    "car_type": "Sedan"
  },
  {
    "year": 2001,
    "manufacturer_name": "BMW",
    "model_name": "M",
    "car_type": "Hatchback, Convertible"
  },
  {
    "year": 2001,
    "manufacturer_name": "Audi",
    "model_name": "S4",
    "car_type": "Wagon, Sedan"
  },
  {
    "year": 2001,
    "manufacturer_name": "Audi",
    "model_name": "A6",
    "car_type": "Wagon, Sedan"
  },
  {
    "year": 2001,
    "manufacturer_name": "Buick",
    "model_name": "Century",
    "car_type": "Sedan"
  },
  {
    "year": 2001,
    "manufacturer_name": "Audi",
    "model_name": "allroad",
    "car_type": "Wagon"
  },
  {
    "year": 2001,
    "manufacturer_name": "Cadillac",
    "model_name": "DeVille",
    "car_type": "Sedan"
  },
  {
    "year": 2001,
    "manufacturer_name": "BMW",
    "model_name": "7 Series",
    "car_type": "Sedan"
  },
  {
    "year": 2001,
    "manufacturer_name": "Audi",
    "model_name": "TT",
    "car_type": "Coupe, Convertible"
  },
  {
    "year": 2001,
    "manufacturer_name": "BMW",
    "model_name": "3 Series",
    "car_type": "Coupe, Sedan, Wagon, Convertible"
  },
  {
    "year": 2001,
    "manufacturer_name": "BMW",
    "model_name": "Z3",
    "car_type": "Convertible, Hatchback"
  },
  {
    "year": 2001,
    "manufacturer_name": "BMW",
    "model_name": "5 Series",
    "car_type": "Wagon, Sedan"
  },
  {
    "year": 2001,
    "manufacturer_name": "BMW",
    "model_name": "M5",
    "car_type": "Sedan"
  },
  {
    "year": 2001,
    "manufacturer_name": "BMW",
    "model_name": "X5",
    "car_type": "SUV"
  },
  {
    "year": 2001,
    "manufacturer_name": "Chevrolet",
    "model_name": "Express 1500 Passenger",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2001,
    "manufacturer_name": "Chevrolet",
    "model_name": "Astro Passenger",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2001,
    "manufacturer_name": "Buick",
    "model_name": "Regal",
    "car_type": "Sedan"
  },
  {
    "year": 2001,
    "manufacturer_name": "Cadillac",
    "model_name": "Catera",
    "car_type": "Sedan"
  },
  {
    "year": 2001,
    "manufacturer_name": "Chevrolet",
    "model_name": "Blazer",
    "car_type": "SUV"
  },
  {
    "year": 2001,
    "manufacturer_name": "Chevrolet",
    "model_name": "Cavalier",
    "car_type": "Sedan, Coupe"
  },
  {
    "year": 2001,
    "manufacturer_name": "Cadillac",
    "model_name": "Seville",
    "car_type": "Sedan"
  },
  {
    "year": 2001,
    "manufacturer_name": "Buick",
    "model_name": "Park Avenue",
    "car_type": "Sedan"
  },
  {
    "year": 2001,
    "manufacturer_name": "Cadillac",
    "model_name": "Eldorado",
    "car_type": "Coupe"
  },
  {
    "year": 2001,
    "manufacturer_name": "Buick",
    "model_name": "LeSabre",
    "car_type": "Sedan"
  },
  {
    "year": 2001,
    "manufacturer_name": "Chevrolet",
    "model_name": "Astro Cargo",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2001,
    "manufacturer_name": "Chevrolet",
    "model_name": "Impala",
    "car_type": "Sedan"
  },
  {
    "year": 2001,
    "manufacturer_name": "Chevrolet",
    "model_name": "Express 1500 Cargo",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2001,
    "manufacturer_name": "Chevrolet",
    "model_name": "Express 3500 Cargo",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2001,
    "manufacturer_name": "Chevrolet",
    "model_name": "Silverado 1500 HD Crew Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2001,
    "manufacturer_name": "Chevrolet",
    "model_name": "S10 Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2001,
    "manufacturer_name": "Chevrolet",
    "model_name": "Metro",
    "car_type": "Sedan"
  },
  {
    "year": 2001,
    "manufacturer_name": "Chevrolet",
    "model_name": "Corvette",
    "car_type": "Convertible, Coupe, Hatchback"
  },
  {
    "year": 2001,
    "manufacturer_name": "Chevrolet",
    "model_name": "Camaro",
    "car_type": "Coupe, Convertible"
  },
  {
    "year": 2001,
    "manufacturer_name": "Chevrolet",
    "model_name": "S10 Extended Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2001,
    "manufacturer_name": "Chevrolet",
    "model_name": "Express 3500 Passenger",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2001,
    "manufacturer_name": "Chevrolet",
    "model_name": "Malibu",
    "car_type": "Sedan"
  },
  {
    "year": 2001,
    "manufacturer_name": "Chevrolet",
    "model_name": "Monte Carlo",
    "car_type": "Coupe"
  },
  {
    "year": 2001,
    "manufacturer_name": "Chevrolet",
    "model_name": "Express 2500 Passenger",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2001,
    "manufacturer_name": "Chevrolet",
    "model_name": "Express 2500 Cargo",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2001,
    "manufacturer_name": "Chevrolet",
    "model_name": "S10 Crew Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2001,
    "manufacturer_name": "Chevrolet",
    "model_name": "Silverado 1500 Extended Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2001,
    "manufacturer_name": "Chevrolet",
    "model_name": "Lumina",
    "car_type": "Sedan"
  },
  {
    "year": 2001,
    "manufacturer_name": "Chevrolet",
    "model_name": "Prizm",
    "car_type": "Sedan"
  },
  {
    "year": 2001,
    "manufacturer_name": "Chevrolet",
    "model_name": "Silverado 2500 HD Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2001,
    "manufacturer_name": "Chevrolet",
    "model_name": "Silverado 3500 Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2001,
    "manufacturer_name": "Chevrolet",
    "model_name": "Silverado 2500 HD Crew Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2001,
    "manufacturer_name": "Chevrolet",
    "model_name": "Suburban 2500",
    "car_type": "SUV"
  },
  {
    "year": 2001,
    "manufacturer_name": "Daewoo",
    "model_name": "Nubira",
    "car_type": "Sedan, Wagon"
  },
  {
    "year": 2001,
    "manufacturer_name": "Chevrolet",
    "model_name": "Silverado 2500 Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2001,
    "manufacturer_name": "Chrysler",
    "model_name": "Sebring",
    "car_type": "Sedan, Coupe, Convertible"
  },
  {
    "year": 2001,
    "manufacturer_name": "Chevrolet",
    "model_name": "Tracker",
    "car_type": "SUV"
  },
  {
    "year": 2001,
    "manufacturer_name": "Chrysler",
    "model_name": "Voyager",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2001,
    "manufacturer_name": "Daewoo",
    "model_name": "Leganza",
    "car_type": "Sedan"
  },
  {
    "year": 2001,
    "manufacturer_name": "Chevrolet",
    "model_name": "Silverado 1500 Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2001,
    "manufacturer_name": "Chevrolet",
    "model_name": "Suburban 1500",
    "car_type": "SUV"
  },
  {
    "year": 2001,
    "manufacturer_name": "Chevrolet",
    "model_name": "Silverado 2500 HD Extended Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2001,
    "manufacturer_name": "Chrysler",
    "model_name": "300M",
    "car_type": "Sedan"
  },
  {
    "year": 2001,
    "manufacturer_name": "Daewoo",
    "model_name": "Lanos",
    "car_type": "Hatchback, Sedan"
  },
  {
    "year": 2001,
    "manufacturer_name": "Chevrolet",
    "model_name": "Tahoe",
    "car_type": "SUV"
  },
  {
    "year": 2001,
    "manufacturer_name": "Chevrolet",
    "model_name": "Silverado 2500 Extended Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2001,
    "manufacturer_name": "Chrysler",
    "model_name": "LHS",
    "car_type": "Sedan"
  },
  {
    "year": 2001,
    "manufacturer_name": "Chrysler",
    "model_name": "Prowler",
    "car_type": "Convertible"
  },
  {
    "year": 2001,
    "manufacturer_name": "Chevrolet",
    "model_name": "Venture Passenger",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2001,
    "manufacturer_name": "Chrysler",
    "model_name": "Concorde",
    "car_type": "Sedan"
  },
  {
    "year": 2001,
    "manufacturer_name": "Chevrolet",
    "model_name": "Silverado 3500 Crew Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2001,
    "manufacturer_name": "Chrysler",
    "model_name": "Town & Country",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2001,
    "manufacturer_name": "Chevrolet",
    "model_name": "Silverado 3500 Extended Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2001,
    "manufacturer_name": "Chrysler",
    "model_name": "PT Cruiser",
    "car_type": "Wagon"
  },
  {
    "year": 2001,
    "manufacturer_name": "Dodge",
    "model_name": "Caravan Passenger",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2001,
    "manufacturer_name": "Dodge",
    "model_name": "Ram 1500 Quad Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2001,
    "manufacturer_name": "Dodge",
    "model_name": "Ram 1500 Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2001,
    "manufacturer_name": "Dodge",
    "model_name": "Durango",
    "car_type": "SUV"
  },
  {
    "year": 2001,
    "manufacturer_name": "Dodge",
    "model_name": "Neon",
    "car_type": "Sedan"
  },
  {
    "year": 2001,
    "manufacturer_name": "Dodge",
    "model_name": "Dakota Quad Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2001,
    "manufacturer_name": "Dodge",
    "model_name": "Ram 3500 Quad Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2001,
    "manufacturer_name": "Dodge",
    "model_name": "Grand Caravan Passenger",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2001,
    "manufacturer_name": "Dodge",
    "model_name": "Ram 3500 Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2001,
    "manufacturer_name": "Dodge",
    "model_name": "Dakota Club Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2001,
    "manufacturer_name": "Dodge",
    "model_name": "Ram Van 2500",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2001,
    "manufacturer_name": "Dodge",
    "model_name": "Intrepid",
    "car_type": "Sedan"
  },
  {
    "year": 2001,
    "manufacturer_name": "Dodge",
    "model_name": "Ram 2500 Quad Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2001,
    "manufacturer_name": "Dodge",
    "model_name": "Dakota Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2001,
    "manufacturer_name": "Dodge",
    "model_name": "Ram 1500 Club Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2001,
    "manufacturer_name": "Dodge",
    "model_name": "Ram Wagon 2500",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2001,
    "manufacturer_name": "Dodge",
    "model_name": "Ram 2500 Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2001,
    "manufacturer_name": "Dodge",
    "model_name": "Ram Van 3500",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2001,
    "manufacturer_name": "Dodge",
    "model_name": "Ram Wagon 1500",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2001,
    "manufacturer_name": "Dodge",
    "model_name": "Ram Van 1500",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2001,
    "manufacturer_name": "Ford",
    "model_name": "Crown Victoria",
    "car_type": "Sedan"
  },
  {
    "year": 2001,
    "manufacturer_name": "Ford",
    "model_name": "Econoline E250 Cargo",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2001,
    "manufacturer_name": "Ford",
    "model_name": "Econoline E350 Super Duty Passenger",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2001,
    "manufacturer_name": "Dodge",
    "model_name": "Ram Wagon 3500",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2001,
    "manufacturer_name": "Ford",
    "model_name": "F150 Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2001,
    "manufacturer_name": "Ford",
    "model_name": "Econoline E350 Super Duty Cargo",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2001,
    "manufacturer_name": "Ford",
    "model_name": "Econoline E150 Passenger",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2001,
    "manufacturer_name": "Ford",
    "model_name": "Excursion",
    "car_type": "SUV"
  },
  {
    "year": 2001,
    "manufacturer_name": "Ford",
    "model_name": "Econoline E150 Cargo",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2001,
    "manufacturer_name": "Dodge",
    "model_name": "Stratus",
    "car_type": "Coupe, Sedan"
  },
  {
    "year": 2001,
    "manufacturer_name": "Dodge",
    "model_name": "Viper",
    "car_type": "Convertible, Coupe"
  },
  {
    "year": 2001,
    "manufacturer_name": "Ford",
    "model_name": "Expedition",
    "car_type": "SUV"
  },
  {
    "year": 2001,
    "manufacturer_name": "Ford",
    "model_name": "Escape",
    "car_type": "SUV"
  },
  {
    "year": 2001,
    "manufacturer_name": "Ford",
    "model_name": "Explorer Sport",
    "car_type": "SUV"
  },
  {
    "year": 2001,
    "manufacturer_name": "Ford",
    "model_name": "F350 Super Duty Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2001,
    "manufacturer_name": "GMC",
    "model_name": "Savana 2500 Passenger",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2001,
    "manufacturer_name": "Ford",
    "model_name": "F250 Super Duty Crew Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2001,
    "manufacturer_name": "Ford",
    "model_name": "F150 SuperCrew Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2001,
    "manufacturer_name": "Ford",
    "model_name": "Escort",
    "car_type": "Sedan"
  },
  {
    "year": 2001,
    "manufacturer_name": "GMC",
    "model_name": "Safari Cargo",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2001,
    "manufacturer_name": "Ford",
    "model_name": "F150 Super Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2001,
    "manufacturer_name": "GMC",
    "model_name": "Safari Passenger",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2001,
    "manufacturer_name": "Ford",
    "model_name": "Explorer",
    "car_type": "SUV"
  },
  {
    "year": 2001,
    "manufacturer_name": "Ford",
    "model_name": "Ranger Super Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2001,
    "manufacturer_name": "GMC",
    "model_name": "Sierra 1500 HD Crew Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2001,
    "manufacturer_name": "Ford",
    "model_name": "Focus",
    "car_type": "Sedan, Hatchback, Wagon"
  },
  {
    "year": 2001,
    "manufacturer_name": "GMC",
    "model_name": "Sierra 2500 HD Crew Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2001,
    "manufacturer_name": "Ford",
    "model_name": "F350 Super Duty Crew Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2001,
    "manufacturer_name": "Ford",
    "model_name": "F250 Super Duty Super Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2001,
    "manufacturer_name": "Ford",
    "model_name": "Taurus",
    "car_type": "Sedan, Wagon"
  },
  {
    "year": 2001,
    "manufacturer_name": "Ford",
    "model_name": "F250 Super Duty Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2001,
    "manufacturer_name": "GMC",
    "model_name": "Sonoma Extended Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2001,
    "manufacturer_name": "Ford",
    "model_name": "F350 Super Duty Super Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2001,
    "manufacturer_name": "Ford",
    "model_name": "Explorer Sport Trac",
    "car_type": "Pickup"
  },
  {
    "year": 2001,
    "manufacturer_name": "Ford",
    "model_name": "Ranger Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2001,
    "manufacturer_name": "GMC",
    "model_name": "Sierra 3500 Extended Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2001,
    "manufacturer_name": "GMC",
    "model_name": "Savana 3500 Cargo",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2001,
    "manufacturer_name": "Ford",
    "model_name": "Windstar Cargo",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2001,
    "manufacturer_name": "GMC",
    "model_name": "Sierra 2500 Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2001,
    "manufacturer_name": "GMC",
    "model_name": "Savana 2500 Cargo",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2001,
    "manufacturer_name": "Ford",
    "model_name": "Mustang",
    "car_type": "Coupe, Convertible"
  },
  {
    "year": 2001,
    "manufacturer_name": "Ford",
    "model_name": "Windstar Passenger",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2001,
    "manufacturer_name": "GMC",
    "model_name": "Savana 1500 Cargo",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2001,
    "manufacturer_name": "GMC",
    "model_name": "Savana 3500 Passenger",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2001,
    "manufacturer_name": "GMC",
    "model_name": "Sierra 2500 HD Extended Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2001,
    "manufacturer_name": "GMC",
    "model_name": "Sierra 1500 Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2001,
    "manufacturer_name": "GMC",
    "model_name": "Savana 1500 Passenger",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2001,
    "manufacturer_name": "Ford",
    "model_name": "ZX2",
    "car_type": "Coupe"
  },
  {
    "year": 2001,
    "manufacturer_name": "GMC",
    "model_name": "Jimmy",
    "car_type": "SUV"
  },
  {
    "year": 2001,
    "manufacturer_name": "GMC",
    "model_name": "Sierra 1500 Extended Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2001,
    "manufacturer_name": "GMC",
    "model_name": "Yukon",
    "car_type": "SUV"
  },
  {
    "year": 2001,
    "manufacturer_name": "GMC",
    "model_name": "Yukon XL 1500",
    "car_type": "SUV"
  },
  {
    "year": 2001,
    "manufacturer_name": "GMC",
    "model_name": "Sierra 2500 HD Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2001,
    "manufacturer_name": "GMC",
    "model_name": "Sierra 3500 Crew Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2001,
    "manufacturer_name": "GMC",
    "model_name": "Sonoma Crew Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2001,
    "manufacturer_name": "GMC",
    "model_name": "Sierra 3500 Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2001,
    "manufacturer_name": "Honda",
    "model_name": "S2000",
    "car_type": "Convertible"
  },
  {
    "year": 2001,
    "manufacturer_name": "Hyundai",
    "model_name": "Elantra",
    "car_type": "Hatchback, Sedan"
  },
  {
    "year": 2001,
    "manufacturer_name": "Honda",
    "model_name": "Accord",
    "car_type": "Sedan, Coupe"
  },
  {
    "year": 2001,
    "manufacturer_name": "Honda",
    "model_name": "Passport",
    "car_type": "SUV"
  },
  {
    "year": 2001,
    "manufacturer_name": "GMC",
    "model_name": "Sierra 2500 Extended Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2001,
    "manufacturer_name": "GMC",
    "model_name": "Yukon XL 2500",
    "car_type": "SUV"
  },
  {
    "year": 2001,
    "manufacturer_name": "GMC",
    "model_name": "Sonoma Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2001,
    "manufacturer_name": "Honda",
    "model_name": "CR-V",
    "car_type": "SUV"
  },
  {
    "year": 2001,
    "manufacturer_name": "INFINITI",
    "model_name": "I",
    "car_type": "Sedan"
  },
  {
    "year": 2001,
    "manufacturer_name": "Hyundai",
    "model_name": "Santa Fe",
    "car_type": "SUV"
  },
  {
    "year": 2001,
    "manufacturer_name": "HUMMER",
    "model_name": "H1",
    "car_type": "Wagon, SUV"
  },
  {
    "year": 2001,
    "manufacturer_name": "Honda",
    "model_name": "Prelude",
    "car_type": "Coupe"
  },
  {
    "year": 2001,
    "manufacturer_name": "Hyundai",
    "model_name": "Sonata",
    "car_type": "Sedan"
  },
  {
    "year": 2001,
    "manufacturer_name": "INFINITI",
    "model_name": "Q",
    "car_type": "Sedan"
  },
  {
    "year": 2001,
    "manufacturer_name": "Honda",
    "model_name": "Odyssey",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2001,
    "manufacturer_name": "Hyundai",
    "model_name": "Tiburon",
    "car_type": "Hatchback"
  },
  {
    "year": 2001,
    "manufacturer_name": "Isuzu",
    "model_name": "Rodeo Sport",
    "car_type": "SUV"
  },
  {
    "year": 2001,
    "manufacturer_name": "Honda",
    "model_name": "Insight",
    "car_type": "Hatchback"
  },
  {
    "year": 2001,
    "manufacturer_name": "INFINITI",
    "model_name": "G",
    "car_type": "Sedan"
  },
  {
    "year": 2001,
    "manufacturer_name": "Hyundai",
    "model_name": "XG300",
    "car_type": "Sedan"
  },
  {
    "year": 2001,
    "manufacturer_name": "Honda",
    "model_name": "Civic",
    "car_type": "Sedan, Coupe"
  },
  {
    "year": 2001,
    "manufacturer_name": "INFINITI",
    "model_name": "QX",
    "car_type": "SUV"
  },
  {
    "year": 2001,
    "manufacturer_name": "Isuzu",
    "model_name": "Rodeo",
    "car_type": "SUV"
  },
  {
    "year": 2001,
    "manufacturer_name": "Hyundai",
    "model_name": "Accent",
    "car_type": "Hatchback, Sedan"
  },
  {
    "year": 2001,
    "manufacturer_name": "Isuzu",
    "model_name": "Trooper",
    "car_type": "SUV"
  },
  {
    "year": 2001,
    "manufacturer_name": "Lexus",
    "model_name": "LS",
    "car_type": "Sedan"
  },
  {
    "year": 2001,
    "manufacturer_name": "Jaguar",
    "model_name": "S-Type",
    "car_type": "Sedan"
  },
  {
    "year": 2001,
    "manufacturer_name": "Kia",
    "model_name": "Optima",
    "car_type": "Sedan"
  },
  {
    "year": 2001,
    "manufacturer_name": "Jeep",
    "model_name": "Grand Cherokee",
    "car_type": "SUV"
  },
  {
    "year": 2001,
    "manufacturer_name": "Isuzu",
    "model_name": "VehiCROSS",
    "car_type": "SUV"
  },
  {
    "year": 2001,
    "manufacturer_name": "Jeep",
    "model_name": "Cherokee",
    "car_type": "SUV"
  },
  {
    "year": 2001,
    "manufacturer_name": "Lincoln",
    "model_name": "Continental",
    "car_type": "Sedan"
  },
  {
    "year": 2001,
    "manufacturer_name": "Jaguar",
    "model_name": "XJ",
    "car_type": "Sedan"
  },
  {
    "year": 2001,
    "manufacturer_name": "Jaguar",
    "model_name": "XK",
    "car_type": "Convertible, Coupe"
  },
  {
    "year": 2001,
    "manufacturer_name": "Lexus",
    "model_name": "IS",
    "car_type": "Sedan"
  },
  {
    "year": 2001,
    "manufacturer_name": "Kia",
    "model_name": "Rio",
    "car_type": "Sedan"
  },
  {
    "year": 2001,
    "manufacturer_name": "Lexus",
    "model_name": "GS",
    "car_type": "Sedan"
  },
  {
    "year": 2001,
    "manufacturer_name": "Kia",
    "model_name": "Spectra",
    "car_type": "Hatchback"
  },
  {
    "year": 2001,
    "manufacturer_name": "Lincoln",
    "model_name": "Town Car",
    "car_type": "Sedan"
  },
  {
    "year": 2001,
    "manufacturer_name": "Lexus",
    "model_name": "ES",
    "car_type": "Sedan"
  },
  {
    "year": 2001,
    "manufacturer_name": "Land Rover",
    "model_name": "Range Rover",
    "car_type": "SUV"
  },
  {
    "year": 2001,
    "manufacturer_name": "Lexus",
    "model_name": "RX",
    "car_type": "SUV"
  },
  {
    "year": 2001,
    "manufacturer_name": "Jeep",
    "model_name": "Wrangler",
    "car_type": "SUV"
  },
  {
    "year": 2001,
    "manufacturer_name": "Lincoln",
    "model_name": "LS",
    "car_type": "Sedan"
  },
  {
    "year": 2001,
    "manufacturer_name": "MAZDA",
    "model_name": "MPV",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2001,
    "manufacturer_name": "Kia",
    "model_name": "Sportage",
    "car_type": "SUV"
  },
  {
    "year": 2001,
    "manufacturer_name": "Kia",
    "model_name": "Sephia",
    "car_type": "Sedan"
  },
  {
    "year": 2001,
    "manufacturer_name": "Land Rover",
    "model_name": "Discovery Series II",
    "car_type": "SUV"
  },
  {
    "year": 2001,
    "manufacturer_name": "MAZDA",
    "model_name": "B-Series Cab Plus",
    "car_type": "Pickup"
  },
  {
    "year": 2001,
    "manufacturer_name": "Lexus",
    "model_name": "LX",
    "car_type": "SUV"
  },
  {
    "year": 2001,
    "manufacturer_name": "Lincoln",
    "model_name": "Navigator",
    "car_type": "SUV"
  },
  {
    "year": 2001,
    "manufacturer_name": "MAZDA",
    "model_name": "B-Series Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2001,
    "manufacturer_name": "MAZDA",
    "model_name": "626",
    "car_type": "Sedan"
  },
  {
    "year": 2001,
    "manufacturer_name": "Mitsubishi",
    "model_name": "Montero Sport",
    "car_type": "SUV"
  },
  {
    "year": 2001,
    "manufacturer_name": "Mitsubishi",
    "model_name": "Mirage",
    "car_type": "Coupe, Sedan"
  },
  {
    "year": 2001,
    "manufacturer_name": "Nissan",
    "model_name": "Pathfinder",
    "car_type": "SUV"
  },
  {
    "year": 2001,
    "manufacturer_name": "Mercedes-Benz",
    "model_name": "CL-Class",
    "car_type": "Coupe"
  },
  {
    "year": 2001,
    "manufacturer_name": "Mercury",
    "model_name": "Villager",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2001,
    "manufacturer_name": "MAZDA",
    "model_name": "Protege",
    "car_type": "Sedan"
  },
  {
    "year": 2001,
    "manufacturer_name": "Mercedes-Benz",
    "model_name": "CLK-Class",
    "car_type": "Coupe, Convertible"
  },
  {
    "year": 2001,
    "manufacturer_name": "MAZDA",
    "model_name": "Millenia",
    "car_type": "Sedan"
  },
  {
    "year": 2001,
    "manufacturer_name": "Mercedes-Benz",
    "model_name": "SLK-Class",
    "car_type": "Convertible"
  },
  {
    "year": 2001,
    "manufacturer_name": "Mitsubishi",
    "model_name": "Galant",
    "car_type": "Sedan"
  },
  {
    "year": 2001,
    "manufacturer_name": "Mercedes-Benz",
    "model_name": "SL-Class",
    "car_type": "Convertible"
  },
  {
    "year": 2001,
    "manufacturer_name": "Nissan",
    "model_name": "Frontier Crew Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2001,
    "manufacturer_name": "MAZDA",
    "model_name": "Tribute",
    "car_type": "SUV"
  },
  {
    "year": 2001,
    "manufacturer_name": "Nissan",
    "model_name": "Sentra",
    "car_type": "Sedan"
  },
  {
    "year": 2001,
    "manufacturer_name": "MAZDA",
    "model_name": "MX-5 Miata",
    "car_type": "Convertible"
  },
  {
    "year": 2001,
    "manufacturer_name": "Mercedes-Benz",
    "model_name": "C-Class",
    "car_type": "Sedan"
  },
  {
    "year": 2001,
    "manufacturer_name": "Mitsubishi",
    "model_name": "Montero",
    "car_type": "SUV"
  },
  {
    "year": 2001,
    "manufacturer_name": "Mercedes-Benz",
    "model_name": "M-Class",
    "car_type": "SUV"
  },
  {
    "year": 2001,
    "manufacturer_name": "Mitsubishi",
    "model_name": "Diamante",
    "car_type": "Sedan"
  },
  {
    "year": 2001,
    "manufacturer_name": "Mercury",
    "model_name": "Cougar",
    "car_type": "Coupe"
  },
  {
    "year": 2001,
    "manufacturer_name": "Mercedes-Benz",
    "model_name": "E-Class",
    "car_type": "Sedan, Wagon"
  },
  {
    "year": 2001,
    "manufacturer_name": "Nissan",
    "model_name": "Frontier Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2001,
    "manufacturer_name": "Mercury",
    "model_name": "Grand Marquis",
    "car_type": "Sedan"
  },
  {
    "year": 2001,
    "manufacturer_name": "Mitsubishi",
    "model_name": "Eclipse",
    "car_type": "Hatchback, Convertible"
  },
  {
    "year": 2001,
    "manufacturer_name": "Nissan",
    "model_name": "Frontier King Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2001,
    "manufacturer_name": "Mercedes-Benz",
    "model_name": "S-Class",
    "car_type": "Sedan"
  },
  {
    "year": 2001,
    "manufacturer_name": "Mercury",
    "model_name": "Sable",
    "car_type": "Sedan, Wagon"
  },
  {
    "year": 2001,
    "manufacturer_name": "Mercury",
    "model_name": "Mountaineer",
    "car_type": "SUV"
  },
  {
    "year": 2001,
    "manufacturer_name": "Nissan",
    "model_name": "Altima",
    "car_type": "Sedan"
  },
  {
    "year": 2001,
    "manufacturer_name": "Nissan",
    "model_name": "Xterra",
    "car_type": "SUV"
  },
  {
    "year": 2001,
    "manufacturer_name": "Oldsmobile",
    "model_name": "Silhouette",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2001,
    "manufacturer_name": "Pontiac",
    "model_name": "Bonneville",
    "car_type": "Sedan"
  },
  {
    "year": 2001,
    "manufacturer_name": "Pontiac",
    "model_name": "Grand Am",
    "car_type": "Coupe, Sedan"
  },
  {
    "year": 2001,
    "manufacturer_name": "Subaru",
    "model_name": "Impreza",
    "car_type": "Wagon, Sedan, Coupe"
  },
  {
    "year": 2001,
    "manufacturer_name": "Porsche",
    "model_name": "911",
    "car_type": "Coupe, Convertible"
  },
  {
    "year": 2001,
    "manufacturer_name": "Nissan",
    "model_name": "Maxima",
    "car_type": "Sedan"
  },
  {
    "year": 2001,
    "manufacturer_name": "Subaru",
    "model_name": "Legacy",
    "car_type": "Sedan, Wagon"
  },
  {
    "year": 2001,
    "manufacturer_name": "Pontiac",
    "model_name": "Aztek",
    "car_type": "SUV"
  },
  {
    "year": 2001,
    "manufacturer_name": "Pontiac",
    "model_name": "Montana",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2001,
    "manufacturer_name": "Oldsmobile",
    "model_name": "Bravada",
    "car_type": "SUV"
  },
  {
    "year": 2001,
    "manufacturer_name": "Oldsmobile",
    "model_name": "Aurora",
    "car_type": "Sedan"
  },
  {
    "year": 2001,
    "manufacturer_name": "Suzuki",
    "model_name": "Swift",
    "car_type": "Hatchback"
  },
  {
    "year": 2001,
    "manufacturer_name": "Nissan",
    "model_name": "Quest",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2001,
    "manufacturer_name": "Oldsmobile",
    "model_name": "Alero",
    "car_type": "Sedan, Coupe"
  },
  {
    "year": 2001,
    "manufacturer_name": "Saab",
    "model_name": "3-Sep",
    "car_type": "Hatchback, Convertible"
  },
  {
    "year": 2001,
    "manufacturer_name": "Oldsmobile",
    "model_name": "Intrigue",
    "car_type": "Sedan"
  },
  {
    "year": 2001,
    "manufacturer_name": "Suzuki",
    "model_name": "Esteem",
    "car_type": "Sedan, Wagon"
  },
  {
    "year": 2001,
    "manufacturer_name": "Subaru",
    "model_name": "Outback",
    "car_type": "Wagon, Sedan"
  },
  {
    "year": 2001,
    "manufacturer_name": "Suzuki",
    "model_name": "Grand Vitara",
    "car_type": "SUV"
  },
  {
    "year": 2001,
    "manufacturer_name": "Saturn",
    "model_name": "S-Series",
    "car_type": "Coupe, Sedan, Wagon"
  },
  {
    "year": 2001,
    "manufacturer_name": "Pontiac",
    "model_name": "Firebird",
    "car_type": "Coupe, Convertible"
  },
  {
    "year": 2001,
    "manufacturer_name": "Pontiac",
    "model_name": "Grand Prix",
    "car_type": "Sedan, Coupe"
  },
  {
    "year": 2001,
    "manufacturer_name": "Suzuki",
    "model_name": "XL-7",
    "car_type": "SUV"
  },
  {
    "year": 2001,
    "manufacturer_name": "Saturn",
    "model_name": "L-Series",
    "car_type": "Sedan, Wagon"
  },
  {
    "year": 2001,
    "manufacturer_name": "Pontiac",
    "model_name": "Sunfire",
    "car_type": "Coupe, Sedan"
  },
  {
    "year": 2001,
    "manufacturer_name": "Plymouth",
    "model_name": "Neon",
    "car_type": "Sedan"
  },
  {
    "year": 2001,
    "manufacturer_name": "Suzuki",
    "model_name": "Vitara",
    "car_type": "SUV"
  },
  {
    "year": 2001,
    "manufacturer_name": "Porsche",
    "model_name": "Boxster",
    "car_type": "Convertible"
  },
  {
    "year": 2001,
    "manufacturer_name": "Saab",
    "model_name": "5-Sep",
    "car_type": "Sedan, Wagon"
  },
  {
    "year": 2001,
    "manufacturer_name": "Subaru",
    "model_name": "Forester",
    "car_type": "SUV"
  },
  {
    "year": 2001,
    "manufacturer_name": "Toyota",
    "model_name": "4Runner",
    "car_type": "SUV"
  },
  {
    "year": 2001,
    "manufacturer_name": "Toyota",
    "model_name": "MR2",
    "car_type": "Convertible"
  },
  {
    "year": 2001,
    "manufacturer_name": "Toyota",
    "model_name": "RAV4",
    "car_type": "SUV"
  },
  {
    "year": 2001,
    "manufacturer_name": "Toyota",
    "model_name": "Land Cruiser",
    "car_type": "SUV"
  },
  {
    "year": 2001,
    "manufacturer_name": "Toyota",
    "model_name": "Corolla",
    "car_type": "Sedan"
  },
  {
    "year": 2001,
    "manufacturer_name": "Toyota",
    "model_name": "Camry",
    "car_type": "Sedan"
  },
  {
    "year": 2001,
    "manufacturer_name": "Toyota",
    "model_name": "Avalon",
    "car_type": "Sedan"
  },
  {
    "year": 2001,
    "manufacturer_name": "Toyota",
    "model_name": "Echo",
    "car_type": "Coupe, Sedan"
  },
  {
    "year": 2001,
    "manufacturer_name": "Toyota",
    "model_name": "Celica",
    "car_type": "Hatchback"
  },
  {
    "year": 2001,
    "manufacturer_name": "Toyota",
    "model_name": "Prius",
    "car_type": "Sedan"
  },
  {
    "year": 2001,
    "manufacturer_name": "Toyota",
    "model_name": "Highlander",
    "car_type": "SUV"
  },
  {
    "year": 2001,
    "manufacturer_name": "Toyota",
    "model_name": "Sienna",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2001,
    "manufacturer_name": "Toyota",
    "model_name": "Tacoma Xtracab",
    "car_type": "Pickup"
  },
  {
    "year": 2001,
    "manufacturer_name": "Toyota",
    "model_name": "Sequoia",
    "car_type": "SUV"
  },
  {
    "year": 2001,
    "manufacturer_name": "Toyota",
    "model_name": "Tacoma Double Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2001,
    "manufacturer_name": "Toyota",
    "model_name": "Solara",
    "car_type": "Coupe, Convertible"
  },
  {
    "year": 2001,
    "manufacturer_name": "Toyota",
    "model_name": "Tacoma Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2001,
    "manufacturer_name": "Toyota",
    "model_name": "Tundra Access Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2001,
    "manufacturer_name": "Volvo",
    "model_name": "S40",
    "car_type": "Sedan"
  },
  {
    "year": 2001,
    "manufacturer_name": "Toyota",
    "model_name": "Tundra Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2001,
    "manufacturer_name": "Volkswagen",
    "model_name": "Eurovan",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2001,
    "manufacturer_name": "Volvo",
    "model_name": "V40",
    "car_type": "Wagon"
  },
  {
    "year": 2001,
    "manufacturer_name": "Volvo",
    "model_name": "C70",
    "car_type": "Convertible, Coupe"
  },
  {
    "year": 2001,
    "manufacturer_name": "Volkswagen",
    "model_name": "GTI",
    "car_type": "Hatchback"
  },
  {
    "year": 2001,
    "manufacturer_name": "Volkswagen",
    "model_name": "Passat",
    "car_type": "Sedan, Wagon"
  },
  {
    "year": 2001,
    "manufacturer_name": "Volvo",
    "model_name": "S80",
    "car_type": "Sedan"
  },
  {
    "year": 2000,
    "manufacturer_name": "Acura",
    "model_name": "TL",
    "car_type": "Sedan"
  },
  {
    "year": 2001,
    "manufacturer_name": "Volkswagen",
    "model_name": "Passat (New)",
    "car_type": "Sedan, Wagon"
  },
  {
    "year": 2001,
    "manufacturer_name": "Volkswagen",
    "model_name": "Cabrio",
    "car_type": "Convertible"
  },
  {
    "year": 2000,
    "manufacturer_name": "Acura",
    "model_name": "NSX",
    "car_type": "Coupe, Convertible"
  },
  {
    "year": 2001,
    "manufacturer_name": "Volkswagen",
    "model_name": "Golf",
    "car_type": "Hatchback"
  },
  {
    "year": 2000,
    "manufacturer_name": "Audi",
    "model_name": "A4",
    "car_type": "Wagon, Sedan"
  },
  {
    "year": 2001,
    "manufacturer_name": "Volkswagen",
    "model_name": "New Beetle",
    "car_type": "Hatchback"
  },
  {
    "year": 2001,
    "manufacturer_name": "Volvo",
    "model_name": "S60",
    "car_type": "Sedan"
  },
  {
    "year": 2001,
    "manufacturer_name": "Volkswagen",
    "model_name": "Jetta",
    "car_type": "Sedan, Wagon"
  },
  {
    "year": 2001,
    "manufacturer_name": "Volvo",
    "model_name": "V70",
    "car_type": "Wagon"
  },
  {
    "year": 2000,
    "manufacturer_name": "Acura",
    "model_name": "Integra",
    "car_type": "Sedan, Hatchback"
  },
  {
    "year": 2000,
    "manufacturer_name": "Audi",
    "model_name": "A6",
    "car_type": "Sedan, Wagon"
  },
  {
    "year": 2000,
    "manufacturer_name": "Acura",
    "model_name": "RL",
    "car_type": "Sedan"
  },
  {
    "year": 2000,
    "manufacturer_name": "Audi",
    "model_name": "TT",
    "car_type": "Coupe"
  },
  {
    "year": 2000,
    "manufacturer_name": "BMW",
    "model_name": "5 Series",
    "car_type": "Sedan, Wagon"
  },
  {
    "year": 2000,
    "manufacturer_name": "Buick",
    "model_name": "Regal",
    "car_type": "Sedan"
  },
  {
    "year": 2000,
    "manufacturer_name": "BMW",
    "model_name": "X5",
    "car_type": "SUV"
  },
  {
    "year": 2000,
    "manufacturer_name": "Buick",
    "model_name": "Park Avenue",
    "car_type": "Sedan"
  },
  {
    "year": 2000,
    "manufacturer_name": "Audi",
    "model_name": "A8",
    "car_type": "Sedan"
  },
  {
    "year": 2000,
    "manufacturer_name": "Buick",
    "model_name": "Century",
    "car_type": "Sedan"
  },
  {
    "year": 2000,
    "manufacturer_name": "BMW",
    "model_name": "7 Series",
    "car_type": "Sedan"
  },
  {
    "year": 2000,
    "manufacturer_name": "BMW",
    "model_name": "3 Series",
    "car_type": "Sedan, Wagon, Convertible, Coupe"
  },
  {
    "year": 2000,
    "manufacturer_name": "Audi",
    "model_name": "S4",
    "car_type": "Sedan"
  },
  {
    "year": 2000,
    "manufacturer_name": "BMW",
    "model_name": "M5",
    "car_type": "Sedan"
  },
  {
    "year": 2000,
    "manufacturer_name": "BMW",
    "model_name": "Z8",
    "car_type": "Convertible"
  },
  {
    "year": 2000,
    "manufacturer_name": "Cadillac",
    "model_name": "Eldorado",
    "car_type": "Coupe"
  },
  {
    "year": 2000,
    "manufacturer_name": "Cadillac",
    "model_name": "Catera",
    "car_type": "Sedan"
  },
  {
    "year": 2000,
    "manufacturer_name": "BMW",
    "model_name": "M",
    "car_type": "Hatchback, Convertible"
  },
  {
    "year": 2000,
    "manufacturer_name": "BMW",
    "model_name": "Z3",
    "car_type": "Convertible, Hatchback"
  },
  {
    "year": 2000,
    "manufacturer_name": "Cadillac",
    "model_name": "DeVille",
    "car_type": "Sedan"
  },
  {
    "year": 2000,
    "manufacturer_name": "Buick",
    "model_name": "LeSabre",
    "car_type": "Sedan"
  },
  {
    "year": 2000,
    "manufacturer_name": "Chevrolet",
    "model_name": "2500 HD Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2000,
    "manufacturer_name": "Cadillac",
    "model_name": "Seville",
    "car_type": "Sedan"
  },
  {
    "year": 2000,
    "manufacturer_name": "Chevrolet",
    "model_name": "2500 Crew Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2000,
    "manufacturer_name": "Chevrolet",
    "model_name": "Metro",
    "car_type": "Hatchback, Sedan"
  },
  {
    "year": 2000,
    "manufacturer_name": "Chevrolet",
    "model_name": "Astro Cargo",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2000,
    "manufacturer_name": "Cadillac",
    "model_name": "Escalade",
    "car_type": "SUV"
  },
  {
    "year": 2000,
    "manufacturer_name": "Chevrolet",
    "model_name": "Express 3500 Cargo",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2000,
    "manufacturer_name": "Chevrolet",
    "model_name": "2500 HD Extended Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2000,
    "manufacturer_name": "Chevrolet",
    "model_name": "3500 Crew Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2000,
    "manufacturer_name": "Chevrolet",
    "model_name": "3500 Extended Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2000,
    "manufacturer_name": "Chevrolet",
    "model_name": "Corvette",
    "car_type": "Coupe, Convertible"
  },
  {
    "year": 2000,
    "manufacturer_name": "Chevrolet",
    "model_name": "Silverado 1500 Extended Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2000,
    "manufacturer_name": "Chevrolet",
    "model_name": "3500 Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2000,
    "manufacturer_name": "Chevrolet",
    "model_name": "Suburban 1500",
    "car_type": "SUV"
  },
  {
    "year": 2000,
    "manufacturer_name": "Chevrolet",
    "model_name": "Tracker",
    "car_type": "SUV"
  },
  {
    "year": 2000,
    "manufacturer_name": "Chrysler",
    "model_name": "Concorde",
    "car_type": "Sedan"
  },
  {
    "year": 2000,
    "manufacturer_name": "Chevrolet",
    "model_name": "Lumina",
    "car_type": "Sedan"
  },
  {
    "year": 2000,
    "manufacturer_name": "Chevrolet",
    "model_name": "Astro Passenger",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2000,
    "manufacturer_name": "Chevrolet",
    "model_name": "Express 3500 Passenger",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2000,
    "manufacturer_name": "Chevrolet",
    "model_name": "Silverado 2500 Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2000,
    "manufacturer_name": "Chevrolet",
    "model_name": "Express 1500 Passenger",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2000,
    "manufacturer_name": "Chevrolet",
    "model_name": "Tahoe (New)",
    "car_type": "SUV"
  },
  {
    "year": 2000,
    "manufacturer_name": "Chrysler",
    "model_name": "Cirrus",
    "car_type": "Sedan"
  },
  {
    "year": 2000,
    "manufacturer_name": "Chevrolet",
    "model_name": "Tahoe",
    "car_type": "SUV"
  },
  {
    "year": 2000,
    "manufacturer_name": "Chevrolet",
    "model_name": "Camaro",
    "car_type": "Coupe, Convertible"
  },
  {
    "year": 2000,
    "manufacturer_name": "Dodge",
    "model_name": "Caravan Passenger",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2000,
    "manufacturer_name": "Chevrolet",
    "model_name": "Express 2500 Cargo",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2000,
    "manufacturer_name": "Chevrolet",
    "model_name": "Silverado 2500 HD Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2000,
    "manufacturer_name": "Chevrolet",
    "model_name": "Silverado 2500 HD Extended Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2000,
    "manufacturer_name": "Chevrolet",
    "model_name": "Blazer",
    "car_type": "SUV"
  },
  {
    "year": 2000,
    "manufacturer_name": "Chevrolet",
    "model_name": "Express 2500 Passenger",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2000,
    "manufacturer_name": "Chrysler",
    "model_name": "300M",
    "car_type": "Sedan"
  },
  {
    "year": 2000,
    "manufacturer_name": "Chevrolet",
    "model_name": "Venture Cargo",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2000,
    "manufacturer_name": "Chevrolet",
    "model_name": "Malibu",
    "car_type": "Sedan"
  },
  {
    "year": 2000,
    "manufacturer_name": "Chrysler",
    "model_name": "Voyager",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2000,
    "manufacturer_name": "Chevrolet",
    "model_name": "Suburban 2500",
    "car_type": "SUV"
  },
  {
    "year": 2000,
    "manufacturer_name": "Chrysler",
    "model_name": "Grand Voyager",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2000,
    "manufacturer_name": "Daewoo",
    "model_name": "Nubira",
    "car_type": "Sedan, Wagon"
  },
  {
    "year": 2000,
    "manufacturer_name": "Chrysler",
    "model_name": "Town & Country",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2000,
    "manufacturer_name": "Chevrolet",
    "model_name": "Impala",
    "car_type": "Sedan"
  },
  {
    "year": 2000,
    "manufacturer_name": "Chevrolet",
    "model_name": "S10 Extended Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2000,
    "manufacturer_name": "Chevrolet",
    "model_name": "Cavalier",
    "car_type": "Coupe, Sedan, Convertible"
  },
  {
    "year": 2000,
    "manufacturer_name": "Chevrolet",
    "model_name": "S10 Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2000,
    "manufacturer_name": "Chevrolet",
    "model_name": "Prizm",
    "car_type": "Sedan"
  },
  {
    "year": 2000,
    "manufacturer_name": "Chrysler",
    "model_name": "LHS",
    "car_type": "Sedan"
  },
  {
    "year": 2000,
    "manufacturer_name": "Chevrolet",
    "model_name": "Silverado 1500 Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2000,
    "manufacturer_name": "Chevrolet",
    "model_name": "Monte Carlo",
    "car_type": "Coupe"
  },
  {
    "year": 2000,
    "manufacturer_name": "Chevrolet",
    "model_name": "Venture Passenger",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2000,
    "manufacturer_name": "Chevrolet",
    "model_name": "Express 1500 Cargo",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2000,
    "manufacturer_name": "Chevrolet",
    "model_name": "Silverado 2500 Extended Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2000,
    "manufacturer_name": "Chrysler",
    "model_name": "Sebring",
    "car_type": "Coupe, Convertible"
  },
  {
    "year": 2000,
    "manufacturer_name": "Daewoo",
    "model_name": "Lanos",
    "car_type": "Sedan, Hatchback"
  },
  {
    "year": 2000,
    "manufacturer_name": "Dodge",
    "model_name": "Avenger",
    "car_type": "Coupe"
  },
  {
    "year": 2000,
    "manufacturer_name": "Daewoo",
    "model_name": "Leganza",
    "car_type": "Sedan"
  },
  {
    "year": 2000,
    "manufacturer_name": "Dodge",
    "model_name": "Ram 2500 Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2000,
    "manufacturer_name": "Dodge",
    "model_name": "Ram 1500 Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2000,
    "manufacturer_name": "Dodge",
    "model_name": "Ram 1500 Club Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2000,
    "manufacturer_name": "Ford",
    "model_name": "Contour",
    "car_type": "Sedan"
  },
  {
    "year": 2000,
    "manufacturer_name": "Dodge",
    "model_name": "Dakota Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2000,
    "manufacturer_name": "Dodge",
    "model_name": "Ram Wagon 2500",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2000,
    "manufacturer_name": "Dodge",
    "model_name": "Dakota Club Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2000,
    "manufacturer_name": "Ford",
    "model_name": "Econoline E150 Passenger",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2000,
    "manufacturer_name": "Ford",
    "model_name": "Econoline E350 Super Duty Passenger",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2000,
    "manufacturer_name": "Dodge",
    "model_name": "Dakota Quad Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2000,
    "manufacturer_name": "Dodge",
    "model_name": "Ram Van 1500",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2000,
    "manufacturer_name": "Dodge",
    "model_name": "Ram 1500 Quad Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2000,
    "manufacturer_name": "Dodge",
    "model_name": "Ram Wagon 3500",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2000,
    "manufacturer_name": "Dodge",
    "model_name": "Ram 2500 Quad Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2000,
    "manufacturer_name": "Dodge",
    "model_name": "Durango",
    "car_type": "SUV"
  },
  {
    "year": 2000,
    "manufacturer_name": "Dodge",
    "model_name": "Grand Caravan Passenger",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2000,
    "manufacturer_name": "Dodge",
    "model_name": "Intrepid",
    "car_type": "Sedan"
  },
  {
    "year": 2000,
    "manufacturer_name": "Dodge",
    "model_name": "Ram Van 3500",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2000,
    "manufacturer_name": "Dodge",
    "model_name": "Ram 3500 Quad Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2000,
    "manufacturer_name": "Dodge",
    "model_name": "Ram Van 2500",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2000,
    "manufacturer_name": "Dodge",
    "model_name": "Ram 3500 Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2000,
    "manufacturer_name": "Ford",
    "model_name": "Crown Victoria",
    "car_type": "Sedan"
  },
  {
    "year": 2000,
    "manufacturer_name": "Dodge",
    "model_name": "Ram Wagon 1500",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2000,
    "manufacturer_name": "Dodge",
    "model_name": "Stratus",
    "car_type": "Sedan"
  },
  {
    "year": 2000,
    "manufacturer_name": "Dodge",
    "model_name": "Neon",
    "car_type": "Sedan"
  },
  {
    "year": 2000,
    "manufacturer_name": "Dodge",
    "model_name": "Viper",
    "car_type": "Convertible, Coupe"
  },
  {
    "year": 2000,
    "manufacturer_name": "Ford",
    "model_name": "Econoline E150 Cargo",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2000,
    "manufacturer_name": "Ford",
    "model_name": "F150 Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2000,
    "manufacturer_name": "Ford",
    "model_name": "Econoline E350 Super Duty Cargo",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2000,
    "manufacturer_name": "Ford",
    "model_name": "F250 Super Duty Super Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2000,
    "manufacturer_name": "Ford",
    "model_name": "Excursion",
    "car_type": "SUV"
  },
  {
    "year": 2000,
    "manufacturer_name": "Ford",
    "model_name": "Explorer",
    "car_type": "SUV"
  },
  {
    "year": 2000,
    "manufacturer_name": "Ford",
    "model_name": "F250 Super Duty Crew Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2000,
    "manufacturer_name": "Ford",
    "model_name": "Econoline E250 Cargo",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2000,
    "manufacturer_name": "Ford",
    "model_name": "Escort",
    "car_type": "Sedan, Coupe"
  },
  {
    "year": 2000,
    "manufacturer_name": "Ford",
    "model_name": "F150 Super Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2000,
    "manufacturer_name": "Ford",
    "model_name": "Expedition",
    "car_type": "SUV"
  },
  {
    "year": 2000,
    "manufacturer_name": "Ford",
    "model_name": "F350 Super Duty Crew Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2000,
    "manufacturer_name": "Ford",
    "model_name": "Explorer Sport",
    "car_type": "SUV"
  },
  {
    "year": 2000,
    "manufacturer_name": "Ford",
    "model_name": "F250 Super Duty Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2000,
    "manufacturer_name": "Ford",
    "model_name": "Taurus",
    "car_type": "Sedan, Wagon"
  },
  {
    "year": 2000,
    "manufacturer_name": "Ford",
    "model_name": "F350 Super Duty Super Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2000,
    "manufacturer_name": "GMC",
    "model_name": "Envoy",
    "car_type": "SUV"
  },
  {
    "year": 2000,
    "manufacturer_name": "GMC",
    "model_name": "Savana 1500 Cargo",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2000,
    "manufacturer_name": "Ford",
    "model_name": "Mustang",
    "car_type": "Convertible, Coupe"
  },
  {
    "year": 2000,
    "manufacturer_name": "Ford",
    "model_name": "Focus",
    "car_type": "Sedan, Hatchback, Wagon"
  },
  {
    "year": 2000,
    "manufacturer_name": "Ford",
    "model_name": "Ranger Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2000,
    "manufacturer_name": "Ford",
    "model_name": "Windstar Passenger",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2000,
    "manufacturer_name": "Ford",
    "model_name": "F350 Super Duty Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2000,
    "manufacturer_name": "GMC",
    "model_name": "Safari Cargo",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2000,
    "manufacturer_name": "GMC",
    "model_name": "Jimmy",
    "car_type": "SUV"
  },
  {
    "year": 2000,
    "manufacturer_name": "Ford",
    "model_name": "Ranger Super Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2000,
    "manufacturer_name": "Ford",
    "model_name": "Windstar Cargo",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2000,
    "manufacturer_name": "GMC",
    "model_name": "Yukon XL 2500",
    "car_type": "SUV"
  },
  {
    "year": 2000,
    "manufacturer_name": "Hyundai",
    "model_name": "Tiburon",
    "car_type": "Hatchback"
  },
  {
    "year": 2000,
    "manufacturer_name": "GMC",
    "model_name": "Sierra (Classic) 3500 Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2000,
    "manufacturer_name": "Hyundai",
    "model_name": "Accent",
    "car_type": "Hatchback, Sedan"
  },
  {
    "year": 2000,
    "manufacturer_name": "GMC",
    "model_name": "Savana 3500 Cargo",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2000,
    "manufacturer_name": "GMC",
    "model_name": "Sierra 1500 Extended Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2000,
    "manufacturer_name": "INFINITI",
    "model_name": "G",
    "car_type": "Sedan"
  },
  {
    "year": 2000,
    "manufacturer_name": "GMC",
    "model_name": "Safari Passenger",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2000,
    "manufacturer_name": "GMC",
    "model_name": "Savana 2500 Passenger",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2000,
    "manufacturer_name": "GMC",
    "model_name": "Sierra 1500 Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2000,
    "manufacturer_name": "Honda",
    "model_name": "Civic",
    "car_type": "Coupe, Sedan, Hatchback"
  },
  {
    "year": 2000,
    "manufacturer_name": "GMC",
    "model_name": "Savana 1500 Passenger",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2000,
    "manufacturer_name": "GMC",
    "model_name": "Sierra (Classic) 3500 Crew Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2000,
    "manufacturer_name": "GMC",
    "model_name": "Yukon Denali",
    "car_type": "SUV"
  },
  {
    "year": 2000,
    "manufacturer_name": "GMC",
    "model_name": "Sierra (Classic) 2500 HD Extended Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2000,
    "manufacturer_name": "GMC",
    "model_name": "Savana 2500 Cargo",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2000,
    "manufacturer_name": "GMC",
    "model_name": "Sierra (Classic) 3500 Extended Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2000,
    "manufacturer_name": "Honda",
    "model_name": "Insight",
    "car_type": "Hatchback"
  },
  {
    "year": 2000,
    "manufacturer_name": "GMC",
    "model_name": "Savana 3500 Passenger",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2000,
    "manufacturer_name": "Honda",
    "model_name": "CR-V",
    "car_type": "SUV"
  },
  {
    "year": 2000,
    "manufacturer_name": "HUMMER",
    "model_name": "H1",
    "car_type": "SUV, Wagon"
  },
  {
    "year": 2000,
    "manufacturer_name": "GMC",
    "model_name": "Sonoma Extended Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2000,
    "manufacturer_name": "GMC",
    "model_name": "Sierra 2500 Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2000,
    "manufacturer_name": "GMC",
    "model_name": "Yukon",
    "car_type": "SUV"
  },
  {
    "year": 2000,
    "manufacturer_name": "GMC",
    "model_name": "Yukon XL 1500",
    "car_type": "SUV"
  },
  {
    "year": 2000,
    "manufacturer_name": "Honda",
    "model_name": "Odyssey",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2000,
    "manufacturer_name": "Honda",
    "model_name": "Prelude",
    "car_type": "Coupe"
  },
  {
    "year": 2000,
    "manufacturer_name": "Hyundai",
    "model_name": "Sonata",
    "car_type": "Sedan"
  },
  {
    "year": 2000,
    "manufacturer_name": "GMC",
    "model_name": "Sierra 2500 HD Extended Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2000,
    "manufacturer_name": "GMC",
    "model_name": "Sierra 2500 HD Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2000,
    "manufacturer_name": "GMC",
    "model_name": "Sierra (Classic) 2500 HD Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2000,
    "manufacturer_name": "GMC",
    "model_name": "Sonoma Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2000,
    "manufacturer_name": "Hyundai",
    "model_name": "Elantra",
    "car_type": "Wagon, Sedan"
  },
  {
    "year": 2000,
    "manufacturer_name": "Honda",
    "model_name": "S2000",
    "car_type": "Convertible"
  },
  {
    "year": 2000,
    "manufacturer_name": "INFINITI",
    "model_name": "I",
    "car_type": "Sedan"
  },
  {
    "year": 2000,
    "manufacturer_name": "GMC",
    "model_name": "Sierra (Classic) 2500 Crew Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2000,
    "manufacturer_name": "Isuzu",
    "model_name": "Amigo",
    "car_type": "SUV"
  },
  {
    "year": 2000,
    "manufacturer_name": "Honda",
    "model_name": "Passport",
    "car_type": "SUV"
  },
  {
    "year": 2000,
    "manufacturer_name": "GMC",
    "model_name": "Sierra 2500 Extended Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2000,
    "manufacturer_name": "INFINITI",
    "model_name": "QX",
    "car_type": "SUV"
  },
  {
    "year": 2000,
    "manufacturer_name": "Honda",
    "model_name": "Accord",
    "car_type": "Sedan, Coupe"
  },
  {
    "year": 2000,
    "manufacturer_name": "Isuzu",
    "model_name": "Trooper",
    "car_type": "SUV"
  },
  {
    "year": 2000,
    "manufacturer_name": "Isuzu",
    "model_name": "Hombre Spacecab",
    "car_type": "Pickup"
  },
  {
    "year": 2000,
    "manufacturer_name": "Isuzu",
    "model_name": "Rodeo",
    "car_type": "SUV"
  },
  {
    "year": 2000,
    "manufacturer_name": "INFINITI",
    "model_name": "Q",
    "car_type": "Sedan"
  },
  {
    "year": 2000,
    "manufacturer_name": "Isuzu",
    "model_name": "Hombre Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2000,
    "manufacturer_name": "Isuzu",
    "model_name": "VehiCROSS",
    "car_type": "SUV"
  },
  {
    "year": 2000,
    "manufacturer_name": "Jaguar",
    "model_name": "S-Type",
    "car_type": "Sedan"
  },
  {
    "year": 2000,
    "manufacturer_name": "Jaguar",
    "model_name": "XJ",
    "car_type": "Sedan"
  },
  {
    "year": 2000,
    "manufacturer_name": "Jaguar",
    "model_name": "XK",
    "car_type": "Coupe, Convertible"
  },
  {
    "year": 2000,
    "manufacturer_name": "Jeep",
    "model_name": "Cherokee",
    "car_type": "SUV"
  },
  {
    "year": 2000,
    "manufacturer_name": "Jeep",
    "model_name": "Wrangler",
    "car_type": "SUV"
  },
  {
    "year": 2000,
    "manufacturer_name": "Kia",
    "model_name": "Sportage",
    "car_type": "SUV"
  },
  {
    "year": 2000,
    "manufacturer_name": "Lincoln",
    "model_name": "LS",
    "car_type": "Sedan"
  },
  {
    "year": 2000,
    "manufacturer_name": "Kia",
    "model_name": "Sephia",
    "car_type": "Sedan"
  },
  {
    "year": 2000,
    "manufacturer_name": "Lexus",
    "model_name": "RX",
    "car_type": "SUV"
  },
  {
    "year": 2000,
    "manufacturer_name": "Land Rover",
    "model_name": "Discovery Series II",
    "car_type": "SUV"
  },
  {
    "year": 2000,
    "manufacturer_name": "Jeep",
    "model_name": "Grand Cherokee",
    "car_type": "SUV"
  },
  {
    "year": 2000,
    "manufacturer_name": "Lexus",
    "model_name": "LS",
    "car_type": "Sedan"
  },
  {
    "year": 2000,
    "manufacturer_name": "Kia",
    "model_name": "Spectra",
    "car_type": "Hatchback"
  },
  {
    "year": 2000,
    "manufacturer_name": "Lincoln",
    "model_name": "Continental",
    "car_type": "Sedan"
  },
  {
    "year": 2000,
    "manufacturer_name": "Lexus",
    "model_name": "GS",
    "car_type": "Sedan"
  },
  {
    "year": 2000,
    "manufacturer_name": "Lexus",
    "model_name": "SC",
    "car_type": "Coupe"
  },
  {
    "year": 2000,
    "manufacturer_name": "Lexus",
    "model_name": "ES",
    "car_type": "Sedan"
  },
  {
    "year": 2000,
    "manufacturer_name": "Lexus",
    "model_name": "LX",
    "car_type": "SUV"
  },
  {
    "year": 2000,
    "manufacturer_name": "MAZDA",
    "model_name": "Millenia",
    "car_type": "Sedan"
  },
  {
    "year": 2000,
    "manufacturer_name": "MAZDA",
    "model_name": "B-Series Cab Plus",
    "car_type": "Pickup"
  },
  {
    "year": 2000,
    "manufacturer_name": "MAZDA",
    "model_name": "626",
    "car_type": "Sedan"
  },
  {
    "year": 2000,
    "manufacturer_name": "Lincoln",
    "model_name": "Navigator",
    "car_type": "SUV"
  },
  {
    "year": 2000,
    "manufacturer_name": "Land Rover",
    "model_name": "Range Rover",
    "car_type": "SUV"
  },
  {
    "year": 2000,
    "manufacturer_name": "Mercedes-Benz",
    "model_name": "M-Class",
    "car_type": "SUV"
  },
  {
    "year": 2000,
    "manufacturer_name": "Mercedes-Benz",
    "model_name": "S-Class",
    "car_type": "Sedan"
  },
  {
    "year": 2000,
    "manufacturer_name": "Mitsubishi",
    "model_name": "Eclipse",
    "car_type": "Coupe"
  },
  {
    "year": 2000,
    "manufacturer_name": "Lincoln",
    "model_name": "Town Car",
    "car_type": "Sedan"
  },
  {
    "year": 2000,
    "manufacturer_name": "Mercury",
    "model_name": "Mystique",
    "car_type": "Sedan"
  },
  {
    "year": 2000,
    "manufacturer_name": "MAZDA",
    "model_name": "MPV",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2000,
    "manufacturer_name": "Mercury",
    "model_name": "Cougar",
    "car_type": "Coupe"
  },
  {
    "year": 2000,
    "manufacturer_name": "Mercury",
    "model_name": "Mountaineer",
    "car_type": "SUV"
  },
  {
    "year": 2000,
    "manufacturer_name": "MAZDA",
    "model_name": "B-Series Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2000,
    "manufacturer_name": "Mercedes-Benz",
    "model_name": "SL-Class",
    "car_type": "Convertible"
  },
  {
    "year": 2000,
    "manufacturer_name": "MAZDA",
    "model_name": "MX-5 Miata",
    "car_type": "Convertible"
  },
  {
    "year": 2000,
    "manufacturer_name": "Mitsubishi",
    "model_name": "Diamante",
    "car_type": "Sedan"
  },
  {
    "year": 2000,
    "manufacturer_name": "MAZDA",
    "model_name": "Protege",
    "car_type": "Sedan"
  },
  {
    "year": 2000,
    "manufacturer_name": "Mercedes-Benz",
    "model_name": "CL-Class",
    "car_type": "Coupe"
  },
  {
    "year": 2000,
    "manufacturer_name": "Mercedes-Benz",
    "model_name": "C-Class",
    "car_type": "Sedan"
  },
  {
    "year": 2000,
    "manufacturer_name": "Mercedes-Benz",
    "model_name": "CLK-Class",
    "car_type": "Coupe, Convertible"
  },
  {
    "year": 2000,
    "manufacturer_name": "Mercedes-Benz",
    "model_name": "SLK-Class",
    "car_type": "Convertible"
  },
  {
    "year": 2000,
    "manufacturer_name": "Mercedes-Benz",
    "model_name": "E-Class",
    "car_type": "Sedan, Wagon"
  },
  {
    "year": 2000,
    "manufacturer_name": "Mercury",
    "model_name": "Grand Marquis",
    "car_type": "Sedan"
  },
  {
    "year": 2000,
    "manufacturer_name": "Mercury",
    "model_name": "Villager",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2000,
    "manufacturer_name": "Mitsubishi",
    "model_name": "Galant",
    "car_type": "Sedan"
  },
  {
    "year": 2000,
    "manufacturer_name": "Mitsubishi",
    "model_name": "Montero Sport",
    "car_type": "SUV"
  },
  {
    "year": 2000,
    "manufacturer_name": "Nissan",
    "model_name": "Maxima",
    "car_type": "Sedan"
  },
  {
    "year": 2000,
    "manufacturer_name": "Mercury",
    "model_name": "Sable",
    "car_type": "Wagon, Sedan"
  },
  {
    "year": 2000,
    "manufacturer_name": "Oldsmobile",
    "model_name": "Bravada",
    "car_type": "SUV"
  },
  {
    "year": 2000,
    "manufacturer_name": "Mitsubishi",
    "model_name": "Montero",
    "car_type": "SUV"
  },
  {
    "year": 2000,
    "manufacturer_name": "Plymouth",
    "model_name": "Grand Voyager",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2000,
    "manufacturer_name": "Mitsubishi",
    "model_name": "Mirage",
    "car_type": "Coupe, Sedan"
  },
  {
    "year": 2000,
    "manufacturer_name": "Nissan",
    "model_name": "Frontier Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2000,
    "manufacturer_name": "Nissan",
    "model_name": "Altima",
    "car_type": "Sedan"
  },
  {
    "year": 2000,
    "manufacturer_name": "Nissan",
    "model_name": "Frontier Crew Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2000,
    "manufacturer_name": "Nissan",
    "model_name": "Pathfinder",
    "car_type": "SUV"
  },
  {
    "year": 2000,
    "manufacturer_name": "Plymouth",
    "model_name": "Breeze",
    "car_type": "Sedan"
  },
  {
    "year": 2000,
    "manufacturer_name": "Nissan",
    "model_name": "Quest",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2000,
    "manufacturer_name": "Nissan",
    "model_name": "Xterra",
    "car_type": "SUV"
  },
  {
    "year": 2000,
    "manufacturer_name": "Nissan",
    "model_name": "Frontier King Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2000,
    "manufacturer_name": "Oldsmobile",
    "model_name": "Alero",
    "car_type": "Sedan, Coupe"
  },
  {
    "year": 2000,
    "manufacturer_name": "Suzuki",
    "model_name": "Esteem",
    "car_type": "Sedan, Wagon"
  },
  {
    "year": 2000,
    "manufacturer_name": "Pontiac",
    "model_name": "Bonneville",
    "car_type": "Sedan"
  },
  {
    "year": 2000,
    "manufacturer_name": "Oldsmobile",
    "model_name": "Silhouette",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2000,
    "manufacturer_name": "Porsche",
    "model_name": "Boxster",
    "car_type": "Convertible"
  },
  {
    "year": 2000,
    "manufacturer_name": "Saturn",
    "model_name": "L-Series",
    "car_type": "Sedan, Wagon"
  },
  {
    "year": 2000,
    "manufacturer_name": "Pontiac",
    "model_name": "Firebird",
    "car_type": "Coupe, Convertible"
  },
  {
    "year": 2000,
    "manufacturer_name": "Pontiac",
    "model_name": "Sunfire",
    "car_type": "Sedan, Coupe, Convertible"
  },
  {
    "year": 2000,
    "manufacturer_name": "Pontiac",
    "model_name": "Grand Prix",
    "car_type": "Sedan, Coupe"
  },
  {
    "year": 2000,
    "manufacturer_name": "Pontiac",
    "model_name": "Grand Am",
    "car_type": "Sedan, Coupe"
  },
  {
    "year": 2000,
    "manufacturer_name": "Nissan",
    "model_name": "Sentra",
    "car_type": "Sedan"
  },
  {
    "year": 2000,
    "manufacturer_name": "Saturn",
    "model_name": "S-Series",
    "car_type": "Coupe, Sedan, Wagon"
  },
  {
    "year": 2000,
    "manufacturer_name": "Toyota",
    "model_name": "Sienna",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2000,
    "manufacturer_name": "Plymouth",
    "model_name": "Neon",
    "car_type": "Sedan"
  },
  {
    "year": 2000,
    "manufacturer_name": "Plymouth",
    "model_name": "Voyager",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2000,
    "manufacturer_name": "Oldsmobile",
    "model_name": "Intrigue",
    "car_type": "Sedan"
  },
  {
    "year": 2000,
    "manufacturer_name": "Toyota",
    "model_name": "Echo",
    "car_type": "Sedan, Coupe"
  },
  {
    "year": 2000,
    "manufacturer_name": "Porsche",
    "model_name": "911",
    "car_type": "Coupe, Convertible"
  },
  {
    "year": 2000,
    "manufacturer_name": "Plymouth",
    "model_name": "Prowler",
    "car_type": "Convertible"
  },
  {
    "year": 2000,
    "manufacturer_name": "Saab",
    "model_name": "3-Sep",
    "car_type": "Hatchback, Convertible"
  },
  {
    "year": 2000,
    "manufacturer_name": "Suzuki",
    "model_name": "Swift",
    "car_type": "Hatchback"
  },
  {
    "year": 2000,
    "manufacturer_name": "Subaru",
    "model_name": "Impreza",
    "car_type": "Wagon, Sedan, Coupe"
  },
  {
    "year": 2000,
    "manufacturer_name": "Subaru",
    "model_name": "Forester",
    "car_type": "SUV"
  },
  {
    "year": 2000,
    "manufacturer_name": "Subaru",
    "model_name": "Outback",
    "car_type": "Wagon, Sedan"
  },
  {
    "year": 2000,
    "manufacturer_name": "Suzuki",
    "model_name": "Vitara",
    "car_type": "SUV"
  },
  {
    "year": 2000,
    "manufacturer_name": "Toyota",
    "model_name": "Avalon",
    "car_type": "Sedan"
  },
  {
    "year": 2000,
    "manufacturer_name": "Pontiac",
    "model_name": "Montana",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2000,
    "manufacturer_name": "Toyota",
    "model_name": "Corolla",
    "car_type": "Sedan"
  },
  {
    "year": 2000,
    "manufacturer_name": "Saab",
    "model_name": "5-Sep",
    "car_type": "Wagon, Sedan"
  },
  {
    "year": 2000,
    "manufacturer_name": "Toyota",
    "model_name": "Celica",
    "car_type": "Hatchback"
  },
  {
    "year": 2000,
    "manufacturer_name": "Suzuki",
    "model_name": "Grand Vitara",
    "car_type": "SUV"
  },
  {
    "year": 2000,
    "manufacturer_name": "Toyota",
    "model_name": "Tacoma Xtracab",
    "car_type": "Pickup"
  },
  {
    "year": 2000,
    "manufacturer_name": "Toyota",
    "model_name": "Land Cruiser",
    "car_type": "SUV"
  },
  {
    "year": 2000,
    "manufacturer_name": "Toyota",
    "model_name": "4Runner",
    "car_type": "SUV"
  },
  {
    "year": 2000,
    "manufacturer_name": "Subaru",
    "model_name": "Legacy",
    "car_type": "Wagon, Sedan"
  },
  {
    "year": 2000,
    "manufacturer_name": "Toyota",
    "model_name": "Tacoma Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2000,
    "manufacturer_name": "Toyota",
    "model_name": "Solara",
    "car_type": "Coupe, Convertible"
  },
  {
    "year": 2000,
    "manufacturer_name": "Toyota",
    "model_name": "Camry",
    "car_type": "Sedan"
  },
  {
    "year": 2000,
    "manufacturer_name": "Toyota",
    "model_name": "MR2",
    "car_type": "Convertible"
  },
  {
    "year": 2000,
    "manufacturer_name": "Toyota",
    "model_name": "RAV4",
    "car_type": "SUV"
  },
  {
    "year": 2000,
    "manufacturer_name": "Toyota",
    "model_name": "Tundra Access Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2000,
    "manufacturer_name": "Volkswagen",
    "model_name": "Eurovan",
    "car_type": "Van/Minivan"
  },
  {
    "year": 2000,
    "manufacturer_name": "Toyota",
    "model_name": "Tundra Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 2000,
    "manufacturer_name": "Volkswagen",
    "model_name": "Golf",
    "car_type": "Hatchback"
  },
  {
    "year": 2000,
    "manufacturer_name": "Volkswagen",
    "model_name": "Jetta",
    "car_type": "Sedan"
  },
  {
    "year": 2000,
    "manufacturer_name": "Volkswagen",
    "model_name": "GTI",
    "car_type": "Hatchback"
  },
  {
    "year": 2000,
    "manufacturer_name": "Volkswagen",
    "model_name": "Cabrio",
    "car_type": "Convertible"
  },
  {
    "year": 2000,
    "manufacturer_name": "Volkswagen",
    "model_name": "New Beetle",
    "car_type": "Hatchback"
  },
  {
    "year": 2000,
    "manufacturer_name": "Volvo",
    "model_name": "S70",
    "car_type": "Sedan"
  },
  {
    "year": 2000,
    "manufacturer_name": "Volvo",
    "model_name": "V40",
    "car_type": "Wagon"
  },
  {
    "year": 1999,
    "manufacturer_name": "Acura",
    "model_name": "SLX",
    "car_type": "SUV"
  },
  {
    "year": 1999,
    "manufacturer_name": "Acura",
    "model_name": "NSX",
    "car_type": "Convertible, Coupe"
  },
  {
    "year": 2000,
    "manufacturer_name": "Volvo",
    "model_name": "V70",
    "car_type": "Wagon"
  },
  {
    "year": 2000,
    "manufacturer_name": "Volvo",
    "model_name": "C70",
    "car_type": "Coupe, Convertible"
  },
  {
    "year": 2000,
    "manufacturer_name": "Volkswagen",
    "model_name": "Passat",
    "car_type": "Wagon, Sedan"
  },
  {
    "year": 2000,
    "manufacturer_name": "Volvo",
    "model_name": "S40",
    "car_type": "Sedan"
  },
  {
    "year": 2000,
    "manufacturer_name": "Volvo",
    "model_name": "S80",
    "car_type": "Sedan"
  },
  {
    "year": 1999,
    "manufacturer_name": "Acura",
    "model_name": "Integra",
    "car_type": "Sedan, Hatchback"
  },
  {
    "year": 1999,
    "manufacturer_name": "Acura",
    "model_name": "CL",
    "car_type": "Coupe"
  },
  {
    "year": 1999,
    "manufacturer_name": "Acura",
    "model_name": "RL",
    "car_type": "Sedan"
  },
  {
    "year": 1999,
    "manufacturer_name": "Buick",
    "model_name": "Regal",
    "car_type": "Sedan"
  },
  {
    "year": 1999,
    "manufacturer_name": "Chevrolet",
    "model_name": "2500 Crew Cab",
    "car_type": "Pickup"
  },
  {
    "year": 1999,
    "manufacturer_name": "BMW",
    "model_name": "3 Series",
    "car_type": "Coupe, Hatchback, Convertible, Sedan"
  },
  {
    "year": 1999,
    "manufacturer_name": "BMW",
    "model_name": "7 Series",
    "car_type": "Sedan"
  },
  {
    "year": 1999,
    "manufacturer_name": "Cadillac",
    "model_name": "Eldorado",
    "car_type": "Coupe"
  },
  {
    "year": 1999,
    "manufacturer_name": "Audi",
    "model_name": "A4",
    "car_type": "Sedan, Wagon"
  },
  {
    "year": 1999,
    "manufacturer_name": "Chevrolet",
    "model_name": "2500 HD Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 1999,
    "manufacturer_name": "Acura",
    "model_name": "TL",
    "car_type": "Sedan"
  },
  {
    "year": 1999,
    "manufacturer_name": "Cadillac",
    "model_name": "Escalade",
    "car_type": "SUV"
  },
  {
    "year": 1999,
    "manufacturer_name": "Audi",
    "model_name": "A8",
    "car_type": "Sedan"
  },
  {
    "year": 1999,
    "manufacturer_name": "BMW",
    "model_name": "M3",
    "car_type": "Coupe, Convertible"
  },
  {
    "year": 1999,
    "manufacturer_name": "Cadillac",
    "model_name": "Catera",
    "car_type": "Sedan"
  },
  {
    "year": 1999,
    "manufacturer_name": "Buick",
    "model_name": "LeSabre",
    "car_type": "Sedan"
  },
  {
    "year": 1999,
    "manufacturer_name": "Audi",
    "model_name": "A6",
    "car_type": "Sedan, Wagon"
  },
  {
    "year": 1999,
    "manufacturer_name": "BMW",
    "model_name": "5 Series",
    "car_type": "Wagon, Sedan"
  },
  {
    "year": 1999,
    "manufacturer_name": "Buick",
    "model_name": "Riviera",
    "car_type": "Coupe"
  },
  {
    "year": 1999,
    "manufacturer_name": "Cadillac",
    "model_name": "DeVille",
    "car_type": "Sedan"
  },
  {
    "year": 1999,
    "manufacturer_name": "Buick",
    "model_name": "Park Avenue",
    "car_type": "Sedan"
  },
  {
    "year": 1999,
    "manufacturer_name": "Chevrolet",
    "model_name": "Astro Passenger",
    "car_type": "Van/Minivan"
  },
  {
    "year": 1999,
    "manufacturer_name": "Buick",
    "model_name": "Century",
    "car_type": "Sedan"
  },
  {
    "year": 1999,
    "manufacturer_name": "Chevrolet",
    "model_name": "3500 Crew Cab",
    "car_type": "Pickup"
  },
  {
    "year": 1999,
    "manufacturer_name": "Chevrolet",
    "model_name": "Astro Cargo",
    "car_type": "Van/Minivan"
  },
  {
    "year": 1999,
    "manufacturer_name": "Cadillac",
    "model_name": "Seville",
    "car_type": "Sedan"
  },
  {
    "year": 1999,
    "manufacturer_name": "Chevrolet",
    "model_name": "1500 Extended Cab",
    "car_type": "Pickup"
  },
  {
    "year": 1999,
    "manufacturer_name": "BMW",
    "model_name": "Z3",
    "car_type": "Convertible, Coupe"
  },
  {
    "year": 1999,
    "manufacturer_name": "Chevrolet",
    "model_name": "2500 HD Extended Cab",
    "car_type": "Pickup"
  },
  {
    "year": 1999,
    "manufacturer_name": "Chevrolet",
    "model_name": "3500 Extended Cab",
    "car_type": "Pickup"
  },
  {
    "year": 1999,
    "manufacturer_name": "Chevrolet",
    "model_name": "Blazer",
    "car_type": "SUV"
  },
  {
    "year": 1999,
    "manufacturer_name": "Chevrolet",
    "model_name": "Metro",
    "car_type": "Coupe, Sedan"
  },
  {
    "year": 1999,
    "manufacturer_name": "Chevrolet",
    "model_name": "Prizm",
    "car_type": "Sedan"
  },
  {
    "year": 1999,
    "manufacturer_name": "Chevrolet",
    "model_name": "Malibu",
    "car_type": "Sedan"
  },
  {
    "year": 1999,
    "manufacturer_name": "Chevrolet",
    "model_name": "Express 1500 Cargo",
    "car_type": "Van/Minivan"
  },
  {
    "year": 1999,
    "manufacturer_name": "Chevrolet",
    "model_name": "Camaro",
    "car_type": "Coupe, Convertible"
  },
  {
    "year": 1999,
    "manufacturer_name": "Chevrolet",
    "model_name": "Express 3500 Cargo",
    "car_type": "Van/Minivan"
  },
  {
    "year": 1999,
    "manufacturer_name": "Chevrolet",
    "model_name": "Corvette",
    "car_type": "Coupe, Convertible"
  },
  {
    "year": 1999,
    "manufacturer_name": "Chevrolet",
    "model_name": "Silverado 1500 Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 1999,
    "manufacturer_name": "Chevrolet",
    "model_name": "Tracker",
    "car_type": "SUV"
  },
  {
    "year": 1999,
    "manufacturer_name": "Chevrolet",
    "model_name": "Silverado 2500 Extended Cab",
    "car_type": "Pickup"
  },
  {
    "year": 1999,
    "manufacturer_name": "Chevrolet",
    "model_name": "Suburban 2500",
    "car_type": "SUV"
  },
  {
    "year": 1999,
    "manufacturer_name": "Chevrolet",
    "model_name": "3500 Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 1999,
    "manufacturer_name": "Chevrolet",
    "model_name": "Lumina",
    "car_type": "Sedan"
  },
  {
    "year": 1999,
    "manufacturer_name": "Chevrolet",
    "model_name": "S10 Extended Cab",
    "car_type": "Pickup"
  },
  {
    "year": 1999,
    "manufacturer_name": "Chevrolet",
    "model_name": "Express 3500 Passenger",
    "car_type": "Van/Minivan"
  },
  {
    "year": 1999,
    "manufacturer_name": "Chevrolet",
    "model_name": "Monte Carlo",
    "car_type": "Coupe"
  },
  {
    "year": 1999,
    "manufacturer_name": "Chevrolet",
    "model_name": "Silverado 2500 HD Extended Cab",
    "car_type": "Pickup"
  },
  {
    "year": 1999,
    "manufacturer_name": "Chevrolet",
    "model_name": "Cavalier",
    "car_type": "Coupe, Sedan, Convertible"
  },
  {
    "year": 1999,
    "manufacturer_name": "Chevrolet",
    "model_name": "Express 2500 Cargo",
    "car_type": "Van/Minivan"
  },
  {
    "year": 1999,
    "manufacturer_name": "Chevrolet",
    "model_name": "Express 1500 Passenger",
    "car_type": "Van/Minivan"
  },
  {
    "year": 1999,
    "manufacturer_name": "Chevrolet",
    "model_name": "Silverado 2500 HD Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 1999,
    "manufacturer_name": "Chevrolet",
    "model_name": "Express 2500 Passenger",
    "car_type": "Van/Minivan"
  },
  {
    "year": 1999,
    "manufacturer_name": "Chevrolet",
    "model_name": "S10 Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 1999,
    "manufacturer_name": "Chevrolet",
    "model_name": "Silverado 1500 Extended Cab",
    "car_type": "Pickup"
  },
  {
    "year": 1999,
    "manufacturer_name": "Chevrolet",
    "model_name": "Suburban 1500",
    "car_type": "SUV"
  },
  {
    "year": 1999,
    "manufacturer_name": "Chrysler",
    "model_name": "Sebring",
    "car_type": "Coupe, Convertible"
  },
  {
    "year": 1999,
    "manufacturer_name": "Chrysler",
    "model_name": "Town & Country",
    "car_type": "Van/Minivan"
  },
  {
    "year": 1999,
    "manufacturer_name": "Daewoo",
    "model_name": "Leganza",
    "car_type": "Sedan"
  },
  {
    "year": 1999,
    "manufacturer_name": "Chrysler",
    "model_name": "Concorde",
    "car_type": "Sedan"
  },
  {
    "year": 1999,
    "manufacturer_name": "Chevrolet",
    "model_name": "Venture Passenger",
    "car_type": "Van/Minivan"
  },
  {
    "year": 1999,
    "manufacturer_name": "Chrysler",
    "model_name": "300",
    "car_type": "Sedan"
  },
  {
    "year": 1999,
    "manufacturer_name": "Chevrolet",
    "model_name": "Silverado 2500 Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 1999,
    "manufacturer_name": "Daewoo",
    "model_name": "Lanos",
    "car_type": "Hatchback, Sedan"
  },
  {
    "year": 1999,
    "manufacturer_name": "Chrysler",
    "model_name": "Cirrus",
    "car_type": "Sedan"
  },
  {
    "year": 1999,
    "manufacturer_name": "Chevrolet",
    "model_name": "Tahoe",
    "car_type": "SUV"
  },
  {
    "year": 1999,
    "manufacturer_name": "Dodge",
    "model_name": "Avenger",
    "car_type": "Coupe"
  },
  {
    "year": 1999,
    "manufacturer_name": "Chevrolet",
    "model_name": "Venture Cargo",
    "car_type": "Van/Minivan"
  },
  {
    "year": 1999,
    "manufacturer_name": "Dodge",
    "model_name": "Ram 1500 Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 1999,
    "manufacturer_name": "Dodge",
    "model_name": "Ram 1500 Quad Cab",
    "car_type": "Pickup"
  },
  {
    "year": 1999,
    "manufacturer_name": "Dodge",
    "model_name": "Intrepid",
    "car_type": "Sedan"
  },
  {
    "year": 1999,
    "manufacturer_name": "Dodge",
    "model_name": "Durango",
    "car_type": "SUV"
  },
  {
    "year": 1999,
    "manufacturer_name": "Dodge",
    "model_name": "Ram 3500 Quad Cab",
    "car_type": "Pickup"
  },
  {
    "year": 1999,
    "manufacturer_name": "Dodge",
    "model_name": "Dakota Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 1999,
    "manufacturer_name": "Dodge",
    "model_name": "Caravan Passenger",
    "car_type": "Van/Minivan"
  },
  {
    "year": 1999,
    "manufacturer_name": "Dodge",
    "model_name": "Ram 2500 Club Cab",
    "car_type": "Pickup"
  },
  {
    "year": 1999,
    "manufacturer_name": "Dodge",
    "model_name": "Grand Caravan Passenger",
    "car_type": "Van/Minivan"
  },
  {
    "year": 1999,
    "manufacturer_name": "Dodge",
    "model_name": "Dakota Club Cab",
    "car_type": "Pickup"
  },
  {
    "year": 1999,
    "manufacturer_name": "Dodge",
    "model_name": "Ram 1500 Club Cab",
    "car_type": "Pickup"
  },
  {
    "year": 1999,
    "manufacturer_name": "Chrysler",
    "model_name": "LHS",
    "car_type": "Sedan"
  },
  {
    "year": 1999,
    "manufacturer_name": "Daewoo",
    "model_name": "Nubira",
    "car_type": "Wagon, Sedan, Hatchback"
  },
  {
    "year": 1999,
    "manufacturer_name": "Dodge",
    "model_name": "Ram 2500 Quad Cab",
    "car_type": "Pickup"
  },
  {
    "year": 1999,
    "manufacturer_name": "Dodge",
    "model_name": "Neon",
    "car_type": "Coupe, Sedan"
  },
  {
    "year": 1999,
    "manufacturer_name": "Dodge",
    "model_name": "Ram 2500 Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 1999,
    "manufacturer_name": "Dodge",
    "model_name": "Ram 3500 Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 1999,
    "manufacturer_name": "Dodge",
    "model_name": "Ram Van 3500",
    "car_type": "Van/Minivan"
  },
  {
    "year": 1999,
    "manufacturer_name": "Ford",
    "model_name": "F250 Super Duty Crew Cab",
    "car_type": "Pickup"
  },
  {
    "year": 1999,
    "manufacturer_name": "Ford",
    "model_name": "Econoline E350 Cargo",
    "car_type": "Van/Minivan"
  },
  {
    "year": 1999,
    "manufacturer_name": "Ford",
    "model_name": "Econoline E250 Cargo",
    "car_type": "Van/Minivan"
  },
  {
    "year": 1999,
    "manufacturer_name": "Ford",
    "model_name": "Econoline E150 Cargo",
    "car_type": "Van/Minivan"
  },
  {
    "year": 1999,
    "manufacturer_name": "Dodge",
    "model_name": "Ram Van 1500",
    "car_type": "Van/Minivan"
  },
  {
    "year": 1999,
    "manufacturer_name": "Ford",
    "model_name": "Crown Victoria",
    "car_type": "Sedan"
  },
  {
    "year": 1999,
    "manufacturer_name": "Ford",
    "model_name": "Contour",
    "car_type": "Sedan"
  },
  {
    "year": 1999,
    "manufacturer_name": "Ford",
    "model_name": "Explorer",
    "car_type": "SUV"
  },
  {
    "year": 1999,
    "manufacturer_name": "Dodge",
    "model_name": "Ram Wagon 2500",
    "car_type": "Van/Minivan"
  },
  {
    "year": 1999,
    "manufacturer_name": "Dodge",
    "model_name": "Viper",
    "car_type": "Coupe, Convertible"
  },
  {
    "year": 1999,
    "manufacturer_name": "Dodge",
    "model_name": "Ram Wagon 1500",
    "car_type": "Van/Minivan"
  },
  {
    "year": 1999,
    "manufacturer_name": "Dodge",
    "model_name": "Ram Wagon 3500",
    "car_type": "Van/Minivan"
  },
  {
    "year": 1999,
    "manufacturer_name": "Ford",
    "model_name": "Econoline E350 Super Duty Passenger",
    "car_type": "Van/Minivan"
  },
  {
    "year": 1999,
    "manufacturer_name": "Dodge",
    "model_name": "Ram Van 2500",
    "car_type": "Van/Minivan"
  },
  {
    "year": 1999,
    "manufacturer_name": "Ford",
    "model_name": "F150 Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 1999,
    "manufacturer_name": "Dodge",
    "model_name": "Stratus",
    "car_type": "Sedan"
  },
  {
    "year": 1999,
    "manufacturer_name": "Ford",
    "model_name": "Econoline E150 Passenger",
    "car_type": "Van/Minivan"
  },
  {
    "year": 1999,
    "manufacturer_name": "Ford",
    "model_name": "Escort",
    "car_type": "Sedan, Wagon, Coupe"
  },
  {
    "year": 1999,
    "manufacturer_name": "Ford",
    "model_name": "Econoline E350 Super Duty Cargo",
    "car_type": "Van/Minivan"
  },
  {
    "year": 1999,
    "manufacturer_name": "Ford",
    "model_name": "F250 Super Duty Super Cab",
    "car_type": "Pickup"
  },
  {
    "year": 1999,
    "manufacturer_name": "Ford",
    "model_name": "F250 Super Duty Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 1999,
    "manufacturer_name": "Ford",
    "model_name": "F150 Super Cab",
    "car_type": "Pickup"
  },
  {
    "year": 1999,
    "manufacturer_name": "Ford",
    "model_name": "Expedition",
    "car_type": "SUV"
  },
  {
    "year": 1999,
    "manufacturer_name": "Ford",
    "model_name": "F250 Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 1999,
    "manufacturer_name": "Ford",
    "model_name": "F350 Super Duty Super Cab",
    "car_type": "Pickup"
  },
  {
    "year": 1999,
    "manufacturer_name": "Ford",
    "model_name": "Mustang",
    "car_type": "Coupe, Convertible"
  },
  {
    "year": 1999,
    "manufacturer_name": "Ford",
    "model_name": "F250 Super Cab",
    "car_type": "Pickup"
  },
  {
    "year": 1999,
    "manufacturer_name": "Ford",
    "model_name": "Windstar Cargo",
    "car_type": "Van/Minivan"
  },
  {
    "year": 1999,
    "manufacturer_name": "Ford",
    "model_name": "F350 Super Duty Crew Cab",
    "car_type": "Pickup"
  },
  {
    "year": 1999,
    "manufacturer_name": "GMC",
    "model_name": "2500 Crew Cab",
    "car_type": "Pickup"
  },
  {
    "year": 1999,
    "manufacturer_name": "GMC",
    "model_name": "3500 Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 1999,
    "manufacturer_name": "Ford",
    "model_name": "Windstar Passenger",
    "car_type": "Van/Minivan"
  },
  {
    "year": 1999,
    "manufacturer_name": "GMC",
    "model_name": "Jimmy",
    "car_type": "SUV"
  },
  {
    "year": 1999,
    "manufacturer_name": "GMC",
    "model_name": "Safari Cargo",
    "car_type": "Van/Minivan"
  },
  {
    "year": 1999,
    "manufacturer_name": "GMC",
    "model_name": "1500 Club Coupe",
    "car_type": "Pickup"
  },
  {
    "year": 1999,
    "manufacturer_name": "Ford",
    "model_name": "Ranger Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 1999,
    "manufacturer_name": "GMC",
    "model_name": "Savana 2500 Cargo",
    "car_type": "Van/Minivan"
  },
  {
    "year": 1999,
    "manufacturer_name": "Ford",
    "model_name": "Taurus",
    "car_type": "Sedan, Wagon"
  },
  {
    "year": 1999,
    "manufacturer_name": "Ford",
    "model_name": "F350 Super Duty Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 1999,
    "manufacturer_name": "GMC",
    "model_name": "Savana 1500 Passenger",
    "car_type": "Van/Minivan"
  },
  {
    "year": 1999,
    "manufacturer_name": "GMC",
    "model_name": "Savana 2500 Passenger",
    "car_type": "Van/Minivan"
  },
  {
    "year": 1999,
    "manufacturer_name": "GMC",
    "model_name": "Sierra 2500 Extended Cab",
    "car_type": "Pickup"
  },
  {
    "year": 1999,
    "manufacturer_name": "GMC",
    "model_name": "3500 Extended Cab",
    "car_type": "Pickup"
  },
  {
    "year": 1999,
    "manufacturer_name": "GMC",
    "model_name": "2500 HD Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 1999,
    "manufacturer_name": "GMC",
    "model_name": "Envoy",
    "car_type": "SUV"
  },
  {
    "year": 1999,
    "manufacturer_name": "GMC",
    "model_name": "Savana 1500 Cargo",
    "car_type": "Van/Minivan"
  },
  {
    "year": 1999,
    "manufacturer_name": "GMC",
    "model_name": "Savana 3500 Passenger",
    "car_type": "Van/Minivan"
  },
  {
    "year": 1999,
    "manufacturer_name": "GMC",
    "model_name": "2500 HD Extended Cab",
    "car_type": "Pickup"
  },
  {
    "year": 1999,
    "manufacturer_name": "Honda",
    "model_name": "Accord",
    "car_type": "Coupe, Sedan"
  },
  {
    "year": 1999,
    "manufacturer_name": "GMC",
    "model_name": "Sonoma Extended Cab",
    "car_type": "Pickup"
  },
  {
    "year": 1999,
    "manufacturer_name": "Ford",
    "model_name": "Ranger Super Cab",
    "car_type": "Pickup"
  },
  {
    "year": 1999,
    "manufacturer_name": "Isuzu",
    "model_name": "Trooper",
    "car_type": "SUV"
  },
  {
    "year": 1999,
    "manufacturer_name": "GMC",
    "model_name": "Sierra 2500 HD Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 1999,
    "manufacturer_name": "GMC",
    "model_name": "Safari Passenger",
    "car_type": "Van/Minivan"
  },
  {
    "year": 1999,
    "manufacturer_name": "GMC",
    "model_name": "Sierra 2500 Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 1999,
    "manufacturer_name": "GMC",
    "model_name": "3500 Crew Cab",
    "car_type": "Pickup"
  },
  {
    "year": 1999,
    "manufacturer_name": "Hyundai",
    "model_name": "Tiburon",
    "car_type": "Hatchback"
  },
  {
    "year": 1999,
    "manufacturer_name": "GMC",
    "model_name": "Savana 3500 Cargo",
    "car_type": "Van/Minivan"
  },
  {
    "year": 1999,
    "manufacturer_name": "Isuzu",
    "model_name": "Amigo",
    "car_type": "SUV"
  },
  {
    "year": 1999,
    "manufacturer_name": "Honda",
    "model_name": "Prelude",
    "car_type": "Coupe"
  },
  {
    "year": 1999,
    "manufacturer_name": "GMC",
    "model_name": "Sonoma Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 1999,
    "manufacturer_name": "GMC",
    "model_name": "Sierra 1500 Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 1999,
    "manufacturer_name": "GMC",
    "model_name": "Sierra 1500 Extended Cab",
    "car_type": "Pickup"
  },
  {
    "year": 1999,
    "manufacturer_name": "Honda",
    "model_name": "Civic",
    "car_type": "Coupe, Hatchback, Sedan"
  },
  {
    "year": 1999,
    "manufacturer_name": "GMC",
    "model_name": "Sierra 2500 HD Extended Cab",
    "car_type": "Pickup"
  },
  {
    "year": 1999,
    "manufacturer_name": "GMC",
    "model_name": "Suburban 2500",
    "car_type": "SUV"
  },
  {
    "year": 1999,
    "manufacturer_name": "Land Rover",
    "model_name": "Discovery Series II",
    "car_type": "SUV"
  },
  {
    "year": 1999,
    "manufacturer_name": "Honda",
    "model_name": "CR-V",
    "car_type": "SUV"
  },
  {
    "year": 1999,
    "manufacturer_name": "Honda",
    "model_name": "Passport",
    "car_type": "SUV"
  },
  {
    "year": 1999,
    "manufacturer_name": "GMC",
    "model_name": "Yukon",
    "car_type": "SUV"
  },
  {
    "year": 1999,
    "manufacturer_name": "Hyundai",
    "model_name": "Elantra",
    "car_type": "Sedan, Wagon"
  },
  {
    "year": 1999,
    "manufacturer_name": "Lexus",
    "model_name": "LX",
    "car_type": "SUV"
  },
  {
    "year": 1999,
    "manufacturer_name": "HUMMER",
    "model_name": "H1",
    "car_type": "SUV, Wagon"
  },
  {
    "year": 1999,
    "manufacturer_name": "Jeep",
    "model_name": "Grand Cherokee",
    "car_type": "SUV"
  },
  {
    "year": 1999,
    "manufacturer_name": "INFINITI",
    "model_name": "G",
    "car_type": "Sedan"
  },
  {
    "year": 1999,
    "manufacturer_name": "GMC",
    "model_name": "Suburban 1500",
    "car_type": "SUV"
  },
  {
    "year": 1999,
    "manufacturer_name": "Honda",
    "model_name": "Odyssey",
    "car_type": "Van/Minivan"
  },
  {
    "year": 1999,
    "manufacturer_name": "Hyundai",
    "model_name": "Sonata",
    "car_type": "Sedan"
  },
  {
    "year": 1999,
    "manufacturer_name": "Hyundai",
    "model_name": "Accent",
    "car_type": "Hatchback, Sedan"
  },
  {
    "year": 1999,
    "manufacturer_name": "INFINITI",
    "model_name": "I",
    "car_type": "Sedan"
  },
  {
    "year": 1999,
    "manufacturer_name": "INFINITI",
    "model_name": "QX",
    "car_type": "SUV"
  },
  {
    "year": 1999,
    "manufacturer_name": "INFINITI",
    "model_name": "Q",
    "car_type": "Sedan"
  },
  {
    "year": 1999,
    "manufacturer_name": "Isuzu",
    "model_name": "Hombre Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 1999,
    "manufacturer_name": "Jaguar",
    "model_name": "XK",
    "car_type": "Coupe, Convertible"
  },
  {
    "year": 1999,
    "manufacturer_name": "Jeep",
    "model_name": "Cherokee",
    "car_type": "SUV"
  },
  {
    "year": 1999,
    "manufacturer_name": "Isuzu",
    "model_name": "VehiCROSS",
    "car_type": "SUV"
  },
  {
    "year": 1999,
    "manufacturer_name": "Isuzu",
    "model_name": "Rodeo",
    "car_type": "SUV"
  },
  {
    "year": 1999,
    "manufacturer_name": "Jaguar",
    "model_name": "XJ",
    "car_type": "Sedan"
  },
  {
    "year": 1999,
    "manufacturer_name": "Isuzu",
    "model_name": "Hombre Spacecab",
    "car_type": "Pickup"
  },
  {
    "year": 1999,
    "manufacturer_name": "Jeep",
    "model_name": "Wrangler",
    "car_type": "SUV"
  },
  {
    "year": 1999,
    "manufacturer_name": "Land Rover",
    "model_name": "Discovery",
    "car_type": "SUV"
  },
  {
    "year": 1999,
    "manufacturer_name": "Isuzu",
    "model_name": "Oasis",
    "car_type": "Van/Minivan"
  },
  {
    "year": 1999,
    "manufacturer_name": "Kia",
    "model_name": "Sportage",
    "car_type": "SUV"
  },
  {
    "year": 1999,
    "manufacturer_name": "Lexus",
    "model_name": "GS",
    "car_type": "Sedan"
  },
  {
    "year": 1999,
    "manufacturer_name": "Lexus",
    "model_name": "ES",
    "car_type": "Sedan"
  },
  {
    "year": 1999,
    "manufacturer_name": "Kia",
    "model_name": "Sephia",
    "car_type": "Sedan"
  },
  {
    "year": 1999,
    "manufacturer_name": "Lexus",
    "model_name": "LS",
    "car_type": "Sedan"
  },
  {
    "year": 1999,
    "manufacturer_name": "Land Rover",
    "model_name": "Range Rover",
    "car_type": "SUV"
  },
  {
    "year": 1999,
    "manufacturer_name": "Lexus",
    "model_name": "RX",
    "car_type": "SUV"
  },
  {
    "year": 1999,
    "manufacturer_name": "Lexus",
    "model_name": "SC",
    "car_type": "Coupe"
  },
  {
    "year": 1999,
    "manufacturer_name": "MAZDA",
    "model_name": "Protege",
    "car_type": "Sedan"
  },
  {
    "year": 1999,
    "manufacturer_name": "Mercedes-Benz",
    "model_name": "E-Class",
    "car_type": "Sedan, Wagon"
  },
  {
    "year": 1999,
    "manufacturer_name": "Mercury",
    "model_name": "Cougar",
    "car_type": "Coupe"
  },
  {
    "year": 1999,
    "manufacturer_name": "Lincoln",
    "model_name": "Continental",
    "car_type": "Sedan"
  },
  {
    "year": 1999,
    "manufacturer_name": "MAZDA",
    "model_name": "Millenia",
    "car_type": "Sedan"
  },
  {
    "year": 1999,
    "manufacturer_name": "MAZDA",
    "model_name": "MX-5 Miata",
    "car_type": "Convertible"
  },
  {
    "year": 1999,
    "manufacturer_name": "Mercedes-Benz",
    "model_name": "C-Class",
    "car_type": "Sedan"
  },
  {
    "year": 1999,
    "manufacturer_name": "MAZDA",
    "model_name": "B-Series Cab Plus",
    "car_type": "Pickup"
  },
  {
    "year": 1999,
    "manufacturer_name": "Lincoln",
    "model_name": "Town Car",
    "car_type": "Sedan"
  },
  {
    "year": 1999,
    "manufacturer_name": "Lincoln",
    "model_name": "Navigator",
    "car_type": "SUV"
  },
  {
    "year": 1999,
    "manufacturer_name": "MAZDA",
    "model_name": "626",
    "car_type": "Sedan"
  },
  {
    "year": 1999,
    "manufacturer_name": "MAZDA",
    "model_name": "B-Series Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 1999,
    "manufacturer_name": "Mercedes-Benz",
    "model_name": "CL-Class",
    "car_type": "Coupe"
  },
  {
    "year": 1999,
    "manufacturer_name": "Oldsmobile",
    "model_name": "Cutlass",
    "car_type": "Sedan"
  },
  {
    "year": 1999,
    "manufacturer_name": "Mitsubishi",
    "model_name": "Galant",
    "car_type": "Sedan"
  },
  {
    "year": 1999,
    "manufacturer_name": "Mercury",
    "model_name": "Villager",
    "car_type": "Van/Minivan"
  },
  {
    "year": 1999,
    "manufacturer_name": "Mercury",
    "model_name": "Sable",
    "car_type": "Sedan, Wagon"
  },
  {
    "year": 1999,
    "manufacturer_name": "Mercedes-Benz",
    "model_name": "CLK-Class",
    "car_type": "Coupe, Convertible"
  },
  {
    "year": 1999,
    "manufacturer_name": "Mercury",
    "model_name": "Tracer",
    "car_type": "Sedan, Wagon"
  },
  {
    "year": 1999,
    "manufacturer_name": "Mitsubishi",
    "model_name": "Diamante",
    "car_type": "Sedan"
  },
  {
    "year": 1999,
    "manufacturer_name": "Nissan",
    "model_name": "Frontier King Cab",
    "car_type": "Pickup"
  },
  {
    "year": 1999,
    "manufacturer_name": "Mercedes-Benz",
    "model_name": "S-Class",
    "car_type": "Sedan"
  },
  {
    "year": 1999,
    "manufacturer_name": "Nissan",
    "model_name": "Altima",
    "car_type": "Sedan"
  },
  {
    "year": 1999,
    "manufacturer_name": "Mitsubishi",
    "model_name": "Montero Sport",
    "car_type": "SUV"
  },
  {
    "year": 1999,
    "manufacturer_name": "Mercedes-Benz",
    "model_name": "M-Class",
    "car_type": "SUV"
  },
  {
    "year": 1999,
    "manufacturer_name": "Mercedes-Benz",
    "model_name": "SL-Class",
    "car_type": "Convertible"
  },
  {
    "year": 1999,
    "manufacturer_name": "Nissan",
    "model_name": "Sentra",
    "car_type": "Sedan"
  },
  {
    "year": 1999,
    "manufacturer_name": "Mitsubishi",
    "model_name": "Mirage",
    "car_type": "Sedan, Coupe"
  },
  {
    "year": 1999,
    "manufacturer_name": "Mercedes-Benz",
    "model_name": "SLK-Class",
    "car_type": "Convertible"
  },
  {
    "year": 1999,
    "manufacturer_name": "Nissan",
    "model_name": "Pathfinder",
    "car_type": "SUV"
  },
  {
    "year": 1999,
    "manufacturer_name": "Mitsubishi",
    "model_name": "Montero",
    "car_type": "SUV"
  },
  {
    "year": 1999,
    "manufacturer_name": "Mitsubishi",
    "model_name": "Eclipse",
    "car_type": "Coupe, Convertible"
  },
  {
    "year": 1999,
    "manufacturer_name": "Mercury",
    "model_name": "Mystique",
    "car_type": "Sedan"
  },
  {
    "year": 1999,
    "manufacturer_name": "Mercury",
    "model_name": "Grand Marquis",
    "car_type": "Sedan"
  },
  {
    "year": 1999,
    "manufacturer_name": "Mercury",
    "model_name": "Mountaineer",
    "car_type": "SUV"
  },
  {
    "year": 1999,
    "manufacturer_name": "Mitsubishi",
    "model_name": "3000GT",
    "car_type": "Hatchback"
  },
  {
    "year": 1999,
    "manufacturer_name": "Nissan",
    "model_name": "Maxima",
    "car_type": "Sedan"
  },
  {
    "year": 1999,
    "manufacturer_name": "Nissan",
    "model_name": "Frontier Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 1999,
    "manufacturer_name": "Porsche",
    "model_name": "911",
    "car_type": "Coupe, Convertible"
  },
  {
    "year": 1999,
    "manufacturer_name": "Oldsmobile",
    "model_name": "Bravada",
    "car_type": "SUV"
  },
  {
    "year": 1999,
    "manufacturer_name": "Plymouth",
    "model_name": "Grand Voyager",
    "car_type": "Van/Minivan"
  },
  {
    "year": 1999,
    "manufacturer_name": "Nissan",
    "model_name": "Quest",
    "car_type": "Van/Minivan"
  },
  {
    "year": 1999,
    "manufacturer_name": "Oldsmobile",
    "model_name": "Silhouette",
    "car_type": "Van/Minivan"
  },
  {
    "year": 1999,
    "manufacturer_name": "Oldsmobile",
    "model_name": "Alero",
    "car_type": "Sedan, Coupe"
  },
  {
    "year": 1999,
    "manufacturer_name": "Oldsmobile",
    "model_name": "Intrigue",
    "car_type": "Sedan"
  },
  {
    "year": 1999,
    "manufacturer_name": "Pontiac",
    "model_name": "Firebird",
    "car_type": "Convertible, Coupe"
  },
  {
    "year": 1999,
    "manufacturer_name": "Oldsmobile",
    "model_name": "Aurora",
    "car_type": "Sedan"
  },
  {
    "year": 1999,
    "manufacturer_name": "Oldsmobile",
    "model_name": "LSS",
    "car_type": "Sedan"
  },
  {
    "year": 1999,
    "manufacturer_name": "Plymouth",
    "model_name": "Breeze",
    "car_type": "Sedan"
  },
  {
    "year": 1999,
    "manufacturer_name": "Oldsmobile",
    "model_name": "88",
    "car_type": "Sedan"
  },
  {
    "year": 1999,
    "manufacturer_name": "Subaru",
    "model_name": "Forester",
    "car_type": "SUV"
  },
  {
    "year": 1999,
    "manufacturer_name": "Plymouth",
    "model_name": "Voyager",
    "car_type": "Van/Minivan"
  },
  {
    "year": 1999,
    "manufacturer_name": "Suzuki",
    "model_name": "Swift",
    "car_type": "Hatchback"
  },
  {
    "year": 1999,
    "manufacturer_name": "Saab",
    "model_name": "5-Sep",
    "car_type": "Sedan, Wagon"
  },
  {
    "year": 1999,
    "manufacturer_name": "Pontiac",
    "model_name": "Grand Prix",
    "car_type": "Sedan, Coupe"
  },
  {
    "year": 1999,
    "manufacturer_name": "Pontiac",
    "model_name": "Sunfire",
    "car_type": "Coupe, Sedan, Convertible"
  },
  {
    "year": 1999,
    "manufacturer_name": "Porsche",
    "model_name": "Boxster",
    "car_type": "Convertible"
  },
  {
    "year": 1999,
    "manufacturer_name": "Pontiac",
    "model_name": "Grand Am",
    "car_type": "Sedan, Coupe"
  },
  {
    "year": 1999,
    "manufacturer_name": "Volkswagen",
    "model_name": "Jetta (New)",
    "car_type": "Sedan"
  },
  {
    "year": 1999,
    "manufacturer_name": "Toyota",
    "model_name": "4Runner",
    "car_type": "SUV"
  },
  {
    "year": 1999,
    "manufacturer_name": "Subaru",
    "model_name": "Impreza",
    "car_type": "Sedan, Coupe, Wagon"
  },
  {
    "year": 1999,
    "manufacturer_name": "Volvo",
    "model_name": "S80",
    "car_type": "Sedan"
  },
  {
    "year": 1999,
    "manufacturer_name": "Plymouth",
    "model_name": "Neon",
    "car_type": "Coupe, Sedan"
  },
  {
    "year": 1999,
    "manufacturer_name": "Saab",
    "model_name": "3-Sep",
    "car_type": "Hatchback, Convertible"
  },
  {
    "year": 1999,
    "manufacturer_name": "Toyota",
    "model_name": "Solara",
    "car_type": "Coupe"
  },
  {
    "year": 1999,
    "manufacturer_name": "Plymouth",
    "model_name": "Prowler",
    "car_type": "Convertible"
  },
  {
    "year": 1999,
    "manufacturer_name": "Pontiac",
    "model_name": "Bonneville",
    "car_type": "Sedan"
  },
  {
    "year": 1999,
    "manufacturer_name": "Volkswagen",
    "model_name": "Cabrio (New)",
    "car_type": "Convertible"
  },
  {
    "year": 1999,
    "manufacturer_name": "Suzuki",
    "model_name": "Esteem",
    "car_type": "Sedan, Wagon"
  },
  {
    "year": 1999,
    "manufacturer_name": "Toyota",
    "model_name": "Celica",
    "car_type": "Hatchback, Convertible"
  },
  {
    "year": 1999,
    "manufacturer_name": "Volkswagen",
    "model_name": "Cabrio",
    "car_type": "Convertible"
  },
  {
    "year": 1999,
    "manufacturer_name": "Suzuki",
    "model_name": "Grand Vitara",
    "car_type": "SUV"
  },
  {
    "year": 1999,
    "manufacturer_name": "Subaru",
    "model_name": "Legacy",
    "car_type": "Sedan, Wagon"
  },
  {
    "year": 1999,
    "manufacturer_name": "Toyota",
    "model_name": "Land Cruiser",
    "car_type": "SUV"
  },
  {
    "year": 1999,
    "manufacturer_name": "Pontiac",
    "model_name": "Montana",
    "car_type": "Van/Minivan"
  },
  {
    "year": 1999,
    "manufacturer_name": "Toyota",
    "model_name": "Avalon",
    "car_type": "Sedan"
  },
  {
    "year": 1999,
    "manufacturer_name": "Toyota",
    "model_name": "Camry",
    "car_type": "Sedan"
  },
  {
    "year": 1999,
    "manufacturer_name": "Saturn",
    "model_name": "S-Series",
    "car_type": "Coupe, Sedan, Wagon"
  },
  {
    "year": 1999,
    "manufacturer_name": "Suzuki",
    "model_name": "Vitara",
    "car_type": "SUV"
  },
  {
    "year": 1999,
    "manufacturer_name": "Volkswagen",
    "model_name": "Eurovan",
    "car_type": "Van/Minivan"
  },
  {
    "year": 1999,
    "manufacturer_name": "Toyota",
    "model_name": "Corolla",
    "car_type": "Sedan"
  },
  {
    "year": 1999,
    "manufacturer_name": "Toyota",
    "model_name": "RAV4",
    "car_type": "SUV"
  },
  {
    "year": 1999,
    "manufacturer_name": "Toyota",
    "model_name": "Sienna",
    "car_type": "Van/Minivan"
  },
  {
    "year": 1999,
    "manufacturer_name": "Toyota",
    "model_name": "Tacoma Xtracab",
    "car_type": "Pickup"
  },
  {
    "year": 1999,
    "manufacturer_name": "Volkswagen",
    "model_name": "Golf",
    "car_type": "Hatchback"
  },
  {
    "year": 1999,
    "manufacturer_name": "Volkswagen",
    "model_name": "Golf (New)",
    "car_type": "Hatchback"
  },
  {
    "year": 1999,
    "manufacturer_name": "Volkswagen",
    "model_name": "GTI (New)",
    "car_type": "Hatchback"
  },
  {
    "year": 1999,
    "manufacturer_name": "Toyota",
    "model_name": "Tacoma Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 1999,
    "manufacturer_name": "Volkswagen",
    "model_name": "Passat",
    "car_type": "Sedan, Wagon"
  },
  {
    "year": 1998,
    "manufacturer_name": "Acura",
    "model_name": "RL",
    "car_type": "Sedan"
  },
  {
    "year": 1999,
    "manufacturer_name": "Volkswagen",
    "model_name": "Jetta",
    "car_type": "Sedan"
  },
  {
    "year": 1999,
    "manufacturer_name": "Volvo",
    "model_name": "S70",
    "car_type": "Sedan"
  },
  {
    "year": 1998,
    "manufacturer_name": "Acura",
    "model_name": "Integra",
    "car_type": "Hatchback, Sedan"
  },
  {
    "year": 1999,
    "manufacturer_name": "Volvo",
    "model_name": "C70",
    "car_type": "Coupe, Convertible"
  },
  {
    "year": 1999,
    "manufacturer_name": "Volvo",
    "model_name": "V70",
    "car_type": "Wagon"
  },
  {
    "year": 1999,
    "manufacturer_name": "Volkswagen",
    "model_name": "New Beetle",
    "car_type": "Hatchback"
  },
  {
    "year": 1998,
    "manufacturer_name": "Acura",
    "model_name": "CL",
    "car_type": "Coupe"
  },
  {
    "year": 1998,
    "manufacturer_name": "Acura",
    "model_name": "NSX",
    "car_type": "Coupe, Convertible"
  },
  {
    "year": 1998,
    "manufacturer_name": "Acura",
    "model_name": "SLX",
    "car_type": "SUV"
  },
  {
    "year": 1998,
    "manufacturer_name": "BMW",
    "model_name": "M3",
    "car_type": "Convertible, Sedan, Coupe"
  },
  {
    "year": 1998,
    "manufacturer_name": "BMW",
    "model_name": "5 Series",
    "car_type": "Sedan"
  },
  {
    "year": 1998,
    "manufacturer_name": "Audi",
    "model_name": "A4",
    "car_type": "Sedan, Wagon"
  },
  {
    "year": 1998,
    "manufacturer_name": "Audi",
    "model_name": "A8",
    "car_type": "Sedan"
  },
  {
    "year": 1998,
    "manufacturer_name": "Audi",
    "model_name": "Cabriolet",
    "car_type": "Convertible"
  },
  {
    "year": 1998,
    "manufacturer_name": "Audi",
    "model_name": "A6",
    "car_type": "Sedan, Wagon"
  },
  {
    "year": 1998,
    "manufacturer_name": "BMW",
    "model_name": "3 Series",
    "car_type": "Coupe, Hatchback, Convertible, Sedan"
  },
  {
    "year": 1998,
    "manufacturer_name": "Acura",
    "model_name": "TL",
    "car_type": "Sedan"
  },
  {
    "year": 1998,
    "manufacturer_name": "Buick",
    "model_name": "Century",
    "car_type": "Sedan"
  },
  {
    "year": 1998,
    "manufacturer_name": "BMW",
    "model_name": "7 Series",
    "car_type": "Sedan"
  },
  {
    "year": 1998,
    "manufacturer_name": "Cadillac",
    "model_name": "Catera",
    "car_type": "Sedan"
  },
  {
    "year": 1998,
    "manufacturer_name": "BMW",
    "model_name": "Z3",
    "car_type": "Convertible"
  },
  {
    "year": 1998,
    "manufacturer_name": "Cadillac",
    "model_name": "Eldorado",
    "car_type": "Coupe"
  },
  {
    "year": 1998,
    "manufacturer_name": "Buick",
    "model_name": "Regal",
    "car_type": "Sedan"
  },
  {
    "year": 1998,
    "manufacturer_name": "Buick",
    "model_name": "Park Avenue",
    "car_type": "Sedan"
  },
  {
    "year": 1998,
    "manufacturer_name": "Cadillac",
    "model_name": "DeVille",
    "car_type": "Sedan"
  },
  {
    "year": 1998,
    "manufacturer_name": "Buick",
    "model_name": "LeSabre",
    "car_type": "Sedan"
  },
  {
    "year": 1998,
    "manufacturer_name": "Buick",
    "model_name": "Skylark",
    "car_type": "Sedan"
  },
  {
    "year": 1998,
    "manufacturer_name": "Buick",
    "model_name": "Riviera",
    "car_type": "Coupe"
  },
  {
    "year": 1998,
    "manufacturer_name": "Chevrolet",
    "model_name": "2500 HD Extended Cab",
    "car_type": "Pickup"
  },
  {
    "year": 1998,
    "manufacturer_name": "Chevrolet",
    "model_name": "3500 Extended Cab",
    "car_type": "Pickup"
  },
  {
    "year": 1998,
    "manufacturer_name": "Chevrolet",
    "model_name": "Blazer",
    "car_type": "SUV"
  },
  {
    "year": 1998,
    "manufacturer_name": "Chevrolet",
    "model_name": "Express 3500 Passenger",
    "car_type": "Van/Minivan"
  },
  {
    "year": 1998,
    "manufacturer_name": "Chevrolet",
    "model_name": "Camaro",
    "car_type": "Coupe, Convertible"
  },
  {
    "year": 1998,
    "manufacturer_name": "Chevrolet",
    "model_name": "2500 Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 1998,
    "manufacturer_name": "Chevrolet",
    "model_name": "Monte Carlo",
    "car_type": "Coupe"
  },
  {
    "year": 1998,
    "manufacturer_name": "Chevrolet",
    "model_name": "1500 Extended Cab",
    "car_type": "Pickup"
  },
  {
    "year": 1998,
    "manufacturer_name": "Chevrolet",
    "model_name": "G-Series 1500",
    "car_type": "Van/Minivan"
  },
  {
    "year": 1998,
    "manufacturer_name": "Chevrolet",
    "model_name": "3500 Crew Cab",
    "car_type": "Pickup"
  },
  {
    "year": 1998,
    "manufacturer_name": "Chevrolet",
    "model_name": "Astro Cargo",
    "car_type": "Van/Minivan"
  },
  {
    "year": 1998,
    "manufacturer_name": "Chevrolet",
    "model_name": "1500 Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 1998,
    "manufacturer_name": "Chevrolet",
    "model_name": "3500 Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 1998,
    "manufacturer_name": "Chevrolet",
    "model_name": "2500 Extended Cab",
    "car_type": "Pickup"
  },
  {
    "year": 1998,
    "manufacturer_name": "Cadillac",
    "model_name": "Seville",
    "car_type": "Sedan"
  },
  {
    "year": 1998,
    "manufacturer_name": "Chevrolet",
    "model_name": "S10 Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 1998,
    "manufacturer_name": "Chevrolet",
    "model_name": "Express 1500 Passenger",
    "car_type": "Van/Minivan"
  },
  {
    "year": 1998,
    "manufacturer_name": "Chevrolet",
    "model_name": "G-Series 3500",
    "car_type": "Van/Minivan"
  },
  {
    "year": 1998,
    "manufacturer_name": "Chevrolet",
    "model_name": "Express 2500 Passenger",
    "car_type": "Van/Minivan"
  },
  {
    "year": 1998,
    "manufacturer_name": "Chevrolet",
    "model_name": "Astro Passenger",
    "car_type": "Van/Minivan"
  },
  {
    "year": 1998,
    "manufacturer_name": "Chevrolet",
    "model_name": "Corvette",
    "car_type": "Hatchback, Convertible"
  },
  {
    "year": 1998,
    "manufacturer_name": "Chevrolet",
    "model_name": "Cavalier",
    "car_type": "Hatchback, Sedan, Convertible"
  },
  {
    "year": 1998,
    "manufacturer_name": "Chevrolet",
    "model_name": "G-Series 2500",
    "car_type": "Van/Minivan"
  },
  {
    "year": 1998,
    "manufacturer_name": "Chevrolet",
    "model_name": "Metro",
    "car_type": "Hatchback, Sedan"
  },
  {
    "year": 1998,
    "manufacturer_name": "Chevrolet",
    "model_name": "Suburban 2500",
    "car_type": "SUV"
  },
  {
    "year": 1998,
    "manufacturer_name": "Chevrolet",
    "model_name": "Malibu",
    "car_type": "Sedan"
  },
  {
    "year": 1998,
    "manufacturer_name": "Chevrolet",
    "model_name": "S10 Extended Cab",
    "car_type": "Pickup"
  },
  {
    "year": 1998,
    "manufacturer_name": "Chevrolet",
    "model_name": "Lumina",
    "car_type": "Sedan"
  },
  {
    "year": 1998,
    "manufacturer_name": "Chevrolet",
    "model_name": "Venture Cargo",
    "car_type": "Van/Minivan"
  },
  {
    "year": 1998,
    "manufacturer_name": "Chevrolet",
    "model_name": "Suburban 1500",
    "car_type": "SUV"
  },
  {
    "year": 1998,
    "manufacturer_name": "Dodge",
    "model_name": "Ram 2500 Club Cab",
    "car_type": "Pickup"
  },
  {
    "year": 1998,
    "manufacturer_name": "Chevrolet",
    "model_name": "Tracker",
    "car_type": "SUV"
  },
  {
    "year": 1998,
    "manufacturer_name": "Dodge",
    "model_name": "Caravan Passenger",
    "car_type": "Van/Minivan"
  },
  {
    "year": 1998,
    "manufacturer_name": "Dodge",
    "model_name": "Dakota Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 1998,
    "manufacturer_name": "Dodge",
    "model_name": "Grand Caravan Passenger",
    "car_type": "Van/Minivan"
  },
  {
    "year": 1998,
    "manufacturer_name": "Dodge",
    "model_name": "Avenger",
    "car_type": "Coupe"
  },
  {
    "year": 1998,
    "manufacturer_name": "Chrysler",
    "model_name": "Town & Country",
    "car_type": "Van/Minivan"
  },
  {
    "year": 1998,
    "manufacturer_name": "Chevrolet",
    "model_name": "Tahoe",
    "car_type": "SUV"
  },
  {
    "year": 1998,
    "manufacturer_name": "Chrysler",
    "model_name": "Cirrus",
    "car_type": "Sedan"
  },
  {
    "year": 1998,
    "manufacturer_name": "Dodge",
    "model_name": "Intrepid",
    "car_type": "Sedan"
  },
  {
    "year": 1998,
    "manufacturer_name": "Dodge",
    "model_name": "Durango",
    "car_type": "SUV"
  },
  {
    "year": 1998,
    "manufacturer_name": "Chrysler",
    "model_name": "Sebring",
    "car_type": "Convertible, Coupe"
  },
  {
    "year": 1998,
    "manufacturer_name": "Chevrolet",
    "model_name": "Venture Passenger",
    "car_type": "Van/Minivan"
  },
  {
    "year": 1998,
    "manufacturer_name": "Chrysler",
    "model_name": "Concorde",
    "car_type": "Sedan"
  },
  {
    "year": 1998,
    "manufacturer_name": "Chevrolet",
    "model_name": "Prizm",
    "car_type": "Sedan"
  },
  {
    "year": 1998,
    "manufacturer_name": "Dodge",
    "model_name": "Ram 1500 Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 1998,
    "manufacturer_name": "Dodge",
    "model_name": "Ram 1500 Quad Cab",
    "car_type": "Pickup"
  },
  {
    "year": 1998,
    "manufacturer_name": "Dodge",
    "model_name": "Ram 3500 Quad Cab",
    "car_type": "Pickup"
  },
  {
    "year": 1998,
    "manufacturer_name": "Dodge",
    "model_name": "Ram Wagon 3500",
    "car_type": "Van/Minivan"
  },
  {
    "year": 1998,
    "manufacturer_name": "Dodge",
    "model_name": "Dakota Club Cab",
    "car_type": "Pickup"
  },
  {
    "year": 1998,
    "manufacturer_name": "Dodge",
    "model_name": "Ram 3500 Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 1998,
    "manufacturer_name": "Dodge",
    "model_name": "Ram Van 1500",
    "car_type": "Van/Minivan"
  },
  {
    "year": 1998,
    "manufacturer_name": "Dodge",
    "model_name": "Ram 1500 Club Cab",
    "car_type": "Pickup"
  },
  {
    "year": 1998,
    "manufacturer_name": "Dodge",
    "model_name": "Neon",
    "car_type": "Sedan, Coupe"
  },
  {
    "year": 1998,
    "manufacturer_name": "Dodge",
    "model_name": "Ram 2500 Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 1998,
    "manufacturer_name": "Dodge",
    "model_name": "Ram 2500 Quad Cab",
    "car_type": "Pickup"
  },
  {
    "year": 1998,
    "manufacturer_name": "Dodge",
    "model_name": "Ram Wagon 1500",
    "car_type": "Van/Minivan"
  },
  {
    "year": 1998,
    "manufacturer_name": "Ford",
    "model_name": "Expedition",
    "car_type": "SUV"
  },
  {
    "year": 1998,
    "manufacturer_name": "Ford",
    "model_name": "Ranger Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 1998,
    "manufacturer_name": "Ford",
    "model_name": "F150 Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 1998,
    "manufacturer_name": "Ford",
    "model_name": "Contour",
    "car_type": "Sedan"
  },
  {
    "year": 1998,
    "manufacturer_name": "Ford",
    "model_name": "Club Wagon",
    "car_type": "Van/Minivan"
  },
  {
    "year": 1998,
    "manufacturer_name": "Ford",
    "model_name": "F250 Super Cab",
    "car_type": "Pickup"
  },
  {
    "year": 1998,
    "manufacturer_name": "Ford",
    "model_name": "F250 Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 1998,
    "manufacturer_name": "Ford",
    "model_name": "F150 Super Cab",
    "car_type": "Pickup"
  },
  {
    "year": 1998,
    "manufacturer_name": "Eagle",
    "model_name": "Talon",
    "car_type": "Hatchback"
  },
  {
    "year": 1998,
    "manufacturer_name": "Dodge",
    "model_name": "Ram Van 3500",
    "car_type": "Van/Minivan"
  },
  {
    "year": 1998,
    "manufacturer_name": "Ford",
    "model_name": "Econoline E150 Cargo",
    "car_type": "Van/Minivan"
  },
  {
    "year": 1998,
    "manufacturer_name": "Ford",
    "model_name": "Taurus",
    "car_type": "Sedan, Wagon"
  },
  {
    "year": 1998,
    "manufacturer_name": "Dodge",
    "model_name": "Stratus",
    "car_type": "Sedan"
  },
  {
    "year": 1998,
    "manufacturer_name": "Ford",
    "model_name": "Mustang",
    "car_type": "Coupe, Convertible"
  },
  {
    "year": 1998,
    "manufacturer_name": "Dodge",
    "model_name": "Ram Wagon 2500",
    "car_type": "Van/Minivan"
  },
  {
    "year": 1998,
    "manufacturer_name": "Ford",
    "model_name": "Escort",
    "car_type": "Sedan, Coupe, Wagon"
  },
  {
    "year": 1998,
    "manufacturer_name": "Ford",
    "model_name": "Explorer",
    "car_type": "SUV"
  },
  {
    "year": 1998,
    "manufacturer_name": "Dodge",
    "model_name": "Ram Van 2500",
    "car_type": "Van/Minivan"
  },
  {
    "year": 1998,
    "manufacturer_name": "Ford",
    "model_name": "Econoline E350 Cargo",
    "car_type": "Van/Minivan"
  },
  {
    "year": 1998,
    "manufacturer_name": "Ford",
    "model_name": "Econoline E250 Cargo",
    "car_type": "Van/Minivan"
  },
  {
    "year": 1998,
    "manufacturer_name": "Ford",
    "model_name": "Crown Victoria",
    "car_type": "Sedan"
  },
  {
    "year": 1998,
    "manufacturer_name": "Ford",
    "model_name": "Ranger Super Cab",
    "car_type": "Pickup"
  },
  {
    "year": 1998,
    "manufacturer_name": "Dodge",
    "model_name": "Viper",
    "car_type": "Convertible, Coupe"
  },
  {
    "year": 1998,
    "manufacturer_name": "Ford",
    "model_name": "Windstar Passenger",
    "car_type": "Van/Minivan"
  },
  {
    "year": 1998,
    "manufacturer_name": "GMC",
    "model_name": "2500 Club Coupe",
    "car_type": "Pickup"
  },
  {
    "year": 1998,
    "manufacturer_name": "GMC",
    "model_name": "2500 Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 1998,
    "manufacturer_name": "GMC",
    "model_name": "3500 Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 1998,
    "manufacturer_name": "GMC",
    "model_name": "1500 Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 1998,
    "manufacturer_name": "GMC",
    "model_name": "Safari Cargo",
    "car_type": "Van/Minivan"
  },
  {
    "year": 1998,
    "manufacturer_name": "GMC",
    "model_name": "3500 Crew Cab",
    "car_type": "Pickup"
  },
  {
    "year": 1998,
    "manufacturer_name": "GMC",
    "model_name": "3500 Club Coupe",
    "car_type": "Pickup"
  },
  {
    "year": 1998,
    "manufacturer_name": "GMC",
    "model_name": "1500 Club Coupe",
    "car_type": "Pickup"
  },
  {
    "year": 1998,
    "manufacturer_name": "Ford",
    "model_name": "Windstar Cargo",
    "car_type": "Van/Minivan"
  },
  {
    "year": 1998,
    "manufacturer_name": "GMC",
    "model_name": "Safari Passenger",
    "car_type": "Van/Minivan"
  },
  {
    "year": 1998,
    "manufacturer_name": "GMC",
    "model_name": "Jimmy",
    "car_type": "SUV"
  },
  {
    "year": 1998,
    "manufacturer_name": "GMC",
    "model_name": "Sonoma Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 1998,
    "manufacturer_name": "INFINITI",
    "model_name": "I",
    "car_type": "Sedan"
  },
  {
    "year": 1998,
    "manufacturer_name": "Isuzu",
    "model_name": "Rodeo",
    "car_type": "SUV"
  },
  {
    "year": 1998,
    "manufacturer_name": "GMC",
    "model_name": "Sonoma Club Coupe Cab",
    "car_type": "Pickup"
  },
  {
    "year": 1998,
    "manufacturer_name": "Isuzu",
    "model_name": "Trooper",
    "car_type": "SUV"
  },
  {
    "year": 1998,
    "manufacturer_name": "GMC",
    "model_name": "Savana 2500 Passenger",
    "car_type": "Van/Minivan"
  },
  {
    "year": 1998,
    "manufacturer_name": "GMC",
    "model_name": "Savana 3500 Cargo",
    "car_type": "Van/Minivan"
  },
  {
    "year": 1998,
    "manufacturer_name": "GMC",
    "model_name": "Yukon",
    "car_type": "SUV"
  },
  {
    "year": 1998,
    "manufacturer_name": "Honda",
    "model_name": "Civic",
    "car_type": "Coupe, Hatchback, Sedan"
  },
  {
    "year": 1998,
    "manufacturer_name": "Honda",
    "model_name": "Prelude",
    "car_type": "Coupe"
  },
  {
    "year": 1998,
    "manufacturer_name": "Honda",
    "model_name": "Accord",
    "car_type": "Sedan, Coupe"
  },
  {
    "year": 1998,
    "manufacturer_name": "GMC",
    "model_name": "2500 HD Club Coupe",
    "car_type": "Pickup"
  },
  {
    "year": 1998,
    "manufacturer_name": "GMC",
    "model_name": "Savana 2500 Cargo",
    "car_type": "Van/Minivan"
  },
  {
    "year": 1998,
    "manufacturer_name": "Honda",
    "model_name": "Odyssey",
    "car_type": "Van/Minivan"
  },
  {
    "year": 1998,
    "manufacturer_name": "Hyundai",
    "model_name": "Elantra",
    "car_type": "Sedan, Wagon"
  },
  {
    "year": 1998,
    "manufacturer_name": "Jeep",
    "model_name": "Grand Cherokee",
    "car_type": "SUV"
  },
  {
    "year": 1998,
    "manufacturer_name": "GMC",
    "model_name": "Savana 1500 Cargo",
    "car_type": "Van/Minivan"
  },
  {
    "year": 1998,
    "manufacturer_name": "GMC",
    "model_name": "Savana 1500 Passenger",
    "car_type": "Van/Minivan"
  },
  {
    "year": 1998,
    "manufacturer_name": "Isuzu",
    "model_name": "Amigo",
    "car_type": "SUV"
  },
  {
    "year": 1998,
    "manufacturer_name": "GMC",
    "model_name": "Suburban 1500",
    "car_type": "SUV"
  },
  {
    "year": 1998,
    "manufacturer_name": "GMC",
    "model_name": "Suburban 2500",
    "car_type": "SUV"
  },
  {
    "year": 1998,
    "manufacturer_name": "Jeep",
    "model_name": "Cherokee",
    "car_type": "SUV"
  },
  {
    "year": 1998,
    "manufacturer_name": "Isuzu",
    "model_name": "Oasis",
    "car_type": "Van/Minivan"
  },
  {
    "year": 1998,
    "manufacturer_name": "GMC",
    "model_name": "Envoy",
    "car_type": "SUV"
  },
  {
    "year": 1998,
    "manufacturer_name": "Hyundai",
    "model_name": "Sonata",
    "car_type": "Sedan"
  },
  {
    "year": 1998,
    "manufacturer_name": "GMC",
    "model_name": "Savana 3500 Passenger",
    "car_type": "Van/Minivan"
  },
  {
    "year": 1998,
    "manufacturer_name": "Hyundai",
    "model_name": "Accent",
    "car_type": "Hatchback, Sedan"
  },
  {
    "year": 1998,
    "manufacturer_name": "HUMMER",
    "model_name": "H1",
    "car_type": "SUV, Wagon"
  },
  {
    "year": 1998,
    "manufacturer_name": "Honda",
    "model_name": "Passport",
    "car_type": "SUV"
  },
  {
    "year": 1998,
    "manufacturer_name": "Hyundai",
    "model_name": "Tiburon",
    "car_type": "Hatchback"
  },
  {
    "year": 1998,
    "manufacturer_name": "Isuzu",
    "model_name": "Hombre Spacecab",
    "car_type": "Pickup"
  },
  {
    "year": 1998,
    "manufacturer_name": "Honda",
    "model_name": "CR-V",
    "car_type": "SUV"
  },
  {
    "year": 1998,
    "manufacturer_name": "INFINITI",
    "model_name": "Q",
    "car_type": "Sedan"
  },
  {
    "year": 1998,
    "manufacturer_name": "Land Rover",
    "model_name": "Discovery",
    "car_type": "SUV"
  },
  {
    "year": 1998,
    "manufacturer_name": "INFINITI",
    "model_name": "QX",
    "car_type": "SUV"
  },
  {
    "year": 1998,
    "manufacturer_name": "Isuzu",
    "model_name": "Hombre Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 1998,
    "manufacturer_name": "Land Rover",
    "model_name": "Range Rover",
    "car_type": "SUV"
  },
  {
    "year": 1998,
    "manufacturer_name": "Jaguar",
    "model_name": "XK",
    "car_type": "Coupe, Convertible"
  },
  {
    "year": 1998,
    "manufacturer_name": "Lexus",
    "model_name": "LX",
    "car_type": "SUV"
  },
  {
    "year": 1998,
    "manufacturer_name": "Jeep",
    "model_name": "Wrangler",
    "car_type": "SUV"
  },
  {
    "year": 1998,
    "manufacturer_name": "MAZDA",
    "model_name": "B-Series Cab Plus",
    "car_type": "Pickup"
  },
  {
    "year": 1998,
    "manufacturer_name": "Mitsubishi",
    "model_name": "3000GT",
    "car_type": "Hatchback"
  },
  {
    "year": 1998,
    "manufacturer_name": "Mercedes-Benz",
    "model_name": "C-Class",
    "car_type": "Sedan"
  },
  {
    "year": 1998,
    "manufacturer_name": "Mercury",
    "model_name": "Villager",
    "car_type": "Van/Minivan"
  },
  {
    "year": 1998,
    "manufacturer_name": "Kia",
    "model_name": "Sephia",
    "car_type": "Sedan"
  },
  {
    "year": 1998,
    "manufacturer_name": "MAZDA",
    "model_name": "626",
    "car_type": "Sedan"
  },
  {
    "year": 1998,
    "manufacturer_name": "Lexus",
    "model_name": "LS",
    "car_type": "Sedan"
  },
  {
    "year": 1998,
    "manufacturer_name": "Lexus",
    "model_name": "ES",
    "car_type": "Sedan"
  },
  {
    "year": 1998,
    "manufacturer_name": "Jaguar",
    "model_name": "XJ",
    "car_type": "Sedan"
  },
  {
    "year": 1998,
    "manufacturer_name": "Kia",
    "model_name": "Sportage",
    "car_type": "SUV"
  },
  {
    "year": 1998,
    "manufacturer_name": "MAZDA",
    "model_name": "Millenia",
    "car_type": "Sedan"
  },
  {
    "year": 1998,
    "manufacturer_name": "Lexus",
    "model_name": "SC",
    "car_type": "Coupe"
  },
  {
    "year": 1998,
    "manufacturer_name": "Mercedes-Benz",
    "model_name": "E-Class",
    "car_type": "Sedan, Wagon"
  },
  {
    "year": 1998,
    "manufacturer_name": "Mercury",
    "model_name": "Tracer",
    "car_type": "Sedan, Wagon"
  },
  {
    "year": 1998,
    "manufacturer_name": "Lexus",
    "model_name": "GS",
    "car_type": "Sedan"
  },
  {
    "year": 1998,
    "manufacturer_name": "Mercury",
    "model_name": "Mountaineer",
    "car_type": "SUV"
  },
  {
    "year": 1998,
    "manufacturer_name": "Mercury",
    "model_name": "Grand Marquis",
    "car_type": "Sedan"
  },
  {
    "year": 1998,
    "manufacturer_name": "Mitsubishi",
    "model_name": "Galant",
    "car_type": "Sedan"
  },
  {
    "year": 1998,
    "manufacturer_name": "Lincoln",
    "model_name": "Continental",
    "car_type": "Sedan"
  },
  {
    "year": 1998,
    "manufacturer_name": "Lincoln",
    "model_name": "Town Car",
    "car_type": "Sedan"
  },
  {
    "year": 1998,
    "manufacturer_name": "Lincoln",
    "model_name": "Navigator",
    "car_type": "SUV"
  },
  {
    "year": 1998,
    "manufacturer_name": "Mercury",
    "model_name": "Mystique",
    "car_type": "Sedan"
  },
  {
    "year": 1998,
    "manufacturer_name": "Mercedes-Benz",
    "model_name": "SL-Class",
    "car_type": "Convertible"
  },
  {
    "year": 1998,
    "manufacturer_name": "MAZDA",
    "model_name": "B-Series Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 1998,
    "manufacturer_name": "Mitsubishi",
    "model_name": "Mirage",
    "car_type": "Sedan, Coupe"
  },
  {
    "year": 1998,
    "manufacturer_name": "MAZDA",
    "model_name": "MPV",
    "car_type": "Van/Minivan"
  },
  {
    "year": 1998,
    "manufacturer_name": "Mercedes-Benz",
    "model_name": "S-Class",
    "car_type": "Sedan"
  },
  {
    "year": 1998,
    "manufacturer_name": "Lincoln",
    "model_name": "Mark VIII",
    "car_type": "Coupe"
  },
  {
    "year": 1998,
    "manufacturer_name": "Mercedes-Benz",
    "model_name": "SLK-Class",
    "car_type": "Convertible"
  },
  {
    "year": 1998,
    "manufacturer_name": "MAZDA",
    "model_name": "Protege",
    "car_type": "Sedan"
  },
  {
    "year": 1998,
    "manufacturer_name": "Mitsubishi",
    "model_name": "Diamante",
    "car_type": "Sedan"
  },
  {
    "year": 1998,
    "manufacturer_name": "Mercedes-Benz",
    "model_name": "M-Class",
    "car_type": "SUV"
  },
  {
    "year": 1998,
    "manufacturer_name": "Mercedes-Benz",
    "model_name": "CLK-Class",
    "car_type": "Coupe"
  },
  {
    "year": 1998,
    "manufacturer_name": "Mercedes-Benz",
    "model_name": "CL-Class",
    "car_type": "Coupe"
  },
  {
    "year": 1998,
    "manufacturer_name": "Nissan",
    "model_name": "Altima",
    "car_type": "Sedan"
  },
  {
    "year": 1998,
    "manufacturer_name": "Nissan",
    "model_name": "200SX",
    "car_type": "Coupe"
  },
  {
    "year": 1998,
    "manufacturer_name": "Nissan",
    "model_name": "Frontier King Cab",
    "car_type": "Pickup"
  },
  {
    "year": 1998,
    "manufacturer_name": "Nissan",
    "model_name": "Quest",
    "car_type": "Van/Minivan"
  },
  {
    "year": 1998,
    "manufacturer_name": "Nissan",
    "model_name": "240SX",
    "car_type": "Coupe"
  },
  {
    "year": 1998,
    "manufacturer_name": "Nissan",
    "model_name": "Maxima",
    "car_type": "Sedan"
  },
  {
    "year": 1998,
    "manufacturer_name": "Oldsmobile",
    "model_name": "88",
    "car_type": "Sedan"
  },
  {
    "year": 1998,
    "manufacturer_name": "Mitsubishi",
    "model_name": "Montero",
    "car_type": "SUV"
  },
  {
    "year": 1998,
    "manufacturer_name": "Mercury",
    "model_name": "Sable",
    "car_type": "Wagon, Sedan"
  },
  {
    "year": 1998,
    "manufacturer_name": "Mitsubishi",
    "model_name": "Eclipse",
    "car_type": "Coupe, Convertible"
  },
  {
    "year": 1998,
    "manufacturer_name": "Nissan",
    "model_name": "Frontier Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 1998,
    "manufacturer_name": "Mitsubishi",
    "model_name": "Montero Sport",
    "car_type": "SUV"
  },
  {
    "year": 1998,
    "manufacturer_name": "Nissan",
    "model_name": "Pathfinder",
    "car_type": "SUV"
  },
  {
    "year": 1998,
    "manufacturer_name": "Nissan",
    "model_name": "Sentra",
    "car_type": "Sedan"
  },
  {
    "year": 1998,
    "manufacturer_name": "Oldsmobile",
    "model_name": "Achieva",
    "car_type": "Sedan"
  },
  {
    "year": 1998,
    "manufacturer_name": "Subaru",
    "model_name": "Forester",
    "car_type": "SUV"
  },
  {
    "year": 1998,
    "manufacturer_name": "Porsche",
    "model_name": "Boxster",
    "car_type": "Convertible"
  },
  {
    "year": 1998,
    "manufacturer_name": "Plymouth",
    "model_name": "Breeze",
    "car_type": "Sedan"
  },
  {
    "year": 1998,
    "manufacturer_name": "Oldsmobile",
    "model_name": "Bravada",
    "car_type": "SUV"
  },
  {
    "year": 1998,
    "manufacturer_name": "Oldsmobile",
    "model_name": "Cutlass",
    "car_type": "Sedan"
  },
  {
    "year": 1998,
    "manufacturer_name": "Pontiac",
    "model_name": "Bonneville",
    "car_type": "Sedan"
  },
  {
    "year": 1998,
    "manufacturer_name": "Oldsmobile",
    "model_name": "LSS",
    "car_type": "Sedan"
  },
  {
    "year": 1998,
    "manufacturer_name": "Oldsmobile",
    "model_name": "Regency",
    "car_type": "Sedan"
  },
  {
    "year": 1998,
    "manufacturer_name": "Pontiac",
    "model_name": "Firebird",
    "car_type": "Coupe, Convertible"
  },
  {
    "year": 1998,
    "manufacturer_name": "Plymouth",
    "model_name": "Voyager",
    "car_type": "Van/Minivan"
  },
  {
    "year": 1998,
    "manufacturer_name": "Suzuki",
    "model_name": "Sidekick",
    "car_type": "SUV"
  },
  {
    "year": 1998,
    "manufacturer_name": "Pontiac",
    "model_name": "Grand Am",
    "car_type": "Sedan, Coupe"
  },
  {
    "year": 1998,
    "manufacturer_name": "Pontiac",
    "model_name": "Sunfire",
    "car_type": "Convertible, Sedan, Coupe"
  },
  {
    "year": 1998,
    "manufacturer_name": "Porsche",
    "model_name": "911",
    "car_type": "Coupe, Convertible"
  },
  {
    "year": 1998,
    "manufacturer_name": "Oldsmobile",
    "model_name": "Silhouette",
    "car_type": "Van/Minivan"
  },
  {
    "year": 1998,
    "manufacturer_name": "Oldsmobile",
    "model_name": "Aurora",
    "car_type": "Sedan"
  },
  {
    "year": 1998,
    "manufacturer_name": "Pontiac",
    "model_name": "Trans Sport",
    "car_type": "Van/Minivan"
  },
  {
    "year": 1998,
    "manufacturer_name": "Pontiac",
    "model_name": "Grand Prix",
    "car_type": "Coupe, Sedan"
  },
  {
    "year": 1998,
    "manufacturer_name": "Plymouth",
    "model_name": "Neon",
    "car_type": "Coupe, Sedan"
  },
  {
    "year": 1998,
    "manufacturer_name": "Oldsmobile",
    "model_name": "Intrigue",
    "car_type": "Sedan"
  },
  {
    "year": 1998,
    "manufacturer_name": "Plymouth",
    "model_name": "Grand Voyager",
    "car_type": "Van/Minivan"
  },
  {
    "year": 1998,
    "manufacturer_name": "Saturn",
    "model_name": "S-Series",
    "car_type": "Coupe, Sedan, Wagon"
  },
  {
    "year": 1998,
    "manufacturer_name": "Subaru",
    "model_name": "Impreza",
    "car_type": "Sedan, Wagon, Coupe"
  },
  {
    "year": 1998,
    "manufacturer_name": "Toyota",
    "model_name": "Supra",
    "car_type": "Hatchback"
  },
  {
    "year": 1998,
    "manufacturer_name": "Saab",
    "model_name": "900",
    "car_type": "Hatchback, Convertible"
  },
  {
    "year": 1998,
    "manufacturer_name": "Toyota",
    "model_name": "Camry",
    "car_type": "Sedan"
  },
  {
    "year": 1998,
    "manufacturer_name": "Toyota",
    "model_name": "Celica",
    "car_type": "Coupe, Hatchback, Convertible"
  },
  {
    "year": 1998,
    "manufacturer_name": "Toyota",
    "model_name": "T100 Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 1998,
    "manufacturer_name": "Saab",
    "model_name": "9000",
    "car_type": "Hatchback"
  },
  {
    "year": 1998,
    "manufacturer_name": "Toyota",
    "model_name": "Tacoma Xtracab",
    "car_type": "Pickup"
  },
  {
    "year": 1998,
    "manufacturer_name": "Toyota",
    "model_name": "4Runner",
    "car_type": "SUV"
  },
  {
    "year": 1998,
    "manufacturer_name": "Suzuki",
    "model_name": "Esteem",
    "car_type": "Sedan, Wagon"
  },
  {
    "year": 1998,
    "manufacturer_name": "Suzuki",
    "model_name": "X-90",
    "car_type": "SUV"
  },
  {
    "year": 1998,
    "manufacturer_name": "Toyota",
    "model_name": "RAV4",
    "car_type": "SUV"
  },
  {
    "year": 1998,
    "manufacturer_name": "Toyota",
    "model_name": "Corolla",
    "car_type": "Sedan"
  },
  {
    "year": 1998,
    "manufacturer_name": "Toyota",
    "model_name": "Sienna",
    "car_type": "Van/Minivan"
  },
  {
    "year": 1998,
    "manufacturer_name": "Suzuki",
    "model_name": "Swift",
    "car_type": "Hatchback"
  },
  {
    "year": 1998,
    "manufacturer_name": "Subaru",
    "model_name": "Legacy",
    "car_type": "Sedan, Wagon"
  },
  {
    "year": 1998,
    "manufacturer_name": "Toyota",
    "model_name": "Avalon",
    "car_type": "Sedan"
  },
  {
    "year": 1998,
    "manufacturer_name": "Toyota",
    "model_name": "T100 Xtracab",
    "car_type": "Pickup"
  },
  {
    "year": 1998,
    "manufacturer_name": "Volkswagen",
    "model_name": "Golf",
    "car_type": "Hatchback"
  },
  {
    "year": 1998,
    "manufacturer_name": "Volvo",
    "model_name": "S70",
    "car_type": "Sedan"
  },
  {
    "year": 1998,
    "manufacturer_name": "Volkswagen",
    "model_name": "Cabrio",
    "car_type": "Convertible"
  },
  {
    "year": 1998,
    "manufacturer_name": "Volvo",
    "model_name": "C70",
    "car_type": "Coupe, Convertible"
  },
  {
    "year": 1998,
    "manufacturer_name": "Toyota",
    "model_name": "Tacoma Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 1997,
    "manufacturer_name": "Acura",
    "model_name": "RL",
    "car_type": "Sedan"
  },
  {
    "year": 1998,
    "manufacturer_name": "Toyota",
    "model_name": "Land Cruiser",
    "car_type": "SUV"
  },
  {
    "year": 1998,
    "manufacturer_name": "Volkswagen",
    "model_name": "New Beetle",
    "car_type": "Hatchback"
  },
  {
    "year": 1997,
    "manufacturer_name": "Acura",
    "model_name": "Integra",
    "car_type": "Coupe, Sedan"
  },
  {
    "year": 1997,
    "manufacturer_name": "Acura",
    "model_name": "TL",
    "car_type": "Sedan"
  },
  {
    "year": 1997,
    "manufacturer_name": "BMW",
    "model_name": "3 Series",
    "car_type": "Coupe, Hatchback, Convertible, Sedan"
  },
  {
    "year": 1998,
    "manufacturer_name": "Toyota",
    "model_name": "Tercel",
    "car_type": "Sedan"
  },
  {
    "year": 1997,
    "manufacturer_name": "Buick",
    "model_name": "Park Avenue",
    "car_type": "Sedan"
  },
  {
    "year": 1997,
    "manufacturer_name": "Acura",
    "model_name": "SLX",
    "car_type": "SUV"
  },
  {
    "year": 1998,
    "manufacturer_name": "Volvo",
    "model_name": "V70",
    "car_type": "Wagon"
  },
  {
    "year": 1998,
    "manufacturer_name": "Volkswagen",
    "model_name": "Passat",
    "car_type": "Sedan, Wagon"
  },
  {
    "year": 1998,
    "manufacturer_name": "Volkswagen",
    "model_name": "Jetta",
    "car_type": "Sedan"
  },
  {
    "year": 1997,
    "manufacturer_name": "Audi",
    "model_name": "A6",
    "car_type": "Wagon, Sedan"
  },
  {
    "year": 1998,
    "manufacturer_name": "Volvo",
    "model_name": "V90",
    "car_type": "Wagon"
  },
  {
    "year": 1998,
    "manufacturer_name": "Volvo",
    "model_name": "S90",
    "car_type": "Sedan"
  },
  {
    "year": 1997,
    "manufacturer_name": "BMW",
    "model_name": "M3",
    "car_type": "Sedan, Coupe"
  },
  {
    "year": 1997,
    "manufacturer_name": "Audi",
    "model_name": "Cabriolet",
    "car_type": "Convertible"
  },
  {
    "year": 1997,
    "manufacturer_name": "Acura",
    "model_name": "NSX",
    "car_type": "Coupe, Convertible"
  },
  {
    "year": 1997,
    "manufacturer_name": "BMW",
    "model_name": "8 Series",
    "car_type": "Coupe"
  },
  {
    "year": 1997,
    "manufacturer_name": "Acura",
    "model_name": "CL",
    "car_type": "Coupe"
  },
  {
    "year": 1997,
    "manufacturer_name": "BMW",
    "model_name": "Z3",
    "car_type": "Convertible"
  },
  {
    "year": 1997,
    "manufacturer_name": "BMW",
    "model_name": "7 Series",
    "car_type": "Sedan"
  },
  {
    "year": 1997,
    "manufacturer_name": "Audi",
    "model_name": "A4",
    "car_type": "Sedan"
  },
  {
    "year": 1997,
    "manufacturer_name": "Audi",
    "model_name": "A8",
    "car_type": "Sedan"
  },
  {
    "year": 1997,
    "manufacturer_name": "Buick",
    "model_name": "Regal",
    "car_type": "Sedan"
  },
  {
    "year": 1997,
    "manufacturer_name": "Cadillac",
    "model_name": "DeVille",
    "car_type": "Sedan"
  },
  {
    "year": 1997,
    "manufacturer_name": "BMW",
    "model_name": "5 Series",
    "car_type": "Sedan"
  },
  {
    "year": 1997,
    "manufacturer_name": "Buick",
    "model_name": "Riviera",
    "car_type": "Coupe"
  },
  {
    "year": 1997,
    "manufacturer_name": "Buick",
    "model_name": "LeSabre",
    "car_type": "Sedan"
  },
  {
    "year": 1997,
    "manufacturer_name": "Chevrolet",
    "model_name": "2500 Extended Cab",
    "car_type": "Pickup"
  },
  {
    "year": 1997,
    "manufacturer_name": "Buick",
    "model_name": "Century",
    "car_type": "Sedan"
  },
  {
    "year": 1997,
    "manufacturer_name": "Chevrolet",
    "model_name": "1500 Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 1997,
    "manufacturer_name": "Chevrolet",
    "model_name": "2500 Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 1997,
    "manufacturer_name": "Chevrolet",
    "model_name": "2500 HD Extended Cab",
    "car_type": "Pickup"
  },
  {
    "year": 1997,
    "manufacturer_name": "Chevrolet",
    "model_name": "3500 Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 1997,
    "manufacturer_name": "Cadillac",
    "model_name": "Seville",
    "car_type": "Sedan"
  },
  {
    "year": 1997,
    "manufacturer_name": "Cadillac",
    "model_name": "Eldorado",
    "car_type": "Coupe"
  },
  {
    "year": 1997,
    "manufacturer_name": "Buick",
    "model_name": "Skylark",
    "car_type": "Sedan, Coupe"
  },
  {
    "year": 1997,
    "manufacturer_name": "Chevrolet",
    "model_name": "1500 Extended Cab",
    "car_type": "Pickup"
  },
  {
    "year": 1997,
    "manufacturer_name": "Cadillac",
    "model_name": "Catera",
    "car_type": "Sedan"
  },
  {
    "year": 1997,
    "manufacturer_name": "Chevrolet",
    "model_name": "Astro Cargo",
    "car_type": "Van/Minivan"
  },
  {
    "year": 1997,
    "manufacturer_name": "Chevrolet",
    "model_name": "Cavalier",
    "car_type": "Coupe, Convertible, Sedan"
  },
  {
    "year": 1997,
    "manufacturer_name": "Chevrolet",
    "model_name": "Astro Passenger",
    "car_type": "Van/Minivan"
  },
  {
    "year": 1997,
    "manufacturer_name": "Chevrolet",
    "model_name": "3500 Extended Cab",
    "car_type": "Pickup"
  },
  {
    "year": 1997,
    "manufacturer_name": "Chevrolet",
    "model_name": "G-Series 1500",
    "car_type": "Van/Minivan"
  },
  {
    "year": 1997,
    "manufacturer_name": "Chevrolet",
    "model_name": "Corvette",
    "car_type": "Hatchback"
  },
  {
    "year": 1997,
    "manufacturer_name": "Chevrolet",
    "model_name": "Express 2500 Passenger",
    "car_type": "Van/Minivan"
  },
  {
    "year": 1997,
    "manufacturer_name": "Chevrolet",
    "model_name": "Express 1500 Passenger",
    "car_type": "Van/Minivan"
  },
  {
    "year": 1997,
    "manufacturer_name": "Chevrolet",
    "model_name": "G-Series 2500",
    "car_type": "Van/Minivan"
  },
  {
    "year": 1997,
    "manufacturer_name": "Chevrolet",
    "model_name": "Blazer",
    "car_type": "SUV"
  },
  {
    "year": 1997,
    "manufacturer_name": "Chevrolet",
    "model_name": "Camaro",
    "car_type": "Convertible, Coupe"
  },
  {
    "year": 1997,
    "manufacturer_name": "Chevrolet",
    "model_name": "3500 Crew Cab",
    "car_type": "Pickup"
  },
  {
    "year": 1997,
    "manufacturer_name": "Chevrolet",
    "model_name": "G-Series 3500",
    "car_type": "Van/Minivan"
  },
  {
    "year": 1997,
    "manufacturer_name": "Chevrolet",
    "model_name": "Express 3500 Passenger",
    "car_type": "Van/Minivan"
  },
  {
    "year": 1997,
    "manufacturer_name": "Chevrolet",
    "model_name": "Malibu",
    "car_type": "Sedan"
  },
  {
    "year": 1997,
    "manufacturer_name": "Chevrolet",
    "model_name": "Monte Carlo",
    "car_type": "Coupe"
  },
  {
    "year": 1997,
    "manufacturer_name": "Chevrolet",
    "model_name": "Lumina",
    "car_type": "Sedan"
  },
  {
    "year": 1997,
    "manufacturer_name": "Chrysler",
    "model_name": "Cirrus",
    "car_type": "Sedan"
  },
  {
    "year": 1997,
    "manufacturer_name": "Chevrolet",
    "model_name": "Suburban 2500",
    "car_type": "SUV"
  },
  {
    "year": 1997,
    "manufacturer_name": "Chevrolet",
    "model_name": "S10 Extended Cab",
    "car_type": "Pickup"
  },
  {
    "year": 1997,
    "manufacturer_name": "Chevrolet",
    "model_name": "Tahoe",
    "car_type": "SUV"
  },
  {
    "year": 1997,
    "manufacturer_name": "Chrysler",
    "model_name": "LHS",
    "car_type": "Sedan"
  },
  {
    "year": 1997,
    "manufacturer_name": "Chevrolet",
    "model_name": "S10 Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 1997,
    "manufacturer_name": "Chevrolet",
    "model_name": "Venture Passenger",
    "car_type": "Van/Minivan"
  },
  {
    "year": 1997,
    "manufacturer_name": "Chevrolet",
    "model_name": "Suburban 1500",
    "car_type": "SUV"
  },
  {
    "year": 1997,
    "manufacturer_name": "Chrysler",
    "model_name": "Sebring",
    "car_type": "Coupe, Convertible"
  },
  {
    "year": 1997,
    "manufacturer_name": "Chrysler",
    "model_name": "Town & Country",
    "car_type": "Van/Minivan"
  },
  {
    "year": 1997,
    "manufacturer_name": "Ford",
    "model_name": "Aerostar Passenger",
    "car_type": "Van/Minivan"
  },
  {
    "year": 1997,
    "manufacturer_name": "Dodge",
    "model_name": "Ram 2500 Club Cab",
    "car_type": "Pickup"
  },
  {
    "year": 1997,
    "manufacturer_name": "Dodge",
    "model_name": "Dakota Club Cab",
    "car_type": "Pickup"
  },
  {
    "year": 1997,
    "manufacturer_name": "Dodge",
    "model_name": "Ram Wagon 1500",
    "car_type": "Van/Minivan"
  },
  {
    "year": 1997,
    "manufacturer_name": "Dodge",
    "model_name": "Ram 1500 Club Cab",
    "car_type": "Pickup"
  },
  {
    "year": 1997,
    "manufacturer_name": "Dodge",
    "model_name": "Intrepid",
    "car_type": "Sedan"
  },
  {
    "year": 1997,
    "manufacturer_name": "Dodge",
    "model_name": "Grand Caravan Passenger",
    "car_type": "Van/Minivan"
  },
  {
    "year": 1997,
    "manufacturer_name": "Ford",
    "model_name": "Aspire",
    "car_type": "Hatchback"
  },
  {
    "year": 1997,
    "manufacturer_name": "Dodge",
    "model_name": "Dakota Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 1997,
    "manufacturer_name": "Dodge",
    "model_name": "Avenger",
    "car_type": "Coupe"
  },
  {
    "year": 1997,
    "manufacturer_name": "Dodge",
    "model_name": "Caravan Passenger",
    "car_type": "Van/Minivan"
  },
  {
    "year": 1997,
    "manufacturer_name": "Dodge",
    "model_name": "Ram 2500 Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 1997,
    "manufacturer_name": "Ford",
    "model_name": "Econoline E150 Cargo",
    "car_type": "Van/Minivan"
  },
  {
    "year": 1997,
    "manufacturer_name": "Dodge",
    "model_name": "Ram Wagon 2500",
    "car_type": "Van/Minivan"
  },
  {
    "year": 1997,
    "manufacturer_name": "Dodge",
    "model_name": "Ram 3500 Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 1997,
    "manufacturer_name": "Chrysler",
    "model_name": "Concorde",
    "car_type": "Sedan"
  },
  {
    "year": 1997,
    "manufacturer_name": "Dodge",
    "model_name": "Stratus",
    "car_type": "Sedan"
  },
  {
    "year": 1997,
    "manufacturer_name": "Dodge",
    "model_name": "Ram 3500 Club Cab",
    "car_type": "Pickup"
  },
  {
    "year": 1997,
    "manufacturer_name": "Dodge",
    "model_name": "Neon",
    "car_type": "Sedan, Coupe"
  },
  {
    "year": 1997,
    "manufacturer_name": "Dodge",
    "model_name": "Ram 1500 Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 1997,
    "manufacturer_name": "Dodge",
    "model_name": "Ram Van 3500",
    "car_type": "Van/Minivan"
  },
  {
    "year": 1997,
    "manufacturer_name": "Dodge",
    "model_name": "Ram Wagon 3500",
    "car_type": "Van/Minivan"
  },
  {
    "year": 1997,
    "manufacturer_name": "Dodge",
    "model_name": "Ram Van 1500",
    "car_type": "Van/Minivan"
  },
  {
    "year": 1997,
    "manufacturer_name": "Dodge",
    "model_name": "Ram Van 2500",
    "car_type": "Van/Minivan"
  },
  {
    "year": 1997,
    "manufacturer_name": "Dodge",
    "model_name": "Viper",
    "car_type": "Coupe"
  },
  {
    "year": 1997,
    "manufacturer_name": "Ford",
    "model_name": "Aerostar Cargo",
    "car_type": "Van/Minivan"
  },
  {
    "year": 1997,
    "manufacturer_name": "Eagle",
    "model_name": "Vision",
    "car_type": "Sedan"
  },
  {
    "year": 1997,
    "manufacturer_name": "Ford",
    "model_name": "Econoline E350 Cargo",
    "car_type": "Van/Minivan"
  },
  {
    "year": 1997,
    "manufacturer_name": "Ford",
    "model_name": "F250 Super Cab",
    "car_type": "Pickup"
  },
  {
    "year": 1997,
    "manufacturer_name": "Ford",
    "model_name": "Probe",
    "car_type": "Hatchback"
  },
  {
    "year": 1997,
    "manufacturer_name": "Ford",
    "model_name": "Econoline E250 Cargo",
    "car_type": "Van/Minivan"
  },
  {
    "year": 1997,
    "manufacturer_name": "Ford",
    "model_name": "Contour",
    "car_type": "Sedan"
  },
  {
    "year": 1997,
    "manufacturer_name": "Eagle",
    "model_name": "Talon",
    "car_type": "Hatchback"
  },
  {
    "year": 1997,
    "manufacturer_name": "Ford",
    "model_name": "Expedition",
    "car_type": "SUV"
  },
  {
    "year": 1997,
    "manufacturer_name": "Ford",
    "model_name": "F150 Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 1997,
    "manufacturer_name": "Ford",
    "model_name": "Escort",
    "car_type": "Sedan, Wagon"
  },
  {
    "year": 1997,
    "manufacturer_name": "Ford",
    "model_name": "Crown Victoria",
    "car_type": "Sedan"
  },
  {
    "year": 1997,
    "manufacturer_name": "Ford",
    "model_name": "Club Wagon",
    "car_type": "Van/Minivan"
  },
  {
    "year": 1997,
    "manufacturer_name": "Ford",
    "model_name": "Explorer",
    "car_type": "SUV"
  },
  {
    "year": 1997,
    "manufacturer_name": "Ford",
    "model_name": "F350 Crew Cab",
    "car_type": "Pickup"
  },
  {
    "year": 1997,
    "manufacturer_name": "Ford",
    "model_name": "F250 Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 1997,
    "manufacturer_name": "Ford",
    "model_name": "F350 Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 1997,
    "manufacturer_name": "Ford",
    "model_name": "Windstar Passenger",
    "car_type": "Van/Minivan"
  },
  {
    "year": 1997,
    "manufacturer_name": "GMC",
    "model_name": "1500 Club Coupe",
    "car_type": "Pickup"
  },
  {
    "year": 1997,
    "manufacturer_name": "Ford",
    "model_name": "F250 Crew Cab",
    "car_type": "Pickup"
  },
  {
    "year": 1997,
    "manufacturer_name": "Ford",
    "model_name": "F350 Super Cab",
    "car_type": "Pickup"
  },
  {
    "year": 1997,
    "manufacturer_name": "Ford",
    "model_name": "Ranger Super Cab",
    "car_type": "Pickup"
  },
  {
    "year": 1997,
    "manufacturer_name": "Geo",
    "model_name": "Metro",
    "car_type": "Coupe, Sedan"
  },
  {
    "year": 1997,
    "manufacturer_name": "Ford",
    "model_name": "Windstar Cargo",
    "car_type": "Van/Minivan"
  },
  {
    "year": 1997,
    "manufacturer_name": "Ford",
    "model_name": "F150 Super Cab",
    "car_type": "Pickup"
  },
  {
    "year": 1997,
    "manufacturer_name": "GMC",
    "model_name": "Safari Passenger",
    "car_type": "Van/Minivan"
  },
  {
    "year": 1997,
    "manufacturer_name": "GMC",
    "model_name": "3500 Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 1997,
    "manufacturer_name": "GMC",
    "model_name": "3500 Crew Cab",
    "car_type": "Pickup"
  },
  {
    "year": 1997,
    "manufacturer_name": "Ford",
    "model_name": "Ranger Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 1997,
    "manufacturer_name": "Geo",
    "model_name": "Prizm",
    "car_type": "Sedan"
  },
  {
    "year": 1997,
    "manufacturer_name": "Ford",
    "model_name": "Mustang",
    "car_type": "Convertible, Coupe"
  },
  {
    "year": 1997,
    "manufacturer_name": "Ford",
    "model_name": "Thunderbird",
    "car_type": "Coupe"
  },
  {
    "year": 1997,
    "manufacturer_name": "Ford",
    "model_name": "Taurus",
    "car_type": "Wagon, Sedan"
  },
  {
    "year": 1997,
    "manufacturer_name": "GMC",
    "model_name": "3500 Club Coupe",
    "car_type": "Pickup"
  },
  {
    "year": 1997,
    "manufacturer_name": "GMC",
    "model_name": "2500 Club Coupe",
    "car_type": "Pickup"
  },
  {
    "year": 1997,
    "manufacturer_name": "GMC",
    "model_name": "1500 Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 1997,
    "manufacturer_name": "GMC",
    "model_name": "2500 Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 1997,
    "manufacturer_name": "Geo",
    "model_name": "Tracker",
    "car_type": "SUV"
  },
  {
    "year": 1997,
    "manufacturer_name": "GMC",
    "model_name": "Savana 1500 Cargo",
    "car_type": "Van/Minivan"
  },
  {
    "year": 1997,
    "manufacturer_name": "GMC",
    "model_name": "Suburban 2500",
    "car_type": "SUV"
  },
  {
    "year": 1997,
    "manufacturer_name": "GMC",
    "model_name": "Savana 1500 Passenger",
    "car_type": "Van/Minivan"
  },
  {
    "year": 1997,
    "manufacturer_name": "Honda",
    "model_name": "CR-V",
    "car_type": "SUV"
  },
  {
    "year": 1997,
    "manufacturer_name": "Honda",
    "model_name": "Accord",
    "car_type": "Sedan, Wagon, Coupe"
  },
  {
    "year": 1997,
    "manufacturer_name": "GMC",
    "model_name": "2500 HD Club Coupe",
    "car_type": "Pickup"
  },
  {
    "year": 1997,
    "manufacturer_name": "GMC",
    "model_name": "Safari Cargo",
    "car_type": "Van/Minivan"
  },
  {
    "year": 1997,
    "manufacturer_name": "Honda",
    "model_name": "Civic",
    "car_type": "Coupe, Hatchback, Sedan"
  },
  {
    "year": 1997,
    "manufacturer_name": "GMC",
    "model_name": "Savana 3500 Cargo",
    "car_type": "Van/Minivan"
  },
  {
    "year": 1997,
    "manufacturer_name": "GMC",
    "model_name": "Savana 3500 Passenger",
    "car_type": "Van/Minivan"
  },
  {
    "year": 1997,
    "manufacturer_name": "GMC",
    "model_name": "Jimmy",
    "car_type": "SUV"
  },
  {
    "year": 1997,
    "manufacturer_name": "GMC",
    "model_name": "Yukon",
    "car_type": "SUV"
  },
  {
    "year": 1997,
    "manufacturer_name": "GMC",
    "model_name": "Savana 2500 Passenger",
    "car_type": "Van/Minivan"
  },
  {
    "year": 1997,
    "manufacturer_name": "Honda",
    "model_name": "Prelude",
    "car_type": "Coupe"
  },
  {
    "year": 1997,
    "manufacturer_name": "GMC",
    "model_name": "Savana 2500 Cargo",
    "car_type": "Van/Minivan"
  },
  {
    "year": 1997,
    "manufacturer_name": "Honda",
    "model_name": "Odyssey",
    "car_type": "Van/Minivan"
  },
  {
    "year": 1997,
    "manufacturer_name": "Hyundai",
    "model_name": "Elantra",
    "car_type": "Wagon, Sedan"
  },
  {
    "year": 1997,
    "manufacturer_name": "GMC",
    "model_name": "Sonoma Club Coupe Cab",
    "car_type": "Pickup"
  },
  {
    "year": 1997,
    "manufacturer_name": "Honda",
    "model_name": "del Sol",
    "car_type": "Coupe"
  },
  {
    "year": 1997,
    "manufacturer_name": "HUMMER",
    "model_name": "H1",
    "car_type": "SUV, Wagon"
  },
  {
    "year": 1997,
    "manufacturer_name": "GMC",
    "model_name": "Sonoma Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 1997,
    "manufacturer_name": "GMC",
    "model_name": "Suburban 1500",
    "car_type": "SUV"
  },
  {
    "year": 1997,
    "manufacturer_name": "Hyundai",
    "model_name": "Accent",
    "car_type": "Hatchback, Sedan"
  },
  {
    "year": 1997,
    "manufacturer_name": "Honda",
    "model_name": "Passport",
    "car_type": "SUV"
  },
  {
    "year": 1997,
    "manufacturer_name": "Hyundai",
    "model_name": "Sonata",
    "car_type": "Sedan"
  },
  {
    "year": 1997,
    "manufacturer_name": "Lincoln",
    "model_name": "Town Car",
    "car_type": "Sedan"
  },
  {
    "year": 1997,
    "manufacturer_name": "Isuzu",
    "model_name": "Hombre Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 1997,
    "manufacturer_name": "Isuzu",
    "model_name": "Trooper",
    "car_type": "SUV"
  },
  {
    "year": 1997,
    "manufacturer_name": "INFINITI",
    "model_name": "J",
    "car_type": "Sedan"
  },
  {
    "year": 1997,
    "manufacturer_name": "Hyundai",
    "model_name": "Tiburon",
    "car_type": "Hatchback"
  },
  {
    "year": 1997,
    "manufacturer_name": "INFINITI",
    "model_name": "QX",
    "car_type": "SUV"
  },
  {
    "year": 1997,
    "manufacturer_name": "Jeep",
    "model_name": "Cherokee",
    "car_type": "SUV"
  },
  {
    "year": 1997,
    "manufacturer_name": "Isuzu",
    "model_name": "Rodeo",
    "car_type": "SUV"
  },
  {
    "year": 1997,
    "manufacturer_name": "Jaguar",
    "model_name": "XJ",
    "car_type": "Sedan"
  },
  {
    "year": 1997,
    "manufacturer_name": "INFINITI",
    "model_name": "Q",
    "car_type": "Sedan"
  },
  {
    "year": 1997,
    "manufacturer_name": "Jeep",
    "model_name": "Grand Cherokee",
    "car_type": "SUV"
  },
  {
    "year": 1997,
    "manufacturer_name": "INFINITI",
    "model_name": "I",
    "car_type": "Sedan"
  },
  {
    "year": 1997,
    "manufacturer_name": "Isuzu",
    "model_name": "Oasis",
    "car_type": "Van/Minivan"
  },
  {
    "year": 1997,
    "manufacturer_name": "Kia",
    "model_name": "Sportage",
    "car_type": "SUV"
  },
  {
    "year": 1997,
    "manufacturer_name": "Lincoln",
    "model_name": "Continental",
    "car_type": "Sedan"
  },
  {
    "year": 1997,
    "manufacturer_name": "Isuzu",
    "model_name": "Hombre Spacecab",
    "car_type": "Pickup"
  },
  {
    "year": 1997,
    "manufacturer_name": "Kia",
    "model_name": "Sephia",
    "car_type": "Sedan"
  },
  {
    "year": 1997,
    "manufacturer_name": "Jaguar",
    "model_name": "XK",
    "car_type": "Convertible, Coupe"
  },
  {
    "year": 1997,
    "manufacturer_name": "Land Rover",
    "model_name": "Defender 90",
    "car_type": "SUV"
  },
  {
    "year": 1997,
    "manufacturer_name": "MAZDA",
    "model_name": "626",
    "car_type": "Sedan"
  },
  {
    "year": 1997,
    "manufacturer_name": "Jeep",
    "model_name": "Wrangler",
    "car_type": "SUV"
  },
  {
    "year": 1997,
    "manufacturer_name": "Lexus",
    "model_name": "LX",
    "car_type": "SUV"
  },
  {
    "year": 1997,
    "manufacturer_name": "Lexus",
    "model_name": "LS",
    "car_type": "Sedan"
  },
  {
    "year": 1997,
    "manufacturer_name": "Land Rover",
    "model_name": "Range Rover",
    "car_type": "SUV"
  },
  {
    "year": 1997,
    "manufacturer_name": "Lexus",
    "model_name": "GS",
    "car_type": "Sedan"
  },
  {
    "year": 1997,
    "manufacturer_name": "Land Rover",
    "model_name": "Discovery",
    "car_type": "SUV"
  },
  {
    "year": 1997,
    "manufacturer_name": "Lexus",
    "model_name": "ES",
    "car_type": "Sedan"
  },
  {
    "year": 1997,
    "manufacturer_name": "Lexus",
    "model_name": "SC",
    "car_type": "Coupe"
  },
  {
    "year": 1997,
    "manufacturer_name": "Mercury",
    "model_name": "Mystique",
    "car_type": "Sedan"
  },
  {
    "year": 1997,
    "manufacturer_name": "MAZDA",
    "model_name": "MPV",
    "car_type": "Van/Minivan"
  },
  {
    "year": 1997,
    "manufacturer_name": "MAZDA",
    "model_name": "B-Series Cab Plus",
    "car_type": "Pickup"
  },
  {
    "year": 1997,
    "manufacturer_name": "MAZDA",
    "model_name": "Protege",
    "car_type": "Sedan"
  },
  {
    "year": 1997,
    "manufacturer_name": "Lincoln",
    "model_name": "Mark VIII",
    "car_type": "Coupe"
  },
  {
    "year": 1997,
    "manufacturer_name": "MAZDA",
    "model_name": "B-Series Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 1997,
    "manufacturer_name": "Mercury",
    "model_name": "Mountaineer",
    "car_type": "SUV"
  },
  {
    "year": 1997,
    "manufacturer_name": "MAZDA",
    "model_name": "MX-5 Miata",
    "car_type": "Convertible"
  },
  {
    "year": 1997,
    "manufacturer_name": "Mercedes-Benz",
    "model_name": "E-Class",
    "car_type": "Sedan"
  },
  {
    "year": 1997,
    "manufacturer_name": "Mercury",
    "model_name": "Cougar",
    "car_type": "Sedan"
  },
  {
    "year": 1997,
    "manufacturer_name": "Mercedes-Benz",
    "model_name": "C-Class",
    "car_type": "Sedan"
  },
  {
    "year": 1997,
    "manufacturer_name": "MAZDA",
    "model_name": "Millenia",
    "car_type": "Sedan"
  },
  {
    "year": 1997,
    "manufacturer_name": "Mercedes-Benz",
    "model_name": "S-Class",
    "car_type": "Sedan, Coupe"
  },
  {
    "year": 1997,
    "manufacturer_name": "MAZDA",
    "model_name": "MX-6",
    "car_type": "Coupe"
  },
  {
    "year": 1997,
    "manufacturer_name": "Mercedes-Benz",
    "model_name": "SL-Class",
    "car_type": "Convertible"
  },
  {
    "year": 1997,
    "manufacturer_name": "Mercury",
    "model_name": "Villager",
    "car_type": "Van/Minivan"
  },
  {
    "year": 1997,
    "manufacturer_name": "Nissan",
    "model_name": "Maxima",
    "car_type": "Sedan"
  },
  {
    "year": 1997,
    "manufacturer_name": "Mitsubishi",
    "model_name": "Galant",
    "car_type": "Sedan"
  },
  {
    "year": 1997,
    "manufacturer_name": "Oldsmobile",
    "model_name": "Cutlass",
    "car_type": "Sedan"
  },
  {
    "year": 1997,
    "manufacturer_name": "Mitsubishi",
    "model_name": "Montero",
    "car_type": "SUV"
  },
  {
    "year": 1997,
    "manufacturer_name": "Mitsubishi",
    "model_name": "Diamante",
    "car_type": "Sedan"
  },
  {
    "year": 1997,
    "manufacturer_name": "Nissan",
    "model_name": "240SX",
    "car_type": "Coupe"
  },
  {
    "year": 1997,
    "manufacturer_name": "Mitsubishi",
    "model_name": "Montero Sport",
    "car_type": "SUV"
  },
  {
    "year": 1997,
    "manufacturer_name": "Mercury",
    "model_name": "Grand Marquis",
    "car_type": "Sedan"
  },
  {
    "year": 1997,
    "manufacturer_name": "Mitsubishi",
    "model_name": "3000GT",
    "car_type": "Hatchback"
  },
  {
    "year": 1997,
    "manufacturer_name": "Mercury",
    "model_name": "Tracer",
    "car_type": "Sedan, Wagon"
  },
  {
    "year": 1997,
    "manufacturer_name": "Nissan",
    "model_name": "200SX",
    "car_type": "Coupe"
  },
  {
    "year": 1997,
    "manufacturer_name": "Mercury",
    "model_name": "Sable",
    "car_type": "Sedan, Wagon"
  },
  {
    "year": 1997,
    "manufacturer_name": "Mitsubishi",
    "model_name": "Mirage",
    "car_type": "Sedan, Coupe"
  },
  {
    "year": 1997,
    "manufacturer_name": "Nissan",
    "model_name": "Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 1997,
    "manufacturer_name": "Nissan",
    "model_name": "Altima",
    "car_type": "Sedan"
  },
  {
    "year": 1997,
    "manufacturer_name": "Mitsubishi",
    "model_name": "Eclipse",
    "car_type": "Coupe, Convertible"
  },
  {
    "year": 1997,
    "manufacturer_name": "Nissan",
    "model_name": "Sentra",
    "car_type": "Sedan"
  },
  {
    "year": 1997,
    "manufacturer_name": "Nissan",
    "model_name": "Quest",
    "car_type": "Van/Minivan"
  },
  {
    "year": 1997,
    "manufacturer_name": "Nissan",
    "model_name": "Pathfinder",
    "car_type": "SUV"
  },
  {
    "year": 1997,
    "manufacturer_name": "Oldsmobile",
    "model_name": "88",
    "car_type": "Sedan"
  },
  {
    "year": 1997,
    "manufacturer_name": "Nissan",
    "model_name": "King Cab",
    "car_type": "Pickup"
  },
  {
    "year": 1997,
    "manufacturer_name": "Oldsmobile",
    "model_name": "Cutlass Supreme",
    "car_type": "Sedan, Coupe"
  },
  {
    "year": 1997,
    "manufacturer_name": "Oldsmobile",
    "model_name": "Aurora",
    "car_type": "Sedan"
  },
  {
    "year": 1997,
    "manufacturer_name": "Pontiac",
    "model_name": "Bonneville",
    "car_type": "Sedan"
  },
  {
    "year": 1997,
    "manufacturer_name": "Plymouth",
    "model_name": "Breeze",
    "car_type": "Sedan"
  },
  {
    "year": 1997,
    "manufacturer_name": "Oldsmobile",
    "model_name": "Bravada",
    "car_type": "SUV"
  },
  {
    "year": 1997,
    "manufacturer_name": "Pontiac",
    "model_name": "Firebird",
    "car_type": "Coupe, Convertible"
  },
  {
    "year": 1997,
    "manufacturer_name": "Plymouth",
    "model_name": "Voyager",
    "car_type": "Van/Minivan"
  },
  {
    "year": 1997,
    "manufacturer_name": "Oldsmobile",
    "model_name": "Regency",
    "car_type": "Sedan"
  },
  {
    "year": 1997,
    "manufacturer_name": "Saturn",
    "model_name": "S-Series",
    "car_type": "Coupe, Sedan, Wagon"
  },
  {
    "year": 1997,
    "manufacturer_name": "Oldsmobile",
    "model_name": "Silhouette",
    "car_type": "Van/Minivan"
  },
  {
    "year": 1997,
    "manufacturer_name": "Suzuki",
    "model_name": "Esteem",
    "car_type": "Sedan"
  },
  {
    "year": 1997,
    "manufacturer_name": "Oldsmobile",
    "model_name": "Achieva",
    "car_type": "Sedan, Coupe"
  },
  {
    "year": 1997,
    "manufacturer_name": "Saab",
    "model_name": "900",
    "car_type": "Coupe, Hatchback, Convertible"
  },
  {
    "year": 1997,
    "manufacturer_name": "Pontiac",
    "model_name": "Trans Sport",
    "car_type": "Van/Minivan"
  },
  {
    "year": 1997,
    "manufacturer_name": "Plymouth",
    "model_name": "Grand Voyager",
    "car_type": "Van/Minivan"
  },
  {
    "year": 1997,
    "manufacturer_name": "Toyota",
    "model_name": "Camry",
    "car_type": "Sedan"
  },
  {
    "year": 1997,
    "manufacturer_name": "Subaru",
    "model_name": "Impreza",
    "car_type": "Coupe, Wagon, Sedan"
  },
  {
    "year": 1997,
    "manufacturer_name": "Porsche",
    "model_name": "911",
    "car_type": "Coupe, Convertible"
  },
  {
    "year": 1997,
    "manufacturer_name": "Pontiac",
    "model_name": "Sunfire",
    "car_type": "Coupe, Convertible, Sedan"
  },
  {
    "year": 1997,
    "manufacturer_name": "Pontiac",
    "model_name": "Grand Prix",
    "car_type": "Sedan, Coupe"
  },
  {
    "year": 1997,
    "manufacturer_name": "Plymouth",
    "model_name": "Prowler",
    "car_type": "Convertible"
  },
  {
    "year": 1997,
    "manufacturer_name": "Plymouth",
    "model_name": "Neon",
    "car_type": "Sedan, Coupe"
  },
  {
    "year": 1997,
    "manufacturer_name": "Suzuki",
    "model_name": "X-90",
    "car_type": "SUV"
  },
  {
    "year": 1997,
    "manufacturer_name": "Porsche",
    "model_name": "Boxster",
    "car_type": "Convertible"
  },
  {
    "year": 1997,
    "manufacturer_name": "Subaru",
    "model_name": "Legacy",
    "car_type": "Sedan, Wagon"
  },
  {
    "year": 1997,
    "manufacturer_name": "Pontiac",
    "model_name": "Grand Am",
    "car_type": "Sedan, Coupe"
  },
  {
    "year": 1997,
    "manufacturer_name": "Saab",
    "model_name": "9000",
    "car_type": "Hatchback"
  },
  {
    "year": 1997,
    "manufacturer_name": "Suzuki",
    "model_name": "Sidekick",
    "car_type": "SUV"
  },
  {
    "year": 1997,
    "manufacturer_name": "Oldsmobile",
    "model_name": "LSS",
    "car_type": "Sedan"
  },
  {
    "year": 1997,
    "manufacturer_name": "Suzuki",
    "model_name": "Swift",
    "car_type": "Hatchback"
  },
  {
    "year": 1997,
    "manufacturer_name": "Toyota",
    "model_name": "4Runner",
    "car_type": "SUV"
  },
  {
    "year": 1997,
    "manufacturer_name": "Subaru",
    "model_name": "SVX",
    "car_type": "Coupe"
  },
  {
    "year": 1997,
    "manufacturer_name": "Toyota",
    "model_name": "Celica",
    "car_type": "Hatchback, Coupe, Convertible"
  },
  {
    "year": 1997,
    "manufacturer_name": "Toyota",
    "model_name": "Avalon",
    "car_type": "Sedan"
  },
  {
    "year": 1997,
    "manufacturer_name": "Toyota",
    "model_name": "Land Cruiser",
    "car_type": "SUV"
  },
  {
    "year": 1997,
    "manufacturer_name": "Toyota",
    "model_name": "T100 Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 1997,
    "manufacturer_name": "Toyota",
    "model_name": "T100 Xtracab",
    "car_type": "Pickup"
  },
  {
    "year": 1997,
    "manufacturer_name": "Toyota",
    "model_name": "RAV4",
    "car_type": "SUV"
  },
  {
    "year": 1996,
    "manufacturer_name": "Acura",
    "model_name": "Integra",
    "car_type": "Sedan, Hatchback"
  },
  {
    "year": 1997,
    "manufacturer_name": "Toyota",
    "model_name": "Paseo",
    "car_type": "Hatchback, Convertible"
  },
  {
    "year": 1996,
    "manufacturer_name": "Acura",
    "model_name": "SLX",
    "car_type": "SUV"
  },
  {
    "year": 1997,
    "manufacturer_name": "Toyota",
    "model_name": "Tacoma Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 1997,
    "manufacturer_name": "Toyota",
    "model_name": "Supra",
    "car_type": "Hatchback"
  },
  {
    "year": 1996,
    "manufacturer_name": "BMW",
    "model_name": "7 Series",
    "car_type": "Sedan"
  },
  {
    "year": 1996,
    "manufacturer_name": "Acura",
    "model_name": "TL",
    "car_type": "Sedan"
  },
  {
    "year": 1996,
    "manufacturer_name": "Audi",
    "model_name": "A4",
    "car_type": "Sedan"
  },
  {
    "year": 1996,
    "manufacturer_name": "Acura",
    "model_name": "NSX",
    "car_type": "Coupe, Convertible"
  },
  {
    "year": 1997,
    "manufacturer_name": "Volkswagen",
    "model_name": "Passat",
    "car_type": "Sedan, Wagon"
  },
  {
    "year": 1997,
    "manufacturer_name": "Toyota",
    "model_name": "Corolla",
    "car_type": "Sedan"
  },
  {
    "year": 1997,
    "manufacturer_name": "Volkswagen",
    "model_name": "Golf",
    "car_type": "Hatchback"
  },
  {
    "year": 1997,
    "manufacturer_name": "Volkswagen",
    "model_name": "Jetta",
    "car_type": "Sedan"
  },
  {
    "year": 1996,
    "manufacturer_name": "Audi",
    "model_name": "Cabriolet",
    "car_type": "Convertible"
  },
  {
    "year": 1996,
    "manufacturer_name": "BMW",
    "model_name": "3 Series",
    "car_type": "Hatchback, Coupe, Sedan, Convertible"
  },
  {
    "year": 1997,
    "manufacturer_name": "Toyota",
    "model_name": "Previa",
    "car_type": "Van/Minivan"
  },
  {
    "year": 1997,
    "manufacturer_name": "Toyota",
    "model_name": "Tacoma Xtracab",
    "car_type": "Pickup"
  },
  {
    "year": 1996,
    "manufacturer_name": "BMW",
    "model_name": "Z3",
    "car_type": "Convertible"
  },
  {
    "year": 1996,
    "manufacturer_name": "Buick",
    "model_name": "LeSabre",
    "car_type": "Sedan"
  },
  {
    "year": 1997,
    "manufacturer_name": "Volvo",
    "model_name": "850",
    "car_type": "Sedan, Wagon"
  },
  {
    "year": 1996,
    "manufacturer_name": "Audi",
    "model_name": "A6",
    "car_type": "Sedan, Wagon"
  },
  {
    "year": 1997,
    "manufacturer_name": "Toyota",
    "model_name": "Tercel",
    "car_type": "Sedan"
  },
  {
    "year": 1997,
    "manufacturer_name": "Volvo",
    "model_name": "960",
    "car_type": "Sedan, Wagon"
  },
  {
    "year": 1996,
    "manufacturer_name": "BMW",
    "model_name": "8 Series",
    "car_type": "Coupe"
  },
  {
    "year": 1997,
    "manufacturer_name": "Volvo",
    "model_name": "V90",
    "car_type": "Wagon"
  },
  {
    "year": 1996,
    "manufacturer_name": "Acura",
    "model_name": "RL",
    "car_type": "Sedan"
  },
  {
    "year": 1997,
    "manufacturer_name": "Volkswagen",
    "model_name": "Cabrio",
    "car_type": "Convertible"
  },
  {
    "year": 1997,
    "manufacturer_name": "Volvo",
    "model_name": "S90",
    "car_type": "Sedan"
  },
  {
    "year": 1996,
    "manufacturer_name": "Chevrolet",
    "model_name": "1500 Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 1996,
    "manufacturer_name": "Buick",
    "model_name": "Century",
    "car_type": "Wagon, Sedan"
  },
  {
    "year": 1996,
    "manufacturer_name": "Buick",
    "model_name": "Riviera",
    "car_type": "Coupe"
  },
  {
    "year": 1996,
    "manufacturer_name": "Buick",
    "model_name": "Regal",
    "car_type": "Coupe, Sedan"
  },
  {
    "year": 1996,
    "manufacturer_name": "Buick",
    "model_name": "Roadmaster",
    "car_type": "Sedan, Wagon"
  },
  {
    "year": 1996,
    "manufacturer_name": "BMW",
    "model_name": "M3",
    "car_type": "Coupe"
  },
  {
    "year": 1996,
    "manufacturer_name": "Buick",
    "model_name": "Park Avenue",
    "car_type": "Sedan"
  },
  {
    "year": 1996,
    "manufacturer_name": "Buick",
    "model_name": "Skylark",
    "car_type": "Coupe, Sedan"
  },
  {
    "year": 1996,
    "manufacturer_name": "Cadillac",
    "model_name": "DeVille",
    "car_type": "Sedan"
  },
  {
    "year": 1996,
    "manufacturer_name": "Chevrolet",
    "model_name": "1500 Extended Cab",
    "car_type": "Pickup"
  },
  {
    "year": 1996,
    "manufacturer_name": "Chevrolet",
    "model_name": "Impala",
    "car_type": "Sedan"
  },
  {
    "year": 1996,
    "manufacturer_name": "Chevrolet",
    "model_name": "Express 1500 Passenger",
    "car_type": "Van/Minivan"
  },
  {
    "year": 1996,
    "manufacturer_name": "Chevrolet",
    "model_name": "Express 3500 Passenger",
    "car_type": "Van/Minivan"
  },
  {
    "year": 1996,
    "manufacturer_name": "Cadillac",
    "model_name": "Fleetwood",
    "car_type": "Sedan"
  },
  {
    "year": 1996,
    "manufacturer_name": "Chevrolet",
    "model_name": "3500 Extended Cab",
    "car_type": "Pickup"
  },
  {
    "year": 1996,
    "manufacturer_name": "Chevrolet",
    "model_name": "G-Series 2500",
    "car_type": "Van/Minivan"
  },
  {
    "year": 1996,
    "manufacturer_name": "Chevrolet",
    "model_name": "Astro Passenger",
    "car_type": "Van/Minivan"
  },
  {
    "year": 1996,
    "manufacturer_name": "Chevrolet",
    "model_name": "Astro Cargo",
    "car_type": "Van/Minivan"
  },
  {
    "year": 1996,
    "manufacturer_name": "Cadillac",
    "model_name": "Seville",
    "car_type": "Sedan"
  },
  {
    "year": 1996,
    "manufacturer_name": "Cadillac",
    "model_name": "Eldorado",
    "car_type": "Coupe"
  },
  {
    "year": 1996,
    "manufacturer_name": "Chevrolet",
    "model_name": "2500 HD Extended Cab",
    "car_type": "Pickup"
  },
  {
    "year": 1996,
    "manufacturer_name": "Chevrolet",
    "model_name": "Beretta",
    "car_type": "Coupe"
  },
  {
    "year": 1996,
    "manufacturer_name": "Chevrolet",
    "model_name": "G-Series G30",
    "car_type": "Van/Minivan"
  },
  {
    "year": 1996,
    "manufacturer_name": "Chevrolet",
    "model_name": "3500 Crew Cab",
    "car_type": "Pickup"
  },
  {
    "year": 1996,
    "manufacturer_name": "Chevrolet",
    "model_name": "G-Series 1500",
    "car_type": "Van/Minivan"
  },
  {
    "year": 1996,
    "manufacturer_name": "Chevrolet",
    "model_name": "Lumina",
    "car_type": "Sedan"
  },
  {
    "year": 1996,
    "manufacturer_name": "Chevrolet",
    "model_name": "Suburban 1500",
    "car_type": "SUV"
  },
  {
    "year": 1996,
    "manufacturer_name": "Chevrolet",
    "model_name": "2500 Extended Cab",
    "car_type": "Pickup"
  },
  {
    "year": 1996,
    "manufacturer_name": "Chevrolet",
    "model_name": "Lumina Passenger",
    "car_type": "Van/Minivan"
  },
  {
    "year": 1996,
    "manufacturer_name": "Chevrolet",
    "model_name": "Sportvan G30",
    "car_type": "Van/Minivan"
  },
  {
    "year": 1996,
    "manufacturer_name": "Chevrolet",
    "model_name": "2500 Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 1996,
    "manufacturer_name": "Chevrolet",
    "model_name": "Corvette",
    "car_type": "Hatchback, Convertible"
  },
  {
    "year": 1996,
    "manufacturer_name": "Chevrolet",
    "model_name": "Corsica",
    "car_type": "Sedan"
  },
  {
    "year": 1996,
    "manufacturer_name": "Chevrolet",
    "model_name": "Blazer",
    "car_type": "SUV"
  },
  {
    "year": 1996,
    "manufacturer_name": "Chevrolet",
    "model_name": "Lumina Cargo",
    "car_type": "Van/Minivan"
  },
  {
    "year": 1996,
    "manufacturer_name": "Chevrolet",
    "model_name": "Express 2500 Passenger",
    "car_type": "Van/Minivan"
  },
  {
    "year": 1996,
    "manufacturer_name": "Chevrolet",
    "model_name": "Camaro",
    "car_type": "Hatchback, Convertible"
  },
  {
    "year": 1996,
    "manufacturer_name": "Chevrolet",
    "model_name": "Caprice Classic",
    "car_type": "Sedan, Wagon"
  },
  {
    "year": 1996,
    "manufacturer_name": "Chevrolet",
    "model_name": "3500 Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 1996,
    "manufacturer_name": "Chevrolet",
    "model_name": "S10 Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 1996,
    "manufacturer_name": "Chevrolet",
    "model_name": "Cavalier",
    "car_type": "Sedan, Coupe, Convertible"
  },
  {
    "year": 1996,
    "manufacturer_name": "Chrysler",
    "model_name": "Concorde",
    "car_type": "Sedan"
  },
  {
    "year": 1996,
    "manufacturer_name": "Dodge",
    "model_name": "Neon",
    "car_type": "Sedan, Coupe"
  },
  {
    "year": 1996,
    "manufacturer_name": "Chrysler",
    "model_name": "Cirrus",
    "car_type": "Sedan"
  },
  {
    "year": 1996,
    "manufacturer_name": "Dodge",
    "model_name": "Caravan Passenger",
    "car_type": "Van/Minivan"
  },
  {
    "year": 1996,
    "manufacturer_name": "Chrysler",
    "model_name": "Town & Country",
    "car_type": "Van/Minivan"
  },
  {
    "year": 1996,
    "manufacturer_name": "Chevrolet",
    "model_name": "Monte Carlo",
    "car_type": "Coupe"
  },
  {
    "year": 1996,
    "manufacturer_name": "Dodge",
    "model_name": "Grand Caravan Passenger",
    "car_type": "Van/Minivan"
  },
  {
    "year": 1996,
    "manufacturer_name": "Dodge",
    "model_name": "Avenger",
    "car_type": "Coupe"
  },
  {
    "year": 1996,
    "manufacturer_name": "Dodge",
    "model_name": "Intrepid",
    "car_type": "Sedan"
  },
  {
    "year": 1996,
    "manufacturer_name": "Dodge",
    "model_name": "Ram 2500 Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 1996,
    "manufacturer_name": "Chrysler",
    "model_name": "LHS",
    "car_type": "Sedan"
  },
  {
    "year": 1996,
    "manufacturer_name": "Chevrolet",
    "model_name": "S10 Extended Cab",
    "car_type": "Pickup"
  },
  {
    "year": 1996,
    "manufacturer_name": "Chevrolet",
    "model_name": "Suburban 2500",
    "car_type": "SUV"
  },
  {
    "year": 1996,
    "manufacturer_name": "Chrysler",
    "model_name": "Sebring",
    "car_type": "Coupe, Convertible"
  },
  {
    "year": 1996,
    "manufacturer_name": "Dodge",
    "model_name": "Ram 3500 Club Cab",
    "car_type": "Pickup"
  },
  {
    "year": 1996,
    "manufacturer_name": "Chevrolet",
    "model_name": "Tahoe",
    "car_type": "SUV"
  },
  {
    "year": 1996,
    "manufacturer_name": "Dodge",
    "model_name": "Dakota Regular Cab",
    "car_type": "Pickup"
  },
  {
    "year": 1996,
    "manufacturer_name": "Chrysler",
    "model_name": "New Yorker",
    "car_type": "Sedan"
  },
  {
    "year": 1996,
    "manufacturer_name": "Dodge",
    "model_name": "Ram Van 3500",
    "car_type": "Van/Minivan"
  },
  {
    "year": 1996,
    "manufacturer_name": "Dodge",
    "model_name": "Ram Van 1500",
    "car_type": "Van/Minivan"
  },
]