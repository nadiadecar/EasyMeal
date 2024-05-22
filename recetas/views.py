from django.shortcuts import render

recetas_disponibles = [
        {
            'id': 0, 
            'nombre': "Cazuela de pollo",
            'ingredientes': ['Pollo', 'Aceite', 'Orégano', 'Pimentón', 'Papas', 'Choclo', 'Zapallo', 'Zanahoria', 'Cebolla', 'Arroz', 'Porotos Verdes'],
            'pasos': {
                '1':'En una olla, calentar el aceite a fuego medio. Agregar la cebolla y cocinar 5-6 minutos sin que se dore. Agregar el pollo y cocinar 6-8 minutos o hasta dorar por todos los lados.',
                '2':'Añadir los pimentones, papas, zapallo, choclo, zanahoria. Revolver.',
                '3':'Agregar 6 tazas de agua y el caldo en polvo de pollo Gourmet. Hervir la mezcla a fuego alto, reducir el calor  y cocinar semi tapado 15 minutos. Luego agregar el arroz y dejarlo cocinando por 15 minutos más. Si seca, agregar más agua.',
                '4':'A último momento agregar los porotos verdes y cocinar por 5 minutos más o bien hasta que las papas estén cocidas. Revolver de vez en cuando.',
                '5':'Servir bien caliente y espolvorear con perejil.'
            },
            'tiempo_estimado': 40, #en minutos
            'dificultad': 'Media',
            'link': 'https://www.gourmet.cl/recetas/cazuela-de-ave/',
            'imagen': 'assets/img/cazuela_pollo.png',
            'Tipo': 'Carnívoro'
        },
        {
            'id': 1, 
            'nombre': 'Fideos de arroz con salteado de tofu y pimiento', 
            'ingredientes': ['Fideos de arroz', 'Tofu firme', 'Pimiento Rojo', 'Jengibre', 'Salsa de soja', 'Pimienta negra', 'Sal', 'Aceite de oliva', 'Perejil', 'Curry molido', 'Ajo granulado', 'Cúrcuma', 'Lima'], 
            'pasos': {
                '1':'Desechar el líquido del tofu y escurrir bien. Envolver en varias capas de papel de cocina y dejar como mínimo 15 minutos con un peso encima.', 
                '2':'Cortar en cubos del tamaño de un bocado. ',
                '3':'Calentar un poco de aceite en una sartén y dorar el tofu por todos lados. Retirar.',
                '4':'Cocer los fideos de arroz en agua hirviendo con un poco de sal durante unos tres minutos, siguiendo las instrucciones del paquete. ',
                '5':'Escurrir y enjuagar con agua fría, soltándolos un poco con un tenedor. Reservar.',
                '6':'Rallar o picar fino el jengibre. Cortar el pimiento en tiras finas. Saltear en la misma sartén a fuego alto ambos ingredientes durante dos minutos. ',
                '7':'Salpimentar, agregar la salsa de soja y las especias. Rehogar 5 minutos. ',
                '8':'Devolver el tofu, dar unas vueltas e incorporar los fideos. Mezclar todo bien hasta que se integren. Servir con perejil picado.'
            },
            'tiempo_estimado': 35, 
            'dificultad': 'Fácil', 
            'link': 'https://www.directoalpaladar.com/recetario/13-recetas-veganas-ricas-proteinas-vegetales-para-celebrar-dia-mundial-veganismo',
            'imagen': 'assets/img/fideos_tofu.png',
            'Tipo': 'Vegetariano'
        },
        {
            'id': 2, 
            'nombre': 'Falafel Ligero', 
            'ingredientes': ['Garbanzos cocidos y escurridos', 'Pan de molde', 'Cebolla', 'Dientes de ajo', 'Comino molido', 'Pimentón', 'Cilantro', 'Perejil','Aceite de oliva', 'Levadura química', 'Agua'], 
            'pasos': {
                '1':'Lavar los garbanzos escurridos y triturar todos los ingredientes en el robot Magimix Cook Expert o robot de cocina, ajustando la textura con agua si fuera necesario. Tomamos pequeñas porciones de la masa y formamos bolitas de igual tamaño. ', 
                '2':'Las colocamos sobre una bandeja de horno cubierta con papel sulfurizado y aplastamos ligeramente con las manos. Dejamos reposar una hora en la nevera o en una zona fría de la cocina.',
                '3':'Cocemos en horno pre calentado a 180ºC, arriba y abajo con calor tradicional, durante unos 20 minutos o hasta que estén dorados. Volteamos cada uno a media cocción, es decir, después de los primeros 10 minutos.',
                '4':'Retiramos del horno y servimos inmediatamente.'
            },
            'tiempo_estimado': 30, 
            'dificultad': 'Fácil', 
            'link': 'https://www.directoalpaladar.com/recetario/13-recetas-veganas-ricas-proteinas-vegetales-para-celebrar-dia-mundial-veganismo',
            'imagen': 'assets/img/falafel.png',
            'Tipo': 'Vegetariano'
        },
        {
            'id': 3, 
            'nombre': 'Ensalada con atún', 
            'ingredientes': ['Zanahorias', 'Paltas', 'Huevos', 'Tomates', 'Choclo', 'Lata de atún', 'Lechuga'], 
            'pasos': {
                '1':'Cocemos los granos de choclo y huevos por separado.',
                '2':'Pelamos y rallamos las zanahorias',
                '3':'Cortamos el tomate en rodajas yo lo dejo con cáscara.. las paltas pueden ir en mitad o en rodajas',
                '4':'Montamos nuestro plato con todas las verduras atún y huevos',
                '5':'Aliñar a gusto'
            },
            'tiempo_estimado': 0, 
            'dificultad': 'Fácil', 
            'link': 'https://cookpad.com/cl/recetas/11065230-hipocalorico?ref=search&search_term=hipocaloricas',
            'imagen': 'assets/img/ensalada_atun.png',
            'Tipo': 'Hipocalórico'
        },
        {
            'id': 4, 
            'nombre': 'Lentejas estofadas sin grasas y cremosas', 
            'ingredientes': ['Lentejas secas', 'Dientes de ajo', 'Hoja de laurel', 'Cebolla', 'Zanahorias', 'Pimenton rojo', 'Pimiento verde', 'Agua o caldo de verduras', 'Pimentón dulce', 'Sal', 'Pimienta'], 
            'pasos': {
                '1':'Introducimos las verduras en una olla a presión con las lentejas sin remojar, el pimentón y el laurel. Añadimos suficiente agua o caldo para cubrir y cerramos la olla, colocando la válvula en la posición 2. ',
                '2':'En el momento en que empiece a salir el vapor, bajamos la intensidad del fuego y contamos 15 minutos. Apagamos y dejamos que el vapor salga lentamente. Abrimos la olla y retiramos las verduras. ',
                '3':'Si preparáis las lentejas en una olla tradicional, el procedimiento es el mismo a excepción del tiempo de cocción que será mayor: 50 minutos y con la tapadera puesta. ',
                '4':'Trituramos las verduras con un poco de líquido de la cocción. Podemos pasar el puré resultante por un colador o devolverlo tal cual a la olla. ',
                '5':'Salpimentamos, damos un último hervor y servimos.'
            },
            'tiempo_estimado': 150, 
            'dificultad': 'Media', 
            'link': 'https://www.directoalpaladar.com/recetario/comidas-ricas-101-recetas-muy-sabrosas-para-disfrutar-a-grande',
            'imagen': 'assets/img/lentejas_estofadas.png',
            'Tipo': 'Vegetariano'
        },
        {
            'id': 5, 
            'nombre': 'Pollo con almendras estilo chino', 
            'ingredientes': ['Pechuga de pollo', 'Salsa de soja', 'Jengibre molido', 'Azúcar moreno', 'Almendras crudas sin piel', 'Zanahorias', 'Cebolla', 'Caldo de pollo', 'Harina de maíz refinada', 'Aceite de girasol', 'Pimienta', 'Sal'], 
            'pasos': {
                '1':'Sumergimos en pollo en una mezcla de salsa de soja, jengibre y azúcar moreno. Dejamos reposar en la nevera una hora. ',
                '2':'Mientras calentamos un poco de aceite en una sartén y freímos las almendras a fuego medio-alto hasta que estén doradas. En el mismo aceite salteamos la cebolla y la zanahoria, dos o tres minutos. Apagamos el fuego y devolvemos las almendras a la sartén. ',
                '3':'Separamos un poco de caldo de pollo en un vasito, añadimos la harina de maíz refinada y removemos hasta integrar. Incorporamos el pollo con la marinada, el caldo y la mezcla de la harina de maíz.',
                '4':'Cocemos 20 minutos a fuego medio-bajo. Si la salsa está muy espesa, la podemos rebajar con un poco de caldo. Si está muy líquida, agregamos un poco más de harina de maíz diluida en agua, y cocemos unos minutos más.'
            },
            'tiempo_estimado': 120, 
            'dificultad': 'Media', 
            'link': 'https://www.directoalpaladar.com/recetario/comidas-ricas-101-recetas-muy-sabrosas-para-disfrutar-a-grande',
            'imagen': 'assets/img/pollo_con_almendras.png',
            'Tipo': 'Carnívoro'
        },
    ]

# Create your views here.
def inicio(request): 
    return render(request, 'recetas/index.html', {})

def listado_recetas(request): 
    
    return render(request, 'recetas/listado_recetas.html', {'recetas_disponibles': recetas_disponibles})

def ver_receta(request, id): 

    return render(request, 'recetas/receta.html', {'receta': recetas_disponibles[id]})