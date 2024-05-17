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
        "nom": "La posture du cobra – Bhujangasana",
        "image": "https://www.ataraksy.com/wp-content/uploads/2019/02/Posture-du-cobra-en-yoga-ou-aussi-appel%C3%A9e-Bhujangasana-696x392.jpg",
        "description": "Pour pouvoir la réaliser, vous allez devoir vous allonger sur le ventre en tendant bien vos jambes. Ensuite, il vous faudra placer vos paumes de main sur le sol, juste en dessous de vos épaules. Lorsque vous prendrez une inspiration, vous allez devoir soulever doucement votre poitrine, puis tenir la position pendant deux respirations. Par la suite, il vous faudra redescendre votre buste au sol pendant que vous expirez.",
        "instructions": "Allongez-vous à plat ventre sur un tapis de yoga. Joignez les pieds et posez vos paumes de main sur le sol au niveau de vos épaules, en pointant les doigts vers l’avant et en gardant les coudes près du corps. Posez votre front sur le sol. En inspirant, étirez le menton vers l’avant puis levez et faites basculer votre tête en arrière tout en ouvrant la poitrine et en poussant le torse vers l’avant. Soulevez votre torse sans utiliser vos mains.",
        "niveau": "débutant"
    },
    {
        "id": 2,
        "nom": "La posture du bateau – Paripurna-navâsana",
        "image": "https://www.ataraksy.com/wp-content/uploads/2019/02/Posture-du-bateau-en-yoga-ou-aussi-Paripurna-Navasana-543x420.jpg",
        "description": "La posture du bateau fait partie des incontournables du Hatha Yoga et elle commence allongé sur le dos avec les jambes tendues. Lors de la première inspiration, vous allez devoir lever les jambes, tout en veillant bien à les garder tendues. Par la suite, il vous faudra attraper vos mollets avec vos mains en veillant à garder le dos bien droit.",
        "instructions": "Allongez-vous sur le dos, jambes tendues. Inspirez et levez les jambes en les gardant tendues. Attrapez vos mollets avec vos mains, gardez le dos droit. Assurez-vous que votre corps forme un 'V'. Maintenez cette position pendant plusieurs respirations.",
        "niveau": "intermédiaire"
    },
    {
        "id": 3,
        "nom": "La posture de la libération des vents – Pavanamuktasana",
        "image": "https://www.ataraksy.com/wp-content/uploads/2019/02/Posture-de-la-lib%C3%A9ration-des-vents-en-yoga-ou-Pawanmuktasana-693x420.jpg",
        "description": "Encore une fois, vous allez devoir vous allonger sur le dos. Il vous faudra ensuite ramener vos genoux au niveau de votre poitrine en faisant une pression sur votre ventre. Pendant que vous prenez une expiration, vous allez devoir essayer de toucher vos genoux à l’aide de votre menton.",
        "instructions": "Allongez-vous sur le dos. Ramenez vos genoux vers votre poitrine, en appliquant une légère pression sur votre ventre. En expirant, essayez de toucher vos genoux avec votre menton. Maintenez cette position pendant quelques respirations.",
        "niveau": "débutant"
    },
    {
        "id": 4,
        "nom": "La posture de la planche – Kumbhakâsana-dandâsana",
        "image": "https://www.ataraksy.com/wp-content/uploads/2019/02/posture-de-la-planche-en-yoga-aussi-appel%C3%A9e-Kumbhak%C3%A2sana-dand%C3%A2sana-635x420.jpg",
        "description": "Cette fois-ci, il faudra vous allonger sur le ventre et poser vos mains de chaque côté des épaules. Ensuite, il vous faudra pousser sur vos mains pour relever votre corps. L’objectif est de rester aussi droit que possible en formant une ligne avec tout son corps.",
        "instructions": "Allongez-vous sur le ventre, placez vos mains de chaque côté des épaules. Poussez sur vos mains pour relever votre corps. Gardez votre corps aussi droit que possible, formant une ligne droite de la tête aux pieds. Maintenez cette position pendant plusieurs respirations.",
        "niveau": "intermédiaire"
    },
    {
        "id": 5,
        "nom": "La posture de l’arc – Dhanurasana",
        "image": "https://www.ataraksy.com/wp-content/uploads/2019/02/posture-de-larc-en-yoga.jpeg",
        "description": "Cette posture du Hatha Yoga demande également de s’allonger sur le ventre. Une fois au sol, il faudra plier vos genoux afin de pouvoir attraper vos chevilles avec vos mains. Tout en inspirant, vous allez relever la tête et regarder droit devant vous.",
        "instructions": "Allongez-vous sur le ventre. Pliez vos genoux et attrapez vos chevilles avec vos mains. En inspirant, relevez la tête et regardez droit devant vous. Maintenez cette position en respirant profondément.",
        "niveau": "intermédiaire"
    },
    {
        "id": 6,
        "nom": "La posture de la pompe – Chaturanga Dandasana",
        "image": "https://www.ataraksy.com/wp-content/uploads/2019/02/posture-de-yoga-Chaturanga-Dandasana-300x135.jpg",
        "description": "Appelée familièrement « posture de la pompe » ou « position du bâton », cette position fait partie intégrante du Vinyasa yoga. Pour la réaliser, il faudra commencer par se mettre dans la position du chien tête en bas puis faire la posture de la planche. Il faudra inspirer et expirer en baissant son corps vers le sol. Le corps se devra d’être parallèle au sol tout en gardant les jambes droites.",
        "instructions": "Commencez en position de chien tête en bas. Passez à la posture de la planche. Inspirez et abaissez votre corps vers le sol, en gardant votre corps parallèle au sol et les jambes droites. Maintenez cette position en respirant profondément.",
        "niveau": "avancé"
    },
    {
        "id": 7,
        "nom": "La posture Utpluthih",
        "image": "https://www.ataraksy.com/wp-content/uploads/2019/02/pose-yoga-utpluthih-300x200.jpg",
        "description": "Cette position peut demander un certain niveau en termes de pratique du yoga, mais elle n’en reste pas moins bénéfique. Pour commencer, il faudra prendre la position du lotus et placer ses mains au sol au niveau de chacune de ses hanches. En expirant, il faudra pousser avec ses mains sur le sol, puis soulever ses jambes et ses fesses vers le haut.",
        "instructions": "Asseyez-vous en position du lotus. Placez vos mains au sol au niveau de vos hanches. En expirant, poussez avec vos mains sur le sol et soulevez vos jambes et vos fesses vers le haut. Maintenez cette position en respirant profondément.",
        "niveau": "avancé"
    },
    {
        "id": 8,
        "nom": "La posture du bateau – Paripurna-navâsana",
        "image": "https://www.ataraksy.com/wp-content/uploads/2019/02/Posture-du-bateau-en-yoga-ou-aussi-Paripurna-Navasana-300x232.jpg",
        "description": "Pour débuter la posture du bateau, il faut tout d’abord s’asseoir au sol, sur ses ischions. Tout en serrant le périnée, il faudra abaisser ses omoplates puis attraper ses mollets en passant ses bras en dessous des cuisses. Par la suite, il vous sera demandé de lâcher vos mains, de mettre vos bras parallèles au sol, puis de tendre sur vos jambes et d’étirer vos pieds.",
        "instructions": "Asseyez-vous sur vos ischions. Répartissez équitablement votre poids entre vos deux fesses. Serrez le périnée et abaissez vos omoplates. Attrapez vos mollets en passant vos bras sous vos cuisses. Lâchez vos mains et mettez vos bras parallèles au sol. Tendez vos jambes et étirez vos pieds. Maintenez cette position en respirant profondément.",
        "niveau": "intermédiaire"
    },
    {
        "id": 9,
        "nom": "La posture de la chandelle – Salamba Sarvangasana",
        "image": "https://www.ataraksy.com/wp-content/uploads/2019/02/yoga_chandelle_sarvangasana-300x223.png",
        "description": "Appelée également posture sur les épaules, cette position vous demandera de lever votre buste et vos jambes en l’air, tout en collant votre sternum au niveau de votre menton. Le dos sera soutenu avec les mains et les coudes seront bien ancrés dans le sol. Le but est de se tenir le plus droit possible tout en étirant et en dynamisant ses jambes au maximum.",
        "instructions": "Allongez-vous sur le dos. Soulevez votre buste et vos jambes en l'air, en collant votre sternum contre votre menton. Soutenez votre dos avec vos mains et ancrez fermement vos coudes dans le sol. Étirez et dynamisez vos jambes au maximum. Maintenez cette position en respirant profondément.",
        "niveau": "avancé"
    },
    {
        "id": 10,
        "nom": "La posture du triangle – Trikonâsana",
        "image": "https://www.ataraksy.com/wp-content/uploads/2019/02/la-posture-du-triangle-en-yoga-Trikon%C3%A2sana.jpg",
        "description": "La posture du triangle, qui est réputée pour lutter contre le mal de dos, est très importante dans l’Ashtanga yoga. Avant toute chose, pour bien la préparer, un petit échauffement sera généralement de mise dans le but d’ouvrir votre taille et d’améliorer votre souplesse. Pour mettre en place cette posture, il vous sera demandé de vous mettre en position de la montagne avec les pieds joints. Par la suite, vous allez devoir expirer en écartant les pieds d’environ 1,50 m. Ensuite, vous allez devoir rentrer la pointe de votre pied gauche un peu vers la droite puis tourner votre autre pied de 90° vers l’extérieur. Tout au long de cette position, vos hanches doivent rester de face. Une fois que cela sera fait, vous pouvez expirer tout en étirant votre bassin est votre torse vers la droite, ainsi qu’en glissant votre main droite le long de votre jambe. Par la suite, étirez votre autre bras à la verticale.",
        "instructions": "Mettez-vous en position de la montagne avec les pieds joints. Expirez et écartez les pieds d’environ 1,50 m. Rentrez la pointe de votre pied gauche légèrement vers la droite puis tournez votre autre pied de 90° vers l’extérieur. Gardez vos hanches de face. Expirez en étirant votre bassin et votre torse vers la droite, en glissant votre main droite le long de votre jambe. Étirez votre autre bras à la verticale. Maintenez cette position en respirant profondément.",
        "niveau": "intermédiaire"
    },
    {
        "id": 11,
        "nom": "La posture du guerrier – Virabhadrâsana",
        "image": "https://www.ataraksy.com/wp-content/uploads/2019/02/La-posture-du-guerrier-1-en-yoga-Virabhadr%C3%A2sana-I.jpg",
        "description": "Cette position fait partie des incontournables de l’Ashtanga. Pour la mettre en place, vous allez devoir adopter la posture de la montagne. Cela consiste à se tenir debout et à garder ses pieds et ses talons joints. Il vous faudra poser vos mains sur vos hanches, puis écarter vos jambes d’une dizaine de centimètres. Par la suite, vous allez devoir faire un grand pas vers l’avant avec le pied droit afin de mettre une distance d’environ 1 m entre vos pieds. Votre jambe devra faire un angle droit et vous devrez rentrer votre coccyx. Au moment de l’inspiration, vous allez lever votre bras droit au-dessus de votre tête, puis vous joindrez vos mains paume à paume. Lors de l’expiration, vous devrez faire descendre votre bassin et fléchir votre jambe droite afin de former un angle droit. Ensuite, il faudra tourner votre pied gauche vers l’extérieur et tendre votre jambe. Par la suite, vous allez étirer votre colonne vertébrale en mettant vos bras vers le haut, tout en veillant à garder une bonne pression de vos mains placées l’une contre l’autre.",
        "instructions": "Adoptez la posture de la montagne, debout avec les pieds et les talons joints. Posez vos mains sur vos hanches et écartez vos jambes d’une dizaine de centimètres. Faites un grand pas vers l’avant avec le pied droit pour mettre une distance d’environ 1 m entre vos pieds. Formez un angle droit avec votre jambe droite et rentrez votre coccyx. Inspirez et levez votre bras droit au-dessus de votre tête, joignez vos mains paume à paume. Expirez en faisant descendre votre bassin et fléchissez votre jambe droite pour former un angle droit. Tournez votre pied gauche vers l’extérieur et tendez votre jambe gauche. Étirez votre colonne vertébrale en levant vos bras vers le haut, maintenez une bonne pression de vos mains l’une contre l’autre. Maintenez cette position en respirant profondément.",
        "niveau": "intermédiaire"
    },
    {
        "id": 12,
        "nom": "La posture de la chandelle – Salamba Sarvangasana",
        "image": "https://www.ataraksy.com/wp-content/uploads/2019/02/yoga_chandelle_sarvangasana.png",
        "description": "Dans la liste des positions incontournables de ce yoga, on retrouve la posture de la chandelle. Pour y parvenir, vous allez devoir vous allonger sur votre tapis de yoga en mettant le dos bien à plat. Il vous faudra ensuite joindre vos jambes, puis les lever à la verticale en gardant bien vos pieds joints et vos jambes tendues. Une fois que vos jambes seront en l’air, vous pourrez placer vos mains sous votre dos et décoller votre fessier du sol. Vos pieds et vos jambes doivent rester à la verticale tout au long de la posture. À noter que vos jambes ne doivent pas basculer en arrière.",
        "instructions": "Allongez-vous sur votre tapis de yoga avec le dos bien à plat. Joignez vos jambes et levez-les à la verticale en gardant vos pieds joints et vos jambes tendues. Placez vos mains sous votre dos et décollez votre fessier du sol. Vos pieds et vos jambes doivent rester à la verticale tout au long de la posture. Assurez-vous que vos jambes ne basculent pas en arrière. Maintenez cette position en respirant profondément.",
        "niveau": "avancé"
    },
    {
        "id": 13,
        "nom": "La posture du bateau – Paripurna-navâsana",
        "image": "https://www.ataraksy.com/wp-content/uploads/2019/02/Posture-du-bateau-en-yoga-ou-aussi-Paripurna-Navasana.jpg",
        "description": "La posture du bateau commence par le fait de s’asseoir sur ces ischions. Il faudra être vigilant à repartir équitablement son poids entre ses deux fesses. Vos cuisses, vos genoux, vos chevilles et vos pieds doivent se toucher. Ensuite, il faudra placer vos paumes de main sur le sol, au niveau de vos hanches, et mettre vos doigts vers l’avant. Vous placerez votre menton sur votre sternum et vous devrez ouvrir vos épaules. Par la suite, vous allez devoir redresser votre corps, étirer vos bras à la verticale au-dessus de votre tête, puis inspirer profondément, le tout en ouvrant bien votre cage thoracique.",
        "instructions": "Asseyez-vous sur vos ischions et répartissez équitablement votre poids entre vos deux fesses. Vos cuisses, genoux, chevilles et pieds doivent se toucher. Placez vos paumes de main sur le sol au niveau de vos hanches avec les doigts pointant vers l’avant. Placez votre menton sur votre sternum et ouvrez vos épaules. Redressez votre corps, étirez vos bras à la verticale au-dessus de votre tête et inspirez profondément, en ouvrant bien votre cage thoracique. Maintenez cette position en respirant profondément.",
        "niveau": "intermédiaire"
    },
    {
        "id": 14,
        "nom": "La posture de la tortue – Kurmâsana",
        "image": "https://www.ataraksy.com/wp-content/uploads/2019/03/posture-de-la-tortue-kurmasana-1024x576.jpg",
        "description": "Pour la posture de la tortue, il faudra également s’asseoir sur le sol et replier ses jambes devant soi. Les genoux doivent être ouverts et les plantes de pied être l’une contre l’autre. Au cours de cette posture, vos mains seront amenées à attraper vos chevilles, tout en repoussant le sol avec vos fesses afin de faire basculer votre bassin en avant et d’étirer votre dos. Ensuite, il vous faudra glisser vos poignets sous vos chevilles et descendre vos coudes vers le sol.",
        "instructions": "Asseyez-vous sur le sol et repliez vos jambes devant vous. Ouvrez vos genoux et placez les plantes de pied l’une contre l’autre. Attrapez vos chevilles avec vos mains et repoussez le sol avec vos fesses pour basculer votre bassin en avant et étirer votre dos. Glissez vos poignets sous vos chevilles et descendez vos coudes vers le sol. Maintenez cette position en respirant profondément.",
        "niveau": "avancé"
    },
    {
        "id": 15,
        "nom": "La posture de la grenouille – Mandukâsana",
        "video": "https://youtu.be/ulyud9c7IaY",
        "description": "Pour libérer le chakra de l’enracinement, il faudra se pencher d’un peu plus près sur la posture de la grenouille. Outre le fait d’aider à améliorer la souplesse de certaines parties de notre corps, cette position aidera à avoir une meilleure confiance dans la vie de façon générale. Pour l’atteindre, il faudra s’accroupir tout en veillant à garder le dos droit. Ensuite, il faudra poser les mains sur le sol, tout en décollant ses talons. Il sera également important de garder ses épaules basses et de rentrer son nombril. Dans cette posture, il sera recommandé d’expirer en posant ses talons au sol et en relevant ses fesses.",
        "instructions": "Accroupissez-vous en gardant le dos droit. Posez vos mains sur le sol, décollez vos talons. Gardez vos épaules basses et rentrez votre nombril. Expirez en posant vos talons au sol et en relevant vos fesses. Maintenez cette position en respirant profondément.",
        "niveau": "intermédiaire"
    },
    {
        "id": 16,
        "nom": "La posture du corbeau",
        "video": "https://youtu.be/xWiDxdeI4aM",
        "description": "Lorsque l’on va travailler sur le chakra sacré, c’est-à-dire celui qui se trouve sous le nombril, il faudra mettre à profit la position du corbeau. Pour réaliser la posture du corbeau, commencer en position debout puis écarter les pieds de la largeur de vos épaules. Ensuite, penchez vous en avant en pliant les genoux tout en plaçant vos paumes de mains sur le sol. Puis pliez les coudes pour prendre appui sur le haut des bras sur lesquels vous viendrez caler vos genoux. Maintenant, déplacez le poids du corps sur vos poignets et levez les jambes. Attention à l’équilibre !",
        "instructions": "Commencez en position debout, écartez les pieds à la largeur de vos épaules. Penchez-vous en avant en pliant les genoux et placez vos paumes de mains sur le sol. Pliez les coudes et prenez appui sur le haut des bras avec vos genoux. Déplacez le poids du corps sur vos poignets et levez les jambes. Maintenez votre équilibre.",
        "niveau": "avancé"
    },
    {
        "id": 17,
        "nom": "La posture du chameau – Ustrasana",
        "video": "https://youtu.be/QLch06AdEjM",
        "description": "Afin de libérer les chakras qui se trouvent au niveau de notre gorge et de notre cœur, il sera intéressant de se concentrer sur la posture du chameau. Pour cela, il faut se mettre à genoux, tout en gardant les épaules basses, le nombril rentré et notre périnée serré. Par la suite, on placera nos mains en bas de notre dos préalablement arrondi. Enfin, on viendra placer nos mains sur l’arrière des chevilles.",
        "instructions": "Mettez-vous à genoux, gardez les épaules basses, le nombril rentré et le périnée serré. Placez vos mains en bas de votre dos. Arrondissez votre dos légèrement puis placez vos mains sur l'arrière de vos chevilles. Inclinez votre tête en arrière et ouvrez votre poitrine. Maintenez cette position en respirant profondément.",
        "niveau": "avancé"
    },
    {
        "id": 18,
        "nom": "La posture du cobra – Bhujangasana",
        "video": "https://youtu.be/RGYgiC9319o",
        "description": "Pour faire circuler l’information entre nos différents chakras, il faudra libérer celui que l’on considère comme étant le « chakra de la gorge ». Pour y parvenir, il faudra s’allonger sur le sol et ancré la paume de nos mains dans le sol. Ensuite, il faudra relever notre buste en poussant sur nos bras et répéter ce mouvement jusqu’à sept fois.",
        "instructions": "Allongez-vous sur le sol et ancrez vos paumes dans le sol. Relevez votre buste en poussant sur vos bras. Répétez ce mouvement jusqu'à sept fois pour activer et libérer le chakra de la gorge.",
        "niveau": "débutant"
    },
    {
        "id": 19,
        "nom": "La posture de la montagne tadasana",
        "image": "https://www.ataraksy.com/wp-content/uploads/2019/02/La-posture-de-la-montagne-tadasana.jpg",
        "video": "https://www.youtube.com/embed/ve_cJNhiQVA",
        "description": "Debout, elle vous apprend à être bien stable et à ressentir la terre sous vos pieds. La posture de la montagne peut sembler assez simple et on est tenté de se dire qu’on « simplement debout », mais en fait ce n’est pas aussi simple que cela et les débutants devraient vite s’en rendre compte.",
        "instructions": "Commencez par vous tenir debout, les pieds joints. Enfoncez vos dix orteils dans le sol tout en les écartant. Engagez vos quadriceps pour relever vos genoux. Rentrez et remontez vos abdominaux en soulevant votre poitrine et en rentrant vos épaules. Sentez vos omoplates venir l’une vers l’autre et ouvrez votre poitrine. Faites attention de bien garder vos paumes vers l’intérieur, face à votre corps. Ensuite, imaginez une corde tirant votre tête vers le plafond en inspirant profondément. Tenez la posture pendant 5 à 8 respirations.",
        "niveau": "débutant"
    },
    {
        "id": 20,
        "nom": "Posture du chien tête en bas",
        "image": "https://www.ataraksy.com/wp-content/uploads/2019/02/posture-du-chien-tête-en-bas.jpg",
        "video": "https://www.youtube.com/embed/8C74-mZ0PAY",
        "description": "Cette posture classique de yoga étire tout le corps, en particulier les muscles du dos et les ischio-jambiers, tout en renforçant les bras et les jambes.",
        "instructions": "Commencez à quatre pattes, les mains sous les épaules et les genoux sous les hanches. Expirez et soulevez vos genoux du sol, en redressant vos jambes autant que possible et en poussant vos talons vers le sol. Gardez vos bras tendus et appuyez fermement avec vos paumes. Essayez de former une ligne droite de vos poignets à vos hanches. Respirez profondément et maintenez la position.",
        "niveau": "débutant"
    },
    {
        "id": 21,
        "nom": "Posture de la planche en yoga Kumbhakâsana-dandâsana",
        "image": "https://www.ataraksy.com/wp-content/uploads/2019/02/posture-de-la-planche-en-yoga-Kumbhakâsana-dandâsana.jpg",
        "video": "https://www.youtube.com/embed/iPYg0GCEZWQ",
        "description": "La posture de la planche renforce tout le corps, en particulier les muscles du tronc, des bras et des jambes.",
        "instructions": "Commencez en position de chien tête en bas. Déplacez votre poids vers l'avant, en amenant vos épaules au-dessus de vos poignets et en alignant votre corps en une ligne droite des talons à la tête. Engagez vos muscles abdominaux et maintenez la position en respirant profondément.",
        "niveau": "intermédiaire"
    },
    {
        "id": 22,
        "nom": "La posture du triangle en yoga Trikonâsana",
        "image": "https://www.ataraksy.com/wp-content/uploads/2019/02/la-posture-du-triangle-en-yoga-Trikon%C3%A2sana.jpg",
        "video": "https://www.youtube.com/embed/bKECTBC3-nM",
        "description": "La posture du triangle aide à étirer et renforcer les jambes, les hanches et le torse, tout en améliorant l'équilibre et la stabilité.",
        "instructions": "Mettez-vous en position de la montagne avec les pieds joints. Expirez et écartez les pieds d'environ 1,50 mètre. Rentrez la pointe de votre pied gauche légèrement vers la droite et tournez votre pied droit de 90 degrés vers l'extérieur. Gardez vos hanches de face. Étirez votre torse vers la droite, en glissant votre main droite le long de votre jambe droite. Levez votre bras gauche à la verticale. Maintenez cette position en respirant profondément.",
        "niveau": "intermédiaire"
    },
    {
        "id": 23,
        "nom": "La posture de l’arbre en yoga",
        "image": "https://www.ataraksy.com/wp-content/uploads/2019/02/La-posture-de-l’arbre-en-yoga.jpg",
        "video": "https://www.youtube.com/embed/eSOyjxlDpy8",
        "description": "La posture de l'arbre améliore l'équilibre et la stabilité, tout en renforçant les muscles des jambes.",
        "instructions": "Commencez en position de la montagne. Déplacez votre poids sur votre pied droit et placez la plante de votre pied gauche contre l'intérieur de votre cuisse droite ou votre mollet (évitez le genou). Joignez vos mains en prière devant votre poitrine ou levez-les au-dessus de votre tête. Maintenez votre regard sur un point fixe pour garder l'équilibre. Respirez profondément et maintenez la position.",
        "niveau": "débutant"
    },
    {
        "id": 24,
        "nom": "La posture du guerrier 1 en yoga Virabhadrâsana I",
        "image": "https://www.ataraksy.com/wp-content/uploads/2019/02/La-posture-du-guerrier-1-en-yoga-Virabhadr%C3%A2sana-I.jpg",
        "video": "https://www.youtube.com/embed/TjZVkiLUIOo",
        "description": "Cette posture renforce les jambes et les bras, tout en étirant les hanches et les cuisses. Elle améliore également la concentration et l'équilibre.",
        "instructions": "Commencez en position de la montagne. Faites un grand pas en arrière avec votre pied gauche, en pliant votre genou droit pour former un angle droit. Gardez votre jambe gauche tendue et votre pied gauche tourné légèrement vers l'intérieur. Levez vos bras au-dessus de votre tête, paumes face à face. Regardez vers l'avant ou légèrement vers le haut. Maintenez la position en respirant profondément.",
        "niveau": "intermédiaire"
    },
    {
        "id": 25,
        "nom": "La posture du guerrier 2 Virabhadrâsana II",
        "image": "https://www.ataraksy.com/wp-content/uploads/2019/02/La-posture-du-guerrier-2-Virabhadrâsana-II.jpg",
        "video": "https://www.youtube.com/embed/J2tI2kzdYmg",
        "description": "Cette posture renforce les jambes, ouvre les hanches et la poitrine, et améliore la concentration et l'équilibre.",
        "instructions": "Commencez en position de la montagne. Faites un grand pas en arrière avec votre pied gauche, en pliant votre genou droit pour former un angle droit. Gardez votre jambe gauche tendue et votre pied gauche tourné légèrement vers l'intérieur. Étendez vos bras parallèles au sol, paumes vers le bas. Regardez par-dessus votre main droite. Maintenez la position en respirant profondément.",
        "niveau": "intermédiaire"
    },
    {
        "id": 26,
        "nom": "La posture penchée en avant, assis",
        "image": "https://www.ataraksy.com/wp-content/uploads/2019/02/La-posture-penchée-en-avant-assis.jpg",
        "video": "https://www.youtube.com/embed/fcBLFFbtZ44",
        "description": "Cette posture étire les ischio-jambiers, le dos et les épaules, tout en calmant l'esprit.",
        "instructions": "Asseyez-vous avec les jambes tendues devant vous. Inspirez et allongez votre colonne vertébrale. En expirant, penchez-vous vers l'avant à partir des hanches, en allongeant vos bras vers vos pieds. Attrapez vos pieds, vos chevilles ou vos mollets, selon votre flexibilité. Maintenez cette position en respirant profondément.",
        "niveau": "intermédiaire"
    },
    {
        "id": 27,
        "nom": "La posture du demi pont Ardha-setu-bandhâsana",
        "image": "https://www.ataraksy.com/wp-content/uploads/2019/02/La-posture-du-demi-pont-Ardha-setu-bandhâsana.jpg",
        "video": "https://www.youtube.com/embed/W2hM6cqI6fs",
        "description": "Cette posture renforce les muscles du dos, des fesses et des jambes, tout en ouvrant la poitrine et les épaules.",
        "instructions": "Allongez-vous sur le dos, les genoux pliés et les pieds à plat sur le sol. Placez vos bras le long de votre corps, paumes vers le bas. En inspirant, soulevez vos hanches vers le plafond, en appuyant fermement avec vos pieds et vos bras. Gardez vos cuisses et vos pieds parallèles. Maintenez cette position en respirant profondément.",
        "niveau": "débutant"
    },
    {
        "id": 28,
        "nom": "La posture de l’enfant Bālāsana",
        "image": "https://www.ataraksy.com/wp-content/uploads/2019/02/La-posture-de-l’enfant-Bālāsana.jpg",
        "description": "Cette posture relaxante étire le dos, les hanches et les cuisses, tout en calmant l'esprit.",
        "instructions": "Agenouillez-vous sur le sol, les gros orteils se touchant et les genoux écartés. Asseyez-vous sur vos talons et allongez-vous vers l'avant, en étendant vos bras devant vous ou le long de votre corps. Posez votre front sur le sol et respirez profondément. Maintenez cette position aussi longtemps que vous le souhaitez.",
        "niveau": "débutant"
    }
  ]
}
@app.get('/bienfaits')
def fn_fast_api():

     return {
    "bienfaits": [
    "1 - Amélioration de la flexibilité : Pratiquer le yoga régulièrement aide à étirer les muscles et les articulations, augmentant ainsi la flexibilité et réduisant les risques de blessures.",
    "2 - Renforcement musculaire : Les différentes postures de yoga renforcent les muscles du corps, en particulier ceux du tronc, des bras et des jambes, améliorant la force globale et la stabilité.",
    "3 - Réduction du stress et de l'anxiété : Le yoga inclut des techniques de respiration et de méditation qui aident à calmer l'esprit, réduisant ainsi le stress et l'anxiété.",
    "4 - Amélioration de la qualité du sommeil : Une pratique régulière du yoga peut améliorer la qualité du sommeil, aidant à s'endormir plus facilement et à avoir un sommeil plus réparateur.",
    "5 - Augmentation de la concentration et de la clarté mentale : Les exercices de respiration et de méditation inclus dans le yoga aident à améliorer la concentration, la mémoire et la clarté mentale.",
    "6 - Amélioration de la posture : Les postures de yoga renforcent les muscles du dos et du tronc, aidant à maintenir une bonne posture et à réduire les douleurs liées à une mauvaise position.",
    "7 - Soulagement des douleurs chroniques : Le yoga peut aider à soulager certaines douleurs chroniques, notamment les douleurs lombaires, en renforçant les muscles et en améliorant la flexibilité.",
    "8 - Stimulation du système immunitaire : Les exercices de respiration et la relaxation profonde pratiqués dans le yoga peuvent aider à renforcer le système immunitaire.",
    "9 - Amélioration de la circulation sanguine : Les postures de yoga et les techniques de respiration aident à améliorer la circulation sanguine, ce qui peut bénéficier à la santé cardiovasculaire.",
    "10 - Sens général de bien-être et d'équilibre : En combinant des aspects physiques, mentaux et spirituels, le yoga favorise une sensation générale de bien-être, d'équilibre et de paix intérieure.",
    "En somme, le yoga est une pratique holistique qui peut avoir des effets bénéfiques sur de nombreux aspects de la santé et du bien-être."
  ]
}
# ---------------- FIN DE TON CODE ----------------
#__________________________________________________

if __name__ == '__main__':
    uvicorn.run(app, port=8000, host='0.0.0.0')