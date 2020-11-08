crop_details = {
    'rice': {
        'weather': {
            'im1': '/rice/rice1.jpg',
            'max_temp': 35,
            'min_temp': 25,
            'max_humidity': 80,
            'min_humidity': 84
        },
        'irrigation': {
            'im1': '/rice/rice1.jpg',
            'max_water': 2500,
            'min_water': 900,
            'annual_rainfall': 100
        },
        'diseases': {
            'im1': '/rice/rice1.jpg',
            'name': [ 'False smut', 'Bacterial blight','Bakanae', 'Blast (leaf and collar)'],
            'prevention': ['Use balanced amounts of plant nutrients, especially nitrogen.', 
            'Ensure good drainage of fields (in conventionally flooded crops) and nurseries.', 
            'Keep fields clean.', 
            'Allow fallow fields to dry in order to suppress disease agents in the soil and plant residues.',
            'Where possible, perform conservation tillage and continuous rice cropping.',
            'Use moderate rates of Nitrogen.',
            'Use certified seeds.',
            'Seed treatment with fungicide.']
        },
        'pests': {
            'im1': '/rice/rice1.jpg',
            'pest': {
                'Planthoppers': 'Imidacloprid',
                'Stem Borer':  'Deltamethrin',
                'Aphid': 'Malathion',
                'Meal Bugs': 'Neem Oil',
                'Thrips': 'Spinosad',
                'Rice Bugs': 'Chlorpyriphos'
            }
        },
        'fertilizers': {
            'N': 2,
            'P': 1,
            'K': 2,
            'ph_max': 7.2,
            'ph_min': 5.2,
            'fertilizer': {
                'UREA': 110,
                'DAP or SAP': 27,
                'MOP': 75,
                'ZINC': 20
            },
            'nutrient': {
                'nitrogen': 50,
                'phosphorous': 12,
                'potash': 50
            }
        },
    },
    'grapes': {
        'weather': {
            'im1': 'grapes/grapes1.jpg',
            'max_temp': 32,
            'min_temp': 25,
            'max_humidity': 98,
            'min_humidity': 39
        },
        'irrigation': {
            'im1': '/grapes/grapes1.jpg',
            'type': "Micro Irrigation",
            'max_water': 2200,
            'min_water': 500,
            'annual_rainfall': 20-25
        },
        'diseases': {
            'im1': '/grapes/grapes1.jpg',
           'name': ['Anthracnose', 'Botrytis Bunch Rot', 'Powdery Mildew', 'Leaf Spot'],
            'prevention': [
                'Implementing Crop Rotation.',
                'Application of Fungicides.',
                'Keep fields clean.',
                'Sprays of copper fungicide and Bordeaux mixture.',
                'Severe Pruning.',
                'Use certified seeds.']
        },
        'pests': {
            'im1': '/grapes/grapes1.jpg',
            'pest': {
                'Black vine weevil': 'Metarhizium aniospliae',
                'Grape cane girdler':  'Pruning canes',
                'Grape mealybug': 'Imidacloprid ',
                'Japanese beetle': 'Malathion',
                'Mites': 'Acaricide ',
                'Thrips': 'Pyrethrins '
            }
        },
        'fertilizers': {
                'N': 800,
                'P': 700,
                'K': 850,
                'ph_max': 6.5,
                'ph_min': 5.5,
                'fertilizer': {
                    'UREA': 1/4,
                    'DAP or SAP': 1/2,
                    'MOP': 3/8,
                    'Period for fertilizer spraying': 'Early Summer'
                },
        },
            'nutrient': {
                'nitrogen': 70 - 90,
                'phosphorous': 40 - 60,
                'potash': 75 - 100
            },
        'Seed_details': {
                'Pits':100,
                'Seed spacing to plant': '5 to 6m',
                'Time for sowing': 'December - January',
                'Seed deep to bury': '10 - 20',
                'Season': 'Rabi'

            }
    },
    'millet':
    {
        'weather':
        {
            'im1': 'millet/millets1.jpg',
            'max_temp': 20,
            'min_temp': 15,
            'max_humidity': 40,
            'min_humidity': 40
        },
        'irrigation':
        {
            'im1': 'millet/millets1.jpg',
            "type": "Bio irrigation",
            'max_water': "650 mm/annum",
            'min_water': "450 mm/annum",
            'annual_rainfall': "35-50cm"
        },
        'diseases':
        {
            'im1': 'millet/millets1.jpg',
            'name': ['Head Smut', 'Kernel Smut', 'Grain mold'],
            'prevention': ['seed treatment ', 'crop rotation']
        },
        'pests': {
            'im1': 'millet/millets1.jpg',
            'pest': {
                'corn earworms': 'carbaryl (Sevin), permethrin',
                'aphids': 'Neem oil, insecticidal soaps, and horticultural oils',
                'Lepidoptera larvae': 'Insecticide- H.armigera, S. litura and A. ipsilon',
                'turnip moth': 'insecticidal soap spray '
            }  
        },
        'fertilizers': {
            'N': 2,
            'P': 1,
            'K':  1,
            'ph_max': 5.6,
            'ph_min': 6.2,
            'fertilizer': {
                'UREA': 110,
                'DAP or SAP': 27,
                'MOP': 75,
                'ZINC': 20
            },
            'nutrient': {
                'nitrogen kg/hetare': "100-120",
                'phosphorous kg/hectare': "40-60",
                'potash kg/hectare': "30-40"
            }
        },  
    },
    'banana': 
    {
        'weather': {
            'im1': 'banana/banana1.jpg',
            'max_temp': 32,
            'min_temp': 30,
            'max_humidity': 85,
            'min_humidity': 75
            },
        'irrigation': {
           'im1': 'banana/banana1.jpg',
           'tpye' : "Drip Irrigation",
           'max_water': 2200,
           'min_water': 1200,
           'annual_rainfall': 200-250
           },
           'diseases': {
               'im1': 'banana/banana1.jpg',
               'name': [ 'Panama Wilt', 'Anthracnose','Crown Rot', 'Sigatoka Disease'],
               'prevention': [
                'Severely affected plant should be uprooted and burnt.',
                'Use of improved/resistant cultivars.',
                'Proper sanitation in plantation.',
                ' Improved drainage system.',
                'Foliar spray of Copper Oxychloride contrl diseases.',
                'Minimising bruising.',
                'Prompt cooling to 14 degree celsius.',
                'Proper spacing reduce the incidence of disease.']
                },
                'pests': {
                    'im1': 'banana/banana1.jpg',
                    'pest': {
                        'Adoretus sinicus': 'Sevin',
                        'Caterpillar':  'Carbofuran',
                        'Pentalonia nigronervosa': 'Malathion ',
                        'Bactrocera dorsalis': 'Methyl Eugenol',
                        'Leaf Hoppers': 'Organophosphates ',
                        'Mealy Bugs': 'Neem Oil '
                        }
                    },

            'fertilizers': {
             'N': 7,
             'P': 0.7,
             'K': 17,
             'ph_max': 7.5,
            'ph_min': 6.5,
            'fertilizer': {
                'UREA': 140,
                'DAP or SAP': 155,
                'MOP': 130,
                'Period for fertilizer spraying':'3 - 4 months after planting',
            },
              'nutrient': {
                  'nitrogen': 8,
                  'phosphorous': 10,
                  'potash': 10
                  }
            },
             'Seed_details': {
                'Pits': '30 X 30 cms',
                
                'Seed spacing to plant':'1.5 X 1.5 m',
                
                'Time for sowing':'July-August',
                
                'Seed deep to bury':10 - 20,
                
                'Season':'Except Summer'

            }
    }
}

def get_data(crop, data_name):
    if crop in crop_details:
        return crop_details[crop][data_name]
    return None