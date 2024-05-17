import PropTypes from "prop-types";
import { useState } from "react";
import React, { useRef } from 'react';
import "../components/DailyCard.css";
import MapComponent from "./MapComponents";

// import {
//   MapContainer,
//   TileLayer,
//   Marker,Popup
// } from 'https://cdn.esm.sh/react-leaflet'

function DailyCard({ data }) {
  const audioRef = useRef(null);

  const [count, setCount] = useState(0);

  const handleClick = () => {
    setCount(count + 1);
    if (audioRef.current) {
      audioRef.current.play();
    }
  };
  return (
    <div className="card">
      <div className="card__content"></div>
      <article className="positionCard">
        <h2 className="positionTitle">{data.nom}</h2>
        <img className="positionImg" src={data.image} alt="a yoga position" />
        <div className="paragraphe">
          <h2>Description</h2>
          <p className="description">{data.description}</p>
          <h2>Instructions : </h2>
          <p className="instructions">{data.instructions}</p>
          <div className="ButtonContainer">
            <img src="\src\assets\poule_qui_fait_du_yoga.jpg" alt="Poule compteur" className="LogoPoule"></img>
          <p className="NombreDePoule">Nombre de Poule(s):</p> <p className="counterEggForm"> {count}</p>
          <button className="btn" onClick={handleClick}>
          <audio ref={audioRef} src="\src\assets\Minecraft_-_Mob_Chicken_Hurt_1_-_Gaming_Sound_Effect_Minecraft_HD_Sound_Effects.mp3" preload="auto"></audio>
 
  <div className="wrapper">
    <p className="text">Terminé</p>

    <div className="flower flower1">
      <div className="petal one"></div>
      <div className="petal two"></div>
      <div className="petal three"></div>
      <div className="petal four"></div>
    </div>
    <div className="flower flower2">
      <div className="petal one"></div>
      <div className="petal two"></div>
      <div className="petal three"></div>
      <div className="petal four"></div>
    </div>
    <div className="flower flower3">
      <div className="petal one"></div>
      <div className="petal two"></div>
      <div className="petal three"></div>
      <div className="petal four"></div>
    </div>
    <div className="flower flower4">
      <div className="petal one"></div>
      <div className="petal two"></div>
      <div className="petal three"></div>
      <div className="petal four"></div>
    </div>
    <div className="flower flower5">
      <div className="petal one"></div>
      <div className="petal two"></div>
      <div className="petal three"></div>
      <div className="petal four"></div>
    </div>
    <div className="flower flower6">
      <div className="petal one"></div>
      <div className="petal two"></div>
      <div className="petal three"></div>
      <div className="petal four"></div>
    </div>
  </div>
</button>
</div>
          <MapComponent />
        </div>
      </article>
    </div>
  );
}

DailyCard.propTypes = {
  data: PropTypes.shape({
    nom: PropTypes.string.isRequired,
    image: PropTypes.string.isRequired,
    description: PropTypes.string.isRequired,
    instructions: PropTypes.string.isRequired,
  }).isRequired,
};

export default DailyCard;
