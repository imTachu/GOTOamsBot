from datetime import datetime

TALKS = {
    # Keynotes
    'The Current State of Automotive Security': {
        'speakers': ['Chris Valasek'],
        'track': 'Keynotes',
        'location': 'Effectenbeurszaal',
        'start': datetime(2017, 6, 13, 9, 0),
        'end': datetime(2017, 6, 13, 9, 50),
        'tags': ['security', 'uber']
    },
    'From Heart of Agile to Guest Leadership': {
        'speakers': ['Alistair Cockburn'],
        'track': 'Keynotes',
        'location': 'Effectenbeurszaal',
        'start': datetime(2017, 6, 13, 13, 0),
        'end': datetime(2017, 6, 13, 13, 50),
        'tags': ['agile', 'leadership']
    },
    'Surveillance & Cryptography': {
        'speakers': ['Jaya Baloo'],
        'track': 'Keynotes',
        'location': 'Effectenbeurszaal',
        'start': datetime(2017, 6, 13, 17, 30),
        'end': datetime(2017, 6, 13, 18, 20),
        'tags': ['cryptography', 'surveillance']
    },
    'Engineering You': {
        'speakers': ['Martin Thompson'],
        'track': 'Keynotes',
        'location': 'Effectenbeurszaal',
        'start': datetime(2017, 6, 14, 9, 0),
        'end': datetime(2017, 6, 14, 9, 50),
        'tags': ['personal development']
    },
    'Cloud Trends': {
        'speakers': ['Adrian Cockcroft'],
        'track': 'Keynotes',
        'location': 'Effectenbeurszaal',
        'start': datetime(2017, 6, 14, 13, 0),
        'end': datetime(2017, 6, 14, 13, 50),
        'tags': ['cloud', 'amazon', 'trends']
    },
    'The Scribe\'s Oath': {
        'speakers': ['Robert Martin'],
        'track': 'Keynotes',
        'location': 'Effectenbeurszaal',
        'start': datetime(2017, 6, 14, 17, 10),
        'end': datetime(2017, 6, 13, 18, 0),
        'tags': ['oath', 'clean code']
    },
    # Cloud Native
    'Knee Deep in Microservices': {
        'speakers': ['Adam Sandor'],
        'track': 'Cloud Native',
        'location': 'Effectenbeurszaal',
        'start': datetime(2017, 6, 13, 10, 10),
        'end': datetime(2017, 6, 13, 11, 0),
        'tags': ['microservices', 'DevOps', 'cloud native']
    },
    'From Monoliths Through Cloud Native to Software Supply Chains': {
        'speakers': ['Pini Reznik'],
        'track': 'Cloud Native',
        'location': 'Effectenbeurszaal',
        'start': datetime(2017, 6, 13, 11, 10),
        'end': datetime(2017, 6, 13, 12, 0),
        'tags': ['cloud', 'cloud native', 'monoliths', 'supply chain']
    },
    'From Laptop to the World - Global Deployment at Your Fingertip with Kubernetes Federation': {
        'speakers': ['Ray Tsang'],
        'track': 'Cloud Native',
        'location': 'Effectenbeurszaal',
        'start': datetime(2017, 6, 13, 14, 0),
        'end': datetime(2017, 6, 13, 14, 50),
        'tags': ['kubernetes', 'google', 'DevOps']
    },
    'When should you use a Serverless Approach?': {
        'speakers': ['Paul Johnston'],
        'track': 'Cloud Native',
        'location': 'Effectenbeurszaal',
        'start': datetime(2017, 6, 13, 15, 0),
        'end': datetime(2017, 6, 13, 15, 50),
        'tags': ['serverless']
    },
    'Simplifying Container Management with Habitat': {
        'speakers': ['Michael Ducy'],
        'track': 'Cloud Native',
        'location': 'Effectenbeurszaal',
        'start': datetime(2017, 6, 13, 16, 10),
        'end': datetime(2017, 6, 13, 17, 0),
        'tags': ['containers', 'scalability']
    },
    # Unhackable
    'Applied Microservice Security': {
        'speakers': ['Adrian Mouat'],
        'track': 'Unhackable',
        'location': 'Graanbeurszaal',
        'start': datetime(2017, 6, 13, 10, 10),
        'end': datetime(2017, 6, 13, 11, 0),
        'tags': ['microservices', 'security']
    },
    'Blockchain: The Slowest (and most fascinating) Database in the World': {
        'speakers': ['Stefan Tilkov'],
        'track': 'Unhackable',
        'location': 'Graanbeurszaal',
        'start': datetime(2017, 6, 13, 11, 10),
        'end': datetime(2017, 6, 13, 12, 0),
        'tags': ['blockchain', 'bitcoins', 'cryptocurrency']
    },
    'Code as Risk': {
        'speakers': ['Kevlin Henney'],
        'track': 'Unhackable',
        'location': 'Graanbeurszaal',
        'start': datetime(2017, 6, 13, 14, 0),
        'end': datetime(2017, 6, 13, 14, 50),
        'tags': ['risk', 'development practices']
    },
    'Building Layers of Defense with Spring Security': {
        'speakers': ['Joris Kuipers'],
        'track': 'Unhackable',
        'location': 'Graanbeurszaal',
        'start': datetime(2017, 6, 13, 15, 0),
        'end': datetime(2017, 6, 13, 15, 50),
        'tags': ['spring', 'security', 'java']
    },
    'Security in the Delivery Pipeline': {
        'speakers': ['James Wickett'],
        'track': 'Unhackable',
        'location': 'Graanbeurszaal',
        'start': datetime(2017, 6, 13, 16, 10),
        'end': datetime(2017, 6, 13, 17, 0),
        'tags': ['security', 'delivery']
    },
    # IT & Society
    'When the \'Truth\' no Longer Matters': {
        'speakers': ['Kate Gray'],
        'track': 'IT & Society',
        'location': 'Administratiezaal',
        'start': datetime(2017, 6, 13, 10, 10),
        'end': datetime(2017, 6, 13, 11, 0),
        'tags': ['critical thinking']
    },
    'Teaching Children about Clean Code': {
        'speakers': ['Felienne Hermans'],
        'track': 'IT & Society',
        'location': 'Administratiezaal',
        'start': datetime(2017, 6, 13, 11, 10),
        'end': datetime(2017, 6, 13, 12, 0),
        'tags': ['clean code', 'critical thinking']
    },
    'Actually, It\'s About Ethics In Software Development': {
        'speakers': ['Jonathan Rothwell', 'Steve Freeman'],
        'track': 'IT & Society',
        'location': 'Administratiezaal',
        'start': datetime(2017, 6, 13, 14, 0),
        'end': datetime(2017, 6, 13, 14, 50),
        'tags': ['ethics', 'critical thinking']
    },
    'Moral Foundations Theory: Help in Overcoming Resistance': {
        'speakers': ['Linda Rising'],
        'track': 'IT & Society',
        'location': 'Administratiezaal',
        'start': datetime(2017, 6, 13, 15, 0),
        'end': datetime(2017, 6, 13, 15, 50),
        'tags': ['moral', 'critical thinking']
    },
    'How to Break the Rules': {
        'speakers': ['Dan North'],
        'track': 'IT & Society',
        'location': 'Administratiezaal',
        'start': datetime(2017, 6, 13, 16, 10),
        'end': datetime(2017, 6, 13, 17, 0),
        'tags': ['critical thinking']
    },
    # Machine Learning without a PhD
    'Deep Learning: What It Is and What It Can Do For You': {
        'speakers': ['Diogo Moitinho de Almeida'],
        'track': 'Machine Learning without a PhD',
        'location': 'Veilingzaal',
        'start': datetime(2017, 6, 13, 10, 10),
        'end': datetime(2017, 6, 13, 11, 0),
        'tags': ['deep learning', 'dl']
    },
    'Composing Bach Chorales Using Deep Learning': {
        'speakers': ['Feynman Liang'],
        'track': 'Machine Learning without a PhD',
        'location': 'Veilingzaal',
        'start': datetime(2017, 6, 13, 11, 10),
        'end': datetime(2017, 6, 13, 12, 0),
        'tags': ['deep learning', 'dl']
    },
    'Cloud-Native Data Science: Turning Data-Oriented Business Problems Into Scalable Solutions': {
        'speakers': ['Phil Winder'],
        'track': 'Machine Learning without a PhD',
        'location': 'Veilingzaal',
        'start': datetime(2017, 6, 13, 14, 0),
        'end': datetime(2017, 6, 13, 14, 50),
        'tags': ['cloud', 'cloud native', 'data science', 'scalability']
    },
    'Machine Learning with TensorFlow': {
        'speakers': ['Robert Saxby', 'Rokesh Jankie'],
        'track': 'Machine Learning without a PhD',
        'location': 'Veilingzaal',
        'start': datetime(2017, 6, 13, 15, 0),
        'end': datetime(2017, 6, 13, 15, 50),
        'tags': ['machine learning', 'ml', 'TensorFlow']
    },
    'Voicing Application with Amazon Polly': {
        'speakers': ['Rafal Kuklinski'],
        'track': 'Machine Learning without a PhD',
        'location': 'Veilingzaal',
        'start': datetime(2017, 6, 13, 16, 10),
        'end': datetime(2017, 6, 13, 17, 0),
        'tags': ['amazon', 'polly', 'voice']
    },
    # Solutions Tuesday
    'Angular 2 All the Way': {
        'speakers': ['Henk Bakker', 'Rachel Heimbach'],
        'track': 'Solutions Tuesday',
        'location': 'Keurzaal',
        'start': datetime(2017, 6, 13, 10, 10),
        'end': datetime(2017, 6, 13, 11, 0),
        'tags': ['angular', 'javascript']
    },
    'The Web, Lies, and Videotape': {
        'speakers': ['Jan-Jaap Oosterwijk', 'Scott Seligman'],
        'track': 'Solutions Tuesday',
        'location': 'Keurzaal',
        'start': datetime(2017, 6, 13, 11, 10),
        'end': datetime(2017, 6, 13, 12, 0),
        'tags': ['monitoring', 'P2P']
    },
    'It\'s Not Continuous Delivery If You Can\'t Deploy Right Now': {
        'speakers': ['Ken Mugrage'],
        'track': 'Solutions Tuesday',
        'location': 'Keurzaal',
        'start': datetime(2017, 6, 13, 14, 0),
        'end': datetime(2017, 6, 13, 14, 50),
        'tags': ['continuous delivery', 'scalability']
    },
    'Microservices Without Servers': {
        'speakers': ['Glynn Bird'],
        'track': 'Solutions Tuesday',
        'location': 'Keurzaal',
        'start': datetime(2017, 6, 13, 15, 0),
        'end': datetime(2017, 6, 13, 15, 50),
        'tags': ['microservices']
    },
    'Blockchain for Developers': {
        'speakers': ['Peter Penning', 'Cees van Wijk'],
        'track': 'Solutions Tuesday',
        'location': 'Keurzaal',
        'start': datetime(2017, 6, 13, 16, 10),
        'end': datetime(2017, 6, 13, 17, 0),
        'tags': ['blockchain']
    },
    # Microservices: Legacy of the Future
    'Why the Fuss about Serverless': {
        'speakers': ['Simon Wardley'],
        'track': 'Microservices: Legacy of the Future',
        'location': 'Effectenbeurszaal',
        'start': datetime(2017, 6, 14, 10, 10),
        'end': datetime(2017, 6, 14, 11, 0),
        'tags': ['serverless']
    },
    'Pragmatic Microservices for Organisational Scalability': {
        'speakers': ['Friso van Vollenhoven'],
        'track': 'Microservices: Legacy of the Future',
        'location': 'Effectenbeurszaal',
        'start': datetime(2017, 6, 14, 11, 10),
        'end': datetime(2017, 6, 14, 12, 0),
        'tags': ['microservices', 'scalability']
    },
    'IoT & Microservices in the Home - Technical Marriage Made in Heaven': {
        'speakers': ['Fred George'],
        'track': 'Microservices: Legacy of the Future',
        'location': 'Effectenbeurszaal',
        'start': datetime(2017, 6, 14, 14, 0),
        'end': datetime(2017, 6, 14, 14, 50),
        'tags': ['microservices', 'IoT']
    },
    'Resilience Engineering in a Microservice Landscape': {
        'speakers': ['Maurice Zeijen'],
        'track': 'Microservices: Legacy of the Future',
        'location': 'Effectenbeurszaal',
        'start': datetime(2017, 6, 14, 15, 0),
        'end': datetime(2017, 6, 14, 15, 50),
        'tags': ['microservices', 'resilience']
    },
    'Rethinking Microservices with Stateful Streams': {
        'speakers': ['Ben Stopford'],
        'track': 'Microservices: Legacy of the Future',
        'location': 'Effectenbeurszaal',
        'start': datetime(2017, 6, 14, 16, 10),
        'end': datetime(2017, 6, 14, 17, 0),
        'tags': ['microservices']
    },
    # Herding Cats: Inclusive Collaboration
    'Politics & Hierarchy: How We Create It & How to Stop': {
        'speakers': ['Katherine Kirk'],
        'track': 'Herding Cats: Inclusive Collaboration',
        'location': 'Graanbeurszaal',
        'start': datetime(2017, 6, 14, 10, 10),
        'end': datetime(2017, 6, 14, 11, 0),
        'tags': ['critical thinking']
    },
    'Top 7 Agile Tips I learnt as a Product Manager': {
        'speakers': ['Benjamin Mitchell'],
        'track': 'Herding Cats: Inclusive Collaboration',
        'location': 'Graanbeurszaal',
        'start': datetime(2017, 6, 14, 11, 10),
        'end': datetime(2017, 6, 14, 12, 0),
        'tags': ['critical thinking', 'agile']
    },
    'How to Win Hearts & Minds - The Lessons Learned from Electoral Politics': {
        'speakers': ['Kate Gray', 'Chris Young'],
        'track': 'Herding Cats: Inclusive Collaboration',
        'location': 'Graanbeurszaal',
        'start': datetime(2017, 6, 14, 14, 0),
        'end': datetime(2017, 6, 14, 14, 50),
        'tags': ['critical thinking', 'politics']
    },
    'Team Sense-making with Organizational Constellations': {
        'speakers': ['Andrea Provaglio'],
        'track': 'Herding Cats: Inclusive Collaboration',
        'location': 'Graanbeurszaal',
        'start': datetime(2017, 6, 14, 15, 0),
        'end': datetime(2017, 6, 14, 15, 50),
        'tags': ['critical thinking']
    },
    'The Tech Industry needs all Kinds of Minds - so how do we Support Them?': {
        'speakers': ['Sallyann Freudenberg'],
        'track': 'Herding Cats: Inclusive Collaboration',
        'location': 'Graanbeurszaal',
        'start': datetime(2017, 6, 14, 16, 10),
        'end': datetime(2017, 6, 14, 17, 0),
        'tags': ['critical thinking', 'collaboration']
    },
    # Programming Languages
    'Develop Your Development Automation': {
        'speakers': ['Jessica Kerr'],
        'track': 'Programming Languages',
        'location': 'Administratiezaal',
        'start': datetime(2017, 6, 14, 10, 10),
        'end': datetime(2017, 6, 14, 11, 0),
        'tags': ['rug', 'automation', 'atomist']
    },
    'Real World Java 9': {
        'speakers': ['Trisha Gee'],
        'track': 'Programming Languages',
        'location': 'Administratiezaal',
        'start': datetime(2017, 6, 14, 11, 10),
        'end': datetime(2017, 6, 14, 12, 0),
        'tags': ['java', 'jigsaw']
    },
    'Kotlin - Ready for Production': {
        'speakers': ['Hadi Hariri'],
        'track': 'Programming Languages',
        'location': 'Administratiezaal',
        'start': datetime(2017, 6, 14, 14, 0),
        'end': datetime(2017, 6, 14, 14, 50),
        'tags': ['kotlin']
    },
    'CSS vs. JavaScript, Trust vs. Control': {
        'speakers': ['Chris Heilmann'],
        'track': 'Programming Languages',
        'location': 'Administratiezaal',
        'start': datetime(2017, 6, 14, 15, 0),
        'end': datetime(2017, 6, 14, 15, 50),
        'tags': ['css', 'javascript']
    },
    'JavaScript at Uber': {
        'speakers': ['Dustin Whittle'],
        'track': 'Programming Languages',
        'location': 'Administratiezaal',
        'start': datetime(2017, 6, 14, 16, 10),
        'end': datetime(2017, 6, 14, 17, 0),
        'tags': ['javascript', 'uber']
    },
    # Cyber-Physical Systems
    'Hacking the Internet of Things for Fun & Profit': {
        'speakers': ['Ruben van Vreeland'],
        'track': 'Cyber-Physical Systems',
        'location': 'Veilingzaal',
        'start': datetime(2017, 6, 14, 10, 10),
        'end': datetime(2017, 6, 14, 11, 0),
        'tags': ['IoT']
    },
    'Internet of Healthcare Things - A Platform Approach': {
        'speakers': ['Poorna Kallare'],
        'track': 'Cyber-Physical Systems',
        'location': 'Veilingzaal',
        'start': datetime(2017, 6, 14, 11, 10),
        'end': datetime(2017, 6, 14, 12, 0),
        'tags': ['IoT', 'health']
    },
    'REST no more - Using Actors for the Internet of (LEGO) Trains & Raspberry Pis': {
        'speakers': ['Johan Janssen'],
        'track': 'Cyber-Physical Systems',
        'location': 'Veilingzaal',
        'start': datetime(2017, 6, 14, 14, 0),
        'end': datetime(2017, 6, 14, 14, 50),
        'tags': ['IoT', 'raspberryPi', 'LEGO', 'akka', 'trains']
    },
    'A Gentle introduction to IoT protocols: MQTT, CoAP, HTTP & WebSockets': {
        'speakers': ['Antonio Almeida', 'Jaime Gonzalez-Arintero Berciano'],
        'track': 'Cyber-Physical Systems',
        'location': 'Veilingzaal',
        'start': datetime(2017, 6, 14, 15, 0),
        'end': datetime(2017, 6, 14, 15, 50),
        'tags': ['IoT', 'MQTT', 'CoAP']
    },
    'Visualizing IoT Data with Minecraft': {
        'speakers': ['Lars Gregori'],
        'track': 'Cyber-Physical Systems',
        'location': 'Veilingzaal',
        'start': datetime(2017, 6, 14, 16, 10),
        'end': datetime(2017, 6, 14, 17, 0),
        'tags': ['IoT', 'minecraft']
    },
    # Solutions Wednesday
    'Machine Learning, Your First Steps': {
        'speakers': ['David Stibbe'],
        'track': 'Solutions Wednesday',
        'location': 'Keurzaal',
        'start': datetime(2017, 6, 14, 10, 10),
        'end': datetime(2017, 6, 14, 11, 0),
        'tags': ['machine learning', 'ml']
    },
    'How Do You Apply Machine Learning to Deliver New Functionality For a Complex Application Given Limited Time?': {
        'speakers': ['Attila Houtkooper', 'Torec Luik'],
        'track': 'Solutions Wednesday',
        'location': 'Keurzaal',
        'start': datetime(2017, 6, 14, 11, 10),
        'end': datetime(2017, 6, 14, 12, 0),
        'tags': ['machine learning', 'ml']
    },
    'Feel the Hum of Your System': {
        'speakers': ['Kresten Krab Thorup'],
        'track': 'Solutions Wednesday',
        'location': 'Keurzaal',
        'start': datetime(2017, 6, 14, 14, 0),
        'end': datetime(2017, 6, 14, 14, 50),
        'tags': ['hum', 'monitoring']
    },
    'Alexa Voice Service: Under the Hood': {
        'speakers': ['Rafal Kuklinski'],
        'track': 'Solutions Wednesday',
        'location': 'Keurzaal',
        'start': datetime(2017, 6, 14, 15, 0),
        'end': datetime(2017, 6, 14, 15, 50),
        'tags': ['amazon', 'alexa', 'voice']
    },
    'Enterprise Fast Lane - Transforming to Microservices in the Cloud': {
        'speakers': ['Christian Deger'],
        'track': 'Solutions Wednesday',
        'location': 'Keurzaal',
        'start': datetime(2017, 6, 14, 16, 10),
        'end': datetime(2017, 6, 14, 17, 0),
        'tags': ['microservices', 'cloud']
    }
}
