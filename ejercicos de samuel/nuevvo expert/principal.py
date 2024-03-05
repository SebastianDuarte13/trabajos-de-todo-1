import modulos.camperModule as camp
import modulos.rutasModule as rut
import modulos.areassalones as sal

campus ={
    'campers':{},
    'rutas':{
        'java':{
            'fundamentos':{},
            'web':{},
            'lenguajeformal':{},
            'backend':{}
        },
        'nodejs':{
            'fundamentos':{},
            'web':{},
            'lenguajeformal':{},
            'backend':{}
        },
        'netcore':{
            'fundamentos':{},
            'web':{},
            'lenguajeformal':{},
            'backend':{}
        }
    },
    "areas":{
        'apolo':{
            'nombre':'Apollo',
            'capacidad':33,
        },
        'artemis':{
            'nombre':'artemis',
            'capacidad':35,
        },
        'sputnik':{
            'nombre':'sputnik',
            'capacidad':36,
        }
    },  
    "trainners":{},
    "matricula":{}  
}

camp.AddCamper(campus.get('campers'))
rut.AddRuta(campus.get('rutas'))
sal.AddSalones(campus.get('areas'))