import PropTypes from "prop-types";
import "../components/DailyCard.css";
import MapComponent from "./MapComponents";

function DailyCard({ data }) {
  return (
    <div className="card">
      <div className="card__content"></div>
      <article className="positionCard">
        <h2 className="Title">{data.nom}</h2>
        <img className="positionImg" src={data.image} alt="a yoga position" />
        <div className="paragraphe">
          <h2 className="Title">Description</h2>
          <p className="description">{data.description}</p>
          <h2 className="Title">Instructions</h2>
          <p className="instructions">{data.instructions}</p>
          <h2 className="Title">Spots à proximité</h2>
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
