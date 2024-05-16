import HomeCard from "../components/HomeCard";
import { Link, useLoaderData } from "react-router-dom";
import "./Home.css";

function Home() {
  // const postureData = [{
  //   "id": 1,
  //   "nom": "La posture de la montagne – Tadasana",
  //   "image": "https://www.ataraksy.com/wp-content/uploads/2019/02/La-posture-de-la-montagne-tadasana.jpg",
  //   "video": "https://www.ataraksy.com/yoga-debutant-10-postures-maitriser/",
  //   "description": "Debout, elle vous apprend à être bien stable et à ressentir la terre sous vos pieds. La posture de la montagne peut sembler assez simple et on est tenté de se dire qu’on « simplement debout », mais en fait ce n’est pas aussi simple que cela et les débutants devraient vite s’en rendre compte.",
  //   "instructions": "Commencez par vous tenir debout, les pieds joints. Enfoncez vos dix orteils dans le sol tout en les écartant. Engagez vos quadriceps pour relever vos genoux. Rentrez et remontez vos abdominaux en soulevant votre poitrine et en rentrant vos épaules. Sentez vos omoplates venir l’une vers l’autre et ouvrez votre poitrine. Faites attention de bien garder vos paumes vers l’intérieur, face à votre corps. Ensuite, imaginez une corde tirant votre tête vers le plafond en inspirant profondément. Tenez la posture pendant 5 à 8 respirations."
  // },
  // {
  //   "id": 2,
  //   "nom": "Posture du chien tête en bas",
  //   "image": "https://www.ataraksy.com/wp-content/uploads/2019/02/posture-du-chien-tête-en-bas.jpg",
  //   "video": "https://www.ataraksy.com/yoga-debutant-10-postures-maitriser/",
  //   "description": "Cette posture étire le dos, les épaules, les ischio-jambiers et les mollets tout en renforçant les bras et les jambes.",
  //   "instructions": "Commencez à quatre pattes, les mains alignées avec les épaules et les genoux avec les hanches. Écartez les doigts et appuyez fermement dans vos paumes. Soulevez vos hanches vers le plafond en redressant vos jambes autant que possible. Gardez votre tête entre vos bras, les oreilles alignées avec vos bras. Maintenez la posture en respirant profondément pendant 5 à 8 respirations."
  // }]
  const postureData = useLoaderData();

  return (
    <>
      <div className="homeCardContainer">
        <ul className="posture-list" id="posture-list">
          {postureData &&
            postureData.map((posture) => (
              <li className="postureCard" key={posture.id}>
                <Link to={`/${posture.id}`}>
                  <HomeCard data={posture} />
                </Link>
              </li>
            ))}
        </ul>
      </div>
    </>
  );
}

export default Home;
