import uvicorn
from fastapi import FastAPI
#----------------------------------------------------------------

app = FastAPI()

@app.get('/')
def fn_fast_api():

# -------  INSERER VOTRE CODE ICI -----------------
    
    return {
  "postures": [
    {
      "id": 1,
      "nom": "La posture de la montagne – Tadasana",
      "image": "https://www.ataraksy.com/wp-content/uploads/2019/02/La-posture-de-la-montagne-tadasana.jpg",
      "video": "https://www.ataraksy.com/yoga-debutant-10-postures-maitriser/",
      "description": "Debout, elle vous apprend à être bien stable et à ressentir la terre sous vos pieds. La posture de la montagne peut sembler assez simple et on est tenté de se dire qu’on « simplement debout », mais en fait ce n’est pas aussi simple que cela et les débutants devraient vite s’en rendre compte.",
      "instructions": "Commencez par vous tenir debout, les pieds joints. Enfoncez vos dix orteils dans le sol tout en les écartant. Engagez vos quadriceps pour relever vos genoux. Rentrez et remontez vos abdominaux en soulevant votre poitrine et en rentrant vos épaules. Sentez vos omoplates venir l’une vers l’autre et ouvrez votre poitrine. Faites attention de bien garder vos paumes vers l’intérieur, face à votre corps. Ensuite, imaginez une corde tirant votre tête vers le plafond en inspirant profondément. Tenez la posture pendant 5 à 8 respirations."
    },
    {
      "id": 2,
      "nom": "Posture du chien tête en bas",
      "image": "https://www.ataraksy.com/wp-content/uploads/2019/02/posture-du-chien-tête-en-bas.jpg",
      "video": "https://www.ataraksy.com/yoga-debutant-10-postures-maitriser/",
      "description": "Cette posture étire le dos, les épaules, les ischio-jambiers et les mollets tout en renforçant les bras et les jambes.",
      "instructions": "Commencez à quatre pattes, les mains alignées avec les épaules et les genoux avec les hanches. Écartez les doigts et appuyez fermement dans vos paumes. Soulevez vos hanches vers le plafond en redressant vos jambes autant que possible. Gardez votre tête entre vos bras, les oreilles alignées avec vos bras. Maintenez la posture en respirant profondément pendant 5 à 8 respirations."
    },
    {
      "id": 3,
      "nom": "Posture de la planche en yoga – Kumbhakasana",
      "image": "https://www.ataraksy.com/wp-content/uploads/2019/02/posture-de-la-planche-en-yoga-Kumbhakâsana-dandâsana.jpg",
      "video": "https://www.ataraksy.com/yoga-debutant-10-postures-maitriser/",
      "description": "Cette posture renforce les bras, les épaules, le dos et les muscles abdominaux.",
      "instructions": "Commencez en position de chien tête en bas. Déplacez votre poids vers l'avant pour que vos épaules soient alignées avec vos poignets. Gardez votre corps en ligne droite de la tête aux talons. Engagez vos abdominaux et maintenez la posture en respirant profondément pendant 5 à 8 respirations."
    },
    {
      "id": 4,
      "nom": "La posture du triangle en yoga – Trikonasana",
      "image": "https://www.ataraksy.com/wp-content/uploads/2019/02/la-posture-du-triangle-en-yoga-Trikonâsana.jpg",
      "video": "https://www.ataraksy.com/yoga-debutant-10-postures-maitriser/",
      "description": "Cette posture étire les jambes, les hanches, la colonne vertébrale et les épaules.",
      "instructions": "Commencez en position debout, les pieds écartés. Tournez votre pied droit vers l'extérieur et votre pied gauche légèrement vers l'intérieur. Étendez vos bras à la hauteur des épaules. Inclinez votre torse vers la droite, en posant votre main droite sur votre cheville, votre tibia ou le sol, et étendez votre bras gauche vers le plafond. Gardez vos deux jambes tendues et regardez vers votre main gauche. Maintenez la posture pendant 5 à 8 respirations, puis changez de côté."
    },
    {
      "id": 5,
      "nom": "La posture de l’arbre en yoga – Vrksasana",
      "image": "https://www.ataraksy.com/wp-content/uploads/2019/02/La-posture-de-l’arbre-en-yoga.jpg",
      "video": "https://www.ataraksy.com/yoga-debutant-10-postures-maitriser/",
      "description": "Cette posture améliore l'équilibre et renforce les muscles des jambes.",
      "instructions": "Commencez en position debout, les pieds joints. Déplacez votre poids sur votre pied gauche et placez la plante de votre pied droit contre votre cuisse gauche, en évitant le genou. Joignez vos mains devant votre poitrine ou étendez-les vers le plafond. Maintenez votre regard fixé sur un point fixe devant vous pour garder l'équilibre. Tenez la posture pendant 5 à 8 respirations, puis changez de côté."
    },
    {
      "id": 6,
      "nom": "La posture du guerrier 1 en yoga – Virabhadrasana I",
      "image": "https://www.ataraksy.com/wp-content/uploads/2019/02/La-posture-du-guerrier-1-en-yoga-Virabhadrâsana-I.jpg",
      "video": "https://www.ataraksy.com/yoga-debutant-10-postures-maitriser/",
      "description": "Cette posture renforce les jambes, les hanches, les épaules et le dos.",
      "instructions": "Commencez en position debout, les pieds écartés de la largeur des hanches. Faites un grand pas en arrière avec votre pied gauche et tournez-le légèrement vers l'intérieur. Pliez votre genou droit à 90 degrés en gardant votre genou au-dessus de votre cheville. Levez vos bras vers le plafond, les paumes se faisant face. Gardez vos hanches tournées vers l'avant. Maintenez la posture pendant 5 à 8 respirations, puis changez de côté."
    },
    {
      "id": 7,
      "nom": "La posture du guerrier 2 – Virabhadrasana II",
      "image": "https://www.ataraksy.com/wp-content/uploads/2019/02/La-posture-du-guerrier-2-Virabhadrâsana-II.jpg",
      "video": "https://www.ataraksy.com/yoga-debutant-10-postures-maitriser/",
      "description": "Cette posture renforce les jambes et les épaules tout en améliorant l'endurance.",
      "instructions": "Commencez en position debout, les pieds écartés. Tournez votre pied droit vers l'extérieur et votre pied gauche légèrement vers l'intérieur. Pliez votre genou droit à 90 degrés en gardant votre genou au-dessus de votre cheville. Étendez vos bras à la hauteur des épaules, paumes vers le bas. Regardez par-dessus votre main droite. Maintenez la posture pendant 5 à 8 respirations, puis changez de côté."
    },
    {
      "id": 8,
      "nom": "La posture penchée en avant, assis",
      "image": "https://www.ataraksy.com/wp-content/uploads/2019/02/La-posture-penchée-en-avant-assis.jpg",
      "video": "https://www.ataraksy.com/yoga-debutant-10-postures-maitriser/",
      "description": "Cette posture étire le dos, les épaules et les jambes tout en calmant l'esprit.",
      "instructions": "Asseyez-vous avec les jambes étendues devant vous. Inspirez et allongez votre colonne vertébrale. En expirant, inclinez-vous vers l'avant depuis les hanches, en gardant le dos droit. Essayez d'attraper vos pieds ou vos chevilles. Relâchez la tête et respirez profondément pendant 5 à 8 respirations."
    },
    {
      "id": 9,
      "nom": "La posture du demi pont – Ardha Setu Bandhasana",
      "image": "https://www.ataraksy.com/wp-content/uploads/2019/02/La-posture-du-demi-pont-Ardha-setu-bandhâsana.jpg",
      "video": "https://www.ataraksy.com/yoga-debutant-10-postures-maitriser/",
      "description": "Cette posture renforce le dos, les cuisses et les fessiers tout en ouvrant la poitrine.",
      "instructions": "Allongez-vous sur le dos, les genoux pliés et les pieds à plat sur le sol. Placez vos bras le long de votre corps, les paumes vers le bas. En inspirant, soulevez vos hanches vers le plafond en appuyant sur vos pieds. Tenez la posture pendant 5 à 8 respirations, puis redescendez lentement."
    },
    {
      "id": 10,
      "nom": "La posture de l’enfant – Balasana",
      "image": "https://www.ataraksy.com/wp-content/uploads/2019/02/La-posture-de-l’enfant-Bālāsana.jpg",
      "video": "https://www.ataraksy.com/yoga-debutant-10-postures-maitriser/",
      "description": "Cette posture repose les hanches, les cuisses et les chevilles tout en calmant l'esprit.",
      "instructions": "Commencez à quatre pattes, puis asseyez-vous sur vos talons. Inclinez votre torse vers l'avant et étendez vos bras devant vous ou le long de votre corps. Posez votre front sur le sol. Détendez-vous et respirez profondément pendant 5 à 8 respirations."
    },
    {
      "id": 11,
      "nom": "Posture du cobra en yoga ou aussi appelée Bhujangasana",
      "image": "https://www.ataraksy.com/wp-content/uploads/2019/02/Posture-du-cobra-en-yoga-ou-aussi-appelée-Bhujangasana-300x169.jpg",
      "video": "https://www.ataraksy.com/hatha-yoga-guide-debutant/",
      "description": "Cette posture renforce le dos et ouvre la poitrine, améliorant la flexibilité de la colonne vertébrale.",
      "instructions": "Allongez-vous sur le ventre, les mains sous les épaules. En inspirant, appuyez sur vos mains pour soulever votre poitrine du sol, en gardant les coudes légèrement pliés. Gardez vos épaules éloignées de vos oreilles. Maintenez la posture pendant 5 à 8 respirations."
    },
    {
      "id": 12,
      "nom": "Posture du bateau en yoga ou aussi Paripurna Navasana",
      "image": "https://www.ataraksy.com/wp-content/uploads/2019/02/Posture-du-bateau-en-yoga-ou-aussi-Paripurna-Navasana-300x232.jpg",
      "video": "https://www.ataraksy.com/hatha-yoga-guide-debutant/",
      "description": "Cette posture renforce les abdominaux, le dos et les hanches tout en améliorant l'équilibre.",
      "instructions": "Asseyez-vous avec les genoux pliés et les pieds à plat sur le sol. Penchez-vous légèrement en arrière et soulevez vos pieds du sol, en gardant les genoux pliés. Étendez vos bras devant vous, parallèles au sol. Maintenez la posture pendant 5 à 8 respirations."
    },
    {
      "id": 13,
      "nom": "Posture de la libération des vents en yoga ou Pawanmuktasana",
      "image": "https://www.ataraksy.com/wp-content/uploads/2019/02/Posture-de-la-libération-des-vents-en-yoga-ou-Pawanmuktasana-300x182.jpg",
      "video": "https://www.ataraksy.com/hatha-yoga-guide-debutant/",
      "description": "Cette posture aide à soulager les gaz et améliore la digestion.",
      "instructions": "Allongez-vous sur le dos et ramenez vos genoux vers votre poitrine. Entourez vos genoux avec vos bras et pressez doucement vos cuisses contre votre abdomen. Maintenez la posture pendant 5 à 8 respirations."
    },
    {
      "id": 14,
      "nom": "Posture de la planche en yoga aussi appelée Kumbhakasana",
      "image": "https://www.ataraksy.com/wp-content/uploads/2019/02/posture-de-la-planche-en-yoga-aussi-appelée-Kumbhakâsana-dandâsana-300x198.jpg",
      "video": "https://www.ataraksy.com/hatha-yoga-guide-debutant/",
      "description": "Cette posture renforce les bras, les épaules, le dos et les muscles abdominaux.",
      "instructions": "Commencez en position de chien tête en bas. Déplacez votre poids vers l'avant pour que vos épaules soient alignées avec vos poignets. Gardez votre corps en ligne droite de la tête aux talons. Engagez vos abdominaux et maintenez la posture en respirant profondément pendant 5 à 8 respirations."
    },
    {
      "id": 15,
      "nom": "Posture de l'arc en yoga – Dhanurasana",
      "image": "https://www.ataraksy.com/wp-content/uploads/2019/02/posture-de-larc-en-yoga-300x178.jpeg",
      "video": "https://www.ataraksy.com/hatha-yoga-guide-debutant/",
      "description": "Cette posture renforce le dos et les jambes tout en ouvrant la poitrine et les épaules.",
      "instructions": "Allongez-vous sur le ventre, pliez vos genoux et attrapez vos chevilles avec vos mains. En inspirant, soulevez votre poitrine et vos cuisses du sol, en tirant vos pieds vers le haut. Maintenez la posture pendant 5 à 8 respirations."
    },
    {
      "id": 16,
      "nom": "Posture de yoga Chaturanga Dandasana",
      "image": "https://www.ataraksy.com/wp-content/uploads/2019/02/posture-de-yoga-Chaturanga-Dandasana-300x135.jpg",
      "video": "https://www.ataraksy.com/vinyasa-yoga-guide-debutants/",
      "description": "Cette posture renforce les bras, les épaules et le tronc.",
      "instructions": "Commencez en position de planche. Pliez les coudes à 90 degrés en les gardant près du corps et abaissez-vous jusqu'à ce que vos bras soient parallèles au sol. Maintenez la posture pendant 5 à 8 respirations."
    },
    {
      "id": 17,
      "nom": "Pose yoga Utpluthih",
      "image": "https://www.ataraksy.com/wp-content/uploads/2019/02/pose-yoga-utpluthih-300x200.jpg",
      "video": "https://www.ataraksy.com/vinyasa-yoga-guide-debutants/",
      "description": "Cette posture renforce les bras, les épaules et les abdominaux.",
      "instructions": "Asseyez-vous en position du lotus, les jambes croisées. Placez vos mains sur le sol à côté de vos hanches. En inspirant, appuyez sur vos mains pour soulever votre corps du sol. Maintenez la posture pendant 5 à 8 respirations."
    },
    {
      "id": 18,
      "nom": "Posture du bateau en yoga ou aussi Paripurna Navasana",
      "image": "https://www.ataraksy.com/wp-content/uploads/2019/02/Posture-du-bateau-en-yoga-ou-aussi-Paripurna-Navasana-300x232.jpg",
      "video": "https://www.ataraksy.com/vinyasa-yoga-guide-debutants/",
      "description": "Cette posture renforce les abdominaux, le dos et les hanches tout en améliorant l'équilibre.",
      "instructions": "Asseyez-vous avec les genoux pliés et les pieds à plat sur le sol. Penchez-vous légèrement en arrière et soulevez vos pieds du sol, en gardant les genoux pliés. Étendez vos bras devant vous, parallèles au sol. Maintenez la posture pendant 5 à 8 respirations."
    },
    {
      "id": 19,
      "nom": "Yoga chandelle – Sarvangasana",
      "image": "https://www.ataraksy.com/wp-content/uploads/2019/02/yoga_chandelle_sarvangasana-300x223.png",
      "video": "https://www.ataraksy.com/vinyasa-yoga-guide-debutants/",
      "description": "Cette posture améliore la circulation sanguine et apaise le système nerveux.",
      "instructions": "Allongez-vous sur le dos et soulevez vos jambes vers le plafond. Utilisez vos mains pour soutenir votre dos et soulevez vos hanches du sol. Gardez votre corps aligné et vos pieds pointés vers le plafond. Maintenez la posture pendant 5 à 8 respirations."
    },
    {
      "id": 20,
      "nom": "Femme faisant du yoga dans une salle sur son tapis",
      "image": "https://www.ataraksy.com/wp-content/uploads/2019/02/femme-faisant-du-yoga-dans-une-salle-sur-son-tapis-1024x682.jpg",
      "video": "https://www.ataraksy.com/vinyasa-yoga-guide-debutants/",
      "description": "Cette image montre une femme pratiquant diverses postures de yoga sur son tapis dans une salle dédiée.",
      "instructions": "Suivez les instructions de votre professeur de yoga pour enchaîner les postures correctement et en toute sécurité."
    },
    {
      "id": 21,
      "nom": "Bannière dailylamashop",
      "image": "https://www.ataraksy.com/wp-content/uploads/2020/04/Bannière-dailylamashop.jpg",
      "video": "https://www.ataraksy.com/vinyasa-yoga-guide-debutants/",
      "description": "Cette bannière promotionnelle présente des produits liés à la pratique du yoga disponibles sur Dailylama Shop.",
      "instructions": "Visitez le site web pour découvrir et acheter des produits de yoga."
    },
    {
      "id": 22,
      "nom": "Posture de la tortue – Kurmasana",
      "image": "https://www.ataraksy.com/wp-content/uploads/2019/03/posture-de-la-tortue-kurmasana-1024x576.jpg",
      "video": "https://www.ataraksy.com/ashtanga-yoga-guide-debutants/",
      "description": "Cette posture étire profondément le dos, les hanches et les épaules.",
      "instructions": "Asseyez-vous avec les jambes écartées. Penchez-vous vers l'avant et passez vos bras sous vos genoux. Étendez vos bras sur les côtés et allongez votre torse vers le sol. Maintenez la posture pendant 5 à 8 respirations."
    },
    {
      "id": 23,
      "nom": "Pose yoga Utpluthih",
      "image": "https://www.ataraksy.com/wp-content/uploads/2019/02/pose-yoga-utpluthih.jpg",
      "video": "https://www.ataraksy.com/kundalini-yoga-guide-debutants/",
      "description": "Cette posture renforce les bras, les épaules et les abdominaux.",
      "instructions": "Asseyez-vous en position du lotus, les jambes croisées. Placez vos mains sur le sol à côté de vos hanches. En inspirant, appuyez sur vos mains pour soulever votre corps du sol. Maintenez la posture pendant 5 à 8 respirations."
    },
    {
      "id": 24,
      "nom": "Bannière dailylamashop",
      "image": "https://www.ataraksy.com/wp-content/uploads/2020/04/Bannière-dailylamashop.jpg",
      "video": "https://www.ataraksy.com/kundalini-yoga-guide-debutants/",
      "description": "Cette bannière promotionnelle présente des produits liés à la pratique du yoga disponibles sur Dailylama Shop.",
      "instructions": "Visitez le site web pour découvrir et acheter des produits de yoga."
    }
  ]
}


# ---------------- FIN DE TON CODE ----------------
#__________________________________________________

if __name__ == '__main__':
    uvicorn.run(app, port=8000, host='0.0.0.0')