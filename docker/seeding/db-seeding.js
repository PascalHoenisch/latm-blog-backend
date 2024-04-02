db.getCollection("blogs").insertOne({
    author: "Pascal",
    date: ISODate('2023-11-23T08:30:00.000Z'),
    tag: [
        "homeoffice",
        "development"
    ],
    title: {
        en: "Db seeding",
        es: "Db siembra",
        de: "Db sähen",
    },
    slug: {
        en: "ab-seeding",
        es: "db-siembra",
        de: "db-sähen",
    },
    description: {
        en: "This article is all about database seeding. It shows how to setup a manual workflow with docker/ docker compose and mongo db to add some test data.",
        es: "Este articulo trata sobre la siembra de bases de datos. Muestra cómo configurar " +
            "un flujo de trabajo manual con Docker/Docker Compose y Mongo DB para agregar algunos datos de prueba.",
        de: "Dieser Artikel handelt von test Werten fuer die Datenbank. In diesem Artikel wird gezeigt, wie ein Arbeitsfluss mit Docker/Docker-Compose " +
            "und MongoDb zum hinzufuegen implementiert wird.",
    },
    content: {
        md: {
            en: 'Welcome to pad.systemli.org. \n ![the image description](path/to/cat.jpg) \n\n This pad text is synchronized as you type, so that everyone viewing this page sees the same text.\n\nPlease notice:\n- This pad will be DELETED automatically if it wasn\'t edited within the selected expiry time!\n- This pad is accessible by anyone who has the address to it. You\'re adviced to use an unguessable pad name.\n- If you encounter an error while loading the pad, please press CTRL+F5 or CTRL+SHIFT+F5.\n- If you want to store text without editing it afterwards, use https://paste.systemli.org/\n\nFurther details about this and our other services can be found on https://www.systemli.org/en/service/\n\n',
            es: 'Bienvenido a pad.systemli.org.\n ![la descripción de la imagen](path/to/cat.jpg) \nEste pad se sincroniza mientras escribes, por lo que todo el mundo que vea esta página verá el mismo texto.\n\nPor favor, ten en cuenta:\n- ¡Este pad será BORRADO automáticamente si no se edita dentro del tiempo de caducidad seleccionado!\n- Este pad es accesible para cualquiera que tenga su dirección. Te aconsejamos que uses un nombre de pad impredecible.\n- Si encuentras un error mientras se carga el pad, por favor presiona CTRL+F5 o CTRL+SHIFT+F5.\n- Si quieres almacenar texto sin editarlo posteriormente, usa https://paste.systemli.org/\n\nPuedes encontrar más detalles sobre este y otros de nuestros servicios en https://www.systemli.org/en/service/\n\n',
            de: 'Willkommen auf pad.systemli.org.\n ![die Bildbeschreibung](path/to/cat.jpg) \nDieses Pad wird live synchronisiert, so dass alle, die es geöffnet haben, den selben Text sehen.\n\nBitte beachte:\n- Dieses Pad wird automatisch GELÖSCHT, wenn es nicht innerhalb der ausgewählten Ablaufzeit bearbeitet worden ist!\n- Dieses Pad ist für alle lesbar, denen die Adresse des Pads bekannt ist. Wähle sicherheitshalber einen nicht erratbaren Namen für das Pad.\n- Falls beim Laden des Pads eine Fehlermeldung erscheint, drücke STRG+F5 oder STRG+SHIFT+F5.\n- Möchtest du Text nur ablegen und nicht mehr bearbeiten, nutze https://paste.systemli.org/\n\nDetails zu diesem und unseren anderen Diensten findest du unter https://www.systemli.org/service/'
        },
        // is automatic generated from md, set to empty string to regenerate when queried
        cached_html: {
            en: '',
            es: '',
            de: ''
        }
    },
    title_image: {
        path: "path/to/cat.jpg",
        description: {
            en: "a sweet brown cat looking at you",
            es: "una gata mirandote",
            de: "ein süße braune Katze die dich anschaut"
        }
    }
});

db.getCollection("authors").insertOne({
    alt: {
        en: 'john doe looking sweet at you with a hat',
        es: 'John Doe te mira dulcemente y tiene un sombrero puesto.',
        de: 'john doe schaut dich süß an und hat dabei einen hut auf'
    },
    about: {
        en: 'hello I am John doe <br> i like to travel hello I am John doe <br> i like to travel hello I am John doe i like to travel hello I am John doe i like to travel hello I am John doe i like to travel hello I am John doe <br> i like to travel hello I am John doe <br> i like to travel hello I am John doe <br> i like to travel',
        es: 'hola soy john doe, me gusta viajar',
        de: 'hallo ich bin John doe, <br> ich reise gerne'
    },
    imageUri: 'author/nice-image.jpeg',
    name: 'Pascal',
    previewImageUri: 'author/preview/author.png',
    slogan: {
        en: 'english slogan',
        es: 'espańol slogan',
        de: 'deutscher slogan'
    },
    previewImageAlt: {
        en: 'john doe looking sweet at you with a hat only the face',
        es: 'John Doe te mira dulcemente y tiene un sombrero puesto.',
        de: 'john doe schaut dich süß an und hat dabei einen hut auf'
    }
});
