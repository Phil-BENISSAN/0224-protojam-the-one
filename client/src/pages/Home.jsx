// import { Link, useRouteLoaderData } from "react-router-dom";
import HomeCard from "../components/HomeCard";
import {Link} from "react-router-dom";
import "./Home.css";

const postureExemple = [
  {
    id: 1,
    nom: "Tadasana (Montagne)",
    description:
      "Tadasana, également connue sous le nom de posture de la montagne, est une position de yoga debout qui favorise l'alignement et la stabilité. Elle renforce les jambes, la colonne vertébrale et améliore la posture.",
  },
  {
    id: 2,
    nom: "Adho Mukha Svanasana (Chien tête en bas)",
    description:
      "Adho Mukha Svanasana, ou la posture du chien tête en bas, étire et renforce simultanément plusieurs parties du corps, y compris les bras, les épaules, le dos et les jambes. Elle aide également à soulager le stress et à calmer l'esprit.",
  },
  {
    id: 3,
    nom: "Balasana (Posture de l'enfant)",
    description:
      "Balasana, souvent appelée la posture de l'enfant, est une position de repos qui étire doucement le dos, les hanches et les cuisses. Elle favorise la relaxation et aide à soulager la tension dans le corps et l'esprit.",
  },
  {
    id: 4,
    nom: "Virabhadrasana I (Guerrier I)",
    description:
      "Virabhadrasana I, ou la posture du guerrier I, renforce les jambes, les bras et le tronc tout en améliorant l'équilibre et la concentration. Elle inspire confiance et détermination.",
  },
  {
    id: 5,
    nom: "Utkatasana (Chaise)",
    description:
      "Utkatasana, connue sous le nom de posture de la chaise, renforce les muscles des jambes, des fesses et du dos tout en améliorant l'équilibre et la stabilité. Elle active également le centre du corps et stimule la circulation sanguine.",
  },
  {
    id: 6,
    nom: "Sukhasana (Posture facile)",
    description:
      "Sukhasana, ou la posture facile, est une position assise de méditation qui favorise le calme et la concentration. Elle étire les hanches, le dos et les épaules tout en permettant une respiration profonde et détendue.",
  },
  {
    id: 7,
    nom: "Bhujangasana (Cobra)",
    description:
      "Bhujangasana, ou la posture du cobra, renforce les muscles du dos tout en ouvrant la poitrine et les épaules. Elle stimule également les organes abdominaux et aide à soulager le stress et la fatigue.",
  },
  {
    id: 8,
    nom: "Paschimottanasana (Pince assise)",
    description:
      "Paschimottanasana, également connue sous le nom de pince assise, étire doucement la colonne vertébrale, les ischio-jambiers et les muscles du dos. Elle favorise la relaxation et calme l'esprit.",
  },
  {
    id: 9,
    nom: "Vrikshasana (Arbre)",
    description:
      "Vrikshasana, ou la posture de l'arbre, développe l'équilibre, la concentration et la force des jambes. Elle renforce également les chevilles et les muscles du pied tout en améliorant la posture et la stabilité émotionnelle.",
  },
  {
    id: 10,
    nom: "Savasana (Posture du cadavre)",
    description:
      "Savasana, également appelée la posture du cadavre, est une position de relaxation finale qui permet au corps et à l'esprit de se détendre profondément. Elle favorise la régénération et la clarté mentale.",
  },
];

function Home() {
  // const posturesData = useRouteLoaderData();

  return (
    <>
      <div className="homeCardContainer">
        <ul className="posture-list" id="posture-list">
          {postureExemple.map((posture) => (
            <li className="postureCard" key={posture.id}>
              <Link  to={`/${posture.id}`}>
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
